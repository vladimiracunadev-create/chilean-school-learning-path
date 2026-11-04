"""Cuaderno del estudiante, 1.º medio Orientación: OA 07 (participación social e institucional cercana) y OA 08 (iniciativas de justicia, buen trato y bien común)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA7, OA8 = "OR1M OA 07", "OR1M OA 08"


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


# ================================================================ OA 07
lesson(
    OA7, 1,
    "Una hoja y un lápiz. El acta del Consejo de Curso de 1.º B está escrita en los ejercicios; es ficticia y no tiene datos reales.",
    "Aprenderé a leer el acta de un curso y a identificar un problema, quiénes se ven afectados y qué instancias existen para participar. Sirve para contribuir a resolver problemas de mi curso, mi colegio o mi barrio.",
    ["Sé que el Consejo de Curso es un espacio para dialogar y decidir (8.º básico).", "Sé que tengo derecho a opinar."],
    [
        "Participar es tomar parte en las decisiones y acciones de un grupo. Puedes participar en tu curso, tu establecimiento, tu barrio u otros espacios. Los espacios de participación formal en un colegio son, por ejemplo, el Consejo de Curso, la directiva del curso y el Centro de Estudiantes; en el barrio, pueden ser una junta de vecinos, un club deportivo o una biblioteca.",
        "Una persona es sujeto de derecho cuando tiene derechos que se le deben respetar y puede exigirlos. Los y las estudiantes lo son: tienen derecho a opinar, a ser escuchados y a que se respeten su dignidad y su diversidad. Para participar bien se parte por entender el problema: qué pasa, a quiénes afecta, desde cuándo y qué instancia podría ayudar.",
        "Un acta es el registro escrito de lo conversado y acordado en una reunión. Un buen acta incluye fecha, asistentes, temas, acuerdos, responsables y plazos. Leer un acta permite distinguir hechos de opiniones y ver qué falta. Los valores que guían la participación son la dignidad, la diversidad, la equidad de género, la inclusión, la justicia, el bienestar y la participación democrática.",
    ],
    [("participación", "tomar parte en decisiones y acciones de un grupo"), ("sujeto de derecho", "persona con derechos que se le deben respetar y que puede exigir"), ("acta", "registro escrito de lo conversado y acordado en una reunión"), ("instancia", "espacio formal donde se puede participar o decidir"), ("actor", "persona o grupo que influye o es afectado por un problema")],
    [
        W("Identificar el problema", "Acta de ejemplo: «Tema: el patio tiene basura después del recreo. Hechos: hay 3 basureros para 400 estudiantes. Acuerdo: pedir más basureros». ¿Cuál es el problema?", ["Hay basura en el patio.", "Los basureros son pocos para tantas personas."], "La basura en el patio y la falta de basureros"),
        W("Instancia adecuada", "El curso quiere pedir más basureros. ¿A qué instancia puede llevar la propuesta?", ["Primero a la directiva y al profesor jefe.", "Luego al Centro de Estudiantes o a la dirección."], "A la directiva del curso, al profesor jefe o al Centro de Estudiantes"),
    ],
    [
        M("Creer que participar es solo votar.", "Se piensa que participar acaba en la elección.", "Participar incluye proponer, informarse, dialogar y comprometerse."),
        M("Confundir una opinión con un hecho al leer un acta.", "Se toma lo dicho como probado.", "Marca qué dato se puede comprobar."),
    ],
    R=[
        ex("¿Cuál es una instancia de participación dentro de un colegio? A) El Consejo de Curso B) El recreo", "A", "Es un espacio formal para dialogar y decidir."),
        ex("Un curso quiere dejar por escrito qué se acordó, quién lo hará y para cuándo. ¿Qué documento usa? A) Un acta B) Un afiche", "A", "El acta registra acuerdos, responsables y plazos."),
        ex("Un adulto dice: «los estudiantes no opinan en esta reunión». ¿Qué principio ignora? A) Que los y las estudiantes tienen derecho a opinar y ser escuchados B) Que las reuniones deben ser cortas", "A", "Los y las estudiantes son sujetos de derecho."),
    ],
    U=[
        ex("¿Qué es un sujeto de derecho? A) Una persona con derechos que puede exigir B) Una persona que debe obedecer sin opinar.", "A", "Tiene derechos reconocidos."),
        ex("¿Cuál es una instancia de participación del barrio? A) Una junta de vecinos B) Un grupo de amigos que se junta a jugar", "A", "Reúne a vecinos para tratar problemas comunes."),
        ex("¿Qué aporta un acta bien hecha? A) Acuerdos, responsables y plazos B) Solo la fecha.", "A", "Permite seguir lo acordado."),
    ],
    A=[
        ex("Acta de ejemplo: «Asisten 28 de 36 estudiantes. Tema: el baño del segundo piso no tiene jabón desde hace 2 semanas. Acuerdo: Valentina avisará al profesor jefe el lunes». ¿Cuál es el hecho comprobable? A) El baño no tiene jabón hace 2 semanas B) El colegio no se preocupa.", "A", "Se puede verificar; la otra frase es una opinión."),
        ex("Acta de ejemplo: «Asisten 28 de 36 estudiantes». ¿Cuántos faltaron?", "8", "36 menos 28 son 8 estudiantes."),
        ex("Un acta dice: «Acuerdo: Valentina avisará al profesor jefe el lunes». Según el acta, ¿quién avisa y a quién? A) Valentina avisa al profesor jefe B) El profesor jefe avisa a Valentina.", "A", "El acuerdo nombra a Valentina como responsable."),
    ],
    Z=[
        ex("¿Por qué conviene identificar a quiénes afecta un problema antes de proponer una solución?", "Porque la solución debe considerar a todas las personas afectadas", "Si se ignora a alguien, la solución puede ser injusta."),
        ex("Un compañero dice: «Es problema del colegio, no mío». ¿Qué le responderías? A) Que el curso también puede proponer y contribuir B) Que tiene razón.", "A", "La participación incluye aportar en el entorno cercano."),
    ],
    D=[
        arith("En un acta de ejemplo, 24 de 32 estudiantes votan a favor de una propuesta. ¿Cuántos no votan a favor?", "32-24", "Al total se le restan los votos a favor."),
        arith("Un curso de 36 estudiantes forma comisiones de 4 personas para atender 3 temas del acta. ¿Cuántas comisiones se pueden formar con todos?", "36//4", "Se divide el total entre los integrantes de cada comisión."),
    ],
    context=[ex("Tu colegio no tiene rampa para una compañera que usa silla de ruedas. El curso discute qué hacer. ¿Qué valor guía principalmente la participación? A) La inclusión B) El ahorro de dinero.", "A", "Busca que todas las personas puedan acceder y participar.")],
    selfcheck=[ex("En Orientación: ¿participar es tomar parte en decisiones y acciones?", "Sí", "Es su definición."), ex("¿Un acta ayuda a distinguir hechos y acuerdos?", "Sí", "Los registra por escrito."), ex("¿Los y las estudiantes son sujetos de derecho?", "Sí", "Tienen derechos reconocidos.")],
    task=T("Lee esta acta inventada: «Consejo de Curso de 1.º B. Asisten 30 de 35 estudiantes. Tema 1: en el patio no hay sombra y dos estudiantes se mareeron en el recreo de las 13:00. Tema 2: la cancha la usan solo los hombres. Acuerdo: Pedro hablará con el profesor jefe. Plazo: el viernes». Escribe: los dos problemas, quiénes se afectan en cada uno, un valor en juego y una instancia a la que llevarías cada propuesta.", "Problema 1: falta de sombra, afecta a todo el curso; valor: bienestar; instancia: profesor jefe o dirección. Problema 2: la cancha excluye a mujeres; valor: equidad de género e inclusión; instancia: Consejo de Curso y Centro de Estudiantes.", ["identifica los dos problemas", "nombra a quiénes afecta", "nombra un valor por problema", "nombra una instancia por problema"], ["tabla escrita", "texto oral"], ["confundir problema con solución", "olvidar a las personas afectadas"], "Reconoce los problemas y pregunta qué valor guía cada propuesta."),
    reinforce="Escribe un problema de tu curso inventado y la instancia a la que lo llevarías.",
    extend="Explica por qué un acta ayuda a que los acuerdos se cumplan.",
)

lesson(
    OA7, 2,
    "Una hoja y un lápiz. La tarjeta de derechos y los casos del Consejo de Curso, con personas inventadas, están escritos en los ejercicios.",
    "Aprenderé a distinguir hechos, derechos y límites en la participación: qué puedo pedir, a quién y dentro de qué competencias. Sirve para proponer con fundamentos y sin pedir cosas que nadie puede decidir ahí.",
    ["Sé identificar problemas y actores en un acta.", "Sé que mi opinión vale igual que la de los demás."],
    [
        "La Convención sobre los Derechos del Niño, que Chile reconoce, establece que niñas, niños y adolescentes tienen derecho a opinar sobre lo que les afecta y a que se les tome en cuenta. Participar es un derecho, no un favor. También protege la dignidad: nadie puede ser humillado por opinar distinto, y se garantiza la no discriminación.",
        "Los hechos sustentan una propuesta. Un hecho es un dato comprobable, como «hay 3 basureros para 400 personas». Una opinión es una valoración, como «el colegio es un desastre». Las propuestas con hechos son más persuasivas. También hay límites de competencia: el curso decide sobre sus propias actividades, pero no sobre el presupuesto del colegio, que lo definen la dirección y quienes administran el colegio; y el municipio decide sobre la plaza del barrio.",
        "Hay límites éticos también: no se participa con insultos, con amenazas, difundiendo fotos o rumores de otros, ni dañando bienes. La participación democrática significa que todas las voces se escuchan, que se decide con reglas conocidas y que se respeta la decisión tomada, aunque no sea la que uno prefería.",
    ],
    [("derecho a opinar", "derecho a expresar lo que uno piensa sobre lo que le afecta y ser escuchado"), ("competencia", "lo que una instancia puede decidir"), ("hecho", "dato que se puede comprobar"), ("participación democrática", "participar con reglas conocidas escuchando todas las voces"), ("presupuesto", "dinero disponible para gastar en un período")],
    [
        W("Hecho u opinión", "«Hay un solo bebedero para 400 estudiantes» y «Este colegio no cuida a nadie». ¿Cuál es hecho?", ["El número de bebederos se puede contar.", "La otra frase es una valoración."], "La primera"),
        W("Competencia", "El curso quiere cambiar el presupuesto anual del colegio. ¿Puede decidirlo el Consejo de Curso?", ["El presupuesto lo definen la dirección y quienes administran el colegio.", "El curso puede presentar una propuesta."], "No decide, pero puede proponer"),
    ],
    [
        M("Creer que tener derecho a opinar significa que mi propuesta debe aceptarse.", "Se confunde ser escuchado con imponer.", "Se escucha a todos y se decide con reglas conocidas."),
        M("Pedir al Consejo de Curso algo que no puede decidir.", "No se revisa la competencia.", "Identifica la instancia que sí decide."),
    ],
    R=[
        ex("Los estudiantes opinan sobre un cambio de horario que les afecta. ¿Qué derecho ejercen? A) El derecho a opinar sobre lo que les afecta B) El derecho a decidir el presupuesto", "A", "La Convención reconoce ese derecho."),
        ex("«Hay 2 puertas de salida para 300 personas», ¿es un hecho o una opinión?", "Un hecho", "Se puede contar."),
        ex("¿Cuál de estas conductas cruza un límite ético al participar? A) Difundir fotos de otros sin permiso B) Pedir la palabra", "A", "Atenta contra la privacidad y la dignidad."),
    ],
    U=[
        ex("¿Quién define el presupuesto del colegio? A) La dirección y quienes administran el colegio B) El Consejo de Curso.", "A", "El curso no maneja ese presupuesto."),
        ex("¿Qué hace más fuerte una propuesta? A) Datos comprobables B) Palabras más fuertes.", "A", "Los hechos la sustentan."),
        ex("¿Qué significa participación democrática? A) Escuchar todas las voces y respetar la decisión con reglas B) Que mande quien habla más fuerte.", "A", "Se basa en reglas y en escuchar."),
    ],
    A=[
        ex("Clasifica con H (hecho) o O (opinión): 1) Faltan 2 sillas en la sala. 2) Esta sala es horrible. 3) Hay un solo enchufe para 30 personas. Escribe las letras en orden.", "H, O, H", "La 1 y la 3 se pueden contar; la 2 es una valoración."),
        ex("El curso quiere una actividad para recaudar fondos del paseo. ¿Quién puede decidirla? A) El propio curso con la autorización de la dirección B) El municipio.", "A", "Es una actividad del curso dentro del colegio."),
        ex("Un estudiante propone: «Subamos fotos de los profesores para criticarlos». ¿Qué problema tiene? A) Cruza el límite del respeto y la privacidad B) Es una forma de participar.", "A", "Expone y daña a personas."),
    ],
    Z=[
        ex("¿Por qué respetar una decisión democrática aunque no sea mi favorita?", "Porque se tomó con reglas y escuchando a todos", "El proceso legítimo se respeta aunque el resultado no guste."),
        ex("Un curso quiere pedir mejoras al municipio por la plaza del barrio. ¿Qué es lo más adecuado? A) Presentar la propuesta con datos a la instancia que decide B) Dañar la plaza para llamar la atención.", "A", "Es una vía pacífica y fundamentada."),
    ],
    D=[
        arith("En una votación de ejemplo, 18 estudiantes votan a favor, 9 en contra y 3 se abstienen. ¿Cuántos votaron en total?", "18+9+3", "Se suman todos los votos."),
        arith("De 36 estudiantes, 27 asisten al Consejo de Curso. ¿Cuántos no asisten?", "36-27", "Al total se le restan los que asisten."),
    ],
    context=[ex("En el curso quieren pedir más tiempo de recreo. Alguien propone preguntar primero qué instancia puede cambiar los horarios. ¿Por qué es buena idea? A) Porque se pide a quien tiene competencia B) Porque retrasa el tema.", "A", "Evita pedir a quien no puede decidir.")],
    selfcheck=[ex("En Orientación: ¿participar es un derecho?", "Sí", "No es un favor."), ex("¿Una propuesta con hechos es más sólida?", "Sí", "Se puede comprobar."), ex("¿Se puede participar insultando?", "No", "Atenta contra la dignidad.")],
    task=T("Lee las cinco frases inventadas de un Consejo de Curso: (a) «El baño tiene 2 lavamanos para 70 personas»; (b) «Esta dirección es inútil»; (c) «Queremos organizar un campeonato de ajedrez»; (d) «Que el director cambie el presupuesto»; (e) «Quien no vote como yo es traidor». Clasifica cada una como hecho, opinión, propuesta dentro de la competencia del curso o propuesta fuera de ella, o conducta que no respeta; y reescribe (b) como una propuesta con un hecho.", "(a) hecho; (b) opinión; (c) propuesta dentro del curso; (d) fuera de su competencia (puede proponer); (e) conducta que no respeta. Reescritura: «Proponemos más lavamanos: hay 2 para 70 personas».", ["clasifica las cinco frases", "reescribe con un hecho", "distingue competencia", "no usa insultos"], ["tabla escrita", "texto oral"], ["confundir opinión con hecho", "olvidar la competencia"], "Reconoce lo bien clasificado y pregunta quién decidiría la propuesta (d)."),
    reinforce="Escribe una opinión y la transformas en una propuesta con un hecho.",
    extend="Explica por qué el derecho a opinar no obliga a que todos estén de acuerdo.",
)

lesson(
    OA7, 3,
    "Una hoja y un lápiz. Las tres propuestas del curso inventado y la tabla de criterios están escritas en los ejercicios.",
    "Aprenderé a comparar propuestas de participación con criterios (dignidad, inclusión, equidad de género, bienestar, factibilidad) y a prever sus consecuencias. Sirve para elegir la mejor para el curso.",
    ["Sé distinguir hechos de opiniones y competencias.", "Sé qué es inclusión."],
    [
        "Cuando un curso tiene varias propuestas, conviene compararlas con criterios claros. Algunos criterios son: dignidad (respeta a las personas), inclusión (permite que todos participen), equidad de género (da oportunidades parejas a mujeres y hombres), bienestar (mejora la vida escolar), justicia (es justa para todos) y factibilidad (se puede hacer con el tiempo, el dinero y los permisos disponibles).",
        "Un cuadro de comparación pone las propuestas en filas y los criterios en columnas. Se marca sí o no, o se da 1 punto por criterio cumplido. Sumar ayuda a decidir, pero no basta: un criterio puede pesar más. Por ejemplo, una propuesta que excluye a un grupo no es aceptable aunque sea barata.",
        "También se anticipan las consecuencias, tanto para el curso como para el colegio: a corto plazo (esfuerzo y tiempo) y a largo plazo (costumbres y convivencia). Una propuesta con mayores beneficios para más personas, sin dañar a nadie y que se pueda realizar, suele ser la mejor.",
    ],
    [("criterio", "regla para comparar propuestas"), ("factible", "que se puede realizar con los recursos disponibles"), ("equidad de género", "oportunidades justas y parejas para mujeres y hombres"), ("bienestar", "sensación de estar bien en el colegio"), ("consecuencia", "lo que ocurre después de aplicar una propuesta")],
    [
        W("Puntuar una propuesta", "Propuesta: un campeonato mixto de fútbol. Dignidad sí, inclusión sí, equidad de género sí, bienestar sí, factible sí. ¿Cuántos puntos tiene?", ["Se cuenta 1 punto por criterio cumplido.", "Cumple los 5."], "5 puntos"),
        W("Un criterio que pesa más", "La propuesta B tiene 4 puntos, pero excluye a las estudiantes. La C tiene 3 y excluye a nadie. ¿Cuál conviene?", ["Excluir vulnera la dignidad y la inclusión.", "C es aceptable."], "La propuesta C"),
    ],
    [
        M("Elegir solo por la propuesta más barata.", "Se mira solo la factibilidad.", "Considera todos los criterios y las personas afectadas."),
        M("Sumar puntos sin mirar si alguna propuesta excluye a alguien.", "Se cree que la suma decide todo.", "Una propuesta que excluye no se acepta aunque sume."),
    ],
    R=[
        ex("Una propuesta de campeonato es solo para quienes ya juegan bien. ¿Qué criterio incumple? A) La inclusión B) La factibilidad", "A", "Deja afuera a quienes no juegan tan bien."),
        ex("Una propuesta cuesta mucho y la dirección no la autoriza. ¿Qué criterio incumple? A) La factibilidad B) La dignidad", "A", "No se puede realizar con los recursos y permisos disponibles."),
        ex("En un cuadro de comparación, ¿qué va en las filas y qué en las columnas? A) Propuestas en las filas y criterios en las columnas B) Personas en las filas y votos en las columnas", "A", "Cada propuesta se evalúa con los mismos criterios."),
    ],
    U=[
        ex("¿Qué propuesta cumple mejor la equidad de género? A) Un campeonato mixto con turnos parejos B) Un campeonato solo para quienes ya juegan bien.", "A", "Da oportunidades parejas."),
        ex("¿Qué criterio revisa si alcanza el tiempo y los permisos? A) La factibilidad B) La dignidad.", "A", "Evalúa si se puede realizar."),
        ex("¿Qué consecuencia a largo plazo tiene una actividad inclusiva repetida? A) Mejor convivencia B) Más gasto sin ningún efecto.", "A", "Todos se sienten parte."),
    ],
    A=[
        ex("Tres propuestas con 1 punto por criterio: A: dignidad, inclusión, bienestar (3 puntos); B: dignidad, factibilidad (2 puntos); C: dignidad, inclusión, equidad, bienestar, factibilidad (5 puntos). ¿Cuál suma más?", "C", "Tiene 5 puntos."),
        ex("Una propuesta cuesta $40.000 y el curso dispone de $25.000. ¿Es factible tal como está? A) No B) Sí.", "A", "Faltan $15.000 para pagarla."),
        ex("Propuesta X: una feria con un stand de cada curso, abierta a todos. Propuesta Y: una feria solo para quienes pagan entrada alta. ¿Cuál respeta mejor la inclusión? A) X B) Y", "A", "No deja afuera por dinero."),
    ],
    Z=[
        ex("¿Por qué una propuesta con la suma más alta puede no ser la mejor si excluye a alguien?", "Porque vulnera la dignidad y la inclusión", "Un derecho no se compensa con otros puntos."),
        ex("Dos propuestas empatan en puntos. ¿Qué conviene hacer? A) Revisar consecuencias y escuchar a las personas afectadas B) Tirar una moneda.", "A", "Hay información que falta."),
    ],
    D=[
        arith("El curso recauda $2.000 por semana durante 8 semanas. ¿Cuántos pesos reúne?", "2000*8", "Se multiplican los pesos por las semanas.", " pesos"),
        arith("Una actividad cuesta $36.000 y la pagan 30 estudiantes por partes iguales. ¿Cuánto paga cada uno?", "36000//30", "Se divide el costo total entre los estudiantes.", " pesos"),
    ],
    context=[ex("El curso debe elegir entre un paseo caro que solo pueden pagar algunos y una jornada deportiva gratuita para todos. ¿Qué propuesta cumple mejor la inclusión? A) La jornada gratuita B) El paseo caro.", "A", "Permite que todos participen.")],
    selfcheck=[ex("En Orientación: ¿comparar propuestas requiere criterios?", "Sí", "Orden y justicia al decidir."), ex("¿Una propuesta que excluye puede aceptarse solo por ser barata?", "No", "Vulnera la inclusión."), ex("¿Las consecuencias a largo plazo importan?", "Sí", "Afectan la convivencia.")],
    task=T("Lee las tres propuestas inventadas de un curso: (1) «Una radio escolar con un horario para cada curso»; (2) «Un torneo de fútbol solo para el equipo del colegio»; (3) «Un huerto con turnos mixtos». Haz una tabla con cinco criterios (dignidad, inclusión, equidad de género, bienestar, factibilidad), marca sí o no con un dato y concluye cuál recomendarías y por qué.", "Radio: cumple 4, factibilidad dudosa. Torneo: no incluye ni da equidad. Huerto: cumple los 5. Recomiendo el huerto porque incluye y es factible.", ["completa la tabla", "justifica con un dato", "da una conclusión", "no excluye a nadie"], ["tabla escrita", "texto oral"], ["marcar sin dato", "sumar sin mirar la exclusión"], "Reconoce los criterios aplicados y pregunta qué dato falta en el menos claro."),
    reinforce="Compara dos actividades de curso con tres criterios.",
    extend="Explica por qué un criterio puede pesar más que la suma de puntos.",
)

lesson(
    OA7, 4,
    "Una hoja y un lápiz. El mapa de actores del colegio inventado está escrito en los ejercicios.",
    "Aprenderé a elegir una forma pacífica, segura y democrática de llevar adelante una propuesta, identificando a los actores y las instancias. Sirve para que mi participación sea efectiva y cuidadosa.",
    ["Sé comparar propuestas con criterios.", "Sé distinguir competencias."],
    [
        "Un mapa de actores muestra quién influye en un problema o puede ayudar a resolverlo. Los actores en un colegio pueden ser: el curso, la directiva, el profesor jefe, la dirección, el Centro de Estudiantes, el equipo de convivencia escolar y las familias. En el barrio: la junta de vecinos, la municipalidad, la biblioteca. Para cada actor conviene anotar qué hace, qué necesita y cómo se le contacta.",
        "Una acción segura de participación es pacífica, respeta los canales formales, protege la privacidad y es acompañada. Ejemplos: presentar una carta firmada por el curso a la dirección, pedir una reunión con el Centro de Estudiantes, hacer una campaña de afiches con permiso. No son acciones seguras: tomarse espacios sin avisar, publicar fotos de personas sin permiso, juntar datos personales sin cuidado o insultar a autoridades en redes.",
        "Una vez elegida la acción, se define quién hace qué, para cuándo y cómo se revisará. Si algo sale mal o hay conflicto, se pide apoyo a un adulto, como el profesor jefe. Participar de forma segura protege a las personas y mejora la probabilidad de lograr el cambio.",
    ],
    [("mapa de actores", "esquema de quién influye o puede ayudar en un problema"), ("canal formal", "vía oficial para presentar propuestas, como una carta o una reunión"), ("acción pacífica", "acción que no daña a personas ni bienes"), ("firma colectiva", "lista de apoyo de varias personas a una propuesta"), ("responsable", "persona que se encarga de una tarea")],
    [
        W("Elegir actor", "El curso quiere más basureros. ¿A quién contacta primero?", ["Al profesor jefe y a la directiva.", "Luego a la dirección."], "Al profesor jefe y a la directiva del curso"),
        W("Acción segura", "Opción A: una carta firmada por el curso a la dirección. Opción B: subir fotos de los baños sucios con rostros de estudiantes. ¿Cuál es segura?", ["A usa un canal formal.", "B expone a personas."], "La opción A"),
    ],
    [
        M("Creer que una acción llamativa es mejor que una pacífica.", "Se confunde atención con efectividad.", "Las acciones pacíficas y formales suelen lograr más y no dañan."),
        M("Juntar datos personales sin cuidado para una petición.", "Se cree que más firmas con datos es mejor.", "Pide solo nombre y curso con consentimiento y guárdalo bien."),
    ],
    R=[
        ex("Un curso quiere presentar su propuesta. ¿Cuál es un canal formal? A) Una carta firmada por el curso a la dirección B) Un mensaje anónimo contra la dirección en redes", "A", "Es una vía oficial para presentar una propuesta."),
        ex("Al reunir firmas, ¿cuál es una acción segura? A) Pedir solo nombre y curso, con consentimiento B) Publicar fotos de quienes no quisieron firmar", "A", "Protege la privacidad."),
        ex("¿Para qué sirve un mapa de actores? A) Para ver quién influye o puede ayudar en un problema B) Para decidir quién gana una votación", "A", "Ordena a las personas e instancias que pueden ayudar."),
    ],
    U=[
        ex("¿Qué acción es pacífica? A) Pedir una reunión con el Centro de Estudiantes B) Tomarse el patio sin avisar.", "A", "Respeta los canales y no daña."),
        ex("¿Quién puede ayudar si hay un conflicto al llevar adelante una propuesta? A) El profesor jefe B) Nadie, es un secreto.", "A", "Un adulto acompaña y media."),
        ex("¿Qué debe tener una acción una vez elegida? A) Responsables, plazo y revisión B) Solo entusiasmo.", "A", "Así se puede cumplir."),
    ],
    A=[
        ex("Mapa de actores inventado: curso, directiva, profesor jefe, dirección, Centro de Estudiantes, familias, junta de vecinos. ¿Cuántos son del colegio (sin contar familias ni junta de vecinos)?", "5", "Curso, directiva, profesor jefe, dirección y Centro de Estudiantes."),
        ex("Clasifica con S (segura) o N (no segura): 1) carta con firmas de nombre y curso; 2) tomarse el pasillo; 3) pedir reunión con la dirección. Escribe las letras en orden.", "S, N, S", "La 1 y la 3 usan canales formales; la 2 es una toma sin aviso."),
        ex("Una campaña de afiches para pedir sombra en el patio. ¿Qué primero? A) Pedir permiso a la dirección para pegarlos B) Pegarlos en todas las paredes sin avisar.", "A", "Respeta las normas del colegio."),
    ],
    Z=[
        ex("¿Por qué conviene que una acción de participación esté acompañada por un adulto?", "Porque ayuda a orientar y resolver conflictos", "El adulto da apoyo y respaldo."),
        ex("Un curso quiere presionar con insultos en redes a una autoridad. ¿Qué consecuencia es probable? A) Que se cierre el diálogo y se dañe a personas B) Que se resuelva mejor.", "A", "Los insultos bloquean el diálogo."),
    ],
    D=[
        arith("Para una petición, el curso recoge 3 firmas por cada integrante de 12 comisiones. ¿Cuántas firmas son?", "3*12", "Se multiplican firmas por comisiones."),
        arith("De 150 estudiantes, 96 firman una petición. ¿Cuántos no firman?", "150-96", "Al total se le restan los que firman."),
    ],
    context=[ex("Tu curso quiere pedir arreglar las bancas rotas. ¿Qué plan es seguro? A) Enviar una carta a la dirección con fotos de las bancas, sin personas B) Romper más bancas para mostrar el problema.", "A", "Es pacífica y no expone a nadie.")],
    selfcheck=[ex("En Orientación: ¿una acción pacífica evita dañar personas y bienes?", "Sí", "Es una de sus condiciones."), ex("¿Un canal formal es una vía oficial?", "Sí", "Por ejemplo, una carta."), ex("¿Se acompaña la acción con un adulto?", "Sí", "Ayuda a orientar.")],
    task=T("Lee el caso inventado: el curso 1.º C quiere que se instale sombra en el patio. Los actores son el curso, la directiva, el profesor jefe, la dirección, el Centro de Estudiantes y las familias. Escribe un mapa con tres actores, la acción segura que elegirías, el responsable de cada paso, el plazo y la revisión.", "Actores: directiva, profesor jefe, dirección. Acción: carta firmada a la dirección con datos de la falta de sombra. Responsables: Pedro redacta, Camila reúne firmas de nombre y curso. Plazo: dos semanas. Revisión: reunión de la directiva a la semana.", ["nombra tres actores", "elige una acción segura y pacífica", "asigna responsables, plazo y revisión", "no usa datos personales reales"], ["plan escrito", "tabla"], ["acción sin canal formal", "pasos sin responsable"], "Reconoce el plan claro y pregunta qué haría si no hubiera respuesta."),
    reinforce="Escribe tres actores que pueden ayudar a resolver el problema de un baño sin jabón.",
    extend="Explica por qué una acción pacífica suele lograr más que una acción dañina.",
)

lesson(
    OA7, 5,
    "Una hoja y un lápiz. La estructura de la carta y el esquema de intervención están escritos en los ejercicios; usa personas inventadas.",
    "Aprenderé a comunicar una propuesta por carta y en una asamblea, con datos, respeto y turnos. Sirve para que mi voz se escuche y para recibir y responder opiniones distintas.",
    ["Sé elegir una acción segura y pacífica.", "Sé que debo respetar los turnos."],
    [
        "Una carta de propuesta tiene cinco partes: saludo, presentación (quiénes escriben), problema con un dato, propuesta concreta y despedida con agradecimiento. Por ejemplo: «Estimada directora: somos el curso 1.º C. En el patio hay 2 bancas para 40 estudiantes. Proponemos instalar 4 bancas más. Agradecemos su atención». Es breve y respetuosa, sin acusar ni exigir.",
        "En una asamblea o Consejo de Curso, las reglas son: pedir la palabra, hablar sin interrumpir, hablar solo del tema, escuchar para entender y no solo para responder. Una intervención clara tiene una idea, un dato y una petición. Cuando alguien piensa distinto, se puede decir: «Entiendo tu punto, yo pienso que…». Se critica la idea y no a la persona.",
        "Si la propuesta recibe respuestas negativas, se pregunta por qué y se ajusta. Escuchar objeciones mejora la propuesta. Y si hay faltas de respeto, quien modera la asamblea pide volver al diálogo o avisa a un adulto.",
    ],
    [("propuesta", "idea concreta de acción para resolver un problema"), ("asamblea", "reunión de un grupo para conversar y decidir"), ("moderador", "persona que da la palabra y cuida las reglas"), ("objeción", "razón que se da en contra de una propuesta"), ("intervención", "momento en que una persona habla en una reunión")],
    [
        W("Ordenar la carta", "Ordena las partes de la carta: problema con dato, saludo, propuesta, presentación, despedida.", ["Primero el saludo.", "Luego la presentación.", "Después el problema con dato.", "Después la propuesta.", "Al final la despedida."], "Saludo, presentación, problema, propuesta y despedida"),
        W("Responder con respeto", "Alguien dice: «Tu idea no sirve». Reformula una respuesta respetuosa.", ["Entiende la objeción.", "Pregunta por la razón."], "«Entiendo que dudas. ¿Qué parte no te convence?»"),
    ],
    [
        M("Escribir una carta con acusaciones y sin propuesta.", "Se enfoca el enojo en vez de la solución.", "Incluye un dato, una propuesta concreta y un agradecimiento."),
        M("Hablar sin pedir la palabra porque «es urgente».", "Se confunde urgencia con derecho a interrumpir.", "Pide la palabra al moderador."),
    ],
    R=[
        ex("En una carta de propuesta aparece: «En el gimnasio hay 3 ampolletas quemadas». ¿Qué parte es? A) El problema con un dato B) La despedida", "A", "Describe el problema con un dato comprobable."),
        ex("Un estudiante quiere hablar en el Consejo de Curso. ¿Qué hace primero? A) Pedir la palabra al moderador B) Hablar más fuerte que los demás", "A", "Evita que se interrumpan."),
        ex("Un compañero propone algo que no te convence. ¿Cuál es la forma respetuosa de responder? A) Criticar la idea y explicar tu razón B) Burlarte de quien la propuso", "A", "Respeta la dignidad de la persona."),
    ],
    U=[
        ex("¿Cuál es la mejor frase para discrepar? A) «Entiendo tu punto; yo pienso que…» B) «Eso es una tontería.»", "A", "Reconoce al otro y expresa la propia idea."),
        ex("¿Qué parte de la carta propone una acción? A) La propuesta concreta B) El saludo.", "A", "Dice qué se pide hacer."),
        ex("¿Qué debe hacer el moderador? A) Dar la palabra y cuidar las reglas B) Hablar más que nadie.", "A", "Es su función."),
    ],
    A=[
        ex("Carta de ejemplo: «Estimada directora: somos el curso 1.º C. Hay 2 bebederos para 300 estudiantes. Proponemos instalar 3 bebederos más. Gracias». ¿Cuál es la propuesta concreta? A) Instalar 3 bebederos más B) Que haya mejoras.", "A", "Es la acción específica pedida."),
        ex("Carta de ejemplo: «Hay 2 bebederos para 300 estudiantes». Si se agregan 3 bebederos, ¿cuántos habrá?", "5", "2 más 3 son 5 bebederos."),
        ex("Una compañera critica tu propuesta con una objeción válida. ¿Qué haces? A) Preguntar y ajustar la propuesta B) Ignorarla.", "A", "Mejora el resultado."),
    ],
    Z=[
        ex("¿Por qué conviene incluir un dato en la carta?", "Porque muestra que el problema es real y comprobable", "Un dato sustenta la propuesta."),
        ex("Un moderador interrumpe a quien insulta y pide volver al tema. ¿Qué cuida? A) El respeto y el diálogo B) Su propia opinión.", "A", "Mantiene las reglas."),
    ],
    D=[
        arith("En una asamblea de 36 estudiantes, cada intervención dura 2 minutos y hay 9 intervenciones. ¿Cuántos minutos duran en total?", "2*9", "Se multiplican minutos por intervenciones.", " minutos"),
        arith("Una carta se imprime en 4 copias de 2 hojas. ¿Cuántas hojas se usan?", "4*2", "Se multiplican copias por hojas."),
    ],
    context=[ex("En el Consejo de Curso, Vero pide la palabra, plantea el problema del ruido en la biblioteca con un dato y propone un horario de silencio. ¿Qué hizo bien? A) Siguió las reglas y propuso algo concreto B) Impuso su idea.", "A", "Pidió la palabra y usó un dato.")],
    selfcheck=[ex("En Orientación: ¿una carta tiene saludo y despedida?", "Sí", "Sigue una estructura."), ex("¿Se critica la idea y no a la persona?", "Sí", "Respeta la dignidad."), ex("¿Escuchar objeciones puede mejorar la propuesta?", "Sí", "Aporta información nueva.")],
    task=T("Redacta una carta de cinco partes para pedir que el recreo de tu curso tenga un espacio de sombra, usando el dato inventado de que hay 1 toldo para 120 estudiantes. Después escribe una frase para discrepar con respeto si alguien dice «no hay presupuesto».", "Estimada directora: somos el curso 1.º C. Hay 1 toldo para 120 estudiantes. Proponemos instalar 2 toldos más. Agradecemos su atención. Frase: «Entiendo que el presupuesto es limitado; ¿podemos conversar opciones más baratas?».", ["incluye las cinco partes", "incluye un dato y una propuesta concreta", "escribe una frase para discrepar con respeto", "no acusa ni insulta"], ["carta escrita", "texto oral"], ["carta sin propuesta", "frase que ataca a la persona"], "Reconoce las partes bien escritas y pregunta cuál dato daría más fuerza."),
    reinforce="Ordena las cinco partes de una carta con tus palabras.",
    extend="Explica por qué escuchar objeciones puede mejorar una propuesta.",
)

lesson(
    OA7, 6,
    "Una hoja y un lápiz. La plantilla de acuerdo y los casos del barrio inventado están escritos en los ejercicios.",
    "Aprenderé a transferir lo aprendido a una situación nueva en el barrio y a escribir un acuerdo con responsables, plazo y revisión. Sirve para participar fuera del colegio sin exponer mi vida personal.",
    ["Sé usar mapa de actores y acciones seguras.", "Sé redactar propuestas con datos."],
    [
        "Transferir es usar lo aprendido en un caso nuevo. Imagina un barrio inventado: la plaza tiene luces quemadas, juegos rotos y poca limpieza. Los actores pueden ser la junta de vecinos, la municipalidad, la biblioteca, los clubes deportivos y las familias. Se aplica la misma secuencia: entender el problema con hechos, identificar a quienes afecta, comparar propuestas con criterios, elegir una acción segura y comunicarla.",
        "En el barrio, los valores de la participación son los mismos: respetar la dignidad de todos, incluir a distintas edades y personas con discapacidad, cuidar la equidad de género en el uso de espacios, buscar la justicia y el bienestar. Una plaza inclusiva tiene luz, rampas, bancas y juegos para diversas edades.",
        "Un acuerdo con responsables, plazo y revisión es la herramienta para concretar: «Qué: pedir reparación de luces. Quién: Sofía y Lucas. Plazo: el 15. Revisión: reunión de vecinos el 22». Una iniciativa segura es acompañada por personas adultas, respeta la privacidad y no pone a nadie en riesgo.",
    ],
    [("barrio", "zona cercana donde viven y conviven las personas"), ("iniciativa", "acción propuesta para mejorar algo"), ("junta de vecinos", "organización de vecinos que trata los problemas del barrio"), ("accesibilidad", "posibilidad de que todas las personas usen un espacio"), ("revisión", "momento para comprobar si lo acordado se cumplió")],
    [
        W("Aplicar la secuencia al barrio", "Caso: las luces de la plaza están quemadas hace 3 semanas. ¿Cuál es el hecho y a quién puede contactar el curso?", ["El hecho es que las luces están quemadas hace 3 semanas.", "Puede contactar a la junta de vecinos y a la municipalidad."], "Hecho: luces quemadas hace 3 semanas; contactos: junta de vecinos y municipalidad"),
        W("Redactar el acuerdo", "Redacta un acuerdo para pedir arreglar las luces.", ["Qué: carta a la municipalidad.", "Quién: Sofía y Lucas.", "Plazo: 15 días.", "Revisión: reunión de vecinos al final."], "Acuerdo con qué, quién, plazo y revisión"),
    ],
    [
        M("Pensar que en el barrio todo se hace sin adultos.", "Se olvida la seguridad y las competencias.", "Una iniciativa segura se acompaña de adultos."),
        M("Hacer una iniciativa pensando solo en un grupo de edad.", "Se olvida la inclusión.", "Considera distintas edades y capacidades."),
    ],
    R=[
        ex("Una plaza tiene escalones y ninguna rampa. ¿Qué valor falla? A) La inclusión, porque personas con discapacidad no pueden entrar B) La puntualidad", "A", "No todas las personas pueden usar el espacio."),
        ex("Un acuerdo dice: «Sofía lleva la carta. Plazo: el viernes». ¿Qué parte le falta? A) La revisión B) El plazo", "A", "Tiene responsable, conducta y plazo, pero no dice cómo se comprobará."),
        ex("¿Quién debe acompañar una iniciativa de barrio de estudiantes de 1.º medio? A) Una persona adulta, por ejemplo de la junta de vecinos o de una familia B) Nadie, para hacerlo más rápido", "A", "El acompañamiento adulto protege a quienes participan."),
    ],
    U=[
        ex("¿Qué valor cuida una plaza con juegos para distintas edades? A) La inclusión B) El ruido.", "A", "Permite que más personas participen."),
        ex("¿Qué debe decir la revisión de un acuerdo? A) Cuándo se comprueba si se cumplió B) Quién fue culpable.", "A", "Permite ajustar lo acordado."),
        ex("¿Cuál es una condición de una iniciativa segura en el barrio? A) Que la acompañen personas adultas B) Que se mantenga en secreto", "A", "Protege a quienes participan."),
    ],
    A=[
        ex("Plan de ejemplo: «Sofía y Lucas llevan una carta a la municipalidad el lunes; la junta de vecinos revisa el viernes». ¿Cuántas personas o grupos tienen una tarea?", "3", "Sofía, Lucas y la junta de vecinos."),
        ex("Clasifica con S (segura) o N (no segura): 1) pedir una reunión con la junta de vecinos; 2) subir fotos con rostros de niños jugando; 3) enviar una carta con una descripción del problema. Escribe las letras en orden.", "S, N, S", "La 1 y la 3 usan canales formales; la 2 expone a niños."),
        ex("Una plaza tiene 12 juegos y 5 están rotos. ¿Cuántos funcionan?", "7", "12 menos 5 son 7."),
    ],
    Z=[
        ex("¿Por qué conviene considerar a personas de distintas edades en una iniciativa de barrio?", "Porque así el espacio sirve a todos y no excluye", "La inclusión requiere pensar en varios grupos."),
        ex("Un vecino dice: «Con la queja en redes basta». ¿Qué falta? A) Una propuesta concreta presentada a quien decide B) Más enojo.", "A", "La queja sola no cambia nada."),
    ],
    D=[
        arith("Una plaza tiene 8 luminarias y 3 están quemadas. Si se arreglan 2, ¿cuántas quedan sin arreglar?", "3-2", "A las quemadas se les restan las arregladas."),
        arith("Una jornada de limpieza dura 3 horas con 15 voluntarios. ¿Cuántas horas de trabajo suman en total?", "3*15", "Se multiplican horas por voluntarios.", " horas"),
    ],
    context=[ex("Un grupo del curso quiere organizar una jornada de limpieza en la plaza. ¿Qué es lo primero que deben hacer? A) Contactar a la junta de vecinos y pedir acompañamiento adulto B) Ir sin avisar a nadie.", "A", "Es una acción segura y con apoyo.")],
    selfcheck=[ex("En Orientación: ¿una iniciativa de barrio debe incluir a distintas edades?", "Sí", "Se busca inclusión."), ex("¿Un acuerdo tiene responsables y plazo?", "Sí", "Así se cumple."), ex("¿Se necesita acompañamiento adulto en una iniciativa del barrio?", "Sí", "Protege a los participantes.")],
    task=T("Un barrio inventado tiene una plaza con las luces quemadas, la rampa rota y pocas bancas. Elige uno de los tres problemas y redacta un plan con: un hecho, tres actores, una acción segura, responsables, plazo y revisión, y un valor que cuida (dignidad, inclusión, equidad de género, justicia o bienestar).", "Problema: rampa rota. Hecho: la rampa está rota hace un mes. Actores: junta de vecinos, municipalidad, biblioteca. Acción: carta firmada. Responsables: Ema y Pedro. Plazo: 15 días. Revisión: reunión de vecinos. Valor: inclusión.", ["elige un problema y da un hecho", "nombra tres actores", "define responsables, plazo y revisión", "nombra un valor"], ["plan escrito", "tabla"], ["acción sin plazo", "olvidar el valor"], "Reconoce el plan completo y pregunta qué ajustaría si la carta no recibe respuesta."),
    reinforce="Escribe tres actores que ayudarían a arreglar una plaza.",
    extend="Explica cómo la accesibilidad es parte de la inclusión.",
)

# ================================================================ OA 08
lesson(
    OA8, 1,
    "Una hoja y un lápiz. El acta del Consejo de Curso de 1.º A, con tres iniciativas, está escrita en los ejercicios; es ficticia.",
    "Aprenderé a examinar iniciativas de un curso y a distinguir si promueven el respeto, la justicia, el buen trato, las relaciones pacíficas o el bien común. Sirve para elegir acciones que mejoren la convivencia.",
    ["Sé participar en un Consejo de Curso (OA 07).", "Sé distinguir hechos y opiniones."],
    [
        "El buen trato es tratar a los demás con respeto, cuidado y consideración. La justicia es dar a cada persona el trato que le corresponde, considerando sus necesidades; por ejemplo, la equidad no significa dar lo mismo a todos, sino dar a cada uno lo que necesita para participar en igualdad. Las relaciones pacíficas resuelven conflictos sin violencia. El bien común es lo que beneficia a todo el grupo, no solo a algunos.",
        "Una iniciativa es una acción que un grupo propone para mejorar algo. Por ejemplo, una campaña de buen trato, un reglamento de turnos de cancha o una colecta solidaria. Para examinarla se pregunta: ¿qué problema resuelve?, ¿a quiénes beneficia?, ¿respeta la dignidad de todos?, ¿se puede hacer?, ¿cómo se decide?",
        "Las instancias colectivas, como el Consejo de Curso y los órganos de representación estudiantil, permiten decidir de manera colaborativa y democrática. Allí se dialoga, se debate con respeto y se vota o se busca consenso. Todas las opiniones valen, aunque no todas se aprueben.",
    ],
    [("buen trato", "trato respetuoso, cuidadoso y considerado"), ("justicia", "dar a cada persona lo que corresponde según sus necesidades"), ("equidad", "dar a cada persona lo que necesita para participar en igualdad"), ("bien común", "lo que beneficia a todo el grupo"), ("iniciativa", "acción propuesta por un grupo para mejorar algo")],
    [
        W("Clasificar iniciativas", "Una iniciativa propone una colecta de útiles para estudiantes que los necesitan. ¿Qué valor promueve principalmente?", ["Ayuda a quien lo necesita.", "Busca justicia y bien común."], "Justicia y bien común"),
        W("Equidad", "Hay dos estudiantes: Ema y Beto. Ema necesita una rampa para ingresar a la sala; Beto no. ¿Dar la misma ayuda a los dos es justo?", ["Ema necesita algo distinto.", "La equidad da a cada uno lo que necesita."], "No; la equidad pide la rampa para Ema"),
    ],
    [
        M("Creer que justicia es dar exactamente lo mismo a todos.", "Se confunde igualdad con equidad.", "Justicia considera las necesidades de cada persona."),
        M("Pensar que bien común es lo que gusta a la mayoría.", "Se ignora a las minorías.", "El bien común considera a todo el grupo."),
    ],
    R=[
        ex("¿Cuál es una conducta de buen trato? A) Saludar y agradecer a quien limpia la sala B) Burlarse de quien se equivoca", "A", "Trata con respeto y consideración."),
        ex("Dos cursos discuten por la cancha. ¿Cuál es una forma pacífica de resolverlo? A) Conversar y acordar turnos B) Quitarse la pelota a empujones", "A", "Se resuelve con diálogo y sin violencia."),
        ex("¿Cuál iniciativa busca el bien común? A) Cuidar la biblioteca que usa todo el colegio B) Reservar una sala solo para el grupo de un curso", "A", "Beneficia a todo el grupo y no solo a algunos."),
    ],
    U=[
        ex("Una iniciativa busca que todas las voces se escuchen antes de decidir. ¿Qué promueve? A) La participación democrática B) La competencia", "A", "Decide escuchando a todas las personas."),
        ex("¿Cuál es un ejemplo de equidad? A) Dar un apoyo extra a quien lo necesita para participar B) Dar lo mismo a todos sin mirar necesidades.", "A", "Atiende necesidades distintas."),
        ex("Una colecta solidaria entre todos los cursos, ¿qué valor promueve? A) El bien común B) La competencia.", "A", "Beneficia a la comunidad."),
    ],
    A=[
        ex("Acta de ejemplo con tres iniciativas: 1) campaña de buen trato; 2) turnos para usar la cancha entre todos los cursos; 3) colecta solidaria. ¿Cuál se enfoca en repartir un recurso compartido de manera justa?", "La 2", "Reparte turnos de un espacio común."),
        ex("En una votación del Consejo de Curso de 32 estudiantes, 20 votan por la campaña de buen trato. ¿Cuántos no votan por ella?", "12", "32 menos 20 son 12."),
        ex("Una iniciativa propone que solo los estudiantes con buen rendimiento usen la sala de computación. ¿Qué valor falla? A) La justicia y la inclusión B) La puntualidad.", "A", "Excluye según un criterio que no corresponde."),
    ],
    Z=[
        ex("¿Por qué una iniciativa que beneficia a la mayoría puede no ser buena para el bien común?", "Porque puede dañar o excluir a un grupo pequeño", "El bien común considera a todos."),
        ex("Un compañero dice: «Mi iniciativa es la mejor porque a mí me gusta». ¿Qué le falta? A) Mostrar a quiénes beneficia y qué problema resuelve B) Más votos.", "A", "Una iniciativa se fundamenta en el problema y las personas."),
    ],
    D=[
        arith("En un Consejo de 40 estudiantes, se aprueban 3 iniciativas con 28, 31 y 35 votos a favor. ¿Cuántos votos a favor suman en total?", "28+31+35", "Se suman los votos de las tres."),
        arith("De una colecta de útiles, 45 estudiantes aportan 2 lápices cada uno. ¿Cuántos lápices reúnen?", "45*2", "Se multiplican estudiantes por lápices."),
    ],
    context=[ex("El Consejo de Curso discute dos iniciativas: una competencia para ver qué curso es mejor y una jornada de juegos mixtos para conocerse. ¿Cuál promueve más el buen trato? A) La jornada de juegos mixtos B) La competencia.", "A", "Favorece la convivencia.")],
    selfcheck=[ex("En Orientación: ¿la justicia considera las necesidades de cada persona?", "Sí", "Esa es la equidad."), ex("¿El bien común beneficia solo a algunos?", "No", "Debe considerar a todo el grupo."), ex("¿El Consejo de Curso permite decidir de manera democrática?", "Sí", "Se dialoga y se vota.")],
    task=T("Lee las tres iniciativas inventadas de un Consejo de Curso: (a) «Cada viernes, un compañero distinto saluda por turnos a todo el curso con una frase amable»; (b) «Solo los estudiantes que ganen el torneo usan la cancha»; (c) «Una colecta de abrigos en invierno, abierta a todo el colegio». Clasifica cada una según promueva buen trato, justicia o bien común, o falle en alguno, y justifica con una frase.", "(a) Buen trato: favorece el saludo respetuoso. (b) Falla en justicia: excluye. (c) Bien común y justicia: ayuda a quien lo necesita.", ["clasifica las tres iniciativas", "justifica con una frase", "distingue justicia de exclusión", "no usa nombres reales"], ["tabla escrita", "texto oral"], ["confundir equidad con igualdad", "justificar la exclusión"], "Reconoce las iniciativas bien clasificadas y pregunta cómo mejoraría la (b)."),
    reinforce="Escribe una iniciativa que promueva el buen trato en tu curso.",
    extend="Explica la diferencia entre justicia y dar lo mismo a todos.",
)

lesson(
    OA8, 2,
    "Una hoja y un lápiz. Las reglas de debate y los argumentos del Consejo de Curso, con personas inventadas, están escritos en los ejercicios.",
    "Aprenderé a distinguir hechos, argumentos y ataques personales en un debate, y a reconocer los derechos y límites al opinar. Sirve para debatir con respeto cuando hay opiniones distintas.",
    ["Sé que opinar es un derecho.", "Sé distinguir hechos de opiniones."],
    [
        "En un debate respetuoso hay reglas: pedir la palabra, no interrumpir, hablar sobre el tema, justificar con razones y escuchar. Un argumento es una razón que apoya una idea; puede apoyarse en un hecho, como un dato, o en un valor, como la justicia. Un ataque personal, en cambio, critica a la persona en vez de la idea: «tú siempre propones tonteras». No es un argumento y rompe el diálogo.",
        "Algunos errores comunes al argumentar: generalizar apresuradamente («todos dicen que es mala idea»), apelar a la mayoría («la mayoría lo hace, entonces es correcto»), o atacar a la persona. Un buen argumento tiene tres partes: una afirmación, una razón y un dato o ejemplo. Por ejemplo: «Propongo turnos de cancha (afirmación), porque así todos los cursos pueden jugar (razón); hoy solo juega un curso (dato)».",
        "Los derechos en un debate son: opinar, ser escuchado y no ser humillado. Los límites son los insultos, las amenazas y la desinformación. Cuando alguien cruza el límite, quien modera pide volver al respeto; si continúa, se informa a un adulto. Respetar a quien piensa distinto es parte de la participación democrática.",
    ],
    [("argumento", "razón con que se apoya una idea"), ("ataque personal", "crítica a la persona en vez de a la idea"), ("generalización", "decir que algo vale para todos sin comprobarlo"), ("moderador", "persona que da la palabra y cuida las reglas"), ("desinformación", "información falsa o engañosa")],
    [
        W("Argumento o ataque", "«Tu propuesta no considera a quienes no pueden pagar» y «tú siempre propones tonteras». ¿Cuál es argumento?", ["La primera critica la idea con una razón.", "La segunda critica a la persona."], "La primera"),
        W("Armar un argumento", "Arma un argumento con afirmación, razón y dato sobre turnos de cancha.", ["Afirmación: propongo turnos.", "Razón: así todos pueden jugar.", "Dato: hoy solo juega un curso."], "«Propongo turnos porque así todos pueden jugar; hoy solo juega un curso.»"),
    ],
    [
        M("Creer que un debate se gana humillando al otro.", "Se confunde ganar con imponer.", "Un debate busca entender y decidir mejor."),
        M("Creer que si muchos lo dicen, es verdad.", "Se confunde cantidad con prueba.", "Pide un dato que lo respalde."),
    ],
    R=[
        ex("Alguien dice: «Tú siempre arruinas las reuniones». ¿Qué es esa frase? A) Un ataque personal B) Un argumento", "A", "Critica a la persona y no da una razón sobre la idea."),
        ex("¿Cuál es una regla de un debate respetuoso? A) Pedir la palabra y no interrumpir B) Hablar todos a la vez", "A", "Permite que todas las voces se escuchen."),
        ex("¿Cuál es un límite al opinar en un debate? A) Insultar o amenazar B) Dar un dato", "A", "Los insultos y amenazas dañan la dignidad."),
    ],
    U=[
        ex("¿Cuál es un argumento? A) «Propongo turnos porque hoy solo juega un curso.» B) «Eres un flojo.»", "A", "Da una razón y un dato."),
        ex("«La mayoría lo hace, entonces está bien». ¿Qué error tiene? A) Apela a la mayoría como prueba B) Es muy corto.", "A", "La cantidad no demuestra que algo sea correcto."),
        ex("¿Qué derecho se cuida cuando se escucha a todos? A) El derecho a ser escuchado B) El derecho a ganar.", "A", "Es parte del respeto democrático."),
    ],
    A=[
        ex("Clasifica con A (argumento) o P (ataque personal): 1) «Los turnos evitan peleas por la cancha»; 2) «Tú nunca piensas»; 3) «Hoy solo juega un curso». Escribe las letras en orden.", "A, P, A", "La 1 y la 3 dan razones y datos; la 2 ataca."),
        ex("Un compañero dice: «Todos dicen que la idea es mala». ¿Qué error tiene? A) Generaliza sin datos B) Es un dato comprobado.", "A", "No dice quiénes ni por qué."),
        ex("En un debate, Lucas interrumpe a Pía varias veces. ¿Qué regla incumple? A) No interrumpir B) Hablar sobre el tema.", "A", "Debe esperar su turno."),
    ],
    Z=[
        ex("¿Por qué un ataque personal no ayuda a decidir bien?", "Porque no da razones sobre la idea", "Desvía la atención de la propuesta."),
        ex("Un debate se vuelve muy tenso. ¿Qué hace el moderador? A) Pide volver al respeto y a las reglas B) Gritar más fuerte.", "A", "Mantiene el diálogo."),
    ],
    D=[
        arith("En un debate de ejemplo hay 6 intervenciones de 2 minutos y 3 de 3 minutos. ¿Cuántos minutos duran en total?", "6*2+3*3", "Se suman los minutos de ambos tipos."),
        arith("De 30 estudiantes, 22 escuchan sin interrumpir y el resto interrumpe. ¿Cuántos interrumpen?", "30-22", "Al total se le restan los que no interrumpen."),
    ],
    context=[ex("Nicolás propone un horario de silencio en la sala de estudio. Camila responde: «Esa idea es de Nicolás, seguro es mala». ¿Qué error tiene? A) Ataca a la persona en vez de la idea B) Da un dato.", "A", "No analiza la propuesta.")],
    selfcheck=[ex("En Orientación: ¿un argumento tiene una razón?", "Sí", "Apoya la idea."), ex("¿Un ataque personal es un argumento válido?", "No", "No da razones sobre la idea."), ex("¿Todas las opiniones tienen derecho a ser escuchadas?", "Sí", "Es parte del respeto.")],
    task=T("Lee las cuatro frases inventadas de un debate sobre los recreos: (a) «Propongo un recreo más largo porque 15 minutos no alcanzan para comer y jugar»; (b) «Quien quiera un recreo largo no sabe nada»; (c) «Todos los cursos lo quieren»; (d) «Entiendo tu idea, pero el horario no se puede cambiar por el reglamento». Clasifica cada una como argumento con razón, ataque personal, generalización o respuesta respetuosa, y reescribe (b) como un argumento.", "(a) Argumento con razón. (b) Ataque personal. (c) Generalización. (d) Respuesta respetuosa con razón. Reescritura de (b): «No estoy de acuerdo con un recreo más largo porque quita tiempo de clases».", ["clasifica las cuatro frases", "reescribe (b) como argumento", "distingue ataque de argumento", "no insulta"], ["tabla escrita", "texto oral"], ["llamar argumento a un ataque", "olvidar la razón"], "Reconoce lo bien clasificado y pregunta qué dato apoyaría el argumento."),
    reinforce="Escribe un argumento con afirmación, razón y dato sobre cualquier propuesta inventada del curso.",
    extend="Explica por qué la generalización puede ser un error al argumentar.",
)

lesson(
    OA8, 3,
    "Una hoja y un lápiz. Los resultados de votación y los métodos de decisión están escritos en los ejercicios con datos de ejemplo.",
    "Aprenderé a comparar formas de decidir en un curso (votar por mayoría, buscar consenso y delegar) y sus consecuencias para la justicia y el bien común. Sirve para elegir el método adecuado.",
    ["Sé distinguir argumentos de ataques.", "Sé qué es una instancia democrática."],
    [
        "Un curso puede decidir de varias maneras. En la votación por mayoría se elige la opción con más votos; es rápida y clara, pero la minoría puede sentirse excluida. En el consenso se busca una decisión con la que todos puedan vivir; toma más tiempo, pero compromete a todos. Al delegar, se encarga la decisión a una persona o comisión, como la directiva; ahorra tiempo, pero requiere confianza y rendición de cuentas.",
        "Cada método tiene consecuencias. La mayoría puede aprobar algo que daña a una minoría, por lo que se necesita siempre respetar sus derechos básicos. El consenso puede tardar mucho o estancar el debate. Delegar sin informar puede generar desconfianza. Un buen curso combina: busca el consenso, vota si no se logra y informa lo decidido.",
        "Para elegir, mira tres cosas: la importancia del tema, el tiempo disponible y el efecto sobre las personas. Por ejemplo, para elegir el color del afiche basta una votación; para un reglamento de convivencia es mejor buscar consenso con todas las voces. En todos los casos, se respeta lo decidido y se puede revisar después.",
    ],
    [("votación por mayoría", "elegir la opción con más votos"), ("consenso", "decisión con la que todos pueden vivir"), ("delegar", "encargar una decisión a una persona o comisión"), ("minoría", "grupo con menos votos o menos personas"), ("rendición de cuentas", "informar al grupo lo que se hizo con la decisión delegada")],
    [
        W("Contar una mayoría", "Votan 30 estudiantes: 17 por la opción A y 13 por la B. ¿Qué opción gana por mayoría?", ["17 es mayor que 13.", "Gana A."], "La opción A"),
        W("Elegir el método", "El curso debe decidir el color del afiche y también un reglamento de convivencia. ¿Qué método conviene para cada uno?", ["El afiche es un tema simple: votación.", "El reglamento afecta a todos: consenso."], "Afiche: votación; reglamento: consenso"),
    ],
    [
        M("Creer que la mayoría siempre tiene la razón.", "Se confunde mayor número con justicia.", "La mayoría decide, pero respeta los derechos de la minoría."),
        M("Creer que el consenso exige que todos piensen igual.", "Se confunde acuerdo con unanimidad.", "Es una decisión con la que todos pueden vivir."),
    ],
    R=[
        ex("Votan 25 estudiantes: 14 por X y 11 por Y. ¿Qué opción gana por mayoría? A) X B) Y", "A", "14 es mayor que 11."),
        ex("Un curso conversa hasta lograr una decisión con la que todos pueden vivir. ¿Qué método usa? A) Consenso B) Votación por mayoría", "A", "Busca una decisión aceptable para todos."),
        ex("La directiva decide la compra de materiales y después informa al curso. ¿Qué método es? A) Delegar, con rendición de cuentas B) Consenso", "A", "Se encarga la decisión y luego se informa."),
    ],
    U=[
        ex("¿Qué ventaja tiene votar por mayoría? A) Es rápida y clara B) Garantiza que nadie quede en minoría.", "A", "Permite decidir pronto."),
        ex("¿Qué riesgo tiene delegar sin informar? A) Generar desconfianza B) Acelerar el consenso.", "A", "El grupo no sabe qué se decidió."),
        ex("¿Qué método suele comprometer más a todos? A) El consenso B) La imposición.", "A", "Busca una decisión aceptable para todos."),
    ],
    A=[
        ex("Votan 36 estudiantes: 21 por A, 10 por B y 5 se abstienen. ¿Cuántos votaron por una opción?", "31", "21 + 10 son 31; las 5 abstenciones no votan por opción."),
        ex("Un curso debe elegir el color de un afiche entre rojo, azul y verde con 33 votos: rojo 12, azul 11, verde 10. ¿Qué opción gana?", "Rojo", "Tiene más votos."),
        ex("Un reglamento de convivencia afecta a todos. ¿Qué método conviene más? A) Buscar consenso con todas las voces B) Delegar sin informar.", "A", "Afecta a todos y requiere compromiso."),
    ],
    Z=[
        ex("¿Por qué la mayoría debe respetar los derechos de la minoría?", "Porque ganar una votación no autoriza a dañar a otros", "La democracia protege a todas las personas."),
        ex("Un curso vota y gana una propuesta con 17 votos contra 15. ¿Qué conviene después? A) Escuchar a la minoría y revisar el efecto B) Ignorar a quienes perdieron.", "A", "Mejora la convivencia."),
    ],
    D=[
        arith("En una votación de 45 estudiantes, 28 votan por A y el resto por B. ¿Cuántos votan por B?", "45-28", "Al total se le restan los votos de A."),
        arith("Un consenso toma 3 reuniones de 25 minutos cada una. ¿Cuántos minutos se necesitan?", "3*25", "Se multiplican reuniones por minutos.", " minutos"),
    ],
    context=[ex("El Consejo de Curso debe decidir entre un paseo a la playa o a un museo. Votan 34 estudiantes: 19 por la playa y 15 por el museo. ¿Qué es mejor hacer después de votar? A) Ver si se puede incluir a quienes votaron por el museo B) Ignorarlos.", "A", "Cuida a la minoría.")],
    selfcheck=[ex("En Orientación: ¿el consenso busca una decisión con la que todos puedan vivir?", "Sí", "Es su definición."), ex("¿La mayoría puede ignorar los derechos de la minoría?", "No", "La democracia protege a todas las personas."), ex("¿Delegar exige rendición de cuentas?", "Sí", "Se informa lo decidido.")],
    task=T("Un curso inventado tiene tres decisiones: (1) elegir el nombre del curso; (2) acordar normas de convivencia; (3) encargar la compra de materiales a una comisión. Para cada una elige votación por mayoría, consenso o delegar, justifica con una frase y escribe una consecuencia posible.", "(1) Votación: tema simple y rápido; consecuencia: gana una opción y quizá alguien quede disconforme. (2) Consenso: afecta a todos; consecuencia: lleva más tiempo, pero compromete. (3) Delegar: es una tarea práctica; consecuencia: se requiere informar.", ["asigna un método a cada decisión", "justifica con una frase", "anota una consecuencia", "respeta a la minoría"], ["tabla escrita", "texto oral"], ["votar todo sin pensar", "olvidar a la minoría"], "Reconoce los métodos bien elegidos y pregunta cómo cuidaría a la minoría."),
    reinforce="Elige un método para decidir el menú de una fiesta de curso inventada y justifica.",
    extend="Explica la diferencia entre consenso y unanimidad.",
)

lesson(
    OA8, 4,
    "Una hoja y un lápiz. El caso de la campaña de buen trato de 1.º B y los pasos de la iniciativa, con personas inventadas, están escritos en los ejercicios.",
    "Aprenderé a diseñar una iniciativa de buen trato de forma segura, inclusiva y democrática, y a saber qué hacer cuando aparece discriminación. Sirve para actuar en el curso con cuidado.",
    ["Sé comparar métodos de decisión.", "Sé que el buen trato respeta a todos."],
    [
        "Para llevar adelante una iniciativa de buen trato sigue seis pasos: 1) nombrar el problema con un hecho, 2) fijar una meta observable, 3) elegir una acción pacífica e inclusiva, 4) asignar responsables y plazos, 5) decidir de manera democrática y 6) revisar los resultados. Una meta observable es una conducta que se puede ver, como «cada recreo hay un grupo mixto jugando juntos».",
        "Una iniciativa de buen trato es segura cuando no expone a personas, no usa burlas ni etiquetas y cuenta con el apoyo de un adulto. Es inclusiva si considera la diversidad: edades, género, origen, discapacidad y distintas opiniones. Ejemplos: una semana de saludos, una brigada de mediadores, un buzón de ideas anónimas de buen trato (sin acusaciones).",
        "Si en la iniciativa aparece discriminación o violencia, no se confronta a solas: se detiene la situación, se protege a la persona afectada y se avisa a un adulto del colegio. Reparar también es parte: invitar a quien se equivocó a corregir y acompañar a la persona dañada.",
    ],
    [("meta observable", "resultado que se puede ver y comprobar"), ("brigada de mediadores", "grupo de estudiantes capacitados para ayudar a resolver conflictos entre pares"), ("buzón anónimo", "caja de ideas sin nombres para mejorar la convivencia"), ("inclusiva", "que considera a todas las personas"), ("reparar", "corregir el daño causado")],
    [
        W("Meta observable", "¿Cuál es una meta observable de buen trato: «mejorar la convivencia» o «cada viernes 4 estudiantes saludan por turnos a otro curso»?", ["La primera no dice qué se vería ni cuándo.", "La segunda dice qué se ve, cuántas personas y cuándo."], "La segunda"),
        W("Qué hacer ante discriminación", "Durante la campaña, un estudiante se burla de otro por su acento. ¿Qué haces?", ["Detener la situación sin pelear.", "Proteger a la persona afectada.", "Avisar a un adulto del colegio."], "Proteger a la persona y avisar a un adulto"),
    ],
    [
        M("Hacer una campaña que señala a quienes se portan mal.", "Se confunde promover con acusar.", "Promueve conductas positivas sin exponer a nadie."),
        M("Creer que la iniciativa termina al realizar la actividad.", "No se revisa el efecto.", "Revisa si hubo cambio observable."),
    ],
    R=[
        ex("¿Cuál es una meta observable? A) «Este mes habrá 8 recreos con juegos mixtos.» B) «Que todos se lleven bien.»", "A", "Se puede contar y comprobar."),
        ex("En plena campaña, un estudiante insulta a otro por su origen. ¿Cuál es el primer paso seguro? A) Detener la situación, proteger al insultado y avisar a un adulto B) Insultarlo de vuelta", "A", "No se confronta a solas ni se responde con agresión."),
        ex("Una campaña de buen trato debe ser inclusiva. ¿Qué significa? A) Considerar edades, género, origen y discapacidad B) Beneficiar solo a quienes votaron por ella", "A", "Considera a todas las personas."),
    ],
    U=[
        ex("¿Cuál es el sexto paso de la iniciativa? A) Revisar resultados B) Elegir responsables.", "A", "Es el último paso."),
        ex("¿Cuál es el primer paso de la iniciativa de buen trato? A) Nombrar el problema con un hecho B) Revisar los resultados", "A", "Se parte por el problema y su hecho."),
        ex("¿Qué es un buzón anónimo de buen trato? A) Una caja de ideas sin nombres ni acusaciones B) Una lista de culpables.", "A", "Recoge ideas sin exponer."),
    ],
    A=[
        ex("Una brigada de mediadores de 12 estudiantes se reparte en 4 recreos por semana en partes iguales. ¿Cuántos mediadores hay por recreo?", "3", "12 dividido en 4 recreos da 3."),
        ex("Clasifica con S (segura) o N (no segura): 1) campaña de saludos por turnos; 2) lista pública de quienes se pelean; 3) buzón de ideas sin acusaciones. Escribe las letras en orden.", "S, N, S", "La 2 expone a personas."),
        ex("En la brigada de mediadores, dos estudiantes empiezan a empujarse. ¿Qué es lo más seguro? A) Avisar de inmediato a un adulto del colegio B) Separarlos a empujones", "A", "No se interviene con violencia."),
    ],
    Z=[
        ex("¿Por qué conviene revisar los resultados de la iniciativa?", "Porque permite saber si funcionó y ajustar", "Sin revisión no se aprende."),
        ex("Una campaña usa fotos de estudiantes burlándose de otros para «dar el ejemplo». ¿Qué problema tiene? A) Expone y humilla a personas B) Ninguno.", "A", "Daña la dignidad."),
    ],
    D=[
        arith("Una semana de saludos tiene 5 días y cada día participan 8 estudiantes. ¿Cuántas participaciones hay en la semana?", "5*8", "Se multiplican días por estudiantes."),
        arith("La meta es 20 recreos con juegos mixtos y se cumplieron 14. ¿Cuántos faltan?", "20-14", "A la meta se le restan los cumplidos."),
    ],
    context=[ex("Tu curso quiere una brigada de mediadores. ¿Qué es lo primero que deben pedir? A) Capacitación y apoyo de un adulto del colegio B) Que los mediadores castiguen.", "A", "Se necesita formación y respaldo.")],
    selfcheck=[ex("En Orientación: ¿una iniciativa de buen trato debe ser segura?", "Sí", "No debe exponer a nadie."), ex("¿Se revisa si la iniciativa funcionó?", "Sí", "Es el sexto paso."), ex("¿Ante discriminación se avisa a un adulto?", "Sí", "Se protege a la persona.")],
    task=T("Diseña una iniciativa de buen trato para un curso inventado de 1.º medio. Escribe los seis pasos: problema con un hecho, meta observable, acción pacífica e inclusiva, responsables y plazos, cómo se decide, cómo se revisa. Agrega qué harían si alguien se burla de un compañero durante la iniciativa.", "Problema: en los recreos juegan separados mujeres y hombres. Meta: 4 recreos con juegos mixtos al mes. Acción: juegos mixtos organizados por turnos. Responsables: Ema y Pedro; plazo: 1 mes. Decisión: votación y consenso. Revisión: conteo de recreos. Si hay burla: detener, proteger y avisar al profesor jefe.", ["escribe los seis pasos", "la meta es observable", "es inclusiva y segura", "incluye qué hacer ante discriminación"], ["plan escrito", "tabla"], ["meta vaga", "olvidar la revisión"], "Reconoce el plan completo y pregunta cómo medirían el resultado."),
    reinforce="Escribe una meta observable para una semana de buen trato.",
    extend="Explica por qué la inclusión es parte del buen trato.",
)

lesson(
    OA8, 5,
    "Una hoja y un lápiz. El esquema del debate y los roles están escritos en los ejercicios; usa personas inventadas.",
    "Aprenderé a preparar y conducir un debate respetuoso entre opiniones distintas en el Consejo de Curso. Sirve para dialogar, escuchar y llegar a acuerdos sin dañar la convivencia.",
    ["Sé distinguir argumentos de ataques.", "Sé comparar formas de decidir."],
    [
        "Un debate respetuoso tiene roles: quienes defienden, quienes cuestionan y un moderador. Se organiza en tiempos: una exposición breve, una réplica y un cierre. Antes de hablar, se prepara una tesis (la idea principal), dos argumentos y un dato por cada argumento. Quien escucha anota la objeción más fuerte para responder con respeto.",
        "Frases útiles para el diálogo: «Entiendo que piensas…, y yo veo que…», «¿Podrías explicarme esa razón?», «Estoy de acuerdo en… y no en…». Estas frases reconocen a la otra persona sin renunciar a la propia opinión. Evita ironías, gritos y burlas. Si alguien se enoja, se hace una pausa breve.",
        "Al terminar un debate, se resume en qué hubo acuerdo, en qué no y qué sigue. Los desacuerdos no son fracasos: son parte de vivir en diversidad. Si un debate se vuelve violento o humillante, el moderador lo detiene y se avisa a un adulto del colegio.",
    ],
    [("tesis", "idea principal que se defiende"), ("réplica", "respuesta a lo que dijo el otro"), ("moderador", "persona que da la palabra y cuida las reglas"), ("objeción", "razón en contra de una idea"), ("diversidad de opiniones", "variedad de formas de pensar sobre un tema")],
    [
        W("Preparar la intervención", "Camila defiende «alargar el recreo». Prepara tesis, dos argumentos y un dato.", ["Tesis: el recreo debería durar 5 minutos más.", "Argumento 1: se necesita más tiempo para comer.", "Argumento 2: el juego reduce el estrés.", "Dato: hoy dura 15 minutos."], "Tesis con dos argumentos y un dato"),
        W("Responder con respeto", "Alguien dice: «Alargar el recreo quita tiempo de clases». ¿Cómo responde Camila?", ["Reconoce la objeción.", "Aporta su razón."], "«Entiendo la preocupación; propongo recortar 5 minutos de la hora de almuerzo»"),
    ],
    [
        M("Preparar solo lo que voy a decir y no lo que puede decir el otro.", "Se espera ganar y no dialogar.", "Anota la objeción más fuerte y piensa una respuesta."),
        M("Considerar el desacuerdo como una pelea.", "Se confunde diferencia con enemistad.", "El desacuerdo respetuoso enriquece."),
    ],
    R=[
        ex("Pía dice: «Los cursos deberían rotar el uso de la sala de computación». ¿Qué es esa frase en su intervención? A) La tesis B) La réplica", "A", "Es la idea principal que defiende."),
        ex("Dos personas hablan a la vez en un debate. ¿Qué hace el moderador? A) Da la palabra por turnos B) Elige quién tiene la razón", "A", "Su función es dar la palabra y cuidar las reglas."),
        ex("Dos estudiantes opinan distinto sobre un paseo y se respetan. ¿Qué ejemplifica eso? A) La diversidad de opiniones B) Un conflicto sin solución", "A", "Cada persona piensa de manera propia."),
    ],
    U=[
        ex("¿Qué frase reconoce a la otra persona sin renunciar a la propia opinión? A) «Entiendo tu punto, y yo veo que…» B) «Estás equivocado.»", "A", "Respeta y expone la propia idea."),
        ex("¿Qué se prepara antes de hablar en un debate? A) Tesis, dos argumentos y un dato por argumento B) Solo una broma.", "A", "Da orden y fuerza a la intervención."),
        ex("¿Qué se hace si alguien se enoja? A) Se hace una pausa breve B) Se grita más fuerte.", "A", "Permite que todos se calmen."),
    ],
    A=[
        ex("Un debate tiene exposición de 3 minutos, réplica de 2 minutos y cierre de 1 minuto. ¿Cuántos minutos dura cada turno completo?", "6", "3 + 2 + 1 son 6 minutos."),
        ex("Clasifica con R (respetuosa) o I (irrespetuosa): 1) «¿Podrías explicarme esa razón?»; 2) «Qué ridículo»; 3) «Estoy de acuerdo en el dato, pero no en la conclusión». Escribe las letras en orden.", "R, I, R", "La 2 humilla; las otras dialogan."),
        ex("Si el debate se vuelve humillante y el moderador no logra parar, ¿qué se hace? A) Avisar a un adulto del colegio B) Seguir hasta el final.", "A", "Protege a las personas."),
    ],
    Z=[
        ex("¿Por qué anotar la objeción más fuerte ayuda en un debate?", "Porque permite preparar una respuesta respetuosa y razonada", "Se responde con argumentos y no con enojo."),
        ex("Dos personas terminan sin ponerse de acuerdo pero se respetan. ¿Qué indica? A) Que el debate fue respetuoso B) Que fracasó.", "A", "Disentir con respeto es válido."),
    ],
    D=[
        arith("Un debate tiene 4 intervenciones de 3 minutos y 2 de 5 minutos. ¿Cuántos minutos suma?", "4*3+2*5", "Se suman los minutos de ambos tipos.", " minutos"),
        arith("De 36 estudiantes, 24 participan en el debate como oyentes, y el resto como expositores. ¿Cuántos son expositores?", "36-24", "Al total se le restan los oyentes."),
    ],
    context=[ex("En el Consejo de Curso se debate si el paseo será a la playa o al campo. Dos estudiantes discuten con gritos. ¿Qué debe hacer el moderador? A) Pedir calma y volver a las reglas B) Dejar que griten.", "A", "Mantiene el respeto.")],
    selfcheck=[ex("En Orientación: ¿un debate respetuoso tiene un moderador?", "Sí", "Cuida las reglas."), ex("¿Es válido disentir con respeto?", "Sí", "La diversidad de opiniones enriquece."), ex("¿Se puede gritar para ganar un debate?", "No", "Rompe el respeto.")],
    task=T("Se debate si el curso debe tener un día a la semana sin celulares en la sala. Prepara dos intervenciones: una a favor y una en contra, cada una con tesis, dos argumentos y un dato de ejemplo. Escribe además una frase respetuosa para cuestionar y una para cerrar el debate.", "A favor: tesis: un día sin celulares mejora la atención; argumentos: se interrumpe menos y se conversa más; dato (de ejemplo): se interrumpió 6 veces en una hora. En contra: tesis: el celular sirve como herramienta; argumentos: consultar datos y emergencias. Frase: «¿Podrías explicarme cómo evitar distracciones?». Cierre: «Coincidimos en cuidar la atención y no en el día fijo».", ["escribe las dos posturas con tesis y argumentos", "usa un dato rotulado de ejemplo", "incluye una frase respetuosa para cuestionar", "incluye un cierre"], ["guion escrito", "debate oral"], ["argumentos sin datos", "tono irrespetuoso"], "Reconoce las posturas bien armadas y pregunta cuál objeción es la más fuerte."),
    reinforce="Prepara una tesis y dos argumentos para una propuesta del curso.",
    extend="Explica por qué disentir con respeto fortalece la convivencia.",
)
