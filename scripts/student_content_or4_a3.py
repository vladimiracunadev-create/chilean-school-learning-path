"""Cuaderno del estudiante, 4.º básico Orientación: OA 05 (autocuidado, intimidad y protección) y OA 06 (solidaridad, empatía, buen trato)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA5, OA6 = "OR04 OA 05", "OR04 OA 06"


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


# ================================================================ OA 05
lesson(
    OA5, 1,
    "Una hoja y un lápiz. Los horarios y los casos están escritos en los ejercicios. Cada hogar tiene recursos distintos: la clase no pide comprar nada.",
    "Aprenderé a planificar una rutina de higiene que se pueda ajustar cuando algo cambia. Sirve para cuidar mi cuerpo de forma autónoma, sin angustia.",
    ["Sé lavarme las manos y los dientes.", "Sé pedir ayuda a una persona adulta."],
    [
        "La higiene es la limpieza que cuida tu cuerpo y tu salud. Las rutinas básicas son lavarte las manos con agua y jabón durante al menos 20 segundos, antes de comer y después de ir al baño. También cepillarte los dientes al menos dos veces al día, durante unos dos minutos cada vez. Ducharte con regularidad, cambiarte de ropa interior y mantener las uñas limpias y cortas, con ayuda si hace falta.",
        "Una rutina flexible es un plan que puedes ajustar. Si un día hay poco tiempo, mantienes lo esencial: manos y dientes. Si cambia el horario, la ducha puede pasar de la mañana a la tarde. Lo importante es que el cuidado ocurra, no que el orden sea siempre el mismo.",
        "Algunas familias tienen más recursos que otras. Si falta jabón, pasta dental o agua, no es culpa tuya. Avisa a una persona adulta de confianza, de tu casa o de la escuela, para que te ayuden a encontrar una solución. En esta clase no hace falta comparar lo que tiene cada uno.",
    ],
    [("higiene", "limpieza que cuida mi cuerpo y mi salud"), ("rutina", "cosas que hago con regularidad"), ("flexible", "que se puede ajustar sin dejar de cumplir lo esencial"), ("esencial", "lo más importante, lo que no puede faltar"), ("autónomo", "que lo hace por sí mismo, con ayuda solo si la necesita")],
    [
        W("Calcular el cepillado", "Camila se cepilla los dientes 2 minutos, 2 veces al día. ¿Cuántos minutos se cepilla al día?", ["Cada vez son 2 minutos.", "Son 2 veces al día.", "Se multiplica: 2 por 2."], "4 minutos"),
        W("Ajustar la rutina", "Hoy Tomás se levantó tarde y no le alcanza el tiempo para todo. ¿Qué mantiene como esencial: lavarse las manos y los dientes o solo peinarse?", ["Lo esencial cuida la salud.", "Manos y dientes son esenciales.", "Lo demás puede pasar a la tarde."], "Lavarse las manos y los dientes"),
    ],
    [
        M("Pensar que si falta jabón o pasta es mi culpa.", "Se cree que el niño debe resolver los recursos del hogar.", "Avisa a un adulto de confianza; no es tu responsabilidad conseguirlos."),
        M("Dejar toda la rutina si no puedo hacerla completa.", "Se piensa que solo vale si es perfecta.", "Mantén lo esencial y ajusta lo demás."),
    ],
    R=[
        ex("¿Cuántos segundos como mínimo hay que lavarse las manos con jabón?", "20 segundos", "Es el tiempo mínimo recomendado."),
        ex("¿Cuántas veces al día como mínimo hay que cepillarse los dientes?", "2 veces", "Se recomienda mañana y noche, al menos."),
        ex("Antes de comer, ¿hay que lavarse las manos?", "Sí", "Así se evita llevar gérmenes a la boca."),
    ],
    U=[
        ex("¿Qué es una rutina flexible?", "Un plan que se puede ajustar sin dejar lo esencial", "Se adapta a lo que cambie en el día."),
        ex("Si en tu casa no hay jabón, ¿es culpa tuya?", "No", "Los recursos del hogar los resuelven los adultos."),
        ex("Si hay poco tiempo, ¿qué es lo esencial de la higiene?", "Manos y dientes", "Son lo básico para cuidar la salud."),
    ],
    A=[
        arith("Un estudiante se cepilla 2 minutos cada vez, 2 veces al día, durante 7 días. ¿Cuántos minutos se cepilla en una semana?", "2*2*7", "Son 4 minutos al día repetidos 7 días."),
        arith("Lola se lava las manos 20 segundos, 5 veces durante el día. ¿Cuántos segundos de lavado hay en total?", "20*5", "Es 20 segundos repetido 5 veces."),
        ex("Hoy Pía se acostó tarde y mañana tendrá poco tiempo. ¿Qué ajuste flexible mantiene lo esencial: lavarse manos y dientes y ducharse en la tarde, o saltarse manos, dientes y ducha?", "Lavarse manos y dientes, y ducharse en la tarde", "Mantiene lo esencial y mueve lo demás."),
    ],
    Z=[
        ex("Un niño no tiene pasta de dientes. ¿Qué es lo mejor: no cepillarse nunca o avisar a una persona adulta de confianza?", "Avisar a una persona adulta de confianza", "Así se busca una solución sin culpa."),
        ex("Una rutina tiene 5 pasos y hoy hay poco tiempo. ¿Es mejor abandonar todo o mantener los pasos esenciales?", "Mantener los pasos esenciales", "Algo del cuidado es mejor que nada."),
    ],
    D=[
        arith("Una rutina de la mañana tiene 3 pasos de 5 minutos cada uno. Si los dos primeros ya se hicieron, ¿cuántos minutos faltan?", "3*5-2*5", "Los 15 minutos totales menos los 10 ya usados."),
        ex("Plan A: «Cada día igual y si falla, no sirve». Plan B: «Manos y dientes siempre; la ducha cuando se pueda». ¿Cuál es flexible?", "Plan B", "Conserva lo esencial y deja ajustar lo demás."),
    ],
    context=[ex("Un día, Dino salió corriendo al colegio y no se cepilló los dientes. Al llegar a casa, lo hizo con calma y sin enojarse consigo mismo. ¿Aplicó una rutina flexible?", "Sí", "Ajustó el momento del cuidado sin dejarlo de lado.")],
    selfcheck=[ex("En Orientación: ¿manos y dientes son lo esencial de la higiene?", "Sí", "Son la base del cuidado."), ex("¿Es tu culpa si en casa falta un producto de higiene?", "No", "Pide ayuda a un adulto de confianza."), ex("¿Una rutina puede ajustarse en un día difícil?", "Sí", "Es un plan flexible.")],
    task=T("Arma tu plan de higiene con estos momentos: al despertar, antes de comer, después del baño, antes de dormir. Para cada uno escribe qué harías (por ejemplo, manos o dientes). Agrega una versión corta para un día con poco tiempo y quién te ayudaría si falta algo.", "Al despertar: lavarme la cara y los dientes. Antes de comer: manos 20 segundos. Día corto: solo manos y dientes. Ayuda: una persona de mi casa.", ["escribe una acción por cada momento", "tiene una versión corta con lo esencial", "nombra a quién pedir ayuda si falta algo"], ["plan escrito o dibujado"], ["rutina rígida", "culparse por falta de recursos"], "Reconoce lo esencial y revisa que el plan se pueda ajustar."),
    reinforce="Dibuja o escribe una rutina de higiene de cinco pasos para un día normal.",
    extend="Escribe una versión de dos pasos de tu rutina para un día con mucha prisa.",
)

lesson(
    OA5, 2,
    "Una hoja y un lápiz. Los horarios están escritos en los ejercicios.",
    "Aprenderé a equilibrar el descanso, la recreación y la actividad física. Sirve para cuidar mi cuerpo y mis emociones de forma autónoma.",
    ["Conozco una rutina de higiene.", "Sé que dormir ayuda a aprender."],
    [
        "El cuerpo necesita descansar, jugar y moverse. Para tu edad, se recomienda dormir entre 9 y 11 horas cada noche. Dormir bien ayuda a pensar, a regular las emociones y a crecer. Acostarte a una hora parecida cada noche y apagar las pantallas un rato antes de dormir ayuda a que el sueño llegue.",
        "La recreación es lo que haces por gusto: jugar, leer, dibujar o conversar con amigos. Sirve para descansar la mente y disfrutar. La actividad física es moverse con energía, como correr, saltar, bailar o andar en bicicleta. Se recomienda al menos 60 minutos de movimiento al día, que pueden sumarse a lo largo del día.",
        "El equilibrio no significa hacerlo todo igual cada día. Algunos días hay más tareas y otros más tiempo libre. Lo importante es que durante la semana haya descanso, juego y movimiento. Si no puedes dormir bien o te sientes sin energía muchos días, cuéntaselo a una persona adulta de confianza.",
    ],
    [("descanso", "tiempo para recuperar energía, como dormir"), ("recreación", "actividad que hago por gusto para disfrutar"), ("actividad física", "moverse con energía"), ("equilibrio", "que haya un poco de cada cosa que necesito"), ("pantalla", "aparato con imagen, como un celular o un televisor")],
    [
        W("Horas de sueño", "Pedro se acuesta a las 21:00 y se levanta a las 7:00 de la mañana. ¿Cuántas horas duerme?", ["De las 21:00 a las 24:00 son 3 horas.", "De las 24:00 a las 7:00 son 7 horas.", "Se suman: 3 más 7."], "10 horas"),
        W("Sumar el movimiento", "Ana se movió 20 minutos en el recreo, 25 en Educación Física y 15 caminando a casa. ¿Cuántos minutos se movió?", ["Se suman los tres momentos.", "20 más 25 más 15.", "El total dice si llegó a 60."], "60 minutos"),
    ],
    [
        M("Pensar que dormir poco no importa.", "Se cree que solo cansa y ya.", "Dormir bien ayuda a aprender, a sentirse mejor y a crecer."),
        M("Creer que el movimiento debe ser un deporte exigente.", "Se piensa que solo vale competir.", "Jugar, bailar o caminar rápido también cuentan."),
    ],
    R=[
        ex("¿Cuántas horas se recomienda dormir como mínimo a tu edad: 9 o 5?", "9", "Se recomienda entre 9 y 11 horas."),
        ex("Jugar con amigos o dibujar, ¿es recreación?", "Sí", "Se hace por gusto, para disfrutar."),
        ex("Bailar o correr, ¿es actividad física?", "Sí", "Es moverse con energía."),
    ],
    U=[
        ex("¿Por qué conviene apagar las pantallas un rato antes de dormir?", "Porque ayuda a que llegue el sueño", "Las pantallas pueden mantener la mente despierta."),
        ex("¿Cuántos minutos de movimiento se recomiendan al día?", "Al menos 60 minutos", "Pueden sumarse a lo largo del día."),
        ex("Si te sientes sin energía muchos días, ¿qué haces?", "Se lo cuento a una persona adulta de confianza", "Puede haber algo que ajustar."),
    ],
    A=[
        arith("Lola se acuesta a las 22:00 y se levanta a las 7:00. ¿Cuántas horas duerme? Calcula las horas hasta medianoche y suma.", "2+7", "De 22:00 a medianoche son 2 horas y luego 7 más."),
        arith("Marta caminó 15 minutos, jugó a la pelota 30 minutos y bailó 15. ¿Cuántos minutos se movió en total?", "15+30+15", "Se suman los tres momentos."),
        ex("Un día tienes mucha tarea. ¿Cuál es un buen ajuste: dormir menos o hacer una pausa corta de movimiento y mantener tu hora de dormir?", "Hacer una pausa corta de movimiento y mantener la hora de dormir", "Cuida el descanso y el equilibrio."),
    ],
    Z=[
        ex("Un niño dice: «Mejor no duermo, así juego más». ¿Qué le dices?", "Que dormir ayuda a aprender y a sentirse bien", "El descanso es necesario."),
        ex("Una niña dice que no puede hacer 60 minutos de movimiento seguidos. ¿Cómo puede lograrlo?", "Sumando momentos cortos durante el día", "Se pueden sumar tramos de movimiento."),
    ],
    D=[
        arith("Una semana tiene 7 noches. Si Dino duerme 9 horas cada noche, ¿cuántas horas duerme en la semana?", "9*7", "Es 9 horas repetido 7 noches."),
        ex("Plan A: dormir 6 horas, ninguna actividad. Plan B: dormir 10 horas, 60 minutos de movimiento y un rato de juego. ¿Cuál tiene equilibrio?", "Plan B", "Incluye descanso, movimiento y recreación."),
    ],
    context=[ex("Después de la tarea, Joaquín jugó a la pelota 30 minutos con vecinos, leyó un rato y se acostó a su hora. ¿Cuidó el equilibrio?", "Sí", "Tuvo movimiento, recreación y descanso.")],
    selfcheck=[ex("En Orientación: ¿el descanso, el juego y el movimiento son parte del autocuidado?", "Sí", "El cuerpo necesita las tres cosas."), ex("¿Dormir ayuda a aprender?", "Sí", "El sueño ayuda a la memoria y a la atención."), ex("¿Jugar también cuenta como recreación?", "Sí", "Se hace por gusto.")],
    task=T("Arma un horario de un día de colegio con estos tres bloques: descanso (a qué hora te acuestas y te levantas), movimiento (qué harías y cuántos minutos) y recreación (qué disfrutarías). Si no tienes alguno de los materiales, usa un juego sin materiales. Revisa que sumen los minutos de movimiento.", "Descanso: acostarme a las 21:30 y levantarme a las 7:00. Movimiento: caminar 20 minutos y bailar 20. Recreación: dibujar.", ["tiene los tres bloques", "suma los minutos de movimiento", "no pide materiales especiales"], ["horario escrito o dibujado"], ["no incluir descanso", "olvidar la recreación"], "Reconoce los tres bloques y pregunta cómo ajustaría el plan un día con más tarea."),
    reinforce="Escribe tres actividades físicas que podrías hacer en tu casa o patio, sin materiales.",
    extend="Anota por tres días cuántas horas dormiste y cuántos minutos te moviste, y escribe qué ajustarías.",
)

lesson(
    OA5, 3,
    "Una hoja y un lápiz. Los menús están escritos en los ejercicios. No se habla del peso ni del cuerpo de nadie.",
    "Aprenderé a elegir y disfrutar alimentos variados, sin culpa y sin controlar el cuerpo. Sirve para cuidar mi salud de manera tranquila.",
    ["Conozco rutinas de higiene y descanso.", "Sé que comer da energía."],
    [
        "Comer variado ayuda a crecer, a pensar y a tener energía. Los grupos de alimentos son: frutas y verduras, legumbres como lentejas y porotos, cereales como arroz y pan, lácteos, y carnes, huevos o pescados. También es importante tomar agua. Un plato variado tiene alimentos de varios grupos.",
        "Ningún alimento te hace una mejor o peor persona. Algunos conviene comerlos todos los días y otros de vez en cuando, como las golosinas. Los envases con sellos «ALTO EN» avisan que tienen mucha azúcar, sal o grasas, y conviene comerlos pocas veces. Comer según el hambre, sin culpa ni castigo, también es autocuidado.",
        "No es un tema para comentar el cuerpo de los demás ni para hacer dietas por tu cuenta. Los adultos que te cuidan deciden las compras y las comidas según lo que tienen. Si no tienes suficiente comida o te quedas con hambre, no es tu culpa. Cuéntaselo a una persona adulta de confianza de la escuela para que te ayude.",
    ],
    [("alimentación", "lo que comemos y bebemos"), ("variado", "con muchos tipos distintos"), ("legumbre", "alimento como lentejas, porotos o garbanzos"), ("sello ALTO EN", "aviso del envase de que tiene mucha azúcar, sal o grasas"), ("hidratación", "tomar agua para que el cuerpo funcione bien")],
    [
        W("Plato variado", "Un almuerzo tiene arroz, lentejas, ensalada de tomate y un yogur. ¿Cuántos grupos distintos de alimentos hay?", ["El arroz es cereal.", "Las lentejas son legumbres, el tomate es del grupo frutas y verduras y el yogur es lácteo.", "Se cuentan: 4 grupos."], "4 grupos"),
        W("Sin comentar el cuerpo", "Un compañero dice: «No comas pan, que engorda». ¿Es respetuoso?", ["Comentar el cuerpo de otros no corresponde.", "Un solo alimento no define a una persona.", "No es respetuoso."], "No es respetuoso"),
    ],
    [
        M("Decir que un alimento es «bueno» o «malo» como persona.", "Se mezcla la comida con el valor de uno.", "Hay alimentos para todos los días y otros de vez en cuando; nadie es mejor por lo que come."),
        M("Pensar que debo conseguir la comida de mi casa.", "Se cree que el niño resuelve los recursos.", "Si falta comida, avisa a un adulto de confianza; no es tu culpa."),
    ],
    R=[
        ex("¿Las lentejas son legumbres?", "Sí", "Las legumbres incluyen lentejas, porotos y garbanzos."),
        ex("El arroz y el pan, ¿son cereales?", "Sí", "Se hacen con granos de cereal."),
        ex("¿Es importante tomar agua?", "Sí", "El cuerpo necesita hidratarse."),
    ],
    U=[
        ex("¿Qué avisan los sellos «ALTO EN»?", "Que el alimento tiene mucha azúcar, sal o grasas", "Conviene comerlos pocas veces."),
        ex("¿Ser buena persona depende de qué alimentos comes?", "No", "El valor de una persona no depende de la comida."),
        ex("Si te quedas con hambre en tu casa, ¿es tu culpa?", "No", "Debes avisar a un adulto de confianza."),
    ],
    A=[
        ex("Un menú tiene fideos, carne, ensalada de lechuga y una manzana. ¿Cuántos grupos distintos hay? Recuerda que frutas y verduras son un solo grupo.", "3", "Los fideos son cereal, la carne es otro grupo, y la lechuga y la manzana son del mismo grupo: frutas y verduras."),
        arith("La recomendación es comer 5 porciones de frutas y verduras al día. Ya comiste 3. ¿Cuántas te faltan?", "5-3", "Se resta lo comido de lo recomendado."),
        ex("Un compañero comenta lo que come otro en el recreo. ¿Qué frase es respetuosa: «Cada uno come lo que tiene, no comentemos» o «Qué poco sano comes»?", "«Cada uno come lo que tiene, no comentemos»", "No se comentan las comidas ni el cuerpo de los demás."),
    ],
    Z=[
        ex("Un niño dice: «Si como un dulce, soy malo». ¿Qué le dices?", "Que ningún alimento te hace malo y que los dulces se comen de vez en cuando", "Se come sin culpa."),
        ex("Una niña dice «hoy no tengo qué comer en mi casa». ¿Qué debe hacer?", "Contárselo a una persona adulta de confianza de la escuela", "Los adultos pueden ayudar."),
    ],
    D=[
        arith("En una semana de 5 días de colegio, Ema tomó 6 vasos de agua cada día. ¿Cuántos vasos tomó en esos 5 días?", "6*5", "Es 6 vasos repetidos 5 días."),
        ex("Plan A: «Solo como lo que me gusta». Plan B: «Como de varios grupos y de vez en cuando golosinas». ¿Cuál es más variado?", "Plan B", "Incluye alimentos de varios grupos."),
    ],
    context=[ex("En la hora de almuerzo, Nico ve que su compañero tiene un sello «ALTO EN» en su galleta y le dice «qué mala persona eres». ¿Es correcto?", "No", "Un alimento no define a una persona.")],
    selfcheck=[ex("En Orientación: ¿comer variado ayuda a crecer?", "Sí", "Da energía y nutrientes."), ex("¿Hay que sentir culpa por comer un dulce de vez en cuando?", "No", "Se puede comer sin castigo."), ex("¿Puedes pedir ayuda si no tienes suficiente comida?", "Sí", "Los adultos pueden ayudarte.")],
    task=T("Arma un menú para un día con desayuno, almuerzo y once o cena con alimentos variados. Marca qué grupo tiene cada alimento y cuántas porciones de frutas y verduras incluiste. Usa solo comidas comunes. Si en tu casa no puedes completar el menú, escribe a qué persona adulta de confianza pedirías ayuda.", "Desayuno: pan y leche. Almuerzo: arroz, lentejas y ensalada. Once: yogur y una manzana. Frutas y verduras: 2 porciones (la ensalada y la manzana).", ["incluye alimentos de varios grupos", "cuenta las porciones de frutas y verduras", "no comenta el cuerpo ni juzga a otros"], ["menú escrito o dibujado"], ["decir bueno o malo como persona", "comentar el cuerpo"], "Reconoce los grupos y revisa que no haya culpa ni comparaciones."),
    reinforce="Dibuja un plato con alimentos de tres grupos distintos.",
    extend="Lee los sellos de un envase de tu casa, con un adulto, y anota cuál dice «ALTO EN».",
)

lesson(
    OA5, 4,
    "Una hoja y un lápiz. Los casos con personajes están escritos en los ejercicios.",
    "Aprenderé a resguardar mi cuerpo, mi intimidad y mi información personal. Sirve para estar seguro dentro y fuera de internet.",
    ["Conozco el consentimiento y los límites.", "Sé que mi cuerpo es mío."],
    [
        "Tu cuerpo es tuyo. Las partes que cubre el traje de baño son privadas: nadie debe tocarlas, mirarlas, sacarles fotos ni pedirte que las muestres. Solo hay excepciones de salud o higiene, por ejemplo un control médico con una persona adulta de tu confianza presente. Antes te explican qué harán y por qué, y tú puedes preguntar o decir que no estás cómodo. Tu intimidad también incluye lo que piensas, sientes y escribes.",
        "La información personal es lo que dice quién eres: tu nombre completo, tu dirección, tu teléfono, tu colegio, tus claves, tus fotos y tus horarios. En internet o en un juego, esa información no se comparte con personas que no conoces. Las claves se guardan en secreto y solo se comparten con una persona adulta de tu familia. No aceptes encuentros ni regalos de desconocidos.",
        "No debes enviar fotos de tu cuerpo, aunque te las pidan como un juego, un premio o una amenaza. Si alguien te las pide, no respondas, guarda el mensaje y cuéntaselo a una persona adulta de confianza. Si algo te asusta, no es tu culpa. Pedir ayuda siempre es correcto.",
    ],
    [("intimidad", "lo privado de una persona: su cuerpo y lo que siente"), ("información personal", "datos que dicen quién soy y dónde estoy"), ("clave", "palabra secreta que protege mis cuentas"), ("desconocido", "persona que no conozco o que no conoce mi familia"), ("privado", "algo que cada persona decide si comparte")],
    [
        W("Información que se comparte o no", "En un juego en línea, un jugador te pregunta cuál es tu dirección. ¿La compartes?", ["La dirección dice dónde vives.", "No conoces al jugador.", "No la compartes."], "No, no la compartes"),
        W("Si alguien pide una foto", "Un desconocido te pide una foto de tu cuerpo como juego. ¿Qué haces?", ["Nadie debe pedir eso.", "No respondes y guardas el mensaje.", "Se lo cuentas a una persona adulta de confianza."], "No responder, guardar el mensaje y contárselo a un adulto de confianza"),
    ],
    [
        M("Pensar que si me lo piden como un juego, puedo hacerlo.", "Se confunde un juego con una presión.", "Nadie puede pedirte fotos de tu cuerpo ni que lo muestres."),
        M("Compartir mis claves con amigos para demostrar confianza.", "Se cree que la confianza se muestra así.", "Las claves son secretas; solo se comparten con una persona adulta de tu familia."),
    ],
    R=[
        ex("Las partes que cubre el traje de baño, ¿son privadas?", "Sí", "Nadie debe tocarlas ni pedirte que las muestres."),
        ex("Tu dirección, ¿es información personal?", "Sí", "Dice dónde vives."),
        ex("¿Las claves se comparten con cualquiera?", "No", "Son secretas y solo se comparten con una persona adulta de tu familia."),
    ],
    U=[
        ex("¿Qué haces si alguien te pide fotos de tu cuerpo?", "No respondo y se lo cuento a un adulto de confianza", "Nadie debe pedir eso."),
        ex("¿Es tu culpa si alguien te pide algo así?", "No", "La responsabilidad es de quien lo pide."),
        ex("Un desconocido te ofrece un regalo si te encuentras con él. ¿Aceptas?", "No", "No se aceptan encuentros ni regalos de desconocidos."),
    ],
    A=[
        ex("Clasifica: color favorito, dirección, nombre del colegio y comida preferida. ¿Cuáles son información personal que no se comparte con desconocidos?", "Dirección y nombre del colegio", "Dicen dónde estás."),
        ex("Un amigo te pide tu clave del juego «para jugar contigo». ¿Qué respondes?", "No, es secreta", "Las claves no se comparten con amigos ni desconocidos."),
        ex("En un control médico, la doctora te explica antes qué hará y una persona adulta de tu confianza está presente. ¿Es una excepción de salud?", "Sí", "Se explica antes y hay un adulto de confianza presente."),
    ],
    Z=[
        ex("Un desconocido dice que si no mandas la foto, le contará algo a todos. ¿Qué haces?", "No respondo y se lo cuento a un adulto de confianza", "Es una amenaza y hay que pedir ayuda."),
        ex("Un niño dice: «No se lo cuento a nadie porque me da vergüenza». ¿Qué le dices?", "Que contarlo a un adulto de confianza es lo correcto", "La vergüenza no debe impedir pedir ayuda."),
    ],
    D=[
        arith("En una lista de 12 datos, 5 son información personal que no se comparte. ¿Cuántos se pueden compartir con seguridad?", "12-5", "Se restan los datos privados del total."),
        ex("Tres frases: A) «Mi clave es secreta». B) «Doy mi dirección a todos en el juego». C) «Aviso a un adulto si algo me asusta». ¿Cuáles protegen a la persona?", "A y C", "La B comparte información personal."),
    ],
    context=[ex("En un chat, un desconocido pregunta a Ana dónde vive y a qué hora sale del colegio. Ana no responde y le cuenta a su tía. ¿Cuidó su información?", "Sí", "No compartió datos y pidió ayuda a una persona adulta.")],
    selfcheck=[ex("En Orientación: ¿tu cuerpo y tu intimidad son tuyos?", "Sí", "Nadie puede tocarte si no quieres."), ex("¿Se comparte la dirección con desconocidos?", "No", "Pone en riesgo tu seguridad."), ex("¿Puedes pedir ayuda a un adulto aunque te dé vergüenza?", "Sí", "Siempre puedes pedir ayuda.")],
    task=T("Lee: Eli juega en línea. Un jugador le pide su nombre completo, su dirección y que le mande una foto. Escribe qué le responde Eli, qué guarda y a qué persona adulta de confianza le cuenta. Después escribe una regla de tres puntos para cuidar la información personal.", "Eli no responde y guarda el mensaje. Se lo cuenta a su tía. Reglas: no compartir dirección, no compartir claves, avisar si algo asusta.", ["no comparte datos", "guarda el mensaje y avisa a un adulto", "escribe tres reglas"], ["texto escrito o dicho"], ["compartir datos por juego", "no contar a un adulto"], "Reconoce la decisión y revisa que las reglas protejan la información."),
    reinforce="Haz una lista de cuatro datos que no se comparten con desconocidos.",
    extend="Escribe una frase firme para decir «no» a quien pide información personal.",
)

lesson(
    OA5, 5,
    "Una hoja y un lápiz. Los casos con personajes están escritos en los ejercicios. Nadie debe contar experiencias propias.",
    "Aprenderé a aplicar cuatro pasos ante una situación de riesgo: parar, alejarme, contar y seguir contando. Sirve para protegerme del abuso y del consumo de drogas.",
    ["Conozco límites e intimidad.", "Sé que no es mi culpa si alguien me hace daño."],
    [
        "Hay situaciones que pueden ser un riesgo: que alguien toque tu cuerpo de una forma que te incomoda, que te pida guardar un secreto que da miedo, que te ofrezca cigarrillos, alcohol u otra droga, o que te presione para hacer algo que no quieres. Quien te presiona puede ser alguien conocido o un desconocido. Siempre es responsabilidad de quien hace el daño, no tuya.",
        "Los cuatro pasos son: parar, alejarse, contar y seguir contando. Parar es decir «no» con voz firme: «No, no quiero». Alejarse es irte a un lugar seguro, cerca de otras personas. Contar es decírselo a una persona adulta de confianza. Seguir contando es insistir con otra persona adulta si la primera no te escucha o no te cree. Si el problema es con alguien de tu casa, cuéntalo a otra persona adulta de confianza, como tu profesora o la orientadora.",
        "Si te ofrecen un cigarrillo, alcohol o una pastilla que no te dio un adulto de tu casa, la respuesta es «no, gracias», alejarte y contarlo. Los medicamentos solo los da una persona adulta. Haz una lista de tres adultos de confianza. Así sabrás a quién acudir. Contar no es acusar: es pedir ayuda para que estés a salvo.",
    ],
    [("riesgo", "situación en que puedo sufrir un daño"), ("parar", "decir no con voz firme"), ("alejarse", "irme a un lugar seguro"), ("seguir contando", "contarlo a otro adulto si el primero no me ayuda"), ("droga", "sustancia que daña el cuerpo y la mente, como el alcohol o el tabaco")],
    [
        W("Los cuatro pasos", "Un compañero mayor te ofrece un cigarrillo. Ordena: A) contarlo a un adulto, B) decir «no, gracias», C) alejarte.", ["Primero se para con un no firme: B.", "Luego te alejas: C.", "Después lo cuentas: A."], "B, C, A"),
        W("Seguir contando", "Lola le contó a un adulto que alguien le pedía guardar un secreto que le daba miedo, pero no la escuchó. ¿Qué hace?", ["El primer adulto no ayudó.", "Hay otros adultos de confianza.", "Sigue contando a otro."], "Sigue contando a otro adulto de confianza"),
    ],
    [
        M("Guardar el secreto para no meter a nadie en problemas.", "Se cree que contar es acusar.", "Los secretos que dan miedo se cuentan siempre."),
        M("Dejar de contar si el primer adulto no me creyó.", "Se piensa que es culpa mía.", "Sigue contando a otra persona adulta de confianza."),
    ],
    R=[
        ex("¿Qué es parar?", "Decir no con voz firme", "Es el primer paso."),
        ex("Alejarse, ¿es irse a un lugar seguro, cerca de otras personas?", "Sí", "Así te proteges."),
        ex("Si el primer adulto no te cree, ¿puedes seguir contando a otro?", "Sí", "Debes insistir hasta que te ayuden."),
    ],
    U=[
        ex("¿Es tu culpa si alguien te presiona para hacer algo que no quieres?", "No", "La responsabilidad es de quien presiona."),
        ex("¿Contar un secreto que da miedo es acusar?", "No", "Es pedir ayuda para estar a salvo."),
        ex("¿Quién da los medicamentos?", "Solo una persona adulta", "Un niño no debe tomar pastillas que le dé otra persona."),
    ],
    A=[
        ex("Alguien te ofrece alcohol. ¿Qué frase es firme y clara: «No, gracias, no quiero» o «Bueno, solo un poquito»?", "«No, gracias, no quiero»", "Es corta y clara."),
        ex("Ordena los pasos: contar, parar, seguir contando, alejarse. Escribe las letras en orden correcto con P, A, C y S (parar, alejarse, contar, seguir contando).", "P, A, C, S", "Primero parar y luego alejarse, contar y seguir contando."),
        ex("Elige un lugar seguro para alejarte: «un rincón solo» o «cerca de la profesora y otros compañeros»", "Cerca de la profesora y otros compañeros", "Un lugar con personas protege más."),
    ],
    Z=[
        ex("Alguien dice: «Si cuentas, nadie te va a creer». ¿Qué haces?", "Cuento a una persona adulta de confianza y sigo contando", "Una amenaza no impide pedir ayuda."),
        ex("Un amigo te ofrece una pastilla que encontró. ¿Qué haces?", "No la tomo, me alejo y se lo cuento a un adulto", "No se toman pastillas que no da un adulto."),
    ],
    D=[
        arith("Eli escribió una lista con 3 adultos de confianza en su casa y 2 en la escuela. ¿Cuántos adultos tiene en su lista?", "3+2", "Se suman los de la casa y los de la escuela."),
        ex("Tres frases: A) «No, gracias, no quiero». B) «Mejor me quedo callado, así no hay problemas». C) «Me alejo y lo cuento». ¿Cuáles ayudan a protegerte?", "A y C", "La B no pide ayuda."),
    ],
    context=[ex("Un compañero mayor le ofrece un cigarrillo a Pablo. Pablo dice «no, gracias», se va con sus amigos y después se lo cuenta a su profesora. ¿Aplicó parar, alejarse y contar?", "Sí", "Usó los tres primeros pasos.")],
    selfcheck=[ex("En Orientación: ¿los pasos son parar, alejarse, contar y seguir contando?", "Sí", "Son los cuatro pasos."), ex("¿Es tu culpa si alguien te hace daño?", "No", "Nunca es tu culpa."), ex("¿Puedes pedir ayuda a más de un adulto?", "Sí", "Sigue contando hasta que te ayuden.")],
    task=T("Lee: Un niño mayor le dice a Ema que si no guarda un secreto sobre un toque que la incomodó, se enojará con ella. Escribe los cuatro pasos para Ema con una frase en cada uno y anota a tres adultos de confianza posibles (por ejemplo, un familiar, la profesora, la orientadora). No uses nombres reales.", "Parar: «No, no quiero». Alejarme: ir con la profesora. Contar: le cuento a mi tía. Seguir contando: si no me cree, le cuento a la orientadora.", ["escribe los cuatro pasos con una frase cada uno", "anota tres adultos de confianza", "no culpa a Ema"], ["texto escrito o dicho"], ["guardar el secreto", "no seguir contando"], "Reconoce los pasos y recuerda que Ema no tiene la culpa."),
    reinforce="Practica en voz alta una frase para decir «no» y escribe a quién contarías.",
    extend="Escribe cómo ayudarías a un amigo que te cuenta que alguien le hizo sentir miedo.",
)

# ================================================================ OA 06
lesson(
    OA6, 1,
    "Una hoja y un lápiz. Los casos de personajes están escritos en los ejercicios.",
    "Aprenderé a ponerme en el lugar del otro sin hablar por él y a respetar que piense distinto. Sirve para entender a mis compañeros y convivir mejor.",
    ["Sé reconocer emociones propias y ajenas.", "Sé que cada persona es distinta."],
    [
        "La empatía es entender cómo se puede sentir otra persona, poniéndote en su lugar. Para hacerlo, observa lo que pasó, piensa cómo te sentirías y pregunta. No puedes saber con certeza lo que otro siente. Por eso se dice «tal vez te sientas…» y se pregunta «¿cómo estás?». No hablas por el otro ni decides lo que debe sentir.",
        "Cada persona piensa y opina de manera distinta. Tienes derecho a decir tu opinión y los demás también. Respetar una opinión distinta no significa estar de acuerdo. Significa escuchar sin burlarte ni interrumpir. Puedes decir «yo lo veo distinto» con un buen trato.",
        "Cuando alguien necesita algo, la empatía te ayuda a decidir cómo ayudar. Primero escuchas, luego preguntas qué necesita y después actúas. La empatía no es sentir pena ni resolver todo por el otro. Es entender y acompañar con respeto.",
    ],
    [("empatía", "entender cómo se puede sentir otro, poniéndome en su lugar"), ("perspectiva", "la manera en que una persona ve una situación"), ("opinión", "lo que una persona piensa sobre algo"), ("respeto", "tratar bien al otro y aceptar que piensa distinto"), ("suponer", "creer algo sin haberlo comprobado")],
    [
        W("Preguntar y no suponer", "Nico llega callado a la sala. ¿Qué es más empático: «Estás enojado» o «Te veo callado, ¿cómo estás?»", ["No sabes con certeza lo que siente.", "La pregunta deja que Nico responda.", "La segunda frase es más empática."], "«Te veo callado, ¿cómo estás?»"),
        W("Opinión distinta", "Ana prefiere jugar al fútbol y Lola prefiere dibujar. Lola dice: «Yo lo veo distinto, pero entiendo tu idea». ¿Respetó la opinión de Ana?", ["No se burló ni interrumpió.", "Dijo lo suyo con buen trato.", "Respetó su opinión."], "Sí, la respetó"),
    ],
    [
        M("Decir «sé exactamente lo que sientes».", "Se supone lo que siente el otro.", "Dilo con cautela y pregunta: «¿Te sientes así?»"),
        M("Pensar que respetar una opinión es estar de acuerdo.", "Se confunde respetar con aceptar todo.", "Puedes pensar distinto y tratar bien al otro."),
    ],
    R=[
        ex("La empatía, ¿es entender cómo se puede sentir otro o decidir lo que siente?", "Entender cómo se puede sentir otro", "No se habla por el otro."),
        ex("¿Se puede saber con certeza lo que siente otra persona?", "No", "Por eso se pregunta."),
        ex("¿Todos tienen derecho a dar su opinión?", "Sí", "Cada persona puede expresarse."),
    ],
    U=[
        ex("¿Qué frase pregunta y no supone: «Estás triste» o «¿Cómo te sientes?»", "«¿Cómo te sientes?»", "Deja que el otro responda."),
        ex("¿Respetar una opinión distinta es estar de acuerdo?", "No", "Es escuchar y tratar bien aunque pienses distinto."),
        ex("¿Qué haces antes de ayudar a alguien: preguntar qué necesita o hacerlo todo por él?", "Preguntar qué necesita", "No se decide por el otro."),
    ],
    A=[
        ex("Eli perdió su lápiz favorito. ¿Qué frase es empática y no supone lo que siente: «Veo que buscas tu lápiz, ¿quieres ayuda?» o «Estás triste por una tontería»?", "«Veo que buscas tu lápiz, ¿quieres ayuda?»", "Describe lo que ve y pregunta."),
        ex("Pedro dice: «Yo creo que el recreo debe ser más largo». Tomás piensa distinto. ¿Qué dice Tomás con buen trato: «Yo lo veo distinto, pero te escucho» o «Qué idea más tonta»?", "«Yo lo veo distinto, pero te escucho»", "Expresa su opinión sin burlarse."),
        ex("Un compañero se cayó. ¿Qué es mejor: reírte o preguntarle «¿estás bien?»", "Preguntarle «¿estás bien?»", "Muestra interés por su estado."),
    ],
    Z=[
        ex("Un niño dice: «Tú no puedes sentir eso, no es para tanto». ¿Es empático?", "No", "Decide por el otro y le quita importancia."),
        ex("Dos niños piensan distinto sobre un juego y se enojan. ¿Qué puede ayudar: escuchar la idea del otro o insistir más fuerte?", "Escuchar la idea del otro", "Escuchar permite entender su perspectiva."),
    ],
    D=[
        arith("En una actividad, 24 estudiantes se juntan en parejas para practicar la escucha. ¿Cuántas parejas hay?", "24//2", "Se reparten 24 estudiantes de a dos."),
        ex("Tres frases: A) «Parece que te molestó, ¿es así?» B) «Estás mintiendo». C) «Yo lo veo distinto, pero te escucho». ¿Cuáles muestran empatía y respeto?", "A y C", "La B acusa y no pregunta."),
    ],
    context=[ex("En la clase, Lola dice que le gustó el cuento y Teo dice que no. La profesora pide: «Cada uno diga por qué, sin burlas». ¿Respeta el derecho a pensar distinto?", "Sí", "Permite opiniones distintas con buen trato.")],
    selfcheck=[ex("En Orientación: ¿puedes preguntar a alguien cómo se siente?", "Sí", "Eso muestra empatía."), ex("¿Se puede suponer lo que siente otro?", "No", "Hay que preguntar."), ex("¿Respetar es estar siempre de acuerdo?", "No", "Es escuchar y tratar bien.")],
    task=T("Lee: Rita se quedó sin pareja para el trabajo y se sienta sola. Escribe lo que ves, una frase empática que no suponga cómo se siente, una pregunta y una forma de ayudar si ella lo acepta. Después escribe cómo dirías que piensas distinto si no estás de acuerdo con una idea del grupo, con buen trato.", "Veo que Rita está sola. «Te veo sola, ¿cómo estás?». Puedo ofrecerle trabajar conmigo. Pensar distinto: «Yo lo veo distinto, pero te escucho».", ["describe lo que ve", "usa una pregunta y no una afirmación", "expresa una opinión distinta con buen trato"], ["texto escrito o dicho"], ["suponer lo que siente", "hablar por el otro"], "Reconoce la empatía y revisa que no se hable por la otra persona."),
    reinforce="Escribe tres frases que preguntan cómo se siente alguien sin suponer.",
    extend="Escribe una situación en que pienses distinto de un compañero y cómo lo dirías con respeto.",
)

lesson(
    OA6, 2,
    "Una hoja y un lápiz. Las listas de conductas están escritas en los ejercicios.",
    "Aprenderé a practicar un buen trato que se pueda observar y a cuidar el ambiente de aprendizaje de mi sala. Sirve para que todos podamos aprender en paz.",
    ["Sé saludar y agradecer.", "Sé esperar mi turno."],
    [
        "El buen trato es tratar a los demás con respeto y cariño. Se puede observar en conductas concretas: saludar al llegar, despedirse al irse, pedir las cosas por favor, dar las gracias, esperar el turno, hablar con un tono tranquilo y mirar a quien te habla. El buen trato no depende de si el otro te cae bien o mal: se aplica con todos.",
        "El ambiente de aprendizaje es el clima de la sala donde estudiamos. Se cuida cuando llegamos a la hora, escuchamos cuando alguien habla, levantamos la mano para opinar, usamos los materiales con cuidado y mantenemos la sala ordenada. Gritar, interrumpir, tirar cosas o quitar materiales lo daña. Cuando el ambiente es bueno, todos aprenden mejor.",
        "Un buen trato se puede comprobar con una lista. Si la conducta se ve, se oye o se puede contar, es observable. «Ser amable» es una idea. «Saludar con una sonrisa al llegar» es una conducta. Así podemos decir con claridad qué hacemos y qué podemos mejorar.",
    ],
    [("buen trato", "tratar a otros con respeto y cariño"), ("conducta observable", "algo que se ve o se oye y se puede contar"), ("ambiente de aprendizaje", "clima de la sala donde estudiamos"), ("turno", "momento que me toca hablar o hacer algo"), ("tono", "la manera en que sueno al hablar")],
    [
        W("Conducta observable", "¿Cuál es una conducta observable: «ser amable» o «saludar con una sonrisa al llegar»?", ["Una conducta se puede ver.", "«Ser amable» es una idea.", "Saludar con una sonrisa se puede contar."], "«Saludar con una sonrisa al llegar»"),
        W("Contar el buen trato", "En una mañana, Pía saludó 4 veces, dijo gracias 3 veces y pidió por favor 5 veces. ¿Cuántas conductas de buen trato hubo?", ["Se suman las tres cantidades.", "4 + 3 + 5.", "El total cuenta las conductas."], "12 conductas"),
    ],
    [
        M("Pensar que el buen trato es solo con quienes me caen bien.", "Se confunde el buen trato con la amistad.", "Se trata bien a todos, aunque no sean mis amigos."),
        M("Creer que gritar es solo ser divertido.", "No se mira cómo afecta al curso.", "Los gritos dañan el ambiente de aprendizaje."),
    ],
    R=[
        ex("Saludar al llegar, ¿es una conducta de buen trato?", "Sí", "Se puede ver y muestra respeto."),
        ex("Decir por favor y gracias, ¿es buen trato?", "Sí", "Son palabras de respeto."),
        ex("Interrumpir a quien habla, ¿cuida el ambiente de aprendizaje?", "No", "Lo daña mucho."),
    ],
    U=[
        ex("¿Por qué «ser amable» no es una conducta observable?", "Porque es una idea y no una acción que se vea", "No dice qué hacer."),
        ex("¿Se trata bien solo a los amigos?", "No", "El buen trato es con todos."),
        ex("¿Qué cuida el ambiente de aprendizaje: levantar la mano para opinar o gritar?", "Levantar la mano para opinar", "Permite que se escuche a todos."),
    ],
    A=[
        arith("Una mañana, Dino saludó 3 veces, dijo gracias 4 veces y esperó su turno 5 veces. ¿Cuántas conductas de buen trato hubo?", "3+4+5", "Se suman las tres cantidades."),
        ex("¿Cuál es una conducta observable para «ser respetuoso»: «esperar mi turno para hablar» o «tener buen corazón»?", "«Esperar mi turno para hablar»", "Es una acción que se ve; «tener buen corazón» es una idea."),
        ex("De cuatro conductas: saludar, gritar, esperar el turno y quitar un lápiz, ¿cuántas cuidan el ambiente de aprendizaje?", "2", "Saludar y esperar el turno lo cuidan; las otras lo dañan."),
    ],
    Z=[
        ex("Un niño dice: «Pido por favor solo a la profesora, no a mis compañeros». ¿Es buen trato?", "No", "El buen trato es con todos."),
        ex("Una niña dice: «Yo soy simpática, no necesito hacer nada más». ¿Qué le falta para que sea observable?", "Una conducta que se vea, como saludar o esperar el turno", "«Simpática» es una idea."),
    ],
    D=[
        arith("En una semana de 5 días, un curso de 30 estudiantes se saluda al entrar. Si cada estudiante saluda a la profesora una vez al día, ¿cuántos saludos hay en la semana?", "30*5", "Es 30 saludos repetidos 5 días."),
        ex("Lista de conductas: (a) llegar a la hora, (b) tirar papeles, (c) escuchar sin interrumpir, (d) dejar la sala ordenada. ¿Cuántas cuidan el ambiente de aprendizaje?", "3", "Las (a), (c) y (d) lo cuidan."),
    ],
    context=[ex("Al entrar a la sala, Tomás saluda, deja sus cosas ordenadas y espera su turno para hablar. ¿Practicó buen trato observable?", "Sí", "Tiene conductas concretas que se ven.")],
    selfcheck=[ex("En Orientación: ¿saludar y despedirse es buen trato?", "Sí", "Muestra respeto siempre."), ex("¿Una conducta observable se puede ver o contar?", "Sí", "Por eso se puede comprobar."), ex("¿Gritar en clase cuida el ambiente?", "No", "Afecta a todo el curso.")],
    task=T("Crea una lista de cinco conductas de buen trato para tu sala, cada una observable (por ejemplo, saludar con una sonrisa). Anota si las cumplirías todos los días, a veces o todavía no, y qué harías para mejorar una de ellas. No evalúes a otros compañeros por su nombre.", "1) Saludar al llegar: todos los días. 2) Pedir por favor: a veces. Para mejorar: usar «por favor» cuando pida un lápiz.", ["escribe cinco conductas observables", "se evalúa a sí mismo", "propone una mejora"], ["lista escrita"], ["escribir ideas y no conductas", "evaluar a otros por su nombre"], "Reconoce cada conducta observable y pregunta cómo la comprobarían."),
    reinforce="Escribe tres conductas que cuidan el ambiente de aprendizaje.",
    extend="Propone una regla de curso para pedir turno que todos puedan cumplir.",
)

lesson(
    OA6, 3,
    "Una hoja y un lápiz. Los casos de personajes están escritos en los ejercicios.",
    "Aprenderé a ayudar a quien lo necesita sin hacer las cosas por él ni dejarlo mal. Sirve para actuar con solidaridad y respeto.",
    ["Sé que la empatía incluye preguntar.", "Sé practicar buen trato."],
    [
        "La solidaridad es ayudar a otros, especialmente a quien más lo necesita, y apoyar a quienes tienen una dificultad. Puede ser prestar un material, explicar un paso, acompañar a alguien que está solo o avisar a un adulto cuando alguien necesita ayuda. La solidaridad se hace con respeto y sin esperar nada a cambio.",
        "Para ayudar bien, sigue tres pasos. Primero, pregunta: «¿Quieres ayuda?» o «¿Qué necesitas?». Segundo, ofrece una ayuda que le sirva: a veces es hacer algo juntos, no hacerlo por el otro. Tercero, respeta si dice que no. Sustituir es hacer por el otro lo que él puede hacer, y eso le quita la oportunidad de aprender o decidir.",
        "Ayudar no es sentir pena ni dar órdenes. Tampoco se ayuda delante de todos para que nos feliciten. Cuando alguien necesita ayuda que va más allá de lo que puedes hacer, como una herida o una situación de peligro, avisa a un adulto. Pedir ayuda a un adulto también es solidaridad.",
    ],
    [("solidaridad", "ayudar a otros, especialmente a quien más lo necesita"), ("sustituir", "hacer por el otro lo que él puede hacer"), ("necesidad", "algo que alguien necesita para estar bien"), ("acompañar", "estar con alguien para que no se sienta solo"), ("autonomía", "poder hacer o decidir por uno mismo")],
    [
        W("Ayudar sin sustituir", "Dino no entiende un ejercicio de matemática. ¿Qué es mejor: hacerle toda la tarea o explicarle el primer paso y dejar que siga?", ["Hacer la tarea le quita la oportunidad de aprender.", "Explicar el primer paso lo apoya.", "Dejar que siga respeta su autonomía."], "Explicarle el primer paso y dejar que siga"),
        W("Preguntar antes", "Eli parece tener dificultad para abrir su mochila. ¿Qué dices primero: «Yo te la abro» o «¿Quieres ayuda?»", ["Antes de ayudar, se pregunta.", "Eli puede preferir hacerlo sola.", "Se pregunta primero."], "«¿Quieres ayuda?»"),
    ],
    [
        M("Hacerle la tarea al compañero porque a mí me sale más rápido.", "Se cree que ayudar es hacer por el otro.", "Ayuda a que pueda hacerlo él, paso a paso."),
        M("Ayudar solo si me van a felicitar.", "Se confunde ayudar con lucirse.", "La solidaridad no espera nada a cambio."),
    ],
    R=[
        ex("La solidaridad, ¿es ayudar a otros con respeto o hacer todo por ellos?", "Ayudar a otros con respeto", "No se sustituye al otro."),
        ex("Antes de ayudar, ¿se pregunta «¿quieres ayuda?»", "Sí", "Así se respeta lo que necesita."),
        ex("Si alguien dice que no necesita ayuda, ¿se respeta?", "Sí", "Cada uno decide si la quiere."),
    ],
    U=[
        ex("¿Qué es sustituir?", "Hacer por el otro lo que él puede hacer", "Le quita oportunidad de aprender."),
        ex("¿Se ayuda mejor delante de todos para que feliciten?", "No", "La solidaridad no busca lucirse."),
        ex("¿Avisar a un adulto cuando alguien necesita ayuda es solidaridad?", "Sí", "A veces la ayuda necesaria es de un adulto."),
    ],
    A=[
        ex("Rita se quedó sola en el recreo. ¿Qué frase acompaña preguntando primero: «¿Quieres jugar conmigo?» o «Tienes que jugar con nosotros»?", "«¿Quieres jugar conmigo?»", "Pregunta y ofrece compañía; la otra frase manda."),
        ex("Pedro no alcanzó a copiar la pizarra. ¿Qué ayuda no lo sustituye: «Te presto mi cuaderno unos minutos para que copies tú» o «Dame tu cuaderno, yo copio todo por ti»?", "«Te presto mi cuaderno unos minutos para que copies tú»", "Ayuda sin sustituir."),
        ex("Un compañero se cortó la mano en el patio. ¿Qué es lo más solidario: curarlo tú mismo o avisar a un adulto de inmediato?", "Avisar a un adulto de inmediato", "Una herida necesita ayuda adulta."),
    ],
    Z=[
        ex("Un niño dice: «Le hice la tarea para ayudarlo». ¿Fue una ayuda bien hecha?", "No", "Sustituyó al compañero."),
        ex("Una niña ofreció ayuda y el compañero dijo «no, gracias». Ella insistió. ¿Respetó?", "No", "Debe aceptar el no."),
    ],
    D=[
        arith("Para una campaña solidaria, cada uno de los 28 estudiantes de un curso escribe 4 cartas de ánimo. ¿Cuántas cartas escriben en total?", "28*4", "Se repiten 4 cartas por cada uno de los 28."),
        ex("Tres ayudas: A) «¿Quieres que te explique?». B) «Dame, yo lo hago». C) «Te acompaño a ver a la profesora». ¿Cuáles son solidarias y respetuosas?", "A y C", "La B sustituye."),
    ],
    context=[ex("Joaquín vio que Ema no podía alcanzar un libro. Le preguntó «¿te ayudo?», y cuando ella dijo sí, se lo bajó. ¿Fue una ayuda respetuosa?", "Sí", "Preguntó antes y respetó su respuesta.")],
    selfcheck=[ex("En Orientación: ¿ayudar es sustituir al otro?", "No", "Es acompañar sin quitarle autonomía."), ex("¿Se pregunta antes de ayudar?", "Sí", "Así se respeta."), ex("¿Se ayuda para recibir aplausos?", "No", "La solidaridad no busca lucirse.")],
    task=T("Lee tres casos: A) un compañero no entiende un ejercicio, B) alguien está solo en el recreo, C) un compañero se cayó y le sangra la rodilla. Para cada caso escribe qué dirías y qué harías, si preguntarías primero y si avisarías a un adulto.", "A) «¿Quieres que te explique el primer paso?» B) «¿Quieres jugar?» C) Aviso de inmediato a la profesora y me quedo con él.", ["pregunta antes de ayudar en A y B", "avisa a un adulto en C", "no hace por el otro lo que puede hacer"], ["texto escrito o dicho"], ["sustituir al otro", "no avisar a un adulto cuando hay peligro"], "Reconoce las preguntas y revisa que la ayuda respete la autonomía."),
    reinforce="Escribe tres frases que ofrezcan ayuda preguntando primero.",
    extend="Piensa en una necesidad de tu curso y escribe una acción solidaria que puedan hacer entre todos.",
)

lesson(
    OA6, 4,
    "Una hoja y un lápiz. Los casos de personajes están escritos en los ejercicios. No se comparten experiencias propias ni nombres reales.",
    "Aprenderé a reconocer la violencia y la discriminación y a rechazarlas con seguridad. Sirve para proteger a quien lo necesita y para no sumarme a daños.",
    ["Conozco el buen trato.", "Sé que nadie merece que lo lastimen."],
    [
        "La violencia es cualquier acción que daña a otra persona, por la fuerza, por palabras o por exclusión. Puede ser un golpe, un insulto, una amenaza, un rumor, un mensaje que humilla o dejar a alguien afuera a propósito. La violencia no es un simple desacuerdo entre iguales: quien la sufre se siente asustado, humillado o sin poder defenderse.",
        "La discriminación es tratar peor a una persona por ser distinta, por ejemplo por su etnia, su género, su religión, su nacionalidad u otra característica. Decir que «las niñas no sirven para el fútbol», burlarse del acento de alguien o dejar de lado a un niño por su religión es discriminar. Todas las personas tienen los mismos derechos y merecen respeto.",
        "Si ves violencia o discriminación, puedes: decir con firmeza «basta, eso no está bien», no sumarte ni reírte, apoyar a quien la sufre y avisar a un adulto. Si estás en peligro, avisa de inmediato. No tienes que enfrentar solo una situación grave. Y si eres tú quien la sufre, no es tu culpa y puedes pedir ayuda sin esperar que el daño pase.",
    ],
    [("violencia", "acción que daña a otra persona de forma física, verbal o emocional"), ("discriminación", "tratar peor a alguien por ser distinto"), ("etnia", "grupo de personas con una cultura y origen compartidos"), ("exclusión", "dejar a alguien fuera a propósito"), ("derecho", "algo que toda persona merece")],
    [
        W("Reconocer discriminación", "Un grupo no deja jugar a Lola porque su familia es de otro país. ¿Es discriminación?", ["La están tratando peor por su nacionalidad.", "Eso afecta sus derechos.", "Sí, es discriminación."], "Sí, es discriminación"),
        W("Qué hacer", "Tres niños se ríen de un apodo ofensivo. ¿Qué puede hacer un compañero: unirse a la risa o decir «basta, eso no está bien» y apoyar al niño?", ["Reírse apoya la burla.", "Decir basta y apoyar protege.", "Elige la segunda."], "Decir «basta, eso no está bien» y apoyar al niño"),
    ],
    [
        M("Pensar que la violencia es lo mismo que una discusión entre iguales.", "Se mira solo que ambos están enojados.", "En la violencia hay daño o miedo y alguien no puede defenderse."),
        M("Reírme de una burla porque «no hago nada».", "Se cree que mirar no importa.", "Reírse apoya la burla; di «basta» o avisa a un adulto."),
    ],
    R=[
        ex("Un golpe, un insulto o una amenaza, ¿son violencia?", "Sí", "Dañan a otra persona."),
        ex("Dejar a alguien afuera a propósito, ¿puede ser violencia?", "Sí", "Es exclusión que daña."),
        ex("Tratar peor a alguien por su religión, ¿es discriminación?", "Sí", "Se trata distinto por ser diferente."),
    ],
    U=[
        ex("¿La violencia es solo golpear?", "No, también hay insultos, amenazas y exclusión", "Puede ser física, verbal o emocional."),
        ex("¿Qué diferencia hay entre un desacuerdo y la violencia?", "En la violencia hay daño o miedo y alguien no puede defenderse", "En un desacuerdo, ambos pueden opinar sin miedo."),
        ex("Si te discriminan, ¿es tu culpa?", "No", "La responsabilidad es de quien discrimina."),
    ],
    A=[
        ex("Un niño dice: «Las niñas no pueden jugar fútbol». ¿Es discriminación por género?", "Sí", "Trata peor a alguien por ser niña."),
        ex("Un compañero se burla del acento de un niño que llegó de otro país. ¿Qué frase detiene la burla: «Basta, eso no está bien» o «Jaja, es verdad que habla raro»?", "«Basta, eso no está bien»", "Es firme, corta y rechaza la burla."),
        ex("Cuatro conductas: golpear, insultar, invitar a jugar y compartir el material. ¿Cuántas son violencia?", "2", "Golpear e insultar dañan; las otras cuidan."),
    ],
    Z=[
        ex("Un niño dice: «Es solo una broma, no pasa nada». ¿Cómo sabes si dañó?", "Mirando cómo se siente la persona", "El impacto es lo que importa."),
        ex("Un compañero amenaza a otro y te pide que no cuentes nada. ¿Qué haces?", "Aviso a un adulto de confianza", "La violencia no debe quedar en secreto."),
    ],
    D=[
        arith("En un juego de casos hay 14 situaciones. 9 son violencia o discriminación y las demás son desacuerdos. ¿Cuántas son desacuerdos?", "14-9", "Se restan las de violencia del total."),
        ex("Tres frases: A) «Todos tenemos los mismos derechos». B) «Mis compañeros de otro país no pueden jugar». C) «Si veo discriminación, aviso a un adulto». ¿Cuáles rechazan la discriminación?", "A y C", "La B discrimina."),
    ],
    context=[ex("En el patio, unos niños dicen que un compañero no puede participar por su religión. Marta dice: «Basta, todos pueden jugar» y avisa a la profesora. ¿Rechazó la discriminación?", "Sí", "Se opuso con firmeza y pidió ayuda.")],
    selfcheck=[ex("En Orientación: ¿la discriminación puede ser por etnia, género, religión o nacionalidad?", "Sí", "Son algunas razones."), ex("¿Reírse de una burla ayuda?", "No", "La apoya sin querer."), ex("¿Puedes avisar a un adulto si ves violencia?", "Sí", "Es lo recomendado.")],
    task=T("Lee: unos niños no dejan jugar a Teo porque es de otro país y se ríen de su acento. Escribe qué es violencia o discriminación en este caso, una frase firme para detenerla, cómo apoyarías a Teo y a qué adulto avisarías. No uses nombres reales.", "Es discriminación por nacionalidad. Frase: «Basta, eso no está bien». Apoyo: invitar a Teo a jugar. Aviso a mi profesora.", ["identifica la discriminación", "escribe una frase firme", "apoya a Teo y avisa a un adulto"], ["texto escrito o dicho"], ["justificar la burla", "enfrentar solo una situación grave"], "Reconoce la discriminación y revisa que se avise a un adulto."),
    reinforce="Escribe dos frases firmes para detener una burla o una exclusión.",
    extend="Escribe una regla de curso que proteja a todos de la discriminación.",
)

lesson(
    OA6, 5,
    "Una hoja y un lápiz. Los casos de personajes están escritos en los ejercicios.",
    "Aprenderé a incluir a otros y a reparar un daño con seguridad. Sirve para que todos tengan un lugar en el curso y para recuperar la confianza.",
    ["Conozco la solidaridad.", "Sé que debo rechazar la violencia."],
    [
        "Incluir es invitar a alguien a participar y adaptar el juego o el trabajo para que pueda hacerlo. Por ejemplo, ofrecer un lugar en el equipo, explicar las reglas con calma o cambiar una regla para que todos puedan jugar. La inclusión también respeta el derecho de cada uno a opinar y a pensar distinto, sin burlas ni presión.",
        "Reparar es hacerse cargo cuando dañamos a alguien. Tiene cuatro pasos: reconocer lo que hice, decir lo siento, preguntar qué necesita el otro y hacer algo concreto para arreglarlo, como devolver algo, ayudar a rehacer un trabajo o invitarlo a jugar. La reparación no se fuerza: la otra persona decide si acepta, y puede necesitar tiempo.",
        "Hay situaciones en que no debes reparar solo. Si hubo golpes, amenazas o miedo, avisa a un adulto y no intentes resolverlo a solas. Nadie está obligado a reconciliarse con quien lo lastimó. Primero se protege a la persona dañada y después se repara con ayuda de un adulto.",
    ],
    [("inclusión", "invitar y adaptar para que todos puedan participar"), ("reparar", "hacerme cargo de un daño y arreglarlo"), ("adaptar", "cambiar algo para que todos puedan participar"), ("acuerdo", "decisión que aceptan las personas involucradas"), ("reconciliarse", "volver a llevarse bien después de un conflicto")],
    [
        W("Incluir", "Un grupo juega a las escondidas y Mía, que usa muletas, quiere jugar. ¿Qué pueden hacer: decirle que no puede o adaptar el juego, por ejemplo con lugares cercanos?", ["Mía tiene derecho a participar.", "Adaptar permite que todos jueguen.", "Se adapta el juego."], "Adaptar el juego para que todos puedan participar"),
        W("Reparar", "Teo rompió sin querer el dibujo de Ana. Ordena: A) preguntar qué necesita Ana, B) reconocer lo que hizo, C) hacer algo concreto, D) decir lo siento.", ["Primero se reconoce: B.", "Luego se pide perdón: D.", "Después se pregunta y se repara: A, C."], "B, D, A, C"),
    ],
    [
        M("Obligar a alguien a perdonar de inmediato.", "Se cree que reparar es lo mismo que reconciliarse.", "La otra persona decide y puede necesitar tiempo."),
        M("Resolver solo una situación con golpes o amenazas.", "Se piensa que avisar es acusar.", "Avisa a un adulto; la seguridad es lo primero."),
    ],
    R=[
        ex("Incluir, ¿es invitar a participar o dejar afuera?", "Invitar a participar", "Todos tienen derecho a participar."),
        ex("¿Reparar es hacerse cargo de un daño?", "Sí", "Incluye arreglarlo después."),
        ex("¿Se puede forzar a alguien a perdonar?", "No", "Cada persona decide."),
    ],
    U=[
        ex("¿Qué significa adaptar un juego?", "Cambiarlo para que todos puedan participar", "Facilita la inclusión."),
        ex("Si hubo golpes, ¿conviene resolverlo solo o avisar a un adulto?", "Avisar a un adulto", "Primero se protege a las personas."),
        ex("¿Respetar una opinión distinta es parte de la inclusión?", "Sí", "Todos tienen derecho a opinar."),
    ],
    A=[
        ex("Ordena con letras los pasos de la reparación: pedir perdón (P), reconocer lo que hice (R), hacer algo concreto (C), preguntar qué necesita (N).", "R, P, N, C", "Primero se reconoce y luego se repara."),
        ex("Una niña nueva no conoce las reglas del juego. ¿Qué frase la incluye: «¿Quieres jugar con nosotros? Te explico las reglas» o «No sabes jugar, mejor mira»?", "«¿Quieres jugar con nosotros? Te explico las reglas»", "Invita y explica."),
        ex("Pedro escondió el lápiz de Eli. ¿Qué acción concreta repara el daño: devolver el lápiz y pedir perdón, o decir que fue una broma y no hacer nada?", "Devolver el lápiz y pedir perdón", "Arregla lo que hizo."),
    ],
    Z=[
        ex("Un niño dice: «Pedí perdón, así que ya me tienen que perdonar». ¿Es correcto?", "No", "El otro decide cuándo y si perdona."),
        ex("En un grupo dicen «Esa idea es tonta» a una compañera que opina distinto. ¿Es inclusivo?", "No", "No respetan su derecho a opinar."),
    ],
    D=[
        arith("En una actividad hay 30 estudiantes y se arman equipos de 5 para jugar de forma inclusiva. ¿Cuántos equipos hay?", "30//5", "Se reparten 30 estudiantes en grupos de 5."),
        ex("Tres frases: A) «Te dejo un lugar en el equipo». B) «Perdónanos ya». C) «Lo siento, ¿qué necesitas?». ¿Cuáles incluyen o reparan sin forzar?", "A y C", "La B fuerza el perdón."),
    ],
    context=[ex("Luis empujó a un compañero y le dijo «lo siento, te empujé sin querer, ¿estás bien?». Luego avisó a la profesora. El compañero dijo que necesitaba tiempo, y Luis lo respetó. ¿Reparó con respeto?", "Sí", "Se hizo cargo y respetó su tiempo.")],
    selfcheck=[ex("En Orientación: ¿incluir es invitar a participar?", "Sí", "Todos tienen un lugar."), ex("¿Reparar es obligar a perdonar?", "No", "El otro decide."), ex("¿Puedes avisar a un adulto si hay miedo?", "Sí", "Primero se protege a las personas.")],
    task=T("Elige un caso: A) una compañera que usa silla de ruedas quiere jugar a las escondidas, B) un niño nuevo no conoce el juego, C) rompiste sin querer el trabajo de un compañero. Para A o B escribe cómo incluirías con una frase y un cambio al juego. Para C escribe los cuatro pasos de la reparación. Anota quién sería el adulto de apoyo.", "A) «Juega con nosotros». Cambio: lugares cercanos. C) Reconozco, digo lo siento, pregunto qué necesita, le ayudo a rehacerlo. Adulto: mi profesora.", ["incluye con una frase y un cambio", "repara con los cuatro pasos", "no fuerza el perdón"], ["texto escrito o dicho"], ["obligar a perdonar", "resolver solo una situación de violencia"], "Reconoce la inclusión y revisa que la reparación no obligue al otro."),
    reinforce="Escribe una frase para invitar a alguien a un juego y una regla que pueda adaptarse.",
    extend="Escribe cómo repararías un daño a un compañero en cuatro pasos y qué harías si no quiere hablar.",
)
