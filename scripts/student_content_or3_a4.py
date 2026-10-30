"""Cuaderno del estudiante, 3.º básico Orientación: OA 07 (participación y responsabilidades) y OA 08 (hábitos, esfuerzo, honestidad y organización)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA7, OA8 = "OR03 OA 07", "OR03 OA 08"


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
    "Una hoja y un lápiz. Las situaciones del curso están escritas en los ejercicios.",
    "Aprenderé a proponer una iniciativa clara y a recibir las ideas de otros con respeto. Sirve para participar en las decisiones del curso.",
    ["Sé dar mi opinión.", "Sé esperar mi turno para hablar."],
    [
        "Una iniciativa es una idea que alguien propone para mejorar algo en el curso o en la escuela. Por ejemplo: «Hagamos un rincón de lectura» o «Cuidemos las plantas del patio». Participar es hacer propuestas, escuchar las de otros y ayudar a que se realicen. No es mandar ni decidir por todos.",
        "Una buena propuesta dice qué se hará, para qué sirve y cuándo. Por ejemplo: «Propongo un rincón de lectura desde el lunes, para que podamos leer en los recreos lluviosos». Si puedes, agrega cómo hacerlo, como traer libros del curso. Así los demás entienden y pueden opinar.",
        "También hay que saber recibir iniciativas. Escucha sin interrumpir, pregunta si no entiendes y di con respeto si estás de acuerdo o no. Si tu idea no se elige, no pasa nada: participar es compartir y respetar al grupo. Todas las ideas merecen ser escuchadas.",
    ],
    [("iniciativa", "idea que alguien propone para mejorar algo"), ("participar", "tomar parte en lo que hace el grupo"), ("propuesta", "idea que presento a otros"), ("acuerdo", "decisión que acepta el grupo"), ("respetar", "tratar con cuidado lo que otros piensan")],
    [
        W("Propuesta clara", "¿Cuál propuesta es más clara: «Hagamos algo» o «Propongo ordenar la biblioteca del curso el viernes para encontrar los libros más rápido»?", ["Una buena propuesta dice qué, para qué y cuándo.", "La segunda lo dice.", "La primera es muy general."], "«Propongo ordenar la biblioteca del curso el viernes para encontrar los libros más rápido»"),
        W("Recibir una idea", "Rita propone un rincón de lectura. A Beto no le gusta. ¿Qué respuesta respeta a Rita: «Esa idea es tonta» o «Entiendo tu idea, yo prefiero otra por esta razón»?", ["Escucha la idea completa.", "Dice su opinión con respeto.", "No se burla ni la rechaza de mala forma."], "«Entiendo tu idea, yo prefiero otra por esta razón»"),
    ],
    [
        M("Pensar que participar es mandar a los demás.", "Se confunde proponer con decidir por otros.", "Participar es proponer, escuchar y respetar las decisiones del grupo."),
        M("Enojarme porque mi idea no fue elegida.", "Siento que mi idea es lo mismo que yo.", "Una idea puede no ser elegida; yo sigo siendo parte del grupo."),
    ],
    R=[
        ex("¿Una iniciativa es una idea para mejorar algo?", "Sí", "Se propone al grupo."),
        ex("¿Participar es escuchar las ideas de otros?", "Sí", "También se escucha y se colabora."),
        ex("¿Todas las ideas merecen ser escuchadas?", "Sí", "Se escuchan antes de decidir."),
    ],
    U=[
        ex("¿Qué tres cosas dice una buena propuesta?", "Qué se hará, para qué y cuándo", "Así los demás entienden."),
        ex("En Orientación: ¿Participar es lo mismo que mandar?", "No", "Participar es proponer y respetar al grupo."),
        ex("Si tu idea no es elegida, ¿dejas de ser parte del grupo?", "No", "Sigues participando en lo que se decida."),
    ],
    A=[
        ex("Escribe una propuesta para cuidar las plantas del curso: qué, para qué y cuándo.", "Regar las plantas los lunes para que no se sequen", "Dice qué, para qué y cuándo."),
        ex("Un compañero propone una idea y tú no la entiendes. ¿Qué haces: reírte o preguntar?", "Preguntar", "Preguntar ayuda a entender."),
        ex("Elige la respuesta respetuosa: «Esa idea es tonta» o «Prefiero otra porque…».", "«Prefiero otra porque…»", "Da una opinión sin burlarse."),
    ],
    Z=[
        ex("Dos niñas proponen ideas distintas para el diario mural. Una dice «la mía es mejor y punto». ¿Participa con respeto?", "No", "No escucha ni acepta otras ideas."),
        ex("Un niño es tímido y casi no habla. ¿Cómo puede participar el curso para que él aporte?", "Dándole tiempo o pidiéndole su idea por escrito", "Participar admite distintas formas."),
    ],
    D=[
        arith("En el curso se proponen 3 ideas por la mañana y 4 en la tarde. ¿Cuántas ideas hay en total?", "3+4", "Se suman las ideas de ambos momentos."),
        ex("Una niña propone un cambio que perjudicaría a un compañero. ¿Conviene aceptar la propuesta sin revisar los derechos de todos?", "No", "Toda propuesta debe respetar a todos."),
    ],
    context=[ex("En el consejo de curso, Camilo propone: «Hagamos un buzón de ideas para que todos puedan proponer sin hablar fuerte». Los demás escuchan y preguntan. ¿Participan bien?", "Sí", "Proponen, escuchan y preguntan.")],
    selfcheck=[ex("En Orientación: ¿participar es mandar?", "No", "Es proponer y respetar."), ex("¿Una propuesta clara dice qué y para qué?", "Sí", "Ayuda a entender."), ex("¿Puedo aceptar que mi idea no sea elegida?", "Sí", "Es parte de convivir.")],
    task=T("Elige un problema del curso de esta lista: el patio con basura, pocos libros en la sala, mucho ruido, sin plantas. Escribe una propuesta con qué, para qué y cuándo. Después escribe una frase respetuosa para recibir una idea distinta a la tuya.", "Problema: pocos libros. Propuesta: armar un rincón de lectura el viernes para leer en los recreos. Frase: «Entiendo tu idea, ¿cómo la haríamos?».", ["propuesta con qué, para qué y cuándo", "frase respetuosa para otra idea", "no manda ni decide por todos"], ["propuesta escrita"], ["propuesta muy general", "burlarse de otras ideas"], "Reconoce la propuesta y revisa que sea clara."),
    reinforce="Escribe una iniciativa pequeña que mejoraría tu sala.",
    extend="Explica cómo recibir una idea que no te gusta sin burlarte.",
)

lesson(
    OA7, 2,
    "Una hoja y un lápiz. Las votaciones de ejemplo están escritas en los ejercicios.",
    "Aprenderé a tomar decisiones con reglas claras, como votar y contar. Sirve para que el curso decida de manera justa.",
    ["Sé proponer una idea.", "Sé contar hasta 100."],
    [
        "Para decidir en un grupo hacen falta reglas claras, que se conocen antes. Una regla es hablar por turnos. Otra es votar: cada persona tiene un voto y vale lo mismo. Se puede votar con la mano levantada o con un papel doblado, para que sea secreto. Se cuentan los votos y gana la opción con más votos.",
        "Respetar la decisión es parte de participar. Quien votó por otra opción también cumple lo que se decidió. Y quien ganó no se burla de los demás. Si hay empate, se puede hablar más y votar otra vez, o usar una regla acordada antes, como que el empate se resuelve con un sorteo.",
        "Las decisiones del curso deben respetar los derechos de todos. Si una propuesta deja a alguien afuera o lo expone, no se vota: se cambia. Y nadie debe ser presionado a votar de cierta manera.",
    ],
    [("regla", "norma acordada que todos conocen"), ("voto", "elección que hace cada persona"), ("mayoría", "la opción con más votos"), ("empate", "cuando dos opciones tienen los mismos votos"), ("sorteo", "elegir al azar con una regla justa")],
    [
        W("Contar votos", "Votaciones: biblioteca 9 votos, plantas 12 votos, juegos 7 votos. ¿Qué opción gana?", ["Se comparan los votos.", "12 es el mayor.", "Gana la opción con más votos."], "Plantas"),
        W("Empate", "Dos propuestas tienen 10 votos cada una. ¿Qué se puede hacer?", ["No hay mayoría.", "Se puede debatir y votar otra vez.", "O usar una regla acordada antes, como un sorteo."], "Debatir y votar otra vez, o usar la regla acordada"),
    ],
    [
        M("Pensar que, si perdí, no tengo que cumplir lo decidido.", "Se siente que mi opinión no importó.", "Cumplir la decisión del grupo es parte de convivir."),
        M("Presionar a otros para que voten como yo.", "Quiero que mi idea gane.", "Cada persona vota libremente."),
    ],
    R=[
        ex("¿Cada persona tiene un voto que vale lo mismo?", "Sí", "Todos tienen los mismos derechos."),
        ex("¿Gana la opción con más votos?", "Sí", "Esa es la regla de mayoría."),
        ex("¿Se puede presionar a alguien para que vote de cierta manera?", "No", "El voto es libre."),
    ],
    U=[
        ex("¿Por qué las reglas se acuerdan antes de votar?", "Para que la decisión sea justa", "Así todos saben cómo se decidirá."),
        ex("Si perdió tu opción, ¿qué haces?", "Respeto y cumplo lo decidido", "Es parte de participar."),
        ex("¿Una propuesta que deja a alguien afuera se vota igual?", "No", "Debe respetar los derechos de todos."),
    ],
    A=[
        arith("En una votación, 8 niños eligen cuentos y 11 eligen juegos. ¿Cuántos votos hay en total?", "8+11", "Se suman todos los votos."),
        arith("Gana una propuesta con 15 votos y la otra tiene 9. ¿Cuántos votos de diferencia hay?", "15-9", "Se resta el menor al mayor."),
        ex("Votan por paseo, cine o picnic: paseo 6, cine 10, picnic 8. ¿Cuál gana?", "Cine", "Tiene más votos."),
    ],
    Z=[
        ex("Un niño dice: «Voté por la otra opción, así que no la cumplo». ¿Es correcto?", "No", "La decisión del grupo se respeta."),
        ex("Dos opciones tienen los mismos votos. ¿Es justo elegir al azar si todos lo acordaron antes?", "Sí", "La regla era conocida y justa."),
    ],
    D=[
        arith("El curso tiene 28 estudiantes y todos votaron. Si 17 votaron por una opción, ¿cuántos votaron por la otra?", "28-17", "Se resta los votos de una opción al total."),
        ex("Una votación quiere decidir si dejar fuera de un juego a un niño. ¿Se debe votar eso?", "No", "No se puede votar para excluir a alguien."),
    ],
    context=[ex("Para elegir un juego, la profesora explica: «Cada uno vota una vez, alzando la mano; gana el que tenga más votos; si hay empate, volvemos a conversar». ¿Las reglas están claras?", "Sí", "Dice cómo se vota y qué pasa con el empate.")],
    selfcheck=[ex("En Orientación: ¿las reglas se conocen antes de decidir?", "Sí", "Así es justo."), ex("¿Cada voto vale lo mismo?", "Sí", "Todos tienen igual derecho."), ex("¿Hay que cumplir lo que decide el grupo si fue justo?", "Sí", "Es parte de convivir.")],
    task=T("El curso debe elegir entre tres actividades: pintar un mural, hacer una feria de libros o plantar flores. Escribe tres reglas para la votación (por turnos, un voto por persona y qué pasa con el empate). Después cuenta estos votos: mural 10, libros 7, flores 12, y escribe cuál gana y cuántos votos hubo en total.", "Reglas: hablar por turnos; un voto por persona; empate: nueva votación. Gana flores con 12; total 29.", ["tres reglas claras", "cuenta correcta de votos", "respeta la decisión"], ["reglas y conteo escritos"], ["no decir qué pasa en un empate", "sumar mal"], "Reconoce las reglas y revisa el conteo."),
    reinforce="Escribe una regla para votar en tu sala.",
    extend="Explica qué harías si tu opción pierde.",
)

lesson(
    OA7, 3,
    "Una hoja y un lápiz. Las listas de roles están escritas en los ejercicios.",
    "Aprenderé a repartir roles en el curso de manera equitativa. Sirve para que todos participen y se cuiden los derechos de cada uno.",
    ["Sé votar con reglas claras.", "Sé escuchar las ideas de otros."],
    [
        "Un rol es una tarea que una persona tiene en el grupo. Por ejemplo: encargado de materiales, de ordenar, de anunciar o de anotar acuerdos. Distribuir roles es repartirlos entre todos. Para que sea equitativo, cada persona tiene la misma oportunidad. Se pueden rotar los roles: cada semana, otras personas los hacen.",
        "Los roles no se reparten por género, popularidad o porque alguien «siempre lo hace bien». Un niño puede ser encargado de ordenar y una niña de anunciar. Todos pueden aprender un rol. Si alguien necesita ayuda o prefiere uno distinto, se conversa. Ningún rol es solo para un tipo de persona.",
        "Respetar los derechos también es no cargar a una sola persona con todo, ni dejar a alguien sin tarea. Se puede ofrecer elegir entre dos roles. Y si un rol no se puede por algún motivo, se busca otro o se pide ayuda al profesor.",
    ],
    [("rol", "tarea que tengo en un grupo"), ("equidad", "dar a cada uno lo que necesita para participar"), ("rotar", "cambiar turnos entre todos"), ("distribuir", "repartir entre varias personas"), ("derecho", "algo que todos merecen")],
    [
        W("Repartir roles", "El curso tiene 24 estudiantes y 6 roles. Si cada rol lo hacen la misma cantidad de niños, ¿cuántos niños hay por rol?", ["Se reparten 24 niños en 6 roles.", "Se divide 24 entre 6.", "El resultado es la cantidad por rol."], "4 niños por rol"),
        W("Un rol no es de género", "Alguien dice: «Ordenar es cosa de niñas». ¿Qué respondes?", ["Un rol no depende del género.", "Todos pueden aprender a ordenar.", "Es una idea injusta."], "Que todos pueden ordenar"),
    ],
    [
        M("Dar siempre el mismo rol a la misma persona porque lo hace bien.", "Es más fácil y rápido.", "Rota los roles para que todos aprendan."),
        M("Repartir roles según género o a quién cae mejor.", "Se repiten ideas antiguas o preferencias.", "Reparte por turnos o sorteo, con las mismas oportunidades."),
    ],
    R=[
        ex("¿Un rol es una tarea en el grupo?", "Sí", "Cada persona aporta con una tarea."),
        ex("¿Rotar significa cambiar de roles entre todos?", "Sí", "Todos tienen su oportunidad."),
        ex("¿Los roles dependen del género?", "No", "Todos pueden hacer cualquier rol."),
    ],
    U=[
        ex("¿Por qué es mejor rotar los roles?", "Porque todos tienen la oportunidad de aprender", "Así se reparte con equidad."),
        ex("Si alguien prefiere otro rol, ¿qué se puede hacer?", "Conversarlo y ver si se puede cambiar", "Se escucha lo que necesita."),
        ex("¿Se debe cargar a una persona con todos los roles?", "No", "Los roles se reparten entre todos."),
    ],
    A=[
        arith("El grupo tiene 5 roles y 20 niños. Si todos los roles tienen la misma cantidad de niños, ¿cuántos niños hay por rol?", "20//5", "Se reparten en partes iguales."),
        ex("Un curso reparte los roles por sorteo. ¿Es una manera equitativa?", "Sí", "Todos tienen la misma oportunidad."),
        ex("Escribe una frase para ofrecer a alguien elegir entre dos roles.", "¿Prefieres ser encargado de materiales o de anotar?", "Le da elección."),
    ],
    Z=[
        ex("La más popular siempre es la anunciadora. Otra niña también quiere. ¿Qué puede proponer el curso?", "Rotar el rol cada semana", "Todas tienen la misma oportunidad."),
        ex("Un niño dice: «Mejor que lo haga Tomás, que lo hace perfecto». ¿Eso reparte con equidad?", "No", "No da oportunidad a los demás."),
    ],
    D=[
        arith("Hay 3 roles para repartir entre 12 niños, con la misma cantidad de niños en cada rol. ¿Cuántos niños quedan en cada rol?", "12//3", "Se reparte el total en partes iguales."),
        ex("Si se rotan 4 roles entre 4 grupos y ningún grupo repite un rol, ¿cuántos roles distintos habrá hecho cada grupo después de 4 semanas?", "4", "Cada grupo hace los 4 roles."),
    ],
    context=[ex("En el consejo, el curso arma una lista: materiales, ordenar, anunciar y anotar. Cada lunes cambian de rol por sorteo. ¿Reparten con equidad?", "Sí", "Todos tienen la misma oportunidad.")],
    selfcheck=[ex("En Orientación: ¿los roles son para un solo género?", "No", "Todos pueden hacerlos."), ex("¿Rotar ayuda a repartir con equidad?", "Sí", "Así todos aprenden."), ex("¿Se puede elegir entre dos roles?", "Sí", "Respeta lo que cada uno prefiere.")],
    task=T("El curso necesita cuatro roles para limpiar la sala: materiales, borrar la pizarra, ordenar libros y regar plantas. Hay ocho niños en el grupo. Escribe una forma equitativa de repartirlos (sorteo o rotación) y cuántos niños quedan en cada rol. Agrega una regla para que nadie cargue con todo.", "Sorteo semanal: 2 niños por rol (8 entre 4). Regla: nadie repite el mismo rol dos semanas seguidas.", ["reparto equitativo", "cuántos niños por rol (8 entre 4)", "regla para no cargar a una persona"], ["plan escrito"], ["repartir por género o popularidad", "dejar a alguien sin rol"], "Reconoce el reparto y verifica que sea equitativo."),
    reinforce="Escribe una lista de cuatro roles que tu curso podría rotar.",
    extend="Explica por qué repartir roles por género no es justo.",
)

lesson(
    OA7, 4,
    "Una hoja y un lápiz. Los registros de ejemplo están escritos en los ejercicios.",
    "Aprenderé a cumplir mi responsabilidad en el curso y a evaluar cómo me fue, con honestidad y sin culpar a nadie. Sirve para mejorar el trabajo del grupo.",
    ["Sé repartir roles con equidad.", "Sé proponer una iniciativa."],
    [
        "Una responsabilidad es una tarea que te comprometiste a hacer. Cumplirla es importante porque otros cuentan contigo. Para cumplir, anota qué debes hacer y cuándo. Por ejemplo: «Regar las plantas el lunes y el jueves». Si no puedes hacerlo, avisa con tiempo para que otro te ayude.",
        "Después de cumplir, se evalúa: ¿qué hice?, ¿qué salió bien?, ¿qué podría mejorar? Una buena evaluación mira lo que pasó, no busca culpables. Por ejemplo: «Regué las plantas el lunes, pero olvidé el jueves; mañana pondré un recordatorio». Decir lo que pasó con honestidad ayuda a mejorar.",
        "También se revisan los derechos de todos: ¿alguien hizo demasiado?, ¿alguien se quedó sin participar? Si hace falta, se cambian los roles. Si un compañero tiene dificultades, se le ofrece ayuda y no se le reta delante de todos.",
    ],
    [("responsabilidad", "tarea que me comprometí a hacer"), ("cumplir", "hacer lo que me comprometí a hacer"), ("evaluar", "revisar cómo salió algo"), ("recordatorio", "señal que me ayuda a no olvidar"), ("honestidad", "decir lo que pasó sin esconderlo")],
    [
        W("Anotar y cumplir", "Rafa debe ordenar los libros los viernes. ¿Qué puede hacer para no olvidarlo?", ["Anota el día.", "Pone un recordatorio visible.", "Así cumple lo que prometió."], "Anotarlo y poner un recordatorio"),
        W("Evaluar con honestidad", "Lola dice: «Regué dos veces de las tres que debía». ¿Cuántas veces olvidó regar?", ["Debía regar 3 veces.", "Lo hizo 2.", "Se resta 3 menos 2."], "1 vez"),
    ],
    [
        M("Decir «no fue mi culpa» sin mirar qué podría cambiar.", "Duele reconocer un error.", "Cuenta lo que pasó y qué harás distinto, sin culpar."),
        M("Retar a un compañero delante de todos por no cumplir.", "Se piensa que así aprende.", "Se le ofrece ayuda y se conversa en privado."),
    ],
    R=[
        ex("¿Cumplir mi responsabilidad es importante porque otros cuentan conmigo?", "Sí", "El grupo depende de lo que cada uno hace."),
        ex("¿Evaluar es revisar cómo salió algo?", "Sí", "Ayuda a mejorar."),
        ex("Si no puedes cumplir, ¿conviene avisar con tiempo?", "Sí", "Así otro puede ayudar."),
    ],
    U=[
        ex("¿Por qué conviene decir lo que pasó con honestidad?", "Porque ayuda a mejorar", "Sin honestidad no se aprende."),
        ex("¿Una buena evaluación busca culpables?", "No", "Busca entender y mejorar."),
        ex("Si un compañero tiene dificultades, ¿qué le ofreces?", "Ayuda", "Retarlo no lo ayuda."),
    ],
    A=[
        arith("Camilo debía cumplir su responsabilidad 5 días. Cumplió 4. ¿Cuántos días le faltaron?", "5-4", "Se resta lo cumplido al total."),
        ex("Escribe un recordatorio para regar las plantas los lunes.", "Poner una nota en la mochila que diga «regar el lunes»", "Ayuda a no olvidar."),
        ex("Marta olvidó su tarea de ordenar. Escribe una frase honesta de evaluación.", "Olvidé ordenar, mañana pondré un recordatorio", "Dice lo que pasó y qué hará."),
    ],
    Z=[
        ex("Un niño dice: «Yo siempre cumplo», pero faltó dos veces. ¿Su evaluación es honesta?", "No", "Esconde lo que pasó."),
        ex("Dos compañeros evalúan: uno dice «fue culpa de Rita» y otra «el lunes olvidé; mañana lo haré». ¿Quién evalúa mejor?", "La que explica qué pasó y qué hará", "Se hace cargo de su parte."),
    ],
    D=[
        arith("El grupo tiene 6 responsabilidades. Cumplió 4 la semana 1 y 5 la semana 2. ¿Cuántas más cumplió en la semana 2?", "5-4", "Se compara la semana 2 con la 1."),
        ex("Si un niño hizo todas las tareas del grupo, ¿se respetaron los derechos de los demás?", "No", "Todos tienen derecho a participar."),
    ],
    context=[ex("Al final de la semana, el grupo revisa: «Se regaron las plantas 3 de 4 veces. Falló el jueves. ¿Qué podemos cambiar?». ¿Evalúan sin buscar culpables?", "Sí", "Revisan lo que pasó y buscan mejorar.")],
    selfcheck=[ex("En Orientación: ¿evaluar es solo buscar culpables?", "No", "Evaluar sirve para mejorar."), ex("¿Avisar si no puedo cumplir es responsable?", "Sí", "Permite que otro ayude."), ex("¿Es bueno anotar mis tareas?", "Sí", "Ayuda a recordar.")],
    task=T("Lee: tu grupo debía ordenar la sala cuatro veces esta semana y la ordenó tres. Escribe una evaluación con tres partes: qué salió bien, qué faltó y qué harían distinto. Evita culpar a alguien por su nombre.", "Salió bien: ordenamos 3 veces. Faltó: una vez. Haremos: poner un recordatorio.", ["tres partes", "dice cuánto faltó (4 menos 3)", "no culpa a nadie"], ["evaluación escrita"], ["culpar a un compañero", "no decir qué cambiará"], "Reconoce la evaluación y verifica que no culpe."),
    reinforce="Anota una responsabilidad tuya de esta semana y cómo te fue.",
    extend="Propón dos recordatorios para cumplir una tarea del curso.",
)

# ================================================================ OA 08
lesson(
    OA8, 1,
    "Una hoja y un lápiz. Los horarios y las listas de útiles están escritos en los ejercicios.",
    "Aprenderé a organizar mi tiempo y mis útiles para llegar preparado a clases. Sirve para trabajar con calma y a tiempo.",
    ["Sé leer la hora en punto y media.", "Sé que debo traer mis útiles."],
    [
        "Organizarte es preparar con tiempo lo que necesitas. Por ejemplo, revisar la mochila la noche anterior con ayuda de una lista de útiles: cuaderno, estuche, lápices y lo que pida la profesora. Así no olvidas nada. También es útil tener un lugar fijo donde dejar tus cosas.",
        "La puntualidad es llegar a la hora acordada. Asistir a clases y llegar a tiempo ayuda a no perder partes de lo que se enseña. Se aprende de a poco y ayuda a no perder partes de la clase. Planea cuánto tiempo necesitas para alistarte. A veces se llega tarde por cosas que no controlas, como el transporte o el tiempo de los adultos. Eso no es tu culpa: puedes avisar y pedir ayuda.",
        "Tener un horario de la semana ayuda a saber qué llevar cada día. Una meta pequeña puede ser: «Esta semana, revisaré mi mochila antes de dormir». Si un día falla, vuelves a intentar al día siguiente.",
    ],
    [("organización", "preparar con tiempo lo que necesito"), ("puntualidad", "llegar a la hora acordada"), ("útiles", "materiales que uso en clases"), ("lista", "anotación de cosas que necesito"), ("meta", "lo que quiero lograr")],
    [
        W("Revisar con lista", "La lista pide: cuaderno, estuche, regla. Tomás tiene cuaderno y estuche. ¿Qué le falta?", ["La lista tiene tres cosas.", "Tiene dos.", "Falta la regla."], "La regla"),
        W("Tiempo para alistarse", "Lola necesita 10 minutos para vestirse y 15 para desayunar. ¿Cuántos minutos necesita en total?", ["Se suman los tiempos.", "10 más 15.", "El resultado es el tiempo que necesita."], "25 minutos"),
    ],
    [
        M("Culparme porque llegué tarde por algo que no controlo.", "Se piensa que todo depende de mí.", "Avisa y pide ayuda; no es tu culpa lo que dependió de otros."),
        M("Preparar la mochila en la mañana, con apuro.", "Parece que da lo mismo cuándo.", "Revisa la noche anterior con una lista."),
    ],
    R=[
        ex("¿Una lista de útiles ayuda a no olvidar nada?", "Sí", "Se revisa cada cosa."),
        ex("¿Revisar la mochila la noche anterior es organizarse?", "Sí", "Se prepara con tiempo."),
        ex("¿Puntualidad es llegar a la hora acordada?", "Sí", "Ayuda a no perder la clase."),
    ],
    U=[
        ex("Si llegas tarde por algo que no controlas, ¿qué haces?", "Aviso y pido ayuda", "No es tu culpa."),
        ex("¿Por qué ayuda tener un horario?", "Porque muestra qué llevar cada día", "Así no se olvida nada."),
        ex("¿Una meta pequeña puede ser revisar la mochila?", "Sí", "Es concreta y posible."),
    ],
    A=[
        arith("Rosa necesita 12 minutos para vestirse y 18 para desayunar. ¿Cuántos minutos necesita en total?", "12+18", "Se suman los dos tiempos."),
        ex("La lista dice: cuaderno, lápiz, goma, regla. Rafa tiene cuaderno, lápiz y regla. ¿Qué le falta?", "La goma", "Es lo único que no tiene."),
        ex("Escribe una meta pequeña de organización para esta semana.", "Revisar mi mochila cada noche", "Es clara y se puede cumplir."),
    ],
    Z=[
        ex("Un niño llegó tarde porque el transporte se retrasó. ¿Es su culpa?", "No", "Depende de factores fuera de su control."),
        ex("Dos niñas: una prepara la mochila en la noche y la otra en la mañana con apuro. ¿Quién tendrá menos olvidos probablemente?", "La que prepara la noche anterior", "Con calma se revisa mejor."),
    ],
    D=[
        arith("En una semana, un niño revisó su mochila 4 noches y otro 5 noches. ¿Cuántas noches revisaron entre los dos?", "4+5", "Se suman las noches de cada niño."),
        ex("Una mochila tiene 8 cosas en la lista y se llevan 6. ¿Cuántas faltan?", "2", "8 menos 6 es 2."),
    ],
    context=[ex("Antes de dormir, Camila mira su lista, pone el cuaderno de lenguaje y el estuche en la mochila y deja la ropa lista. ¿Se organizó con tiempo?", "Sí", "Preparó todo la noche anterior.")],
    selfcheck=[ex("En Orientación: ¿llegar tarde por el transporte es mi culpa?", "No", "Depende de otros."), ex("¿Revisar con una lista ayuda?", "Sí", "No se olvida nada."), ex("¿Puedo volver a intentar si un día me falla?", "Sí", "Los hábitos se construyen de a poco.")],
    task=T("Arma tu lista de útiles para el lunes con al menos cinco cosas (por ejemplo: cuaderno, estuche, lápiz, goma, regla, botella). Escribe una hora aproximada en que revisarás la mochila y una meta pequeña de organización para esta semana. Si algo no depende de ti, escribe qué harías (avisar o pedir ayuda).", "Lista: cuaderno, estuche, lápiz, goma, regla. Reviso a las 20:00. Meta: revisar la mochila cada noche. Si llego tarde, aviso.", ["lista de al menos cinco cosas", "hora y meta concretas", "sabe que lo que no controla no es su culpa"], ["lista escrita"], ["culparse por lo que no controla", "metas poco claras"], "Reconoce la lista y la meta."),
    reinforce="Escribe tu horario de mañana: qué libros y cuadernos llevarás.",
    extend="Propón un lugar fijo en tu casa para dejar tus útiles.",
)

lesson(
    OA8, 2,
    "Una hoja y un lápiz. Los calendarios y las tareas de ejemplo están escritos en los ejercicios.",
    "Aprenderé a cumplir plazos con un plan que puedo ajustar. Sirve para entregar mis trabajos a tiempo sin apuro.",
    ["Sé organizar mis útiles.", "Sé contar días."],
    [
        "Un plazo es el día en que debes entregar un trabajo. Para cumplirlo, divide el trabajo en partes pequeñas y ponles un día. Por ejemplo, para hacer un afiche en 4 días: día 1, elegir el tema; día 2, escribir; día 3, dibujar; día 4, revisar. Así no queda todo para el último día.",
        "Un plan puede ajustarse. Si un día no pudiste avanzar, reorganizas las partes que quedan. Si ves que no alcanzas, avisas con tiempo a la profesora o a un adulto y pides ayuda o más tiempo. Decirlo antes es responsable, no es flojera.",
        "También puede haber cosas que no controlas, como estar enfermo o no tener materiales. Eso no es tu culpa. Lo importante es avisar y conversar un nuevo plan. Cumplir un plazo no es lo mismo que aprender, por eso también revisas si entendiste.",
    ],
    [("plazo", "día límite para entregar algo"), ("plan", "pasos ordenados para lograr algo"), ("ajustar", "cambiar un plan según lo que pasa"), ("entregar", "dar un trabajo terminado"), ("avisar", "decir a tiempo que necesito ayuda")],
    [
        W("Dividir en partes", "Hay 4 días para un afiche: elegir tema, escribir, dibujar y revisar. ¿Qué haces el día 3 si el orden es ese?", ["Día 1: elegir tema.", "Día 2: escribir.", "Día 3: dibujar."], "Dibujar"),
        W("Ajustar el plan", "Beto planeó 3 partes en 3 días, pero el día 2 estuvo enfermo. Le quedan dos partes. ¿Qué hace?", ["No pudo avanzar.", "Revisa cuántos días le quedan.", "Avisa y conversa un nuevo plan."], "Avisa y conversa un nuevo plan"),
    ],
    [
        M("Dejar todo el trabajo para el último día.", "Parece que hay mucho tiempo.", "Divide en partes y pon un día a cada una."),
        M("Callarme cuando no voy a alcanzar a terminar.", "Me da vergüenza.", "Avisar con tiempo es responsable."),
    ],
    R=[
        ex("¿Un plazo es el día límite para entregar?", "Sí", "Marca hasta cuándo debo terminar."),
        ex("¿Dividir un trabajo en partes ayuda a cumplir?", "Sí", "Cada día se avanza un poco."),
        ex("¿Un plan se puede ajustar?", "Sí", "Se cambia según lo que pasa."),
    ],
    U=[
        ex("¿Qué haces si ves que no alcanzas a terminar?", "Aviso con tiempo y pido ayuda", "Es una forma responsable."),
        ex("Si estás enfermo y no avanzas, ¿es tu culpa?", "No", "Hay cosas que no se controlan."),
        ex("¿Cumplir un plazo es lo mismo que aprender?", "No", "También hay que entender el contenido."),
    ],
    A=[
        arith("Un trabajo tiene 6 partes y hay 3 días para hacerlo, la misma cantidad cada día. ¿Cuántas partes hay por día?", "6//3", "Se reparte en partes iguales."),
        arith("Lola tenía que escribir 10 renglones. Ya escribió 6. ¿Cuántos le faltan?", "10-6", "Se resta lo hecho al total."),
        ex("Escribe una frase para avisar a la profesora que no alcanzarás a terminar.", "Profesora, necesito más tiempo para terminar; ya hice una parte", "Avisa con tiempo y dice qué hizo."),
    ],
    Z=[
        ex("Dos niños tienen 3 días. Uno hace todo el último día y el otro una parte cada día. ¿Quién tiene menos riesgo de no terminar?", "El que hace una parte cada día", "Reparte el esfuerzo."),
        ex("Una niña terminó a tiempo pero copió todo. ¿Cumplió el plazo y aprendió?", "Cumplió el plazo pero no aprendió", "No basta con entregar."),
    ],
    D=[
        arith("Un plan tiene 4 partes de 15 minutos cada una. ¿Cuántos minutos son en total?", "4*15", "Se repite 15 minutos cuatro veces."),
        ex("Si un adulto no pudo comprar los materiales a tiempo, ¿es culpa del niño?", "No", "No depende de él."),
    ],
    context=[ex("La profesora pide un cartel para el viernes. Joaquín lo divide en: lunes idea, martes borrador, miércoles dibujo, jueves revisar. ¿Planificó bien?", "Sí", "Dividió en partes y puso días.")],
    selfcheck=[ex("En Orientación: ¿puedo ajustar mi plan?", "Sí", "Los planes cambian."), ex("¿Avisar a tiempo es responsable?", "Sí", "Así otros pueden ayudar."), ex("¿Es mi culpa si me enfermé?", "No", "No depende de mí.")],
    task=T("Un trabajo vence el viernes y tienes cuatro días: lunes a jueves. Hay cuatro partes: (1) elegir el tema, (2) buscar información, (3) escribir y (4) revisar y entregar. Arma un plan con un día para cada parte. Escribe qué harías si el miércoles no pudieras avanzar.", "Lunes: tema. Martes: información. Miércoles: escribir. Jueves: revisar. Si el miércoles no puedo, aviso y paso escribir al jueves y revisar con ayuda.", ["una parte por día", "plan que se puede ajustar", "avisa a tiempo"], ["plan escrito"], ["dejarlo todo para el final", "no avisar"], "Reconoce el plan y verifica que se pueda ajustar."),
    reinforce="Divide una tarea tuya en tres partes con días.",
    extend="Escribe qué le dirías a tu profesora si necesitas más tiempo.",
)

lesson(
    OA8, 3,
    "Una hoja y un lápiz. Las situaciones de sala están escritas en los ejercicios.",
    "Aprenderé a respetar el estudio y el trabajo de mis compañeros. Sirve para que todos podamos concentrarnos.",
    ["Sé hablar bajo.", "Sé esperar mi turno."],
    [
        "Respetar el trabajo de otros es cuidar su concentración y sus cosas. Cuando alguien trabaja, hablamos bajo, no lo interrumpimos sin necesidad y no hacemos ruidos fuertes. Si necesitas algo, esperas a que termine o lo pides en voz baja.",
        "También respetamos lo que otros hicieron. No tocamos ni rayamos un cuaderno ajeno. No movemos un trabajo que está secándose. Si lo tocas por error, avisas y ayudas a arreglarlo. Pedimos permiso antes de usar un material de otra persona.",
        "Cada persona trabaja a su ritmo. Si alguien se demora, no se le apura ni se burla. Si tú necesitas silencio, puedes pedirlo con respeto. Estas reglas cuidan el ambiente de aprendizaje de todos.",
    ],
    [("concentración", "atención puesta en una tarea"), ("interrumpir", "cortar lo que alguien hace o dice"), ("permiso", "aprobación para usar algo"), ("ritmo", "velocidad con que una persona trabaja"), ("ambiente de aprendizaje", "lugar donde todos pueden estudiar")],
    [
        W("Pedir en voz baja", "Rita necesita una goma y su compañero está escribiendo. ¿Qué hace con respeto?", ["No lo interrumpe de golpe.", "Espera un momento.", "Pide la goma en voz baja."], "Esperar y pedir en voz baja"),
        W("Un trabajo ajeno", "Eli tocó sin querer el dibujo de Pablo y se arrugó. ¿Qué hace?", ["Reconoce lo que pasó.", "Avisa a Pablo.", "Le ayuda a arreglarlo."], "Avisar a Pablo y ayudar a arreglarlo"),
    ],
    [
        M("Apurar a un compañero que trabaja más lento.", "Pensamos que todos deben ir igual.", "Cada persona tiene su ritmo; ofrece ayuda."),
        M("Usar el material de otro sin preguntar.", "Parece algo pequeño.", "Pide permiso antes."),
    ],
    R=[
        ex("Cuando alguien trabaja, ¿hablas bajo?", "Sí", "Así cuidas su concentración."),
        ex("¿Se pide permiso antes de usar un material ajeno?", "Sí", "Es respetar lo de otros."),
        ex("¿Se puede rayar el cuaderno de un compañero?", "No", "Es su trabajo."),
    ],
    U=[
        ex("¿Por qué no se interrumpe a quien trabaja?", "Porque necesita concentrarse", "Interrumpir corta la tarea."),
        ex("Si dañas sin querer el trabajo de otro, ¿qué haces?", "Aviso y ayudo a arreglarlo", "Te haces cargo."),
        ex("¿Todas las personas trabajan al mismo ritmo?", "No", "Cada uno tiene su ritmo."),
    ],
    A=[
        ex("Escribe una frase para pedir silencio con respeto.", "¿Podemos hablar más bajo, por favor?", "Pide con respeto."),
        ex("Un compañero deja su cuaderno abierto. ¿Lo miras sin permiso o lo dejas?", "Lo dejo", "Es su trabajo."),
        ex("Escribe una frase para pedir un lápiz prestado.", "¿Me prestas tu lápiz, por favor?", "Pide permiso antes de usarlo."),
    ],
    Z=[
        ex("Una niña dice «yo hablo fuerte porque ya terminé». ¿Respeta a quienes aún trabajan?", "No", "Afecta la concentración."),
        ex("Dos niñas conversan bajito al lado de un compañero que no logra concentrarse. ¿Qué pueden hacer?", "Conversar en otro lugar o dejarlo para después", "Se cuida la concentración de quien trabaja."),
    ],
    D=[
        arith("En una sala de 28 niños, 20 están trabajando. ¿Cuántos no trabajan?", "28-20", "Se resta los que trabajan al total."),
        ex("Si un compañero termina antes, ¿qué puede hacer sin molestar a otros: leer o conversar fuerte?", "Leer", "No interrumpe a nadie."),
    ],
    context=[ex("Mientras el curso escribe, Tomás termina y saca un libro para leer en silencio. ¿Respetó el trabajo de los demás?", "Sí", "Cuidó la concentración de todos.")],
    selfcheck=[ex("En Orientación: ¿interrumpir cuida la concentración?", "No", "Rompe la concentración de otros."), ex("¿Hay que pedir permiso para usar lo de otros?", "Sí", "Es una forma de respeto."), ex("¿Cada uno tiene su ritmo?", "Sí", "Nadie debe apurarte.")],
    task=T("Lee tres situaciones: (1) alguien quiere conversar mientras otro escribe, (2) quieres un borrador de un compañero, (3) un compañero se demora en terminar. Para cada una escribe qué harías con respeto y una frase que dirías.", "(1) Espero y hablo después. (2) «¿Me prestas tu borrador, por favor?». (3) «¿Quieres que te ayude?» sin apurarlo.", ["tres respuestas respetuosas", "frases amables", "no se burla ni apura"], ["respuestas escritas"], ["interrumpir", "usar sin permiso"], "Reconoce las respuestas y revisa el tono."),
    reinforce="Escribe dos reglas para cuidar la concentración en tu sala.",
    extend="Explica cómo ayudarías a un compañero que se demora sin apurarlo.",
)

lesson(
    OA8, 4,
    "Una hoja y un lápiz. Los casos están escritos en los ejercicios. Usa personajes.",
    "Aprenderé a distinguir entre ayuda, copia y plagio, y a ser honesto con mi trabajo. Sirve para aprender de verdad y respetar lo que otros hicieron.",
    ["Sé que mi trabajo es mío.", "Sé pedir ayuda."],
    [
        "Pedir ayuda es válido: puedes preguntar, escuchar una explicación o revisar un ejemplo. La ayuda te deja hacer tu propio trabajo. Copiar es escribir como tuyo lo que otro hizo. Por ejemplo, cambiar solo el nombre en el trabajo de otro. Copiar no te hace aprender, porque no practicas ni piensas tú, y no es honesto.",
        "El plagio es usar las palabras, el dibujo o la idea de otra persona como si fueran tuyas. Puede pasar con un libro, un compañero o internet. Para evitarlo, escribe con tus palabras lo que entendiste, y si usas una frase de un libro, di de dónde la sacaste. Por ejemplo: «Según el libro de ciencias…».",
        "Si te equivocas, ser honesto es mejor que copiar. Un error se corrige y enseña. Y si alguien te pide que lo copies, puedes decir que no y ofrecerle explicarle cómo hacerlo.",
    ],
    [("copia", "escribir como mío lo que hizo otro"), ("plagio", "usar palabras o ideas de otros como si fueran mías"), ("autoría", "ser quien hizo un trabajo"), ("fuente", "libro o lugar de donde saqué una información"), ("honesto", "que dice y hace la verdad")],
    [
        W("Ayuda o copia", "Pía no entiende un ejercicio y su compañera le explica cómo se resuelve. Después Pía lo hace sola. ¿Es ayuda o copia?", ["La compañera explicó.", "Pía hizo su trabajo.", "Es ayuda."], "Es ayuda"),
        W("Citar la fuente", "Joaquín leyó en un libro que las abejas hacen miel. ¿Cómo evita el plagio al escribirlo?", ["Lo escribe con sus palabras.", "Dice de dónde lo sacó.", "Así reconoce la fuente."], "Lo escribe con sus palabras y dice «según el libro…»"),
    ],
    [
        M("Pasar mi trabajo para que otro lo copie «porque es mi amigo».", "Se cree que es ser buen amigo.", "Ofrece explicarle cómo hacerlo, sin darle el trabajo."),
        M("Copiar una frase de un libro sin decir de dónde viene.", "Parece algo pequeño.", "Escribe con tus palabras o di la fuente."),
    ],
    R=[
        ex("¿Pedir una explicación es ayuda?", "Sí", "Te deja hacer tu propio trabajo."),
        ex("¿Cambiar solo el nombre en el trabajo de otro es copiar?", "Sí", "No es tu trabajo."),
        ex("¿Usar las palabras de un libro como si fueran mías es plagio?", "Sí", "No reconozco a quien lo escribió."),
    ],
    U=[
        ex("¿Qué debes decir si usas una frase de un libro?", "De dónde la sacaste", "Así reconoces la fuente."),
        ex("¿Por qué copiar no ayuda a aprender?", "Porque no practico ni pienso yo", "Lo importante es hacer el trabajo y comprender."),
        ex("Si un compañero te pide copiar, ¿qué puedes responder?", "No, pero te explico cómo hacerlo", "Cuidas su aprendizaje."),
    ],
    A=[
        ex("Lee: «Los gatos duermen muchas horas al día». Escribe esa idea con tus palabras.", "Los gatos pasan gran parte del día durmiendo", "Cambia las palabras manteniendo la idea."),
        ex("Rita copió el dibujo de un compañero y puso su nombre. ¿Es plagio?", "Sí", "Usó su dibujo como propio."),
        ex("Elige la frase que cita la fuente: «Los volcanes arrojan lava» o «Según mi libro de ciencias, los volcanes arrojan lava».", "«Según mi libro de ciencias, los volcanes arrojan lava»", "Dice de dónde sacó la información."),
    ],
    Z=[
        ex("Dos niños tienen la misma nota. Uno aprendió y otro copió. ¿Tienen el mismo aprendizaje?", "No", "Quien copió no comprendió."),
        ex("Una niña dice: «Si cambio algunas palabras de un texto de internet, ya es mío». ¿Es cierto?", "No", "Si no entiendo ni nombro la fuente, es plagio."),
    ],
    D=[
        arith("En un curso de 30, 18 explicaron con sus palabras y el resto copió frases. ¿Cuántos copiaron frases?", "30-18", "Se resta lo explicado al total."),
        ex("Un compañero necesita ayuda con una tarea. ¿Qué le ofreces: tu cuaderno para copiar o explicarle un ejemplo?", "Explicarle un ejemplo", "Le ayudas a aprender sin copiar."),
    ],
    context=[ex("Para un trabajo de ciencias, Marta lee sobre las abejas, anota ideas con sus palabras y escribe al final el nombre del libro. ¿Evitó el plagio?", "Sí", "Usó sus palabras y reconoció la fuente.")],
    selfcheck=[ex("En Orientación: ¿pedir una explicación es copiar?", "No", "Es una ayuda."), ex("¿Reconocer la fuente evita el plagio?", "Sí", "Se reconoce a quien lo escribió."), ex("¿Copiar me hace aprender?", "No", "No comprendo el contenido.")],
    task=T("Lee este texto de práctica: «Las mariposas adultas tienen cuatro alas y muchas se alimentan de néctar». Escríbelo con tus palabras y agrega «según…» para mencionar la fuente (aquí, «el texto de esta clase»). Después escribe qué le dirías a un compañero que te pide copiar tu trabajo.", "«Según el texto de esta clase, las mariposas adultas tienen cuatro alas y muchas toman néctar». A mi compañero: «No te lo paso, pero te explico cómo hacerlo».", ["parafrasea con sus palabras", "menciona la fuente", "responde con respeto y sin copiar"], ["texto escrito"], ["copiar frases exactas sin fuente", "pasar el trabajo para que lo copie"], "Reconoce la parafraseo y verifica que cite la fuente."),
    reinforce="Escribe con tus palabras una idea de un libro que hayas leído y di de dónde viene.",
    extend="Explica la diferencia entre copia y plagio con un ejemplo.",
)

lesson(
    OA8, 5,
    "Una hoja y un lápiz. Los registros de ejemplo y la lista de temas están escritos en los ejercicios.",
    "Aprenderé a evaluar mi esfuerzo y mis estrategias, y a elegir un siguiente paso. También a preguntar y buscar información de un tema que me interesa. Sirve para seguir aprendiendo.",
    ["Sé que puedo mejorar con práctica.", "Sé que ser honesto ayuda a aprender."],
    [
        "El esfuerzo es poner atención y energía en lo que haces, aunque cueste. No siempre se ve en la nota. A veces te esfuerzas mucho y el resultado no es el esperado. Eso no es fracaso: significa que puedes cambiar la estrategia, que es la forma de hacer algo. Por ejemplo, repasar un poco cada día, pedir una explicación o practicar con ejemplos.",
        "Para evaluar tu esfuerzo, pregúntate: ¿qué hice?, ¿qué estrategia usé?, ¿qué me ayudó?, ¿qué cambiaré? Luego elige un siguiente paso pequeño. Por ejemplo: «Mañana repasaré las tablas 5 minutos». Esto es mejor que decir «soy malo» o «no sirvo».",
        "Aprender también es preguntar y buscar información sobre lo que te interesa. Si te interesan los delfines, puedes preguntar a una persona adulta, buscar en un libro de la biblioteca o mirar una enciclopedia. Anota una pregunta y dónde buscarías la respuesta. Escribe con tus palabras lo que descubras. También puedes hacer una actividad sobre tu interés, como dibujar un animal y anotar tres datos que descubriste.",
    ],
    [("esfuerzo", "energía y atención que pongo en algo"), ("estrategia", "forma de hacer algo para lograrlo"), ("siguiente paso", "lo próximo pequeño que haré"), ("interés", "tema que quiero conocer más"), ("fuente", "lugar de donde saco información")],
    [
        W("Cambiar de estrategia", "Rafa estudió leyendo una sola vez y no recordó. ¿Qué estrategia nueva puede probar?", ["La estrategia anterior no funcionó.", "Puede repasar cada día un poco.", "También puede practicar con ejemplos."], "Repasar un poco cada día y practicar con ejemplos"),
        W("Buscar información", "A Ema le interesan los delfines. ¿Qué puede hacer para saber más?", ["Escribe una pregunta.", "Busca en un libro o pregunta a un adulto.", "Anota lo que aprende con sus palabras."], "Escribir una pregunta y buscar en un libro o preguntar a un adulto"),
    ],
    [
        M("Pensar que si no tuve buena nota, no me esforcé.", "Se mezclan esfuerzo y resultado.", "Revisa tu estrategia y cámbiala."),
        M("Decir «soy malo» en vez de pensar un siguiente paso.", "Duele equivocarse.", "Elige un paso pequeño y vuelve a intentar."),
    ],
    R=[
        ex("¿El esfuerzo es poner atención y energía?", "Sí", "Se hace aunque cueste."),
        ex("¿Una estrategia es una forma de hacer algo?", "Sí", "Se puede cambiar."),
        ex("¿Preguntar y buscar información ayuda a aprender?", "Sí", "Permite conocer más."),
    ],
    U=[
        ex("Si te esforzaste y no resultó, ¿qué haces?", "Cambio la estrategia", "Así pruebas otra forma."),
        ex("¿Una buena evaluación dice «soy malo»?", "No", "Busca un siguiente paso."),
        ex("¿Dónde puedes buscar información sobre un tema que te interesa?", "En un libro o preguntando a un adulto", "Son fuentes posibles."),
    ],
    A=[
        arith("Si repasas 5 minutos al día durante 6 días, ¿cuántos minutos repasaste?", "5*6", "Se repite 5 minutos seis veces."),
        ex("Escribe una pregunta que te gustaría investigar sobre un animal.", "¿Qué comen los delfines?", "Es una pregunta concreta."),
        ex("Rita no entendió una suma. Escribe un siguiente paso pequeño.", "Pedir un ejemplo a mi profesora", "Es pequeño y posible."),
    ],
    Z=[
        ex("Dos niños sacaron la misma nota. Uno estudió mucho y otro poco. ¿Se esforzaron igual?", "No", "La nota no mide el esfuerzo."),
        ex("Una niña dice «no sé nada de estrellas». ¿Qué puede hacer para aprender?", "Preguntar y buscar en un libro", "Preguntar y buscar es aprender."),
    ],
    D=[
        ex("A Luisa le interesan las aves. ¿Cuál es una actividad sobre su interés: «dibujar un ave y anotar tres datos que descubrió» o «esperar a que alguien le cuente»?", "«Dibujar un ave y anotar tres datos que descubrió»", "Hace algo propio sobre lo que le interesa."),
        ex("Si cambias de estrategia tres veces hasta lograr entender, ¿hiciste mal?", "No", "Probar otras formas es parte de aprender."),
    ],
    context=[ex("A Pablo le gustan las aves. Anota: «¿Cómo vuelan los pájaros?», lo pregunta a una persona adulta y busca un libro en la biblioteca. ¿Siguió una estrategia para aprender?", "Sí", "Preguntó y buscó una fuente.")],
    selfcheck=[ex("En Orientación: ¿esfuerzo y nota son lo mismo?", "No", "Pueden ser distintos."), ex("¿Puedo cambiar de estrategia?", "Sí", "Es parte de aprender."), ex("¿Preguntar es una forma de aprender?", "Sí", "Permite conocer más.")],
    task=T("Escribe tu evaluación de esta semana con cuatro partes: algo en lo que te esforzaste, la estrategia que usaste, qué cambiarás y tu siguiente paso. Después elige un tema de esta lista que te interese (delfines, volcanes, estrellas, aves) y anota una pregunta, dónde buscarías la respuesta y una actividad que harías sobre ese tema.", "Me esforcé en leer. Estrategia: leer 10 minutos. Cambiaré: leer antes de dormir. Siguiente paso: pedir un libro. Tema: aves; pregunta: ¿cómo vuelan?; busco en la biblioteca; actividad: dibujar un ave y anotar tres datos.", ["cuatro partes de evaluación", "una pregunta y una fuente", "no usa «soy malo»"], ["evaluación escrita"], ["juzgarse con una etiqueta", "pregunta sin fuente"], "Reconoce la estrategia y verifica que haya un siguiente paso."),
    reinforce="Escribe una estrategia nueva que probarás esta semana.",
    extend="Elige un tema de tu interés y escribe tres preguntas y dónde buscarlas.",
)
