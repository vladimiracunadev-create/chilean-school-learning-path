"""Cuaderno del estudiante, 4.º básico Orientación: OA 07 (resolución guiada de conflictos) y OA 08 (participación y responsabilidades en el curso)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA7, OA8 = "OR04 OA 07", "OR04 OA 08"


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
    "Una hoja y un lápiz. Los conflictos con personajes están escritos en los ejercicios. Nadie cuenta un conflicto propio.",
    "Aprenderé a reconstruir qué pasó en un conflicto y a ver las dos perspectivas. Sirve para entender antes de buscar una solución.",
    ["Sé escuchar y reformular.", "Sé distinguir una emoción de lo que hago."],
    [
        "Un conflicto es cuando dos o más personas quieren cosas distintas o piensan distinto, y eso les genera un problema. Puede pasar entre amigos y no significa que alguien sea malo. Un conflicto no es lo mismo que la violencia: en la violencia alguien daña o asusta. Si hay golpes o amenazas, se avisa a un adulto.",
        "Para entender un conflicto, separa cuatro cosas. Los hechos: lo que pasó y se pudo ver o escuchar. Las interpretaciones: lo que cada uno cree que pasó o por qué. Las emociones: lo que sintió cada uno. Y las necesidades: lo que cada uno quería o necesitaba. Por ejemplo, «Tomás tomó la pelota» es un hecho. «Lo hizo para molestarme» es una interpretación. Cuidado con «siempre» y «nunca»: casi nunca son hechos, sino exageraciones.",
        "Cada persona tiene una perspectiva, es decir, su manera de ver lo que pasó. Las dos pueden ser parciales. Buscar un culpable antes de comprender suele empeorar las cosas. Primero escucha a cada uno, luego reconstruye los hechos, y después piensa en cómo resolver el problema.",
    ],
    [("conflicto", "problema entre personas que quieren cosas distintas"), ("hecho", "lo que pasó y se puede ver o escuchar"), ("interpretación", "lo que creo sobre por qué pasó algo"), ("necesidad", "lo que una persona quería o necesitaba"), ("perspectiva", "la manera en que una persona ve una situación")],
    [
        W("Hecho o interpretación", "Dino dice: «Ana tomó mi lápiz para molestarme». ¿Qué parte es un hecho y cuál es interpretación?", ["«Ana tomó mi lápiz» se pudo ver.", "«Para molestarme» es lo que Dino cree.", "Se separan los dos."], "Hecho: Ana tomó su lápiz; interpretación: para molestarlo"),
        W("Dos perspectivas", "Ema y Rita quieren usar el mismo balón en el recreo. Ema dice que lo pidió primero. Rita dice que lo vio primero. ¿Qué necesidades hay?", ["Ema quiere jugar con el balón.", "Rita también quiere jugar con el balón.", "Ambas necesitan jugar."], "Las dos necesitan jugar con el balón"),
    ],
    [
        M("Buscar quién tiene la culpa antes de escuchar a todos.", "Se piensa que primero hay que castigar.", "Escucha a cada uno y reconstruye los hechos."),
        M("Creer que un conflicto significa que somos enemigos.", "Se confunde conflicto con maldad.", "Un conflicto es un problema que se puede resolver."),
    ],
    R=[
        ex("Un conflicto, ¿es un problema entre personas que quieren cosas distintas?", "Sí", "Así se define."),
        ex("«Tomás tomó la pelota». ¿Es un hecho o una interpretación?", "Un hecho", "Se pudo ver."),
        ex("«Lo hizo para molestarme». ¿Es un hecho o una interpretación?", "Una interpretación", "Es lo que cree quien habla."),
    ],
    U=[
        ex("¿Por qué conviene escuchar a todos antes de buscar un culpable?", "Porque cada uno tiene una perspectiva y falta información", "Así se entiende mejor el conflicto."),
        ex("Si hay golpes o amenazas en un conflicto, ¿qué haces?", "Aviso a un adulto", "Ya no es solo un desacuerdo."),
        ex("¿Tener un conflicto significa ser una mala persona?", "No", "Es un problema que se puede resolver."),
    ],
    A=[
        ex("Pía dice: «Luis rompió mi trabajo porque me odia». Separa un hecho y una interpretación.", "Hecho: Luis rompió su trabajo; interpretación: porque la odia", "El hecho se vio; la razón es lo que cree."),
        ex("Pedro quería usar el computador para terminar una tarea y Eli para jugar. ¿Qué necesita cada uno?", "Pedro necesita terminar la tarea y Eli quiere jugar", "Cada necesidad es distinta."),
        ex("En un conflicto, ¿qué va primero: reconstruir lo que pasó o decidir el castigo?", "Reconstruir lo que pasó", "Primero se comprende."),
    ],
    Z=[
        ex("Dos niños cuentan versiones distintas de lo que pasó. ¿Qué conviene hacer: elegir a uno o reconstruir los hechos que ambos aceptan?", "Reconstruir los hechos que ambos aceptan", "Así se parte de lo común."),
        ex("Un niño dice «él siempre me molesta». ¿Es un hecho concreto o una exageración con «siempre»?", "Una exageración con «siempre»", "«Siempre» no cuenta qué pasó ni cuándo; no es un hecho concreto."),
    ],
    D=[
        arith("Una actividad tiene 6 conflictos de ejemplo. En cada uno se identifican 4 cosas: hechos, interpretaciones, emociones y necesidades. ¿Cuántas cosas se identifican en total?", "6*4", "Son 4 cosas repetidas 6 veces."),
        ex("Frases: A) «Tomó mi libro». B) «Seguro lo hizo a propósito». C) «Me sentí enojada». D) «Yo quería terminar mi lectura». ¿Cuál es un hecho?", "A", "Es lo que se vio: tomó el libro."),
    ],
    context=[ex("En el recreo, dos niños discuten por un asiento. La profesora pregunta a cada uno qué pasó y qué quería, sin decir quién está equivocado. ¿Está reconstruyendo hechos y perspectivas?", "Sí", "Escucha a ambos antes de decidir.")],
    selfcheck=[ex("En Orientación: ¿un conflicto es lo mismo que la violencia?", "No", "En la violencia hay daño o miedo."), ex("¿Se separan hechos de interpretaciones?", "Sí", "Así se entiende mejor."), ex("¿Se busca un culpable primero?", "No", "Primero se escucha a todos.")],
    task=T("Lee: Marta y Pablo quieren usar el único pegamento del grupo a la vez. Marta dice «lo tomé yo primero» y Pablo dice «yo lo necesito para terminar». Escribe un hecho, una interpretación posible, una emoción posible y una necesidad de cada uno. No busques un culpable.", "Hecho: los dos quieren el pegamento. Interpretación: «él quiere molestarme». Emoción: molestia. Necesidades: Marta, usarlo ya; Pablo, terminar su trabajo.", ["separa hechos, interpretaciones, emociones y necesidades", "las necesidades de ambos están claras", "no busca culpable"], ["texto escrito o dicho"], ["mezclar hechos con interpretaciones", "buscar un culpable"], "Reconoce cada parte y pregunta qué falta saber para entender mejor."),
    reinforce="Escribe un conflicto inventado y separa un hecho, una emoción y una necesidad.",
    extend="Escribe cómo contarías un conflicto usando solo hechos, sin acusar.",
)

lesson(
    OA7, 2,
    "Una hoja y un lápiz. Los diálogos están escritos en los ejercicios.",
    "Aprenderé a escuchar, a reformular y a describir los sentimientos del otro para entender sus necesidades. Sirve para resolver un conflicto sin pelear.",
    ["Sé reconstruir hechos y perspectivas.", "Sé que no sé con certeza lo que siente otro."],
    [
        "Para resolver un conflicto, cada uno necesita ser escuchado. Hay reglas simples: hablar por turnos, no interrumpir, mirar a quien habla y no insultar. Primero habla uno y el otro escucha, luego cambian. Si no se puede hablar con calma, se hace una pausa o se pide ayuda a un adulto.",
        "Después de escuchar, reformulas: dices con tus palabras lo que entendiste. Por ejemplo: «Entiendo que quieres usar el balón porque llevas rato esperando». También puedes describir con cautela cómo se pudo sentir el otro: «Parece que te molestó, ¿es así?». No afirmas lo que siente: lo preguntas.",
        "Detrás de cada conflicto hay necesidades: jugar, ser respetado, descansar, terminar una tarea o ser tomado en cuenta. Cuando entiendes la necesidad del otro, es más fácil encontrar una solución. Escuchar no es darle la razón. Es comprender qué necesita para buscar un acuerdo.",
    ],
    [("turno", "momento que me toca hablar"), ("reformular", "decir con mis palabras lo que entendí"), ("necesidad", "lo que una persona quería o necesitaba"), ("cautela", "cuidado para no afirmar lo que no sé"), ("escuchar", "prestar atención para entender a otro")],
    [
        W("Reformular", "Lola dice: «Estuve esperando el balón todo el recreo y nadie me lo pasó». ¿Qué frase reformula: «Entiendo que esperaste todo el recreo y no te lo pasaron» o «Eso no es tan grave»?", ["Reformular repite lo entendido.", "La segunda frase le quita importancia.", "Elige la primera."], "«Entiendo que esperaste todo el recreo y no te lo pasaron»"),
        W("Necesidad detrás del reclamo", "Tomás grita «¡No me dejan jugar!». ¿Qué necesidad hay detrás: jugar con los demás o ganar un premio?", ["Dice que no lo dejan jugar.", "Quiere participar.", "Su necesidad es jugar con los demás."], "Jugar con los demás"),
    ],
    [
        M("Interrumpir para explicar mi versión.", "Se piensa que si no hablo ya, perderé.", "Espera tu turno; tendrás tiempo."),
        M("Decir «tú estás enojado» como si lo supiera.", "Se afirma lo que siente el otro.", "Pregunta: «Parece que te molestó, ¿es así?»"),
    ],
    R=[
        ex("Para escuchar bien, ¿se habla por turnos o todos a la vez?", "Por turnos", "Así se escucha a todos."),
        ex("Reformular, ¿es decir con mis palabras lo que entendí?", "Sí", "Muestra que escuché."),
        ex("¿Escuchar es darle la razón al otro?", "No", "Es comprender lo que necesita."),
    ],
    U=[
        ex("¿Por qué se pregunta «¿es así?» en vez de afirmar lo que siente el otro?", "Porque no sabes con certeza lo que siente", "Se usa cautela."),
        ex("Si no se puede hablar con calma, ¿qué se hace?", "Una pausa o pedir ayuda a un adulto", "Así se evita pelear."),
        ex("¿Qué cosas hay detrás de un conflicto: necesidades o solo enojos?", "Necesidades", "Cada uno quiere o necesita algo."),
    ],
    A=[
        ex("Dino dice: «Me da rabia que me quiten el turno». ¿Qué frase reformula lo que dijo: «Entiendo que te da rabia que te quiten el turno» o «Sí, pero tú también lo quitaste»?", "«Entiendo que te da rabia que te quiten el turno»", "Repite lo entendido; la otra frase lo acusa."),
        ex("Eli cruza los brazos y no habla en medio del conflicto. ¿Qué frase usa cautela: «Parece que algo te molestó, ¿es así?» o «Estás enojada, no lo niegues»?", "«Parece que algo te molestó, ¿es así?»", "Describe y pregunta."),
        ex("Pedro dice: «No me dejan terminar mi trabajo porque hacen ruido». ¿Qué necesidad tiene: silencio para terminar o ganar el juego?", "Silencio para terminar", "Quiere poder concentrarse mejor."),
    ],
    Z=[
        ex("Dos niños hablan al mismo tiempo y se gritan. ¿Qué regla falta?", "Hablar por turnos", "Sin turnos no se escucha."),
        ex("Un niño dijo: «Quiero terminar mi trabajo en silencio». Otro lo reformula: «Entonces quieres que me calle para siempre». ¿Reformuló bien?", "No", "Cambió lo que dijo el otro."),
    ],
    D=[
        arith("En un taller de escucha hay 4 parejas. En cada pareja, cada persona habla 3 minutos. ¿Cuántos minutos de habla hay en total?", "4*2*3", "Cada pareja tiene dos personas que hablan 3 minutos."),
        ex("Tres frases: A) «Entiendo que quieres jugar». B) «Siempre te quejas». C) «Parece que te sentiste excluido, ¿es así?». ¿Cuáles escuchan y reformulan?", "A y C", "La B acusa."),
    ],
    context=[ex("Dos amigas discuten por un lápiz. Una dice «Primero habla tú y yo escucho, luego hablo yo». Después reformula lo que escuchó. ¿Aplicó la escucha para resolver el conflicto?", "Sí", "Usó turnos y reformuló.")],
    selfcheck=[ex("En Orientación: ¿se pueden describir los sentimientos del otro con cautela?", "Sí", "Preguntando y no afirmando."), ex("¿Interrumpir ayuda a resolver un conflicto?", "No", "Impide escuchar al otro."), ex("¿Reformular muestra que escuchaste?", "Sí", "Dice lo que entendiste.")],
    task=T("Lee: Ana y Nico discuten porque ambos quieren el computador de la sala para hacer su trabajo. Ana dice «llevo media hora esperando» y Nico dice «me queda poco para terminar». Escribe cómo reformularías lo que dijo cada uno, cómo describirías con cautela cómo se sienten y qué necesidad tiene cada uno.", "Ana: Entiendo que llevas media hora esperando. Nico: Entiendo que te falta poco. Parece que ambos se sienten apurados, ¿es así? Necesidades: Ana usar el computador, Nico terminar su trabajo.", ["reformula a los dos", "describe con cautela cómo se sienten", "nombra una necesidad de cada uno"], ["texto escrito o dicho"], ["afirmar lo que siente el otro", "dar la razón a uno"], "Reconoce la reformulación y revisa que no tome partido."),
    reinforce="Escribe tres frases que reformulen lo que dijo otra persona.",
    extend="Escribe un guion corto de cómo se turnarían dos personas para hablar en un conflicto.",
)

lesson(
    OA7, 3,
    "Una hoja y un lápiz. Los casos con personajes están escritos en los ejercicios.",
    "Aprenderé a proponer varias opciones de solución que respeten los derechos de las dos partes. Sirve para encontrar acuerdos justos.",
    ["Sé escuchar y reformular.", "Sé reconocer las necesidades de cada uno."],
    [
        "Cuando ya entendiste qué pasó y qué necesita cada uno, puedes buscar opciones. Una opción es una posible solución. Conviene proponer varias antes de elegir. Algunas opciones son turnos, sortear con un método justo, compartir, hacer algo juntos, esperar un tiempo o pedir ayuda a un adulto.",
        "No todas las opciones sirven. Una buena opción cumple cuatro criterios: es segura, es justa para las dos partes, respeta los derechos de todos y se puede cumplir. Quitar algo a la fuerza, amenazar, excluir o burlarse no son opciones: violan los derechos de la otra persona. Una opción también debe respetar lo que cada uno necesita.",
        "Para elegir, mira qué necesidad cubre cada opción. Una buena opción cubre al menos algo importante de cada parte. Por ejemplo, si dos niños quieren el mismo balón, jugar por turnos de 5 minutos cubre la necesidad de ambos. Si ninguna opción cubre a ambos, se puede pedir ayuda a un adulto.",
    ],
    [("opción", "posible solución a un problema"), ("criterio", "regla para decidir si algo sirve"), ("derecho", "algo que toda persona merece"), ("justo", "que no favorece a uno y deja mal al otro"), ("turno", "momento que le toca a cada uno")],
    [
        W("Opciones para un conflicto", "Dos niños quieren el mismo balón. Escribe tres opciones.", ["Una opción: turnos de 5 minutos.", "Otra: jugar juntos en un equipo.", "Otra: pedir otro balón o esperar."], "Turnos, jugar juntos, esperar o pedir otro balón"),
        W("Elegir con criterios", "¿Cuál opción es válida: «el más fuerte se queda con el balón» o «turnos de 5 minutos»?", ["La primera no es justa y puede dañar.", "La segunda es justa y posible.", "Elige la segunda."], "«Turnos de 5 minutos»"),
    ],
    [
        M("Proponer una opción que deja mal a uno de los dos.", "Se piensa solo en lo que yo quiero.", "Revisa que cubra algo importante de las dos partes."),
        M("Elegir lo que primero se me ocurre.", "Se cree que la primera idea es la mejor.", "Propón varias opciones y compáralas con los criterios."),
    ],
    R=[
        ex("Una opción, ¿es una posible solución?", "Sí", "Así se define."),
        ex("Quitar algo a la fuerza, ¿es una opción válida?", "No", "Viola los derechos del otro."),
        ex("Turnos de 5 minutos, ¿es una opción justa?", "Sí", "Ambos tienen la misma oportunidad."),
    ],
    U=[
        ex("¿Cuál NO es un criterio de una buena opción: que sea justa o que gane el más fuerte?", "Que gane el más fuerte", "Una buena opción debe ser justa y respetar derechos."),
        ex("¿Una amenaza es una opción para resolver un conflicto?", "No", "Asusta y daña."),
        ex("Si ninguna opción sirve a ambos, ¿qué puedes hacer?", "Pedir ayuda a un adulto", "Un adulto puede ayudar a buscar un acuerdo."),
    ],
    A=[
        ex("Dos niños quieren usar la cancha a la vez. ¿Qué opción es justa: «usarla por turnos» o «que la use el que llegó más grande»?", "Usarla por turnos", "Cubre a los dos."),
        ex("Eli y Pedro quieren el mismo libro de la biblioteca. Elige la opción justa: «sortear con una moneda» o «el que lo toma primero se lo queda aunque el otro lo pidió antes».", "Sortear con una moneda", "Es un método justo para ambos."),
        ex("Marta quiere silencio para estudiar y Tomás quiere conversar. ¿Qué opción cubre a ambos: conversar afuera un rato o hablar fuerte?", "Conversar afuera un rato", "Marta tiene silencio y Tomás conversa."),
    ],
    Z=[
        ex("Un niño dice: «La solución es que él se vaya del juego». ¿Respeta los derechos del otro?", "No", "Lo deja afuera injustamente."),
        ex("Un grupo propone dos opciones y una deja mal a un compañero. ¿Qué hacen con la que lo deja mal?", "La descartan", "No cumple el criterio de justicia."),
    ],
    D=[
        arith("En 5 minutos por turno, dos niños juegan con un balón. Si el recreo dura 20 minutos, ¿cuántos turnos de 5 minutos caben?", "20//5", "Se reparten 20 minutos en turnos de 5."),
        ex("Opciones: A) turnos, B) gritar más fuerte, C) sortear, D) amenazar. ¿Cuántas son válidas?", "2", "Turnos y sortear respetan a ambos."),
    ],
    context=[ex("Dos niñas quieren sentarse junto a la ventana. Proponen alternar cada semana. ¿Es una opción justa?", "Sí", "Ambas tendrán el lugar un tiempo.")],
    selfcheck=[ex("En Orientación: ¿conviene proponer varias opciones?", "Sí", "Así se elige mejor."), ex("¿Amenazar es una opción válida?", "No", "Daña a la otra persona."), ex("¿Una buena opción respeta los derechos de ambos?", "Sí", "Es parte de ser justa.")],
    task=T("Lee: Ema y Lola quieren usar el mismo rincón de lectura en el recreo. Escribe tres opciones, di cuál cubre mejor lo que necesitan ambas con los cuatro criterios (segura, justa, respeta derechos, se puede cumplir) y por qué descartarías una opción que quite el lugar a una de ellas.", "Opciones: turnos, leer juntas, alternar días. Mejor: alternar días porque es justa y se puede cumplir. Descartar quitar el lugar por la fuerza porque viola derechos.", ["escribe tres opciones", "elige con los cuatro criterios", "descarta una opción injusta"], ["texto escrito o dicho"], ["elegir la primera idea", "aceptar una opción injusta"], "Reconoce los criterios y revisa que la opción cubra a ambas."),
    reinforce="Inventa un conflicto y escribe tres opciones de solución.",
    extend="Evalúa tus tres opciones con los cuatro criterios y descarta una.",
)

lesson(
    OA7, 4,
    "Una hoja y un lápiz. Los acuerdos de ejemplo están escritos en los ejercicios.",
    "Aprenderé a hacer un acuerdo claro, a reparar y a saber cuándo pedir ayuda a un adulto. Sirve para cerrar un conflicto de forma justa y segura.",
    ["Sé proponer opciones justas.", "Sé que algunas situaciones requieren un adulto."],
    [
        "Un acuerdo es una decisión que aceptan las dos partes. Para ser bueno, debe ser claro: quién hace qué, cuándo y cómo se revisará. Por ejemplo: «Usaremos el balón por turnos de 5 minutos, empieza Ema hoy y mañana Rita». También debe ser voluntario: nadie lo acepta por miedo o presión, y cubre algo importante de ambos.",
        "Después del acuerdo se puede reparar si hubo daño: reconocer lo que pasó, decir lo siento y hacer algo concreto. Pasados unos días, se revisa si el acuerdo funciona. Si no, se ajusta. No se obliga a nadie a ser amigo ni a contar cosas privadas para llegar a un acuerdo.",
        "A veces se necesita un adulto, o un compañero que ayude a mediar. Eso se llama mediación: una persona que no toma partido ayuda a que ambos hablen. Pide ayuda si hay golpes, amenazas o miedo, si uno de los dos no se atreve a hablar, si el conflicto se repite o si no logran un acuerdo. Pedir ayuda no es fracasar.",
    ],
    [("acuerdo", "decisión que aceptan las dos partes"), ("mediación", "ayuda de una persona que no toma partido para que ambos hablen"), ("voluntario", "que se acepta libremente, sin presión"), ("revisar", "mirar después si algo funciona"), ("reparar", "hacerse cargo de un daño y arreglarlo")],
    [
        W("Un acuerdo claro", "¿Cuál es un acuerdo claro: «Seamos buenos» o «Usaremos el balón por turnos de 5 minutos, hoy empieza Ema y mañana Rita»?", ["Un acuerdo dice quién, qué y cuándo.", "El segundo lo dice.", "Elige el segundo."], "«Usaremos el balón por turnos de 5 minutos, hoy empieza Ema y mañana Rita»"),
        W("Cuándo pedir ayuda", "Dino amenaza a Pablo para que acepte un acuerdo. ¿Qué haces?", ["Hay una amenaza.", "El acuerdo no sería voluntario.", "Avisas a un adulto."], "Avisar a un adulto"),
    ],
    [
        M("Aceptar un acuerdo por miedo.", "Se piensa que así termina el problema.", "Un acuerdo debe ser voluntario; si hay miedo, pide ayuda."),
        M("Obligar a los dos a ser amigos.", "Se confunde acuerdo con amistad.", "Basta con un acuerdo respetuoso."),
    ],
    R=[
        ex("Un acuerdo, ¿lo aceptan las dos partes?", "Sí", "Así se define."),
        ex("¿Un acuerdo debe ser voluntario?", "Sí", "Nadie debe aceptarlo por miedo."),
        ex("¿Pedir ayuda a un adulto es fracasar?", "No", "Es una buena decisión."),
    ],
    U=[
        ex("¿Qué debe decir un acuerdo claro?", "Quién hace qué y cuándo", "Así se puede cumplir."),
        ex("Si hay amenazas, ¿qué haces?", "Aviso a un adulto", "No se resuelve a solas."),
        ex("¿Hay que obligar a contar cosas privadas para llegar a un acuerdo?", "No", "El acuerdo no exige exponer a nadie."),
    ],
    A=[
        ex("Dos niñas quieren el mismo rincón. ¿Qué acuerdo es claro: «Ema usa el rincón los lunes y miércoles, y Lola los martes y jueves» o «Lo usaremos cuando se pueda»?", "«Ema usa el rincón los lunes y miércoles, y Lola los martes y jueves»", "Dice quién, qué y cuándo."),
        arith("Un acuerdo es usar el balón por turnos de 5 minutos. Si hay 4 turnos, ¿cuántos minutos juegan en total?", "5*4", "Son 4 turnos de 5 minutos."),
        ex("Un acuerdo no funcionó en una semana. ¿Qué se hace: ajustarlo o culpar al otro?", "Ajustarlo", "Se revisa y se mejora."),
    ],
    Z=[
        ex("Un niño acepta un acuerdo porque tiene miedo de un compañero. ¿Es un buen acuerdo?", "No", "No es voluntario."),
        ex("Dos niños no logran ponerse de acuerdo tras varios intentos. ¿Qué hacen?", "Piden ayuda a un adulto", "Un adulto ayuda a mediar."),
    ],
    D=[
        arith("Un acuerdo se revisa cada 3 días durante 2 semanas, es decir, 14 días. ¿Cuántas revisiones caben?", "14//3", "Se reparten 14 días en grupos de 3 y sobran 2."),
        ex("Tres frases: A) «Lo hacemos así, porque lo digo yo». B) «Aceptamos probar una semana y revisamos». C) «Si no aceptas, te dejo solo». ¿Cuál es un buen acuerdo?", "B", "Es voluntario, claro y revisable."),
    ],
    context=[ex("Dos amigos discuten por un juego. Acuerdan alternarlo cada día. Si hay problemas, hablarán con la profesora. ¿Es un acuerdo claro y seguro?", "Sí", "Dice qué hacer, cuándo y a quién acudir.")],
    selfcheck=[ex("En Orientación: ¿un acuerdo puede ser por miedo?", "No", "Debe ser voluntario."), ex("¿Se puede pedir ayuda a un mediador?", "Sí", "Ayuda a que hablen."), ex("¿Se revisa si el acuerdo funciona?", "Sí", "Así se ajusta.")],
    task=T("Lee: Ana y Luis discuten porque ambos quieren ser el primero en usar la pizarra para exponer. Escribe un acuerdo claro (quién, qué y cuándo), cómo lo revisarían y en qué dos casos pedirían ayuda a un adulto. Si hay un daño, agrega un paso de reparación.", "Acuerdo: Ana expone primero hoy y Luis mañana. Revisión: el viernes. Pedirían ayuda si hay amenazas o si no se ponen de acuerdo.", ["acuerdo con quién, qué y cuándo", "dice cómo lo revisan", "nombra dos casos para pedir ayuda"], ["texto escrito o dicho"], ["acuerdo vago", "aceptar por miedo"], "Reconoce la claridad del acuerdo y revisa que sea voluntario."),
    reinforce="Escribe un acuerdo claro entre dos personajes que quieren el mismo material.",
    extend="Haz una lista de tres situaciones en que pedirías ayuda a un adulto en un conflicto.",
)

# ================================================================ OA 08
lesson(
    OA8, 1,
    "Una hoja y un lápiz. Las propuestas están escritas en los ejercicios.",
    "Aprenderé a proponer una iniciativa y a recibir las iniciativas de otros. Sirve para participar en el curso sin querer mandar.",
    ["Sé proponer una idea en el curso.", "Sé cumplir un rol breve."],
    [
        "Participar es tomar parte en lo que pasa en el curso: dar ideas, escuchar a otros, ayudar y cumplir tareas. Participar no es lo mismo que dirigir. Dirigir es decidir por todos. Participar es aportar y aceptar que los demás también aportan. Una iniciativa es una propuesta para mejorar algo, como cuidar el patio o armar un diario mural.",
        "Una buena iniciativa dice qué se propone, para qué sirve, cómo se haría y quién podría ayudar. Por ejemplo: «Propongo un diario mural para mostrar los trabajos. Sirve para que todos los vean. Lo haríamos cada viernes con ayuda de dos voluntarios». Una propuesta también debe respetar a los demás y la seguridad.",
        "Recibir una iniciativa es escucharla sin burlarse, preguntar lo que no entiendes y decir tu opinión con respeto. Si tu propuesta no se elige, no es un fracaso: puedes mejorarla o apoyar otra. Participar también implica cumplir lo que prometes.",
    ],
    [("iniciativa", "propuesta para mejorar algo"), ("participar", "tomar parte aportando y escuchando"), ("dirigir", "decidir por todos"), ("propuesta", "idea que se presenta al grupo"), ("voluntario", "que ofrece ayuda por decisión propia")],
    [
        W("Armar una iniciativa", "Escribe la iniciativa de Mía: quiere un diario mural. Dice qué, para qué, cómo y quién.", ["Qué: un diario mural.", "Para qué: mostrar los trabajos.", "Cómo y quién: cada viernes, con dos voluntarios."], "Propongo un diario mural para mostrar los trabajos, cada viernes, con dos voluntarios"),
        W("Participar y no dirigir", "Pedro dice: «Mi idea es la mejor, así se hace y punto». ¿Participa o dirige?", ["No escucha otras ideas.", "Decide por todos.", "Dirige."], "Dirige"),
    ],
    [
        M("Pensar que participar es decidir por todos.", "Se confunde participar con dirigir.", "Aporta y escucha; las decisiones se toman entre todos."),
        M("Enojarme si mi propuesta no se elige.", "Se cree que no elegirla es rechazarme.", "Puedes mejorarla o apoyar otra."),
    ],
    R=[
        ex("Una iniciativa, ¿es una propuesta para mejorar algo?", "Sí", "Así se define."),
        ex("Participar, ¿es decidir por todos?", "No", "Eso es dirigir."),
        ex("¿Se escucha una propuesta sin burlarse?", "Sí", "Eso es respeto."),
    ],
    U=[
        ex("¿Qué dice una buena iniciativa?", "Qué, para qué, cómo y quién", "Eso permite entenderla."),
        ex("Si tu propuesta no se elige, ¿qué puedes hacer?", "Mejorarla o apoyar otra", "Es parte de participar."),
        ex("¿Una buena propuesta puede poner en riesgo la seguridad de alguien?", "No", "Debe respetar la seguridad."),
    ],
    A=[
        ex("Ana propone: «Cuidar el patio». ¿Qué versión dice qué, para qué, cómo y quién: «Recoger papeles cada viernes con dos voluntarios para mantener limpio el patio» o «Que alguien cuide el patio»?", "«Recoger papeles cada viernes con dos voluntarios para mantener limpio el patio»", "Dice la acción, el sentido, el cómo y quién."),
        ex("Un compañero presenta una iniciativa y no te gusta. ¿Qué dices con respeto: «No sirve» o «Me preocupa el tiempo, ¿cómo lo harías?»", "«Me preocupa el tiempo, ¿cómo lo harías?»", "Pregunta y opina con respeto."),
        ex("Lola propone una actividad en el patio que obliga a subir a un muro alto. ¿Cumple el criterio de seguridad?", "No", "Pone en riesgo a los demás."),
    ],
    Z=[
        ex("Un niño dice: «Si no se elige mi idea, no participo más». ¿Es lo mejor?", "No", "Puede mejorar su idea o apoyar otra."),
        ex("En un curso de 30, solo 4 niños deciden y proponen todo, y los demás no pueden opinar. ¿Participa todo el curso?", "No", "Participar es aportar entre todos; aquí los demás quedan fuera."),
    ],
    D=[
        arith("En una votación sobre iniciativas se presentaron 3 propuestas con 2 ideas de apoyo cada una. ¿Cuántas ideas de apoyo hay en total?", "3*2", "Son 2 ideas repetidas 3 veces."),
        ex("Frases: A) «Propongo y escucho». B) «Mando y punto». C) «Si no me eligen, me enojo». ¿Cuál es participar?", "A", "Aporta y escucha."),
    ],
    context=[ex("En el curso, Tomás propone una caja de ideas. Rita pregunta cómo la usarían y Eli sugiere cambiarla de lugar. Tomás agradece. ¿Recibió bien las iniciativas de los demás?", "Sí", "Escuchó y agradeció sugerencias.")],
    selfcheck=[ex("En Orientación: ¿participar es lo mismo que dirigir?", "No", "Es aportar y escuchar."), ex("¿Una iniciativa dice qué, para qué, cómo y quién?", "Sí", "Así se entiende."), ex("¿Se puede mejorar una propuesta rechazada?", "Sí", "Es parte de aprender.")],
    task=T("Elige un problema del curso (por ejemplo, ruido en la fila, útiles perdidos, falta de ideas para el recreo). Escribe tu iniciativa con qué, para qué, cómo y quién. Después escribe qué dirías si otro compañero te sugiere un cambio.", "Iniciativa: una caja de objetos perdidos, para encontrar útiles, que revisamos los viernes con dos voluntarios. Si me sugieren un cambio: «Gracias, lo pensaré».", ["escribe qué, para qué, cómo y quién", "respeta seguridad y a los demás", "recibe una sugerencia con respeto"], ["texto escrito o dicho"], ["decidir por todos", "no considerar a los demás"], "Reconoce la iniciativa y revisa que acepte sugerencias."),
    reinforce="Escribe una iniciativa de cuatro partes para mejorar la sala.",
    extend="Elige la iniciativa de un compañero y escribe una pregunta que ayude a mejorarla.",
)

lesson(
    OA8, 2,
    "Una hoja y un lápiz. Los resultados de las votaciones están escritos en los ejercicios.",
    "Aprenderé a tomar decisiones del curso con reglas claras y democráticas. Sirve para que todos sean escuchados y se respeten los acuerdos.",
    ["Sé proponer iniciativas.", "Sé escuchar y esperar mi turno."],
    [
        "Una decisión democrática es la que toman las personas del grupo con reglas claras. Primero se dialoga: cada uno da su opinión por turnos y se escucha con respeto. Luego se decide. Hay dos formas: el consenso, cuando todos aceptan, y la votación, cuando se cuentan los votos y gana la opción con más votos, es decir, la mayoría.",
        "Las reglas deben ser claras antes de decidir: cada persona tiene un voto, se respeta el turno de hablar, se define cuánto dura la discusión y se acepta el resultado aunque no sea el que yo quería. Se cuenta con cuidado: la opción que obtiene más votos gana. Si hay empate, se aplica una regla acordada antes, como una segunda votación o un sorteo.",
        "Decidir de esta forma protege los derechos de todos. Nadie manda solo y nadie queda fuera. La minoría, es decir, quienes votaron por otra opción, también debe ser respetada. Se pueden revisar los acuerdos más adelante si el curso lo decide.",
    ],
    [("democrático", "que se decide entre todos con reglas claras"), ("consenso", "decisión que todos aceptan"), ("votación", "forma de decidir contando votos"), ("mayoría", "la opción con más votos"), ("empate", "cuando dos opciones tienen los mismos votos")],
    [
        W("Contar votos", "En una votación, la opción A tuvo 14 votos y la B tuvo 11. ¿Cuál gana y por cuántos votos?", ["14 es mayor que 11.", "Gana la A.", "La diferencia es 14 menos 11."], "Gana la A por 3 votos"),
        W("Empate", "En otra votación, ambas opciones tuvieron 12 votos. ¿Qué se hace?", ["Hay empate.", "Se usa una regla acordada antes.", "Por ejemplo, una segunda votación."], "Aplicar la regla acordada antes, como una segunda votación"),
    ],
    [
        M("Pensar que la mayoría tiene derecho a ignorar a la minoría.", "Se cree que ganar es mandar.", "La minoría también merece respeto."),
        M("Cambiar las reglas después de votar.", "No me gustó el resultado.", "Las reglas se acuerdan antes y se aceptan."),
    ],
    R=[
        ex("Una votación, ¿se decide contando votos?", "Sí", "Gana la opción con más votos."),
        ex("En una votación, ¿cada persona tiene un voto?", "Sí", "Es una regla básica."),
        ex("La mayoría, ¿es la opción con más votos?", "Sí", "Así se define."),
    ],
    U=[
        ex("¿Por qué las reglas deben ser claras antes de votar?", "Para que todos sepan cómo se decide", "Evita discusiones después."),
        ex("Si hay empate, ¿qué se hace?", "Se aplica la regla acordada antes", "Por ejemplo, otra votación."),
        ex("¿La minoría debe ser respetada?", "Sí", "También tiene derechos."),
    ],
    A=[
        arith("En una votación hubo 13 votos para jugar fútbol y 9 votos para jugar a la pinta. ¿Cuántos estudiantes votaron en total?", "13+9", "Se suman los votos de ambas opciones."),
        arith("En una votación hubo 16 votos para A y 10 votos para B. ¿Por cuántos votos ganó A?", "16-10", "La diferencia entre los votos."),
        ex("Un curso vota entre tres juegos: la pinta tuvo 10 votos, el fútbol 10 votos y el baile 6 votos. ¿Entre cuáles hay empate?", "Entre la pinta y el fútbol", "Tienen los mismos votos y son los más votados."),
    ],
    Z=[
        ex("Un niño dice: «Perdimos la votación, así que no vale». ¿Es democrático?", "No", "El resultado se acepta."),
        ex("Una niña sugiere que se vote por levantar la mano, pero algunos prefieren votar en secreto. ¿Qué conviene hacer antes de votar?", "Acordar cómo se votará", "Las reglas se definen antes."),
    ],
    D=[
        arith("El curso tiene 30 estudiantes. En una votación participaron 27 y 3 estaban ausentes. 15 votaron por la opción A y el resto por la B. ¿Cuántos votaron por la B?", "27-15", "Se resta de los 27 que votaron los 15 de A."),
        ex("Frases: A) «Se acuerda la regla y luego se vota». B) «Cambio la regla si pierdo». C) «Se respeta al que perdió». ¿Cuáles son democráticas?", "A y C", "La B no respeta el acuerdo."),
    ],
    context=[ex("El curso quiere elegir el nombre del equipo. La profesora explica: cada persona tiene un voto, se cuenta en la pizarra, y en caso de empate se vota de nuevo. ¿Hay reglas claras?", "Sí", "Definió voto, conteo y empate.")],
    selfcheck=[ex("En Orientación: ¿en una votación gana la mayoría?", "Sí", "Es la opción con más votos."), ex("¿Se acuerdan las reglas antes de votar?", "Sí", "Así se evita conflicto."), ex("¿Se acepta el resultado?", "Sí", "Es parte de la democracia.")],
    task=T("Lee: el curso debe elegir entre tres salidas: museo, parque o biblioteca. Escribe las reglas que acordarías antes de votar (al menos cuatro), cómo cuentas los votos y qué haces si hay empate. Después inventa un resultado (por ejemplo, 12, 10 y 8 votos) y di quién gana y por cuánto.", "Reglas: un voto por persona, hablar por turnos, 5 minutos de discusión, aceptar el resultado. Resultado: 12, 10, 8. Gana museo por 2 votos más que el parque.", ["escribe cuatro reglas claras", "cuenta bien los votos", "define qué hacer si hay empate"], ["texto escrito o dicho"], ["cambiar las reglas después", "ignorar a la minoría"], "Reconoce las reglas y revisa el conteo."),
    reinforce="Escribe tres reglas para una votación del curso.",
    extend="Explica por qué es importante respetar a la minoría después de una votación.",
)

lesson(
    OA8, 3,
    "Una hoja y un lápiz. Los roles y los grupos están escritos en los ejercicios.",
    "Aprenderé a distribuir roles y responsabilidades de manera justa, sin elegir por género, popularidad ni por quién lo hace mejor. Sirve para que todos participen.",
    ["Sé decidir con reglas claras.", "Sé que cada persona tiene fortalezas."],
    [
        "Un rol es una tarea que cumple una persona en un grupo, como coordinar, anotar, cuidar el tiempo o cuidar los materiales. Una responsabilidad es lo que me comprometo a hacer. Para repartir roles con equidad, se mira que todos participen y que ninguno tenga siempre la tarea más pesada o la más cómoda.",
        "Hay criterios justos para repartir: que la persona quiera, que se rote para que todos prueben cada rol, que se considere lo que necesita aprender y que se respeten los derechos de todos. No se reparte por género, por popularidad ni solo por quién lo hace mejor. Por ejemplo, no hay roles solo de niñas ni solo de niños.",
        "Participar no es dirigir. El que coordina ayuda a organizar, pero las decisiones importantes se toman entre todos. Si un rol resulta muy difícil, se puede pedir ayuda o cambiarlo en acuerdo con el grupo. Rotar los roles permite que todos aprendan.",
    ],
    [("rol", "tarea que cumple una persona en un grupo"), ("responsabilidad", "lo que me comprometo a hacer"), ("equidad", "dar a cada uno lo que necesita para participar"), ("rotar", "cambiar de rol para que todos prueben"), ("criterio", "regla para decidir de forma justa")],
    [
        W("Roles en un grupo", "Un grupo de 4 niños necesita estos roles: coordinar, anotar, cuidar el tiempo y cuidar los materiales. ¿Cuántos roles hay y cuántos niños por rol?", ["Hay 4 roles.", "Hay 4 niños.", "Cada niño cumple uno."], "4 roles, un niño por rol"),
        W("Criterio justo", "¿Qué criterio es justo para repartir: «los niños coordinan y las niñas anotan» o «rotamos los roles cada semana»?", ["La primera reparte por género.", "La segunda da la oportunidad a todos.", "Elige la segunda."], "«Rotamos los roles cada semana»"),
    ],
    [
        M("Repartir roles según quién es más popular.", "Se cree que lo popular lo hace mejor.", "Reparte con criterios justos y rota los roles."),
        M("Dejar siempre la tarea difícil al mismo compañero.", "Se piensa que él puede.", "Rota para que todos compartan lo pesado y lo cómodo."),
    ],
    R=[
        ex("Un rol, ¿es una tarea que cumple una persona en un grupo?", "Sí", "Así se define."),
        ex("¿Se reparten roles por género?", "No", "No es justo."),
        ex("Rotar roles, ¿es cambiar para que todos prueben?", "Sí", "Da la oportunidad a todos."),
    ],
    U=[
        ex("¿Qué criterios son justos para repartir roles?", "Que quiera, rotar, considerar lo que necesita aprender", "Respetan los derechos de todos."),
        ex("¿Participar es lo mismo que dirigir?", "No", "El que coordina ayuda a organizar."),
        ex("Si un rol es muy difícil, ¿qué se puede hacer?", "Pedir ayuda o cambiarlo con acuerdo del grupo", "Se ajusta entre todos."),
    ],
    A=[
        arith("Un curso de 20 estudiantes se organiza en grupos de 4. Cada grupo tiene 4 roles distintos. ¿Cuántos grupos hay?", "20//4", "Se reparten 20 estudiantes de a 4."),
        arith("Un grupo de 5 niños rota 5 roles, uno por semana. Ya pasaron 3 semanas. ¿Cuántas semanas faltan para que todos hagan los 5 roles?", "5-3", "Cada niño debe hacer 5 roles y ya hizo 3."),
        ex("Elige quién coordina con criterio justo: «el más popular» o «el que no ha coordinado aún y quiere hacerlo»", "El que no ha coordinado aún y quiere hacerlo", "Respeta rotación y voluntad."),
    ],
    Z=[
        ex("Un niño dice: «A Ema le toca siempre anotar porque tiene buena letra». ¿Es justo?", "No", "No rota ni considera que otros aprendan."),
        ex("Un grupo reparte roles según género. ¿Qué derecho olvidan?", "El derecho de cada uno a probar cualquier rol", "Todos pueden hacer cualquier rol."),
    ],
    D=[
        arith("Un grupo de 6 niños se reparte 3 roles en partes iguales, para que todos participen. ¿Cuántos niños tiene cada rol?", "6//3", "Se reparten 6 niños en 3 roles."),
        ex("Frases: A) «Todos rotamos». B) «Los roles de mandar son de los más populares». C) «Pregunto a quién le interesa». ¿Cuáles son equitativas?", "A y C", "La B se basa en popularidad."),
    ],
    context=[ex("En el grupo de Teo, cada semana cambian quién coordina. Esta semana le toca a Rita, según el orden de la rotación. ¿Es una distribución equitativa?", "Sí", "Rotan sin elegir por popularidad.")],
    selfcheck=[ex("En Orientación: ¿los roles se reparten con criterios justos?", "Sí", "Con rotación y voluntad."), ex("¿Se asignan por género?", "No", "Todos pueden hacer cualquier rol."), ex("¿Rotar ayuda a que todos aprendan?", "Sí", "Todos prueban distintos roles.")],
    task=T("Lee: un grupo de cinco niños (Ana, Beto, Cata, Dino y Eli) debe hacer una maqueta. Hay cinco roles: coordinar, dibujar, pegar, anotar y cuidar el tiempo. Escribe una tabla de tres semanas con un criterio de rotación. Explica por qué es justa y qué harías si un rol resulta muy difícil.", "Semana 1: Ana coordina, Beto dibuja, Cata pega, Dino anota, Eli cuida el tiempo. Semana 2: cada uno avanza un rol. Criterio: rotación. Si es difícil, pedimos ayuda.", ["usa un criterio de rotación", "todos tienen un rol cada semana", "no reparte por género ni popularidad"], ["tabla escrita"], ["asignar siempre lo mismo", "repartir por popularidad"], "Reconoce el criterio y revisa que todos participen."),
    reinforce="Escribe tres criterios justos para repartir roles.",
    extend="Inventa un grupo de seis niños y haz una rotación de dos semanas.",
)

lesson(
    OA8, 4,
    "Una hoja y un lápiz. Las tablas de seguimiento están escritas en los ejercicios.",
    "Aprenderé a cumplir mis responsabilidades, a revisar cómo van y a ajustar el plan. Sirve para que el curso funcione bien sin culpar a nadie.",
    ["Sé repartir roles con equidad.", "Sé cumplir una tarea breve."],
    [
        "Cumplir una responsabilidad es hacer lo que me comprometí a hacer, con calidad y a tiempo. Para saber cómo vamos, se hace un seguimiento: una tabla simple con las tareas, quién las hace y si se cumplieron. El seguimiento no es para castigar, sino para mejorar. Se revisa cada cierto tiempo, por ejemplo cada viernes.",
        "Cumplir no siempre es lo mismo que aprender: una tarea puede estar hecha, pero hay que preguntarse qué aprendimos. También se evalúa cómo participó cada uno y qué se puede ajustar. Si alguien no pudo cumplir, se pregunta por qué antes de culpar. Puede haber causas fuera de su control, como una enfermedad, una falta de materiales en su casa o un problema de transporte.",
        "Si algo no se cumplió, se busca una solución: pedir ayuda, dividir la tarea, cambiar de rol o dar más tiempo. Los derechos de todos se respetan: nadie debe cargar con todo. Si un compañero no cumple por razones que no puede resolver, se avisa a la profesora para encontrar una solución, sin humillarlo.",
    ],
    [("seguimiento", "revisar cada cierto tiempo cómo van las tareas"), ("cumplir", "hacer lo que me comprometí a hacer"), ("evaluar", "mirar qué salió bien y qué se puede mejorar"), ("ajustar", "cambiar el plan para que funcione mejor"), ("apoyo", "ayuda para poder cumplir")],
    [
        W("Leer un seguimiento", "En una tabla, Ana cumplió 4 de sus 5 tareas. ¿Cuántas le faltan?", ["Eran 5 tareas.", "Cumplió 4.", "Faltan 5 menos 4."], "1 tarea"),
        W("Qué hacer si alguien no cumple", "Tomás no trajo los materiales porque su familia no pudo comprarlos. ¿Qué haces: reclamarle o avisar a la profesora para buscar una solución?", ["No es su culpa.", "Hay una condición fuera de su control.", "Se busca una solución sin humillarlo."], "Avisar a la profesora para buscar una solución"),
    ],
    [
        M("Culpar a un compañero que no cumplió sin preguntar por qué.", "Se piensa que siempre depende de él.", "Pregunta primero y busca una solución."),
        M("Creer que si cumplí la tarea ya aprendí.", "Se confunde terminar con aprender.", "Pregúntate qué aprendiste y qué mejorarías."),
    ],
    R=[
        ex("Cumplir una responsabilidad, ¿es hacer lo que me comprometí a hacer?", "Sí", "Así se define."),
        ex("El seguimiento, ¿sirve para revisar cómo van las tareas?", "Sí", "Se revisa cada cierto tiempo."),
        ex("¿El seguimiento es para castigar?", "No", "Es para mejorar."),
    ],
    U=[
        ex("¿Terminar una tarea siempre significa que aprendí?", "No", "Hay que preguntarse qué se aprendió."),
        ex("Si alguien no cumplió, ¿qué se hace antes de culpar?", "Preguntar por qué", "Puede haber causas fuera de su control."),
        ex("¿Qué se puede hacer si una tarea no se cumplió?", "Pedir ayuda, dividirla o dar más tiempo", "Se busca una solución."),
    ],
    A=[
        arith("Eli debía cumplir 6 tareas en el mes y cumplió 4. ¿Cuántas le faltaron?", "6-4", "La diferencia entre lo planeado y lo cumplido."),
        ex("En una tabla, Dino cumplió el lunes, el martes y el jueves, y no cumplió el miércoles ni el viernes. ¿Cuántos días cumplió de 5?", "3", "Lunes, martes y jueves."),
        ex("Si una compañera no puede cumplir porque estuvo enferma, ¿qué solución justa hay: darle más tiempo o ponerle una anotación negativa?", "Darle más tiempo", "Hay una causa fuera de su control."),
    ],
    Z=[
        ex("Un niño dice: «Como no trajo el material, no merece estar en el grupo». ¿Es justo?", "No", "Puede haber causas fuera de su control."),
        ex("Una tabla muestra que un rol nunca se cumple. ¿Qué es mejor: ajustar el plan o seguir igual y reclamar cada semana?", "Ajustar el plan", "Se busca que funcione."),
    ],
    D=[
        arith("Un grupo tiene 5 roles y 4 semanas de seguimiento. Cada semana se revisa si cada rol se cumplió. ¿Cuántas revisiones hacen en total?", "5*4", "Son 5 revisiones repetidas 4 semanas."),
        ex("Frases: A) «Revisamos juntos y mejoramos». B) «Castigo al que falla». C) «Preguntamos por qué no se cumplió». ¿Cuáles son adecuadas?", "A y C", "La B no busca soluciones."),
    ],
    context=[ex("En el curso, cada viernes revisan una tabla de responsabilidades. Cuando Ema no pudo cumplir, le preguntaron por qué y le ofrecieron ayuda. ¿Evaluaron con respeto?", "Sí", "Buscaron una solución sin culpar.")],
    selfcheck=[ex("En Orientación: ¿el seguimiento es para castigar?", "No", "Es para mejorar."), ex("¿Se pregunta por qué antes de culpar?", "Sí", "Puede haber causas fuera de su control."), ex("¿Cumplir y aprender son siempre lo mismo?", "No", "Se puede cumplir sin aprender.")],
    task=T("Crea una tabla de seguimiento para un grupo con tres roles y cinco días. Marca ✓ si se cumplió o ✗ si no. Inventa un caso en que un rol no se cumplió por una causa fuera del control del niño. Escribe qué harías: preguntar, ajustar el plan y qué dirías al niño. Agrega una pregunta sobre qué aprendió cada uno.", "Tabla con tres roles y cinco días. Caso: no trajo materiales. Pregunto por qué, ajusto el plan y le ofrezco ayuda. Pregunta: ¿qué aprendiste?", ["tabla con tres roles y cinco días", "pregunta por qué antes de culpar", "ajusta el plan y propone apoyo"], ["tabla escrita"], ["culpar por condiciones externas", "confundir cumplir con aprender"], "Reconoce la tabla y revisa que no se humille a nadie."),
    reinforce="Haz una tabla simple de seguimiento para tres tareas de tu curso.",
    extend="Escribe tres preguntas para evaluar cómo funcionó un grupo.",
)

lesson(
    OA8, 5,
    "Una hoja y un lápiz. Los casos con condiciones nuevas están escritos en los ejercicios.",
    "Aprenderé a aplicar lo aprendido cuando cambian las condiciones: falta gente, hay menos tiempo o llueve. Sirve para seguir participando con justicia en situaciones nuevas.",
    ["Sé proponer, decidir, repartir roles y hacer seguimiento.", "Sé ajustar un plan."],
    [
        "A veces cambian las condiciones: falta un compañero, hay menos tiempo o el lugar no se puede usar. Lo que aprendiste sigue siendo útil, pero hay que adaptarlo. Primero, dialoga: cada uno dice cómo el cambio afecta el plan. Segundo, propón ajustes. Tercero, decide con reglas claras. Cuarto, redistribuye los roles con equidad.",
        "Al adaptar, se mantienen los derechos de todos: nadie debe cargar con el trabajo de los ausentes sin acuerdo, nadie queda fuera, y las decisiones se toman con respeto. Si falta una persona, sus roles se reparten entre los demás o se pospone lo que no se puede hacer. No se culpa a quien faltó.",
        "También se pueden ajustar los plazos o el alcance de la tarea. Por ejemplo, si hay la mitad del tiempo, se elige lo más importante. Al final se evalúa: ¿se respetaron los derechos?, ¿se cumplió lo esencial?, ¿qué aprendimos para otra vez? Así transfieres lo aprendido a nuevas situaciones.",
    ],
    [("condición", "algo del contexto que puede cambiar, como el tiempo o quién está"), ("adaptar", "cambiar un plan según la nueva situación"), ("redistribuir", "repartir de nuevo los roles"), ("alcance", "cuánto se va a hacer"), ("transferir", "usar lo aprendido en una situación nueva")],
    [
        W("Falta un compañero", "Un grupo de 5 debía repartir 5 roles. Hoy falta 1 compañero. ¿Cuántos roles se deben redistribuir entre los 4 presentes?", ["Faltaba una persona, con su rol.", "Quedan 4 personas.", "Los 5 roles se reparten entre 4."], "5 roles entre 4 personas, sin culpar al ausente"),
        W("Menos tiempo", "Un grupo tenía 40 minutos y ahora tiene 20. ¿Qué hace: seguir con todo igual o elegir lo más importante?", ["Hay la mitad del tiempo.", "No se puede hacer todo.", "Se elige lo más importante."], "Elegir lo más importante"),
    ],
    [
        M("Dejar que una persona cargue con todo el trabajo cuando alguien falta.", "Se piensa que ella puede.", "Se reparte entre todos con acuerdo."),
        M("Pensar que lo aprendido no sirve cuando cambia la situación.", "Se cree que cada situación es totalmente nueva.", "Se adapta lo que ya sabes."),
    ],
    R=[
        ex("Si falta un compañero, ¿se culpa a quien faltó?", "No", "No se culpa."),
        ex("Si hay menos tiempo, ¿se puede elegir lo más importante?", "Sí", "Se ajusta el alcance."),
        ex("¿Se mantienen los derechos de todos al adaptar?", "Sí", "Siempre se mantienen."),
    ],
    U=[
        ex("¿Qué se hace primero cuando cambian las condiciones: dialogar o decidir sin hablar?", "Dialogar", "Cada uno dice cómo le afecta."),
        ex("¿Qué es redistribuir?", "Repartir de nuevo los roles", "Se ajusta a quienes están."),
        ex("¿Qué se pregunta al final?", "Si se respetaron los derechos, si se cumplió lo esencial y qué aprendimos", "Así se evalúa."),
    ],
    A=[
        arith("Un grupo de 6 tiene 6 roles. Faltan 2 personas. ¿Cuántas personas quedan para repartir los roles?", "6-2", "Se resta a las 6 personas las 2 ausentes."),
        arith("Una tarea debía durar 40 minutos y ahora hay solo 25. ¿Cuántos minutos menos hay?", "40-25", "La diferencia de tiempo."),
        ex("Llueve y el juego del patio no se puede. Elige una adaptación: jugar en la sala con reglas tranquilas o suspender la actividad sin pensarlo.", "Jugar en la sala con reglas tranquilas", "Se adapta manteniendo la participación."),
    ],
    Z=[
        ex("Un niño dice: «Que lo hagan los que vinieron y listo». ¿Qué falta considerar?", "Repartir con acuerdo y no culpar a los ausentes", "Hay que redistribuir con equidad."),
        ex("El curso decide por votación cambiar el día de una actividad. Un grupo pierde. ¿Qué se hace?", "Se respeta el resultado y se apoya al grupo", "Es una decisión democrática."),
    ],
    D=[
        arith("Un curso de 24 estudiantes arma equipos de 6. Hoy faltan 4. ¿Cuántos equipos completos de 6 pueden formar los presentes?", "(24-4)//6", "Quedan 20 estudiantes; en equipos de 6 caben 3 y sobran 2."),
        ex("Frases: A) «Dialogamos, ajustamos y repartimos». B) «Yo mando lo que se hace». C) «Mantenemos lo esencial». ¿Cuáles son adecuadas?", "A y C", "La B no respeta la participación."),
    ],
    context=[ex("Un grupo debía exponer en 10 minutos, pero se redujo a 5. Dialogan, eligen lo esencial y redistribuyen las partes. ¿Transfirieron lo aprendido?", "Sí", "Adaptaron con diálogo y equidad.")],
    selfcheck=[ex("En Orientación: ¿se puede adaptar un plan cuando cambian las condiciones?", "Sí", "Se ajusta manteniendo los derechos."), ex("¿Se culpa al ausente?", "No", "No es justo."), ex("¿Se evalúa al final?", "Sí", "Para aprender para otra vez.")],
    task=T("Lee: un grupo de cinco debe presentar una exposición en 20 minutos. Hoy falta uno de ellos y solo hay 12 minutos. Escribe cómo dialogarían, qué decidirían (qué es lo más importante), cómo redistribuirían los roles y qué dirían al compañero ausente cuando vuelva. Agrega una pregunta de evaluación.", "Dialogan por turnos. Eligen lo esencial. Reparten los roles entre cuatro. Al ausente: «Te contamos lo que hicimos». Pregunta: ¿se respetaron los derechos?", ["dialoga y decide con reglas", "redistribuye con equidad", "no culpa al ausente"], ["texto escrito o dicho"], ["cargar a una persona", "culpar al ausente"], "Reconoce la adaptación y revisa que no se cargue a una sola persona."),
    reinforce="Escribe tres pasos para adaptar un plan cuando falta alguien.",
    extend="Inventa otra condición diferente y explica cómo la resolverías con equidad.",
)
