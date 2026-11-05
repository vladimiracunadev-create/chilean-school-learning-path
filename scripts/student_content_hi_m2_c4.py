"""Cuaderno del estudiante, 2.º medio Historia, Geografía y Ciencias Sociales: OA 23 (Estado de derecho, participación y convivencia) y OA 24 (desafíos pendientes y responsabilidades)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI2M OA 23"

# ================================================================ OA 23, clase 1
F = ("Ficha 1 (todo es de ejemplo; el país «Altamar» es ficticio). "
     "Un Estado de derecho es un Estado donde todas las personas y también las autoridades deben obedecer leyes conocidas, que se aplican por igual. "
     "Sus elementos: (1) una Constitución, que es la ley máxima y fija los derechos y la forma de gobernar; (2) la división de los poderes: el Ejecutivo gobierna y administra, el Legislativo hace las leyes y el Judicial resuelve los conflictos según las leyes; "
     "(3) el respeto a los derechos humanos. "
     "Caso de ejemplo: en Altamar un alcalde ordena cerrar un diario que lo criticó. Un tribunal anula la orden porque la Constitución de Altamar protege la libertad de expresión.")
build(
    OA, 1, F,
    use="Aprenderé a situar el Estado de derecho: qué elementos lo forman y qué actores intervienen, para plantear la pregunta de por qué importa en la vida diaria.",
    prior=["Sé que en un país hay un gobierno, un Congreso y tribunales.", "Conozco la idea de derechos humanos de la Declaración Universal de 1948.", "Sé qué es una fuente y quién la escribe."],
    explain=[
        "Un Estado de derecho es aquel donde nadie está por encima de la ley, ni siquiera quien gobierna. Para lograrlo se necesitan reglas escritas y conocidas, y un mismo trato para todas las personas. La Constitución es la ley más importante: dice qué derechos tienen las personas, cómo se eligen las autoridades y qué límites tiene su poder.",
        "El segundo elemento es la división de los poderes del Estado. El Ejecutivo gobierna y administra; el Legislativo discute y aprueba las leyes; el Judicial resuelve conflictos aplicando esas leyes. Al repartir el poder en tres, uno puede frenar los abusos de otro. El tercer elemento es el respeto a los derechos humanos, que ninguna autoridad puede ignorar.",
        "Los actores son las autoridades, las personas ciudadanas, los tribunales y las organizaciones sociales. Un error frecuente es creer que basta con tener leyes para vivir en un Estado de derecho: hace falta además que se cumplan y que existan instituciones que las hagan cumplir.",
    ],
    vocab=[("Estado de derecho", "Estado donde autoridades y personas obedecen leyes conocidas, iguales para todos"), ("Constitución", "ley máxima que fija derechos y organiza el poder"), ("división de poderes", "reparto del poder entre Ejecutivo, Legislativo y Judicial"), ("Ejecutivo", "poder que gobierna y administra"), ("Judicial", "poder que resuelve los conflictos aplicando la ley")],
    worked=[
        ("Reconocer un poder", "Un tribunal de Altamar resuelve una disputa entre dos vecinos aplicando la ley. ¿Qué poder actúa?", ["El poder que resuelve conflictos aplicando las leyes es el Judicial.", "Ni gobierna ni hace leyes."], "El poder Judicial"),
        ("Aplicar un elemento", "Una ley de Altamar dice que el presidente puede encarcelar a quien quiera sin juicio. ¿Respeta el Estado de derecho?", ["Un Estado de derecho exige respeto a los derechos humanos y límites al poder.", "Encarcelar sin juicio no tiene límites."], "No, porque deja el poder sin límites y sin juicio"),
    ],
    mistakes=[("Decir que basta con tener leyes para que exista un Estado de derecho.", "Se olvida que las autoridades también deben cumplirlas y que debe haber instituciones que las apliquen.", "Revisa los tres elementos y pregunta si la ley se cumple para todos."),
              ("Confundir al Legislativo con el Judicial.", "Ambos trabajan con leyes, pero uno las crea y el otro las aplica a casos.", "Recuerda: Legislativo hace la ley; Judicial la aplica a un conflicto.")],
    T=[
        ("{F} ¿Qué poder hace las leyes?", "El poder Legislativo", "La ficha dice que el Legislativo hace las leyes."),
        ("{F} ¿Cómo se llama la ley máxima que fija derechos y organiza el poder?", "Constitución", "La ficha la define así."),
        ("{F} ¿Cuántos elementos del Estado de derecho enumera la ficha?", "Tres", "Enumera Constitución, división de poderes y respeto a los derechos humanos."),
        ("{F} En Altamar, el Ministerio de Obras construye un puente y paga a los trabajadores. ¿Qué poder actúa? A) Ejecutivo B) Legislativo", "A) Ejecutivo", "Administrar y realizar obras es tarea del poder que gobierna y administra."),
        ("{F} El Congreso de Altamar vota una ley sobre el reciclaje. ¿Qué poder actúa? A) Judicial B) Legislativo", "B) Legislativo", "Discutir y aprobar leyes es función del Legislativo."),
        ("{F} ¿Qué elemento del Estado de derecho aparece cuando el tribunal anula la orden del alcalde? A) La ley también obliga a las autoridades B) La ley solo obliga a los ciudadanos", "A) La ley también obliga a las autoridades", "El alcalde es autoridad y debe obedecer la Constitución, como dice la ficha."),
        ("{F} Un decreto del gobierno de Altamar prohíbe a un grupo de personas asistir a la escuela solo por su origen. ¿Qué elemento se vulnera? A) El respeto a los derechos humanos B) La división de poderes", "A) El respeto a los derechos humanos", "Negar la educación por origen discrimina y viola derechos."),
        ("{F} Un grupo del Legislativo de Altamar, además de hacer leyes, juzga los casos y manda a la policía. ¿Qué problema hay? A) Concentra funciones de varios poderes y nadie lo frena B) Ninguno: el Legislativo puede hacer también esas tareas", "A) Concentra funciones de varios poderes y nadie lo frena", "La división de poderes existe para que uno frene a otro."),
        ("{F} ¿Por qué no basta con que existan leyes escritas para decir que hay Estado de derecho? A) También deben cumplirse y obligar a las autoridades B) Porque en un Estado de derecho las leyes no obligan a las autoridades", "A) También deben cumplirse y obligar a las autoridades", "La explicación indica que hace falta cumplimiento e instituciones, no solo texto."),
        ("{F} Un compañero dice: «Como el alcalde fue elegido, puede cerrar el diario». ¿Cuál es la mejor respuesta? A) Aunque sea elegido, está limitado por la Constitución B) Tiene razón, porque el pueblo lo eligió", "A) Aunque sea elegido, está limitado por la Constitución", "En un Estado de derecho nadie está por encima de la ley, ni quien fue elegido."),
        ("{F} ¿Qué poder impidió el abuso del alcalde en el caso de la ficha? A) El Judicial, anulando la orden B) El Legislativo, cambiando la ley", "A) El Judicial, anulando la orden", "La ficha cuenta que un tribunal anuló la orden."),
        ("¿Cuál es la mejor pregunta para investigar este tema? A) ¿Cómo protegen la Constitución y la división de poderes a las personas frente a los abusos? B) ¿Cuál país tiene la mejor Constitución?", "A) ¿Cómo protegen la Constitución y la división de poderes a las personas frente a los abusos?", "La pregunta A se responde con hechos y ejemplos; la B es un ranking sin criterio."),
        ("{F} Un país tiene Constitución y tres poderes, pero la policía no cumple las órdenes de los tribunales. ¿Qué se puede afirmar? A) Falla el cumplimiento, así que el Estado de derecho está debilitado B) Es un Estado de derecho completo porque tiene tres poderes", "A) Falla el cumplimiento, así que el Estado de derecho está debilitado", "La existencia formal de poderes no basta si las decisiones no se cumplen."),
    ],
    ctx=("En el municipio ficticio de Rinconada el concejo, el alcalde y un juzgado local discuten si un permiso se entregó sin cumplir la ley. ¿Quién debe decidir si la ley se infringió? A) El juzgado, porque resuelve conflictos aplicando la ley B) El alcalde, porque es la máxima autoridad local", "A) El juzgado, porque resuelve conflictos aplicando la ley", "Decidir si una autoridad infringió la ley es labor del poder Judicial."),
    sc=[("¿Qué es una Constitución?", "La ley máxima que fija derechos y organiza el poder", "Así se define en el vocabulario."),
        ("Nombra los tres poderes del Estado.", "Ejecutivo, Legislativo y Judicial", "La explicación los enumera."),
        ("¿Para qué se divide el poder?", "Para que unos poderes frenen los abusos de otros", "Esa es la razón dada en la explicación.")],
    op=("Dibuja un esquema con tres cajas llamadas Ejecutivo, Legislativo y Judicial y escribe en cada una su función. Elige una de estas situaciones de ejemplo y anota qué poder actúa y qué elemento del Estado de derecho aparece: (a) un tribunal anula una multa ilegal; (b) el Congreso cambia una ley de tránsito; (c) un ministerio abre un consultorio. {F}",
        "Ejecutivo: gobierna y administra; Legislativo: hace leyes; Judicial: resuelve conflictos. Situación (a): Judicial; la ley también obliga a las autoridades.",
        ["describe bien las tres funciones", "relaciona la situación con el poder correcto", "nombra un elemento del Estado de derecho"], ["esquema de tres cajas", "una situación analizada"], ["intercambiar las funciones del Legislativo y el Judicial", "no nombrar el elemento"],
        "Pide que explique con otro ejemplo por qué ninguna autoridad está por encima de la ley."),
    reinforce="Explica a una persona de tu casa qué hace cada poder del Estado con un ejemplo de tu comuna.",
    extend="Anota un servicio público que conozcas (una escuela, un consultorio) y di a cuál de los tres poderes se parece su función.",
)

# ================================================================ OA 23, clase 2
F = ("Ficha 2 (tres fuentes de ejemplo escritas para este cuaderno; no son documentos reales). "
     "Fuente A, artículo de la Constitución de Altamar, texto oficial: «Nadie puede ser detenido sin una orden de un tribunal, salvo si lo sorprenden cometiendo un delito.» "
     "Fuente B, columna de opinión de un diario, escrita por un abogado de una organización de derechos humanos: «Las detenciones sin orden se han multiplicado este mes y debilitan la confianza en la ley.» "
     "Fuente C, comunicado del Ministerio del Interior de Altamar: «Las detenciones se hicieron para proteger a la población y se ajustaron a la ley.»")
build(
    OA, 2, F,
    use="Aprenderé a interrogar fuentes sobre el Estado de derecho: preguntar quién las escribe, cuándo, para qué y qué pueden y no pueden probar.",
    prior=["Sé que el Estado de derecho tiene Constitución, división de poderes y derechos humanos.", "Sé distinguir un hecho de una opinión.", "Sé qué es la procedencia de una fuente."],
    explain=[
        "Interrogar una fuente es hacerle preguntas antes de creerle. La procedencia es el origen de la fuente: quién la escribió, cuándo y con qué propósito. Una norma oficial, como un artículo de la Constitución, establece reglas. Una columna de opinión defiende un punto de vista. Un comunicado de gobierno explica sus actos y suele defenderlos.",
        "Ninguna fuente es inútil, pero cada una sirve para algo distinto. La norma sirve para saber qué dice la ley; la columna, para conocer la preocupación de un sector; el comunicado, para conocer la versión de la autoridad. Para saber si la ley se cumplió se necesita además evidencia verificable, como registros de tribunales o datos públicos.",
        "Una conclusión debe ser proporcional a la fuente: si solo hay una columna, se puede decir «este autor afirma», no «está probado». Contrastar fuentes de distinto origen ayuda a acercarse a lo ocurrido.",
    ],
    vocab=[("procedencia", "origen de una fuente: autor, fecha y propósito"), ("norma", "regla escrita que establece lo que se debe o no se debe hacer"), ("columna de opinión", "texto que defiende el punto de vista de su autor"), ("comunicado", "texto con que una institución informa su versión"), ("evidencia verificable", "dato que otras personas pueden comprobar")],
    worked=[
        ("Preguntar por la procedencia", "¿Quién escribe la Fuente B y qué se puede esperar de ella?", ["La ficha dice que es un abogado de una organización de derechos humanos.", "Defenderá la protección de derechos, es decir, un punto de vista."], "Un abogado de una organización de derechos humanos; sirve como punto de vista, no como prueba por sí sola"),
        ("Proporcionar la conclusión", "Con solo la Fuente C, ¿se puede afirmar que la ley se cumplió?", ["La Fuente C es la versión de la autoridad.", "No trae registros que otros puedan comprobar."], "No, solo se puede afirmar que la autoridad dice que se cumplió"),
    ],
    mistakes=[("Creer que una fuente oficial siempre prueba lo ocurrido.", "Un comunicado explica los actos de quien lo escribe; no es evidencia independiente.", "Pregunta quién escribe y busca otra fuente que lo respalde."),
              ("Descartar una columna de opinión por ser opinión.", "Sirve para conocer un punto de vista aunque no pruebe hechos.", "Úsala como perspectiva y contrástala con otras fuentes.")],
    T=[
        ("{F} ¿Qué tipo de fuente es la Fuente A?", "Una norma oficial, un artículo de la Constitución", "La ficha la presenta como texto oficial de la Constitución."),
        ("{F} ¿Quién escribe la Fuente C?", "El Ministerio del Interior de Altamar", "La ficha lo indica."),
        ("{F} ¿Qué dice la Fuente A sobre las detenciones sin orden?", "Que no se permiten salvo si la persona es sorprendida cometiendo un delito", "Es el contenido del artículo citado."),
        ("{F} ¿Qué fuente sirve mejor para conocer lo que la ley permite? A) Fuente A B) Fuente B", "A) Fuente A", "Una norma oficial dice qué establece la ley."),
        ("{F} ¿Qué se puede esperar de la Fuente B por la procedencia de su autor? A) Que defienda la protección de derechos B) Que no tenga ningún punto de vista", "A) Que defienda la protección de derechos", "Quien trabaja en una organización de derechos humanos suele defender ese punto de vista."),
        ("{F} ¿Por qué la Fuente C no basta para saber si la ley se cumplió? A) Es la versión de la autoridad y no trae registros comprobables B) Fue escrita después de la Fuente A", "A) Es la versión de la autoridad y no trae registros comprobables", "Un comunicado defiende los actos de quien lo escribe."),
        ("{F} Se quiere comprobar si hubo detenciones sin orden. ¿Qué evidencia es mejor? A) Registros de tribunales con fechas y números B) Una opinión sin datos de un vecino", "A) Registros de tribunales con fechas y números", "Los registros pueden ser verificados por otras personas."),
        ("{F} Un compañero concluye: «La Fuente B prueba que la ley fue violada». ¿Cómo lo corriges? A) Solo prueba que su autor lo afirma y hay que contrastarlo B) Tiene razón porque el autor es abogado", "A) Solo prueba que su autor lo afirma y hay que contrastarlo", "Una columna de opinión es un punto de vista; la conclusión debe ser proporcional."),
        ("{F} Otro compañero dice: «Como la Fuente C es del gobierno, es falsa». ¿Qué error comete? A) Descarta la fuente sin contrastarla B) Usa evidencia verificable", "A) Descarta la fuente sin contrastarla", "Una fuente se interroga y se contrasta, no se rechaza solo por su origen."),
        ("{F} Si la Fuente B y la Fuente C se contradicen, ¿qué conviene hacer primero? A) Buscar una tercera fuente verificable B) Elegir la que suena más convincente", "A) Buscar una tercera fuente verificable", "La contradicción se resuelve con evidencia independiente."),
        ("{F} ¿Qué conclusión es proporcional? A) Según la Constitución las detenciones sin orden están limitadas; un abogado dice que aumentaron y el ministerio dice que se ajustaron a la ley; falta evidencia verificable B) Está probado que el gobierno actuó mal", "A) Según la Constitución las detenciones sin orden están limitadas; un abogado dice que aumentaron y el ministerio dice que se ajustaron a la ley; falta evidencia verificable", "Reconoce las tres fuentes y el límite de lo que prueban."),
        ("{F} Una fuente D dice: «Los registros del tribunal muestran 12 detenciones sin orden en el mes y 9 fueron declaradas ilegales». ¿Qué ventaja tiene sobre B y C? A) Aporta datos que se pueden comprobar B) Es la opinión de un vecino", "A) Aporta datos que se pueden comprobar", "Los registros permiten verificar el hecho."),
        ("=", "{F} En la fuente D de la pregunta anterior (12 detenciones, 9 declaradas ilegales), ¿qué porcentaje de las detenciones fue declarado ilegal?", "9*100/12", "Se divide 9 entre 12 y se multiplica por cien.", " %"),
    ],
    ctx=("Una radio local informa que un municipio ficticio «cumple siempre la ley», citando solo un folleto del propio municipio. ¿Qué pregunta de procedencia es la más útil? A) ¿Quién lo escribe y qué evidencia independiente lo respalda? B) ¿Es un folleto oficial? Si lo es, no hace falta revisar más", "A) ¿Quién lo escribe y qué evidencia independiente lo respalda?", "Interrogar una fuente es ver quién la escribe y si hay otra evidencia."),
    sc=[("¿Qué es la procedencia de una fuente?", "El origen de la fuente: quién la escribió, cuándo y para qué", "Así se define en el vocabulario."),
        ("¿Una columna de opinión sirve como evidencia verificable?", "No, sirve como punto de vista", "La explicación dice que defiende el punto de vista de su autor."),
        ("¿Qué fuente sirve para conocer lo que dice la ley?", "Una norma oficial", "La explicación indica que la norma sirve para saber lo que dice la ley.")],
    op=("Completa una tabla con tres columnas: fuente, quién la escribe y qué sirve para probar. Úsala con las fuentes A, B y C de la ficha y agrega una frase final que empiece con «Con estas fuentes se puede afirmar que…» sin pasar el límite de lo que muestran. {F}",
        "A: Constitución, sirve para saber lo que establece la ley. B: abogado de una organización, sirve como punto de vista. C: ministerio, sirve como versión de la autoridad. Frase: «Con estas fuentes se puede afirmar que la ley limita las detenciones sin orden y que hay versiones distintas sobre su cumplimiento».",
        ["identifica el autor de cada fuente", "distingue norma, opinión y versión de la autoridad", "su conclusión es proporcional"], ["tabla", "frase final"], ["afirmar que algo está probado con una sola fuente", "no indicar quién escribe"],
        "Pide que diga qué otra fuente agregaría para comprobar los hechos."),
    reinforce="Cuéntale a alguien de tu casa por qué conviene preguntar quién escribe una noticia antes de creerla.",
    extend="Mira una publicidad o un aviso y anota quién lo escribe y para qué.",
)

# ================================================================ OA 23, clase 3
F = ("Ficha 3 (todas las posturas son de ejemplo, escritas para este cuaderno). "
     "Tema: ¿puede el Estado de Altamar vigilar a las personas con cámaras en toda la ciudad para reducir los delitos? "
     "Postura 1, vecina del barrio: «Quiero cámaras en mi calle; me siento más segura y los robos bajaron». "
     "Postura 2, organización de derechos digitales: «La vigilancia permanente puede afectar la privacidad; debe haber una ley clara, control de un tribunal y plazos para borrar las imágenes». "
     "Postura 3, municipio: «Instalaremos 200 cámaras en tres años, 50 el primer año y el resto en partes iguales los años siguientes». "
     "Escalas: lo que ocurre en una calle (local), en la ciudad (municipal) y en todo el país (nacional).")
build(
    OA, 3, F,
    use="Aprenderé a comparar perspectivas y escalas sobre un problema del Estado de derecho, reconociendo qué valora cada postura y a qué escala se refiere.",
    prior=["Sé que el Estado de derecho limita el poder y protege derechos.", "Sé interrogar una fuente por su procedencia.", "Sé distinguir hechos de opiniones."],
    explain=[
        "Comparar perspectivas es ver qué valora cada persona o grupo cuando opina sobre un mismo tema. En un Estado de derecho conviven varios valores a la vez: la seguridad, la libertad, la privacidad y la igualdad ante la ley. Muchas veces dos posturas no se contradicen del todo, sino que ponen más peso en un valor que en otro.",
        "También hay que comparar escalas. Un problema se vive en una calle, se decide en una ciudad y se regula en el país. Una medida local puede ser razonable para un barrio y no para todo el territorio. Por eso conviene preguntar quién decide, a quiénes afecta y qué ley la limita.",
        "Una buena comparación nombra lo que las posturas tienen en común, lo que las separa y qué evidencia haría falta para decidir. Así el debate deja de ser «quién gana» y pasa a ser «qué criterios usamos».",
    ],
    vocab=[("perspectiva", "punto de vista desde el que una persona o grupo mira un problema"), ("escala", "nivel en que se estudia un hecho: local, municipal o nacional"), ("privacidad", "derecho a proteger la vida personal de intromisiones"), ("valor", "idea que una persona considera importante, como la seguridad o la libertad"), ("criterio", "regla que se usa para decidir o comparar")],
    worked=[
        ("Reconocer el valor central", "En la Postura 1, ¿qué valor pesa más?", ["La vecina dice que se siente más segura.", "Eso muestra que valora la seguridad."], "La seguridad"),
        ("Reconocer la escala", "La Postura 3 habla de 200 cámaras en toda la ciudad. ¿A qué escala se refiere?", ["Una decisión que abarca una ciudad no es solo de una calle.", "La ficha la atribuye al municipio."], "A la escala municipal"),
    ],
    mistakes=[("Pensar que las posturas siempre se contradicen por completo.", "Cada una puede dar más peso a un valor distinto, y ambos pueden ser legítimos.", "Pregunta qué valor defiende cada una y busca puntos en común."),
              ("Aplicar una conclusión de una calle a todo el país.", "Se cambia de escala sin evidencia.", "Indica a qué escala se refiere cada dato.")],
    T=[
        ("{F} ¿Qué dice la Postura 1 sobre los robos?", "Que bajaron", "La vecina lo afirma en la ficha."),
        ("{F} ¿Quién expresa la Postura 2?", "Una organización de derechos digitales", "La ficha lo indica."),
        ("{F} ¿Cuántas cámaras instalará el municipio en total según la Postura 3?", "200", "La ficha da ese número total."),
        ("=", "{F} Según la Postura 3, ¿cuántas cámaras se instalarán por año en cada uno de los dos años siguientes al primero?", "(200-50)/2", "Se restan las 50 del primer año y se reparte lo restante en dos años iguales.", " cámaras por año"),
        ("{F} ¿Qué valor pesa más en la Postura 2? A) La privacidad B) El costo de las cámaras", "A) La privacidad", "La organización pide límites y control para proteger la vida personal."),
        ("{F} ¿A qué escala habla la Postura 1? A) Local, de su calle B) Nacional", "A) Local, de su calle", "La vecina habla de su calle."),
        ("{F} ¿Qué tienen en común las Posturas 1 y 2? A) Ambas buscan el bienestar de las personas, con distintos valores B) Ambas piden retirar todas las cámaras", "A) Ambas buscan el bienestar de las personas, con distintos valores", "Una prioriza la seguridad y la otra la privacidad, pero no rechazan la ley."),
        ("{F} ¿Qué condición de la Postura 2 respeta mejor la idea de que ninguna autoridad esté por encima de la ley? A) Una ley clara con control de un tribunal B) Que el municipio decida sin reglas", "A) Una ley clara con control de un tribunal", "Una ley clara y un tribunal son límites al poder."),
        ("{F} Si las cámaras de la calle de la vecina redujeron robos, ¿se puede concluir que también bajarán en todo el país? A) No, falta evidencia a escala nacional B) Sí, porque es la misma medida", "A) No, falta evidencia a escala nacional", "Un resultado local no se traslada al país sin datos nacionales."),
        ("{F} ¿Cómo se podrían conciliar las Posturas 1 y 2? A) Instalar cámaras con ley clara, control de un tribunal y plazos para borrar imágenes B) Instalar cámaras sin ninguna regla", "A) Instalar cámaras con ley clara, control de un tribunal y plazos para borrar imágenes", "Así se cuida la seguridad sin dejar de proteger la privacidad."),
        ("{F} ¿Qué evidencia ayudaría a decidir entre las posturas? A) Datos comprobables de cuánto bajaron los delitos y de cómo se resguardan las imágenes B) La cantidad de personas que opinan en redes", "A) Datos comprobables de cuánto bajaron los delitos y de cómo se resguardan las imágenes", "Se necesitan hechos verificables sobre la eficacia y la privacidad."),
        ("{F} Alguien dice: «Si defiendes la privacidad, no quieres seguridad». ¿Qué error comete? A) Supone que un valor excluye al otro B) Ninguno, es correcto", "A) Supone que un valor excluye al otro", "Se pueden valorar ambos a la vez, como muestra la Postura 2 con condiciones."),
        ("{F} Un reglamento de otro municipio permitiría grabar sin plazo y sin control. ¿Qué criterio de la Postura 2 incumple? A) La ley clara, el control de un tribunal y los plazos para borrar B) El número de cámaras", "A) La ley clara, el control de un tribunal y los plazos para borrar", "La Postura 2 pide justamente esos tres límites."),
    ],
    ctx=("En un colegio ficticio se debate instalar cámaras en los patios. Una apoderada pide más seguridad; un grupo de estudiantes pide que no se graben los baños ni los camarines. ¿Qué criterio concilia ambas posturas? A) Cámaras solo en espacios comunes y con reglas claras de uso B) Ninguna regla, porque cada uno defiende lo suyo", "A) Cámaras solo en espacios comunes y con reglas claras de uso", "Protege la seguridad y la privacidad con límites explícitos."),
    sc=[("¿Qué es una perspectiva?", "Un punto de vista desde el que se mira un problema", "Así se define en el vocabulario."),
        ("Nombra las tres escalas que usó la ficha.", "Local, municipal y nacional", "Están en la última frase de la ficha."),
        ("¿Dos posturas distintas siempre se contradicen por completo?", "No, pueden dar más peso a valores distintos", "La explicación lo dice.")],
    op=("Haz un cuadro de dos columnas para las Posturas 1 y 2: valor principal, escala en que hablan y evidencia que usan. Luego escribe una propuesta de tres líneas que respete ambas, indicando qué ley o institución la controlaría. {F}",
        "Postura 1: seguridad; escala local; experiencia de que bajaron los robos. Postura 2: privacidad; escala municipal o nacional; no trae datos. Propuesta: cámaras en espacios públicos, con ley clara, control de un tribunal y plazo para borrar imágenes.",
        ["identifica el valor de cada postura", "distingue la escala", "su propuesta incluye una institución de control"], ["cuadro completo", "propuesta de tres líneas"], ["decir que una de las posturas es falsa sin evidencia", "no nombrar ningún control"],
        "Pide que explique qué dato cambiaría su propuesta."),
    reinforce="Explica a alguien de tu casa dos valores que pueden chocar en una decisión del colegio.",
    extend="Piensa en una regla de tu colegio y di a quiénes beneficia, a quiénes limita y quién la controla.",
)

# ================================================================ OA 23, clase 4
F = ("Ficha 4 (hechos y cifras de ejemplo del país ficticio «Altamar»). "
     "Cambios: una reforma constitucional de Altamar crea un tribunal que revisa si las leyes respetan la Constitución. "
     "Continuidades: el Ejecutivo sigue proponiendo la mayoría de los proyectos de ley y los tribunales siguen resolviendo conflictos como antes. "
     "Consecuencias para la convivencia: los conflictos entre vecinos se llevan a los tribunales en vez de resolverse por la fuerza. "
     "Participación de ejemplo: en una elección municipal votaron 600 de las 800 personas inscritas. "
     "Gobernabilidad: capacidad de un gobierno de tomar decisiones y que se cumplan. Representación: que las autoridades hablen por quienes las eligieron.")
build(
    OA, 4, F,
    use="Aprenderé a relacionar causas, cambios y continuidades del Estado de derecho con la gobernabilidad, la representación, la participación y la convivencia pacífica.",
    prior=["Sé qué elementos forman el Estado de derecho.", "Sé comparar perspectivas y escalas.", "Sé calcular porcentajes sencillos."],
    explain=[
        "El Estado de derecho no existe aislado: sus reglas producen efectos en la vida colectiva. La gobernabilidad es la capacidad de un gobierno de tomar decisiones y lograr que se cumplan. Cuando las reglas son claras y respetadas, es más fácil gobernar sin recurrir a la fuerza. La representación significa que las autoridades actúan en nombre de quienes las eligieron.",
        "La participación ciudadana incluye votar, pero también opinar, organizarse y fiscalizar a las autoridades, es decir, vigilar que cumplan sus deberes. Un porcentaje de participación se calcula dividiendo las personas que votaron por las inscritas y multiplicando por cien. Una participación baja puede debilitar la representación, porque decide una parte menor de la población.",
        "La convivencia pacífica se logra cuando los conflictos se resuelven con reglas y tribunales y no con violencia. Al estudiar un proceso hay que separar causas, cambios y continuidades: una reforma cambia algo, pero muchas prácticas siguen igual.",
    ],
    vocab=[("gobernabilidad", "capacidad de un gobierno de tomar decisiones y lograr que se cumplan"), ("representación", "actuación de las autoridades en nombre de quienes las eligieron"), ("participación ciudadana", "intervención de las personas en los asuntos públicos: votar, opinar, organizarse"), ("convivencia pacífica", "vida en común donde los conflictos se resuelven sin violencia"), ("reforma", "cambio parcial de una ley o institución")],
    worked=[
        ("Calcular una participación", "En otra elección de ejemplo votaron 450 de 500 personas inscritas. ¿Qué porcentaje participó?", ["Se divide 450 entre 500: 0,9.", "Se multiplica por 100."], "90 %"),
        ("Separar cambio y continuidad", "El Ejecutivo sigue proponiendo la mayoría de los proyectos de ley. ¿Es cambio o continuidad?", ["Es algo que ya ocurría antes de la reforma.", "La reforma no lo modificó."], "Continuidad"),
    ],
    mistakes=[("Pensar que participar es solo votar.", "Se olvidan formas como organizarse, opinar y fiscalizar.", "Enumera al menos tres formas de participación."),
              ("Creer que una reforma cambia todo.", "Se ignoran las continuidades de las instituciones.", "Pregunta qué cambió y qué siguió igual.")],
    T=[
        ("{F} ¿Qué crea la reforma constitucional de Altamar?", "Un tribunal que revisa si las leyes respetan la Constitución", "La ficha lo indica en los cambios."),
        ("{F} ¿Cuántas personas inscritas había en la elección municipal de la ficha?", "800", "La ficha dice que votaron 600 de las 800 inscritas."),
        ("{F} ¿Qué significa gobernabilidad?", "Capacidad de un gobierno de tomar decisiones y lograr que se cumplan", "La ficha la define."),
        ("=", "{F} ¿Cuántas personas inscritas no votaron en la elección municipal?", "800-600", "Se resta quienes votaron al total de inscritas.", " personas"),
        ("=", "{F} ¿Qué porcentaje de las personas inscritas votó?", "600/800*100", "Se divide 600 entre 800 y se multiplica por cien.", " %"),
        ("{F} El tribunal nuevo revisa las leyes. ¿Es un cambio o una continuidad? A) Cambio B) Continuidad", "A) Cambio", "Se creó con la reforma y antes no existía."),
        ("{F} Los tribunales siguen resolviendo conflictos como antes. ¿Qué es eso? A) Una continuidad B) Un cambio", "A) Una continuidad", "La ficha dice que lo hacen igual que antes."),
        ("{F} Dos vecinos de Altamar discuten por un cerco y acuden a un tribunal. ¿Qué aspecto de la convivencia pacífica muestra? A) Resolver el conflicto con reglas y no con fuerza B) Evitar toda discusión", "A) Resolver el conflicto con reglas y no con fuerza", "La convivencia pacífica no elimina los conflictos, los resuelve con reglas."),
        ("{F} Si votara menos de la mitad de las personas inscritas, ¿qué efecto podría tener sobre la representación? A) Decidiría una parte menor de la población y se debilitaría B) No tendría efecto, porque la representación no depende de cuántos votan", "A) Decidiría una parte menor de la población y se debilitaría", "Con menos participación, las autoridades hablan por menos gente."),
        ("{F} ¿Por qué un tribunal que revisa las leyes puede favorecer la gobernabilidad? A) Da reglas claras y las decisiones se cumplen sin fuerza B) Reemplaza al Congreso en la tarea de hacer leyes", "A) Da reglas claras y las decisiones se cumplen sin fuerza", "Gobernar sin fuerza requiere reglas conocidas y respetadas."),
        ("{F} Un compañero dice: «Como votó el 75 %, no hace falta que nadie participe más». ¿Qué le respondes? A) Participar incluye organizarse y fiscalizar, no solo votar B) Tiene razón, el voto lo explica todo", "A) Participar incluye organizarse y fiscalizar, no solo votar", "La participación ciudadana tiene varias formas, como explica la clase."),
        ("{F} ¿Cuál es la mejor síntesis? A) La reforma cambió una institución, pero el Ejecutivo y los tribunales mantuvieron funciones, y la convivencia mejora si se usan las reglas B) Todo cambió con la reforma", "A) La reforma cambió una institución, pero el Ejecutivo y los tribunales mantuvieron funciones, y la convivencia mejora si se usan las reglas", "Reúne cambios y continuidades sin exagerar."),
        ("{F} En una tercera elección de ejemplo votan 360 de 480 personas inscritas. ¿Qué porcentaje participó? A) 75 % B) 80 %", "A) 75 %", "360 dividido en 480 es 0,75."),
    ],
    ctx=("En un centro de estudiantes ficticio votaron 54 de 90 personas inscritas. Un delegado dice que «ganó la participación». ¿Qué porcentaje votó? A) 60 % B) 54 %", "A) 60 %", "54 dividido en 90 es 0,6, es decir, 60 %."),
    sc=[("¿Qué es la representación?", "La actuación de las autoridades en nombre de quienes las eligieron", "Así se define en el vocabulario."),
        ("En Historia: ¿qué significa fiscalizar a las autoridades?", "Vigilar que cumplan sus deberes", "La explicación lo define."),
        ("¿Qué es una continuidad?", "Algo que sigue igual a pesar del cambio", "La explicación lo distingue del cambio.")],
    op=("Dibuja una tabla de tres columnas: causa, cambio y continuidad. Completa una fila con la reforma de Altamar y otra fila con esta situación de ejemplo: un municipio crea una oficina de reclamos, pero el alcalde sigue siendo elegido igual que antes. {F}",
        "Fila 1: causa, necesidad de revisar las leyes; cambio, tribunal nuevo; continuidad, el Ejecutivo propone la mayoría de los proyectos. Fila 2: cambio, oficina de reclamos; continuidad, elección del alcalde.",
        ["distingue causa, cambio y continuidad", "completa las dos filas", "no exagera el efecto de la reforma"], ["tabla de tres columnas", "dos filas completas"], ["poner un cambio en la columna de continuidad", "decir que cambió todo"],
        "Pide que explique cómo la oficina de reclamos puede favorecer la participación."),
    reinforce="Explica a una persona de tu casa qué diferencia hay entre gobernabilidad y representación.",
    extend="Anota una forma de participar en tu colegio que no sea votar.",
)

# ================================================================ OA 23, clase 5
F = ("Ficha 5 (caso de ejemplo del país ficticio «Altamar», con evidencias escritas para este cuaderno). "
     "Pregunta: ¿qué riesgos amenazan al Estado de derecho en Altamar y qué lo defiende? "
     "Evidencia 1, informe de un organismo de control: «Dos autoridades locales contrataron a familiares sin concurso, lo que va contra la ley.» "
     "Evidencia 2, comunicado de un tribunal: «Se sancionó a las dos autoridades y se anuló un contrato.» "
     "Evidencia 3, estudio de una universidad: «Circularon mensajes falsos sobre una votación, que luego fueron desmentidos por medios y por el servicio electoral.» "
     "Evidencia 4, nota de un periódico: «Solo el 40 % de los jóvenes inscritos votó en la última elección local» (dato de ejemplo).")
build(
    OA, 5, F,
    use="Aprenderé a construir una interpretación documentada sobre los riesgos y las defensas del Estado de derecho, sosteniéndola con evidencias.",
    prior=["Sé qué elementos forman el Estado de derecho.", "Sé interrogar fuentes y contrastar perspectivas.", "Sé relacionar causas, cambios y continuidades."],
    explain=[
        "Una interpretación documentada es una explicación que se apoya en evidencias y reconoce sus límites. Para armarla se formula una pregunta, se reúnen fuentes de distinto origen, se extrae de cada una lo que prueba y se escribe una conclusión proporcional. No es lo mismo afirmar «hay riesgos» que mostrar cuáles y cuánto pesan.",
        "Entre los riesgos para un Estado de derecho están la corrupción, que es usar el cargo para beneficio propio; la desinformación, que son mensajes falsos que confunden a la población; y la baja participación, que debilita la representación. Entre las defensas están los organismos de control, los tribunales independientes, la prensa libre y la participación informada.",
        "Un buen texto cita la evidencia («según el informe…»), distingue hechos de interpretaciones y señala lo que falta para saber más. Así el lector puede revisar el razonamiento.",
    ],
    vocab=[("interpretación documentada", "explicación apoyada en evidencias que reconoce sus límites"), ("corrupción", "uso de un cargo público para beneficio propio"), ("desinformación", "difusión de mensajes falsos que confunden a la población"), ("organismo de control", "institución que vigila que las autoridades cumplan la ley"), ("conclusión proporcional", "conclusión que no dice más de lo que muestra la evidencia")],
    worked=[
        ("Extraer lo que prueba una evidencia", "¿Qué prueba la Evidencia 2 y qué no prueba?", ["Prueba que se sancionó a dos autoridades y se anuló un contrato.", "No prueba que no haya más casos de corrupción."], "Prueba esas sanciones; no prueba que no existan otros casos"),
        ("Unir dos evidencias", "¿Qué muestran juntas las Evidencias 1 y 2?", ["La 1 muestra un riesgo: contrataciones ilegales.", "La 2 muestra una defensa: un tribunal que sanciona."], "Un riesgo y su respuesta institucional"),
    ],
    mistakes=[("Afirmar «hay corrupción en todo el país» con dos casos locales.", "La conclusión pasa de lo que muestra la evidencia.", "Escribe «se detectaron dos casos en autoridades locales»."),
              ("Citar solo las evidencias que apoyan lo que uno ya piensa.", "Se omite lo que contradice.", "Incluye evidencias de riesgo y de defensa.")],
    T=[
        ("{F} ¿Qué hicieron las dos autoridades locales según la Evidencia 1?", "Contrataron a familiares sin concurso", "La evidencia lo indica."),
        ("{F} ¿Qué institución sancionó a las autoridades según la Evidencia 2?", "Un tribunal", "El comunicado es de un tribunal."),
        ("{F} ¿Qué es la desinformación?", "La difusión de mensajes falsos que confunden a la población", "Así se define en la clase."),
        ("{F} ¿Qué riesgo muestra la Evidencia 3? A) Desinformación B) Corrupción", "A) Desinformación", "Habla de mensajes falsos sobre una votación."),
        ("{F} ¿Qué defensa del Estado de derecho aparece en la Evidencia 3? A) Medios y servicio electoral que desmintieron B) Una reforma constitucional", "A) Medios y servicio electoral que desmintieron", "Esas instituciones corrigieron los mensajes falsos."),
        ("=", "{F} Si fueran 500 los jóvenes inscritos, ¿cuántos habrían votado según el porcentaje de la Evidencia 4?", "500*40/100", "Se calcula el 40 % de 500.", " jóvenes"),
        ("{F} ¿Qué conclusión proporcional se puede escribir con la Evidencia 1? A) En Altamar se detectaron dos casos de contratación ilegal en autoridades locales B) En Altamar toda autoridad contrata ilegalmente", "A) En Altamar se detectaron dos casos de contratación ilegal en autoridades locales", "Respeta lo que muestra la evidencia."),
        ("{F} Un compañero usa la Evidencia 4 para concluir que a la juventud no le importa la política. ¿Qué corrección haces? A) El dato muestra baja votación, pero no explica sus motivos B) Tiene razón porque votó el 40 %", "A) El dato muestra baja votación, pero no explica sus motivos", "No votar puede tener varias causas que el dato no revela."),
        ("{F} ¿Qué evidencia muestra una defensa del Estado de derecho en acción? A) La Evidencia 2, porque un tribunal sancionó y anuló un contrato B) La Evidencia 1, porque describe la contratación", "A) La Evidencia 2, porque un tribunal sancionó y anuló un contrato", "El tribunal aplicó la ley a autoridades."),
        ("{F} ¿Qué afirmación une un riesgo y una defensa con sus evidencias? A) Según el informe hubo contrataciones ilegales y según el tribunal las autoridades fueron sancionadas B) Hubo contrataciones ilegales y por eso el Estado no funciona", "A) Según el informe hubo contrataciones ilegales y según el tribunal las autoridades fueron sancionadas", "Cita el origen de cada evidencia y las une sin exagerar."),
        ("{F} ¿Qué evidencia faltaría para afirmar que la corrupción aumentó en Altamar? A) Datos de varios años que se puedan comparar B) Otro comunicado del mismo tribunal", "A) Datos de varios años que se puedan comparar", "Para hablar de aumento se necesita comparar en el tiempo."),
        ("{F} Un texto dice: «El Estado de derecho de Altamar está perdido». ¿Qué problema tiene? A) Exagera frente a evidencias que también muestran defensas B) No usa la palabra corrupción", "A) Exagera frente a evidencias que también muestran defensas", "Las evidencias 2 y 3 muestran instituciones funcionando."),
        ("{F} ¿Cuál de estas es la mejor tesis? A) Altamar enfrenta riesgos como corrupción y desinformación, pero tribunales, medios y servicios de control los han enfrentado B) Altamar no tiene problemas porque tiene tribunales", "A) Altamar enfrenta riesgos como corrupción y desinformación, pero tribunales, medios y servicios de control los han enfrentado", "Es la única que usa las evidencias sin exagerar ni ocultar."),
    ],
    ctx=("Un estudiante escribe sobre su comuna ficticia: «El alcalde fue sancionado, por lo tanto toda la municipalidad es corrupta». ¿Cómo lo mejorarías? A) «El alcalde fue sancionado; falta evidencia sobre el resto de la municipalidad» B) «Todo el Estado es corrupto»", "A) «El alcalde fue sancionado; falta evidencia sobre el resto de la municipalidad»", "Una conclusión proporcional no generaliza desde un caso."),
    sc=[("¿Qué es una conclusión proporcional?", "Una conclusión que no dice más de lo que muestra la evidencia", "Así se define en el vocabulario."),
        ("En Historia: ¿cuál de estos es un riesgo para el Estado de derecho y no una defensa? A) La corrupción B) La prensa libre", "A) La corrupción", "La explicación pone la corrupción entre los riesgos y la prensa libre entre las defensas."),
        ("=", "Si de 200 jóvenes inscritos votaron 80, ¿qué porcentaje votó?", "80*100/200", "Se divide 80 entre 200 y se multiplica por cien.", " %")],
    op=("Escribe un párrafo de 5 a 7 líneas que responda la pregunta de la ficha. Debe citar al menos tres evidencias («según el informe…», «según el tribunal…»), incluir un riesgo y una defensa y terminar con una frase sobre lo que falta saber. {F}",
        "«Según el organismo de control, dos autoridades contrataron a familiares sin concurso. Según el tribunal, fueron sancionadas. Según la universidad, hubo mensajes falsos que se desmintieron. Falta saber si estos casos son frecuentes».",
        ["cita al menos tres evidencias", "incluye un riesgo y una defensa", "señala lo que falta saber"], ["párrafo escrito", "evidencias citadas"], ["generalizar desde dos casos", "no citar la fuente"],
        "Pide que cambie una afirmación exagerada por una proporcional."),
    reinforce="Cuéntale a alguien de tu casa un riesgo y una defensa del Estado de derecho con una evidencia.",
    extend="Busca en tu casa una noticia o un aviso y anota qué dato permitiría comprobarlo.",
)

# ================================================================ OA 23, clase 6
F = ("Ficha 6 (debate de ejemplo del país ficticio «Altamar»). "
     "Propuesta en discusión: crear un plan para que los colegios enseñen cómo funcionan los poderes del Estado y cómo participar. "
     "Argumento A a favor, de una profesora: «Una población que conoce sus derechos y las instituciones participa mejor y detecta abusos.» "
     "Argumento B en contra, de un padre: «El colegio ya tiene muchas materias; el plan podría quedar solo en el papel.» "
     "Argumento C, de un estudiante: «Sirve si incluye prácticas reales, como elegir un centro de estudiantes y revisar un presupuesto». "
     "Reglas del debate: respetar turnos, citar evidencias, responder al argumento y no a la persona, y reconocer cuando otra postura tiene razón en algo.")
build(
    OA, 6, F,
    use="Aprenderé a debatir sobre el perfeccionamiento, la defensa y los riesgos del Estado de derecho, con argumentos respetuosos y consecuencias claras.",
    prior=["Sé que el Estado de derecho enfrenta riesgos y tiene defensas.", "Sé citar evidencias.", "Sé distinguir un argumento de una opinión sin razones."],
    explain=[
        "Un debate es una conversación ordenada donde se defienden posturas con razones. Un argumento tiene una afirmación y una razón que la apoya. Por ejemplo: «El plan es útil porque quienes conocen las instituciones participan mejor». Una opinión sin razón, como «me parece mal», no es un argumento.",
        "Debatir bien exige respetar turnos, responder a lo que la otra persona dijo y no atacarla. Un ataque a la persona en vez de a su argumento se llama falacia. También hay que mirar las consecuencias: qué beneficios tiene una propuesta, qué costos y a quiénes afecta. Una propuesta puede ser buena en la idea y débil en cómo se cumple.",
        "Perfeccionar el Estado de derecho es mejorar sus instituciones sin eliminar sus límites; defenderlo es actuar cuando se amenaza; reconocer sus riesgos es mirar lo que puede fallar. Cada persona puede cambiar de postura si recibe mejores razones.",
    ],
    vocab=[("argumento", "afirmación acompañada de una razón que la apoya"), ("falacia", "razonamiento engañoso, como atacar a la persona en vez de su argumento"), ("consecuencia", "efecto que produce una decisión"), ("perfeccionar", "mejorar algo que ya existe"), ("contraargumento", "razón que responde a un argumento contrario")],
    worked=[
        ("Reconocer un argumento", "«El plan es bueno porque quienes conocen las instituciones participan mejor». ¿Es un argumento?", ["Tiene una afirmación: el plan es bueno.", "Tiene una razón: la gente informada participa mejor."], "Sí, tiene afirmación y razón"),
        ("Reconocer una falacia", "«No escuchen a ese padre, ni siquiera estudió». ¿Responde al argumento?", ["Habla de la persona y no de su razón.", "Eso es una falacia."], "No, es un ataque a la persona"),
    ],
    mistakes=[("Responder a la persona y no a su argumento.", "Se cambia lo que se discute y no se aporta razón.", "Resume el argumento de la otra persona y respóndelo con una razón."),
              ("Creer que cambiar de opinión es perder.", "El objetivo del debate es acercarse a la mejor razón.", "Reconoce lo que te convence de otra postura.")],
    T=[
        ("{F} ¿Quién presenta el Argumento B?", "Un padre", "La ficha lo indica."),
        ("{F} ¿Cuál es la propuesta en discusión?", "Crear un plan para que los colegios enseñen cómo funcionan los poderes del Estado y cómo participar", "Es la primera frase de la ficha."),
        ("{F} ¿Qué regla dice cómo responder a otra persona?", "Responder al argumento y no a la persona", "Está en las reglas del debate."),
        ("{F} ¿Qué razón da el Argumento A? A) Que quien conoce derechos e instituciones participa mejor y detecta abusos B) Que el colegio tiene muchas materias", "A) Que quien conoce derechos e instituciones participa mejor y detecta abusos", "La profesora lo dice; la otra razón es del Argumento B."),
        ("{F} El Argumento B teme que el plan quede solo en el papel. ¿Qué consecuencia señala? A) Que no se cumpla en la práctica B) Que sea muy caro", "A) Que no se cumpla en la práctica", "El padre habla de que se quede en el papel."),
        ("{F} ¿Qué argumento responde al Argumento B? A) El Argumento C, que propone prácticas reales B) El Argumento A, que no menciona el tiempo", "A) El Argumento C, que propone prácticas reales", "El estudiante ofrece una condición para que el plan funcione."),
        ("{F} Una persona dice: «A ese estudiante no hay que creerle, tiene 15 años». ¿Qué error comete? A) Ataca a la persona y no al argumento B) Usa una evidencia", "A) Ataca a la persona y no al argumento", "Es una falacia, según el vocabulario de la clase."),
        ("{F} ¿Cuál es un buen contraargumento al Argumento B? A) El riesgo de quedar en el papel se evita si el plan incluye prácticas reales B) El padre no sabe de educación", "A) El riesgo de quedar en el papel se evita si el plan incluye prácticas reales", "Responde la razón con una condición, sin atacar a la persona."),
        ("{F} ¿Qué consecuencia positiva espera la profesora si el plan funciona? A) Que las personas detecten abusos y participen mejor B) Que los colegios tengan más horas libres", "A) Que las personas detecten abusos y participen mejor", "Es la razón del Argumento A."),
        ("{F} ¿Cuál de estas intervenciones sigue mejor las reglas? A) «Entiendo tu preocupación por el tiempo; propongo dedicar solo una hora al mes» B) «Tu idea es ridícula»", "A) «Entiendo tu preocupación por el tiempo; propongo dedicar solo una hora al mes»", "Responde al argumento y aporta una solución."),
        ("{F} Una persona cambia de postura tras oír al estudiante. Según la clase, ¿es una debilidad? A) No, es acercarse a la mejor razón B) Sí, pierde el debate", "A) No, es acercarse a la mejor razón", "La explicación dice que se puede cambiar de postura con mejores razones."),
        ("{F} Para votar el plan, ¿qué dato de ejemplo ayudaría a evaluar su costo? A) Cuántas horas exigiría y cuánto cuesta preparar al personal B) Cuántos estudiantes de otros países hay en el colegio", "A) Cuántas horas exigiría y cuánto cuesta preparar al personal", "Los datos sobre tiempo y costo permiten evaluar las consecuencias."),
        ("{F} ¿Qué postura final tiene razón, consecuencia y límite? A) Apoyo el plan porque forma ciudadanía informada; su límite es que sin prácticas reales podría quedar en el papel B) Apoyo el plan porque sí", "A) Apoyo el plan porque forma ciudadanía informada; su límite es que sin prácticas reales podría quedar en el papel", "Contiene razón y límite; la otra no da ninguna razón."),
    ],
    ctx=("En un debate de curso, una estudiante dice: «La mayoría piensa así, por lo tanto tiene razón». ¿Qué falla? A) Que muchas personas piensen algo no prueba que sea cierto B) Nada: si la mayoría lo cree, es suficiente evidencia", "A) Que muchas personas piensen algo no prueba que sea cierto", "Un argumento necesita razones y evidencias, no solo cantidad de personas."),
    sc=[("¿Qué es un argumento?", "Una afirmación acompañada de una razón que la apoya", "Así se define en el vocabulario."),
        ("En Historia: ¿Qué es una falacia?", "Un razonamiento engañoso, como atacar a la persona en vez de su argumento", "Así se define en la clase."),
        ("¿Qué se debe mirar al evaluar una propuesta?", "Sus consecuencias: beneficios, costos y a quiénes afecta", "La explicación lo indica.")],
    op=("Prepara un debate de dos minutos sobre la propuesta de la ficha. Escribe tu postura en una frase, dos argumentos con evidencia o razón, la respuesta a un argumento contrario y una consecuencia que debería vigilarse. Puedes elegir entre apoyarla, rechazarla o apoyarla con condiciones. {F}",
        "Postura: apoyar con condiciones. Argumentos: forma ciudadanía informada; ayuda a detectar abusos. Respuesta: para que no quede en el papel, incluir prácticas reales. Consecuencia a vigilar: el tiempo que consume.",
        ["la postura es clara", "los argumentos tienen razón", "responde a un contraargumento sin atacar a la persona"], ["texto de la postura", "dos argumentos y una respuesta"], ["dar opiniones sin razón", "atacar a quien piensa distinto"],
        "Pide que diga qué razón de otra postura le parece válida."),
    reinforce="Explica a alguien de tu casa la diferencia entre un argumento y una opinión sin razón.",
    extend="Observa una discusión de redes o de la tele y anota si responde al argumento o a la persona.",
)

OA = "HI2M OA 24"

# ================================================================ OA 24, clase 1
F = ("Ficha 1 (desafíos de ejemplo; las cifras son de ejemplo y no son datos reales de Chile). "
     "Desafíos pendientes que suelen discutirse en el país: (1) reducir la pobreza y la desigualdad; (2) garantizar los derechos de los grupos discriminados; "
     "(3) lograr un desarrollo sustentable, que satisface las necesidades de hoy sin comprometer las de las generaciones futuras; (4) perfeccionar el sistema político; (5) fortalecer la relación con los países vecinos. "
     "Actores: el Estado, que tiene deberes; las empresas; las organizaciones sociales; las familias; cada persona. "
     "Dato de ejemplo: en una región ficticia el 20 % de 5.000 hogares vive en pobreza.")
build(
    OA, 1, F,
    use="Aprenderé a situar los desafíos pendientes del país y a distinguir los deberes del Estado y la responsabilidad de las demás personas.",
    prior=["Sé que Chile tiene un Estado de derecho con instituciones y derechos.", "Sé leer datos de ejemplo y calcular porcentajes sencillos.", "Sé qué es un grupo discriminado."],
    explain=[
        "Un desafío pendiente es un problema importante que la sociedad aún no resuelve del todo. En Chile se suelen discutir cinco: reducir la pobreza y la desigualdad, garantizar los derechos de grupos históricamente discriminados, lograr un desarrollo sustentable, perfeccionar el sistema político y fortalecer la relación con los países vecinos.",
        "El desarrollo sustentable busca satisfacer las necesidades de hoy sin comprometer las de las generaciones futuras. La desigualdad es una distancia grande entre lo que reciben distintos grupos, por ejemplo de ingresos o de acceso a servicios. La pobreza es no tener lo necesario para vivir con dignidad. El sistema político es el conjunto de reglas e instituciones con que se eligen las autoridades y se toman las decisiones públicas.",
        "Los actores son varios. El Estado tiene deberes, como garantizar derechos y crear políticas públicas, que son decisiones para resolver problemas colectivos. Pero también tienen responsabilidad las empresas, las organizaciones, las familias y cada persona. Un error frecuente es pensar que todo depende solo del gobierno.",
    ],
    vocab=[("desafío pendiente", "problema importante que aún no se resuelve del todo"), ("desarrollo sustentable", "desarrollo que satisface necesidades de hoy sin comprometer las de generaciones futuras"), ("desigualdad", "distancia grande entre lo que reciben distintos grupos"), ("política pública", "decisión del Estado para resolver un problema colectivo"), ("deber del Estado", "obligación que el Estado tiene hacia las personas, como garantizar derechos"), ("sistema político", "reglas e instituciones con que se eligen las autoridades y se toman decisiones públicas")],
    worked=[
        ("Clasificar un desafío", "Un río cercano a una ciudad recibe desechos y los pescadores ya no pueden trabajar. ¿Con qué desafío se relaciona?", ["Hay un daño ambiental que afecta a las personas de hoy y del futuro.", "Eso se relaciona con el desarrollo sustentable."], "Con el desarrollo sustentable"),
        ("Calcular con un dato de ejemplo", "En 4.000 hogares de ejemplo, el 25 % vive en pobreza. ¿Cuántos hogares son?", ["Se calcula el 25 % de 4.000: 4.000 × 0,25.", "El resultado es 1.000."], "1.000 hogares"),
    ],
    mistakes=[("Creer que los desafíos dependen solo del gobierno.", "Se olvida la responsabilidad de empresas, organizaciones y personas.", "Nombra el deber del Estado y una acción que cada actor puede hacer."),
              ("Confundir pobreza con desigualdad.", "Una es carecer de lo necesario; la otra es una distancia entre grupos.", "Define cada una con tus palabras y da un ejemplo.")],
    T=[
        ("{F} ¿Cuántos desafíos enumera la ficha?", "Cinco", "La ficha los numera del 1 al 5."),
        ("{F} ¿Qué es el desarrollo sustentable?", "El que satisface las necesidades de hoy sin comprometer las de las generaciones futuras", "Así lo define la ficha."),
        ("{F} ¿Qué actores menciona la ficha además del Estado?", "Las empresas, las organizaciones sociales, las familias y cada persona", "La ficha los enumera."),
        ("=", "{F} ¿Cuántos hogares de la región ficticia viven en pobreza?", "5000*0.2", "Se calcula el 20 % de 5.000 hogares.", " hogares"),
        ("{F} Un colegio de una zona rural no tiene internet y los estudiantes se atrasan. ¿Con qué desafío se relaciona más? A) Reducir la desigualdad B) Fortalecer la relación con los vecinos", "A) Reducir la desigualdad", "La falta de acceso a servicios muestra una distancia entre grupos."),
        ("{F} Un país vecino y Chile discuten cómo cuidar un río que comparten. ¿Qué desafío es? A) Relación con los países vecinos B) Perfeccionar el sistema político", "A) Relación con los países vecinos", "Es un tema compartido con otro país."),
        ("{F} Una persona en silla de ruedas no puede entrar a una oficina pública porque solo tiene escalas. ¿Qué desafío ilustra? A) Garantizar derechos de grupos discriminados B) Desarrollo sustentable", "A) Garantizar derechos de grupos discriminados", "La falta de acceso afecta a un grupo históricamente excluido."),
        ("{F} Una fábrica quiere duplicar su producción usando toda el agua de un lago en un año. ¿Cumple con el desarrollo sustentable? A) No, compromete el agua de las generaciones futuras B) Sí, porque produce más", "A) No, compromete el agua de las generaciones futuras", "Gastar un recurso sin pensar en el futuro contradice la definición."),
        ("{F} Un compañero dice: «Solo el gobierno debe resolver los desafíos». ¿Qué corrección harías? A) El Estado tiene deberes, pero empresas, organizaciones y personas también tienen responsabilidad B) Tiene razón, porque el Estado tiene el poder", "A) El Estado tiene deberes, pero empresas, organizaciones y personas también tienen responsabilidad", "La ficha nombra varios actores."),
        ("{F} ¿Qué acción personal aporta al desafío del desarrollo sustentable? A) Separar los residuos de la casa B) Esperar que otros lo resuelvan", "A) Separar los residuos de la casa", "Es una acción individual de cuidado ambiental."),
        ("{F} Un grupo propone cambiar cómo se eligen y se controlan las autoridades para que representen mejor a la gente. ¿Con qué desafío se relaciona? A) Perfeccionar el sistema político B) Reducir la pobreza", "A) Perfeccionar el sistema político", "Las reglas para elegir y controlar autoridades son parte del sistema político."),
        ("¿Cuál es la mejor pregunta de investigación? A) ¿Qué desafíos pendientes tiene Chile y quién tiene qué responsabilidad frente a cada uno? B) ¿Qué país es el mejor?", "A) ¿Qué desafíos pendientes tiene Chile y quién tiene qué responsabilidad frente a cada uno?", "La pregunta A se puede investigar con datos; la B es un ranking sin criterio."),
        ("{F} Un afiche dice: «Todo desafío se resuelve con una sola ley». ¿Qué problema tiene? A) Ignora que intervienen varios actores y causas B) Pide cambiar demasiadas cosas a la vez", "A) Ignora que intervienen varios actores y causas", "Los desafíos son complejos y requieren acciones de varios actores."),
    ],
    ctx=("En una comuna ficticia faltan áreas verdes, una parte de los hogares tiene bajos ingresos y los vecinos pelean por un terreno. ¿Qué actor puede aportar a la solución? A) El municipio, las organizaciones de vecinos y cada persona B) Solo el Presidente", "A) El municipio, las organizaciones de vecinos y cada persona", "Los desafíos exigen varios actores, según la ficha."),
    sc=[("¿Qué es un desafío pendiente?", "Un problema importante que aún no se resuelve del todo", "Así se define en el vocabulario."),
        ("¿Qué es una política pública?", "Una decisión del Estado para resolver un problema colectivo", "Así se define en la clase."),
        ("=", "En 2.000 hogares de ejemplo el 15 % vive en pobreza. ¿Cuántos hogares son?", "2000*0.15", "Se calcula el 15 % de 2.000.", " hogares")],
    op=("Dibuja una tabla con tres columnas: desafío, deber del Estado y qué puede hacer una persona. Completa dos filas con estos desafíos: (a) desarrollo sustentable; (b) derechos de los grupos discriminados. {F}",
        "(a) Desarrollo sustentable: el Estado regula el uso de recursos; una persona puede cuidar el agua y separar residuos. (b) Derechos de grupos discriminados: el Estado crea leyes y servicios accesibles; una persona puede tratar con respeto y no discriminar.",
        ["completa las dos filas", "distingue deber del Estado y acción personal", "usa palabras de la clase"], ["tabla de tres columnas"], ["poner todo en el Estado", "dar una acción personal sin relación con el desafío"],
        "Pide que explique por qué la acción personal sola no basta."),
    reinforce="Explica a alguien de tu casa dos desafíos del país y quién debe actuar en cada uno.",
    extend="Anota un problema de tu barrio y di cuál de los cinco desafíos se parece más.",
)

# ================================================================ OA 24, clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; sus datos son de ejemplo y no son estadísticas reales). "
     "Fuente A, informe de un instituto de estudios, sobre una ciudad ficticia: «El ingreso del 20 % de hogares más ricos es 8 veces el del 20 % más pobre.» "
     "Fuente B, declaración de una agrupación de vecinos de esa ciudad: «Los barrios del norte no tienen transporte nocturno ni consultorio abierto los fines de semana.» "
     "Fuente C, comunicado del municipio: «Este año se destinó un 10 % más de recursos a los barrios del norte.»")
build(
    OA, 2, F,
    use="Aprenderé a interrogar fuentes sobre desafíos del país, preguntando quién las escribe, qué datos usa y cuánto prueban.",
    prior=["Sé que Chile tiene desafíos pendientes y que varios actores tienen responsabilidad.", "Sé qué es la procedencia de una fuente.", "Sé calcular porcentajes y razones sencillas."],
    explain=[
        "Los datos sobre un desafío, como la desigualdad, pueden venir de fuentes con orígenes distintos. Un instituto de estudios produce informes con datos; una agrupación de vecinos expresa la experiencia de quienes viven un problema; un municipio informa sus acciones. Cada una aporta algo, pero con un propósito diferente.",
        "Para interrogar un dato conviene preguntar quién lo produjo, cuándo, con qué método y a qué grupo se refiere. Una razón de 8 veces significa que un grupo recibe ocho veces lo que recibe otro. Un aumento de 10 % puede sonar grande, pero depende de cuánto era antes: 10 % de una cifra pequeña sigue siendo poco.",
        "Una conclusión proporcional diría, por ejemplo: «según el instituto, la brecha es grande en esa ciudad», no «en todo Chile la brecha es esa». Las fuentes de ejemplo de este cuaderno no representan al país.",
    ],
    vocab=[("brecha", "diferencia entre lo que tienen dos grupos"), ("razón", "comparación entre dos cantidades, por ejemplo «8 veces»"), ("método", "forma en que se obtuvo un dato"), ("declaración", "texto con que un grupo expresa su postura o su experiencia"), ("conclusión proporcional", "conclusión que no dice más de lo que muestra la evidencia")],
    worked=[
        ("Leer una razón", "La Fuente A dice que el 20 % más rico recibe 8 veces el ingreso del 20 % más pobre. Si el 20 % más pobre recibe 100 unidades de ejemplo, ¿cuánto recibe el más rico?", ["Se multiplica la cifra por 8.", "100 × 8 = 800."], "800 unidades de ejemplo"),
        ("Interrogar a un municipio", "¿Qué hay que preguntar a la Fuente C antes de creer que el problema se resolvió?", ["Un 10 % más no dice cuánto era el monto inicial.", "Tampoco dice si el transporte y el consultorio mejoraron."], "Cuánto era el monto inicial y si mejoraron los servicios"),
    ],
    mistakes=[("Creer que un porcentaje grande siempre es una mejora grande.", "No se mira la cifra de partida ni el resultado real.", "Pide la cifra inicial y el efecto en las personas."),
              ("Generalizar los datos de una ciudad a todo el país.", "Se cambia de escala sin evidencia.", "Escribe a qué ciudad o grupo se refiere el dato.")],
    T=[
        ("{F} ¿Quién escribe la Fuente B?", "Una agrupación de vecinos de la ciudad", "La ficha lo indica."),
        ("{F} Según la Fuente A, ¿el ingreso de qué grupo es 8 veces el del otro?", "El del 20 % de hogares más ricos", "La fuente compara al grupo más rico con el más pobre."),
        ("{F} ¿Qué falta en los barrios del norte según la Fuente B?", "Transporte nocturno y consultorio abierto los fines de semana", "La fuente lo menciona."),
        ("=", "{F} Si el 20 % más pobre recibe 150 unidades de ejemplo, ¿cuánto recibe el 20 % más rico según la Fuente A?", "150*8", "Se multiplica por la razón de 8.", " unidades"),
        ("{F} ¿Qué fuente sirve mejor para conocer la experiencia de quienes viven el problema? A) La Fuente B B) La Fuente C", "A) La Fuente B", "La agrupación de vecinos expresa esa experiencia."),
        ("{F} ¿Qué se puede esperar de la Fuente C por su procedencia? A) Que informe lo que hizo el municipio B) Que critique al municipio", "A) Que informe lo que hizo el municipio", "Un comunicado explica los actos de quien lo escribe."),
        ("=", "{F} Un municipio dice «aumentamos 10 % el presupuesto» de un programa que antes tenía 20 unidades de ejemplo. ¿Cuántas unidades aumentó?", "20*0.1", "Se calcula el 10 % de 20.", " unidades"),
        ("{F} Un compañero dice: «La Fuente A prueba que en Chile la desigualdad es 8 veces». ¿Qué corriges? A) El dato es de una ciudad ficticia, no de todo el país B) Tiene razón porque es un instituto", "A) El dato es de una ciudad ficticia, no de todo el país", "Hay que respetar la escala del dato."),
        ("{F} ¿Por qué el comunicado C no basta para decir que el problema de los barrios del norte se resolvió? A) Informa más recursos, pero no muestra si llegó el transporte ni el consultorio B) Porque es del municipio", "A) Informa más recursos, pero no muestra si llegó el transporte ni el consultorio", "Un aumento de recursos no es lo mismo que un servicio mejorado."),
        ("{F} ¿Qué dato adicional ayudaría a comparar las Fuentes B y C? A) Horarios del consultorio y del transporte antes y después B) La cantidad de noticias publicadas sobre el municipio", "A) Horarios del consultorio y del transporte antes y después", "Permitiría verificar si hubo mejora real."),
        ("{F} ¿Qué conclusión es proporcional con las tres fuentes? A) En esta ciudad hay una brecha grande, los vecinos reclaman servicios y el municipio informa más recursos; falta saber si mejoraron B) La desigualdad ya se resolvió en el país", "A) En esta ciudad hay una brecha grande, los vecinos reclaman servicios y el municipio informa más recursos; falta saber si mejoraron", "Une las tres fuentes y señala lo que falta."),
        ("=", "{F} Una fuente D dice: «Antes el consultorio del norte atendía 40 horas semanales; hoy atiende 60». ¿En qué porcentaje aumentó la atención?", "(60-40)/40*100", "Se divide el aumento entre el valor anterior y se multiplica por cien.", " %"),
        ("{F} Si la fuente D del ejercicio anterior viniera de un registro del consultorio, ¿qué ventaja tendría? A) Aportaría un dato comprobable que otros pueden revisar B) Sería la opinión de un vecino", "A) Aportaría un dato comprobable que otros pueden revisar", "Los registros pueden verificarse."),
    ],
    ctx=("Un diario ficticio titula: «Pobreza bajó a la mitad» y el texto explica que pasó de 20 % a 18 % en una comuna. ¿Qué problema tiene el titular? A) Exagera, porque 20 % a 18 % no es la mitad B) No dice el nombre del periodista", "A) Exagera, porque 20 % a 18 % no es la mitad", "Un cambio de 2 puntos no es reducirla a la mitad."),
    sc=[("¿Qué es una brecha?", "Una diferencia entre lo que tienen dos grupos", "Así se define en el vocabulario."),
        ("¿Qué hay que preguntar a un dato?", "Quién lo produjo, cuándo, con qué método y a qué grupo se refiere", "La explicación lo indica."),
        ("=", "Si el 20 % más pobre de una ciudad de ejemplo recibe 90 unidades y el más rico recibe 8 veces eso, ¿cuánto recibe el más rico?", "90*8", "Se multiplica por 8.", " unidades")],
    op=("Haz una tabla con las Fuentes A, B y C: quién la escribe, qué dato o experiencia aporta y qué no puede probar. Luego escribe dos frases: una que describa la brecha de la ciudad y otra que diga qué dato faltaría para decidir si mejoró. {F}",
        "A: instituto; razón de 8 veces; no prueba la situación de todo Chile. B: vecinos; falta de servicios; no mide cuántas personas afecta. C: municipio; 10 % más de recursos; no prueba que haya mejorado el servicio.",
        ["identifica autor y aporte", "indica el límite de cada fuente", "su conclusión es proporcional"], ["tabla", "dos frases"], ["generalizar a todo el país", "creer que un aumento de recursos prueba una mejora"],
        "Pide que diga cómo comprobaría si el transporte nocturno llegó."),
    reinforce="Explica a alguien de tu casa por qué un porcentaje solo no basta para saber si algo mejoró.",
    extend="Mira una noticia con un dato numérico y anota quién produjo el dato.",
)

# ================================================================ OA 24, clase 3
F = ("Ficha 3 (posturas de ejemplo sobre un mismo desafío, escritas para este cuaderno). "
     "Tema: una ciudad ficticia puede instalar una planta de procesamiento de minerales cerca de un río. "
     "Postura 1, sindicato de trabajadores: «La planta crearía 300 empleos estables para la ciudad». "
     "Postura 2, comunidad de agricultores: «El río es nuestra única fuente de agua; no queremos riesgo de contaminación». "
     "Postura 3, ministerio de medio ambiente de ejemplo: «Se aprobará solo con estudios independientes y controles de agua cada mes». "
     "Escalas: local (la ciudad y el río), regional (todas las comunas que usan ese río) y nacional (ingresos del país y cuidado del ambiente).")
build(
    OA, 3, F,
    use="Aprenderé a comparar perspectivas y escalas sobre un desafío del país, entendiendo qué valora cada actor y qué deberes tiene el Estado.",
    prior=["Sé que hay desafíos como el desarrollo sustentable.", "Sé interrogar fuentes.", "Sé distinguir valores e intereses."],
    explain=[
        "Un mismo desafío se ve distinto según quién lo mire. Un sindicato valora el empleo; una comunidad agrícola valora el agua; el Estado debe cuidar tanto el trabajo como el ambiente y las generaciones futuras. Un interés es lo que un grupo quiere lograr; un valor es la idea que considera importante. Los intereses pueden chocar sin que alguien actúe de mala fe.",
        "También cambian las escalas. En lo local pesa el empleo de una ciudad; en lo regional, el agua de varias comunas; en lo nacional, los ingresos del país y el ambiente. Una decisión puede beneficiar a una escala y perjudicar a otra, por eso hay que preguntar a quiénes afecta.",
        "Una buena comparación busca puntos de acuerdo. En el ejemplo, todos podrían aceptar un proyecto si hay estudios independientes, controles frecuentes y sanciones. El Estado tiene el deber de fiscalizar, y las empresas y las personas, la responsabilidad de cumplir.",
    ],
    vocab=[("interés", "lo que un grupo quiere lograr"), ("fiscalizar", "controlar que se cumplan las leyes y las reglas"), ("sustentable", "que se puede mantener sin comprometer a las generaciones futuras"), ("estudio independiente", "estudio hecho por quienes no tienen interés directo en el resultado"), ("generaciones futuras", "personas que vivirán después de nosotros")],
    worked=[
        ("Reconocer el interés", "¿Qué interés defiende la Postura 2?", ["Dice que el río es su única fuente de agua.", "Quiere evitar riesgos de contaminación."], "Proteger el agua del río"),
        ("Reconocer el deber del Estado", "¿Qué deber muestra la Postura 3?", ["Dice que se aprobará solo con estudios independientes y controles.", "Eso es fiscalizar."], "Fiscalizar para cuidar el ambiente y el trabajo"),
    ],
    mistakes=[("Pensar que un grupo tiene razón y otro no, sin mirar sus valores.", "Cada postura protege algo importante.", "Pregunta qué valor defiende cada una y busca un punto de encuentro."),
              ("Olvidar a las generaciones futuras.", "Se decide solo por lo de hoy.", "Pregunta cómo quedará el recurso en el futuro.")],
    T=[
        ("{F} ¿Cuántos empleos creará la planta según la Postura 1?", "300", "El sindicato lo afirma en su postura."),
        ("{F} ¿Qué teme la comunidad de agricultores?", "Que el río se contamine", "La Postura 2 lo señala."),
        ("{F} ¿Con qué frecuencia propone la Postura 3 controlar el agua?", "Cada mes", "La ficha lo dice."),
        ("{F} ¿Qué interés defiende la Postura 1? A) El empleo B) El agua", "A) El empleo", "El sindicato habla de empleos estables."),
        ("{F} ¿A qué escala se refiere el agua que usan varias comunas? A) Regional B) Local", "A) Regional", "Varias comunas comparten el río."),
        ("{F} ¿Cuál de estas es una condición de la Postura 3? A) Estudios independientes B) Prohibir toda planta en el país", "A) Estudios independientes", "La ficha dice que se aprobará solo con ellos."),
        ("{F} ¿Qué punto de acuerdo posible hay entre las Posturas 1 y 2? A) Aprobar la planta con estudios independientes, controles mensuales y sanciones si se contamina B) Aprobar la planta sin controles", "A) Aprobar la planta con estudios independientes, controles mensuales y sanciones si se contamina", "Protege el empleo y el agua a la vez."),
        ("{F} Si la planta crea 300 empleos pero contamina el río, ¿qué queda perjudicado? A) La escala regional y las generaciones futuras B) Solo los dueños de la planta", "A) La escala regional y las generaciones futuras", "La contaminación afecta a todas las comunas que usan el río."),
        ("{F} Un compañero dice: «Los agricultores se oponen al desarrollo». ¿Qué corrección harías? A) Defienden el agua; no se oponen necesariamente al desarrollo B) Tiene razón, porque rechazan la planta", "A) Defienden el agua; no se oponen necesariamente al desarrollo", "Su interés es proteger el agua, y puede coexistir con proyectos con controles."),
        ("{F} ¿Por qué el Estado debe fiscalizar y no confiar solo en la buena voluntad de la empresa? A) Porque debe garantizar derechos y proteger el ambiente para todas las personas B) Porque las empresas siempre mienten", "A) Porque debe garantizar derechos y proteger el ambiente para todas las personas", "Es un deber del Estado, según la clase; no se supone mala fe."),
        ("{F} ¿Qué evidencia ayudaría a decidir entre las posturas? A) Un estudio independiente sobre el riesgo para el agua B) La opinión de una sola persona", "A) Un estudio independiente sobre el riesgo para el agua", "Un estudio independiente aporta datos comprobables."),
        ("{F} Si el estudio de la pregunta anterior mostrara riesgo alto de contaminación, ¿qué debería ocurrir? A) Exigir medidas o rechazar el proyecto B) Aprobarlo igual para tener empleos", "A) Exigir medidas o rechazar el proyecto", "El deber del Estado es proteger el ambiente y a las generaciones futuras."),
        ("{F} ¿Qué propuesta combina empleo, agua y control? A) Aprobar con estudios independientes, controles mensuales y sanciones por incumplir B) Aprobar sin condiciones", "A) Aprobar con estudios independientes, controles mensuales y sanciones por incumplir", "Une los intereses de las tres posturas."),
    ],
    ctx=("Una comunidad ficticia debate si construir un camino a un lago. Algunos piden turismo y empleo; otros, proteger el humedal. ¿Qué pregunta ayuda más a comparar? A) ¿Qué valores defiende cada grupo y a quiénes afecta a corto y largo plazo? B) ¿Qué grupo reúne más personas?", "A) ¿Qué valores defiende cada grupo y a quiénes afecta a corto y largo plazo?", "Comparar perspectivas exige mirar valores y consecuencias."),
    sc=[("¿Qué es un interés?", "Lo que un grupo quiere lograr", "Así se define en el vocabulario."),
        ("¿Qué significa fiscalizar?", "Controlar que se cumplan las leyes y reglas", "Así se define en la clase."),
        ("¿Por qué conviene buscar puntos de acuerdo?", "Porque los intereses pueden conciliarse con reglas y controles", "La explicación lo indica.")],
    op=("Haz un cuadro con las Posturas 1, 2 y 3: interés, escala y qué le pediría a las demás. Después escribe una propuesta de tres líneas que cuide empleo, agua y fiscalización. Puedes usar las condiciones de la Postura 3 como base. {F}",
        "Postura 1: empleo, escala local; pide continuar. Postura 2: agua, escala regional; pide protección. Postura 3: control; escala nacional; pide estudios y controles. Propuesta: planta con estudios independientes, controles mensuales y sanciones.",
        ["identifica el interés y la escala de cada postura", "su propuesta incluye control del Estado", "no descalifica a ningún grupo"], ["cuadro", "propuesta de tres líneas"], ["decir que un grupo está equivocado sin razones", "no incluir fiscalización"],
        "Pide que explique qué haría si el estudio mostrara riesgo alto."),
    reinforce="Explica a alguien de tu casa dos intereses que chocan en un problema del barrio y cómo se podrían conciliar.",
    extend="Piensa en una decisión de tu colegio y anota qué grupos tienen intereses distintos.",
)

# ================================================================ OA 24, clase 4
F = ("Ficha 4 (cadena de causas de ejemplo para una comuna ficticia, «Costa Clara»). "
     "Situación: los jóvenes de Costa Clara abandonan la comuna al terminar el colegio. "
     "Causas de largo plazo: la pesca artesanal tiene menos ingresos; pocos cupos en educación superior cercana; transporte caro a la ciudad. "
     "Detonante: cerró la única planta procesadora de pescado. "
     "Cambios después: el municipio abrió un centro de formación técnica. "
     "Continuidades: el transporte sigue siendo caro y la mayoría de los empleos sigue siendo estacional. "
     "Dato de ejemplo: de 200 jóvenes que terminaron el colegio, 130 se fueron de la comuna.")
build(
    OA, 4, F,
    use="Aprenderé a relacionar causas, cambios y continuidades de un desafío pendiente y a ver cómo se vinculan la pobreza, el trabajo, la educación y el territorio.",
    prior=["Sé qué es un desafío pendiente.", "Sé distinguir causas de largo plazo y detonante.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Los desafíos del país tienen causas que se encadenan. Una comuna sin empleo estable pierde jóvenes; con menos jóvenes, hay menos actividad; con menos actividad, hay menos empleo. A esto se le llama círculo vicioso. Para entenderlo se separan causas de largo plazo, que se acumulan, y el detonante, que desencadena la crisis.",
        "Después se miran los cambios, que son las medidas nuevas, y las continuidades, que son los problemas que siguen. Un cambio como un centro de formación puede ayudar, pero si el transporte sigue caro y el empleo es estacional, el desafío no se resuelve del todo. Conviene calcular proporciones: si 130 de 200 jóvenes se van, se van más de la mitad.",
        "Para evitar errores, no se debe atribuir todo a una sola causa. Un hecho puede tener varias y cada una pesa distinto. También hay que decir qué evidencia falta para saber si una medida realmente produjo un cambio.",
    ],
    vocab=[("círculo vicioso", "cadena de efectos que se refuerzan y empeoran el problema"), ("causa de largo plazo", "razón que se acumula durante años"), ("detonante", "hecho que desencadena una crisis que ya tenía causas previas"), ("estacional", "que depende de ciertas épocas del año"), ("migración", "traslado de personas de un lugar a otro para vivir")],
    worked=[
        ("Separar causa y detonante", "¿El cierre de la planta procesadora de Costa Clara es causa de largo plazo o detonante?", ["Ocurrió en un momento preciso.", "Desencadenó la salida cuando ya había problemas previos."], "Detonante"),
        ("Calcular una proporción", "Si de 300 estudiantes de ejemplo se van 90 de la comuna, ¿qué porcentaje es?", ["Se divide 90 entre 300: 0,3.", "Se multiplica por 100."], "30 %"),
    ],
    mistakes=[("Decir que el cierre de la planta explica todo.", "Se ignoran las causas de largo plazo.", "Separa causas acumuladas y detonante."),
              ("Creer que un centro de formación resuelve todo el problema.", "Se olvidan continuidades como el transporte y el empleo estacional.", "Pregunta qué sigue igual.")],
    T=[
        ("{F} ¿Cómo se llama la comuna de la ficha?", "Costa Clara", "La ficha la nombra."),
        ("{F} ¿Qué detonó la salida de jóvenes?", "El cierre de la única planta procesadora de pescado", "La ficha lo señala como detonante."),
        ("{F} ¿Qué abrió el municipio como cambio?", "Un centro de formación técnica", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos jóvenes se quedaron en la comuna?", "200-130", "Se resta los que se fueron al total.", " jóvenes"),
        ("=", "{F} ¿Qué porcentaje de los jóvenes se fue de la comuna?", "130/200*100", "Se divide 130 entre 200 y se multiplica por cien.", " %"),
        ("{F} ¿Cuál es una causa de largo plazo? A) La pesca artesanal con menos ingresos B) El cierre de la planta", "A) La pesca artesanal con menos ingresos", "Se acumuló durante años; el cierre fue el detonante."),
        ("{F} El transporte sigue caro. ¿Qué es? A) Una continuidad B) Un cambio", "A) Una continuidad", "La ficha lo dice así."),
        ("{F} ¿Qué relación hay entre menos empleo y menos jóvenes en la comuna? A) Se refuerzan: sin empleo se van los jóvenes y sin jóvenes baja la actividad B) No tienen relación", "A) Se refuerzan: sin empleo se van los jóvenes y sin jóvenes baja la actividad", "Es un círculo vicioso."),
        ("{F} ¿Por qué un centro de formación puede no bastar? A) Porque siguen el transporte caro y el empleo estacional B) Porque los centros no sirven", "A) Porque siguen el transporte caro y el empleo estacional", "Las continuidades limitan el efecto del cambio."),
        ("{F} ¿Qué medida enfrenta una continuidad de la ficha? A) Subsidiar el transporte o crear empleos estables B) Subir el precio del pasaje", "A) Subsidiar el transporte o crear empleos estables", "Ataca el transporte caro o el empleo estacional."),
        ("{F} Un compañero dice: «Cerró la planta, por eso se fueron los jóvenes». ¿Cómo lo mejoras? A) Fue el detonante, pero ya había causas como bajos ingresos y transporte caro B) Tiene razón, es la única causa", "A) Fue el detonante, pero ya había causas como bajos ingresos y transporte caro", "Distingue detonante y causas de largo plazo."),
        ("{F} ¿Qué evidencia haría falta para saber si el centro de formación redujo la salida de jóvenes? A) Cuántos jóvenes se van cada año, antes y después B) Cuántos jóvenes viven en la ciudad vecina", "A) Cuántos jóvenes se van cada año, antes y después", "Hay que comparar en el tiempo."),
        ("{F} ¿Qué síntesis tiene una causa, un cambio y una continuidad? A) La pesca con menos ingresos fue causa; se abrió un centro de formación; el transporte sigue caro B) Cerró la planta y todo cambió", "A) La pesca con menos ingresos fue causa; se abrió un centro de formación; el transporte sigue caro", "Reúne los tres elementos."),
    ],
    ctx=("En otra comuna ficticia cierra una mina y 400 de 1.000 trabajadores quedan sin empleo. El municipio ofrece cursos, pero no hay nuevas empresas. ¿Qué continuidad pesa? A) La falta de empleos, aunque haya cursos B) Los cursos mismos", "A) La falta de empleos, aunque haya cursos", "Los cursos son un cambio; la falta de empleo es la continuidad."),
    sc=[("¿Qué es un círculo vicioso?", "Una cadena de efectos que se refuerzan y empeoran el problema", "Así se define en el vocabulario."),
        ("¿Qué es un detonante?", "El hecho que desencadena una crisis que ya tenía causas previas", "Así se define en la clase."),
        ("=", "Si de 250 jóvenes de ejemplo se fueron 100, ¿qué porcentaje se fue?", "100/250*100", "Se divide 100 entre 250 y se multiplica por cien.", " %")],
    op=("Dibuja un esquema para Costa Clara con tres causas de largo plazo, el detonante, un cambio y dos continuidades. Después propone una medida nueva y escribe cómo comprobarías si funcionó. {F}",
        "Causas: ingresos de la pesca, pocos cupos de educación, transporte caro. Detonante: cierre de la planta. Cambio: centro de formación. Continuidades: transporte caro y empleo estacional. Medida: subsidio de transporte; se comprueba comparando cuántos jóvenes se van cada año.",
        ["distingue causa, detonante, cambio y continuidad", "propone una medida coherente", "indica cómo comprobarla"], ["esquema", "medida y forma de comprobarla"], ["poner el detonante como causa de largo plazo", "proponer una medida sin evidencia para evaluarla"],
        "Pide que explique qué dato cambiaría su medida."),
    reinforce="Explica a alguien de tu casa una cadena de causas que haga que un problema se refuerce.",
    extend="Piensa en una comuna que conozcas y anota un cambio y una continuidad en sus servicios.",
)

# ================================================================ OA 24, clase 5
F = ("Ficha 5 (caso de ejemplo para construir una propuesta documentada; todos los datos son de ejemplo). "
     "Pregunta: ¿cómo mejorar la convivencia entre dos países vecinos ficticios, «Norlandia» y «Surlandia», que comparten un río y una frontera? "
     "Evidencia 1, informe de una comisión binacional: «Cada día cruzan 2.000 camiones por el paso fronterizo y la espera promedio es de 6 horas.» "
     "Evidencia 2, declaración de comunidades de la frontera: «Los controles lentos encarecen los productos y dificultan visitar a familiares.» "
     "Evidencia 3, estudio ambiental conjunto: «El río recibe desechos de ambos lados y su calidad empeoró desde hace diez años.» "
     "Evidencia 4, acuerdo vigente entre los países: «Los gobiernos revisarán cada dos años los controles fronterizos y el cuidado del río.»")
build(
    OA, 5, F,
    use="Aprenderé a construir una propuesta documentada sobre un desafío, con evidencias, deberes del Estado, responsabilidades de otros actores y límites.",
    prior=["Sé interrogar fuentes y comparar perspectivas.", "Sé distinguir causas, cambios y continuidades.", "Sé que las relaciones con países vecinos son un desafío del país."],
    explain=[
        "Una propuesta documentada responde una pregunta con evidencias y con medidas concretas. Tiene cuatro partes: el problema explicado con datos, las medidas, los responsables de cada una y los límites o riesgos. Se parece a un argumento, pero termina en acciones.",
        "La relación con los países vecinos se basa en acuerdos que cada Estado debe cumplir, y en la cooperación, que es trabajar juntos por un objetivo común. Los tratados son acuerdos escritos entre Estados. Las comunidades de frontera también tienen un papel: conocen los problemas diarios y pueden participar en las soluciones.",
        "Una medida es mejor si es posible de cumplir, tiene responsables claros y puede evaluarse. Por ejemplo, reducir la espera de 6 a 3 horas puede medirse. Una medida vaga, como «mejorar todo», no.",
    ],
    vocab=[("propuesta documentada", "propuesta con evidencias, responsables y límites"), ("cooperación", "trabajo conjunto por un objetivo común"), ("tratado", "acuerdo escrito entre Estados"), ("binacional", "que reúne a dos países"), ("evaluar", "comprobar si una medida logró lo que buscaba")],
    worked=[
        ("Formular una medida medible", "La espera es de 6 horas. ¿Cómo se formula una meta medible?", ["Se fija una cifra y un plazo.", "Por ejemplo: bajar la espera de 6 a 3 horas en dos años."], "Bajar la espera de 6 a 3 horas en dos años"),
        ("Asignar responsables", "¿Quién debe cuidar el río según el acuerdo de la Evidencia 4?", ["El acuerdo dice que los gobiernos de ambos países revisarán el cuidado del río.", "Ambos Estados comparten la responsabilidad."], "Los gobiernos de ambos países"),
    ],
    mistakes=[("Proponer medidas vagas, como «mejorar la frontera».", "No se pueden evaluar ni asignar a alguien.", "Fija cifra, plazo y responsable."),
              ("Asignar el cuidado del río a un solo país.", "El estudio muestra desechos de ambos lados.", "Reparte responsabilidades entre ambos Estados y las comunidades.")],
    T=[
        ("{F} ¿Cuántos camiones cruzan cada día según la Evidencia 1?", "2.000", "La comisión lo informa."),
        ("{F} ¿Cuánto es la espera promedio?", "6 horas", "La comisión binacional lo indica."),
        ("{F} ¿Cada cuánto revisarán los gobiernos los controles y el río?", "Cada dos años", "La Evidencia 4 lo señala."),
        ("=", "{F} Si la espera baja de 6 horas a 3 horas, ¿en qué porcentaje se redujo?", "(6-3)/6*100", "Se divide lo que bajó entre la espera inicial y se multiplica por cien.", " %"),
        ("{F} ¿Qué problema muestra la Evidencia 3? A) Contaminación del río por ambos lados B) Controles lentos en el paso fronterizo", "A) Contaminación del río por ambos lados", "El estudio habla de desechos de los dos países."),
        ("{F} ¿Qué evidencia expresa la experiencia de las comunidades? A) La Evidencia 2 B) La Evidencia 4", "A) La Evidencia 2", "Es la declaración de comunidades de la frontera."),
        ("{F} Una meta dice: «Bajar la espera de 6 a 3 horas en dos años». ¿Qué tiene de bueno? A) Tiene cifra y plazo, así que se puede evaluar B) Suena ambiciosa", "A) Tiene cifra y plazo, así que se puede evaluar", "Las metas medibles pueden comprobarse."),
        ("{F} Un equipo propone «mejorar todo en la frontera». ¿Qué le falta? A) Medidas concretas, responsables y plazos B) Un nombre más llamativo", "A) Medidas concretas, responsables y plazos", "Sin eso no se puede evaluar."),
        ("{F} ¿Qué responsabilidad pueden asumir las comunidades de frontera? A) Informar problemas y participar en soluciones B) Ninguna", "A) Informar problemas y participar en soluciones", "Conocen los problemas diarios, según la clase."),
        ("{F} ¿Por qué el cuidado del río no puede ser tarea de un solo país? A) Porque ambos países arrojan desechos y comparten el río B) Porque los países vecinos no pueden firmar acuerdos", "A) Porque ambos países arrojan desechos y comparten el río", "El estudio ambiental involucra a los dos lados."),
        ("{F} ¿Qué límite tiene una propuesta de reducir esperas si no se refuerza el control de seguridad? A) Podría reducir la seguridad B) Reduciría los camiones que cruzan", "A) Podría reducir la seguridad", "Hay que equilibrar rapidez y control."),
        ("{F} ¿Qué propuesta tiene medida, responsable y plazo? A) Instalar más puestos de control para bajar la espera a 3 horas, a cargo de ambos gobiernos, en dos años B) Mejorar la frontera pronto", "A) Instalar más puestos de control para bajar la espera a 3 horas, a cargo de ambos gobiernos, en dos años", "Contiene los tres elementos."),
        ("{F} ¿Qué evidencia permitiría evaluar la propuesta anterior? A) La medición de la espera promedio al final de los dos años B) Una encuesta sobre cuántas personas visitan la frontera en verano", "A) La medición de la espera promedio al final de los dos años", "Compara la espera con la meta de 3 horas."),
    ],
    ctx=("Un colegio ficticio de frontera quiere proponer un intercambio escolar con otro país vecino. ¿Qué elementos debe tener la propuesta? A) Objetivo, responsables, plazo y cómo evaluarla B) Un afiche llamativo y la firma del director", "A) Objetivo, responsables, plazo y cómo evaluarla", "Una propuesta documentada incluye esos elementos."),
    sc=[("¿Qué es la cooperación?", "El trabajo conjunto por un objetivo común", "Así se define en el vocabulario."),
        ("¿Qué es un tratado?", "Un acuerdo escrito entre Estados", "Así se define en la clase."),
        ("¿Qué hace evaluable a una medida?", "Tener cifra, plazo y responsable", "La explicación lo indica.")],
    op=("Escribe una propuesta de 6 a 8 líneas para mejorar la convivencia entre Norlandia y Surlandia. Debe usar al menos dos evidencias de la ficha, tres medidas con responsable y plazo y un límite o riesgo. {F}",
        "«Según la comisión binacional, la espera es de 6 horas; según el estudio, el río empeoró. Medidas: bajar la espera a 3 horas en dos años (ambos gobiernos); plan de limpieza del río (ambos gobiernos y comunidades); mesa de diálogo anual con comunidades. Riesgo: reducir la seguridad si se acelera el control».",
        ["usa dos evidencias", "tres medidas con responsable y plazo", "incluye un límite o riesgo"], ["texto de la propuesta"], ["medidas vagas", "no incluir responsables"],
        "Pide que explique cómo medirá si la propuesta funcionó."),
    reinforce="Explica a alguien de tu casa qué hace que una medida sea evaluable.",
    extend="Anota una regla del colegio que se pueda evaluar con una cifra.",
)

# ================================================================ OA 24, clase 6
F = ("Ficha 6 (debate de ejemplo sobre responsabilidades; todo es ficticio). "
     "Propuesta en discusión en la ciudad ficticia de «Valleverde»: cobrar una tarifa a los autos que entren al centro para financiar buses y ciclovías, con el fin de reducir la contaminación. "
     "Argumento A, de una vecina: «Si hay buses y ciclovías, más personas dejarán el auto y respiraremos mejor». "
     "Argumento B, de un comerciante: «La tarifa puede alejar a los clientes y dañar mi negocio». "
     "Argumento C, de un estudiante: «Debe haber transporte público mejor antes de cobrar, y revisar a los dos años si el aire mejoró y si el comercio cayó». "
     "Deberes y responsabilidades: el Estado debe fiscalizar y ofrecer alternativas; las empresas, cumplir normas; las personas, cuidar los bienes comunes.")
build(
    OA, 6, F,
    use="Aprenderé a debatir sobre los desafíos del país, considerando consecuencias, deberes del Estado y responsabilidad de todas las personas, con límites claros.",
    prior=["Sé qué es un argumento y una falacia.", "Sé que los desafíos tienen varios actores.", "Sé evaluar una medida con evidencias."],
    explain=[
        "Un debate sobre un desafío debe considerar consecuencias a corto y largo plazo. Una medida puede mejorar la salud pero encarecer el comercio. Un costo es lo que se pierde o se paga; un beneficio es lo que se gana. Decidir bien no significa que no haya costos, sino que se conozcan, se compartan con justicia y se revisen.",
        "Los deberes del Estado incluyen fiscalizar, ofrecer alternativas y proteger a quienes pueden salir perjudicados. Las empresas deben cumplir las normas, y las personas, cuidar los bienes comunes. Los bienes comunes son aquellos que usamos entre todos, como el aire, el agua y las plazas.",
        "Las medidas deben ser revisables: si no funcionan, se corrigen. Un debate respetuoso reconoce lo que otras posturas aportan, evita ataques personales y distingue lo que se sabe de lo que se cree. Un contraargumento responde a la razón de otra persona; una falacia es un razonamiento engañoso, como atacar a quien habla en vez de responder su razón.",
    ],
    vocab=[("costo", "lo que se pierde o se paga al tomar una decisión"), ("beneficio", "lo que se gana con una decisión"), ("bienes comunes", "recursos que usamos entre todos, como el aire o el agua"), ("revisable", "que puede evaluarse y corregirse con el tiempo"), ("responsabilidad", "obligación de responder por las propias acciones")],
    worked=[
        ("Separar costo y beneficio", "En la propuesta de Valleverde, ¿qué costo señala el comerciante?", ["Habla de clientes que se alejan.", "Eso afecta su ingreso."], "Que los clientes se alejen y dañe su negocio"),
        ("Evaluar una condición", "El estudiante pide revisar en dos años si el aire mejoró. ¿Por qué es útil?", ["Permite comprobar si la medida cumplió su objetivo.", "Permite corregirla si no funcionó."], "Porque la medida se puede evaluar y corregir"),
    ],
    mistakes=[("Defender una medida sin considerar quién paga el costo.", "Se ignora a las personas perjudicadas.", "Pregunta quién gana, quién pierde y cómo se compensa."),
              ("Creer que si hay costos, la medida es mala.", "Toda decisión tiene costos; lo importante es evaluarlos.", "Compara costos y beneficios con evidencias.")],
    T=[
        ("{F} ¿Quién presenta el Argumento B?", "Un comerciante", "La ficha lo indica."),
        ("{F} ¿Qué se busca reducir con la tarifa?", "La contaminación", "Es el fin de la propuesta."),
        ("{F} ¿Cuándo propone el estudiante revisar la medida?", "A los dos años", "La ficha lo dice en el Argumento C."),
        ("{F} ¿Qué beneficio espera la vecina? A) Respirar mejor B) Pagar menos por el transporte", "A) Respirar mejor", "Lo dice en el Argumento A."),
        ("{F} ¿Qué costo teme el comerciante? A) Perder clientes B) Tener más buses", "A) Perder clientes", "Lo dice en el Argumento B."),
        ("{F} ¿Qué condición pone el estudiante antes de cobrar? A) Mejorar el transporte público B) Cobrar desde el primer día", "A) Mejorar el transporte público", "Es la primera condición del Argumento C."),
        ("{F} ¿Qué deber del Estado se vincula con el Argumento C? A) Ofrecer alternativas, como mejor transporte público B) Cobrar desde ya para que la gente se adapte", "A) Ofrecer alternativas, como mejor transporte público", "La ficha dice que el Estado debe ofrecer alternativas."),
        ("{F} Una persona dice: «Ese comerciante solo piensa en su dinero». ¿Qué error comete? A) Ataca a la persona y no responde su argumento B) Aporta una evidencia", "A) Ataca a la persona y no responde su argumento", "Es una falacia de ataque a la persona."),
        ("{F} ¿Cuál es un buen contraargumento al Argumento B? A) Si el transporte público mejora, los clientes pueden llegar sin auto y se reduce la pérdida B) El comerciante exagera por egoísmo", "A) Si el transporte público mejora, los clientes pueden llegar sin auto y se reduce la pérdida", "Responde su razón con una condición, sin atacar a la persona."),
        ("{F} ¿Qué responsabilidad tiene una persona que usa el auto en el centro? A) Cuidar el aire como bien común, por ejemplo compartiendo viajes B) Ninguna", "A) Cuidar el aire como bien común, por ejemplo compartiendo viajes", "Los bienes comunes se cuidan entre todos."),
        ("{F} ¿Cuál es el mayor límite de la propuesta si no hay alternativas de transporte? A) Obliga a pagar a quien no tiene opción B) Reduce la contaminación", "A) Obliga a pagar a quien no tiene opción", "Por eso el Argumento C pide mejorar el transporte primero."),
        ("{F} ¿Qué dato de ejemplo ayudaría a revisar la medida? A) La calidad del aire y las ventas del centro antes y después B) La cantidad de autos de otra ciudad", "A) La calidad del aire y las ventas del centro antes y después", "Permite comparar beneficio y costo."),
        ("{F} ¿Qué postura final incluye razón, consecuencia y forma de revisarla? A) Apoyo la tarifa con mejor transporte antes; reduce la contaminación; se revisa a los dos años con datos del aire y del comercio B) Estoy en contra porque no me gusta", "A) Apoyo la tarifa con mejor transporte antes; reduce la contaminación; se revisa a los dos años con datos del aire y del comercio", "Contiene razón, consecuencia y revisión."),
    ],
    ctx=("En un liceo ficticio se propone cobrar por las fotocopias para financiar una biblioteca. Algunos temen que afecte a quienes tienen menos recursos. ¿Qué medida atiende ambos intereses? A) Cobrar con exención para quienes lo necesiten y revisar después B) Cobrar a todos sin excepción", "A) Cobrar con exención para quienes lo necesiten y revisar después", "Considera el beneficio y protege a quienes serían más perjudicados."),
    sc=[("¿Qué son los bienes comunes?", "Recursos que usamos entre todos, como el aire o el agua", "Así se definen en el vocabulario."),
        ("¿Qué significa que una medida sea revisable?", "Que puede evaluarse y corregirse con el tiempo", "Así se define en la clase."),
        ("¿Qué debe reconocer un debate respetuoso?", "Lo que otras posturas aportan", "La explicación lo indica.")],
    op=("Prepara un debate de dos minutos sobre la propuesta de Valleverde. Escribe tu postura, dos razones, un costo que reconoces, una responsabilidad para el Estado y otra para las personas, y cómo se revisaría la medida. Puedes apoyarla, rechazarla o apoyarla con condiciones. {F}",
        "Postura: apoyar con condiciones. Razones: mejora el aire; financia transporte público. Costo: posible pérdida de clientes. Estado: ofrecer alternativas y fiscalizar. Personas: compartir viajes. Revisión: a los dos años con datos del aire y las ventas.",
        ["postura clara", "reconoce un costo", "asigna responsabilidades al Estado y a las personas", "propone una revisión"], ["texto de postura", "lista de razones y revisión"], ["ignorar los costos", "culpar solo a una persona o grupo"],
        "Pide que diga qué argumento contrario le parece más fuerte y por qué."),
    reinforce="Explica a alguien de tu casa un costo y un beneficio de una medida para cuidar un bien común.",
    extend="Piensa en un bien común de tu barrio y anota una acción que puedan hacer vecinas y vecinos.",
)
