"""Cuaderno del estudiante, 1.º medio Orientación: OA 01 (alternativas de proyectos de vida) y OA 02 (sexualidad, vínculos afectivos, respeto y responsabilidad)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1, OA2 = "OR1M OA 01", "OR1M OA 02"


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
    "Una hoja y un lápiz. El perfil de Tomás, un estudiante inventado, está escrito en los ejercicios. No necesitas contar nada privado tuyo.",
    "Aprenderé a leer un caso de proyecto de vida y a separar intereses, capacidades y condiciones. Sirve para comparar alternativas con datos y no con suposiciones.",
    ["Sé describir mis intereses y capacidades de forma general (8.º básico).", "Sé que una opinión no es lo mismo que un hecho."],
    [
        "Un proyecto de vida es la idea de hacia dónde quieres avanzar en distintos ámbitos: el laboral o de estudios, el familiar, el comunitario y el personal. No es un destino único ni fijo: casi siempre hay varias alternativas posibles. Examinar un caso ayuda a practicar sin exponer tu vida privada.",
        "Para comparar alternativas se miran tres elementos. Los intereses son lo que te atrae (la mecánica, el dibujo, cuidar personas). Las capacidades son lo que puedes hacer o aprender a hacer (reparar, explicar, organizar). Las condiciones son las circunstancias: el dinero disponible, el tiempo, el lugar donde vives y los apoyos que tienes. Algunas condiciones se pueden modificar con un plan y otras no por ahora.",
        "Tus decisiones y experiencias también pesan. Probar un taller, hacer un voluntariado o conversar con alguien de un oficio te da información y abre alternativas. En cambio, descartar algo sin informarte las cierra. Por eso, al leer un caso, primero separa los hechos de las suposiciones.",
    ],
    [("proyecto de vida", "idea de hacia dónde avanzar en estudios, trabajo, familia y vida personal"), ("alternativa", "una de varias opciones posibles"), ("interés", "aquello que atrae o gusta a una persona"), ("capacidad", "lo que una persona puede hacer o aprender a hacer"), ("condición", "circunstancia como dinero, tiempo, lugar o apoyos")],
    [
        W("Clasificar un dato del caso", "Tomás vive en una localidad a 40 minutos en bus de la ciudad más cercana. ¿Es un interés, una capacidad o una condición?", ["El dato habla de dónde vive y de la distancia.", "No dice qué le gusta ni qué sabe hacer.", "Es una circunstancia."], "Una condición"),
        W("Separar hecho y suposición", "Del caso: «Trabajó un verano con su tío en un taller» y «Seguro no le gustará estudiar». ¿Cuál es hecho?", ["El trabajo en el taller ocurrió y se puede comprobar.", "«Seguro no le gustará» es una predicción sin pruebas."], "El trabajo del verano es el hecho"),
    ],
    [
        M("Creer que un proyecto de vida es una sola meta que no puede cambiar.", "Se confunde decidir hoy con quedar atado para siempre.", "Hay varias alternativas y se pueden ajustar con nueva información."),
        M("Tomar una suposición como si fuera un hecho.", "Una frase como «no podría» suena segura, pero nadie la comprobó.", "Pregunta qué dato la apoya antes de descartar una alternativa."),
    ],
    R=[
        ex("«Le gusta dibujar planos de casas». ¿Es un interés, una capacidad o una condición?", "Un interés", "Dice lo que le atrae."),
        ex("«Su familia puede ayudar con el pasaje del bus». ¿Es un interés, una capacidad o una condición?", "Una condición", "Es un apoyo, una circunstancia de su vida."),
        ex("«Sabe cambiar la cámara de una bicicleta». ¿Es un interés, una capacidad o una condición?", "Una capacidad", "Es algo que sabe hacer."),
    ],
    U=[
        ex("Tomás piensa: «Algún día quiero cuidar a mis sobrinos». ¿A qué ámbito de su proyecto de vida pertenece? A) Familiar B) Laboral", "A", "Habla de vínculos de familia y no de un trabajo."),
        ex("¿Cuál de estas frases es un hecho del caso? A) «Trabajó un verano en un taller.» B) «Nunca podrá estudiar en la ciudad.»", "A", "La primera ocurrió y se comprueba; la segunda es una predicción."),
        ex("¿Qué condición de Tomás se puede cambiar con un plan en unos meses? A) Que ahorre para el pasaje B) Que su localidad esté lejos de la ciudad.", "A", "Ahorrar depende de un plan; la distancia no cambia."),
    ],
    A=[
        ex("Clasifica con I (interés), C (capacidad) o D (condición): 1) Le encanta la fotografía. 2) Puede explicar un tema a su curso. 3) En su casa hay un computador compartido. Escribe las letras en orden.", "I, C, D", "La 1 es lo que le atrae, la 2 lo que puede hacer y la 3 una circunstancia."),
        ex("Ana se interesa por cuidar personas y tiene paciencia. ¿Qué alternativa de estudio coincide con su interés? A) Técnico en enfermería B) Técnico en contabilidad", "A", "Enfermería trabaja cuidando a personas."),
        ex("Un cuadro de Tomás anota: «Alternativa: curso de mecánica de bicicletas. Interés: sí. Capacidad: sí. Condición: no tiene transporte». ¿Cuántos de los tres elementos están a favor?", "2", "Interés y capacidad están a favor y la condición no, por ahora."),
    ],
    Z=[
        ex("Marta dice: «Si hoy no tengo dinero, mi proyecto de vida es imposible». ¿Por qué esa frase es incompleta?", "Porque el dinero es una condición que puede cambiar o tener otras vías", "Hay ahorro, becas y otras alternativas, y la condición no cancela intereses ni capacidades."),
        ex("Si Tomás nunca prueba un taller ni conversa con nadie del oficio, ¿qué pasa con sus alternativas? A) Conoce menos y puede descartar opciones sin información B) Sus alternativas se vuelven más seguras.", "A", "Sin experiencias ni datos no puede comparar bien."),
    ],
    D=[
        arith("Tomás ahorra $2.000 por semana durante 12 semanas para un curso que cuesta $30.000. ¿Cuántos pesos le faltan?", "30000-2000*12", "Primero se calcula lo ahorrado y luego se resta del precio.", " pesos"),
        ex("Un cuadro suma 1 punto por cada elemento a favor (interés, capacidad, condición). Alternativa P: 3 puntos. Alternativa Q: interés sí, capacidad sí, condición no. Alternativa R: interés sí, capacidad no, condición no. ¿Cuál alternativa tiene menos puntos?", "R", "R suma 1 punto, Q suma 2 y P suma 3."),
    ],
    context=[ex("En Orientación te dan este caso inventado: Valeria quiere ser diseñadora de ropa, cose bien, pero vive lejos de los cursos y su familia no puede pagar uno. ¿Cuál es la condición que habría que trabajar primero? A) La falta de acceso a un curso o a recursos B) Su interés por la ropa.", "A", "El interés ya existe; lo que limita hoy es el acceso.")],
    selfcheck=[ex("En Orientación: ¿un interés es lo que atrae a una persona?", "Sí", "Describe lo que le gusta o llama su atención."), ex("¿Una condición puede ser el dinero disponible?", "Sí", "Es una circunstancia que influye en las alternativas."), ex("¿Una suposición sin datos sirve para descartar una alternativa?", "No", "Hay que comprobar primero con hechos.")],
    task=T("Lee el perfil de Ámbar, una estudiante inventada: le gusta cantar en el coro; ayuda a su abuela con las compras; su curso la elige para presentar trabajos; en su barrio hay un centro cultural con talleres gratuitos los sábados; se pone nerviosa en las pruebas. Escribe cuatro líneas: un interés, una capacidad, una condición y una suposición que no deberías hacer sobre ella. Apoya cada una en un dato del perfil.", "Interés: cantar en el coro. Capacidad: presentar trabajos, su curso la elige. Condición: hay talleres gratuitos los sábados en su barrio. Suposición a evitar: «seguro no sirve para estudiar porque se pone nerviosa en pruebas».", ["escribe las cuatro líneas pedidas", "cada línea usa un dato del perfil", "separa hecho de suposición", "no cuenta nada privado propio"], ["cuadro escrito", "texto oral"], ["mezclar interés con capacidad", "presentar una suposición como hecho"], "Reconoce las líneas bien clasificadas y pregunta qué dato apoya la más débil."),
    reinforce="Escribe tres datos de un personaje de película y clasifícalos como interés, capacidad o condición.",
    extend="Explica por qué dos personas con el mismo interés pueden tener alternativas distintas.",
)

lesson(
    OA1, 2,
    "Una hoja y un lápiz. Las frases de Sebastián y de Carla, estudiantes inventados, están escritas en los ejercicios.",
    "Aprenderé a distinguir hechos, derechos y límites cuando pienso en mi proyecto de vida. Sirve para no aceptar frases injustas como «eso no es para ti» y para reconocer lo que sí puedo mover.",
    ["Sé separar interés, capacidad y condición.", "Sé que todas las personas tenemos los mismos derechos."],
    [
        "Un hecho se puede comprobar; una opinión o un estereotipo no. «Hay un curso de electricidad los sábados» es un hecho. «Las mujeres no sirven para electricidad» es un estereotipo: una idea fija sobre un grupo que ignora a cada persona. Decidir tu proyecto de vida con estereotipos limita alternativas sin razón.",
        "Todas las personas tienen derecho a la educación y a elegir sus estudios y su trabajo sin discriminación por género, origen, apariencia o situación económica. Un derecho es algo que te corresponde y que otros deben respetar. Si alguien te dice «eso no es para tu género», la frase no describe tus capacidades: describe un prejuicio.",
        "También existen límites. Un límite real es una condición que hoy no puedes cambiar, como los años mínimos que pide una carrera. Un límite aparente es uno que parece fijo pero se puede mover, como «no tengo plata», porque hay becas, ahorro o rutas técnicas. Distinguirlos te permite actuar donde sí puedes.",
    ],
    [("estereotipo", "idea fija y simplificada sobre un grupo de personas"), ("discriminación", "trato injusto a alguien por una característica como su género u origen"), ("derecho", "lo que corresponde a toda persona y los demás deben respetar"), ("límite real", "condición que hoy no se puede cambiar"), ("límite aparente", "obstáculo que parece fijo, pero se puede mover con un plan")],
    [
        W("Reconocer un estereotipo", "Carla oye: «Esa carrera es de hombres». ¿Es un hecho o un estereotipo?", ["La frase generaliza a todo un grupo.", "No dice nada sobre Carla en particular.", "No se puede comprobar."], "Un estereotipo"),
        W("Límite real o aparente", "Sebastián piensa: «No puedo estudiar porque no tengo dinero hoy». Hay ayudas de estudio y trabajo de verano. ¿Es un límite real o aparente?", ["Hoy no tiene dinero, pero eso puede cambiar.", "Existen vías que no se probaron."], "Un límite aparente"),
    ],
    [
        M("Creer que una frase dicha con seguridad es un hecho.", "Se confunde tono firme con prueba.", "Pregunta cómo se podría comprobar."),
        M("Aceptar «eso no es para tu género» como una razón.", "No distingue prejuicio de capacidad.", "Tienes derecho a elegir sin discriminación; pide información real."),
    ],
    R=[
        ex("«Hay un taller de robótica los viernes en la biblioteca». ¿Es un hecho o un estereotipo?", "Un hecho", "Se puede comprobar yendo o preguntando."),
        ex("«Los hombres no sirven para cuidar niños». ¿Es un hecho o un estereotipo?", "Un estereotipo", "Generaliza a todo un grupo sin mirar a cada persona."),
        ex("Dos compañeros comentan: «Cada persona puede elegir su carrera sin que la traten distinto por su género». ¿Qué expresa esa frase? A) Un derecho B) Un estereotipo", "A", "Afirma que todas las personas pueden elegir sin discriminación y no generaliza sobre un grupo."),
    ],
    U=[
        ex("Una profesora le dice a Carla: «Con tus notas puedes postular a ingeniería». ¿Qué valor tiene esa frase? A) Es una opinión apoyada en un dato, las notas B) Es un estereotipo.", "A", "Se apoya en un hecho de Carla y no en su género."),
        ex("«No tengo plata hoy, pero hay becas». ¿Qué tipo de límite es la falta de dinero hoy? A) Aparente B) Real", "A", "Hay vías para moverlo."),
        ex("«Para ser piloto de línea aérea hay una edad mínima legal». Para un estudiante de 15 años, ¿qué tipo de límite es hoy? A) Real B) Aparente", "A", "No lo puede cambiar con esfuerzo y debe esperar."),
    ],
    A=[
        ex("Clasifica con H (hecho) o E (estereotipo): 1) Hay una feria de oficios el 20 de noviembre. 2) Las mujeres son malas para la mecánica. 3) El curso dura 6 meses. Escribe las letras en orden.", "H, E, H", "La 1 y la 3 se pueden comprobar; la 2 generaliza a un grupo."),
        ex("Sebastián quiere estudiar enfermería y su amigo le dice: «Eso es de mujeres». ¿Qué derecho puede recordar Sebastián? A) Elegir su carrera sin discriminación B) Que todos sus amigos opinen igual.", "A", "La elección de estudios no se limita por género."),
        ex("Carla dice: «No puedo ser técnica en electricidad porque en mi liceo no hay esa especialidad». Hay liceos técnicos en otra comuna con locomoción. ¿Qué límite es la falta de la especialidad en su liceo? A) Aparente B) Real", "A", "Puede buscar otro liceo y transporte; no es un límite definitivo."),
    ],
    Z=[
        ex("¿Por qué un estereotipo puede reducir las alternativas de una persona aunque ella tenga capacidades?", "Porque hace que la descarten por su grupo y no por lo que puede hacer", "Se juzga al grupo y se ignoran las capacidades individuales."),
        ex("Dos amigas oyen que una carrera es «solo para hombres». ¿Qué paso es mejor? A) Buscar datos reales: requisitos, mallas y personas que la estudian B) Descartarla para evitar problemas.", "A", "La información real permite decidir sin prejuicio."),
    ],
    D=[
        arith("De 40 estudiantes de un curso, 12 creen que «ciertas carreras son solo de hombres». ¿Cuántos no lo creen? Es un dato de ejemplo.", "40-12", "Al total se le resta el grupo que sí lo cree."),
        arith("Un liceo técnico inventado tiene 5 especialidades. Cada especialidad tiene 2 cursos de 35 estudiantes. ¿Cuántos estudiantes hay en total?", "5*2*35", "Se multiplican especialidades, cursos y estudiantes por curso."),
    ],
    context=[ex("En el recreo escuchas: «Matías no puede ser peluquero, eso es de mujeres». ¿Qué respuesta respeta su derecho? A) «Cada persona puede elegir su oficio.» B) «Mejor que elija otra cosa.»", "A", "Afirma el derecho a elegir sin discriminar.")],
    selfcheck=[ex("En Orientación: ¿un estereotipo se puede comprobar?", "No", "Es una idea fija sobre un grupo, no un dato."), ex("¿Las personas tienen derecho a educación sin discriminación?", "Sí", "Es un derecho de todos."), ex("¿Un límite aparente puede moverse con un plan?", "Sí", "Parece fijo, pero tiene vías de solución.")],
    task=T("Lee estas cuatro frases inventadas: (a) «Hay becas para estudiar en institutos técnicos»; (b) «Esa carrera es para hombres»; (c) «No me alcanza el dinero este año»; (d) «Para matricularse en ese curso de operador de grúas hay que tener 18 años» (dato inventado). Clasifica cada una como hecho, estereotipo, límite aparente o límite real, y escribe una frase de por qué.", "(a) Hecho: se puede comprobar. (b) Estereotipo: generaliza a un grupo. (c) Límite aparente: puede moverse con becas o ahorro. (d) Límite real: es una edad que hoy no puede cambiar.", ["clasifica las cuatro frases", "explica con una razón cada una", "distingue límite real de aparente", "no usa datos personales"], ["tabla escrita", "texto oral"], ["llamar hecho a un estereotipo", "creer que un límite aparente es definitivo"], "Reconoce las frases bien clasificadas y pregunta cómo comprobaría la más dudosa."),
    reinforce="Anota un estereotipo sobre oficios que hayas oído en general y reescríbelo como una frase respetuosa.",
    extend="Explica la diferencia entre un límite real y uno aparente con un ejemplo inventado.",
)

lesson(
    OA1, 3,
    "Una hoja y un lápiz. Las tres alternativas de Fernanda, una estudiante inventada, están escritas en los ejercicios.",
    "Aprenderé a comparar alternativas de proyecto de vida con una tabla de criterios y a prever consecuencias a corto y largo plazo. Sirve para decidir con más información.",
    ["Sé separar hechos, derechos y límites.", "Conozco intereses, capacidades y condiciones."],
    [
        "Comparar alternativas es ponerlas lado a lado con los mismos criterios. Puedes usar una tabla con cuatro criterios: me interesa, puedo hacerlo (capacidad), es viable hoy (condiciones) y qué consecuencia tiene a futuro. Cada alternativa recibe un sí o un no en cada criterio, y se justifica con un dato.",
        "Las consecuencias son lo que pasa después de elegir. A corto plazo pueden ser el esfuerzo, el costo o el tiempo. A largo plazo pueden ser las oportunidades que se abren o se cierran. Una alternativa puede tener un costo hoy y abrir más puertas mañana; otra puede ser cómoda hoy pero cerrar caminos. Mirar ambos plazos evita decidir solo por lo inmediato.",
        "Comparar no significa que siempre haya una ganadora clara. A veces dos alternativas quedan parejas y se necesita más información. También conviene recordar que elegir una no borra las demás para siempre: una decisión puede revisarse si cambian los datos o tus intereses.",
    ],
    [("criterio", "regla o aspecto que se usa para comparar"), ("viable", "que se puede llevar a cabo con las condiciones actuales"), ("consecuencia", "lo que ocurre después de una decisión"), ("corto plazo", "lo que pasa pronto, en días o meses"), ("largo plazo", "lo que pasa después de años")],
    [
        W("Contar criterios", "Fernanda compara el curso de cocina: interés sí, capacidad sí, viable hoy no, abre varias oportunidades sí. ¿Cuántos criterios cumple?", ["Se cuentan los síes.", "Interés, capacidad y oportunidades son tres síes."], "Cumple 3 de 4"),
        W("Corto y largo plazo", "Estudiar inglés los sábados cuesta tiempo libre hoy y puede abrir un trabajo después. ¿Qué parte es corto plazo y cuál largo plazo?", ["Perder tiempo libre ocurre ahora.", "El trabajo posible llega más adelante."], "Corto plazo: tiempo libre; largo plazo: oportunidad laboral"),
    ],
    [
        M("Decidir solo por la alternativa más cómoda hoy.", "Se mira solo el corto plazo.", "Anota también lo que pasa a largo plazo."),
        M("Creer que si dos alternativas quedan parejas hay que elegir al azar.", "No se piensa en conseguir más datos.", "Pide información sobre el criterio que sigue dudoso."),
    ],
    R=[
        ex("Ordena de lo más inmediato a lo más lejano: (1) trabajar con el título obtenido, (2) inscribirse en el curso, (3) aprobar el primer año. Escribe los números en orden.", "2, 3, 1", "Primero se inscribe, luego aprueba el año y al final trabaja con el título."),
        ex("Perder tiempo libre por estudiar hoy, ¿es una consecuencia de corto o de largo plazo?", "De corto plazo", "Ocurre ahora, mientras estudia."),
        ex("Poder trabajar en un oficio dentro de tres años, ¿es una consecuencia de corto o de largo plazo?", "De largo plazo", "Ocurre varios años después."),
    ],
    U=[
        ex("Fernanda compara con una tabla de cuatro criterios. ¿Cuál no es un criterio de esa tabla? A) Qué alternativa eligió la mayoría de su curso B) Si es viable hoy.", "A", "Lo que eligen otros no mide el interés, la capacidad ni las condiciones de ella."),
        ex("Alternativa X: gusta, puede hacerla, no es viable hoy, abre oportunidades. ¿Qué criterio falla? A) La viabilidad hoy B) El interés.", "A", "Es el único que marca no."),
        ex("Fernanda elige el instituto, pero un año después descubre una beca para otra carrera que le interesa más. ¿Qué puede hacer? A) Revisar su decisión con los nuevos datos B) Seguir igual porque ya eligió", "A", "Una decisión puede revisarse si cambian los datos."),
    ],
    A=[
        ex("Fernanda da 1 punto por criterio cumplido. Repostería: interés sí, capacidad sí, viable hoy no, largo plazo sí. Diseño gráfico: interés sí, capacidad no, viable hoy sí, largo plazo no. ¿Cuántos puntos más tiene Repostería que Diseño gráfico?", "1", "Repostería suma 3 puntos y Diseño gráfico suma 2."),
        ex("Un curso de idiomas cuesta $15.000 al mes durante 4 meses y le da un certificado. ¿Qué parte del texto es la consecuencia de largo plazo? A) El certificado que puede servirle después B) El pago mensual.", "A", "El certificado se usa más adelante; el pago es inmediato."),
        ex("Fernanda duda entre dos opciones iguales en puntos. No sabe si puede viajar a la sede. ¿Qué debería hacer primero? A) Averiguar horarios y transporte B) Elegir una moneda.", "A", "Falta información sobre el criterio dudoso."),
    ],
    Z=[
        ex("¿Por qué comparar solo la consecuencia de corto plazo puede llevar a una mala decisión?", "Porque se ignora lo que se abre o se cierra más adelante", "Una opción incómoda hoy puede abrir caminos y una cómoda puede cerrarlos."),
        ex("Dos alternativas empatan en puntos. A es muy barata hoy y no abre opciones; B es cara hoy, pero abre varias. ¿Cuál tiene mejor consecuencia de largo plazo? A) A B) B", "B", "Abre más opciones en el futuro."),
    ],
    D=[
        arith("Fernanda dedica 3 horas cada sábado a un taller durante 10 sábados. ¿Cuántas horas dedica en total?", "3*10", "Se multiplican horas por sábado por el número de sábados."),
        arith("Un curso técnico dura 18 meses. Ella ya completó 7 meses. ¿Cuántos meses le faltan?", "18-7", "Al total se le restan los meses cumplidos."),
    ],
    context=[ex("En el Consejo de Curso, Ignacio compara estudiar en un instituto cercano o en otra ciudad. El instituto cercano le permite vivir en su casa; la otra ciudad ofrece más especialidades pero implica arriendo. ¿Cuál es un criterio de viabilidad? A) El costo de vivir fuera B) Que a un amigo le guste más.", "A", "El costo es una condición concreta para decidir.")],
    selfcheck=[ex("En Orientación: ¿comparar alternativas incluye mirar consecuencias de corto y largo plazo?", "Sí", "Ambas ayudan a decidir mejor."), ex("¿Un criterio es una regla para comparar?", "Sí", "Todas las alternativas se miden con él."), ex("¿Una decisión nunca puede revisarse?", "No", "Puede revisarse si cambian los datos.")],
    task=T("Fernanda tiene tres alternativas para después de 4.º medio: (1) un instituto técnico en su comuna, 2 años, costo bajo, le interesa cuidar mascotas; (2) trabajar en el negocio de su tío, ingreso inmediato, no le interesa mucho; (3) una universidad en otra ciudad, 5 años, mayor costo, le interesa la biología. Haz una tabla con los cuatro criterios (me interesa, puedo hacerlo, viable hoy, consecuencia a largo plazo) y escribe un sí o un no con un dato. Termina con una frase: qué dato necesitarías averiguar.", "Instituto: interés sí, viable hoy sí, largo plazo: título técnico en 2 años. Negocio: interés poco, viable sí, largo plazo: poca formación. Universidad: interés sí, viable hoy dudoso por costo, largo plazo: título profesional. Dato por averiguar: becas y costo de arriendo en esa ciudad.", ["completa los cuatro criterios para las tres alternativas", "apoya cada marca en un dato", "separa corto y largo plazo", "nombra un dato por averiguar"], ["tabla escrita", "texto oral"], ["usar solo el corto plazo", "marcar sin dato"], "Reconoce los criterios bien aplicados y pregunta qué dato falta en la celda dudosa."),
    reinforce="Compara dos actividades de tu fin de semana con tres criterios y escribe qué consecuencia tiene cada una.",
    extend="Explica por qué una alternativa puede tener un costo hoy y ser buena a largo plazo.",
)

lesson(
    OA1, 4,
    "Una hoja y un lápiz. El caso de Joaquín, un estudiante inventado, está escrito en los ejercicios.",
    "Aprenderé a elegir un paso concreto, pequeño y seguro para avanzar hacia una alternativa de proyecto de vida. Sirve para pasar de pensar a actuar sin arriesgarme de más.",
    ["Sé comparar alternativas con criterios.", "Conozco corto y largo plazo."],
    [
        "Una acción segura para avanzar en un proyecto de vida tiene cuatro rasgos. Es concreta: dice qué hacer. Es pequeña: se puede hacer en pocos días. Es reversible: si no resulta, puedes cambiar sin perder mucho. Y es acompañada: avisas o consultas a una persona adulta de confianza. Por ejemplo, asistir a una charla de un instituto es segura; abandonar el colegio sin plan no lo es.",
        "Elegir una acción coherente significa que tu paso conversa con lo que ya sabes de ti: tus intereses, capacidades y condiciones. Si te gusta la mecánica, ir a conocer un taller de un liceo técnico es coherente. Una meta progresiva divide un objetivo grande en pasos, uno por semana o por mes, y cada paso deja una evidencia que puedes mostrar, como una lista o un comprobante.",
        "Las decisiones y experiencias cuentan: cada paso que das te da información nueva. Si un paso te muestra que la alternativa no te gusta, no fracasaste; descubriste algo y puedes ajustar el plan. Lo importante es avanzar con cuidado y revisar.",
    ],
    [("acción segura", "paso concreto, pequeño, reversible y acompañado que no arriesga de más"), ("reversible", "que se puede cambiar o deshacer sin perder mucho"), ("meta progresiva", "objetivo grande dividido en pasos pequeños"), ("evidencia", "prueba de que se hizo algo, como una lista o un comprobante"), ("coherente", "que conversa con lo que uno sabe de sí mismo")],
    [
        W("Elegir la acción más segura", "Joaquín quiere ser técnico en electrónica. Opción A: visitar con un adulto de su familia el taller abierto del liceo técnico. Opción B: dejar el colegio para buscar trabajo. ¿Cuál es más segura?", ["A es concreta, pequeña y acompañada.", "B no es reversible y no tiene plan.", "A da información nueva."], "La opción A"),
        W("Dividir una meta", "La meta de Joaquín: aprender a armar circuitos simples con pila y luz LED en 3 meses. Escribe tres pasos.", ["Paso 1: ver un tutorial confiable y anotar las normas de seguridad.", "Paso 2: practicar en el taller con un adulto del liceo.", "Paso 3: guardar una foto o lista de lo que hizo como evidencia."], "Tres pasos con evidencia y un adulto"),
    ],
    [
        M("Creer que una meta grande se logra con un solo paso enorme.", "No se divide en partes alcanzables.", "Divide en pasos semanales con evidencia."),
        M("Hacer algo arriesgado sin avisar porque «es mi decisión».", "Se confunde autonomía con soledad.", "Avisa a una persona adulta de confianza; es parte de una acción segura."),
    ],
    R=[
        ex("Joaquín anota: «Algún día voy a hacer algo con la electrónica». ¿Qué le falta a ese paso para ser una acción segura? A) Ser concreto: decir qué hará y cuándo B) Ser más grande y arriesgado", "A", "Una acción segura dice qué se hace y para cuándo."),
        ex("Si un paso puede cambiarse sin perder mucho, ¿es reversible o irreversible?", "Reversible", "Se puede deshacer o ajustar."),
        ex("Joaquín quiere mostrar que visitó el taller. ¿Cuál es una evidencia? A) Una nota con la fecha y tres cosas que vio B) Decir que fue", "A", "Una nota con datos se puede mostrar; decirlo no deja prueba."),
    ],
    U=[
        ex("¿Cuál es una acción segura para explorar cocina? A) Asistir a una charla de cocina con una persona adulta B) Abandonar el colegio para empezar mañana.", "A", "Es pequeña, reversible y acompañada."),
        ex("Joaquín quiere ser técnico en electrónica. ¿Cuál formulación es una meta progresiva? A) Este mes visito el taller; el siguiente hago un taller de dos sábados; luego decido B) Mañana empiezo y en una semana ya soy técnico", "A", "Divide el objetivo en pasos pequeños y con plazos realistas."),
        ex("Tras un taller, Daniel nota que no le gusta la mecánica. ¿Cuál es la mejor lectura? A) Obtuvo información para ajustar su plan B) Fracasó y debe dejar todos sus planes", "A", "Descartar una alternativa con datos propios también es avanzar."),
    ],
    A=[
        ex("Joaquín quiere comprobar si le gusta la electrónica. ¿Qué paso es reversible? A) Hacer un taller de dos sábados B) Pagar un curso de un año sin probar antes.", "A", "Si no le gusta, puede parar sin perder mucho."),
        ex("Un paso se llama «ahorrar $5.000 al mes». ¿Qué evidencia sirve? A) Una libreta con los montos anotados B) Decirlo en voz alta.", "A", "La libreta es una prueba que se puede mostrar."),
        ex("Una amiga te cuenta que quiere probar un trabajo de fin de semana en un lugar desconocido sin avisar a nadie. ¿Qué debería agregar para que sea una acción segura? A) Contar a una persona adulta de confianza dónde y cuándo B) Nada, porque es su decisión.", "A", "Una acción segura es acompañada."),
    ],
    Z=[
        ex("¿Por qué una acción reversible es más segura al explorar una alternativa?", "Porque si no resulta puedes cambiar sin perder mucho", "Reduce el riesgo de quedar atrapado."),
        ex("Joaquín aprendió en un taller que no le gusta armar circuitos. ¿Cuál es la mejor lectura? A) Obtuvo información útil y puede ajustar su plan B) Perdió el tiempo.", "A", "Una experiencia sirve aunque descarte una alternativa."),
    ],
    D=[
        arith("La meta de Joaquín es juntar $60.000 en 6 meses. Si ahorra lo mismo cada mes, ¿cuánto debe ahorrar al mes?", "60000//6", "El total se divide en partes iguales por mes.", " pesos"),
        arith("Joaquín planea 4 pasos semanales de 2 horas cada uno durante 3 semanas. ¿Cuántas horas serán en total?", "4*2*3", "Se multiplican pasos por horas por semanas."),
    ],
    context=[ex("Camila quiere conocer el oficio de panadera. Una vecina panadera le ofrece mostrarle su taller un sábado de 10 a 12 horas, y su familia sabe dónde estará. ¿Cuál rasgo de acción segura aparece? A) Es acompañada y pequeña B) Es irreversible.", "A", "Se hace en dos horas y su familia lo sabe.")],
    selfcheck=[ex("En Orientación: ¿una acción segura es concreta y pequeña?", "Sí", "Se puede hacer pronto y tiene un paso claro."), ex("¿Avisar a una persona adulta de confianza es parte de una acción segura?", "Sí", "Aporta acompañamiento y cuidado."), ex("¿Una meta progresiva se divide en pasos?", "Sí", "Así se avanza de a poco y con evidencia.")],
    task=T("Lee el caso inventado de Daniela: quiere ser veterinaria, le preocupa no saber si le gustará de verdad, y cerca de su casa hay una clínica veterinaria que recibe visitas de estudiantes con una persona adulta. Escribe tres pasos para los próximos 30 días. Cada paso debe ser concreto, pequeño, reversible y acompañado, e incluir una evidencia.", "Paso 1 (semana 1): pedir a una persona adulta que llame a la clínica para coordinar una visita; evidencia: anotar la fecha. Paso 2 (semana 2): ir a la visita y anotar tres tareas que vea; evidencia: la lista. Paso 3 (semana 4): escribir qué le gustó y qué no; evidencia: media página.", ["escribe tres pasos", "cada paso es concreto, pequeño, reversible y acompañado", "incluye una evidencia por paso", "usa solo el caso, no datos propios"], ["plan escrito", "texto oral"], ["pasos demasiado grandes", "olvidar al adulto acompañante"], "Reconoce los pasos concretos y pregunta cuál sería reversible en el paso más grande."),
    reinforce="Divide en tres pasos la meta «aprender a andar en bicicleta por la ciclovía» de un personaje inventado.",
    extend="Explica por qué una acción puede ser pequeña y a la vez importante para un proyecto de vida.",
)

lesson(
    OA1, 5,
    "Una hoja y un lápiz. Los mensajes y las preguntas de ejemplo están escritos en los ejercicios; usa personas inventadas.",
    "Aprenderé a pedir orientación para mi proyecto de vida con un mensaje claro y a elegir a quién consultar. Sirve para obtener información real de personas que conocen un oficio o un estudio.",
    ["Sé elegir una acción segura.", "Sé que pedir ayuda es parte de una decisión responsable."],
    [
        "Pedir orientación es buscar información y apoyo en personas o lugares que saben del tema. Para un proyecto de vida puedes recurrir a tu profesor o profesora jefe, a la persona orientadora del colegio, a una persona de tu casa, a alguien que trabaja en el oficio que te interesa o a una charla de un instituto o universidad. Cada una aporta algo distinto: una orienta tus decisiones, otra cuenta cómo es el trabajo real.",
        "Un buen mensaje de pedido de ayuda tiene cuatro partes: quién eres, qué quieres saber, por qué lo preguntas y cuándo lo necesitas. Por ejemplo: «Hola, soy Camila de 1.º medio. Quiero saber cómo es el trabajo de técnico en enfermería, porque estoy comparando alternativas. ¿Podría conversar diez minutos esta semana?». Es breve, respetuoso y deja claro el pedido.",
        "Antes de conversar, prepara tres preguntas abiertas, que inviten a explicar y no solo a responder sí o no, como «¿qué es lo que más disfrutas de tu trabajo?». Después, agradece y anota lo aprendido. Si una información suena dudosa, contrástala con otra fuente confiable. Nunca compartas datos privados con desconocidos en internet: conversa presencialmente y con una persona adulta de confianza al tanto.",
    ],
    [("orientación", "ayuda para decidir con información"), ("pregunta abierta", "pregunta que invita a explicar y no se responde solo con sí o no"), ("fuente confiable", "persona o lugar que entrega información comprobable"), ("contrastar", "comparar una información con otra fuente"), ("persona orientadora", "profesional del colegio que ayuda con decisiones de estudio y vida")],
    [
        W("Armar el mensaje", "Hugo quiere preguntar a un técnico en electricidad cómo es su trabajo. Escribe el pedido con las cuatro partes.", ["Quién soy: «Soy Hugo, de 1.º medio».", "Qué quiero saber: «cómo es su trabajo».", "Por qué: «estoy comparando alternativas».", "Cuándo: «¿podría esta semana, diez minutos?»."], "Mensaje breve con quién, qué, por qué y cuándo"),
        W("Pregunta abierta", "¿Cuál es abierta: «¿Te gusta tu trabajo?» o «¿Qué es lo que más disfrutas de tu trabajo?»", ["La primera se responde con sí o no.", "La segunda invita a explicar."], "«¿Qué es lo que más disfrutas de tu trabajo?»"),
    ],
    [
        M("Escribir un mensaje sin decir quién eres ni para qué lo pides.", "Se supone que la persona entenderá.", "Incluye las cuatro partes: quién, qué, por qué y cuándo."),
        M("Creer toda la información de la primera persona consultada.", "Se confunde una opinión con un dato.", "Contrasta con otra fuente confiable."),
    ],
    R=[
        ex("Clasifica con A (abierta) o C (cerrada, de sí o no): 1) «¿Tuviste que estudiar mucho?» 2) «¿Cómo aprendiste tu oficio?» Escribe las letras en orden.", "C, A", "La 1 se responde con sí o no; la 2 invita a explicar."),
        ex("En un pedido de ayuda escribes: «Soy Hugo, de 1.º medio». ¿Qué parte de las cuatro es esa? A) Quién soy B) Cuándo lo necesito", "A", "Presenta a quien escribe."),
        ex("Quieres saber qué estudios técnicos existen después de 4.º medio. ¿A quién consultas primero en el colegio? A) A la persona orientadora B) A un desconocido que te escribe por chat", "A", "La persona orientadora es una fuente confiable y conocida."),
    ],
    U=[
        ex("¿Cuál es una pregunta abierta? A) «¿Cómo es un día normal en tu trabajo?» B) «¿Trabajas en una oficina?»", "A", "La primera pide una explicación; la segunda se responde con sí o no."),
        ex("En el mensaje «Hola, soy Ema de 1.º medio. Quiero saber cómo es estudiar kinesiología, porque estoy comparando carreras. ¿Podría conversar esta semana?», ¿qué parte falta de las cuatro? A) Ninguna, están las cuatro B) Falta el cuándo.", "A", "Dice quién es, qué quiere, por qué y cuándo."),
        ex("¿Qué haces si una información suena dudosa? A) Contrastarla con otra fuente confiable B) Repetirla a tu curso como cierta.", "A", "Comparar fuentes evita errores."),
    ],
    A=[
        ex("Marca la mejor manera de pedir ayuda: 1) «Dime todo sobre medicina»; 2) «Hola, soy Iván de 1.º medio. Estoy comparando estudios y quiero saber cómo es tu trabajo. ¿Podemos hablar diez minutos el miércoles?»; 3) «Necesito datos, rápido». ¿Cuál es?", "La 2", "Tiene las cuatro partes y es respetuosa."),
        ex("Quieres conversar con una persona de un oficio. ¿Dónde es más seguro? A) En la sala del colegio con la persona orientadora presente B) En la casa de alguien que no conoces.", "A", "Es un lugar conocido y con un adulto del colegio."),
        ex("Gabriela escribió: «¿Qué estudiaste?», «¿Cuánto dura la carrera?» y «¿Qué es lo más difícil de tu trabajo?». ¿Cuál es la pregunta abierta que invita a explicar más? A) «¿Qué es lo más difícil de tu trabajo?» B) «¿Cuánto dura la carrera?»", "A", "Pide explicar; la otra se responde con un dato corto."),
    ],
    Z=[
        ex("¿Por qué conviene preparar tres preguntas antes de conversar con una persona del oficio?", "Para aprovechar el tiempo y obtener información clara", "Una conversación breve rinde más con preguntas pensadas."),
        ex("Un chat desconocido te ofrece «orientación gratis» y pide tu dirección. ¿Qué haces? A) No das datos y cuentas a una persona adulta de confianza B) Das la dirección para que te ayude.", "A", "No se comparten datos privados con desconocidos."),
    ],
    D=[
        arith("Un instituto inventado tiene 6 charlas, de 45 minutos cada una, el mismo día. ¿Cuántos minutos duran en total?", "6*45", "Se multiplican charlas por minutos de cada una.", " minutos"),
        arith("Lucas pidió información a 9 personas. 5 respondieron por escrito y 2 por teléfono. ¿Cuántas no respondieron?", "9-5-2", "Al total se le restan las que respondieron por escrito y por teléfono."),
    ],
    context=[ex("El colegio invita a una ingeniera a conversar. Mateo quiere preguntar algo útil para comparar sus alternativas. ¿Cuál elegirías? A) «¿Qué estudios necesitaste y qué te costó más?» B) «¿Eres famosa?»", "A", "La primera aporta información para decidir.")],
    selfcheck=[ex("En Orientación: ¿un mensaje de pedido de ayuda debe decir qué quieres saber?", "Sí", "Es una de sus cuatro partes."), ex("¿Es seguro dar tu dirección a un desconocido que ofrece orientación en línea?", "No", "Los datos privados no se comparten."), ex("¿Una pregunta abierta pide explicar?", "Sí", "No se responde solo con sí o no.")],
    task=T("Quieres conocer el trabajo de una técnica en párvulos (inventada), llamada Rosa, que trabaja en un jardín infantil de tu comuna, y vas a escribirle por intermedio de una persona adulta de tu casa. Escribe el mensaje con las cuatro partes (quién, qué, por qué, cuándo) y tres preguntas abiertas para la conversación.", "Hola, Rosa, soy Pedro de 1.º medio. Quiero saber cómo es ser técnica en párvulos, porque estoy comparando alternativas. ¿Podríamos conversar diez minutos el viernes? Preguntas: ¿qué es lo que más disfrutas? ¿qué estudios necesitaste? ¿cómo es un día normal?", ["incluye las cuatro partes del mensaje", "escribe tres preguntas abiertas", "es respetuoso y breve", "no incluye datos privados"], ["mensaje escrito", "texto oral"], ["preguntas de sí o no", "mensaje sin pedido claro"], "Reconoce las partes presentes y pregunta cuál pregunta abierta aportaría más información."),
    reinforce="Reescribe como pregunta abierta: «¿Te gusta tu trabajo?».",
    extend="Explica por qué contrastar dos fuentes ayuda a decidir mejor.",
)

# ================================================================ OA 02
lesson(
    OA2, 1,
    "Una hoja y un lápiz. El caso de Lucía y Diego, personas inventadas, está escrito en los ejercicios. Todo se analiza en tercera persona.",
    "Aprenderé a examinar un caso de vínculo afectivo y a reconocer señales de respeto y de falta de respeto. Sirve para cuidarme a mí y a otras personas en las relaciones.",
    ["Sé que tengo derecho a decir «no» (8.º básico).", "Sé que la intimidad y los cuerpos se respetan."],
    [
        "La sexualidad es una dimensión de las personas que incluye el cuerpo, los afectos, las relaciones y los valores. Los vínculos afectivos son las relaciones con cariño: la amistad, la familia y el pololeo. En una relación sana hay respeto, que es tratar al otro como una persona con dignidad, con sus decisiones y su intimidad.",
        "Al examinar un caso, separa tres cosas: lo que pasó (hechos), lo que cada persona podría sentir (emociones) y lo que corresponde cuidar (derechos y valores). Señales de una relación respetuosa: se conversa, se aceptan los «no», se cuida la privacidad y no hay miedo. Señales de alerta: insultos, control del celular, aislamiento de amistades, presión o amenazas.",
        "La responsabilidad significa hacerse cargo de las propias decisiones y de cómo afectan a otros. Cuidar de uno mismo y de los demás incluye la salud, la intimidad y la integridad física y emocional. Si algo en un vínculo genera miedo o incomodidad, es importante conversarlo con una persona adulta de confianza.",
    ],
    [("sexualidad", "dimensión humana que incluye cuerpo, afectos, relaciones y valores"), ("vínculo afectivo", "relación con cariño, como amistad, familia o pololeo"), ("respeto", "tratar a otra persona con dignidad y aceptar sus decisiones"), ("integridad", "derecho a no ser dañado en el cuerpo ni en las emociones"), ("señal de alerta", "conducta que puede indicar una relación dañina")],
    [
        W("Reconocer una señal de alerta", "Diego le exige a Lucía su clave del celular y se enoja si ella sale con amigas. ¿Qué señales aparecen?", ["Exigir la clave controla su privacidad.", "Enojarse por sus salidas la aísla de sus amistades."], "Control y aislamiento: señales de alerta"),
        W("Separar hechos y emociones", "Caso: Lucía no contestó un mensaje en dos horas y Diego le escribió 15 veces. Lucía se siente agobiada. ¿Cuál es el hecho y cuál la emoción?", ["Los 15 mensajes se pueden contar: es un hecho.", "El agobio es lo que ella siente: emoción."], "Hecho: 15 mensajes; emoción: agobio"),
    ],
    [
        M("Pensar que los celos intensos demuestran amor.", "Se confunde control con cariño.", "El amor respeta la privacidad y las decisiones del otro."),
        M("Culpar a la persona que sufre una situación de falta de respeto.", "No se mira la conducta de quien la causa.", "La responsabilidad es de quien presiona o controla; apoya y busca ayuda adulta."),
    ],
    R=[
        ex("Ana le dice a su pololo: «hoy prefiero estudiar», y él responde: «ok, nos vemos mañana». ¿Qué aparece en esa conducta? A) Respeto, porque acepta su decisión B) Control, porque la deja sola", "A", "Acepta lo que ella decide, sin presión."),
        ex("Exigir la clave del celular de tu pareja, ¿es una señal de respeto o de alerta?", "De alerta", "Controla su privacidad."),
        ex("Clasifica con R (respeto) o A (alerta): 1) Preguntarle a su pareja qué prefiere hacer el sábado. 2) Exigirle que avise a quién ve cada día. Escribe las letras en orden.", "R, A", "La 1 consulta su decisión; la 2 la controla."),
    ],
    U=[
        ex("¿Cuál es una señal de relación respetuosa? A) Se aceptan los «no» de cada uno B) Se revisan los chats del otro.", "A", "Aceptar los «no» respeta las decisiones."),
        ex("Si alguien dice «no puedes ver a tus amigas», ¿qué conducta es? A) Aislamiento B) Cuidado.", "A", "Le quita apoyo y libertad."),
        ex("Una persona siente miedo de su pareja cuando discuten. ¿Qué conviene? A) Conversarlo con una persona adulta de confianza B) Callarlo para no empeorar la relación", "A", "El miedo es una señal de que puede haber daño y un adulto puede ayudar."),
    ],
    A=[
        ex("Clasifica con R (respeto) o A (alerta): 1) Pedirle permiso antes de publicar una foto. 2) Amenazar con terminar si no responde de inmediato. 3) Aceptar que hoy no quiere salir. Escribe las letras en orden.", "R, A, R", "La 1 y la 3 respetan decisiones; la 2 presiona con una amenaza."),
        ex("En un caso, Valentina pide a Joaquín que no comparta una conversación privada, y él la reenvía a su grupo. ¿Qué derecho vulneró? A) Su intimidad B) Su derecho a salir.", "A", "Difundió algo privado sin su permiso."),
        ex("Ana ríe cuando Pedro le revisa el celular «por broma». Ana dice que le incomoda, y él continúa. ¿Qué debería cambiar? A) Que Pedro respete su límite B) Que Ana ría más.", "A", "El límite expresado debe respetarse."),
    ],
    Z=[
        ex("¿Por qué «es solo una broma» no justifica una conducta que incomoda a alguien?", "Porque el efecto en la otra persona importa más que la intención", "Si la otra persona se incomoda, la conducta no respeta su dignidad."),
        ex("Un amigo cuenta que su pareja le prohíbe ver a su familia. Para cuidar su integridad emocional, ¿qué le sugieres? A) Contarlo a una persona adulta de confianza B) Guardar el secreto para no causar problemas.", "A", "Pedir ayuda adulta protege; el secreto mantiene el daño."),
    ],
    D=[
        arith("En una lista de ejemplo hay 20 conductas de pololeo. 8 son señales de respeto y 5 son de alerta. El resto no sirve para decidir. ¿Cuántas quedan sin clasificar?", "20-8-5", "Al total se le restan las ya clasificadas."),
        arith("Bruno manda 18 mensajes a Antonia en 3 horas, repartidos en partes iguales. ¿Cuántos mensajes manda por hora?", "18//3", "Se divide el total de mensajes entre las horas."),
    ],
    context=[ex("En el curso se comenta que una pareja de 1.º medio se pelea a gritos y uno de los dos quedó llorando. ¿Qué es lo más responsable que puede hacer un compañero? A) Avisar a una persona adulta del colegio B) Comentarla en redes con una foto.", "A", "Pedir ayuda adulta protege a ambos y no los expone.")],
    selfcheck=[ex("En Orientación: ¿respetar es aceptar las decisiones del otro?", "Sí", "Reconoce su dignidad."), ex("¿Controlar el celular de la pareja es una señal de alerta?", "Sí", "Invade su intimidad."), ex("¿Una persona que sufre falta de respeto es culpable de lo que le pasa?", "No", "La responsabilidad es de quien presiona.")],
    task=T("Lee este caso inventado: Antonia y Bruno son pareja desde hace tres meses. Bruno le pide a Antonia que elimine a sus amigos de la red social, le revisa el celular y se enoja si no le contesta enseguida. Antonia dice que a veces tiene miedo de decirle que no. Escribe: dos señales de alerta, un derecho de Antonia y una persona adulta de confianza a quien podría pedir ayuda.", "Señales: le pide eliminar a sus amigos y le revisa el celular. Derecho: intimidad o decidir sobre sus amistades. Persona adulta: la orientadora o una persona de su casa.", ["nombra dos señales de alerta del caso", "nombra un derecho", "nombra a quién pedir ayuda", "no moraliza ni culpa a Antonia"], ["texto escrito", "tabla de hechos y derechos"], ["culpar a Antonia", "no nombrar a una persona adulta"], "Reconoce las señales bien identificadas y pregunta cuál derecho se ve más afectado."),
    reinforce="Escribe dos señales de respeto en una amistad, con personajes inventados.",
    extend="Explica con tus palabras la diferencia entre cariño y control.",
)

lesson(
    OA2, 2,
    "Una hoja y un lápiz. Las tarjetas de derechos y los casos de Marcos y Elisa, personas inventadas, están escritas en los ejercicios.",
    "Aprenderé qué es el consentimiento y cuáles son sus condiciones. Sirve para saber que toda actividad íntima necesita un «sí» libre y que un «no» se respeta siempre.",
    ["Sé reconocer señales de respeto y de alerta.", "Sé que la intimidad y la integridad se protegen."],
    [
        "El consentimiento es un «sí» que una persona da de manera libre, informada y con ganas, para una acción concreta. Libre significa sin presión, amenaza ni chantaje. Informada significa que sabe lo que acepta. Y es específico: aceptar una cosa no es aceptar otra. El consentimiento se puede retirar en cualquier momento: decir «sí» antes no obliga a seguir.",
        "No hay consentimiento si la persona dice «no», se queda en silencio por miedo, está dormida o bajo los efectos del alcohol u otras sustancias, o si quien pide tiene poder sobre ella, por ejemplo por edad o por ser una autoridad. El silencio y la falta de resistencia tampoco significan «sí». Las insistencias repetidas son presión, no consentimiento.",
        "Un «no» es una respuesta completa: nadie debe pedir explicaciones. Tienes derecho a decidir sobre tu cuerpo y tu intimidad. Y tienes la responsabilidad de respetar el «no» de los demás. Si una persona adulta presiona, engaña o se aprovecha de una persona menor de edad para tener contacto íntimo, es una conducta grave que la ley sanciona, y la persona menor nunca es culpable: debe avisar de inmediato a una persona adulta de confianza.",
    ],
    [("consentimiento", "«sí» libre, informado y específico que se puede retirar"), ("chantaje", "presión que amenaza con algo malo para obtener lo que se quiere"), ("límite", "lo que una persona acepta o no acepta que le hagan"), ("intimidad", "ámbito personal y reservado de una persona"), ("presión", "insistencia o amenaza para que alguien ceda")],
    [
        W("Revisar si hay consentimiento", "Marcos le pide a Elisa que le mande una foto íntima y le dice: «si no lo haces, terminamos». Elisa dice que no. ¿Hay consentimiento?", ["Elisa dijo «no».", "Marcos usa un chantaje.", "Sin sí libre, no hay consentimiento."], "No hay consentimiento"),
        W("Consentimiento que se retira", "Elisa aceptó ir al cine con Marcos, pero cambia de opinión una hora antes. ¿Debe ir igual?", ["Aceptó antes, pero puede cambiar de opinión.", "El consentimiento se puede retirar."], "No debe ir; puede retirar su consentimiento"),
    ],
    [
        M("Creer que el silencio significa «sí».", "Se interpreta la falta de palabras como aceptación.", "Solo cuenta un «sí» claro y libre."),
        M("Pensar que si dijo «sí» una vez, vale para siempre.", "Se confunde un permiso con una obligación.", "El consentimiento es específico y se puede retirar."),
    ],
    R=[
        ex("Dos «sí»: 1) dicho tras cinco insistencias y una amenaza de terminar la relación; 2) dicho sin presión, sabiendo qué se acepta. ¿Cuál es consentimiento? A) El 1 B) El 2", "B", "El 2 es libre e informado; el 1 nace de una presión."),
        ex("Pablo dice «no quiero» y Tere le pregunta cinco veces por qué. ¿Qué debería hacer Tere? A) Aceptar el no sin exigir explicaciones B) Seguir preguntando hasta convencerlo", "A", "Un «no» es una respuesta completa."),
        ex("Julia no responde porque le da miedo la reacción de su compañero. ¿El silencio significa «sí»? A) No, el silencio por miedo no es consentimiento B) Sí, porque no dijo «no»", "A", "No es una aceptación libre."),
    ],
    U=[
        ex("Si alguien acepta algo porque lo amenazan, ¿el consentimiento es libre? A) No B) Sí.", "A", "Hay presión y miedo."),
        ex("¿Se puede retirar el consentimiento en cualquier momento? A) Sí B) No.", "A", "Cambiar de opinión es un derecho."),
        ex("¿Qué falta si una persona no sabe qué está aceptando? A) Que sea informado B) Que sea libre.", "A", "Una de las condiciones es saber lo que se acepta."),
    ],
    A=[
        ex("Cuatro situaciones: 1) dice «sí» sin presión y sabe qué acepta; 2) dice «sí» por miedo a un grito; 3) está dormida; 4) dice «no». ¿En cuántas hay consentimiento?", "1", "Solo en la 1 el sí es libre e informado."),
        ex("Un amigo mayor de edad insiste a Bruno, de 14, en que guarde un secreto de contacto íntimo. ¿Qué es lo mejor que puede hacer Bruno? A) Avisar de inmediato a una persona adulta de confianza B) Guardar el secreto para evitar problemas.", "A", "Un adulto que presiona a un menor para mantener un secreto íntimo actúa gravemente mal, y el menor no es culpable."),
        ex("En una fiesta inventada, Tania dice «no» y su compañero insiste cinco veces. ¿Cómo se llama esa conducta? A) Presión B) Consentimiento.", "A", "La insistencia después de un «no» es presión."),
    ],
    Z=[
        ex("¿Por qué una persona bajo los efectos del alcohol no puede dar un consentimiento válido?", "Porque no puede decidir con libertad ni con claridad", "El alcohol altera el juicio, así que su «sí» no es libre ni informado."),
        ex("Elisa dijo «sí» a un abrazo, pero no a otra cosa. ¿Qué característica del consentimiento se aplica? A) Que es específico B) Que dura para siempre.", "A", "Aceptar una acción no autoriza otra."),
    ],
    D=[
        arith("En una encuesta inventada de 50 estudiantes, 35 conocen las condiciones del consentimiento. ¿Cuántos no las conocen?", "50-35", "Al total se le resta el grupo que sí las conoce."),
        arith("Una lista tiene 4 condiciones del consentimiento. Un curso de 36 estudiantes forma equipos de 4 para explicar una condición cada equipo. ¿Cuántos equipos hay?", "36//4", "Se divide el total de estudiantes entre los integrantes de cada equipo."),
    ],
    context=[ex("En una red social inventada, alguien manda a Camila: «Si me quieres, mándame una foto sin ropa». ¿Qué respuesta protege su intimidad? A) «No, no lo haré», y contárselo a una persona adulta de confianza B) «Bueno, pero no se la muestres a nadie.»", "A", "Un «no» firme y avisar a un adulto protegen; enviarla pone su intimidad en riesgo.")],
    selfcheck=[ex("En Orientación: ¿el consentimiento debe ser libre?", "Sí", "Sin presión ni amenaza."), ex("¿Puedes retirar tu consentimiento después de haberlo dado?", "Sí", "Tienes derecho a cambiar de opinión."), ex("¿Es culpable una persona menor cuando un adulto la presiona?", "No", "La responsabilidad es del adulto.")],
    task=T("Lee tres casos inventados: (a) Rocío acepta tomarse de la mano con Esteban; (b) Nicolás insiste siete veces a Paz para que le mande una foto íntima; (c) Sofía acepta ir a una fiesta y luego decide no ir. Indica en cuáles hay consentimiento, cuáles son presión y qué podría hacer cada persona. Usa las palabras libre, específico y retirar.", "(a) Hay consentimiento específico para tomarse de la mano. (b) Es presión: Paz puede decir «no» y avisar a una persona adulta. (c) Puede retirar su consentimiento sin dar explicaciones largas.", ["analiza los tres casos", "usa las tres palabras pedidas", "propone una acción segura", "no moraliza ni culpa a quien dice no"], ["texto escrito", "tarjetas de consentimiento"], ["confundir silencio con sí", "olvidar que se puede retirar"], "Reconoce el caso bien analizado y pregunta qué palabra faltó en el menos claro."),
    reinforce="Escribe una frase de «no» respetuosa y firme, con un personaje inventado.",
    extend="Explica por qué el silencio no es consentimiento.",
)

lesson(
    OA2, 3,
    "Una hoja y un lápiz. El semáforo y el caso de Valentina y Joaquín, personas inventadas, están escritos en los ejercicios.",
    "Aprenderé a comparar opciones y sus consecuencias ante una presión en un vínculo afectivo, incluso en decisiones sobre salud sexual. Sirve para decidir con información y cuidado.",
    ["Sé qué es el consentimiento y cuáles son sus condiciones.", "Sé decir «no» de forma clara."],
    [
        "Ante una presión puedes responder de varias maneras. Ceder significa aceptar aunque no quieras. Evitar es irte sin decir nada. Confrontar con agresión es insultar. Responder con asertividad es decir lo que decides con claridad y respeto. Pedir ayuda es consultar a una persona adulta de confianza. Cada una trae consecuencias distintas para tu bienestar, tu relación y tu salud.",
        "Las decisiones sobre sexualidad tienen consecuencias emocionales y de salud. Cuando se tiene actividad sexual pueden ocurrir embarazos no planificados o infecciones de transmisión sexual; usar métodos de protección como el preservativo reduce estos riesgos, y las dudas se aclaran con profesionales de un centro de salud. Decidir esperar es siempre una opción válida y respetable.",
        "Para comparar, usa un semáforo: verde si la opción cuida tu salud y tu dignidad; amarillo si tiene riesgos que podrías reducir con ayuda; rojo si te daña o daña a otros. Una decisión responsable considera cómo te sentirás después, no solo ahora, y se toma sin presión.",
    ],
    [("asertivo", "que dice lo que decide con claridad y respeto"), ("consecuencia", "lo que ocurre después de una decisión"), ("infección de transmisión sexual", "enfermedad que se contagia por contacto sexual"), ("preservativo", "método de protección que reduce el riesgo de infecciones y embarazo"), ("semáforo de riesgo", "forma de clasificar opciones en verde, amarillo y rojo")],
    [
        W("Clasificar con semáforo", "Joaquín presiona a Valentina para tener relaciones sexuales «porque todos lo hacen». Opción 1: ceder. Opción 2: decir «no estoy lista» y proponer conversar. ¿Cómo se clasifican?", ["Ceder bajo presión pone en riesgo su salud y su decisión: rojo.", "Decir «no» con claridad protege: verde."], "Ceder: rojo; decir «no estoy lista»: verde"),
        W("Prever consecuencias", "¿Qué consecuencia puede tener ceder bajo presión?", ["Puede haber arrepentimiento.", "Puede haber riesgos de salud como infecciones o un embarazo no planificado."], "Arrepentimiento y riesgos de salud"),
    ],
    [
        M("Pensar que usar un método de protección elimina toda decisión personal.", "Se olvida que sin consentimiento no hay nada que proteger.", "Primero el consentimiento libre; luego, el cuidado de la salud."),
        M("Creer que decir que no daña la relación para siempre.", "Se teme perder el vínculo.", "Una pareja que respeta mantiene el vínculo; si no, el problema es la presión."),
    ],
    R=[
        ex("Con el semáforo, clasifica: «hablar con un profesional de un centro de salud sobre cómo cuidarse». ¿Verde, amarillo o rojo?", "Verde", "Cuida la salud y la dignidad."),
        ex("Decir «no» con claridad y respeto, ¿es una respuesta asertiva o pasiva?", "Asertiva", "Expresa la decisión sin agresión."),
        ex("Un compañero dice: «yo prefiero esperar». ¿Cómo se considera esa decisión? A) Una opción válida y respetable B) Una señal de que algo anda mal en él", "A", "Decidir esperar es una decisión respetable."),
    ],
    U=[
        ex("¿Qué opción cuida más la salud de Valentina? A) Decir «no estoy lista» y conversar B) Aceptar para evitar una pelea.", "A", "Protege su decisión y su salud."),
        ex("¿Qué dos riesgos de salud pueden aparecer con relaciones sexuales sin protección? A) Embarazo no planificado e infecciones de transmisión sexual B) Ninguno, si la pareja es de confianza.", "A", "Ambos son riesgos reales aunque haya confianza; un método de protección los reduce."),
        ex("¿A quién se pueden consultar dudas sobre protección? A) Profesionales de un centro de salud B) Lo que cuentan amigos que dicen saber del tema.", "A", "Entregan información confiable."),
    ],
    A=[
        ex("Hay cuatro respuestas a una presión: 1) ceder; 2) irse sin decir nada; 3) decir «no, gracias» y proponer otra actividad; 4) insultar. ¿Cuál es la asertiva?", "La 3", "Es clara y respetuosa."),
        ex("Una pareja inventada dice: «si me quieres, lo haces». Con el semáforo, ¿cómo se clasifica ceder a esa frase? A) Rojo B) Verde", "A", "Cede ante un chantaje y puede dañarla."),
        ex("Carolina dice: «No quiero hoy y quiero ver con un profesional de salud cómo cuidarme antes de decidir». ¿Qué parte de su respuesta cuida su salud? A) Consultar a un profesional B) Esperar el fin de semana.", "A", "Consultar a un profesional entrega información confiable."),
    ],
    Z=[
        ex("¿Por qué ceder bajo presión puede traer arrepentimiento?", "Porque se decide por miedo y no por ganas propias", "Una decisión que no es libre suele generar malestar después."),
        ex("¿Qué opción es más responsable ante una duda sobre salud sexual? A) Consultar a una persona adulta de confianza o a un centro de salud B) Probar y ver qué pasa.", "A", "Consultar primero permite decidir informado."),
    ],
    D=[
        arith("En una encuesta inventada de 80 jóvenes, 55 dicen que consultarían a un profesional de salud ante una duda. ¿Cuántos no lo harían?", "80-55", "Al total se le resta el grupo que sí consultaría."),
        arith("Un centro de salud inventado atiende 6 consultas de adolescentes por día, de lunes a viernes. ¿Cuántas consultas atiende en una semana?", "6*5", "Se multiplican consultas por días."),
    ],
    context=[ex("En una fiesta inventada, un compañero ofrece a Fabiola «ir a un lugar más tranquilo» y ella siente que no es lo que desea. ¿Cuál es la respuesta más segura? A) Decir «no, gracias» y quedarse con sus amigas B) Ir para no parecer pesada.", "A", "Protege su decisión y no se aísla.")],
    selfcheck=[ex("En Orientación: ¿decidir esperar es una opción válida?", "Sí", "Cada persona decide sin presión."), ex("¿Ceder a un chantaje es una decisión libre?", "No", "Hay presión que quita la libertad."), ex("¿Un profesional de salud puede aclarar dudas sobre protección?", "Sí", "Entrega información confiable.")],
    task=T("Lee el caso inventado: Gonzalo presiona a Daniela para tener relaciones sexuales y le dice que si no, buscará a otra. Escribe tres opciones para Daniela (ceder, responder con asertividad, pedir ayuda), clasifica cada una con el semáforo (verde, amarillo o rojo) y escribe una consecuencia de cada una.", "Ceder: rojo, riesgo de arrepentimiento y de salud. Asertividad («no, no quiero»): verde, protege su decisión. Pedir ayuda a la orientadora: verde, recibe apoyo.", ["escribe tres opciones", "clasifica con el semáforo", "anota una consecuencia por opción", "no culpa a Daniela"], ["tabla escrita", "texto oral"], ["clasificar sin consecuencias", "culpar a la víctima"], "Reconoce las opciones bien clasificadas y pregunta qué consecuencia es la más importante."),
    reinforce="Clasifica con el semáforo dos respuestas a la presión de un grupo para ir a una fiesta sin permiso.",
    extend="Explica por qué «todos lo hacen» no es una razón para decidir.",
)

lesson(
    OA2, 4,
    "Una hoja y un lápiz. Los casos de Isidora, Mateo y Paula, personas inventadas, están escritos en los ejercicios.",
    "Aprenderé a elegir una acción segura en situaciones de presión, secreto o contacto íntimo no deseado. Sirve para saber qué hacer y a quién avisar.",
    ["Sé comparar opciones con el semáforo.", "Sé que el consentimiento debe ser libre."],
    [
        "Una acción segura cuida tu integridad y te acerca a la ayuda. Ante una situación de presión o contacto íntimo no deseado, los pasos son: decir «no» con claridad si puedes, alejarte a un lugar con personas, no guardar el secreto y avisar a una persona adulta de confianza, como una persona de tu casa, tu profesor o profesora jefe, la persona orientadora o el encargado de convivencia escolar.",
        "No te corresponde confrontar a quien te presiona, ni demostrar nada, ni resolverlo solo. Guardar un secreto sobre contactos íntimos con un adulto protege solo a quien hace daño. Si crees que una persona está en peligro, avísale a un adulto de inmediato. En todos estos casos, la persona que sufre una agresión no es culpable.",
        "Cuando necesites apoyo, existe el Fono Niños 147, una línea de ayuda para niños, niñas y adolescentes. Si hay peligro inmediato, un adulto debe pedir ayuda a los servicios de emergencia. Escuchar a un amigo que cuenta algo difícil también es parte de cuidar: no lo juzgues, no repitas lo que te cuenta a otras personas del curso, y ayúdalo a hablar con un adulto de confianza.",
    ],
    [("acción segura", "paso que protege la integridad y acerca a una persona adulta de confianza"), ("persona adulta de confianza", "adulto que escucha, cree y ayuda"), ("convivencia escolar", "área del colegio que cuida el buen trato"), ("secreto dañino", "secreto que oculta una situación de daño o de peligro"), ("Fono Niños 147", "línea de ayuda para niños, niñas y adolescentes")],
    [
        W("Elegir la acción segura", "Un adulto que conoce a Paula, de 15 años, le dice: «Esto es nuestro secreto» y le pide que no cuente un contacto íntimo. ¿Qué debe hacer Paula?", ["No debe guardar un secreto dañino.", "Debe contarlo a una persona adulta de confianza."], "Avisar a una persona adulta de confianza"),
        W("Apoyar a un amigo", "Mateo cuenta a Isidora que alguien lo presiona para enviar una foto íntima. ¿Qué hace Isidora?", ["Lo escucha sin juzgar.", "Lo anima a hablar con un adulto de confianza.", "No difunde lo que le contó."], "Escucha, no juzga y lo anima a pedir ayuda adulta"),
    ],
    [
        M("Pensar que contarlo es «acusar» o «ser soplón».", "Se confunde pedir ayuda con traicionar.", "Avisar a un adulto cuida a la persona en riesgo."),
        M("Querer confrontar solo a la persona que presiona.", "Se cree que enfrentar resuelve el problema.", "Aléjate, no confrontes y avisa a una persona adulta."),
    ],
    R=[
        ex("En un caso inventado, un adulto le dice a un adolescente: «si cuentas esto, te meterás en problemas». ¿Cómo se clasifica esa frase? A) Una amenaza para mantener el secreto B) Un consejo para cuidarse", "A", "Busca que el secreto se mantenga y protege solo a quien hace daño."),
        ex("¿Cuál es una persona adulta de apoyo dentro del colegio? A) El encargado de convivencia escolar B) Un compañero de otro curso", "A", "Es una persona adulta que escucha y puede actuar."),
        ex("Tras una agresión, Paula piensa: «fue mi culpa por no haberme ido antes». ¿Qué debería recordar? A) La responsabilidad es de quien agrede B) Debió actuar distinto", "A", "La responsabilidad es de quien agrede, no de quien sufre."),
    ],
    U=[
        ex("¿Qué debe hacer primero alguien a quien presionan para enviar una foto íntima? A) Decir «no» y avisar a un adulto de confianza B) Enviarla con la cara tapada.", "A", "Enviarla expone su intimidad aunque tape la cara."),
        ex("Si un amigo te cuenta algo grave, ¿qué es lo correcto? A) Escucharlo y animarlo a hablar con un adulto B) Contarlo al curso.", "A", "Contarlo al curso lo expone."),
        ex("¿Para qué sirve el Fono Niños 147? A) Para pedir ayuda y orientación cuando algo te preocupa o te hace daño B) Para consultar notas y horarios del colegio", "A", "Es una línea de ayuda para niños, niñas y adolescentes."),
    ],
    A=[
        ex("Caso: un tío mayor le toca la espalda a Isidora y ella se siente incómoda. Pasos posibles: 1) alejarse, 2) avisar a un adulto de confianza, 3) dejar que pase. ¿Qué dos pasos corresponden?", "1 y 2", "Alejarse y avisar protegen; dejar que pase la deja en riesgo."),
        ex("Mateo dice que no quiere «ser acusador». Su amigo le explica que avisar a un adulto protege a alguien en riesgo. ¿Qué está claro? A) Avisar es cuidar B) Avisar es traicionar.", "A", "Pedir ayuda protege."),
        ex("Una compañera inventada recibe mensajes de un adulto desconocido que le pide ir a verlo sola. ¿Qué debe hacer? A) No ir y avisar a un adulto de confianza B) Ir con una amiga a escondidas.", "A", "Es una situación de peligro que se informa a un adulto."),
    ],
    Z=[
        ex("¿Por qué un secreto sobre contacto íntimo con un adulto debe contarse?", "Porque protege a la persona y detiene el daño", "Un secreto así beneficia solo a quien hace daño."),
        ex("Un amigo te pide no contar que su pareja lo golpeó. ¿Qué respuesta cuida a tu amigo? A) «Te escucho y vamos juntos con la orientadora.» B) «Prometo no decir nada a nadie.»", "A", "No se promete un secreto que mantiene el riesgo."),
    ],
    D=[
        arith("En un colegio inventado, 4 de cada 10 estudiantes saben a quién pedir ayuda. En un curso de 40, ¿cuántos saben a quién acudir?", "40//10*4", "Se calcula cuántos grupos de 10 hay y se multiplica por 4."),
        arith("Un establecimiento inventado tiene 2 orientadoras, 1 encargado de convivencia y 12 profesores jefe. ¿Cuántas personas adultas de apoyo nombradas hay en total?", "2+1+12", "Se suman todas las personas de apoyo."),
    ],
    context=[ex("A Pedro le llega un mensaje: «Si no me envías una foto íntima, le diré a todos que me engañaste». ¿Cuál es la acción segura? A) No enviar nada, guardar el mensaje y avisar a un adulto B) Enviar la foto para que no hable.", "A", "Enviarla da más poder al chantaje; guardar el mensaje sirve como prueba.")],
    selfcheck=[ex("En Orientación: ¿ante un contacto íntimo no deseado se debe avisar a un adulto de confianza?", "Sí", "Es la acción más segura."), ex("¿Debes guardar un secreto que oculta un daño?", "No", "El secreto protege a quien daña."), ex("¿Escuchar sin juzgar es parte de ayudar a un amigo?", "Sí", "Le da confianza para pedir ayuda.")],
    task=T("Lee este caso inventado: una compañera te cuenta que un adulto que la cuida le pide que guarde en secreto lo que hacen a solas y que la hace sentir muy incómoda. Escribe cuatro pasos que le propondrías, empezando por escuchar, e incluye a quién avisar y qué frase usarías.", "1) Escucharla sin juzgar. 2) Decirle que no tiene la culpa. 3) Animarla a avisar a su profesora jefe o a la orientadora, y acompañarla. 4) Frase: «Lo que me cuentas es importante; vamos a contárselo a una persona adulta que pueda ayudarnos».", ["escribe cuatro pasos", "incluye a quién avisar", "incluye una frase de apoyo", "no promete guardar secreto"], ["pasos escritos", "texto oral"], ["prometer guardar el secreto", "culpar a la compañera"], "Reconoce los pasos protectores y pregunta quién sería el mejor adulto para avisar."),
    reinforce="Escribe una frase para decirle a un amigo que necesita ayuda: «No es tu culpa, vamos con…».",
    extend="Explica por qué pedir ayuda no es traicionar.",
)

lesson(
    OA2, 5,
    "Una hoja y un lápiz. Las frases de ejemplo están escritas en los ejercicios; usa personas inventadas.",
    "Aprenderé a practicar frases para poner límites y a pedir ayuda sobre temas de sexualidad y vínculos. Sirve para saber qué decir y a quién acudir cuando algo me incomoda.",
    ["Sé elegir una acción segura.", "Conozco personas adultas de apoyo en el colegio."],
    [
        "Poner un límite es decir qué aceptas y qué no. Se hace con frases en primera persona, firmes y cortas: «No quiero», «Para, por favor», «No me siento cómoda con eso». No necesitas justificarte ni pedir perdón. Si no te escuchan, repite la frase y aléjate. Una buena frase para un límite tiene tres partes: lo que sientes, lo que pides y, si hace falta, lo que harás.",
        "Pedir ayuda a una persona adulta es otro acto de cuidado. Puedes decir: «Necesito contarte algo que me incomoda» y luego dar hechos: qué pasó, cuándo y dónde. No tienes que tener todas las pruebas. Si la primera persona no te escucha, sigue buscando a otra: la persona orientadora, la profesora jefe, una persona de tu casa, el centro de salud o el Fono Niños 147.",
        "En un chat, la comunicación también cuenta. Si alguien te presiona por mensajes, no respondas con enojo: guarda una captura, bloquea y avisa a un adulto. Y al recibir el «no» de otra persona, respétalo de inmediato: «ok, gracias por decírmelo». Practicar estas frases antes te ayuda a decirlas cuando las necesites.",
    ],
    [("límite", "lo que una persona acepta o no acepta"), ("frase en primera persona", "frase que empieza con «yo» y dice lo que uno siente o decide"), ("captura de pantalla", "imagen de lo que se ve en el celular, útil como evidencia"), ("bloquear", "impedir que otra persona te escriba o te vea"), ("evidencia", "prueba de lo ocurrido")],
    [
        W("Armar una frase de límite", "Fabián quiere decirle a un compañero que no le toque la mochila sin permiso. Usa las tres partes.", ["Siento: «me incomoda».", "Pido: «no la toques sin permiso».", "Haré: «si lo haces, me alejo»."], "«Me incomoda. No la toques sin permiso. Si lo haces, me alejo.»"),
        W("Pedir ayuda con hechos", "Lorena quiere contar a su profesora que un compañero le manda mensajes que la incomodan. ¿Qué hechos da?", ["Qué mensajes recibe.", "Desde cuándo.", "Qué hizo ella: guardó capturas y bloqueó."], "Qué, desde cuándo y qué hizo"),
    ],
    [
        M("Decir un límite pidiendo perdón o dando excusas largas.", "Se teme que el otro se enoje.", "Usa frases cortas y firmes, sin justificarte."),
        M("Esperar a tener todas las pruebas para pedir ayuda.", "Se cree que sin pruebas no te creerán.", "Cuenta lo que pasó y guarda las capturas; el adulto ayuda a averiguar."),
    ],
    R=[
        ex("¿Cuál frase tiene las tres partes (lo que siento, lo que pido, lo que haré)? A) «Me incomoda. Para, por favor. Si sigues, me voy.» B) «No sé, quizás, después vemos.»", "A", "Dice lo que siente, pide algo y anuncia qué hará."),
        ex("Un chat te incomoda y quieres mostrárselo a un adulto. ¿Qué sirve como evidencia? A) Una captura de pantalla con fecha y hora B) Un recuerdo vago de lo que decía", "A", "Muestra lo que se escribió."),
        ex("Alguien te presiona por chat. ¿Qué haces primero? A) Guardar una captura y luego bloquear B) Responder con insultos para que pare", "A", "La captura queda como evidencia y el bloqueo evita que siga."),
    ],
    U=[
        ex("¿Cuál frase es un límite claro? A) «Para, por favor, no me gusta.» B) «Quizás, no sé, déjame ver.»", "A", "Dice lo que siente y lo que pide."),
        ex("Si la primera persona adulta no te escucha, ¿qué haces? A) Sigues buscando a otra persona de confianza B) Dejas de contar.", "A", "Hay varias personas y servicios de apoyo."),
        ex("¿Qué debes responder cuando alguien te dice «no»? A) «Ok, gracias por decírmelo.» B) «Vamos, no seas así.»", "A", "Se respeta el límite."),
    ],
    A=[
        ex("Clasifica cada frase como L (límite claro) o E (excusa): 1) «No me gusta que me toques.» 2) «Es que mi mamá se enoja, por eso no.» 3) «Para, por favor.» Escribe las letras en orden.", "L, E, L", "La 1 y la 3 son directas; la 2 se apoya en otra persona."),
        ex("Rodrigo quiere pedir ayuda a su profesor jefe porque lo molestan con bromas sexuales. ¿Cuál es el mejor inicio? A) «Necesito contarle algo que me incomoda.» B) «No es nada, olvídelo.»", "A", "Abre la conversación con claridad."),
        ex("Una persona desconocida pide fotos íntimas a una amiga por chat. ¿Qué haces? A) Guardar la captura, bloquear y avisar a un adulto B) Reírte y contestar.", "A", "Es el protocolo de protección en línea."),
    ],
    Z=[
        ex("¿Por qué no es necesario justificar un «no»?", "Porque tienes derecho a decidir sobre tu cuerpo sin explicar", "El límite es un derecho y no depende de aprobación."),
        ex("¿Por qué conviene guardar las capturas de un chat que te incomoda? A) Porque permiten mostrar a un adulto qué pasó B) Para reenviarlas al curso.", "A", "Son evidencia; reenviarlas expone a otros."),
    ],
    D=[
        arith("Una orientadora inventada atiende 5 estudiantes por jornada, en 4 jornadas a la semana. ¿Cuántos estudiantes atiende por semana?", "5*4", "Se multiplican estudiantes por jornadas."),
        arith("En una actividad, 36 estudiantes practican frases de límite en parejas. ¿Cuántas parejas se forman?", "36//2", "Se divide el total entre los 2 integrantes de cada pareja."),
    ],
    context=[ex("Lucía recibe en el recreo comentarios sexuales de un compañero. ¿Qué serie de pasos es la más segura? A) Decir «para, no me gusta», alejarse y avisar a un adulto B) Gritarle y pegarle.", "A", "Pone un límite sin violencia y busca ayuda.")],
    selfcheck=[ex("En Orientación: ¿un límite debe ser claro y breve?", "Sí", "Se entiende mejor."), ex("¿Hay que tener todas las pruebas antes de pedir ayuda?", "No", "Basta contar lo que pasó."), ex("¿Puedes bloquear y avisar a un adulto si alguien te presiona por chat?", "Sí", "Es una forma de cuidarte.")],
    task=T("Lee las tres situaciones inventadas: (a) un compañero te hace bromas sexuales en el pasillo; (b) un chat desconocido te pide una foto; (c) una amiga te cuenta que su pololo le revisa el celular y se enoja. Escribe una frase de límite para (a), tres pasos de protección para (b) y una frase para ayudar a tu amiga en (c).", "(a) «Me incomoda. Para, por favor.» (b) Guardar captura, bloquear, avisar a un adulto. (c) «Lo que cuentas es importante, vamos a hablar con la orientadora».", ["escribe una frase de límite", "escribe tres pasos para el chat", "ofrece apoyo a la amiga", "no usa casos propios"], ["frases escritas", "juego de roles"], ["frase larga con excusas", "olvidar al adulto"], "Reconoce las frases firmes y pregunta cuál paso es el primero en el chat."),
    reinforce="Escribe dos frases cortas de límite para usar con un compañero que te molesta.",
    extend="Explica por qué bloquear no es lo mismo que dejar de pedir ayuda.",
)

lesson(
    OA2, 6,
    "Una hoja y un lápiz. Los casos del curso inventado están escritos en los ejercicios; ninguna actividad pide contar experiencias propias.",
    "Aprenderé a aplicar lo aprendido a un caso nuevo y a proponer acuerdos de respeto para un curso. Sirve para convivir cuidando la intimidad, la diversidad y la dignidad de todos.",
    ["Sé qué es el consentimiento.", "Sé poner un límite y pedir ayuda."],
    [
        "Transferir significa usar lo aprendido en una situación distinta. Frente a un caso nuevo, usa una secuencia: 1) separa hechos y emociones, 2) identifica los derechos en juego (dignidad, intimidad, integridad), 3) compara opciones con el semáforo, 4) elige una acción segura y 5) señala a qué adulto o servicio avisar.",
        "Respetar la diversidad también es parte del cuidado. Todas las personas tienen dignidad sin importar su orientación sexual o su identidad de género; burlarse, difundir rumores o excluir es discriminación y daña. Los rumores sobre la intimidad de alguien, incluso si fueran ciertos, no se difunden: la intimidad se protege.",
        "Un curso puede construir acuerdos de respeto: reglas simples y observables que todos cumplen, como «compartimos solo lo que cada persona autoriza», «aceptamos un no sin insistir» y «si alguien se siente mal, avisamos a un adulto». Los acuerdos funcionan mejor si se escriben en positivo, se revisan cada cierto tiempo y todos participan al crearlos.",
    ],
    [("transferir", "usar lo aprendido en una situación distinta"), ("diversidad", "variedad de personas, identidades y formas de ser"), ("discriminación", "trato injusto por una característica de la persona"), ("rumor", "comentario que circula sin comprobarse"), ("acuerdo de respeto", "regla simple y observable que un grupo se compromete a cumplir")],
    [
        W("Aplicar la secuencia", "Caso: se difunde un rumor sobre la intimidad de una compañera. Aplica la secuencia en dos pasos.", ["Derecho en juego: su intimidad y dignidad.", "Acción segura: no reenviar, y avisar a un adulto del colegio."], "No reenviar y avisar a un adulto"),
        W("Redactar un acuerdo", "Transforma «no molesten» en un acuerdo observable en positivo.", ["Un acuerdo debe decir qué sí se hace.", "«Hablamos sin insultos y aceptamos un no.»"], "«Hablamos sin insultos y aceptamos un no.»"),
    ],
    [
        M("Pensar que difundir un rumor «verdadero» no hace daño.", "Se cree que lo cierto se puede contar.", "La intimidad se protege aunque el dato sea cierto."),
        M("Redactar acuerdos que solo prohíben y no dicen qué hacer.", "Sirven menos porque no son observables.", "Escríbelos en positivo, con conductas que se vean."),
    ],
    R=[
        ex("Burlarse de la orientación sexual de alguien, ¿es respeto o discriminación?", "Discriminación", "Es un trato injusto por una característica de la persona."),
        ex("Difundir un rumor sobre la intimidad de una persona, ¿la protege o la daña?", "La daña", "Expone su intimidad."),
        ex("¿Cuál es un acuerdo escrito en positivo? A) «Escuchamos a cada persona sin interrumpir.» B) «No interrumpan.»", "A", "Dice qué conducta sí se hace; la otra solo prohíbe."),
    ],
    U=[
        ex("¿Cuál es un acuerdo observable? A) «Aceptamos un no sin insistir.» B) «Seamos buenos.»", "A", "La primera dice una conducta que se ve."),
        ex("Se comenta que Bruno, un compañero, «es diferente». ¿Qué valor corresponde? A) Dignidad y respeto a la diversidad B) Dudar de él.", "A", "Todas las personas tienen dignidad."),
        ex("En la secuencia de la clase, ¿qué se hace después de comparar opciones con el semáforo? A) Elegir una acción segura B) Difundir el caso.", "A", "Es el paso 4."),
    ],
    A=[
        ex("Un grupo comparte una imagen íntima de una compañera, inventada, en un chat. Siguiendo el protocolo, ¿qué haces? A) No reenviarla, no guardarla y avisar a un adulto B) Guardarla por si sirve.", "A", "Guardar o reenviar imágenes íntimas las difunde."),
        ex("Clasifica: 1) hacer un chiste sobre la identidad de género de alguien; 2) invitar a un compañero nuevo a jugar. ¿Cuál es discriminación?", "La 1", "Se burla de una característica personal."),
        ex("Un curso quiere un acuerdo sobre fotos. ¿Cuál sirve? A) «Tomamos y publicamos fotos solo con permiso de cada persona.» B) «Nadie hace cosas malas.»", "A", "Describe una conducta clara y observable."),
    ],
    Z=[
        ex("¿Por qué un rumor sobre la intimidad de una persona hace daño aunque sea cierto?", "Porque expone su intimidad sin que ella lo decida", "La intimidad es un derecho y no se difunde."),
        ex("Un curso revisa su acuerdo de respeto cada mes. ¿Qué ventaja tiene? A) Ajusta lo que no funciona B) Hace más largas las clases.", "A", "La revisión mejora los acuerdos."),
    ],
    D=[
        arith("Un curso de 40 estudiantes forma 5 equipos iguales para redactar acuerdos. ¿Cuántos estudiantes tiene cada equipo?", "40//5", "Se divide el total entre el número de equipos."),
        arith("De 30 acuerdos propuestos, el curso votó y se descartaron 11 por repetidos. ¿Cuántos acuerdos distintos quedan?", "30-11", "Al total se le restan los repetidos."),
    ],
    context=[ex("En el Consejo de Curso se propone el acuerdo «llamamos a cada persona por el nombre con que ella pide ser llamada». ¿Qué valor protege? A) La dignidad y el respeto a la diversidad B) La rapidez de las clases.", "A", "Reconoce a cada persona como ella se identifica.")],
    selfcheck=[ex("En Orientación: ¿la intimidad de una persona se protege aunque el dato sea cierto?", "Sí", "No se difunde sin su decisión."), ex("¿Un acuerdo de respeto se escribe mejor en positivo?", "Sí", "Dice qué se hace."), ex("¿Burlarse de la identidad de alguien es discriminación?", "Sí", "Daña su dignidad.")],
    task=T("Un curso inventado de 1.º medio vive tres situaciones: (a) circula un rumor sobre la intimidad de una compañera; (b) alguien se burla de la identidad de otro estudiante; (c) una pareja se pelea a gritos en el patio. Redacta tres acuerdos de respeto en positivo, uno por cada situación, y escribe a qué adulto del colegio avisarías en cada caso.", "(a) Compartimos solo lo que cada persona autoriza; aviso a la orientadora. (b) Nos tratamos con el nombre que cada persona elige; aviso a convivencia escolar. (c) Hablamos sin gritos y pedimos ayuda si hay violencia; aviso a la profesora jefe.", ["redacta tres acuerdos en positivo", "cada acuerdo es observable", "nombra un adulto por caso", "no incluye experiencias propias"], ["lista escrita", "afiche del curso"], ["acuerdos solo prohibitivos", "olvidar al adulto"], "Reconoce los acuerdos observables y pregunta cómo revisarían que se cumplen."),
    reinforce="Reescribe en positivo: «no se burlen».",
    extend="Explica por qué la diversidad es parte del cuidado entre compañeros.",
)
