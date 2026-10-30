"""Student material for 1.º básico Educación Física y Salud, OA 06 (actividad moderada a vigorosa), OA 07 (actividad cotidiana y juegos tradicionales) y OA 08 (respuestas corporales)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


OA6, OA7, OA8 = "EF01 OA 06", "EF01 OA 07", "EF01 OA 08"

SCALE = ("Escala del habla: 1 = puedo cantar; 2 = puedo conversar fácil; 3 = hablo con frases cortas (esfuerzo moderado); "
         "4 = solo digo palabras sueltas (esfuerzo vigoroso); 5 = no puedo hablar (debo parar y descansar).")

# ---------------------------------------------------------------- OA 06
register(
    OA6, 1,
    materials="Espacio de 4 × 4 m, reloj con segundos, agua para beber y zapatillas amarradas. La escala del habla está escrita en esta clase.",
    use="Aprenderé a calentar el cuerpo de a poco antes de jugar fuerte. Sirve para no cansarme de golpe y para cuidar mis músculos y mi corazón.",
    prior=["Sé caminar, trotar suave y saltar con control.", "Sé mirar el reloj."],
    explain=[
        "Activar el cuerpo progresivamente significa empezar suave y subir el esfuerzo poco a poco. Primero caminas, después trotas suave, luego saltas más y recién después juegas con más fuerza. Así tu corazón, tus pulmones y tus músculos se preparan.",
        "Para saber cuánto esfuerzo haces, usa la escala del habla. " + SCALE + " En esta clase quedarás entre los niveles 1 y 3.",
        "No partas al máximo. Si partes muy fuerte, te cansas rápido y puedes lastimarte. Después de cada tramo bebe unos sorbos de agua si tienes sed. Si te mareas, te duele algo o no puedes hablar, paras y avisas a un adulto.",
    ],
    vocab=[("progresivo", "poco a poco, de menos a más"), ("calentar", "preparar el cuerpo antes de jugar fuerte"), ("esfuerzo", "cuánto trabaja mi cuerpo"), ("moderado", "esfuerzo en que puedo hablar frases cortas"), ("vigoroso", "esfuerzo fuerte en que solo digo palabras sueltas")],
    worked=[
        W("Calentamiento de 4 tramos", "Haces 4 tramos de 20 segundos de acción y 20 de pausa: caminar, trote suave, saltos suaves y trote. ¿Cuántos segundos de acción haces?", ["Cada tramo tiene 20 segundos de acción.", "Son 4 tramos: 20 × 4.", "20 × 4 = 80."], "80 segundos de acción."),
        W("Usar la escala", "Trotas y puedes decir «estoy trotando» pero no cantar. ¿Qué número de la escala es?", ["No puedo cantar, así que no es 1.", "Puedo hablar frases cortas.", "Eso corresponde al 3."], "Nivel 3, esfuerzo moderado."),
    ],
    mistakes=[M("Partir corriendo al máximo.", "Se piensa que más fuerte es mejor.", "Empieza caminando y sube poco a poco."),
              M("No beber agua aunque haya sed.", "Se quiere seguir jugando.", "Toma unos sorbos de agua entre tramos.")],
    tiers={
        "recovery": [
            ex("Calentar significa preparar el cuerpo de ¿menos a más o de más a menos?", "De menos a más", "Se sube el esfuerzo poco a poco."),
            ex("En el primer tramo del calentamiento, ¿caminas o saltas fuerte?", "Caminas", "Se empieza suave."),
            ex("Si tienes sed entre tramos, ¿qué haces?", "Bebes unos sorbos de agua", "El agua repone lo que pierdes."),
        ],
        "understand": [
            ex("En la escala del habla, ¿qué número es «puedo cantar»?", "1", "Es el esfuerzo más suave."),
            ex("Dices solo palabras sueltas al correr. ¿Qué nivel es?", "4", "Es esfuerzo vigoroso."),
            ex("¿Por qué no se parte al máximo?", "Para no cansarse de golpe ni lastimarse", "El cuerpo necesita prepararse."),
        ],
        "apply": [
            arith("Haces 4 tramos de 20 segundos de acción. ¿Cuántos segundos son en total?", "4*20", "Se multiplican tramos por segundos.", " segundos"),
            ex("Orden de tramos: caminar, trote suave, saltos suaves, trote. ¿Cuál es el tercero?", "Saltos suaves", "Está en el tercer lugar."),
            arith("Cada tramo tiene 20 de acción y 20 de pausa. ¿Cuántos segundos dura todo el calentamiento de 4 tramos?", "(20+20)*4", "Cada tramo incluye acción y pausa.", " segundos"),
        ],
        "reason": [
            ex("Beto parte corriendo al máximo y a los 10 segundos solo dice «ya… no… puedo». ¿Qué nivel de la escala alcanzó?", "5", "No puede hablar: debe parar."),
            ex("Ana trota y puede conversar con facilidad. ¿Qué debería hacer para llegar a esfuerzo moderado: ir un poco más rápido o quedarse igual?", "Ir un poco más rápido", "Conversar fácil es nivel 2; el moderado es 3."),
        ],
        "challenge": [
            ex("Un calentamiento de 4 tramos tuvo estos niveles de la escala, en orden: 1, 2, 2, 3. ¿Cuántos tramos estuvieron por debajo del nivel 3?", "3", "1, 2 y 2 son menores que 3."),
            arith("Un calentamiento de 80 segundos y un juego de 120 segundos. ¿Cuántos segundos son juntos?", "80+120", "Se suman los dos tiempos.", " segundos"),
        ],
    },
    context=[ex("Llegas al recreo y tus amigos quieren jugar a pillarse de inmediato. Hace frío. ¿Qué haces primero: A) corres al máximo, B) caminas y trotas suave 1 minuto, C) te sientas?", "B", "Calentar de a poco prepara el cuerpo.")],
    selfcheck=[
        ex("¿Qué significa «progresivo»?", "Poco a poco", "Sube de menos a más."),
        ex("¿Qué nivel de la escala es «puedo hablar frases cortas»?", "3", "Es esfuerzo moderado."),
        ex("Si no puedes hablar, ¿sigues o paras?", "Paras", "Es nivel 5."),
    ],
    open_task=task("Con reloj y un espacio de 4 × 4 m, haz 4 tramos de 20 segundos de acción con 20 de pausa: 1) caminar, 2) trote suave en el lugar, 3) saltos suaves, 4) trote suave. Al terminar cada tramo, di en qué número de la escala del habla estabas (1 a 5) y bebe un sorbo de agua si tienes sed. " + SCALE,
                   "Tramo 1: nivel 1. Tramo 2: nivel 2. Tramo 3: nivel 2. Tramo 4: nivel 3. Terminé en 3, bebí agua y pude decir frases cortas.",
                   ["sube el esfuerzo de a poco", "usa la escala del habla", "respeta las pausas"],
                   ["tabla con 4 niveles", "observación de un adulto", "relato oral"],
                   ["partir al máximo", "no usar la escala", "ignorar la pausa"],
                   "Reconoce que subió el esfuerzo gradualmente y pide explicar cómo supo su nivel."),
    reinforce="Camina 30 segundos y trota suave 20 segundos, contando en voz alta.",
    extend="Diseña un calentamiento de 5 tramos con niveles 1, 2, 2, 3, 3 y explica por qué ese orden.",
)

register(
    OA6, 2,
    materials="Un circuito de 4 estaciones marcado con conos, botellas vacías o zapatos, una cuerda en el suelo, un reloj y agua. Espacio de 4 × 4 m.",
    use="Aprenderé a mantener un esfuerzo moderado durante varios minutos con buena técnica. Sirve para mejorar mi condición física jugando.",
    prior=["Sé usar la escala del habla.", "Sé calentar de a poco."],
    explain=[
        "Un circuito continuo es un recorrido de estaciones donde te mueves varias veces sin parar mucho. Hoy las estaciones son: 1) trote suave rodeando un cono, 2) saltos con dos pies sobre una cuerda en el suelo, 3) caminar rápido de lado (pasos laterales) y 4) saltos de tijera suaves en el lugar. Cada estación dura 30 segundos de acción y 30 de pausa.",
        "Moderado significa nivel 3 de la escala del habla: puedes decir frases cortas. Si estás en 4, baja un poco la velocidad. " + SCALE + " La técnica es más importante que la velocidad: rodillas dobladas al saltar, mirada al frente y espalda recta.",
        "Para completar el circuito, anota cuántas vueltas haces. Una vuelta es pasar por las 4 estaciones. Camina entre estaciones y cuida la distancia de dos brazos con los demás. Al final, camina 1 minuto para recuperarte.",
    ],
    vocab=[("circuito", "recorrido con estaciones"), ("continuo", "sin parar mucho"), ("técnica", "forma correcta de hacer un movimiento"), ("vuelta", "pasar por todas las estaciones una vez"), ("recuperar", "volver a respirar tranquilo")],
    worked=[
        W("Duración de una vuelta", "Una vuelta tiene 4 estaciones. Cada una tiene 30 segundos de acción y 30 de pausa. ¿Cuántos segundos dura una vuelta?", ["Una estación: 30 + 30 = 60.", "Cuatro estaciones: 60 × 4.", "60 × 4 = 240."], "240 segundos (4 minutos)."),
        W("Bajar el esfuerzo", "En el trote dices solo palabras sueltas. ¿Qué haces?", ["Estoy en nivel 4, demasiado fuerte para el circuito moderado.", "Bajo la velocidad al paso de trote suave.", "Compruebo que puedo decir frases cortas."], "Bajo la velocidad hasta nivel 3."),
    ],
    mistakes=[M("Saltar con las piernas rígidas.", "No se dobla la rodilla al caer.", "Dobla las rodillas en cada aterrizaje."),
              M("Correr entre estaciones.", "Se quiere terminar más rápido.", "Camina entre estaciones para recuperar.")],
    tiers={
        "recovery": [
            ex("Un circuito tiene ¿estaciones o un solo ejercicio?", "Estaciones", "Cada una tiene una acción."),
            ex("En el circuito, entre estaciones, ¿caminas o corres?", "Caminas", "Así te recuperas entre estaciones."),
            ex("Esfuerzo moderado es el nivel ¿3 o 5?", "3", "En 5 no puedes hablar."),
        ],
        "understand": [
            ex("¿Qué es una vuelta?", "Pasar por las 4 estaciones", "Cada estación se hace una vez."),
            ex("Si estás en nivel 4, ¿subes o bajas la velocidad?", "Bajas", "Hoy se trabaja nivel 3."),
            ex("¿Qué importa más: la técnica o ser el más rápido?", "La técnica", "Una buena técnica evita lesiones."),
        ],
        "apply": [
            arith("Una estación dura 30 de acción y 30 de pausa. ¿Cuántos segundos dura?", "30+30", "Se suman acción y pausa.", " segundos"),
            arith("Haces 2 vueltas de 4 estaciones cada una. ¿Cuántas estaciones haces?", "2*4", "Se multiplican vueltas por estaciones.", " estaciones"),
            arith("Una vuelta dura 240 segundos. ¿Cuántos minutos son?", "240//60", "Un minuto tiene 60 segundos.", " minutos"),
        ],
        "reason": [
            ex("Caro hace todas las estaciones corriendo y no puede hablar. ¿Qué nivel tiene y qué debe cambiar?", "Nivel 5; bajar la velocidad", "Debe bajar a nivel 3."),
            ex("Dani salta con las piernas rectas y le duelen las rodillas. ¿Qué técnica corrige?", "Doblar las rodillas al caer", "Así se amortigua."),
        ],
        "challenge": [
            arith("Si haces 3 vueltas y cada una dura 4 minutos, ¿cuántos minutos son en total?", "3*4", "Se multiplican vueltas por minutos.", " minutos"),
            ex("Tu meta de hoy en el circuito es de 12 minutos. Ya hiciste 8 minutos. ¿Cuántos minutos te faltan?", "4", "12 menos 8 son 4."),
        ],
    },
    context=[ex("En casa tienes un pasillo y haces el circuito con zapatos como conos. Un hermano pequeño se mete al camino. ¿Qué haces: A) lo esquivas corriendo, B) detienes el circuito y esperas a que salga, C) sigues igual?", "B", "Detener evita choques.")],
    selfcheck=[
        ex("¿Qué nivel de la escala es moderado?", "3", "Hablas frases cortas."),
        ex("¿Cuántas estaciones tiene una vuelta?", "4", "Trote, saltos, pasos laterales y tijera."),
        ex("¿Qué haces al terminar?", "Caminar un minuto", "Así te recuperas con calma."),
    ],
    open_task=task("Haz el circuito de 4 estaciones: 1) trote suave rodeando un cono, 2) saltos con dos pies sobre una cuerda, 3) pasos laterales rápidos, 4) saltos de tijera suaves. Trabaja 30 segundos y descansa 30 en cada estación. Haz 2 vueltas. Al terminar cada estación, anota tu nivel en la escala del habla (1 a 5) y marca si cuidaste la técnica (rodillas dobladas, mirada al frente).",
                   "Vuelta 1: niveles 3, 3, 3, 4 (en la tijera bajé la velocidad). Vuelta 2: 3, 3, 3, 3. Cuidé la técnica en 7 de 8 estaciones.",
                   ["mantiene nivel 3 casi siempre", "usa buena técnica", "respeta pausas y distancia"],
                   ["tabla de niveles", "observación de un adulto", "relato oral"],
                   ["pasar al nivel 5", "saltar sin doblar rodillas", "correr entre estaciones"],
                   "Destaca el uso de la escala y pide un ajuste concreto de técnica."),
    reinforce="Haz una vuelta de solo 2 estaciones, con 30 segundos de acción y 30 de pausa.",
    extend="Agrega una estación 5 de equilibrio sobre una línea y recalcula la duración de una vuelta.",
)

register(
    OA6, 3,
    materials="Un cuadrado de 4 × 4 m, cuatro conos, reloj con segundos, agua y la escala del habla de esta clase.",
    use="Aprenderé a reconocer un tramo vigoroso y a recuperarme después. Sirve para jugar más intenso un rato y descansar bien.",
    prior=["Sé usar la escala del habla.", "Sé hacer un calentamiento."],
    explain=[
        "Un intervalo es un tramo de esfuerzo fuerte seguido de un descanso. En el juego «La carrera de los conos» corres rápido, pero con control, entre cuatro conos durante 50 segundos y luego caminas 50 segundos para recuperarte. Se repite tres veces.",
        "El esfuerzo vigoroso es nivel 4: solo dices palabras sueltas. No dura mucho; por eso viene un descanso. " + SCALE + " Si llegas a 5, paras al instante, caminas despacio y bebes agua.",
        "Recuperar es volver a respirar tranquilo. Sabes que te recuperaste cuando puedes hablar con frases cortas o conversar. Mientras te recuperas, camina, no te sientes de golpe y no pares quieto de inmediato.",
    ],
    vocab=[("intervalo", "tramo de esfuerzo y tramo de descanso"), ("vigoroso", "esfuerzo en que solo digo palabras sueltas"), ("recuperar", "volver a respirar tranquilo"), ("pausa", "descanso entre esfuerzos"), ("repetir", "hacer de nuevo")],
    worked=[
        W("Tiempo total", "Haces 3 intervalos de 50 segundos de acción y 50 de pausa. ¿Cuántos segundos dura todo?", ["Un intervalo: 50 + 50 = 100.", "Tres intervalos: 100 × 3.", "100 × 3 = 300."], "300 segundos (5 minutos)."),
        W("Reconocer vigoroso", "Durante el tramo fuerte solo puedes decir «sí» y «no». ¿Qué nivel es y qué sigue?", ["Palabras sueltas es nivel 4, vigoroso.", "Termina el tramo y comienza la pausa.", "Camino despacio hasta poder hablar frases cortas."], "Nivel 4; sigue la pausa con caminata."),
    ],
    mistakes=[M("Detenerse de golpe y sentarse tras el esfuerzo.", "Se quiere descansar rápido.", "Camina despacio unos segundos antes de sentarte."),
              M("Hacer todos los intervalos al nivel 5.", "Se piensa que más fuerte es mejor.", "Tu esfuerzo fuerte es nivel 4; si pasas a 5, baja.")],
    tiers={
        "recovery": [
            ex("Un intervalo tiene un tramo de esfuerzo y uno de...", "Descanso", "Es la pausa."),
            ex("Esfuerzo vigoroso es el nivel ¿4 o 2?", "4", "Solo palabras sueltas."),
            ex("En la pausa, ¿caminas o te quedas rígido?", "Caminas", "Ayuda a recuperar."),
        ],
        "understand": [
            ex("¿Por qué el esfuerzo vigoroso es corto?", "Porque cansa mucho", "Se necesita recuperar."),
            ex("¿Cómo sabes que te recuperaste?", "Puedes hablar con frases cortas o conversar", "La respiración se calma."),
            ex("Si llegas al nivel 5, ¿qué haces?", "Parar", "No puedes hablar."),
        ],
        "apply": [
            arith("Un intervalo tiene 50 de acción y 50 de pausa. ¿Cuántos segundos son?", "50+50", "Se suman.", " segundos"),
            arith("Haces 3 intervalos de 50 segundos de acción. ¿Cuántos segundos de acción?", "3*50", "Se multiplican.", " segundos"),
            arith("Tres intervalos duran 100 segundos cada uno. ¿Cuántos segundos son en total?", "100*3", "Se multiplican intervalos por segundos.", " segundos"),
        ],
        "reason": [
            ex("Ema se sienta de golpe tras correr y siente mareo. ¿Qué debió hacer?", "Caminar despacio antes de sentarse", "El cuerpo necesita bajar el ritmo."),
            ex("Fito dice «mi tramo vigoroso fue un nivel 2 porque pude conversar». ¿Fue vigoroso?", "No", "Vigoroso es nivel 4."),
        ],
        "challenge": [
            arith("Planeas 3 intervalos de 50 segundos de acción y 50 de pausa y luego un calentamiento de 80 segundos. ¿Cuántos segundos dura todo?", "3*(50+50)+80", "Se suman intervalos y calentamiento.", " segundos"),
            ex("Si cada pausa de 50 segundos te deja hablando frases cortas, ¿te recuperaste lo suficiente para otro intervalo?", "Sí", "Las frases cortas indican nivel 3 o menos."),
        ],
    },
    context=[ex("En el recreo corres mucho y sientes que no puedes hablar. ¿Qué haces: A) sigues corriendo, B) caminas y tomas agua, C) saltas más?", "B", "Si no puedes hablar, debes parar y recuperarte.")],
    selfcheck=[
        ex("¿Qué nivel es vigoroso?", "4", "Solo palabras sueltas."),
        ex("¿Qué haces en la pausa?", "Caminas y recuperas", "Vuelves a respirar tranquilo."),
        ex("Si haces 3 intervalos de 50 segundos de acción, ¿cuántos segundos son?", "150", "3 por 50 son 150."),
    ],
    open_task=task("Con un cuadrado de 4 × 4 m y cuatro conos (o zapatos), juega «La carrera de los conos»: corre rápido, pero con control, de cono en cono por 50 segundos, y luego camina 50 segundos. Repite 3 veces. Después de cada tramo fuerte anota tu nivel (1 a 5) y después de cada pausa anota si ya hablabas frases cortas (sí/no).",
                   "Tramo 1: nivel 4, pausa: sí. Tramo 2: nivel 4, pausa: sí. Tramo 3: nivel 4, pausa: sí. Nunca llegué al nivel 5.",
                   ["alcanza un tramo vigoroso (nivel 4)", "recupera en cada pausa", "no llega al nivel 5"],
                   ["tabla con niveles", "observación de un adulto", "relato oral"],
                   ["saltarse la pausa", "llegar al nivel 5 sin parar", "sentarse de golpe"],
                   "Pregunta cómo supo que se recuperó y felicita el cuidado de su respiración."),
    reinforce="Trota suave 20 segundos y camina 20 segundos, dos veces.",
    extend="Compara tus niveles al final del primer y del tercer intervalo y explica si te costó más.",
)

register(
    OA6, 4,
    materials="Un espacio de 4 × 4 m, reloj, agua y las tarjetas escritas en esta clase: «sube el ritmo», «mantén», «baja el ritmo».",
    use="Aprenderé a subir o bajar mi esfuerzo según lo que siente mi cuerpo. Sirve para jugar fuerte sin pasarme del límite.",
    prior=["Sé usar la escala del habla.", "Sé hacer intervalos."],
    explain=[
        "Regular el esfuerzo es subir o bajar la intensidad según las señales de tu cuerpo. Las señales son: cuánto puedes hablar, cuánto respiras, si sudas y si te sientes cansado. " + SCALE,
        "Un adulto muestra tarjetas. «Sube el ritmo» significa pasar de un nivel al siguiente. «Mantén» significa seguir igual. «Baja el ritmo» significa pasar a un nivel menor. Tú decides cómo hacerlo: por ejemplo, subes trotando más rápido o bajas caminando. Si estás en el nivel 4, «sube el ritmo» no se hace: te quedas en 4.",
        "El mejor esfuerzo no es el máximo, sino el que puedes sostener sin pasar al nivel 5. Si sientes dolor, mareo o falta de aire, dejas el juego y avisas a un adulto, aunque falte tiempo.",
    ],
    vocab=[("regular", "ajustar para que quede bien"), ("intensidad", "cuán fuerte es el esfuerzo"), ("señal del cuerpo", "lo que siento al moverme"), ("sostener", "mantener durante un rato"), ("avisar", "decirle a un adulto lo que me pasa")],
    worked=[
        W("Subir un nivel", "Estás en nivel 2 y la tarjeta dice «sube el ritmo». ¿A qué nivel llegas y cómo?", ["Un nivel más que 2 es 3.", "Trotar un poco más rápido.", "Compruebo que digo frases cortas."], "Nivel 3, trotando un poco más rápido."),
        W("Bajar el ritmo", "Estás en nivel 4 y la tarjeta dice «baja el ritmo». ¿Qué haces?", ["Nivel 4 es el actual.", "Un nivel menos es 3.", "Disminuyo la velocidad hasta decir frases cortas."], "Bajo a nivel 3 yendo más lento."),
    ],
    mistakes=[M("Seguir al nivel 5 por no querer parar.", "Se compite con los demás.", "Baja el ritmo si no puedes hablar."),
              M("Confundir «mantén» con «para».", "No se escucha la tarjeta.", "Mantén significa seguir igual, no detenerte.")],
    tiers={
        "recovery": [
            ex("«Baja el ritmo», ¿es ir más lento o más rápido?", "Más lento", "Baja la intensidad."),
            ex("«Sube el ritmo», ¿es ir más lento o más rápido?", "Más rápido", "Sube la intensidad."),
            ex("«Mantén» significa seguir ¿igual o parar?", "Igual", "No cambias el ritmo."),
        ],
        "understand": [
            ex("¿Cuáles son señales de tu cuerpo: puedo hablar, sudor, mi color favorito?", "Puedo hablar y sudor", "El color favorito no dice cómo está el cuerpo."),
            ex("¿Cuál es el mejor esfuerzo: el máximo o el que puedes sostener?", "El que puedes sostener", "Así no llegas al nivel 5."),
            ex("Si sientes mareo, ¿sigues o avisas a un adulto?", "Avisas a un adulto", "Es una señal para parar."),
        ],
        "apply": [
            ex("Estás en nivel 2 y sale «sube el ritmo». ¿A qué nivel pasas?", "3", "Un nivel más que 2."),
            ex("Estás en nivel 4 y sale «baja el ritmo». ¿A qué nivel pasas?", "3", "Un nivel menos que 4."),
            ex("Las tarjetas son: sube, mantén, baja, baja. Empiezas en nivel 3. ¿En qué nivel terminas?", "2", "Sube a 4, mantiene 4, baja a 3 y baja a 2."),
        ],
        "reason": [
            ex("Beto dice «si estoy en nivel 5, sigo porque soy fuerte». ¿Qué le dices?", "Que pare y baje el ritmo", "En nivel 5 no puedes hablar."),
            ex("Ana está en nivel 1 durante todo el circuito moderado. ¿Qué debería cambiar?", "Subir el ritmo", "Moderado es nivel 3."),
        ],
        "challenge": [
            ex("Empiezas en nivel 2. Tarjetas: sube, sube, mantén, baja. ¿En qué nivel terminas?", "3", "2, 3, 4, 4, 3."),
            arith("Haces 3 tarjetas de 30 segundos cada una. ¿Cuántos segundos dura la actividad?", "3*30", "Se multiplican tarjetas por segundos.", " segundos"),
        ],
    },
    context=[ex("En Educación Física estás en nivel 3 y la profesora dice «bajen el ritmo». ¿Qué haces: A) corres más rápido, B) trotas más lento, C) te sientas?", "B", "Bajar el ritmo es ir más lento.")],
    selfcheck=[
        ex("¿Qué haces si estás en nivel 5?", "Parar", "No puedes hablar."),
        ex("«Sube el ritmo» desde nivel 3, ¿a qué nivel llegas?", "4", "Un nivel más."),
        ex("¿Qué dos señales del cuerpo puedes mirar?", "Cuánto hablo y cuánto respiro", "Muestran el esfuerzo."),
    ],
    open_task=task("Con un adulto que muestre tarjetas, haz esta secuencia de 6 tarjetas de 30 segundos: sube, mantén, sube, baja, mantén, baja. Parte en nivel 2. Anota el nivel después de cada tarjeta. Si algún nivel llega a 5, para, bebe agua y descansa 1 minuto.",
                   "Niveles: 3, 3, 4, 3, 3, 2. Nunca llegué al 5. Regulé trotando más rápido o más lento.",
                   ["sube y baja según la tarjeta", "mantiene el control de su respiración", "avisa o para si hace falta"],
                   ["tabla de niveles", "observación de un adulto", "relato oral"],
                   ["no cambiar de nivel", "llegar al 5 sin parar", "ignorar señales"],
                   "Pregunta qué señal del cuerpo usó para decidir y refuerza el cuidado."),
    reinforce="Trota suave 20 segundos, sube un poco 20 segundos y baja 20 segundos.",
    extend="Crea tus propias tarjetas con tres cambios de ritmo y pide a alguien que las cumpla.",
)

# ---------------------------------------------------------------- OA 07
register(
    OA7, 1,
    materials="Un lápiz y una hoja con una tabla de la semana (lunes a domingo). Una cuerda o tiza. La tabla se explica en esta clase.",
    use="Aprenderé a encontrar momentos del día para moverme con juegos y actividades. Sirve para ser activo todos los días, no solo en clase de Educación Física.",
    prior=["Sé qué hago de lunes a viernes.", "Sé contar minutos."],
    explain=[
        "Moverse en la vida cotidiana es hacer actividad física en las cosas de todos los días: caminar al colegio, subir las escaleras, jugar en el patio o en la plaza, ayudar a ordenar la casa. No necesitas ropa especial ni pagar nada.",
        "Para niños y niñas de tu edad, lo recomendado es moverse al menos 60 minutos al día, con un esfuerzo en que respiras más rápido que en reposo. Esos minutos se pueden juntar de muchas partes: 20 minutos en el recreo, 20 jugando en la tarde y 20 caminando. No tienen que ser seguidos.",
        "Para encontrar tus oportunidades, mira tu día: ¿cuándo camino?, ¿cuándo juego?, ¿cuándo estoy sentado mucho rato? En los momentos de estar sentado, puedes pararte, estirarte o jugar un rato. Siempre que te muevas, hazlo con un adulto cerca y en un lugar seguro.",
    ],
    vocab=[("cotidiano", "de todos los días"), ("oportunidad", "momento en que puedo hacer algo"), ("recomendado", "lo que se aconseja hacer"), ("minuto", "60 segundos"), ("estirarse", "alargar los músculos con suavidad")],
    worked=[
        W("Sumar minutos", "Hoy caminaste 15 minutos al colegio, jugaste 20 minutos en el recreo y 25 minutos en la plaza. ¿Cuántos minutos te moviste?", ["Sumo 15 + 20.", "35 + 25.", "El total es 60."], "60 minutos, justo lo recomendado."),
        W("Encontrar una oportunidad", "Pasas 30 minutos sentado viendo una película. ¿Cómo agregas movimiento?", ["Miro cuánto tiempo llevo quieto.", "Cada 10 minutos me paro y me estiro o camino.", "Así me muevo más seguido."], "Pararme y moverme cada 10 minutos."),
    ],
    mistakes=[M("Pensar que moverse es solo hacer deporte.", "Se cree que necesita equipamiento.", "Caminar, jugar y ayudar en casa también cuentan."),
              M("Quedarse sentado toda la tarde.", "No se mira el tiempo quieto.", "Cada cierto rato, párate y muévete.")],
    tiers={
        "recovery": [
            ex("Caminar al colegio, ¿cuenta como actividad física?", "Sí", "Es movimiento cotidiano."),
            ex("¿Cuántos minutos al día se recomiendan para tu edad?", "60 minutos", "Es la recomendación para niños y niñas."),
            ex("Los 60 minutos, ¿deben ser seguidos o se pueden juntar?", "Se pueden juntar", "Se suman varias partes del día."),
        ],
        "understand": [
            ex("¿Necesitas ropa especial para moverte en lo cotidiano?", "No", "Caminar o jugar no la requiere."),
            ex("Un momento de estar muy sentado es una oportunidad para...", "Pararme y moverme", "Es una oportunidad de actividad."),
            ex("¿Qué significa «cotidiano»?", "De todos los días", "Son rutinas diarias."),
        ],
        "apply": [
            arith("Caminas 15 minutos, juegas 20 y subes escaleras 5. ¿Cuántos minutos suman?", "15+20+5", "Se suman los minutos.", " minutos"),
            arith("Debes completar 60 minutos y llevas 45. ¿Cuántos faltan?", "60-45", "Se resta lo hecho de la meta.", " minutos"),
            arith("Juegas 20 minutos en el recreo y 20 después del colegio. ¿Cuántos minutos son?", "20+20", "Se suman.", " minutos"),
        ],
        "reason": [
            ex("Ema dice que no se mueve porque no tiene balón. ¿Qué le dices?", "Puede caminar, saltar la cuerda o correr", "Hay muchas actividades sin balón."),
            ex("Fito pasó 2 horas sentado sin pararse. ¿Qué podría hacer cada 30 minutos?", "Pararse y moverse", "Mover el cuerpo rompe el tiempo sentado."),
        ],
        "challenge": [
            ex("Tu día: caminar 10 minutos de ida y 10 de vuelta, recreo 20 minutos y plaza 20 minutos. ¿Llegas a 60 minutos?", "Sí, justo", "10 + 10 + 20 + 20 son 60."),
            arith("Quieres sumar 60 minutos cada día durante 5 días. ¿Cuántos minutos son en total?", "60*5", "Se multiplican minutos por días.", " minutos"),
        ],
    },
    context=[ex("Tu amiga dice «mañana me quedo en casa viendo televisión todo el día». ¿Qué le propones: A) jugar 20 minutos en el patio entre programas, B) nada, C) dormir?", "A", "Agregar movimiento sin dejar de descansar.")],
    selfcheck=[
        ex("¿Cuántos minutos al día se recomiendan?", "60", "Es la recomendación."),
        ex("Subir escaleras, ¿cuenta como movimiento?", "Sí", "Es actividad cotidiana."),
        ex("Si llevas 40 minutos, ¿cuántos faltan para 60?", "20", "60 menos 40 son 20."),
    ],
    open_task=task("Anota en una tabla de lunes a viernes: el momento en que te mueves (caminar al colegio, recreo, plaza o ayudar en casa) y los minutos. Usa estos datos de ejemplo para practicar: lunes 15 (caminar) + 20 (recreo); martes 30 (plaza); miércoles 10 + 20 (patio) + 10 (ordenar); jueves 25; viernes 15 + 30. Calcula cuántos minutos hay cada día y cuál día llegó a 60. Luego dibuja una oportunidad nueva para un día que quedó corto.",
                   "Lunes 35, martes 30, miércoles 40, jueves 25, viernes 45. Ningún día llegó a 60. Para el jueves agregaría 35 minutos: caminar 15 y jugar luche 20.",
                   ["suma los minutos por día", "compara con 60", "propone una oportunidad nueva y segura"],
                   ["tabla completada", "dibujo de la oportunidad", "relato oral"],
                   ["no sumar bien", "pensar que solo cuenta el deporte", "proponer algo inseguro"],
                   "Pide que explique su propuesta y refuerza ideas realistas y seguras."),
    reinforce="Suma tus minutos de hoy: caminar, jugar y subir escaleras.",
    extend="Completa una semana de movimiento y calcula el total; intenta que cada día sea al menos 60 minutos.",
)

register(
    OA7, 2,
    materials="Una tiza o cinta para dibujar en el suelo una luche (figura de 8 casillas numeradas), una piedra pequeña lisa o una tapa, una cuerda de 2 m y un adulto. Superficie plana y seca.",
    use="Aprenderé las reglas de dos juegos tradicionales, la luche y saltar la cuerda, y a explicar de dónde los aprendí. Sirve para jugar con la familia y los amigos.",
    prior=["Sé saltar con un pie y con dos.", "Sé contar hasta 8."],
    explain=[
        "Los juegos tradicionales se pasan de una persona a otra: los aprendes de abuelos, padres, vecinos o amigos. Algunos se juegan en todo Chile. Cada familia o barrio puede jugarlos con pequeñas diferencias de reglas. Por eso, siempre se pregunta: ¿quién te lo enseñó?, ¿dónde se juega?, ¿qué reglas usan?",
        "Reglas de la luche, en versión sencilla: 1) se dibujan 8 casillas numeradas del 1 al 8, 2) se tira la tapa o piedra a la casilla 1, 3) se salta con un pie por las casillas, sin pisar la casilla de la tapa ni las líneas, 4) en la casilla 8 se da media vuelta y se vuelve, 5) al volver se recoge la tapa y se avanza al siguiente turno con la casilla 2. Si pisas una línea, pierdes el turno.",
        "Para saltar la cuerda: 1) dos personas giran la cuerda o tú la giras solo, 2) saltas cuando toca el suelo, 3) cuentas cuántos saltos seguidos haces. Ambos juegos se hacen en un lugar plano, seco y sin objetos. Siempre con zapatillas amarradas.",
    ],
    vocab=[("tradicional", "que se transmite de generación en generación"), ("luche", "juego de saltar por casillas dibujadas en el suelo"), ("casilla", "cuadro dibujado en el suelo"), ("turno", "momento en que me toca jugar"), ("procedencia", "de dónde viene algo o quién lo enseñó")],
    worked=[
        W("Contar casillas", "En la luche hay 8 casillas y la tapa está en la casilla 3. ¿Cuántas casillas puedes pisar al saltar de la 1 a la 8?", ["Hay 8 casillas.", "La casilla 3 tiene la tapa y no se pisa.", "8 − 1 = 7."], "7 casillas."),
        W("Preguntar la procedencia", "Tu abuela te enseña un juego. ¿Qué preguntas haces para conocer su procedencia?", ["¿Quién te lo enseñó?", "¿Dónde lo jugabas?", "¿Cuáles eran las reglas?"], "Quién lo enseñó, dónde se jugaba y cuáles eran las reglas."),
    ],
    mistakes=[M("Pisar las líneas y seguir jugando.", "Se olvida la regla.", "Si pisas una línea, pierdes el turno y esperas."),
              M("Saltar la cuerda en un piso mojado.", "No se revisa el suelo.", "Elige un lugar plano y seco.")],
    tiers={
        "recovery": [
            ex("En la luche, ¿saltas con un pie o con dos pies cada vez en las casillas?", "Con un pie", "Es la regla sencilla de la luche."),
            ex("Si pisas una línea, ¿pierdes el turno o ganas puntos?", "Pierdes el turno", "Es la regla."),
            ex("Los juegos tradicionales, ¿se pasan de persona a persona?", "Sí", "Se transmiten de generación en generación."),
        ],
        "understand": [
            ex("¿Qué significa «procedencia»?", "De dónde viene algo o quién lo enseñó", "Es el origen."),
            ex("¿Por qué es importante jugar en un lugar seco y plano?", "Para no resbalar ni tropezar", "Así se evitan las caídas."),
            ex("¿Cuántas casillas tiene esta luche sencilla?", "8", "Van del 1 al 8."),
        ],
        "apply": [
            arith("Haces 5 saltos de cuerda seguidos, luego 7 y luego 9. ¿Cuántos saltos hiciste en total?", "5+7+9", "Se suman los tres grupos.", " saltos"),
            arith("Si la tapa está en la casilla 3, ¿cuántas casillas sin tapa hay de las 8?", "8-1", "Solo una casilla tiene la tapa.", " casillas"),
            ex("Dos amigos juegan luche por turnos. Ema lanza a la casilla 1 y Beto a la 2. ¿Quién va primero?", "Ema", "Ella empieza en la casilla 1."),
        ],
        "reason": [
            ex("Beto pisó una línea y dice «no vale». ¿Qué regla se aplica?", "Pierde el turno", "Pisar una línea hace perder el turno."),
            ex("Una amiga dice que en su barrio la luche se juega distinto. ¿Está mal?", "No", "Los juegos pueden tener variantes."),
        ],
        "challenge": [
            ex("Tu abuela te enseña un juego de cuerda. ¿Qué tres datos anotas para conocer su procedencia?", "Quién lo enseñó, dónde se juega y qué reglas tiene", "Responden a la procedencia."),
            arith("Saltas la cuerda 3 veces; cada vez haces 12 saltos. ¿Cuántos saltos haces?", "3*12", "Se multiplican veces por saltos.", " saltos"),
        ],
    },
    context=[ex("Un día de lluvia el patio está mojado y hay charcos. ¿Juegas luche allí: A) sí, B) no, esperas a que seque o juegas adentro?", "B", "El suelo mojado resbala.")],
    selfcheck=[
        ex("¿Qué se hace al pisar una línea?", "Pierdes el turno", "Es la regla."),
        ex("¿Qué se pregunta para conocer la procedencia?", "¿Quién te lo enseñó?", "Dice de dónde viene."),
        ex("¿En qué suelo se juega luche?", "Plano y seco", "Así se evitan las caídas."),
    ],
    open_task=task("Dibuja una luche de 8 casillas con tiza o cinta y juega con un adulto 2 turnos usando una tapa como piedra. Reglas: tira a la casilla del turno, salta con un pie sin pisar líneas ni la casilla de la tapa, da media vuelta en la 8 y vuelve a recogerla. Anota cuántas veces pisaste una línea. Después pregunta a un adulto de tu familia: ¿quién le enseñó este juego u otro parecido?, ¿dónde jugaba?, ¿qué reglas usaba? Anota sus respuestas.",
                   "Jugué 2 turnos y pisé una línea 1 vez. Mi abuela dice que se lo enseñó su vecina, que jugaba en el patio de su casa y que usaban una piedra plana.",
                   ["sigue las reglas del juego", "juega en un lugar seguro", "anota la procedencia con preguntas"],
                   ["luche dibujada", "registro de turnos", "respuestas del adulto"],
                   ["pisar líneas sin perder turno", "jugar en piso mojado", "no preguntar la procedencia"],
                   "Reconoce que valora lo aprendido de otros y pide comparar con otro juego."),
    reinforce="Salta por las 8 casillas de la luche con un pie, ida y vuelta, con cuidado.",
    extend="Compara la luche con otro juego que conozcas: ¿qué reglas se parecen?",
)

register(
    OA7, 3,
    materials="Un espacio de 4 × 4 m, una tiza o cuerda para marcar, una pelota blanda opcional y reloj. Un grupo de 3 o más personas.",
    use="Aprenderé a cambiar el espacio, el tiempo o el material de un juego para que todos puedan participar. Sirve para jugar con niños y niñas distintos sin dejar a nadie fuera.",
    prior=["Sé jugar a la luche o a otro juego con reglas.", "Sé que cada persona se mueve distinto."],
    explain=[
        "Variar para incluir significa cambiar algo del juego para que más personas puedan participar. Se puede cambiar el espacio (más grande o más pequeño), el tiempo (más corto o más largo) o el implemento (una pelota más blanda o más grande). La idea es que todos puedan jugar y que el juego sea seguro.",
        "Por ejemplo, en la luche, si alguien no puede saltar con un pie, puede ir caminando por las casillas. Si el espacio es pequeño, se dibujan 6 casillas en lugar de 8. Si un niño es más pequeño, la tapa se lanza más cerca.",
        "Antes de cambiar, se pregunta: ¿quién no puede jugar bien?, ¿qué se puede cambiar?, ¿sigue siendo seguro? Luego se prueba. Si todos juegan, el cambio sirvió. Si alguien sigue afuera, se prueba otro cambio. Nunca se dice que alguien «no sirve» para jugar.",
    ],
    vocab=[("variar", "hacer cambios"), ("incluir", "hacer que todos participen"), ("implemento", "objeto que se usa en el juego"), ("adaptar", "cambiar algo para que sirva a más personas"), ("seguro", "que no lastima")],
    worked=[
        W("Adaptar la luche", "Juegan luche 3 personas. Ana no puede saltar con un pie. ¿Qué cambio propones?", ["Pienso en quién queda fuera: Ana.", "Ella camina por las casillas en vez de saltar con un pie.", "Todos pueden elegir saltar o caminar."], "Permitir caminar por las casillas."),
        W("Cambiar el espacio", "El patio solo permite dibujar 6 casillas en lugar de 8. ¿Cuántas casillas hay de menos?", ["Había 8 casillas.", "Ahora hay 6.", "8 − 6 = 2."], "2 casillas menos."),
    ],
    mistakes=[M("Decir «tú no puedes jugar».", "Se piensa solo en ganar.", "Pregunta qué cambio permite que todos jueguen."),
              M("Cambiar una regla y hacerlo inseguro.", "Se quiere más emoción.", "Un cambio nunca debe agregar peligro.")],
    tiers={
        "recovery": [
            ex("Variar para incluir sirve para que ¿pocos o todos participen?", "Todos", "Ese es el objetivo."),
            ex("Una pelota más blanda es un cambio de ¿implemento o de tiempo?", "Implemento", "La pelota es un objeto."),
            ex("Hacer el juego más corto es un cambio de ¿tiempo o de espacio?", "Tiempo", "Cambia cuánto dura."),
        ],
        "understand": [
            ex("¿Qué se pregunta antes de cambiar una regla?", "Quién no puede jugar y qué se puede cambiar", "Se piensa en los demás."),
            ex("Un cambio que agrega peligro, ¿se acepta?", "No", "La seguridad siempre se mantiene."),
            ex("¿Qué se hace si el cambio no resulta?", "Probar otro cambio", "Se busca otra solución."),
        ],
        "apply": [
            arith("El juego duraba 60 segundos y lo acortas 20 segundos. ¿Cuántos segundos dura ahora?", "60-20", "Se resta lo acortado.", " segundos"),
            arith("Una luche tenía 8 casillas; la reduces a 6. ¿Cuántas casillas quitaste?", "8-6", "Se resta lo que queda.", " casillas"),
            ex("Beto es más pequeño y la tapa cae lejos. Elige: A) acercar la línea de tiro, B) que no juegue, C) alejarla. ¿Cuál incluye?", "A", "Acercar le permite jugar."),
        ],
        "reason": [
            ex("Dani no puede correr rápido. En un juego de persecución, ¿qué cambio sirve: que todos caminen rápido o que Dani no juegue?", "Que todos caminen rápido", "Así Dani puede participar."),
            ex("Ema propone saltar sobre una banca para que sea más emocionante. ¿Es un buen cambio?", "No", "Saltar sobre una banca agrega peligro."),
        ],
        "challenge": [
            arith("Quieres que 4 personas jueguen cada una 3 turnos de 15 segundos. ¿Cuántos segundos dura el juego?", "4*3*15", "Se multiplican personas, turnos y segundos.", " segundos"),
            ex("Propón dos cambios para un juego donde un niño usa muletas: un cambio de espacio y uno de implemento. Respuesta modelo: reducir la distancia a 3 pasos y usar una pelota blanda grande. ¿Cuántos cambios hay?", "2", "Uno de espacio y uno de implemento."),
        ],
    },
    context=[ex("En tu patio juegan a la luche y una niña con el tobillo vendado quiere participar. ¿Qué haces: A) le dices que no, B) dejas que vaya caminando por las casillas, C) la empujas?", "B", "Se adapta el juego para incluirla.")],
    selfcheck=[
        ex("¿Qué significa «incluir»?", "Hacer que todos participen", "No dejar a nadie fuera."),
        ex("Si el espacio es chico, ¿haces más o menos casillas?", "Menos", "Cabe en el lugar."),
        ex("¿Se puede agregar peligro para que sea emocionante?", "No", "La seguridad siempre se mantiene."),
    ],
    open_task=task("Juego: «lanzar la tapa a un aro» con un aro o círculo de cuerda a 4 pasos. Imagina tres personas: Ema (no alcanza a lanzar tan lejos), Beto (siempre acierta) y Dani (usa un andador y no puede mover muy rápido los pies). Escribe un cambio para cada una usando espacio, tiempo o implemento, y verifica que sea seguro. Pruébalo con un adulto y anota si todos pudieron participar.",
                   "Ema: acerco el aro a 3 pasos. Beto: lo alejo a 5 pasos. Dani: le doy más tiempo para cada lanzamiento y despejo el camino hasta el aro. Probamos y todos pudimos participar.",
                   ["propone un cambio para cada persona", "cuida la seguridad", "verifica que todos participen"],
                   ["tabla con cambios", "observación de un adulto", "relato oral"],
                   ["dejar a alguien afuera", "agregar peligro", "no probar"],
                   "Reconoce los cambios que incluyen y pide revisar si algún cambio dejó a alguien afuera."),
    reinforce="Juega con un aro a 3 pasos y luego a 5 pasos y anota cuántos aciertos hay en cada una.",
    extend="Inventa un juego de lanzar con tres reglas que incluya a una persona que no puede correr.",
)

register(
    OA7, 4,
    materials="Una hoja con una tabla de lunes a domingo, lápiz y un calendario familiar sencillo. Los datos de ejemplo están escritos en esta clase.",
    use="Aprenderé a armar un plan semanal con actividades variadas y posibles. Sirve para moverme todos los días de la semana de manera realista.",
    prior=["Sé sumar minutos.", "Sé cuántos días tiene una semana."],
    explain=[
        "Un plan semanal es una tabla con los días de la semana y la actividad que harás cada día. Para que sea realista, usa actividades que puedas hacer de verdad: caminar al colegio, jugar luche, saltar la cuerda, andar en bicicleta con casco o ayudar en casa. No necesita comprar nada.",
        "Un buen plan es variado (no siempre lo mismo), seguro (con un adulto cuando haga falta) y con tiempo suficiente. La recomendación es mover el cuerpo unos 60 minutos al día, y también tener días para descansar y jugar tranquilo. Escucha tu cuerpo: si estás cansado, escoge algo suave.",
        "Para armar el plan, escribe para cada día una actividad y los minutos. Suma los minutos de la semana y comprueba cuántos días llegaron a 60. Si hay un día corto, agrega 10 o 15 minutos de algo fácil. Revisa el plan al final de la semana.",
    ],
    vocab=[("plan", "lista de lo que haré"), ("semana", "siete días"), ("variado", "con cosas distintas"), ("realista", "posible de hacer de verdad"), ("revisar", "mirar cómo resultó")],
    worked=[
        W("Sumar la semana", "Lunes 40 minutos, martes 30, miércoles 60 y jueves 50. ¿Cuántos minutos suman en esos cuatro días?", ["40 + 30 = 70.", "70 + 60 = 130.", "130 + 50 = 180."], "180 minutos."),
        W("Un plan variado", "Tu plan dice: lunes caminar, martes caminar, miércoles caminar. ¿Cómo lo mejoras?", ["Veo que se repite la misma actividad.", "Cambio el martes por saltar la cuerda y el miércoles por luche.", "Ahora hay tres actividades distintas."], "Cambiar el martes y el miércoles por actividades distintas."),
    ],
    mistakes=[M("Planear 2 horas cada día aunque no hay tiempo.", "Se quiere hacer mucho.", "Elige un tiempo que puedas cumplir, como 60 minutos."),
              M("Poner solo actividades que necesitan comprar cosas.", "No se mira lo que hay en casa.", "Usa actividades con lo que tienes: cuerda, tiza, patio.")],
    tiers={
        "recovery": [
            ex("Si cuentas de lunes a domingo, ¿cuántos días planificas en una semana completa?", "7", "Lunes a domingo son siete días."),
            ex("Un plan variado, ¿tiene actividades iguales o distintas?", "Distintas", "Variado es diferente."),
            ex("Un plan realista, ¿se puede hacer de verdad o no?", "Se puede hacer de verdad", "Un plan realista es posible de cumplir."),
        ],
        "understand": [
            ex("¿Por qué conviene tener días de descanso o de actividad suave?", "Porque el cuerpo también necesita descansar", "El descanso es parte de la salud."),
            ex("¿Qué haces con el plan al final de la semana?", "Lo revisas", "Ves cómo resultó."),
            ex("Si estás cansado, ¿escoges una actividad suave o muy fuerte?", "Suave", "Escuchas tu cuerpo."),
        ],
        "apply": [
            arith("Lunes 40 minutos, martes 30 y miércoles 60. ¿Cuántos minutos suman?", "40+30+60", "Se suman.", " minutos"),
            arith("Quieres 60 minutos y llevas 35. ¿Cuántos faltan?", "60-35", "Se resta.", " minutos"),
            ex("Tu plan: lunes luche, martes cuerda, miércoles caminar, jueves luche. ¿Cuántas actividades distintas hay?", "3", "Luche, cuerda y caminar."),
        ],
        "reason": [
            ex("Un plan dice «viernes: andar en bicicleta por la calle solo». ¿Qué debe cambiar?", "Hacerlo con un adulto y en un lugar seguro", "La calle es un riesgo."),
            ex("Ema planea 30 minutos de salto de cuerda todos los días y se cansa mucho. ¿Qué cambia?", "Variar y descansar", "El cuerpo necesita variedad."),
        ],
        "challenge": [
            arith("Una semana: 40, 30, 60, 50, 45, 70 y 35 minutos. ¿Cuántos minutos son?", "40+30+60+50+45+70+35", "Se suman los siete días.", " minutos"),
            ex("En la semana anterior, ¿cuántos días llegaron a 60 minutos o más?", "2", "Miércoles (60) y sábado (70)."),
        ],
    },
    context=[ex("Tu mamá pregunta qué harás el sábado. Tienes patio, una cuerda y una tiza. ¿Qué planeas: A) comprar un equipo caro, B) saltar la cuerda y jugar luche, C) nada?", "B", "Con lo que tienes en casa.")],
    selfcheck=[
        ex("Para completar la meta diaria de movimiento, ¿cuántos minutos juntas en total?", "60", "Es la recomendación diaria."),
        ex("Un plan variado, ¿repite siempre lo mismo?", "No", "Tiene cosas distintas."),
        ex("Si el viernes tienes 45 minutos, ¿cuántos faltan para 60?", "15", "60 menos 45 son 15."),
    ],
    open_task=task("Completa este plan con una actividad y minutos por día (usa solo lo que hay en casa o el patio): lunes ___, martes ___, miércoles ___, jueves ___, viernes ___, sábado ___, domingo ___. Reglas: al menos 3 actividades distintas, un día de descanso o suave, y cada día sumar de 30 a 60 minutos. Suma los minutos de la semana y escribe qué día cambiarías si llegaras cansado.",
                   "Lunes caminar 40; martes cuerda 30; miércoles luche 45; jueves descanso 30 (estirarme); viernes caminar 60; sábado plaza 60; domingo juego en familia 45. Total 310 minutos. Si llego cansado cambio el viernes por algo suave.",
                   ["incluye actividades variadas", "es realista y seguro", "suma bien los minutos"],
                   ["plan completo", "suma escrita", "explicación oral"],
                   ["plan irreal", "actividades inseguras", "no sumar"],
                   "Reconoce la variedad y el realismo del plan; propone revisar en una semana."),
    reinforce="Escribe tres actividades distintas que puedes hacer esta semana sin comprar nada.",
    extend="Haz el plan por una semana y anota cuántos días lo cumpliste.",
)

# ---------------------------------------------------------------- OA 08
register(
    OA8, 1,
    materials="Una silueta de cuerpo dibujada en una hoja, lápiz de colores, un reloj con segundos y agua. Se describen aquí las señales: color de la piel, calor, respiración, corazón y cansancio.",
    use="Aprenderé a notar cómo está mi cuerpo antes de moverme. Sirve para después saber qué cambió y cuidarme.",
    prior=["Sé nombrar partes del cuerpo.", "Sé respirar tranquilo."],
    explain=[
        "Antes de moverte, tu cuerpo está en reposo. Observa tus señales: ¿cómo es tu respiración (lenta o rápida)?, ¿sientes calor o frío?, ¿cómo es el color de tu cara?, ¿cómo late tu corazón con la mano en el pecho?, ¿cuánto cansancio sientes? Anótalas en tu silueta.",
        "En reposo, tu respiración es tranquila y puedes hablar sin esfuerzo. Tu corazón late suave y tu piel tiene su color normal. A esto lo llamamos «punto de partida». Más adelante compararás con lo que sientes durante y después de moverte.",
        "Para registrar, pon una mano en el pecho y cuenta tus latidos durante 15 segundos. Anota el número. Este número no es bueno ni malo: es tuyo. Compararlo después te permite notar cuánto cambió tu cuerpo. Nunca compares tu número con el de otro niño.",
    ],
    vocab=[("reposo", "estar quieto y tranquilo"), ("señal del cuerpo", "algo que mi cuerpo me dice"), ("punto de partida", "cómo estoy antes de empezar"), ("latido", "golpe que da el corazón"), ("respiración", "entrada y salida de aire")],
    worked=[
        W("Contar latidos", "Cuentas 18 latidos en 15 segundos en reposo. ¿Qué anotas en tu silueta?", ["Pongo la mano en el pecho.", "Cuento durante 15 segundos con el reloj.", "Anoto el número: 18."], "18 latidos en 15 segundos."),
        W("Mi punto de partida", "Antes de moverte dices: respiro tranquilo, hablo sin esfuerzo y mi cara tiene su color normal. ¿Qué anotas?", ["Respiración tranquila.", "Hablo sin esfuerzo.", "Color normal."], "Estoy en reposo, con respiración tranquila y color normal."),
    ],
    mistakes=[M("Comparar mis latidos con los de otro.", "Se piensa que un número es mejor.", "Compara solo contigo antes y después."),
              M("Contar latidos en 5 segundos.", "Se apura.", "Cuenta durante 15 segundos para anotar bien.")],
    tiers={
        "recovery": [
            ex("Estar quieto y tranquilo se llama...", "Reposo", "No hay esfuerzo."),
            ex("Para sentir tu corazón, ¿pones la mano en el pecho o en el pie?", "En el pecho", "Ahí se siente."),
            ex("En reposo, ¿respiras tranquilo o muy rápido?", "Tranquilo", "No hay esfuerzo."),
        ],
        "understand": [
            ex("¿Por qué se anota el punto de partida?", "Para comparar después", "Muestra cuánto cambia el cuerpo."),
            ex("¿El número de latidos de un compañero es mejor o peor que el tuyo?", "Ni mejor ni peor", "Cada cuerpo es distinto."),
            ex("¿Cuántos segundos se cuentan los latidos?", "15", "Así se registra."),
        ],
        "apply": [
            arith("Cuentas 18 latidos en 15 segundos y después de un juego 30 en 15 segundos. ¿Cuántos latidos más son?", "30-18", "Se resta el reposo del juego.", " latidos"),
            ex("Tu silueta dice: respiración tranquila, color normal, sin sudor. ¿Estás en reposo?", "Sí", "Todas son señales de reposo."),
            arith("Registras tus señales 3 veces. Cada vez anotas 4 señales. ¿Cuántas señales anotas?", "3*4", "Se multiplican veces por señales.", " señales"),
        ],
        "reason": [
            ex("Ana dice «mi corazón late 22 en 15 segundos, el de Beto 18; el mío es peor». ¿Qué le dices?", "Que no es peor, cada cuerpo es distinto", "No se compara con otros."),
            ex("Dani cuenta sus latidos justo después de correr y los llama «mi reposo». ¿Está bien?", "No", "El reposo es antes de moverse."),
        ],
        "challenge": [
            ex("Orden para registrar: A) anotar el número, B) poner la mano en el pecho, C) contar 15 segundos. ¿Cuál es el orden?", "B, C, A", "Primero sientes, luego cuentas y al final anotas."),
            arith("Si cuentas 20 latidos en 15 segundos y luego repites la medición 2 veces más con el mismo resultado, ¿cuántos latidos contaste en total?", "20*3", "Se multiplican latidos por mediciones.", " latidos"),
        ],
    },
    context=[ex("Antes de la clase de Educación Física te sientes tranquilo, con la cara normal. La profesora pide que anotes tus señales. ¿Qué anotas: A) que estás cansado, B) que estás en reposo, C) que estás enojado?", "B", "Tus señales son de reposo.")],
    selfcheck=[
        ex("¿Dónde pones la mano para sentir el corazón?", "En el pecho", "Se siente el latido."),
        ex("¿Cuántos segundos cuentas?", "15", "Es el tiempo de registro."),
        ex("¿Por qué anotas antes de moverte?", "Para comparar después", "Se ve el cambio."),
    ],
    open_task=task("Dibuja una silueta del cuerpo. Con un adulto que mire el reloj, siéntate tranquilo 1 minuto. Luego pon la mano en el pecho y cuenta tus latidos durante 15 segundos. Anota en la silueta: tu número de latidos, cómo es tu respiración (tranquila o rápida), cómo es el color de tu cara (normal o rojo) y si sientes calor. Guarda tu hoja para la próxima clase.",
                   "Conté 19 latidos en 15 segundos. Respiración tranquila, cara de color normal, sin calor. Estoy en reposo.",
                   ["hace el conteo en 15 segundos", "anota cuatro señales", "no compara con otros"],
                   ["silueta con anotaciones", "número escrito", "relato oral"],
                   ["contar mal el tiempo", "olvidar señales", "compararse"],
                   "Pregunta qué señal fue más fácil de notar y refuerza el registro tranquilo."),
    reinforce="Pon la mano en el pecho 15 segundos y cuenta tus latidos tres veces.",
    extend="Anota tu respiración, tu color y tus latidos en la mañana y en la tarde de un día de descanso.",
)

register(
    OA8, 2,
    materials="Tu silueta de la clase anterior, lápiz rojo y azul, reloj con segundos, agua, un espacio de 4 × 4 m y la escala del habla de esta clase.",
    use="Aprenderé a notar cómo cambia mi cuerpo cuando me muevo fuerte. Sirve para saber cuándo estoy haciendo mucho esfuerzo.",
    prior=["Sé contar mis latidos en 15 segundos.", "Sé usar la escala del habla."],
    explain=[
        "Cuando haces ejercicio, tu cuerpo cambia. Tu corazón late más rápido para llevar sangre a los músculos. Respiras más rápido para tomar más aire. Tu cara se pone más roja porque llega más sangre a la piel. Empiezas a sudar para enfriar el cuerpo y sientes calor. También te cansas y te cuesta hablar.",
        "Estas respuestas son normales cuando haces actividad. Pero si el cambio es muy grande, tu cuerpo te está diciendo que bajes el ritmo. " + SCALE,
        "Para observar el cambio, haz 40 segundos de trote suave y salto en el lugar, y mide ahí mismo: tus latidos durante 15 segundos, tu respiración (rápida o tranquila), tu piel (más roja o normal), el sudor (sí o no) y qué nivel de la escala del habla sientes.",
    ],
    vocab=[("sudor", "agua que sale de la piel para enfriar el cuerpo"), ("agitación", "respiración rápida por el esfuerzo"), ("cambio de color", "la piel se pone más roja"), ("cansancio", "sensación de que el cuerpo necesita descanso"), ("dificultad al hablar", "me cuesta decir frases largas")],
    worked=[
        W("Comparar latidos", "En reposo contaste 18 latidos en 15 segundos y después del ejercicio 32. ¿Cuántos más hay?", ["Latidos del ejercicio: 32.", "Latidos en reposo: 18.", "32 − 18 = 14."], "14 latidos más."),
        W("Leer las señales", "Después de saltar sientes calor, tienes la cara roja, respiras rápido y dices solo palabras sueltas. ¿Qué nivel de la escala es y qué haces?", ["Solo palabras sueltas es nivel 4.", "Mi cuerpo está trabajando mucho.", "Bajo el ritmo y bebo agua."], "Nivel 4; bajo el ritmo y bebo agua."),
    ],
    mistakes=[M("Pensar que sudar mucho es malo.", "No se sabe que el sudor enfría.", "El sudor es normal; repón agua después."),
              M("Seguir al nivel 5 sin parar.", "Se quiere seguir jugando.", "Si no puedes hablar, para y descansa.")],
    tiers={
        "recovery": [
            ex("Durante el ejercicio, ¿tu corazón late más rápido o más lento?", "Más rápido", "Lleva más sangre a los músculos."),
            ex("El sudor sirve para ¿enfriar el cuerpo o ensuciar la ropa?", "Enfriar el cuerpo", "Es su función."),
            ex("Con el ejercicio, ¿tu cara se pone más roja o más blanca?", "Más roja", "Llega más sangre a la piel."),
        ],
        "understand": [
            ex("¿Por qué respiras más rápido al correr?", "Para tomar más aire", "Los músculos lo necesitan."),
            ex("¿Es normal tener calor y sudar al hacer ejercicio?", "Sí", "Son respuestas normales."),
            ex("¿Qué significa dificultad al hablar?", "Me cuesta decir frases largas", "Es una señal de esfuerzo fuerte."),
        ],
        "apply": [
            arith("En reposo 18 latidos y tras el ejercicio 30, en 15 segundos. ¿Cuántos latidos más?", "30-18", "Se resta.", " latidos"),
            ex("Después de correr dices solo «sí» y «no». ¿Qué nivel de la escala es?", "4", "Decir solo palabras sueltas es nivel 4."),
            arith("Haces 3 intentos de 30 segundos de acción. ¿Cuántos segundos son?", "3*30", "Se multiplican.", " segundos"),
        ],
        "reason": [
            ex("Ana dice «no puedo hablar nada y me mareo». ¿Sigue jugando?", "No, debe parar y avisar", "Es una señal de peligro."),
            ex("Beto está muy rojo, pero puede hablar frases cortas y respira rápido. ¿Debe parar?", "No necesariamente; está en nivel 3", "Son respuestas normales."),
        ],
        "challenge": [
            ex("Cuatro señales: más latidos, sudor, cara roja y respiración rápida. Si en un juego notas las cuatro, ¿cuántas señales notaste?", "4", "Se cuentan las cuatro señales."),
            arith("Reposo: 18 latidos. Moderado: 26. Vigoroso: 34. ¿Cuántos latidos más tiene el vigoroso que el reposo?", "34-18", "Se restan.", " latidos"),
        ],
    },
    context=[ex("Juegas a pillarse y sientes calor, mucho sudor y la cara roja, pero puedes hablar. ¿Qué haces: A) sigues y bebes agua en la pausa, B) gritas, C) te acuestas?", "A", "Son respuestas normales; repón agua.")],
    selfcheck=[
        ex("¿Qué hace el corazón durante el ejercicio?", "Late más rápido", "Lleva más sangre."),
        ex("¿Para qué sirve el sudor?", "Para enfriar el cuerpo", "Es una respuesta normal."),
        ex("Cuando tu cuerpo ya no te deja hablar nada, ¿sigues jugando o descansas?", "Descansas", "Es nivel 5 de la escala."),
    ],
    open_task=task("Haz 40 segundos de trote suave en el lugar y saltos con un adulto que mire el reloj. Justo al terminar anota: latidos en 15 segundos (compara con tu número de reposo; usa 18 si no lo tienes), respiración (rápida o tranquila), color de la piel (más roja o normal), sudor (sí o no) y nivel de la escala del habla. Escribe en una frase qué cambió más.",
                   "Latidos: 30 en 15 segundos (12 más que en reposo). Respiración rápida, piel más roja, sudor poco y nivel 3. Lo que más cambió fueron mis latidos.",
                   ["registra las cinco señales", "compara con el reposo", "identifica el cambio mayor"],
                   ["tabla de señales", "silueta con colores", "relato oral"],
                   ["no comparar", "saltarse señales", "seguir al nivel 5"],
                   "Pregunta qué señal le dice que debe bajar el ritmo y refuerza la comparación con su reposo."),
    reinforce="Trota suave 20 segundos y cuenta tus latidos en 15 segundos; compáralos con tu reposo.",
    extend="Compara tus señales después de trotar suave y después de saltar fuerte; ¿cuál cambió más?",
)

register(
    OA8, 3,
    materials="Tu silueta, el registro de latidos de las clases anteriores, un reloj con segundos y agua. Se hace un esfuerzo corto de 30 segundos y luego se mide la recuperación.",
    use="Aprenderé a ver cómo mi cuerpo vuelve poco a poco a la calma después de moverme. Sirve para saber cuándo puedo seguir jugando.",
    prior=["Sé contar latidos en 15 segundos.", "Sé las señales del ejercicio."],
    explain=[
        "Después de moverte, tu cuerpo necesita recuperarse. Recuperarse es volver poco a poco al reposo: el corazón late más lento, la respiración se calma, el sudor disminuye y la cara vuelve a su color. Esto ocurre en minutos, no en un instante.",
        "Para recuperarte, camina despacio un minuto, bebe agua en sorbos y respira profundo, llevando el aire por la nariz y soltándolo por la boca. No te sientes ni te acuestes de golpe. Cuando puedes hablar con calma y tu corazón late casi como en reposo, ya estás recuperado.",
        "Cada persona se recupera a su ritmo. Algunos tardan 1 minuto y otros 3. No es una competencia. Si en cualquier momento te mareas, te duele algo o no puedes hablar, avisa de inmediato a un adulto. Si después de 5 minutos sigues muy agitado, también avisa.",
    ],
    vocab=[("recuperación", "volver poco a poco al reposo"), ("respirar profundo", "tomar aire lento por la nariz"), ("calma", "estar tranquilo"), ("sorbo", "trago pequeño"), ("avisar", "decirle a un adulto lo que me pasa")],
    worked=[
        W("Recuperación de latidos", "Después de correr contaste 32 latidos en 15 segundos. A los 2 minutos contaste 22. ¿Cuántos bajaron?", ["Después de correr: 32.", "A los 2 minutos: 22.", "32 − 22 = 10."], "Bajaron 10 latidos."),
        W("Cuándo estoy recuperado", "Tras 3 minutos caminas despacio, hablas con calma y la cara está normal. ¿Qué concluyes?", ["Hablo con calma.", "La cara está normal.", "Mi cuerpo vuelve al reposo."], "Estoy recuperado."),
    ],
    mistakes=[M("Sentarse o acostarse de golpe.", "Se quiere descansar rápido.", "Camina despacio un minuto antes de sentarte."),
              M("Compararse con un compañero que se recuperó antes.", "Se cree que es una competencia.", "Cada uno se recupera a su ritmo.")],
    tiers={
        "recovery": [
            ex("Recuperarse es volver al...", "Reposo", "Es el estado tranquilo."),
            ex("Para recuperarte, ¿caminas despacio o corres?", "Caminas despacio", "Baja el ritmo gradualmente."),
            ex("El agua se toma en ¿sorbos o de golpe?", "Sorbos", "Es más cómodo."),
        ],
        "understand": [
            ex("¿Por qué no te sientas de golpe después de correr?", "Para que el cuerpo baje el ritmo de a poco", "Así se evitan los mareos."),
            ex("¿Se recupera todo el mundo en el mismo tiempo?", "No", "Cada persona tiene su ritmo."),
            ex("¿Qué haces si pasan 5 minutos y sigues sin poder hablar?", "Avisar a un adulto", "Puede ser una señal que requiere ayuda."),
        ],
        "apply": [
            arith("Después de correr 32 latidos; a los 2 minutos 24. ¿Cuántos bajaron?", "32-24", "Se resta.", " latidos"),
            ex("Latidos en reposo: 18. Después del esfuerzo: 32. A los 3 minutos: 20. ¿Está más cerca del reposo que del esfuerzo?", "Sí", "20 está más cerca de 18 que de 32."),
            arith("Caminas despacio 1 minuto y respiras profundo 30 segundos. ¿Cuántos segundos son en total?", "60+30", "Se pasa el minuto a segundos y se suma.", " segundos"),
        ],
        "reason": [
            ex("Ema dice «me recuperé antes que Beto, soy mejor». ¿Qué le dices?", "Que cada uno se recupera a su ritmo", "No es competencia."),
            ex("Dani se sienta de golpe y se marea. ¿Qué debe hacer la próxima vez?", "Caminar despacio antes de sentarse", "El cuerpo necesita bajar el ritmo."),
        ],
        "challenge": [
            ex("Orden para recuperarte: A) beber sorbos de agua, B) caminar despacio, C) hablar con calma. ¿Cuál es el orden más lógico?", "B, A, C", "Primero bajas el ritmo, luego te hidratas y compruebas."),
            arith("Una persona se recupera en 2 minutos y otra en 3. ¿Cuántos segundos de diferencia hay?", "(3-2)*60", "Un minuto tiene 60 segundos.", " segundos"),
        ],
    },
    context=[ex("Acabas de correr en el patio y tu amigo te dice «siéntate de una vez». ¿Qué haces: A) te sientas ya, B) caminas despacio 1 minuto y bebes sorbos, C) corres más?", "B", "Es la forma de recuperarse.")],
    selfcheck=[
        ex("¿Qué haces para recuperarte?", "Caminar despacio y beber sorbos", "Bajas el ritmo."),
        ex("Tras trotar, ¿qué dos señales muestran que ya estás recuperado?", "Hablas con calma y el corazón late casi como en reposo", "Son señales de reposo."),
        ex("¿Es una competencia recuperarse?", "No", "Cada uno tiene su ritmo."),
    ],
    open_task=task("Haz 30 segundos de saltos suaves en el lugar. Justo al terminar, cuenta tus latidos 15 segundos (anótalo). Camina despacio 1 minuto, bebe sorbos de agua y respira profundo 3 veces. Cuenta de nuevo 15 segundos (al minuto). Sigue caminando despacio y cuenta otra vez a los 2 minutos. Anota los 3 números y cuándo ya podías hablar con calma.",
                   "Tras saltar: 30. A 1 minuto: 25. A 2 minutos: 20. Hablaba con calma a los 2 minutos. Mi reposo es 18.",
                   ["mide tres veces", "camina y toma agua en sorbos", "interpreta cuándo se recuperó"],
                   ["tabla de latidos", "silueta con anotaciones", "relato oral"],
                   ["sentarse de golpe", "compararse con otros", "no repetir la medición"],
                   "Reconoce la tabla y pregunta cómo supo que se recuperó."),
    reinforce="Camina despacio 1 minuto y respira profundo 3 veces después de trotar.",
    extend="Compara tu recuperación tras 30 segundos de trote suave y tras 30 de trote más rápido.",
)

register(
    OA8, 4,
    materials="Tarjetas escritas aquí (puedes copiarlas en papel): «me falta el aire», «me duele el pecho», «me mareo», «tengo sed», «tengo calor», «me duele una rodilla». Una hoja para clasificar y lápiz.",
    use="Aprenderé a decidir qué hacer según lo que siento: seguir, bajar el ritmo o parar y avisar. Sirve para cuidarme en el juego.",
    prior=["Sé las señales del ejercicio.", "Sé usar la escala del habla."],
    explain=[
        "Algunas señales son normales durante el ejercicio: calor, sudor, cara roja, respiración rápida y corazón más rápido. En esos casos, puedes seguir si puedes hablar frases cortas, o bajar un poco el ritmo si estás en nivel 4.",
        "Otras señales significan que debes parar y avisar a un adulto: dolor en el pecho, mareo, náuseas, falta de aire que no te deja hablar o que no mejora al parar, dolor en una articulación o un golpe. Paras de inmediato, te sientas con cuidado y avisas. No esperes a que termine el juego.",
        "Si tienes sed, bebes agua en la pausa. Si tienes calor, vas a la sombra y bebes. Para decidir, pregúntate: ¿puedo hablar? ¿me duele algo? ¿me siento mareado? Si la respuesta a dolor o mareo es sí, paras y avisas. Pedir ayuda es cuidar tu cuerpo.",
    ],
    vocab=[("autocuidado", "cuidar mi propio cuerpo"), ("señal de alerta", "señal que pide parar y avisar"), ("avisar", "decirle a un adulto lo que me pasa"), ("hidratarse", "beber agua"), ("articulación", "parte donde se doblan los huesos, como la rodilla")],
    worked=[
        W("Clasificar una señal", "Tu tarjeta dice «me mareo». ¿Sigues, bajas el ritmo o paras y avisas?", ["Mareo es una señal de alerta.", "No se espera a que termine el juego.", "Me siento con cuidado y aviso a un adulto."], "Paro y aviso a un adulto."),
        W("Decidir por sed", "Tu tarjeta dice «tengo sed». ¿Qué haces?", ["La sed es una señal normal.", "En la pausa bebo agua.", "Luego sigo si estoy bien."], "Bebo agua en la pausa."),
    ],
    mistakes=[M("Seguir jugando con dolor en el pecho.", "No se quiere dejar el juego.", "Para de inmediato y avisa."),
              M("No avisar por vergüenza.", "Se piensa que es un problema pequeño.", "Avisar siempre es correcto.")],
    tiers={
        "recovery": [
            ex("Si te mareas, ¿sigues jugando o paras y avisas?", "Paras y avisas", "Es una señal de alerta."),
            ex("Si tienes sed, ¿bebes agua o sigues sin tomar?", "Bebes agua", "El agua te repone."),
            ex("Si tienes calor y mucho sudor pero hablas normal, ¿es una señal normal?", "Sí", "Son respuestas al ejercicio."),
        ],
        "understand": [
            ex("¿Por qué avisar a un adulto cuando duele el pecho?", "Para que un adulto me ayude", "Un adulto sabrá qué hacer."),
            ex("Si sientes un dolor en una rodilla, ¿qué haces?", "Parar y avisar", "Podría ser una lesión."),
            ex("¿Pedir ayuda es una señal de debilidad?", "No", "Es cuidar el cuerpo."),
        ],
        "apply": [
            ex("Tarjeta «tengo calor». ¿Sombra y agua o seguir corriendo?", "Sombra y agua", "Ayuda a enfriar."),
            ex("Tarjeta «me falta el aire». Después de parar no mejora. ¿Qué haces?", "Avisar a un adulto", "Falta de aire que no mejora es alerta."),
            ex("Tarjeta «me duele una rodilla». ¿Sigues o paras?", "Paras", "Puede lastimarse más."),
        ],
        "reason": [
            ex("Beto se marea y dice «espero a que termine el juego». ¿Qué le dices?", "Que pare ahora", "No se espera."),
            ex("Ema dice «sudo mucho, voy a parar». Pero puede hablar y no le duele nada. ¿Es necesario parar?", "No; bebe agua en la pausa", "Sudar es normal."),
        ],
        "challenge": [
            ex("Clasifica estas tarjetas en normales o de alerta: tengo sed, me mareo, tengo calor, me duele el pecho. ¿Cuántas son de alerta?", "2", "Mareo y dolor de pecho."),
            arith("Un juego tiene 3 pausas de 30 segundos para beber agua. ¿Cuántos segundos de pausa son?", "3*30", "Se multiplican pausas por segundos.", " segundos"),
        ],
    },
    context=[ex("Juegas en el patio con calor. De pronto sientes un dolor fuerte en el pecho. ¿Qué haces: A) sigues a ver si pasa, B) paras y avisas a un adulto, C) bebes y corres?", "B", "El dolor en el pecho es una alerta.")],
    selfcheck=[
        ex("Dos señales de alerta son...", "Mareo y dolor en el pecho", "Hay que parar y avisar."),
        ex("¿Qué haces con la sed?", "Bebes agua", "Es una señal normal."),
        ex("¿Avisar es cuidarse?", "Sí", "Un adulto puede ayudar."),
    ],
    open_task=task("Con las tarjetas escritas en esta clase («me falta el aire», «me duele el pecho», «me mareo», «tengo sed», «tengo calor», «me duele una rodilla»), dibuja dos columnas: «puedo seguir o bajar el ritmo» y «paro y aviso». Coloca cada tarjeta donde corresponda y escribe la acción de cada una. Cuenta cuántas quedaron en cada columna.",
                   "Seguir o bajar: tengo sed (bebo agua), tengo calor (sombra y agua). Paro y aviso: me falta el aire, me duele el pecho, me mareo, me duele una rodilla. 2 en una columna y 4 en la otra.",
                   ["clasifica bien las seis tarjetas", "escribe una acción por tarjeta", "cuenta las columnas"],
                   ["columnas dibujadas", "relato oral", "tarjetas ordenadas"],
                   ["seguir con dolor", "no avisar", "mezclar señales normales y de alerta"],
                   "Refuerza que avisar es correcto y pide una situación de la vida real."),
    reinforce="Escribe en una hoja dos señales normales y dos de alerta.",
    extend="Explica a un familiar qué haces si te mareas jugando, paso a paso.",
)
