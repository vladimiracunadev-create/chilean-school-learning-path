"""Cuaderno del estudiante, 7.º básico Orientación: OA 07 (necesidades compartidas y colaboración) y OA 08 (acuerdos y participación democrática)."""
from __future__ import annotations

from student_content_or7_a import M, T, W, lesson
from student_lessons import arith, ex

OA7, OA8 = "OR07 OA 07", "OR07 OA 08"

# ================================================================ OA 07
lesson(
    OA7, 1,
    "Una hoja y un lápiz. La lista de situaciones del 7.º E, curso inventado, y las definiciones están escritas en los ejercicios.",
    "Aprenderé a reconocer intereses, inquietudes, problemas y necesidades compartidas con mi grupo. Sirve para ver qué temas importan a todo el curso y no solo a unos pocos.",
    ["Sé que los conflictos se resuelven con diálogo.", "Sé que pertenezco a un curso."],
    [
        "Un grupo de pertenencia es el conjunto de personas con las que compartes un espacio, como tu curso, un equipo deportivo o un taller. En un grupo hay cuatro cosas que pueden ser compartidas. Un interés es algo que a varios les gusta o les importa, como organizar un campeonato. Una inquietud es una preocupación, como no saber cómo será la prueba. Un problema es algo que dificulta al grupo, como una sala muy fría. Una necesidad es algo que el grupo requiere para estar bien, como baños con jabón.",
        "Para saber si algo es compartido, pregúntate: ¿afecta o importa a varias personas del grupo? Si solo le importa a una, es un tema personal; puede ser importante, pero no es una necesidad del curso. Detectar lo compartido permite proponer metas comunes, es decir, objetivos que el grupo quiere lograr junto. Por ejemplo, en el 7.º E, ficticio, muchos dicen que la sala está fría, varios quieren un paseo y una estudiante necesita lápices de colores para su proyecto. Los dos primeros son compartidos; el tercero es personal.",
        "Conversar para identificar lo compartido ayuda a que nadie quede fuera y a que las decisiones representen al grupo. Se puede hacer con una lluvia de ideas, una encuesta breve o una conversación guiada. Nadie está obligado a contar cosas privadas: se trabaja con temas del curso.",
    ],
    [("grupo de pertenencia", "grupo al que una persona pertenece, como su curso"), ("interés", "cosa que a varias personas les gusta o les importa"), ("inquietud", "preocupación de una o varias personas"), ("necesidad", "cosa que el grupo requiere para estar bien"), ("meta común", "objetivo que el grupo quiere lograr junto")],
    [
        W("Clasificar", "En el 7.º E dicen: «La sala está fría y casi nadie se concentra». ¿Es un problema compartido o personal?", ["Afecta a muchas personas.", "Dificulta el trabajo del grupo.", "Es un problema compartido."], "Un problema compartido"),
        W("Distinguir lo personal", "Una estudiante dice: «Necesito lápices de colores para mi proyecto». ¿Es una necesidad del curso?", ["Afecta solo a ella.", "Es importante, pero personal.", "No es una necesidad del curso."], "No, es una necesidad personal"),
    ],
    [
        M("Pensar que lo que me importa a mí le importa a todos.", "Se supone sin preguntar.", "Verifica con el grupo si es compartido."),
        M("Creer que un tema personal no merece atención.", "Se confunde no compartido con no importante.", "Es importante, pero se trata de otra manera."),
    ],
    R=[
        ex("Una sala muy fría que afecta a todo el curso, ¿es un problema compartido o personal?", "Compartido", "Afecta a varias personas."),
        ex("Querer organizar un paseo, ¿es un interés o una necesidad básica?", "Un interés", "Es algo que les gusta."),
        ex("No saber cómo será la prueba, ¿es una inquietud o un interés?", "Una inquietud", "Es una preocupación."),
    ],
    U=[
        ex("¿Qué pregunta ayuda a saber si algo es compartido?", "¿Afecta o importa a varias personas del grupo?", "Si afecta a varios, es compartido."),
        ex("En Orientación: ¿Qué es una meta común?", "Un objetivo que el grupo quiere lograr junto", "Se construye con intereses y necesidades compartidas."),
        ex("¿Se puede trabajar lo compartido sin obligar a nadie a contar cosas privadas, sí o no?", "Sí", "Se usan temas del curso."),
    ],
    A=[
        ex("Lista: 1) baños sin jabón; 2) a Camilo le gusta el ajedrez; 3) muchos quieren un campeonato; 4) falta de basureros en la sala. ¿Cuántos son compartidos?", "3", "El 1, el 3 y el 4 afectan o interesan a varios; el 2 es personal."),
        ex("Una encuesta rápida muestra que 20 de 30 quieren un paseo y 3 quieren aprender ajedrez. ¿Cuál es un interés compartido por la mayoría? A) El paseo. B) El ajedrez.", "A", "Lo eligen 20 de 30."),
        ex("Un estudiante dice: «Me preocupa que no entiendo una materia». Otros 12 dicen lo mismo. ¿Pasa a ser una inquietud compartida, sí o no?", "Sí", "Afecta a varias personas."),
    ],
    Z=[
        ex("Rodrigo dice: «Si lo pienso solo yo, no tiene importancia». ¿Qué error hay?", "Puede ser compartido aunque nadie lo haya dicho", "Hay que preguntar al grupo para saberlo."),
        ex("¿Por qué conviene detectar lo compartido antes de proponer una meta común?", "Para que represente al grupo", "Las decisiones deben partir de lo que importa a varios."),
    ],
    D=[
        arith("En un curso de 32 estudiantes, 24 dicen que la sala está fría. ¿Cuántos no lo dicen?", "32-24", "Al total se le restan los que sí lo dicen."),
        ex("Una encuesta muestra que 3 de 30 quieren cambiar el color de las cortinas, y 25 de 30 quieren más tiempo de almuerzo. ¿Qué tema conviene llevar primero al Consejo de Curso?", "El tiempo de almuerzo", "Lo quieren muchas más personas del curso."),
    ],
    context=[ex("En la reunión del curso salen cuatro temas: la basura de la sala, un paseo, la música del recreo y el cuaderno olvidado de un compañero. ¿Cuál es el más claramente personal?", "El cuaderno olvidado de un compañero", "Solo afecta a una persona.")],
    selfcheck=[ex("En Orientación: ¿una necesidad compartida afecta a varias personas?", "Sí", "Por eso se trabaja en grupo."), ex("¿Una meta común nace de lo compartido?", "Sí", "Se construye desde intereses y necesidades."), ex("¿Debo contar cosas privadas para participar?", "No", "Se usan temas del curso.")],
    task=T("Lee las ocho frases inventadas del 7.º E: sala sin ventilación; me falta un plumón; muchos queremos un campeonato de fútbol; muchos tenemos miedo a la prueba de Matemática; faltan basureros; mi lápiz se perdió; hay poco tiempo para almorzar; a Camilo le gusta el ajedrez. Clasifica cada una como interés, inquietud, problema o necesidad, y marca si es compartida o personal.", "Compartidas: sala sin ventilación (problema), campeonato de fútbol (interés), miedo a la prueba (inquietud), faltan basureros (problema), poco tiempo para almorzar (problema). Personales: me falta un plumón, mi lápiz se perdió, el gusto de Camilo por el ajedrez (interés).", ["clasifica cada frase", "marca compartida o personal", "no cuenta nada personal", "justifica al menos una"], ["tabla escrita"], ["tomar todo como compartido", "confundir interés con necesidad"], "Reconoce la tabla y pregunta qué meta común propondría para el curso."),
    reinforce="Escribe cuatro temas de un curso inventado y clasifícalos como compartidos o personales.",
    extend="Explica por qué un interés de pocas personas también puede formar un grupo de trabajo.",
)

lesson(
    OA7, 2,
    "Una hoja y un lápiz. El caso del trabajo de ciencias de los cuatro estudiantes inventados está escrito en los ejercicios.",
    "Aprenderé a valorar el aporte de cada miembro de un equipo y a distinguir hechos, emociones, derechos y límites en el trabajo grupal. Sirve para colaborar sin que nadie cargue con todo ni quede afuera.",
    ["Sé identificar necesidades compartidas.", "Sé que cada persona tiene derecho a ser escuchada."],
    [
        "Un equipo funciona cuando cada miembro aporta. Un aporte es lo que una persona suma al trabajo: ideas, tiempo, habilidades, materiales, ánimo o ayuda. Los aportes no son todos iguales ni tienen que serlo, pero todos valen. Alguien puede aportar el diseño, otro la investigación, otro la organización y otro la presentación. Reconocer los aportes con hechos («Tomás buscó tres fuentes y las resumió») ayuda a que todos se sientan valorados.",
        "En un trabajo grupal pueden aparecer emociones: molestia si alguien no hace su parte, ansiedad por el plazo, o vergüenza si alguien se siente menos capaz. Es importante separar el hecho («Marta no entregó su parte el viernes»), la emoción («me sentí molesto») y la interpretación («es floja»). Hablar de hechos permite arreglar el problema sin ofender.",
        "Cada integrante tiene derechos: a ser escuchado, a participar y a ser tratado con respeto. También tiene deberes: cumplir su parte y avisar si no puede. Y hay límites: nadie debe hacer todo el trabajo ni ser excluido. Si una persona carga con todo, se agota; si otra no participa, se pierde su aporte. Colaborar es repartir con justicia.",
    ],
    [("aporte", "lo que una persona suma al trabajo del equipo"), ("deber", "responsabilidad que una persona debe cumplir"), ("participar", "tomar parte en una actividad"), ("repartir", "dividir las tareas entre los integrantes"), ("valorar", "reconocer que algo tiene importancia")],
    [
        W("Reconocer un aporte", "Tomás, un estudiante inventado, buscó tres fuentes y las resumió para el trabajo de ciencias. ¿Qué aporte hizo?", ["Dedicó tiempo.", "Investigó y resumió.", "Aportó información."], "Investigación e información"),
        W("Separar hecho, emoción e interpretación", "Marta no entregó su parte el viernes; Daniel se siente molesto y dice «es floja». Separa las tres cosas.", ["Hecho: no entregó su parte el viernes.", "Emoción: molestia.", "Interpretación: «es floja»."], "Hecho: no entregó el viernes. Emoción: molestia. Interpretación: «es floja»"),
    ],
    [
        M("Creer que solo vale el aporte más grande.", "Se mide por la cantidad y no por la utilidad.", "Todos los aportes ayudan al equipo."),
        M("Hacer todo el trabajo yo para que salga bien.", "Se piensa que es más rápido y seguro.", "Reparte tareas; si cargas con todo, el equipo pierde aportes."),
    ],
    R=[
        ex("Dibujar los afiches del grupo, ¿es un aporte, sí o no?", "Sí", "Suma al trabajo del equipo."),
        ex("«Marta no entregó su parte el viernes», ¿es un hecho o una interpretación?", "Un hecho", "Se puede comprobar."),
        ex("«Es floja», ¿es un hecho o una interpretación?", "Una interpretación", "Supone cómo es la persona."),
    ],
    U=[
        ex("¿Por qué conviene reconocer los aportes con hechos?", "Porque muestra lo que cada uno hizo", "Valorar con ejemplos ayuda a que todos se sientan vistos."),
        ex("¿Debe una persona hacer todo el trabajo para que salga bien, sí o no?", "No", "Cargar con todo agota y excluye."),
        ex("¿Tiene derecho a participar un integrante que se siente menos capaz, sí o no?", "Sí", "Todos tienen derecho a participar."),
    ],
    A=[
        ex("Aportes: Tomás investigó, Lucía diseñó, Marta no entregó, Daniel presentó. ¿Cuántos integrantes han cumplido su parte?", "3", "Tomás, Lucía y Daniel; Marta no."),
        ex("Daniel dice: A) «Me siento molesto porque tu parte no llegó el viernes y necesito el lunes para unirla». B) «Eres floja y nunca haces nada». ¿Cuál ayuda a arreglar el problema?", "A", "Habla de hechos, emoción y necesidad."),
        ex("Un integrante tímido nunca opina en las reuniones. ¿Qué podría hacer el grupo para respetar su derecho a participar?", "Invitarlo a opinar y darle un rol", "Se garantiza su participación con respeto."),
    ],
    Z=[
        ex("Camila dice: «Prefiero hacerlo yo sola; los demás se demoran». ¿Qué consecuencia tiene para ella y para el equipo?", "Se agota y el equipo pierde aportes", "El trabajo debe repartirse."),
        ex("¿Por qué separar hecho e interpretación ayuda a no ofender?", "Porque el hecho se puede conversar sin acusar", "La interpretación suele ser injusta."),
    ],
    D=[
        arith("Un trabajo tiene 12 tareas y 4 integrantes. Si las reparten en partes iguales, ¿cuántas tareas hace cada uno?", "12//4", "Se divide el total entre los integrantes."),
        arith("Si cada integrante dedica 3 horas, ¿cuántas horas suma el equipo de 4?", "3*4", "Se multiplican horas por integrantes."),
    ],
    context=[ex("En un trabajo de cuatro personas, una no ha entregado su parte y las otras tres están molestas. Antes de acusarla, ¿qué conviene hacer?", "Preguntarle qué pasó y escucharla", "Puede haber una razón y conviene escuchar antes de juzgar.")],
    selfcheck=[ex("En Orientación: ¿todos los aportes valen en un equipo?", "Sí", "Cada uno suma al trabajo."), ex("¿Una persona debe cargar con todo el trabajo?", "No", "Hay que repartir."), ex("¿Una interpretación es un hecho?", "No", "Es una suposición.")],
    task=T("Lee el caso inventado del equipo de Historia: Bruno investigó, Paz hizo el cartel, Esteban no ha hecho su parte, Antonia presentó. Escribe un aporte reconocido con un hecho para tres integrantes y un mensaje respetuoso a Esteban que diga el hecho, tu emoción y lo que necesitas.", "Aportes: Bruno investigó, Paz hizo el cartel, Antonia presentó. Mensaje: «Esteban, tu parte no llegó el viernes; me siento preocupado porque necesito unirla antes del lunes».", ["reconoce tres aportes con hechos", "escribe un mensaje con hecho, emoción y necesidad", "no acusa", "no cuenta nada personal"], ["texto escrito"], ["acusar a Esteban", "no usar hechos"], "Reconoce el mensaje y pregunta qué ofrecería para ayudar a Esteban."),
    reinforce="Escribe tres aportes distintos para un trabajo de equipo inventado.",
    extend="Explica por qué repartir con justicia es mejor que cargar con todo el trabajo.",
)

lesson(
    OA7, 3,
    "Una hoja y un lápiz. El caso de la campaña de limpieza del 7.º F, curso inventado, y las tres formas de organizarse están escritos en los ejercicios.",
    "Aprenderé a comparar formas de organizar el trabajo para alcanzar una meta común y a anticipar sus consecuencias. Sirve para elegir una manera de colaborar que cumpla la meta y cuide al equipo.",
    ["Sé reconocer los aportes de cada integrante.", "Sé que repartir con justicia es colaborar."],
    [
        "Para alcanzar una meta común se necesita organizarse. Hay varias formas de repartir el trabajo. Una persona hace todo: es rápido al comienzo, pero agota a esa persona y deja a los demás sin participar. Cada uno hace lo que quiere sin acuerdo: puede quedar trabajo repetido o sin hacer. Repartir por habilidades e intereses: cada uno hace lo que mejor sabe, y todos participan. Turnarse en tareas pesadas o aburridas: se reparte la carga de manera justa.",
        "Para decidir, conviene comparar. Pregunta: ¿cumple la meta a tiempo? ¿participan todos? ¿es justo con el esfuerzo? Y anticipa consecuencias. Si una sola persona hace todo, puede cumplirse el plazo pero se pierde el trabajo en equipo y esa persona se cansa. Si hay buen reparto con plazos claros, hay más posibilidades de cumplir y de que todos aprendan.",
        "Un buen plan colaborativo incluye: la meta, las tareas, quién hace cada una, el plazo y cómo se revisará el avance. Por ejemplo, para una campaña de limpieza de la sala: comprar bolsas, preparar carteles, limpiar, recoger lo juntado. Cada tarea tiene responsable y fecha. Revisar a mitad de camino permite corregir a tiempo.",
    ],
    [("organizarse", "ponerse de acuerdo sobre cómo hacer el trabajo"), ("plazo", "fecha límite para terminar algo"), ("responsable", "persona a cargo de una tarea"), ("avance", "parte del trabajo ya realizada"), ("turno", "oportunidad de hacer algo por orden")],
    [
        W("Comparar dos formas", "Para la campaña de limpieza, A) una persona hace todo; B) se reparten tareas según habilidades. ¿Cuál asegura que todos participen?", ["En A solo participa una persona.", "En B cada uno tiene una tarea.", "B asegura participación."], "B: repartir por habilidades"),
        W("Armar el plan", "El 7.º F debe reunir 30 bolsas de basura. Si hay 6 responsables y reparten en partes iguales, ¿cuántas bolsas junta cada uno?", ["Se divide 30 entre 6.", "30 ÷ 6 = 5.", "Cada uno junta 5."], "5 bolsas"),
    ],
    [
        M("Pensar que es más rápido que lo haga todo una sola persona.", "Se ignora el cansancio y la participación.", "Repartir permite que todos aprendan y se cumpla a tiempo."),
        M("Creer que si no hay plazos, el trabajo igual se hará.", "Se confía en que saldrá solo.", "Define quién y para cuándo."),
    ],
    R=[
        ex("Cuando una sola persona hace todo, ¿participan todos?", "No", "Los demás quedan sin participar."),
        ex("Un plan colaborativo, ¿incluye responsables y plazos, sí o no?", "Sí", "Así se sabe quién y cuándo."),
        ex("Turnarse en las tareas pesadas, ¿es una forma justa de repartir, sí o no?", "Sí", "La carga se comparte."),
    ],
    U=[
        ex("¿Por qué repartir por habilidades e intereses ayuda al equipo?", "Porque cada uno hace lo que mejor sabe", "Mejora la calidad y la motivación."),
        ex("¿Qué se logra revisando el avance a mitad de camino?", "Corregir a tiempo", "Permite ajustar antes de que sea tarde."),
        ex("¿Qué consecuencia tiene que cada uno haga lo que quiera sin acuerdo?", "Puede haber trabajo repetido o sin hacer", "No hay coordinación."),
    ],
    A=[
        ex("Tareas de la campaña: comprar bolsas, hacer carteles, limpiar y recoger. Hay 4 integrantes: Ana ama dibujar y Luis prefiere comprar cosas. ¿Qué tareas conviene asignarles según su interés?", "A Ana los carteles y a Luis comprar bolsas", "Repartir por habilidades e intereses motiva y mejora el trabajo."),
        ex("El curso decide juntar 48 botellas para reciclar entre 8 personas en partes iguales. ¿Cuántas botellas debe juntar cada una? A) 6. B) 8.", "A", "48 dividido entre 8 es 6."),
        ex("Un plan dice «hacer la campaña pronto». ¿Qué le falta para ser colaborativo?", "Responsables, tareas y plazos", "Sin ellos no se sabe quién hace qué ni cuándo."),
    ],
    Z=[
        ex("Pía dice: «Si repartimos, se pierde tiempo hablando». ¿Qué responderías?", "Que repartir evita trabajo repetido y agotamiento", "El tiempo de acordar se recupera."),
        ex("¿Por qué conviene que las tareas pesadas se roten?", "Porque comparte la carga con justicia", "Nadie debe cargar siempre con lo más difícil."),
    ],
    D=[
        arith("El curso debe juntar 120 botellas en 5 días iguales. ¿Cuántas botellas debe juntar por día?", "120//5", "Se divide el total entre los días."),
        arith("Si 4 personas juntan 6 botellas cada día durante 5 días, ¿cuántas botellas juntan en total?", "4*6*5", "Se multiplican personas, botellas y días."),
    ],
    context=[ex("El curso quiere pintar un mural y solo dos personas aceptan trabajar. Las demás dicen que no saben dibujar. ¿Cómo podrían participar todos?", "Asignando tareas como preparar pintura, limpiar y organizar", "Hay tareas para todos, no solo dibujar.")],
    selfcheck=[ex("En Orientación: ¿un plan colaborativo tiene responsables y plazos?", "Sí", "Así se organiza el trabajo."), ex("¿Repartir con justicia ayuda al equipo?", "Sí", "Así todos participan y nadie se agota."), ex("¿Revisar el avance sirve para corregir?", "Sí", "Se ajusta a tiempo.")],
    task=T("Lee el caso inventado del 7.º F: quieren hacer una campaña para reducir la basura de la sala en 2 semanas. Hay 6 estudiantes. Arma un plan con la meta, cuatro tareas, un responsable por tarea, un plazo y cómo revisarán el avance.", "Meta: sala con menos basura en 2 semanas. Tareas: carteles (Ana), basureros (Luis), revisar al final del recreo (Pía), contar bolsas (Mateo). Plazo: 2 semanas. Revisión: reunión el viernes de la primera semana.", ["incluye la meta", "incluye tareas con responsable", "incluye un plazo", "incluye una revisión"], ["plan escrito"], ["tareas sin responsable", "no revisar"], "Reconoce el plan y pregunta qué pasaría si alguien no cumple."),
    reinforce="Escribe un plan de cuatro tareas con responsables para una actividad inventada.",
    extend="Explica por qué revisar el avance a mitad de camino ayuda al equipo.",
)

lesson(
    OA7, 4,
    "Una hoja y un lápiz. El caso de la rifa del 7.º G y las reglas de seguridad para grupos en línea están escritos en los ejercicios.",
    "Aprenderé a colaborar de forma segura: sin presión, cuidando el dinero y los datos, y respetando los límites de cada persona. Sirve para que el trabajo en equipo sea justo y protegido.",
    ["Sé comparar formas de organizar el trabajo.", "Sé que debo proteger mis datos en línea."],
    [
        "Colaborar de forma segura significa cuidar a las personas mientras se logra la meta. Primero, nadie debe sentirse presionado. Si una persona dice que no puede, se respeta y se busca otra tarea. Segundo, el dinero se maneja con transparencia: si el curso reúne dinero para una actividad, debe haber un registro de lo que entra y sale, y más de una persona debe revisar. Un adulto del colegio debe saber y autorizar.",
        "Tercero, en grupos de mensajería o trabajos en línea, no se comparten datos personales como direcciones o teléfonos de otros sin permiso, ni se publican fotos del grupo sin acuerdo. Se usan solo las plataformas que indique el colegio para trabajar y se respeta un horario razonable, sin mensajes de madrugada ni presión por responder.",
        "Cuarto, las salidas o actividades fuera del colegio deben ser informadas a las familias y tener un adulto responsable. Y quinto, nadie debe obligar a otros a hacer algo peligroso o incómodo «por el grupo». Un buen equipo cuida a sus integrantes. Si algo parece riesgoso, se avisa al profesor jefe.",
    ],
    [("transparencia", "mostrar con claridad lo que se hace con algo, como el dinero"), ("registro", "anotación de lo que entra y sale"), ("autorizar", "dar permiso formal"), ("presión", "insistir para que alguien acepte algo que no quiere"), ("plataforma", "aplicación o sitio donde se trabaja")],
    [
        W("Manejar dinero con transparencia", "El 7.º G reúne $15.000 con una rifa. ¿Qué debe hacer el curso para manejarlo con transparencia?", ["Anotar lo que entra y lo que sale.", "Que más de una persona lo revise.", "Que un adulto del colegio esté informado."], "Llevar un registro, que lo revisen varias personas y que un adulto sepa"),
        W("Respetar un límite", "Tomás no puede quedarse después de clases a ensayar. ¿Qué hace el grupo?", ["Nadie debe presionarlo.", "Se busca otra tarea o un horario.", "Así sigue participando."], "Ofrecerle otra tarea o buscar otro horario"),
    ],
    [
        M("Pensar que, por ser del curso, el dinero no necesita registro.", "Se confía en que todo saldrá bien sin anotar.", "Un registro cuida a todos."),
        M("Creer que «por el grupo» justifica presionar a alguien.", "Se pone la meta antes que las personas.", "Nadie debe ser presionado."),
    ],
    R=[
        ex("¿Debe llevarse un registro del dinero del curso, sí o no?", "Sí", "Un registro da transparencia al manejo del dinero."),
        ex("¿Se puede presionar a alguien «por el grupo», sí o no?", "No", "Nadie debe ser presionado."),
        ex("¿Se deben compartir teléfonos de otros sin permiso, sí o no?", "No", "Son datos personales."),
    ],
    U=[
        ex("¿Por qué conviene que un adulto del colegio sepa de una actividad con dinero?", "Porque ayuda a cuidar y autorizar", "Un adulto responsable protege al grupo."),
        ex("¿Por qué no se deben mandar mensajes de madrugada para el trabajo en grupo?", "Porque presionan y afectan el descanso", "Se debe respetar un horario razonable."),
        ex("¿Por qué las salidas deben informarse a las familias?", "Para que sepan dónde y con quién están", "Es una medida de seguridad."),
    ],
    A=[
        ex("Reglas: 1) registrar el dinero; 2) compartir el teléfono de todos sin avisar; 3) informar a las familias de la salida; 4) presionar a quien no quiere. ¿Cuántas son seguras?", "2", "La 1 y la 3 protegen; la 2 y la 4 no."),
        ex("Un grupo quiere subir una foto de todos al estado de la aplicación. Camila no quiere salir. A) Se respeta y no se sube su foto. B) Se sube igual porque es del grupo.", "A", "Cada persona decide sobre su imagen."),
        ex("Para una salida, un grupo propone que cada uno lleve $2.000 y los entregue en un sobre al tesorero, que anota cada pago. ¿Qué medida de transparencia usan?", "El registro de cada pago", "Anotar cada pago permite revisar después."),
    ],
    Z=[
        ex("Gaspar dice: «Si yo guardo todo el dinero, es más fácil». ¿Qué riesgo hay?", "Que no haya transparencia ni revisión", "Una sola persona sin control puede generar dudas."),
        ex("¿Por qué un buen equipo cuida a sus integrantes además de cumplir la meta?", "Porque las personas son lo más importante", "Una meta lograda sin cuidar a otros no es un buen trabajo en equipo."),
    ],
    D=[
        arith("El curso reunió $24.000 y gastó $9.000 en materiales y $6.000 en pasajes. ¿Cuánto dinero queda?", "24000-9000-6000", "Al total se le restan ambos gastos."),
        arith("Si cada uno de los 30 estudiantes aporta $500, ¿cuánto dinero reúne el curso?", "30*500", "Se multiplica el aporte por los estudiantes."),
    ],
    context=[ex("En el grupo del curso, alguien propone pedir a todos fotos personales para un collage. Varios no quieren. ¿Qué corresponde?", "Respetar a quienes no quieren y usar dibujos u otras imágenes", "Cada uno decide sobre su imagen.")],
    selfcheck=[ex("En Orientación: ¿colaborar incluye cuidar a las personas?", "Sí", "No solo cumplir la meta."), ex("¿Se registra el dinero del curso?", "Sí", "Así se sabe qué entra y qué sale."), ex("¿Puedo negarme a que suban mi foto?", "Sí", "Es mi imagen.")],
    task=T("Lee el caso inventado del 7.º G: quieren hacer una completada para juntar dinero; algunos proponen que una sola persona maneje el dinero y que todos suban fotos del evento. Escribe tres reglas de seguridad y transparencia para que el curso colabore de forma segura.", "Reglas: registrar el dinero con dos personas que lo revisen; avisar al profesor jefe y a las familias; pedir permiso antes de subir fotos.", ["escribe tres reglas", "incluye transparencia del dinero", "incluye cuidado de datos o imagen", "no cuenta nada personal"], ["lista escrita"], ["una sola persona maneja todo", "no pedir permiso"], "Reconoce las reglas y pregunta cuál sería más difícil de cumplir."),
    reinforce="Escribe dos reglas de seguridad para un grupo de mensajes del curso.",
    extend="Explica por qué el registro del dinero protege también a quien lo maneja.",
)

lesson(
    OA7, 5,
    "Una hoja y un lápiz. El caso del equipo de ciencias del 7.º H y las frases de ejemplo están escritos en los ejercicios.",
    "Aprenderé a expresar las necesidades del grupo, a pedir ayuda cuando el equipo se trabe y a dar retroalimentación respetuosa. Sirve para resolver problemas del trabajo en equipo antes de que crezcan.",
    ["Sé organizarme en equipo.", "Sé hablar con mensajes yo."],
    [
        "Cuando un equipo se traba, hay que comunicarlo con claridad. Una buena forma es describir el problema con hechos, decir cómo afecta al equipo y proponer una solución. Por ejemplo: «Hace dos semanas no tenemos fecha para ensayar. Esto nos atrasa. Propongo que decidamos hoy un horario». Si el problema es una persona que no colabora, se habla primero con ella, con respeto, y se escucha su versión.",
        "A veces el equipo no puede resolverlo solo. Entonces puede pedir ayuda al profesor jefe, al profesor de la asignatura o a orientación. Para pedirla conviene llevar: la meta del trabajo, qué ha pasado, qué intentaron y qué necesitan. Pedir ayuda no es acusar: es cuidar el trabajo y a las personas. También se puede pedir recursos, como un espacio para reunirse o materiales.",
        "Dar retroalimentación respetuosa es decir lo que está bien y lo que se puede mejorar. Se usa la fórmula «lo que me gustó, lo que podría mejorar, una idea». «Me gustó tu esquema claro. Podría mejorar la parte de las fuentes. Una idea es agregar dos más». Así el equipo mejora sin que nadie se sienta atacado.",
    ],
    [("retroalimentación", "dato que se da a otra persona sobre lo que hizo para mejorar"), ("proponer", "ofrecer una idea para resolver algo"), ("recursos", "cosas que el equipo necesita, como materiales o un espacio"), ("versión", "forma en que una persona cuenta lo ocurrido"), ("trabarse", "no poder avanzar")],
    [
        W("Describir un problema", "El equipo de ciencias lleva dos semanas sin fecha para ensayar. ¿Cómo se plantea con hechos, efecto y propuesta?", ["Hecho: dos semanas sin fecha.", "Efecto: se atrasan.", "Propuesta: decidir un horario hoy."], "«Llevamos dos semanas sin fecha; nos atrasamos; decidamos un horario hoy»"),
        W("Dar retroalimentación", "Lucía presentó un esquema claro, pero falta una fuente. ¿Cómo se lo dices con la fórmula?", ["Lo que me gustó: el esquema claro.", "Lo que podría mejorar: la fuente.", "Una idea: buscar una más."], "«Me gustó tu esquema claro; podría mejorar la fuente; una idea es buscar otra»"),
    ],
    [
        M("Pensar que hablar del problema del equipo es acusar.", "Se confunde describir con culpar.", "Habla de hechos y propón una solución."),
        M("Esperar a que el problema crezca antes de pedir ayuda.", "Se cree que se resolverá solo.", "Pide ayuda a tiempo."),
    ],
    R=[
        ex("Describir el problema con hechos, ¿es acusar, sí o no?", "No", "Es hablar de lo ocurrido sin culpar."),
        ex("¿Se puede pedir ayuda al profesor jefe cuando el equipo se traba, sí o no?", "Sí", "Es una persona que puede orientar."),
        ex("La retroalimentación respetuosa, ¿dice solo lo malo o también lo bueno?", "También lo bueno", "Reconoce lo que está bien y lo que se puede mejorar."),
    ],
    U=[
        ex("¿Por qué conviene hablar primero con la persona que no colabora?", "Para escuchar su versión", "Puede haber razones que no conocemos."),
        ex("¿Qué debe llevar el equipo al pedir ayuda a un adulto?", "La meta, lo ocurrido, lo intentado y lo que necesitan", "Eso permite entender y ayudar."),
        ex("¿Qué es un recurso del equipo: un espacio de reunión o una opinión?", "Un espacio de reunión", "Es algo que el equipo necesita."),
    ],
    A=[
        ex("Frases: 1) «Eres un desastre»; 2) «Me gustó tu idea; podría mejorar la presentación; una idea es ensayar»; 3) «Tu parte no llegó; me preocupa el plazo»; 4) «No sirves para esto». ¿Cuántas son respetuosas?", "2", "La 2 y la 3 describen y proponen."),
        ex("El equipo ya habló con Mario, pero sigue sin entregar. A) Pedir ayuda al profesor jefe con la meta, lo ocurrido y lo intentado. B) Acusarlo en el chat del curso.", "A", "Pedir ayuda con claridad resuelve sin humillar."),
        ex("Un equipo necesita un lugar para reunirse y no lo tiene. ¿Qué puede hacer?", "Pedir un espacio al profesor jefe o a orientación", "Los recursos se piden a quienes pueden proporcionarlos."),
    ],
    Z=[
        ex("Ignacio dice: «Si le doy retroalimentación, se va a ofender». ¿Cómo evita eso?", "Usando lo que me gustó, lo que podría mejorar y una idea", "La fórmula respeta a la persona."),
        ex("¿Por qué conviene pedir ayuda a tiempo y no cuando ya hay conflicto grande?", "Porque es más fácil resolverlo temprano", "Los problemas pequeños se arreglan más rápido."),
    ],
    D=[
        ex("Un integrante dice: «Tu presentación estuvo mal». ¿Qué le falta a esa retroalimentación para servir?", "Lo que estuvo bien y una idea para mejorar", "Una crítica sin ejemplos ni ideas no ayuda a mejorar."),
        arith("De 24 trabajos revisados, 18 recibieron retroalimentación respetuosa. ¿Cuántos no la recibieron?", "24-18", "Al total se le restan los que sí la recibieron."),
    ],
    context=[ex("En un trabajo en línea, un integrante no responde los mensajes hace una semana. ¿Cuál es un primer paso respetuoso?", "Escribirle con calma, describir el hecho y preguntar si necesita ayuda", "Se aborda con respeto y se escucha su versión.")],
    selfcheck=[ex("En Orientación: ¿puedo pedir ayuda a un adulto cuando el equipo se traba?", "Sí", "Es cuidar el trabajo."), ex("¿La retroalimentación respetuosa incluye lo bueno?", "Sí", "Reconoce lo que está bien."), ex("¿Hablar con hechos es acusar?", "No", "Es describir lo ocurrido sin culpar.")],
    task=T("Lee el caso inventado del 7.º H: un integrante, Felipe, no ha entregado su parte y el plazo es en tres días. Escribe: un mensaje a Felipe con hecho, efecto y propuesta; una retroalimentación para otra integrante con «lo que me gustó, lo que podría mejorar, una idea»; y qué llevarías si debes pedir ayuda a la profesora jefe.", "Mensaje: «Tu parte no llegó; el plazo es en tres días; propongo que la entregues mañana o que te ayudemos». Retroalimentación: «Me gustó el esquema; podría mejorar las fuentes; una idea es agregar dos». Ayuda: la meta, lo ocurrido, lo intentado y lo que necesitan.", ["escribe el mensaje con hecho, efecto y propuesta", "escribe la retroalimentación con tres partes", "dice qué llevaría al pedir ayuda", "no cuenta nada personal"], ["texto escrito"], ["acusar", "olvidar la propuesta"], "Reconoce los textos y pregunta qué cambiaría si Felipe tuviera una razón personal."),
    reinforce="Escribe una retroalimentación con las tres partes para un trabajo inventado.",
    extend="Explica por qué escuchar la versión del compañero cambia cómo se resuelve un problema de equipo.",
)

# ================================================================ OA 08
lesson(
    OA8, 1,
    "Una hoja y un lápiz. El caso del paseo de fin de año del 7.º A, curso inventado, y las descripciones de cada espacio están escritos en los ejercicios.",
    "Aprenderé qué espacios de participación existen en el curso y el colegio y para qué sirve cada uno. Sirve para elegir el lugar adecuado cuando quiero proponer algo o tomar una decisión con mis compañeros.",
    ["Sé identificar necesidades compartidas.", "Sé que mi opinión es válida."],
    [
        "La participación es tomar parte en las decisiones y actividades que afectan al grupo. En el colegio existen espacios organizados para participar. El Consejo de Curso es la reunión del curso, generalmente con el profesor jefe, donde se conversa y se toman acuerdos sobre temas del curso. La directiva del curso es el grupo de estudiantes elegidos como representantes, por ejemplo presidente, secretario y tesorero. La asamblea es una reunión amplia en que muchas personas opinan. También hay encuentros y comisiones para tareas específicas.",
        "Cada espacio sirve para algo distinto. Para decidir algo del curso, como un paseo, se usa el Consejo de Curso. Para una tarea puntual, como preparar el acto, se forma una comisión. Para llevar una propuesta a la dirección del colegio, se encarga a la directiva. Y todos tienen derecho a participar, sean hombres o mujeres, y a ser escuchados con respeto.",
        "Participar también implica deberes: asistir, escuchar, respetar turnos y cumplir los acuerdos. Los acuerdos del curso deben registrarse, por ejemplo en un acta, es decir, un documento que anota lo conversado y lo decidido.",
    ],
    [("participación", "tomar parte en las decisiones que afectan al grupo"), ("Consejo de Curso", "reunión del curso para conversar y tomar acuerdos"), ("directiva", "grupo de estudiantes elegidos para representar al curso"), ("acta", "documento que anota lo conversado y decidido"), ("comisión", "grupo pequeño encargado de una tarea")],
    [
        W("Elegir el espacio", "El 7.º A debe decidir adónde irá en el paseo de fin de año. ¿Qué espacio usa?", ["Es un tema del curso.", "El Consejo de Curso es el espacio para decidir temas del curso.", "Debe usarse ese espacio."], "El Consejo de Curso"),
        W("Distinguir roles", "El curso quiere llevar una propuesta a la dirección. ¿Quién la presenta?", ["La directiva representa al curso.", "Ellos fueron elegidos.", "La presenta la directiva."], "La directiva del curso"),
    ],
    [
        M("Pensar que participar es solo hablar en el Consejo de Curso.", "Se reduce a un espacio.", "También se participa en comisiones, asambleas y encuentros."),
        M("Creer que los acuerdos no necesitan registro.", "Se confía en que todos recordarán.", "El acta ayuda a recordar y cumplir."),
    ],
    R=[
        ex("¿El Consejo de Curso es una reunión del curso, sí o no?", "Sí", "Es el espacio para conversar y tomar acuerdos."),
        ex("La directiva del curso, ¿la forman estudiantes elegidos o profesores?", "Estudiantes elegidos", "Son representantes del curso."),
        ex("Un acta, ¿anota lo conversado y decidido, sí o no?", "Sí", "Sirve de registro."),
    ],
    U=[
        ex("¿Por qué conviene usar una comisión para una tarea puntual?", "Porque un grupo pequeño se encarga de ella", "Organiza mejor el trabajo."),
        ex("¿Pueden participar hombres y mujeres por igual, sí o no?", "Sí", "Ambos tienen los mismos derechos."),
        ex("¿Qué deberes tiene quien participa?", "Asistir, escuchar, respetar turnos y cumplir acuerdos", "Son las responsabilidades de participar."),
    ],
    A=[
        ex("Espacios: 1) Consejo de Curso; 2) directiva; 3) comisión; 4) asamblea. ¿Cuál se encarga de una tarea puntual como preparar el acto?", "3", "La comisión es para tareas específicas."),
        ex("El curso quiere cambiar la hora del recreo. A) Lo conversan en el Consejo de Curso y luego la directiva lo lleva a la dirección. B) Lo deciden entre dos amigos.", "A", "Es un tema del curso y se lleva por los canales."),
        ex("El 7.º A decidió el paseo, pero no anotó el acuerdo. ¿Qué problema puede aparecer?", "Que después no recuerden lo que acordaron", "El acta ayuda a recordar y cumplir."),
    ],
    Z=[
        ex("Dana dice: «Mi opinión no importa porque soy nueva». ¿Qué respondes?", "Que todos tienen derecho a participar", "Participar es un derecho de todos los miembros del curso."),
        ex("¿Por qué existen distintos espacios de participación y no uno solo?", "Porque cada uno sirve para algo distinto", "Se elige según el tema."),
    ],
    D=[
        arith("En una asamblea de 36 estudiantes, 28 asisten. ¿Cuántos faltan?", "36-28", "Se restan los asistentes del total."),
        ex("Un curso quiere decidir si cambia la hora de una actividad y dos amigos lo resuelven por mensaje sin avisar a los demás. ¿Es participación democrática?", "No", "No participó todo el curso en un espacio común."),
    ],
    context=[ex("El profesor jefe propone que el curso decida cómo gastar el dinero reunido. ¿Dónde conviene hacerlo?", "En el Consejo de Curso", "Es el espacio para decidir temas del curso.")],
    selfcheck=[ex("En Orientación: ¿el Consejo de Curso sirve para tomar acuerdos?", "Sí", "Es su finalidad."), ex("¿Hombres y mujeres tienen los mismos derechos a participar?", "Sí", "Es un principio de igualdad."), ex("¿El acta registra lo decidido?", "Sí", "Ayuda a cumplir.")],
    task=T("Lee el caso inventado del 7.º B: quieren tres cosas. (1) Decidir el destino del paseo; (2) preparar el acto del Día del Libro; (3) pedir a la dirección que se arregle el patio. Para cada una indica el espacio de participación más adecuado (Consejo de Curso, comisión o directiva) y por qué.", "(1) Consejo de Curso: es una decisión del curso. (2) Comisión: es una tarea puntual. (3) Directiva: representa al curso ante la dirección.", ["asigna un espacio a cada caso", "justifica", "no cuenta nada personal", "usa los términos aprendidos"], ["tabla escrita"], ["confundir comisión con directiva", "no justificar"], "Reconoce la tabla y pregunta quién registraría el acuerdo."),
    reinforce="Escribe para qué sirve cada espacio: Consejo de Curso, directiva y comisión.",
    extend="Explica por qué todos los miembros del curso tienen derecho a participar por igual.",
)

lesson(
    OA8, 2,
    "Una hoja y un lápiz. El debate del 7.º C sobre la hora de estudio, curso inventado, está escrito en los ejercicios.",
    "Aprenderé a debatir con respeto, a distinguir hechos de opiniones y a valorar la diversidad de opiniones y el derecho de hombres y mujeres a participar. Sirve para que los acuerdos del curso sean justos.",
    ["Sé que existen espacios de participación.", "Sé distinguir un hecho de una opinión."],
    [
        "Un debate es una conversación ordenada en que las personas defienden sus ideas con argumentos. Un argumento es una razón que apoya una opinión: «Propongo estudiar a la primera hora porque estamos más descansados». Para que el debate sea respetuoso hay reglas: pedir la palabra, respetar turnos, escuchar sin interrumpir, no insultar y atacar las ideas, no a las personas.",
        "Es importante distinguir hechos de opiniones. Un hecho se puede comprobar: «La prueba es el jueves». Una opinión es lo que alguien piensa: «La prueba va a ser difícil». En un debate se usan hechos para apoyar opiniones. También se acepta que hay diferentes opiniones: no todos tienen que pensar igual, y la diversidad enriquece la conversación.",
        "Hombres y mujeres tienen el mismo derecho a opinar, a ser escuchados y a ser elegidos como representantes. Una opinión no vale más ni menos por quien la dice. Si alguien interrumpe a una compañera o ignora lo que dice por ser mujer, o hace lo mismo con un compañero por ser hombre, se vulnera el derecho a participar. El moderador puede recordar las reglas.",
    ],
    [("debate", "conversación ordenada en que se defienden ideas con argumentos"), ("argumento", "razón que apoya una opinión"), ("moderador", "persona que ordena los turnos"), ("diversidad", "variedad de opiniones y personas"), ("interrumpir", "cortar a alguien mientras habla")],
    [
        W("Reconocer un argumento", "En el 7.º C, Camila dice: «Estudiemos a primera hora porque estamos más descansados». ¿Cuál es la razón?", ["La opinión es estudiar a primera hora.", "La razón viene después de «porque».", "Es «estamos más descansados»."], "«Estamos más descansados»"),
        W("Distinguir hecho y opinión", "Frase: «La prueba es el jueves y va a ser difícil». ¿Qué parte es hecho y cuál opinión?", ["La fecha se puede comprobar.", "La dificultad es una percepción.", "Hecho: es el jueves. Opinión: va a ser difícil."], "Hecho: la prueba es el jueves. Opinión: va a ser difícil"),
    ],
    [
        M("Pensar que debatir es ganar y hacer callar al otro.", "Se confunde debatir con pelear.", "Debatir es intercambiar razones y escuchar."),
        M("Creer que una opinión vale más según quién la dice.", "Se da más valor a la persona que a la razón.", "Todas las personas tienen el mismo derecho a opinar."),
    ],
    R=[
        ex("«La prueba es el jueves», ¿es un hecho o una opinión?", "Un hecho", "Se puede comprobar."),
        ex("«Va a ser difícil», ¿es un hecho o una opinión?", "Una opinión", "Es lo que alguien piensa."),
        ex("En un debate respetuoso, ¿se ataca a las ideas o a las personas?", "A las ideas", "No se insulta."),
    ],
    U=[
        ex("¿Por qué un argumento mejora una opinión?", "Porque da una razón", "Permite entender por qué se piensa así."),
        ex("¿Qué hace un moderador?", "Ordena los turnos", "Ayuda a que todos puedan hablar."),
        ex("¿Una opinión vale más si la dice un hombre, sí o no?", "No", "Hombres y mujeres tienen el mismo derecho a opinar."),
    ],
    A=[
        ex("Frases: 1) «Propongo hacer el paseo en mayo porque hay buen clima»; 2) «Tu idea es tonta»; 3) «Escuchemos a Dani antes de decidir»; 4) «Cállate, no sabes». ¿Cuántas respetan las reglas del debate?", "2", "La 1 y la 3 usan razón y turnos."),
        ex("En el debate interrumpen a una compañera porque «las mujeres hablan mucho». ¿Qué corresponde? A) Recordar que todos tienen derecho a opinar sin interrupciones. B) Dejar que sigan.", "A", "Se vulnera el derecho a participar."),
        ex("Un compañero dice: «Mi plan es mejor porque lo dije yo». ¿Es un buen argumento, sí o no?", "No", "No da una razón."),
    ],
    Z=[
        ex("Pablo dice: «Si somos diferentes, no podemos llegar a acuerdos». ¿Qué respondes?", "Que la diversidad enriquece y se puede dialogar", "Escuchar distintas opiniones mejora la decisión."),
        ex("¿Por qué conviene usar hechos para apoyar una opinión?", "Porque la hacen más sólida", "Los hechos se pueden comprobar."),
    ],
    D=[
        arith("En un debate de 40 minutos hay 5 estudiantes que hablan en turnos iguales. ¿Cuántos minutos habla cada uno?", "40//5", "Se divide el tiempo entre los participantes."),
        arith("De 20 intervenciones, 13 usaron argumentos. ¿Cuántas no los usaron?", "20-13", "Al total se le restan las que sí los usaron."),
    ],
    context=[ex("En el Consejo de Curso, dos estudiantes proponen destinos de paseo y se interrumpen. La profesora dice: «Una persona habla a la vez». ¿Qué regla recordó?", "Respetar turnos", "Permite que todos sean escuchados.")],
    selfcheck=[ex("En Orientación: ¿un argumento da una razón?", "Sí", "Apoya una opinión."), ex("¿Hombres y mujeres tienen el mismo derecho a opinar?", "Sí", "Es un principio de igualdad."), ex("¿Debatir es insultar?", "No", "Se atacan ideas, no personas.")],
    task=T("Lee el tema inventado del 7.º C: «¿Los controles de la semana deben ser un solo día o repartidos?». Escribe un argumento a favor y uno en contra, cada uno con una razón; marca un hecho y una opinión; y escribe una regla para que todos puedan opinar, hombres y mujeres.", "A favor de repartidos: así se estudia menos cada día. En contra: puede cansar toda la semana. Hecho: hay 3 controles. Opinión: es mejor repartir. Regla: respetar turnos.", ["escribe un argumento a favor y uno en contra", "marca un hecho y una opinión", "escribe una regla de participación", "no cuenta nada personal"], ["texto escrito"], ["dar opiniones sin razón", "no incluir igualdad"], "Reconoce los argumentos y pregunta cuál le parece más sólido."),
    reinforce="Escribe un argumento con «porque» para una opinión sobre el horario del recreo.",
    extend="Explica por qué la diversidad de opiniones mejora las decisiones.",
)

lesson(
    OA8, 3,
    "Una hoja y un lápiz. La elección de directiva del 7.º D, curso inventado, con sus votos, está escrita en los ejercicios.",
    "Aprenderé a comparar formas de tomar decisiones (votación, consenso, imposición) y cómo se elige democráticamente a representantes. Sirve para participar en elecciones del curso y entender sus reglas.",
    ["Sé debatir con respeto.", "Sé que existen espacios de participación."],
    [
        "Cuando un grupo debe tomar una decisión hay distintas formas. La imposición es cuando una persona o un grupo pequeño decide por todos; no es democrática. La votación es cuando cada persona vota y se decide por mayoría. La mayoría simple significa la opción con más votos. El consenso es cuando todos están de acuerdo o pueden aceptar la decisión. Cada forma tiene ventajas: el consenso es muy inclusivo pero lento; la votación es rápida pero puede dejar descontenta a la minoría.",
        "Los representantes democráticamente electos son personas elegidas por el voto de quienes representan. Una elección democrática tiene pasos: se presentan candidatos o candidatas, que explican qué proponen; se vota en forma secreta para que nadie sea presionado; se cuentan los votos en público, lo que se llama escrutinio; y gana quien tiene más votos. Un voto en blanco es el que no elige a ningún candidato. Después, los elegidos tienen el deber de representar a todos, incluso a quienes no votaron por ellos.",
        "Respetar el resultado es parte de la democracia. Quienes perdieron pueden seguir participando y proponiendo. También es importante que hombres y mujeres puedan postular y votar en igualdad.",
    ],
    [("mayoría simple", "opción que obtiene más votos"), ("consenso", "acuerdo en que todos pueden aceptar la decisión"), ("imposición", "decisión de una persona o grupo pequeño sin consultar"), ("candidato", "persona que se presenta para ser elegida"), ("escrutinio", "conteo de los votos")],
    [
        W("Contar votos", "En el 7.º D votaron 28 estudiantes: Ana 12, Beto 10 y Carla 6. ¿Quién gana por mayoría simple?", ["Se compara quién tiene más votos.", "12 es mayor que 10 y 6.", "Gana Ana."], "Ana"),
        W("Comparar formas", "Para decidir el destino del paseo, el profesor impone un lugar. ¿Es una decisión democrática?", ["Decide una persona sin consultar.", "Eso es imposición.", "No es democrática."], "No, es imposición"),
    ],
    [
        M("Pensar que quien tiene más amigos debe ganar siempre.", "Se confunde popularidad con propuestas.", "Los candidatos presentan propuestas y se vota por ellas."),
        M("Creer que si no gané, ya no puedo participar.", "Se piensa que solo participan los elegidos.", "Todos pueden seguir proponiendo."),
    ],
    R=[
        ex("Imponer una decisión sin consultar, ¿es democrático, sí o no?", "No", "No considera a los demás."),
        ex("El voto secreto, ¿sirve para que nadie sea presionado, sí o no?", "Sí", "Protege la libertad de elegir."),
        ex("El escrutinio, ¿es el conteo de votos, sí o no?", "Sí", "Se hace en público."),
    ],
    U=[
        ex("¿Qué ventaja tiene el consenso?", "Que incluye a todos", "Busca una decisión que todos acepten."),
        ex("¿Qué debe hacer un representante elegido con quienes no votaron por él?", "Representarlos también", "Representa a todo el curso."),
        ex("¿Por qué los candidatos presentan propuestas?", "Para que los votantes decidan con información", "Se vota por ideas."),
    ],
    A=[
        arith("En otra votación del 7.º D, Dani tuvo 13 votos, Eli 9 y Fran 5. ¿Cuántos estudiantes votaron en total?", "13+9+5", "Se suman los votos de los tres candidatos."),
        ex("En una votación hubo 27 votos en total y 3 fueron votos en blanco, es decir, sin elegir a nadie. ¿Cuántos votos fueron por candidatos? A) 24. B) 30.", "A", "27 menos 3 es 24; no puede haber más votos que votantes."),
        ex("Un curso decide el color de una polera por votación: 17 votos a favor del azul y 13 del rojo. ¿Qué opción gana?", "El azul", "Tiene más votos."),
    ],
    Z=[
        ex("Valeria dice: «Si pierdo, me voy». ¿Qué argumento democrático le darías?", "Que puede seguir participando y proponiendo", "La democracia incluye a quienes perdieron."),
        ex("¿Por qué la votación puede dejar descontenta a la minoría y qué se puede hacer?", "Porque su opción no ganó; se pueden escuchar sus propuestas", "Ayuda incorporar parte de lo que pidió."),
    ],
    D=[
        arith("En el curso votaron 30 estudiantes. Daniela obtuvo 16 votos. ¿Cuántos votaron por otros?", "30-16", "Al total se le restan los votos de Daniela."),
        ex("Una candidata dice: «Aunque gane con pocos votos, solo representaré a quienes me votaron». ¿Es correcto según lo aprendido?", "No", "Quien es elegido representa a todo el curso."),
    ],
    context=[ex("En el 7.º D hay empate entre dos candidatos con 14 votos cada uno. ¿Qué pueden hacer para decidir democráticamente?", "Hacer una segunda votación o un debate entre ellos", "Se busca desempatar con participación.")],
    selfcheck=[ex("En Orientación: ¿la mayoría simple es la opción con más votos?", "Sí", "Es la definición."), ex("¿El voto secreto protege la libertad?", "Sí", "Nadie es presionado."), ex("¿Una imposición es democrática?", "No", "No consulta a las personas afectadas.")],
    task=T("Lee el caso inventado: el 7.º D elige presidente. Votan 30 estudiantes: Sofía 11, Mateo 9, Josefa 8, y 2 votos en blanco. Escribe quién gana, cuántos votos válidos por candidatos hubo, dos pasos de una elección democrática y qué debe hacer la persona elegida.", "Gana Sofía con 11. Votos válidos por candidatos: 28. Pasos: candidatos con propuestas; voto secreto y escrutinio. Debe representar a todo el curso.", ["identifica al ganador", "calcula los votos", "nombra dos pasos", "dice qué debe hacer la persona elegida"], ["texto escrito"], ["no sumar bien", "olvidar a la minoría"], "Reconoce el análisis y pregunta qué haría para escuchar a quienes no votaron por ella."),
    reinforce="Inventa una votación con tres candidatos y escribe quién gana por mayoría simple.",
    extend="Explica la diferencia entre consenso y votación.",
)

lesson(
    OA8, 4,
    "Una hoja y un lápiz. El acuerdo del 7.º E sobre el uso del celular, curso inventado, está escrito en los ejercicios.",
    "Aprenderé a redactar acuerdos claros del curso con qué, quién, cuándo y cómo se revisan, respetando a la minoría. Sirve para que los acuerdos se cumplan y no queden solo en palabras.",
    ["Sé comparar formas de decidir.", "Sé que el acta registra lo decidido."],
    [
        "Un acuerdo del curso es una decisión que el grupo acepta cumplir para lograr un fin compartido. Para que funcione, debe ser claro y concreto. Un buen acuerdo responde cinco preguntas: ¿qué se hará?, ¿quién lo hará?, ¿desde cuándo y hasta cuándo?, ¿cómo se sabrá si se cumple? y ¿qué ocurre si no se cumple? Por ejemplo: «Guardaremos los celulares en la caja al entrar a la sala; todos; desde el lunes hasta el fin de mes; el delegado revisará cada viernes; si no se cumple, lo conversaremos en el Consejo de Curso».",
        "Los acuerdos deben respetar los derechos de todos. No pueden humillar, excluir ni perjudicar a una minoría. Si una persona quedó en desacuerdo, se escucha y, si es posible, se agrega una excepción razonable, como que alguien pueda usar el celular para una necesidad de salud. Los acuerdos se anotan en el acta y se leen en voz alta para que todos sepan lo decidido.",
        "Después, se revisan. A veces un acuerdo no funciona y se puede modificar por el mismo medio que se creó: conversándolo y votando. Cumplir los acuerdos es una forma de respetar al grupo y su palabra.",
    ],
    [("acuerdo", "decisión que el grupo acepta cumplir"), ("concreto", "que dice con claridad qué, quién y cuándo"), ("minoría", "grupo con menos votos o menos personas"), ("excepción", "caso en que una regla no se aplica de la misma forma"), ("modificar", "cambiar parte de un acuerdo")],
    [
        W("Evaluar un acuerdo", "Acuerdo: «Seremos más ordenados». ¿Es claro?", ["No dice qué ni quién.", "Tampoco cuándo ni cómo se revisa.", "Es poco claro."], "No, porque no es concreto"),
        W("Redactar un acuerdo", "El 7.º E quiere mantener limpia la sala. Redacta un acuerdo con qué, quién, cuándo y revisión.", ["Qué: dejar la sala ordenada al final del día.", "Quién: dos estudiantes por turno.", "Cuándo y revisión: de lunes a viernes; revisión el viernes."], "Dos estudiantes por turno ordenarán la sala al final del día, de lunes a viernes, y se revisará el viernes"),
    ],
    [
        M("Pensar que basta con una buena intención para que un acuerdo funcione.", "Se omite el plan para cumplirlo.", "Escribe qué, quién, cuándo y cómo se revisa."),
        M("Creer que la minoría debe callar una vez decidido.", "Se confunde mayoría con razón.", "Se escucha a la minoría y se evalúan excepciones razonables."),
    ],
    R=[
        ex("Un acuerdo, ¿dice qué, quién y cuándo, sí o no?", "Sí", "Así es concreto."),
        ex("«Seremos mejores» ¿es un acuerdo concreto, sí o no?", "No", "No dice qué, quién ni cuándo."),
        ex("¿Se anotan los acuerdos en el acta, sí o no?", "Sí", "Ayuda a recordarlos."),
    ],
    U=[
        ex("¿Por qué un acuerdo necesita una forma de revisión?", "Para saber si se cumple", "Permite corregir a tiempo."),
        ex("¿Puede un acuerdo humillar a una minoría, sí o no?", "No", "Debe respetar los derechos de todos."),
        ex("¿Se puede modificar un acuerdo que no funciona, sí o no?", "Sí", "Se conversa y se vota."),
    ],
    A=[
        ex("Acuerdos: 1) «Guardaremos celulares en la caja desde el lunes; el delegado revisa los viernes»; 2) «Nos portaremos bien»; 3) «Nadie hablará con Pedro»; 4) «Leeremos 10 minutos diarios en el primer bloque». ¿Cuántos son claros y respetuosos?", "2", "El 1 y el 4 son concretos; el 2 es vago y el 3 excluye."),
        ex("Un compañero necesita su celular por salud y el acuerdo prohíbe celulares. A) Se agrega una excepción razonable. B) Se le obliga a guardar el celular igual.", "A", "Se respeta su necesidad."),
        ex("Un acuerdo de limpieza no se cumple durante dos semanas. ¿Qué conviene hacer?", "Revisarlo en el Consejo de Curso y ajustarlo", "El acuerdo se evalúa y se mejora."),
    ],
    Z=[
        ex("Nicolás dice: «Si mi voto perdió, no tengo que cumplir». ¿Qué responderías?", "Que cumplir los acuerdos es respetar al grupo", "Los acuerdos obligan a todos los que participaron."),
        ex("¿Por qué conviene leer el acta en voz alta?", "Para que todos sepan lo decidido", "Así se evitan los malentendidos."),
    ],
    D=[
        arith("El acuerdo exige 10 minutos de lectura diaria en 5 días hábiles. ¿Cuántos minutos son a la semana?", "10*5", "Se multiplican minutos por días."),
        arith("De 30 estudiantes, 27 cumplieron el acuerdo. ¿Cuántos no lo cumplieron?", "30-27", "Al total se le restan los que sí cumplieron."),
    ],
    context=[ex("El 7.º E acordó «hablar solo cuando levantemos la mano». Dos semanas después nadie lo recuerda. ¿Qué falta?", "Un registro y una revisión", "Sin ellos el acuerdo se olvida.")],
    selfcheck=[ex("En Orientación: ¿un acuerdo claro dice qué, quién y cuándo?", "Sí", "Así es concreto y se puede cumplir."), ex("¿Se escucha a la minoría?", "Sí", "Para respetar sus derechos."), ex("¿Puede modificarse un acuerdo?", "Sí", "Si no funciona.")],
    task=T("Lee el problema inventado del 7.º E: el curso hace mucho ruido en los cambios de hora. Redacta un acuerdo con qué, quién, desde cuándo y hasta cuándo, cómo se revisará y qué pasa si no se cumple. Agrega una excepción razonable para una persona que lo necesite.", "Acuerdo: durante los cambios de hora conversaremos en voz baja; todos; del lunes al fin de mes; el delegado anotará cada viernes; si no se cumple, lo conversamos en el Consejo. Excepción: quien necesite hablar por una urgencia.", ["responde las cinco preguntas", "incluye una excepción", "respeta a todos", "no cuenta nada personal"], ["acuerdo escrito"], ["acuerdo vago", "no incluir revisión"], "Reconoce el acuerdo y pregunta quién lo anotaría en el acta."),
    reinforce="Convierte «Seamos puntuales» en un acuerdo concreto con qué, quién, cuándo y revisión.",
    extend="Explica por qué cumplir los acuerdos es una forma de respeto.",
)

lesson(
    OA8, 5,
    "Una hoja y un lápiz. El caso de la propuesta del 7.º F a la dirección, curso inventado, está escrito en los ejercicios.",
    "Aprenderé a comunicar una propuesta del curso a la dirección, a rendir cuentas como representante y a pedir ayuda si los acuerdos se rompen. Sirve para que la participación llegue a quienes pueden tomar decisiones.",
    ["Sé redactar un acuerdo claro.", "Sé que los representantes deben representar a todo el curso."],
    [
        "A veces el curso necesita llevar una propuesta a la dirección o a otro estamento del colegio. Para ello, la directiva o un vocero cuenta lo que el curso decidió. Una buena presentación incluye: el problema con hechos, la propuesta concreta, los beneficios para el colegio y un ofrecimiento de colaboración. Por ejemplo: «El patio queda inundado cuando llueve. Proponemos instalar una canaleta. Beneficia a todos. Nos ofrecemos para organizar una campaña».",
        "Quien representa al curso tiene el deber de rendir cuentas, es decir, informar lo que hizo y lo que respondieron. Debe contar la verdad, también cuando la respuesta fue no. Así el curso puede decidir los siguientes pasos. Un representante no decide por su cuenta lo que el curso no acordó.",
        "Si los acuerdos se rompen o una persona es discriminada por su opinión, el curso puede pedir ayuda al profesor jefe, a orientación o a convivencia escolar. También se puede proponer una mediación. Participar es un derecho, y ejercerlo con respeto y responsabilidad fortalece la convivencia.",
    ],
    [("vocero", "persona que habla en nombre de un grupo"), ("rendir cuentas", "informar al grupo lo que se hizo y lo que respondieron"), ("estamento", "grupo de personas con un rol en el colegio, como la dirección"), ("beneficio", "ventaja o mejora que trae algo"), ("ofrecer colaboración", "decir que el grupo ayudará")],
    [
        W("Armar la presentación", "El 7.º F quiere proponer instalar bebederos con agua. ¿Qué incluye la presentación?", ["El problema con hechos.", "La propuesta concreta.", "El beneficio y el ofrecimiento de colaborar."], "Problema con hechos, propuesta, beneficio y colaboración"),
        W("Rendir cuentas", "La dirección respondió que no hay presupuesto este año. ¿Qué debe decir el vocero al curso?", ["Debe decir la verdad.", "Debe contar la respuesta, aunque sea no.", "El curso decidirá los siguientes pasos."], "Que la dirección dijo que no por falta de presupuesto"),
    ],
    [
        M("Pensar que un representante puede decidir cualquier cosa por el curso.", "Se confunde representar con mandar.", "Debe llevar lo que el curso acordó."),
        M("Esconder al curso la respuesta negativa de la dirección.", "Se evita la mala noticia.", "Rendir cuentas incluye contar lo que no resultó."),
    ],
    R=[
        ex("Un vocero, ¿habla en nombre del grupo, sí o no?", "Sí", "Lleva lo que el curso decidió."),
        ex("Rendir cuentas, ¿es contar la verdad aunque la respuesta sea no?", "Sí", "Es informar con honestidad."),
        ex("¿Debe un representante decidir lo que el curso no acordó, sí o no?", "No", "Debe representar los acuerdos."),
    ],
    U=[
        ex("¿Por qué conviene incluir un ofrecimiento de colaboración?", "Porque muestra compromiso del curso", "La dirección ve que el curso también ayudará."),
        ex("¿Por qué es importante presentar el problema con hechos?", "Porque permite entender lo que ocurre", "Los hechos hacen creíble la propuesta."),
        ex("Si un acuerdo se rompe, ¿a quién puede pedir ayuda el curso?", "Al profesor jefe, orientación o convivencia escolar", "Son personas del colegio que apoyan."),
    ],
    A=[
        ex("Presentación: 1) «Hay 30 estudiantes y 1 bebedero»; 2) «Proponemos instalar 2 más»; 3) «Nos ofrecemos a organizar una campaña»; 4) «Todos son flojos». ¿Cuántas partes son correctas?", "3", "Las partes 1, 2 y 3 son hechos, propuesta y colaboración; la 4 ofende."),
        ex("El vocero cuenta al curso solo lo bueno de la reunión. A) No rindió cuentas completa. B) Rindió cuentas completa.", "A", "Debe contar también lo que no resultó."),
        ex("Una compañera es ignorada en el Consejo de Curso por ser mujer. ¿Qué puede hacer el curso?", "Recordar la igualdad y pedir ayuda al profesor jefe si sigue", "Se vulnera su derecho a participar."),
    ],
    Z=[
        ex("Martín dice: «Si la dirección dice que no, hemos perdido». ¿Qué respuesta le darías?", "Que pueden ajustar la propuesta o intentarlo de nuevo", "Participar no es solo ganar."),
        ex("¿Por qué rendir cuentas fortalece la confianza del curso?", "Porque el curso sabe qué se hizo", "La transparencia genera confianza."),
    ],
    D=[
        arith("El 7.º F propone 3 mejoras y la dirección acepta 2. ¿Cuántas no aceptó?", "3-2", "Se resta lo aceptado."),
        ex("El vocero presenta a la dirección una idea que el curso no votó, solo suya. ¿Qué falló?", "No representó lo acordado por el curso", "Un vocero lleva las decisiones del grupo."),
    ],
    context=[ex("La directiva del 7.º F fue a hablar con la dirección y volvió sin contar nada. El curso pregunta qué pasó. ¿Qué falta?", "Rendir cuentas", "El curso tiene derecho a saber qué se hizo.")],
    selfcheck=[ex("En Orientación: ¿un vocero lleva lo que el curso decidió?", "Sí", "Representa el acuerdo."), ex("¿Rendir cuentas incluye lo que salió mal?", "Sí", "Es informar con verdad."), ex("¿Puedo pedir ayuda si se rompen los acuerdos?", "Sí", "Al profesor jefe u orientación.")],
    task=T("Escribe la presentación de una propuesta del 7.º F a la dirección, con el problema (con un hecho), la propuesta concreta, el beneficio y el ofrecimiento de colaboración, sobre este tema inventado: no hay suficientes basureros en el patio. Luego escribe cómo el vocero rendiría cuentas si la respuesta fuera no.", "Problema: hay un basurero para 200 estudiantes. Propuesta: instalar cuatro más. Beneficio: patio limpio. Colaboración: el curso hará carteles. Rendición: «La dirección dijo que no por presupuesto; podemos pedir basureros reutilizados».", ["incluye hecho, propuesta, beneficio y colaboración", "escribe cómo rendir cuentas", "dice la verdad", "no cuenta nada personal"], ["texto escrito"], ["propuesta vaga", "esconder la respuesta"], "Reconoce la presentación y pregunta qué nueva propuesta haría el curso."),
    reinforce="Escribe una propuesta corta del curso con problema, propuesta, beneficio y colaboración.",
    extend="Explica por qué un representante debe contar también las malas noticias.",
)
