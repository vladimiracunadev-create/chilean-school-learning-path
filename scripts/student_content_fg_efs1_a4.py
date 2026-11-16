"""Educación Física y Salud 1, 3.º y 4.º medio FG: OAC-04 (proyectos comunitarios de bienestar y vida activa), clases 1 a 4. Comunidad, encuestas, presupuestos y resultados inventados «de ejemplo»; sin video real."""
from __future__ import annotations

from fg_efs1_common import build

O4 = "FG-EFS1-3y4-OAC-04"

# ============================================================ OAC-04, clase 1
F = ("Ficha 1 (diagnóstico de ejemplo, inventado, de una comunidad ficticia llamada Barrio Los Aromos). "
     "Encuesta anónima a 60 personas de distintas edades sobre qué actividad les gustaría hacer: caminatas 24 personas, baile 18, juegos recreativos al aire libre 12, otra actividad 6. "
     "Barreras que mencionaron (se podía marcar más de una): horario de trabajo o estudio 30 personas, falta de un lugar seguro para moverse 21, costo 15, vergüenza a ser juzgadas 12, falta de rampa en la entrada de la plaza 6. "
     "Recursos: una plaza con espacio despejado, una sede vecinal con sala techada y un grupo de personas voluntarias.")
build(
    O4, 1, F,
    use="Aprenderé a diagnosticar de forma privada y segura las necesidades, intereses y barreras de una comunidad, para proponer proyectos de bienestar y vida activa que valoren la diversidad de las personas.",
    prior=["Sé calcular porcentajes.", "Sé usar datos con respeto a la privacidad.", "Sé que cada persona parte de un lugar distinto."],
    explain=[
        "El bienestar es sentirse bien en lo físico, lo emocional y lo social. El autocuidado es lo que cada persona hace para cuidar su salud (moverse, descansar, comer de forma variada, pedir ayuda cuando hace falta). La vida activa es incorporar movimiento a la rutina diaria. La alimentación saludable es, en general, comer variado, con frutas, verduras y agua, sin dietas estrictas ni prohibiciones; las dudas de salud se conversan con personas adultas y profesionales.",
        "Para promover estos temas en una comunidad (curso, colegio o barrio) primero se hace un diagnóstico participativo: se pregunta qué actividades les interesan, qué lo impide (barreras) y qué recursos hay (lugares, personas voluntarias). La encuesta es anónima, no pide datos personales y se cuenta en porcentajes. Se valora la diversidad: personas de distintas edades, capacidades, géneros, culturas e intereses deben poder participar.",
        "Con los resultados se detectan prioridades: las actividades más pedidas y las barreras más frecuentes. Por ejemplo, si muchas personas mencionan el horario, se proponen opciones en distintos momentos. Un proyecto seguro cuida el espacio, tiene personas adultas responsables y detiene una actividad si alguien siente dolor, mareo o malestar, avisando a una persona adulta.",
    ],
    vocab=[("bienestar", "sentirse bien en lo físico, lo emocional y lo social"), ("autocuidado", "lo que cada persona hace para cuidar su salud"), ("vida activa", "movimiento incorporado a la rutina diaria"), ("diagnóstico participativo", "levantar necesidades preguntando a la comunidad"), ("barrera", "obstáculo que impide participar"), ("diversidad", "diferencias de edad, capacidades, géneros, culturas e intereses")],
    worked=[
        ("Calcular un porcentaje de la encuesta", "En una encuesta de ejemplo a 80 personas, 20 piden juegos al aire libre. ¿Qué porcentaje es?", ["Divide 20 entre 80.", "Multiplica por 100: 0,25 × 100."], "25 %"),
        ("Priorizar una barrera", "En otra comunidad ficticia, 28 de 70 personas mencionan el horario y 7 la falta de rampa. ¿Cuál barrera es más frecuente y qué se hace con la otra?", ["El horario (28 de 70, 40 %) es más frecuente que la rampa (7 de 70, 10 %).", "La rampa afecta a pocas personas, pero es un tema de acceso que también se atiende."], "El horario es más frecuente; la falta de rampa igual se debe resolver"),
    ],
    mistakes=[("Elegir la actividad que más me gusta sin preguntar a la comunidad.", "Un proyecto comunitario responde a necesidades de la comunidad, no solo a gustos propios.", "Pregunta y cuenta; usa porcentajes para priorizar."),
              ("Ignorar una barrera que afecta a pocas personas.", "Quedan excluidas esas personas y se pierde la diversidad.", "Atiende las barreras de acceso aunque sean pocas personas.")],
    T=[
        ('abc', '¿Qué es el autocuidado?', 'Lo que cada persona hace para cuidar su salud, como moverse, descansar y pedir ayuda', 'Que otra persona decida por mí lo que debo hacer para mi salud', 'Hacer dieta estricta para parecerse a otras personas', 'El autocuidado es acción propia para la salud; no es obedecer sin entender ni hacer dietas.'),
        ('abc', '{F} ¿Qué actividad fue la más pedida en la encuesta?', 'Caminatas, con 24 de 60 personas', 'Baile, con 18 de 60 personas', 'Juegos recreativos, con 12 de 60 personas', 'La actividad con mayor número de personas fue la caminata.'),
        ('abc', '¿Qué significa que una encuesta sea anónima?', 'Que no pide nombres ni datos personales', 'Que solo responden las personas que se ofrecieron como voluntarias', 'Que las respuestas se publican con el nombre de cada persona', 'Anónima significa sin identificar a quienes responden.'),
        ('=', '{F} ¿Qué porcentaje de las 60 personas encuestadas pidió caminatas?', '24/60*100', 'Se divide el número de personas entre el total y se pasa a porcentaje.', ' %'),
        ('abc', '{F} ¿Qué barrera fue más frecuente en la comunidad?', 'El horario de trabajo o estudio, con 30 personas', 'La falta de un lugar seguro, con 21 personas', 'La falta de rampa, con 6 personas', 'La barrera más repetida fue el horario, con 30 menciones.'),
        ('abc', '{F} La falta de rampa fue mencionada por 6 personas. ¿Qué decisión respeta la diversidad?', 'Resolverla igualmente, porque es una barrera de acceso, aunque sean pocas personas', 'Ignorarla, porque 6 son pocas personas y no cambian el proyecto, y resolverla costaría más de lo que beneficia al grupo', 'Esperar que quienes la necesitan encuentren otra forma de entrar sin que el equipo tenga que cambiar nada del plan', 'El acceso es un derecho; se atiende aunque haya pocas personas.'),
        ('abc', '{F} Una persona dice que nadie va a participar porque «a mucha gente le da vergüenza ser juzgada». ¿Qué respuesta del equipo es mejor?', 'Diseñar actividades sin comparar ni puntuar cuerpos y con acuerdos de respeto para participar', 'Sacar a las personas más tímidas del proyecto para evitar problemas', 'Hacer una competencia para que se animen todas las personas a mostrarse', 'Se reduce la vergüenza con actividades seguras y acuerdos de respeto, no con presión.'),
        ('abc', 'Durante una actividad de diagnóstico en la plaza, una persona siente un mareo. ¿Qué hace el equipo?', 'Detener la actividad, sentar a la persona, ofrecer agua y avisar a una persona adulta responsable', 'Pedirle que continúe más despacio hasta terminar la encuesta, porque el mareo suele pasar si se sigue con calma y no se detiene la actividad', 'Dejarla sola un momento para no interrumpir al grupo', 'Un mareo obliga a parar y a avisar a una persona adulta responsable.'),
        ('abc', 'Un grupo cuenta 30 personas que prefieren tarde y 10 que prefieren mañana. Otro grupo solo pregunta a sus amistades cercanas. ¿Cuál diagnóstico es más confiable y por qué?', 'El del primer grupo, si preguntó a una variedad de personas de la comunidad', 'El del segundo, porque sus amistades responden con más confianza', 'Los dos igual, porque ambos tienen una opinión', 'Un diagnóstico participativo incluye a personas distintas, no solo al grupo cercano.'),
        ('abc', 'En la encuesta de ejemplo, un equipo dice: «todas las personas quieren caminatas». ¿Qué corrige el análisis de la ficha?', 'Que solo 24 de 60, un 40 %, pidió caminatas, y hay otros intereses', 'Que nadie quiere caminatas', 'Que la encuesta no sirve porque no tiene nombres y así no se sabe a quién corresponde cada respuesta del grupo', 'Los porcentajes muestran que hay diversidad de intereses.'),
        ('abc', 'Un proyecto propone «alimentación saludable» como dietas estrictas para que todas las personas bajen de peso. ¿Qué corresponde señalar?', 'Que no corresponde: la alimentación saludable es variada y las dudas se hablan con adultos y profesionales', 'Que está bien si todo el curso lo hace al mismo tiempo, porque en grupo es más fácil cumplir una dieta estricta durante varias semanas', 'Que es una buena idea si se hace una competencia de resultados', 'Un proyecto escolar no promueve dietas ni comentarios sobre el cuerpo.'),
        ('abc', '{F} Con los datos de la ficha, ¿qué prioridad tiene mejor respaldo para un primer proyecto?', 'Ofrecer caminatas y baile en horarios variados y en un lugar seguro, atendiendo la rampa', 'Hacer solo juegos recreativos, porque son la actividad menos pedida y así no se compite con las actividades más conocidas del barrio', 'Ofrecer actividades en un solo horario para simplificar la organización', 'Se responde a lo más pedido, al horario y al lugar seguro, y se atiende el acceso.'),
        ('abc', '{F} Alguien suma las barreras (30 + 21 + 15 + 12 + 6 = 84) y dice que «84 personas respondieron la encuesta». ¿Qué corrección corresponde?', 'Que cada persona podía marcar más de una barrera: 84 son menciones y los porcentajes se calculan sobre las 60 personas', 'Que respondieron 84 personas, porque cada mención corresponde a una persona distinta y por eso la suma es el total de participantes', 'Que la encuesta tiene un error y hay que repetirla, porque las menciones nunca pueden ser más que las personas', 'Cuando se puede marcar más de una opción, la suma de menciones supera el número de personas.'),
    ],
    ctx=('abc', 'En una comunidad escolar ficticia de 50 personas, 20 piden baile, 15 caminatas, 10 juegos y 5 otras actividades; 25 mencionan el horario y 10 la falta de un lugar techado cuando llueve. ¿Qué propuesta de primer proyecto es más coherente?', 'Baile y caminatas en dos horarios, con una sala techada de respaldo y una persona adulta responsable', 'Solo juegos, porque tienen menos barreras de horario', 'Un torneo competitivo con premios para quienes tengan más resultados, porque motiva a participar a más personas de la comunidad', 'Responde a los intereses más pedidos y a las barreras de horario y de clima.'),
    sc=[
        ("En Educación Física: ¿qué es un diagnóstico participativo?", "Levantar necesidades y barreras preguntando a la comunidad", "Así el proyecto parte de lo que la comunidad necesita."),
        ("¿Por qué se atienden las barreras de acceso aunque afecten a pocas personas?", "Porque la diversidad exige que todas las personas puedan participar", "El acceso no depende de cuántas personas lo necesiten."),
        ("¿Qué se hace ante dolor o mareo en una actividad comunitaria?", "Detener la actividad y avisar a una persona adulta responsable", "La salud va antes que el proyecto."),
    ],
    op=("Diseña una mini encuesta de ejemplo para tu curso o barrio: dos preguntas (una de intereses y una de barreras), datos inventados rotulados «de ejemplo» de 40 personas y la conclusión de una prioridad. Incluye una medida de seguridad y una de respeto a la diversidad.",
        "Datos de ejemplo de 40 personas: 16 caminatas, 12 baile, 8 juegos, 4 otras. Barrera principal: horario, 20 personas. Prioridad: caminatas y baile en dos horarios. Seguridad: una persona adulta responsable y detener ante dolor o mareo. Diversidad: variantes para distintas edades y capacidades.",
        ["dos preguntas anónimas", "porcentajes de ejemplo", "prioridad con seguridad y diversidad"],
        ["mini encuesta de ejemplo con conclusión"],
        ["pedir nombres o datos personales", "decidir sin datos", "ignorar barreras de acceso"],
        "Pregunta: «¿qué dato respalda tu prioridad?». Si no cita un porcentaje, pídele que lo calcule."),
    reinforce="Con permiso de tu docente, conversa con una persona de tu casa sobre qué actividad le gustaría hacer y qué se lo impide, sin anotar su nombre.",
    extend="Explica por qué un proyecto comunitario no se diseña solo con los gustos de quienes lo organizan.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (opciones de proyecto de ejemplo, inventadas), para la comunidad ficticia Barrio Los Aromos. "
     "Opción 1, deportiva: mini torneo de fútbol recreativo. Opción 2, recreativa: tarde de juegos al aire libre para todas las edades. Opción 3, sociocultural: encuentro de baile con música que traiga cada persona. "
     "Criterios y pesos: inclusión (peso 3), seguridad (peso 3), costo bajo (peso 2) y participación esperada (peso 2). Puntaje de 1 a 5 en cada criterio. "
     "Puntajes opción 1: inclusión 3, seguridad 3, costo 3, participación 5. "
     "Opción 2: inclusión 5, seguridad 4, costo 5, participación 4. "
     "Opción 3: inclusión 4, seguridad 5, costo 4, participación 3.")
build(
    O4, 2, F,
    use="Aprenderé a elegir entre proyectos deportivos, recreativos y socioculturales usando criterios con pesos, y a justificar mi elección con razones de inclusión, seguridad, costo y participación.",
    prior=["Conozco el diagnóstico participativo.", "Sé calcular porcentajes.", "Sé justificar una decisión con criterios."],
    explain=[
        "Un proyecto deportivo organiza actividades de práctica o competencia amistosa de un deporte. Un proyecto recreativo propone juegos y movimiento para disfrutar y relacionarse. Un proyecto sociocultural vincula el movimiento con la cultura y la identidad de la comunidad, por ejemplo con bailes o juegos tradicionales. Si se usan juegos o danzas de pueblos originarios, no se inventan sus significados: se invita y se consulta a su educador o educadora tradicional o a representantes de la comunidad. Los tres tipos de proyecto pueden promover la vida activa y el bienestar, y se elige según lo que la comunidad necesita.",
        "Para elegir bien se usan criterios con pesos. El peso indica cuánto importa cada criterio: si la inclusión pesa 3 y el costo pesa 2, la inclusión cuenta más. Cada opción recibe un puntaje de 1 a 5 en cada criterio; se multiplica cada puntaje por su peso y se suman los resultados. La opción con más puntos tiene mejor respaldo, pero se revisa con sentido común y no se aplica de forma automática.",
        "Los criterios de seguridad e inclusión no se sacrifican por la participación: una opción muy popular pero con riesgos o que excluye a personas no es adecuada. Se valora la diversidad y se evita el lenguaje de competencia entre cuerpos. Si durante la actividad alguien siente dolor, mareo o malestar, se detiene y se avisa a una persona adulta.",
    ],
    vocab=[("proyecto deportivo", "actividad de práctica o competencia amistosa de un deporte"), ("proyecto recreativo", "juegos y movimiento para disfrutar y relacionarse"), ("proyecto sociocultural", "movimiento ligado a la cultura de la comunidad"), ("peso de un criterio", "cuánto importa ese criterio al decidir"), ("puntaje ponderado", "puntaje multiplicado por el peso y sumado")],
    worked=[
        ("Calcular un puntaje ponderado", "Una opción de ejemplo tiene inclusión 4 (peso 3), seguridad 4 (peso 3), costo 5 (peso 2) y participación 3 (peso 2). ¿Cuál es su puntaje ponderado?", ["Multiplica cada puntaje por su peso: 12, 12, 10 y 6.", "Suma: 12 + 12 + 10 + 6."], "40 puntos"),
        ("Revisar con sentido común", "Una opción de ejemplo tiene el mayor puntaje, pero su seguridad es 1 sobre 5. ¿Se elige igual?", ["Un puntaje bajo en seguridad es una señal de riesgo importante.", "Se ajusta la opción para mejorar la seguridad antes de decidir."], "No: se mejora la seguridad antes de elegir"),
    ],
    mistakes=[("Elegir el proyecto que más personas dicen que les gusta sin mirar la seguridad ni la inclusión.", "Un proyecto muy popular puede excluir o ser riesgoso.", "Usa varios criterios, con peso mayor para seguridad e inclusión."),
              ("Aplicar el puntaje sin revisar si el resultado tiene sentido.", "Los números ayudan pero no reemplazan el juicio sobre riesgos y exclusión.", "Revisa el resultado con la comunidad antes de decidir.")],
    T=[
        ('abc', '¿Qué es un proyecto sociocultural en este contexto?', 'Uno que vincula el movimiento con la cultura y la identidad de la comunidad', 'Uno que solo organiza partidos de un deporte con premios', 'Uno que se hace sin ninguna persona adulta presente', 'Lo sociocultural une movimiento y cultura; los premios o la ausencia de adultos no lo definen.'),
        ('abc', '{F} ¿Qué opción de la ficha es la deportiva?', 'La opción 1, el mini torneo de fútbol recreativo', 'La opción 2, la tarde de juegos al aire libre', 'La opción 3, el encuentro de baile', 'Un torneo de un deporte es un proyecto deportivo.'),
        ('abc', '¿Qué indica el peso de un criterio?', 'Cuánto importa ese criterio al decidir', 'Cuántas personas respondieron la encuesta', 'Cuánto cuesta realizar la actividad', 'El peso mide la importancia relativa; los otros datos son distintos.'),
        ('=', '{F} ¿Cuál es el puntaje ponderado de la opción 1?', '3*3+3*3+3*2+5*2', 'Se multiplica cada puntaje por su peso y se suman los resultados.', ' puntos'),
        ('=', '{F} ¿Cuál es el puntaje ponderado de la opción 2?', '5*3+4*3+5*2+4*2', 'Se multiplica cada puntaje por su peso y se suman los resultados.', ' puntos'),
        ('=', '{F} ¿Cuál es el puntaje ponderado de la opción 3?', '4*3+5*3+4*2+3*2', 'Se multiplica cada puntaje por su peso y se suman los resultados.', ' puntos'),
        ('abc', '{F} Según los puntajes ponderados, ¿qué opción tiene mejor respaldo?', 'La opción 2, la tarde de juegos, con 45 puntos', 'La opción 1, el torneo, con 34 puntos', 'La opción 3, el baile, con 41 puntos', 'Con 45 puntos, la opción 2 supera a la 3 (41) y a la 1 (34).'),
        ('=', '{F} Si el peso del costo bajara de 2 a 1 y el de participación subiera de 2 a 3 (inclusión y seguridad igual), ¿cuántos puntos tendría la opción 2?', '5*3+4*3+5*1+4*3', 'Se recalcula con los nuevos pesos: 15 + 12 + 5 + 12.', ' puntos'),
        ('abc', 'Una opción popular tiene seguridad 1 sobre 5 por usar un terreno con hoyos. ¿Qué decisión es adecuada?', 'Mejorar el terreno o cambiar el lugar antes de elegirla', 'Elegirla igual, porque muchas personas quieren participar', 'Realizarla sin avisar a una persona adulta', 'La seguridad es un criterio que no se sacrifica por la popularidad.'),
        ('abc', 'Durante la tarde de juegos, una niña siente un mareo. ¿Qué hace el equipo organizador?', 'Detiene el juego en su zona, la sienta con agua y avisa a una persona adulta responsable', 'Le pide que termine el juego para que no pierda el turno y que luego descanse cuando el grupo haya terminado la ronda completa', 'Ignora el mareo para no preocupar a las demás personas', 'Un mareo se atiende de inmediato con una persona adulta.'),
        ('abc', 'Un grupo propone una carrera en la que se anotan los tiempos de cada persona en un panel público. ¿Qué problema tiene para la comunidad?', 'Expone y compara cuerpos y puede excluir; conviene un registro privado o por equipos', 'Ninguno, porque los tiempos son datos objetivos y mostrarlos públicamente motiva a las personas a superarse entre sí', 'Que la carrera sea demasiado corta', 'Comparar públicamente a las personas afecta la participación y el respeto.'),
        ('abc', 'Dos grupos eligieron opciones distintas. Uno usó criterios con pesos y explicó por qué. Otro eligió «la que a todos nos gusta». ¿Cuál tiene una decisión mejor justificada?', 'El primero, porque muestra criterios y puntajes que se pueden revisar', 'El segundo, porque coincide con el gusto de todo el grupo', 'Ninguno, porque ninguna elección se puede justificar', 'La justificación con criterios permite revisar y mejorar la decisión.'),
        ('=', '{F} Si a la opción 3 se le sube la participación de 3 a 5 manteniendo los demás puntajes, ¿cuántos puntos suma con los pesos de la ficha?', '4*3+5*3+4*2+5*2', 'Se recalcula con el nuevo puntaje de participación y los mismos pesos.', ' puntos'),
    ],
    ctx=('abc', 'Una comunidad ficticia tiene opciones: A, un campeonato con premios (inclusión 2, seguridad 3, costo 2, participación 5); B, una jornada de baile y juegos tradicionales abierta a todas las edades (inclusión 5, seguridad 4, costo 4, participación 4). Con los pesos de la ficha, ¿qué decisión es más razonable?', 'Elegir B, con 43 puntos frente a 29 de A, y asegurar el espacio y una persona adulta responsable', 'Elegir A, porque tiene la mayor participación y es lo que más importa para que el proyecto se vea exitoso ante la comunidad', 'No elegir ninguna, porque no se puede decidir con números', 'B suma más con los pesos de inclusión y seguridad; A solo gana en participación.'),
    sc=[
        ("En Educación Física: ¿qué es el peso de un criterio?", "Cuánto importa ese criterio al decidir", "Un criterio con mayor peso influye más en el puntaje."),
        ("En Educación Física 1: ¿Cómo se calcula un puntaje ponderado?", "Multiplicando cada puntaje por su peso y sumando los resultados", "Así los criterios importantes pesan más."),
        ("¿Qué se hace ante dolor o mareo en un proyecto?", "Detener la actividad y avisar a una persona adulta", "La salud va antes que el proyecto."),
    ],
    op=("Elige dos proyectos de ejemplo (uno deportivo, recreativo o sociocultural) para una comunidad ficticia. Define cuatro criterios con pesos, da puntajes de ejemplo, calcula el puntaje ponderado de cada uno y decide con una razón de seguridad o inclusión. Rotula los datos como «de ejemplo».",
        "Datos de ejemplo. Criterios: inclusión 3, seguridad 3, costo 2, participación 2. Proyecto A, juegos tradicionales: 5, 4, 4, 4 = 43. Proyecto B, campeonato: 3, 3, 3, 5 = 34. Elijo A porque incluye a más edades y es más seguro.",
        ["cuatro criterios con pesos", "puntaje ponderado de cada opción", "decisión con seguridad o inclusión"],
        ["tabla de ejemplo con decisión"],
        ["no usar pesos", "decidir solo por popularidad", "ignorar la seguridad"],
        "Pregunta: «¿qué peso tuvo la seguridad?». Si lo olvidó, pídele que lo agregue."),
    reinforce="Con una persona de tu casa, elige entre dos actividades para un paseo y asigna puntajes con tres criterios.",
    extend="Explica por qué los criterios de seguridad e inclusión no deben sacrificarse por la participación.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (plan de proyecto de ejemplo, inventado): «Tarde activa de Los Aromos». "
     "Objetivo: que 40 personas de distintas edades participen en una tarde de juegos y baile, con acceso para todas las personas. "
     "Actividades: calentamiento colectivo de 10 minutos, tres estaciones de 15 minutos (juegos cooperativos, baile y caminata corta por la plaza) y 10 minutos de enfriamiento. "
     "Roles: coordinación, estaciones, primeros auxilios básicos con una persona adulta responsable, registro y comunicación. "
     "Presupuesto de ejemplo: agua y frutas $18.000, materiales $12.000, impresión de afiches $6.000. Aporte de la comunidad: $24.000. "
     "Seguridad e inclusión: rampa temporal, sillas para descansar y variantes de cada actividad.")
build(
    O4, 3, F,
    use="Aprenderé a aplicar un proyecto comunitario: planificar objetivo, actividades, roles, presupuesto, seguridad e inclusión, y promover bienestar, autocuidado y alimentación saludable de forma respetuosa.",
    prior=["Sé elegir un proyecto con criterios.", "Sé calcular porcentajes y sumas con dinero.", "Conozco las señales de detención."],
    explain=[
        "Aplicar un proyecto es organizarlo y llevarlo a cabo. Un buen plan tiene: un objetivo claro y medible, actividades con tiempos, roles para cada persona (coordinación, estaciones, primeros auxilios básicos con una persona adulta responsable, registro, comunicación), recursos y presupuesto, y un plan de seguridad e inclusión. Las actividades combinan calentamiento, parte principal y enfriamiento, igual que una sesión de entrenamiento.",
        "Promover el bienestar y el autocuidado puede incluir mensajes simples: moverse con gusto, descansar, tomar agua, ir con calzado cómodo y pedir ayuda si se siente algún malestar. Promover la alimentación saludable es ofrecer opciones variadas, como agua y fruta, sin dietas ni comentarios sobre los cuerpos. Las dudas de salud y alimentación se derivan a personas adultas y profesionales, no se resuelven en el proyecto.",
        "El presupuesto se calcula sumando los gastos y comparando con el aporte disponible; si faltan recursos, se ajusta el plan en vez de arriesgar la seguridad. En la difusión se evita publicar datos personales o fotos sin permiso. Si alguien siente dolor, mareo o malestar, se detiene la actividad y se avisa a una persona adulta responsable.",
    ],
    vocab=[("objetivo medible", "meta con un dato que permite saber si se logró"), ("rol", "tarea que asume una persona en el proyecto"), ("presupuesto", "suma de los gastos previstos"), ("aporte", "dinero o recursos que ofrece la comunidad"), ("difusión", "forma de avisar el proyecto a la comunidad")],
    worked=[
        ("Calcular un presupuesto", "Un proyecto de ejemplo gasta $9.000 en agua, $15.000 en materiales y $4.000 en afiches, y cuenta con $30.000. ¿Alcanza?", ["Suma los gastos: 9.000 + 15.000 + 4.000.", "Compara con los $30.000 disponibles."], "Gasta $28.000; alcanza y sobran $2.000"),
        ("Ajustar el plan", "Para otro proyecto de ejemplo, el presupuesto supera el aporte en $5.000. ¿Qué se ajusta?", ["Revisa qué gasto se puede reducir sin arriesgar la seguridad: por ejemplo, afiches impresos por avisos digitales o materiales prestados.", "No se reduce el botiquín ni la persona adulta responsable."], "Se reducen afiches o materiales; no se reduce la seguridad"),
    ],
    mistakes=[("Recortar la seguridad (botiquín o persona adulta responsable) para que alcance el dinero.", "La seguridad es una condición del proyecto, no un gasto opcional.", "Recorta otros gastos o busca aportes antes de tocar la seguridad."),
              ("Publicar fotos con nombres de participantes sin pedir permiso.", "Expone datos personales y puede afectar a quienes no desean aparecer.", "Pide permiso y evita nombres y datos personales.")],
    T=[
        ('abc', '¿Qué es un objetivo medible?', 'Una meta con un dato que permite saber si se logró', 'Una frase general sobre lo bueno que sería hacer una actividad', 'Una lista de las personas que no podrán asistir', 'Un objetivo medible incluye un dato verificable; una frase general no lo permite.'),
        ('abc', '{F} ¿Cuál es el objetivo del proyecto de la ficha?', 'Que 40 personas de distintas edades participen, con acceso para todas', 'Que gane el equipo con más puntos de la tarde y que se reconozca públicamente a quienes más se esforzaron', 'Que todas las personas coman lo mismo en la tarde', 'El objetivo de la ficha es participación con acceso; el resto no está en el plan.'),
        ('=', '{F} ¿Cuántos minutos dura la jornada de actividades, incluidos calentamiento, tres estaciones y enfriamiento?', '10+3*15+10', 'Se suman los minutos de calentamiento, las tres estaciones y el enfriamiento.', ' minutos'),
        ('=', '{F} ¿Cuánto suma el presupuesto de ejemplo?', '18000+12000+6000', 'Se suman los tres gastos de la ficha.', ' pesos'),
        ('=', '{F} ¿Cuánto dinero sobra o falta respecto del aporte de la comunidad? (positivo: sobra; negativo: falta)', '24000-(18000+12000+6000)', 'Se resta el presupuesto total al aporte de la comunidad.', ' pesos'),
        ('abc', '{F} Con el resultado anterior, ¿qué decisión es adecuada?', 'Reducir gastos o buscar más aportes, sin recortar la seguridad ni la persona adulta responsable', 'Recortar el botiquín y la persona adulta responsable para que alcance', 'Cancelar el proyecto, porque ningún presupuesto puede ajustarse', 'Se ajusta con otros gastos o aportes; la seguridad no se recorta.'),
        ('abc', '{F} ¿Qué rol necesita una persona adulta responsable en la ficha?', 'Primeros auxilios básicos y avisar si alguien siente dolor o mareo', 'Ganar los juegos para dar el ejemplo a las demás personas y demostrar cómo se participa con esfuerzo', 'Decidir qué cuerpos son mejores para cada estación', 'La persona adulta responsable cuida la seguridad y atiende señales de alerta.'),
        ('abc', 'Alguien propone mostrar en el afiche una foto con nombre de dos participantes de la actividad anterior. ¿Qué corresponde?', 'Pedir permiso y preferir imágenes sin nombres o sin personas identificables', 'Publicarla igual, porque ya participaron antes y ver su imagen en el afiche seguramente les dará gusto', 'Pedir a otras personas que la compartan por mensajes', 'Se protege la privacidad con permiso y sin identificar a las personas.'),
        ('abc', 'En la estación de baile, una persona dice «yo no bailo porque me van a mirar mal». ¿Qué respuesta del equipo es mejor?', 'Ofrecer una variante simple, acuerdos de respeto y la opción de participar a su ritmo', 'Insistir en que baile frente a todas las personas para superar la vergüenza', 'Quitarle un rol en el proyecto para que no se incomode', 'Se promueve la participación con respeto y opciones, sin presión.'),
        ('abc', 'Una voluntaria propone ofrecer solo bebidas con azúcar para atraer público, y otra propone agua y fruta. ¿Qué decisión se alinea con la alimentación saludable?', 'Agua y fruta, porque son opciones variadas y simples de ofrecer', 'Las bebidas con azúcar, porque atraen a más personas y hacen que la actividad se vea más animada y atractiva para todas las edades', 'Ninguna, porque es mejor no ofrecer nada', 'El proyecto promueve opciones variadas, como agua y frutas, sin dietas.'),
        ('abc', 'Durante la caminata corta, un adulto mayor siente cansancio y se sienta. ¿Qué hace el equipo?', 'Acompañarlo, ofrecer agua y que una persona adulta responsable evalúe si debe continuar', 'Pedirle que siga caminando para no retrasar al grupo, porque si se detiene el resto de las personas perderá el tiempo de la estación', 'Dejarlo sentado solo mientras el grupo sigue', 'Se respeta el cansancio y se cuida a la persona con apoyo.'),
        ('abc', 'Un equipo dice que el éxito del proyecto es «que se vea bonito en las fotos». ¿Qué corrige el análisis del proyecto?', 'Que el éxito se mide con el objetivo, como cuántas personas participaron y con qué seguridad', 'Que las fotos son lo único que importa para la evaluación, porque muestran el ambiente de la tarde', 'Que no se debe medir nada en un proyecto comunitario, porque las personas no son números', 'La evaluación usa datos del objetivo, no la imagen.'),
        ('=', '{F} El faltante se cubre con 4 aportes iguales de comercios del barrio. ¿Cuánto debe aportar cada comercio?', '(18000+12000+6000-24000)/4', 'Se calcula el faltante (presupuesto menos aporte de la comunidad) y se reparte entre 4.', ' pesos'),
    ],
    ctx=('abc', 'Un equipo ficticio planifica un proyecto para 30 personas: gasto en agua y frutas $10.000, materiales $8.000, afiches $4.000; aporte $20.000. Falta el botiquín, que cuesta $5.000. ¿Qué decisión es mejor?', 'Agregar el botiquín y ajustar otros gastos o buscar $7.000 más, sin quitar la persona adulta responsable', 'No comprar el botiquín, porque no hay dinero para todo', 'Cancelar el agua y las frutas para comprar más afiches, porque la difusión trae más gente al proyecto y compensa el gasto', 'Con el botiquín el gasto sube a $27.000, faltan $7.000 y se ajusta sin tocar la seguridad.'),
    sc=[
        ("En Educación Física: ¿qué debe incluir un plan de proyecto comunitario?", "Objetivo, actividades, roles, presupuesto, seguridad e inclusión", "Así el proyecto es claro y seguro."),
        ("¿Qué se hace si el presupuesto no alcanza?", "Ajustar otros gastos o buscar aportes, sin recortar la seguridad", "La seguridad no es opcional ni se recorta nunca."),
        ("¿Qué se hace ante dolor o mareo en una actividad?", "Detener la actividad y avisar a una persona adulta responsable", "La salud va antes que cumplir el programa."),
    ],
    op=("Escribe el plan de un proyecto de ejemplo de una tarde activa: objetivo medible, cuatro actividades con minutos, tres roles, presupuesto de ejemplo (con tres gastos y un aporte), una medida de seguridad y una de inclusión. Rotula los datos como «de ejemplo».",
        "Datos de ejemplo. Objetivo: 30 personas participan. Actividades: calentamiento 10, juegos 20, baile 20, enfriamiento 10 minutos. Roles: coordinación, primeros auxilios con persona adulta, registro. Presupuesto: agua y fruta $10.000, materiales $8.000, afiches $3.000 = $21.000; aporte $22.000. Seguridad: botiquín y detener ante dolor o mareo. Inclusión: sillas y variantes simples.",
        ["objetivo medible y actividades con minutos", "roles y presupuesto", "seguridad e inclusión"],
        ["plan de una tarde activa con presupuesto de ejemplo"],
        ["objetivo sin dato", "recortar la seguridad", "publicar datos personales"],
        "Pregunta: «¿cómo sabrás si se logró el objetivo?». Si no hay un dato, pídele que lo agregue."),
    reinforce="Con una persona adulta de confianza, escribe una lista de cinco materiales y su costo de ejemplo para una actividad comunitaria pequeña.",
    extend="Explica por qué la seguridad no se recorta cuando el presupuesto no alcanza.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (resultados de ejemplo, inventados) de «Tarde activa de Los Aromos». "
     "Meta: 40 personas participantes. Asistencia real: 34 personas (9 menores de 12 años, 14 entre 12 y 17 años, 11 de 18 años o más). "
     "Satisfacción (encuesta anónima, 34 respuestas): 24 muy satisfechas, 8 satisfechas, 2 poco satisfechas. "
     "Seguridad: ningún incidente; una persona descansó por cansancio y retomó sin problemas. "
     "Comentarios frecuentes: el horario de las 18:00 fue tarde para algunas personas; la rampa temporal funcionó. "
     "Recursos usados: $33.000 de los $36.000 presupuestados.")
build(
    O4, 4, F,
    use="Aprenderé a registrar y evaluar un proyecto comunitario con indicadores de asistencia, diversidad, satisfacción y seguridad, a calcular porcentajes y a proponer ajustes respetando la privacidad.",
    prior=["Sé aplicar un plan de proyecto.", "Sé calcular porcentajes.", "Sé usar encuestas anónimas."],
    explain=[
        "Evaluar un proyecto es comprobar qué tanto logró su objetivo y qué se puede mejorar. Se usan indicadores: la asistencia (personas que llegaron sobre la meta), la diversidad (si participaron personas de distintas edades y capacidades), la satisfacción (qué opinan, con una encuesta anónima), la seguridad (incidentes y cómo se resolvieron) y el uso de recursos (cuánto se gastó del presupuesto).",
        "Un buen registro se hace durante la actividad con una pauta simple y se completa con una conversación posterior. Se informa a la comunidad con datos generales, sin nombres ni fotos sin permiso. Los resultados no se usan para comparar personas, sino para ajustar el proyecto: por ejemplo, cambiar el horario si varias personas lo mencionan, o mantener lo que funcionó, como la rampa temporal.",
        "También se evalúa el autocuidado del equipo organizador: descansar, repartir tareas y pedir ayuda. Si durante el registro alguien siente dolor, mareo o malestar, se detiene la actividad y se avisa a una persona adulta responsable. Con los resultados se fija una mejora para la próxima vez, de a una cosa a la vez, y se agradece a quienes participaron.",
    ],
    vocab=[("indicador", "dato que sirve para evaluar un resultado"), ("asistencia", "personas que participaron sobre las esperadas"), ("diversidad de participantes", "presencia de personas de distintas edades y capacidades"), ("satisfacción", "opinión de quienes participaron sobre el proyecto"), ("ajuste", "cambio que se hace para la próxima vez")],
    worked=[
        ("Calcular la asistencia", "En un proyecto de ejemplo con meta de 50 personas, llegaron 40. ¿Qué porcentaje de la meta se cumplió?", ["Divide 40 entre 50.", "Multiplica por 100: 0,8 × 100."], "80 % de la meta"),
        ("Proponer un ajuste con datos", "En otro proyecto de ejemplo, 12 de 30 personas dicen que el horario fue tarde. ¿Qué ajuste propones?", ["12 de 30 es el 40 %, un grupo importante.", "Ofrece dos horarios o adelanta la hora de inicio la próxima vez."], "Ofrecer dos horarios o adelantar la hora"),
    ],
    mistakes=[("Concluir que el proyecto fue un éxito porque fue «lindo».", "Sin datos no se sabe si se logró el objetivo.", "Usa indicadores: asistencia, diversidad, satisfacción y seguridad."),
              ("Comparar a las personas participantes para ver «quién se movió más».", "Compara cuerpos y no evalúa el proyecto.", "Evalúa el proyecto, no a las personas.")],
    T=[
        ('abc', '¿Qué es un indicador en la evaluación de un proyecto?', 'Un dato que permite evaluar un resultado, como la asistencia', 'Una opinión general sobre si fue bonito', 'La cantidad de afiches que se imprimieron', 'Un indicador es un dato; una opinión o un nombre no lo es.'),
        ('=', '{F} ¿Qué porcentaje de la meta de 40 personas cumplió la asistencia real?', '34/40*100', 'Se divide la asistencia real entre la meta y se pasa a porcentaje.', ' %'),
        ('abc', '{F} ¿Cuántas personas de las 34 tenían 12 años o más?', '25, porque 14 + 11 = 25', '23, porque 9 + 14 = 23', '34, porque participaron todas', 'Las personas de 12 años o más son los dos grupos de 14 y 11.'),
        ('=', '{F} Entre las personas que dijeron estar satisfechas o muy satisfechas, ¿qué porcentaje dijo estar muy satisfecha?', '24/(24+8)*100', 'Se suman las respuestas satisfechas y muy satisfechas (32) y se calcula qué porcentaje son las 24 muy satisfechas.', ' %'),
        ('abc', '{F} ¿Qué indica el indicador de seguridad de la ficha?', 'Que no hubo incidentes y que una persona descansó y retomó sin problemas', 'Que hubo un incidente que obligó a suspender la actividad para todo el grupo', 'Que no se registró la seguridad en el proyecto', 'La ficha informa ningún incidente y un descanso por cansancio resuelto.'),
        ('=', '{F} ¿Cuánto dinero quedó sin usar del presupuesto?', '36000-33000', 'Se resta lo gastado al presupuesto total.', ' pesos'),
        ('abc', '{F} Un integrante dice: «Con 34 de 40 asistentes el proyecto fracasó». ¿Qué respuesta es más adecuada?', 'Que el 85 % de la meta es un buen resultado y se revisan las barreras de quienes no llegaron', 'Que sí fracasó, porque no llegaron las 40 personas de la meta y una meta no cumplida es un fracaso', 'Que no se debe medir la asistencia, porque contar personas es una forma de compararlas', 'Un 85 % con buena satisfacción y seguridad es un resultado favorable que se puede mejorar.'),
        ('abc', '{F} Varias personas dijeron que las 18:00 horas fue tarde. ¿Qué ajuste es mejor?', 'Ofrecer dos horarios o adelantar el inicio la próxima vez y volver a evaluar', 'Ignorar el comentario, porque la mayoría estaba satisfecha y cambiar el horario complicaría la organización del proyecto', 'Cambiar horario, lugar y actividades a la vez', 'Se ajusta una sola cosa que se relaciona con la barrera mencionada.'),
        ('abc', 'Alguien quiere publicar en redes una lista con nombre de quienes asistieron y su edad. ¿Qué corresponde?', 'No publicar nombres ni edades; compartir resultados generales', 'Publicarla, porque agradece a las personas', 'Pedirla a otra persona para publicar sin que se note', 'Se protegen los datos personales y se informan solo resultados generales.'),
        ('abc', 'Durante el registro de asistencia, una voluntaria siente un mareo. ¿Qué hace el equipo?', 'Detiene el registro, la sienta con agua y avisa a una persona adulta responsable', 'Le pide terminar, porque es la única que sabe llevar la lista y sin ella se perdería el registro completo del proyecto', 'La deja registrando sentada, sin avisar a nadie', 'El mareo es una señal de detención; se cuida a la persona.'),
        ('abc', 'Dos equipos evalúan un proyecto. Uno usa asistencia, diversidad, satisfacción y seguridad. El otro solo usa la opinión de la persona que coordinó. ¿Cuál evaluación es más completa y por qué?', 'La del primero, porque combina varios indicadores sobre distintos aspectos del proyecto', 'La del segundo, porque quien coordina conoce mejor el proyecto', 'Ninguna, porque no se puede evaluar un proyecto comunitario', 'Más indicadores dan una visión más completa y verificable.'),
        ('abc', 'En la evaluación, 2 de 34 personas estuvieron poco satisfechas. ¿Qué decisión es más razonable?', 'Preguntar de forma anónima qué cambiarían y usar sus respuestas para el ajuste', 'Ignorar esas respuestas, porque son pocas frente a las 32 personas satisfechas', 'Culparlas por no disfrutar la actividad y pedirles que la próxima vez se esfuercen más', 'Las opiniones minoritarias pueden mostrar barreras que se pueden resolver.'),
        ('=', '{F} Si la próxima vez la meta es 45 personas, ¿qué porcentaje más de asistencia que las 34 personas de esta vez habría que lograr? Redondea hacia abajo al entero.', '(45-34)*100//34', 'Se calcula el aumento (11 personas), se divide entre 34 y se pasa a porcentaje, redondeado hacia abajo.', ' %'),
    ],
    ctx=('abc', 'En un proyecto ficticio con meta de 50 personas llegaron 30; 27 de 30 respuestas estuvieron muy satisfechas, no hubo incidentes y 10 personas dijeron no haber asistido por la distancia al lugar. ¿Qué conclusión y ajuste son coherentes?', 'Buena satisfacción y seguridad, pero baja asistencia por la distancia: ofrecer una segunda sede o actividades cerca de más hogares', 'El proyecto fue perfecto, porque casi todas las personas estuvieron satisfechas y no hace falta cambiar nada más para la próxima vez, que seguramente será igual', 'El proyecto fracasó, porque no se logró la meta de 50 personas', 'Se reconoce lo que funcionó y se ajusta la barrera que explica la baja asistencia.'),
    sc=[
        ("En Educación Física: ¿qué indicadores sirven para evaluar un proyecto comunitario?", "Asistencia, diversidad, satisfacción, seguridad y uso de recursos", "Cada indicador muestra un aspecto distinto del proyecto."),
        ("¿Para qué se usan los resultados de la evaluación?", "Para ajustar el proyecto, no para comparar personas", "El objetivo es mejorar el proyecto."),
        ("¿Qué se hace ante dolor o mareo durante el registro?", "Detener la actividad y avisar a una persona adulta responsable", "La salud va antes que el registro."),
    ],
    op=("Con datos de ejemplo de un proyecto (meta y asistencia, satisfacción de una encuesta anónima, un incidente o ninguno, un comentario frecuente), calcula dos porcentajes, interpreta y propón un ajuste. Rotula los datos como «de ejemplo».",
        "Datos de ejemplo. Meta: 30 personas; asistieron 24 (80 %). Satisfacción: 18 de 24 muy satisfechas (75 %). Seguridad: sin incidentes. Comentario: poca sombra en la plaza. Ajuste: realizar la próxima vez en la sede techada o con toldos y agua. Ante dolor o mareo, paro y aviso.",
        ["dos porcentajes calculados", "interpretación con un límite", "un ajuste de una sola cosa"],
        ["resumen de evaluación con datos de ejemplo"],
        ["no usar datos", "publicar nombres", "comparar a las personas"],
        "Pregunta: «¿qué dato apoya tu ajuste?». Si no cita uno, pídele que lo busque."),
    reinforce="Con permiso de tu docente, evalúa una actividad de recreo con tres indicadores y anota un ajuste, sin nombres.",
    extend="Explica por qué los resultados de un proyecto comunitario se informan sin datos personales.",
)
