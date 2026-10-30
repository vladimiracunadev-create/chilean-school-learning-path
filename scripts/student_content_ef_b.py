"""Student material for 1.º básico Educación Física y Salud, OA 03 (juegos), OA 04 (entornos diversos) y OA 05 (expresión corporal)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


OA3, OA4, OA5 = "EF01 OA 03", "EF01 OA 04", "EF01 OA 05"

# ---------------------------------------------------------------- OA 03
register(
    OA3, 1,
    materials="Un espacio de 4 × 4 m, 5 bolitas de papel o tapas, una caja o canasto, 4 conos o botellas vacías para los límites y un reloj. Cada niño juega en su propio carril.",
    use="Aprenderé a jugar un juego donde nadie compite contra otro, siguiendo reglas y cuidando el espacio. Sirve para disfrutar y mejorar mi propio desempeño.",
    prior=["Sé esperar mi turno.", "Sé caminar sin empujar."],
    explain=[
        "Hay juegos sin oposición. En ellos nadie intenta quitarte algo ni impedir que logres tu meta. Puedes jugar solo o junto a otros, pero cada uno trata de mejorar su propio resultado. Es un juego individual si juegas por tu cuenta y colectivo si juegan varios al mismo tiempo.",
        "Todo juego tiene reglas. Las reglas dicen qué se puede hacer, qué no se puede hacer, dónde se juega y cuándo termina. Si todos conocen las reglas y las cumplen, el juego es seguro y divertido. Antes de jugar, repite la regla más importante en voz alta.",
        "Cuidar el espacio significa quedarte dentro de los límites y mantener una distancia de dos brazos con los demás. Si hay un objeto en el suelo, lo avisas y lo guardas. Si alguien se sale del límite, se le recuerda con amabilidad, sin gritar.",
    ],
    vocab=[("sin oposición", "nadie intenta impedir que logres tu meta"), ("regla", "lo que se puede y no se puede hacer en el juego"), ("límite", "línea o marca que dice hasta dónde se juega"), ("individual", "que juego yo, por mi cuenta"), ("meta", "lo que quiero lograr en el juego")],
    worked=[
        W("Juego «Tesoro en la ruta»", "Reglas: 1) hay 5 bolitas de papel a un lado del cuadrado y una caja al lado contrario; 2) cada niño juega en su carril; 3) lleva una bolita a la vez, caminando; 4) el juego termina cuando las 5 están en la caja o suenan 60 segundos. Si llevas 3 bolitas, ¿cuántas te faltan?", ["La meta es llevar las 5 bolitas.", "Ya llevé 3.", "5 − 3 = 2."], "Me faltan 2 bolitas."),
        W("Revisar los límites", "Antes de jugar, el adulto te muestra 4 conos que marcan el cuadrado y una zona de espera. ¿Dónde juegas y dónde esperas?", ["Juego solo dentro de los conos.", "Cuando no es mi turno, espero en la zona de espera.", "Mantengo dos brazos de distancia con los demás."], "Juego dentro de los conos y espero en la zona de espera."),
    ],
    mistakes=[M("Cambiar la regla sin avisar.", "Se quiere que sea más fácil.", "Si quieres cambiarla, propónlo y acuerden todos antes de jugar."),
              M("Salirse del límite para llegar primero.", "Se piensa que ganar vale más que cuidar a otros.", "Quédate dentro del cuadrado; en este juego importa cumplir la meta.")],
    tiers={
        "recovery": [
            ex("En un juego sin oposición, ¿alguien intenta impedir que logres tu meta?", "No", "Sin oposición significa que nadie lo impide."),
            ex("Las reglas, ¿dicen qué se puede hacer o solo qué se puede comer?", "Qué se puede hacer", "Son acuerdos sobre cómo jugar."),
            ex("Los límites del juego se marcan con...", "Conos o líneas", "Muestran hasta dónde se juega."),
        ],
        "understand": [
            ex("¿Por qué se necesita una distancia de dos brazos entre las personas?", "Para no chocar", "Esa distancia evita golpes."),
            ex("Un juego donde juego yo solo contra el tiempo, ¿es individual o colectivo?", "Individual", "Hay un solo jugador."),
            ex("Si alguien se sale del límite, ¿qué haces: le avisas con amabilidad o gritas?", "Le avisas con amabilidad", "Así se respeta a los demás."),
        ],
        "apply": [
            arith("El juego tiene 5 bolitas y llevas 4 a la caja. ¿Cuántas faltan?", "5-4", "Se resta lo llevado de lo total.", " bolita"),
            ex("En «Tesoro en la ruta» solo se lleva una bolita a la vez. Si llevas 2 bolitas juntas, ¿cumples la regla?", "No", "Debes llevar solo una por vez."),
            arith("El juego dura 60 segundos y has jugado 45. ¿Cuántos segundos faltan?", "60-45", "Se resta el tiempo jugado del total.", " segundos"),
        ],
        "reason": [
            ex("Beto dice: «es más rápido llevar las 5 bolitas juntas». ¿Qué pasa con la regla y con la seguridad?", "Rompe la regla y puede tropezar", "Cargar muchas a la vez hace perder el control."),
            ex("En el juego tú y Caro llevan bolitas en carriles diferentes. ¿Es un juego sin oposición? Responde sí o no.", "Sí", "Nadie impide que el otro logre su meta."),
        ],
        "challenge": [
            ex("Quieres que el juego sea más difícil sin dejar de ser seguro. Elige una: A) correr, B) llevar las bolitas con la mano izquierda, C) saltar por encima del compañero. ¿Cuál es segura?", "B", "Cambia la tarea sin añadir riesgo."),
            arith("En 3 intentos llevas 5 bolitas cada vez. ¿Cuántas bolitas llevas en total?", "3*5", "Se multiplican los intentos por las bolitas.", " bolitas"),
        ],
    },
    context=[ex("En el recreo tus amigos juegan a pasar bolitas a una caja, cada uno en su fila. De pronto uno corre y empuja a otro. ¿Qué regla se rompió: A) cuidar el espacio, B) usar el color rojo, C) cantar?", "A", "Empujar no cuida el espacio de los demás.")],
    selfcheck=[
        ex("¿Qué es una regla?", "Lo que se puede y no se puede hacer", "Ordena el juego."),
        ex("En un juego sin oposición, ¿el otro jugador me quita la meta?", "No", "Nadie lo impide."),
        ex("¿Qué distancia se mantiene entre las personas?", "Dos brazos", "Sirve para evitar choques."),
    ],
    open_task=task("Juega «Tesoro en la ruta» con 5 bolitas de papel, una caja y un cuadrado de 4 × 4 m marcado con 4 objetos. Reglas: llevas una bolita a la vez, caminando, dentro del cuadrado; el juego termina cuando están las 5 en la caja o pasan 60 segundos. Juega 3 veces y anota cuántas bolitas llevaste cada vez. Di cuál regla fue la más importante.",
                   "Lleve 4, 5 y 5 bolitas. La regla más importante fue caminar y llevar una a la vez para no tropezar. Me quedé dentro del cuadrado las 3 veces.",
                   ["sigue las reglas del juego", "se mantiene dentro de los límites", "explica una regla importante"],
                   ["registro de 3 intentos", "observación de un adulto", "relato oral de la regla"],
                   ["cambiar la regla sin avisar", "salirse del cuadrado", "llevar más de una bolita"],
                   "Reconoce el cumplimiento de reglas y pregunta qué cambiaría para que sea más desafiante sin riesgo."),
    reinforce="Camina llevando una tapa en la mano de un cono a otro, 5 veces, sin salirte del cuadrado.",
    extend="Inventa una regla nueva para el juego que lo haga más desafiante y seguro, y pruébala con un adulto.",
)

register(
    OA3, 2,
    materials="Una pelota blanda o un globo, un círculo de 4–6 personas (pueden ser familiares), un reloj y un espacio de 4 × 4 m.",
    use="Aprenderé a jugar con otros para lograr una meta en común. Sirve para pasar bien con la familia y los compañeros, y para ganar entre todos.",
    prior=["Sé lanzar y recibir una pelota blanda.", "Sé decir el nombre de un compañero."],
    explain=[
        "En un juego con colaboración, todos ayudan para lograr la misma meta. Si uno se equivoca, el equipo no se enoja: lo ayuda y lo vuelve a intentar. Nadie gana solo; ganan juntos o pierden juntos.",
        "En el juego «El globo que no cae» el equipo debe mantener un globo en el aire dando golpes suaves con las manos. Reglas: nadie puede golpear dos veces seguidas, hay que decir en voz alta el nombre de quien recibirá el siguiente golpe, y el globo no puede tocar el suelo. Se cuenta cuántos golpes seguidos logra el grupo.",
        "Para coordinar, miren el globo, hablen claro y cuiden el espacio. Si el globo va hacia alguien, esa persona dice «yo». Si dos personas van al mismo lugar, una cede. Los golpes son suaves y con las manos abiertas.",
    ],
    vocab=[("colaborar", "ayudar para lograr la misma meta"), ("equipo", "grupo que juega junto"), ("coordinar", "ponerse de acuerdo para hacer algo a la vez"), ("turno", "momento de cada uno"), ("ceder", "dejar que otro tome mi lugar")],
    worked=[
        W("Contar golpes", "El equipo da 3 golpes seguidos, luego el globo cae. En el segundo intento da 5, y en el tercero, 7. ¿Cuántos golpes dieron en total en los tres intentos?", ["Sumo los golpes de cada intento: 3 + 5 + 7.", "3 + 5 = 8.", "8 + 7 = 15."], "15 golpes en total."),
        W("Cuidar al equipo", "Un compañero golpea el globo y este va hacia ti. Otro compañero también corre hacia el globo. ¿Qué haces?", ["Digo «yo» fuerte para avisar.", "Miro al compañero y le doy el paso si está más cerca.", "Lo animo si falla: «¡otra vez!»."], "Aviso, cedo si el otro está más cerca y animo."),
    ],
    mistakes=[M("Golpear el globo dos veces seguidas.", "Se quiere asegurar el golpe.", "Deja que otro lo reciba; la regla es no repetir."),
              M("Retar al compañero que dejó caer el globo.", "Se siente enojo.", "Anima al equipo y vuelvan a intentarlo juntos.")],
    tiers={
        "recovery": [
            ex("En un juego con colaboración, ¿todos buscan la misma meta o metas distintas?", "La misma meta", "Colaborar es ayudar en la misma meta."),
            ex("Si el globo cae al suelo, ¿el equipo empieza de nuevo o se rinde?", "Empieza de nuevo", "Se intenta otra vez."),
            ex("Antes de golpear el globo, ¿dices el nombre de quien lo recibirá o te quedas callado?", "Dices el nombre", "Es la regla para coordinar."),
        ],
        "understand": [
            ex("¿Por qué no se permite golpear dos veces seguidas?", "Para que participen todos", "Así más personas juegan."),
            ex("Si dos personas van al mismo lugar, ¿qué hacen: chocan o una cede?", "Una cede", "Ceder evita golpes."),
            ex("¿Qué dices a un compañero que dejó caer el globo?", "Otra vez, tú puedes", "Animar ayuda al equipo."),
        ],
        "apply": [
            arith("El equipo logró 6 golpes en el primer intento y 9 en el segundo. ¿Cuántos golpes sumaron?", "6+9", "Se suman los golpes de ambos intentos.", " golpes"),
            ex("Hay 5 jugadores y cada uno golpea una vez en cada ronda. ¿Cuántos golpes hay en 2 rondas?", "10", "5 por 2 son 10."),
            arith("Quieren lograr 20 golpes seguidos y ya llevan 14. ¿Cuántos faltan?", "20-14", "Se resta lo logrado de la meta.", " golpes"),
        ],
        "reason": [
            ex("En un intento, Ema golpea tres veces seguidas y los demás miran. ¿Qué regla rompe?", "No golpear dos veces seguidas", "Debe pasar el turno a otro."),
            ex("Fito dice «yo juego solo, así gano». ¿Es colaborar?", "No", "Colaborar es lograr la meta entre todos."),
        ],
        "challenge": [
            arith("Hacen 4 intentos: 5, 7, 8 y 6 golpes. ¿Cuántos golpes seguidos fue el mejor intento menos el peor?", "8-5", "Se resta el peor del mejor.", " golpes"),
            ex("Para que el juego sea más difícil, proponen usar dos globos a la vez. ¿Qué regla nueva ayuda a la seguridad?", "Que todos digan «yo» y que se mantengan a distancia", "Con más globos hay más riesgo de chocar."),
        ],
    },
    context=[ex("En tu casa juegan 4 personas a mantener un globo en el aire. Uno se enoja porque el globo cayó. ¿Qué haces: A) lo retas, B) le dices «vamos otra vez, juntos», C) te vas?", "B", "Colaborar es animarse y seguir.")],
    selfcheck=[
        ex("En un juego con colaboración, ¿se gana solo o juntos?", "Juntos", "La meta es compartida."),
        ex("¿Qué se dice antes de golpear el globo?", "El nombre de quien lo recibe", "Ayuda a coordinar."),
        ex("Si el equipo logra 5 y luego 8 golpes, ¿cuántos suman?", "13", "5 más 8 son 13."),
    ],
    open_task=task("Reúne a 3 o más personas (familiares o compañeros) y un globo. Jueguen «El globo que no cae» 3 intentos de 30 segundos cada uno. Reglas: nadie golpea dos veces seguidas, se dice el nombre de quien recibe y el globo no toca el suelo. Anota cuántos golpes lograron en cada intento y qué hicieron para coordinarse.",
                   "Intentos: 8, 11 y 14 golpes. Nos coordinamos diciendo el nombre antes de golpear y cuidando el espacio. Mejoramos 6 golpes del primero al último.",
                   ["cumple las reglas del juego", "dice el nombre de quien recibirá", "anima al equipo y cuida el espacio"],
                   ["registro de tres intentos", "observación de un adulto", "relato oral de una decisión del equipo"],
                   ["golpear dos veces seguidas", "olvidar decir el nombre", "enojarse con quien falló"],
                   "Resalta una acción colaborativa concreta y pide proponer un cambio para mejorar en el siguiente intento."),
    reinforce="Con un adulto, pasen un globo de uno a otro 10 veces seguidas, diciendo el nombre antes de cada golpe.",
    extend="Con 4 personas, intenten llegar a 25 golpes seguidos; anota qué estrategia usaron.",
)

register(
    OA3, 3,
    materials="Un espacio de 4 × 4 m con conos en las esquinas, un pañuelo o cinta que cada jugador lleva sujeto a la cintura por un lado (para el juego de persecución) y reloj.",
    use="Aprenderé a jugar un juego de persecución con oposición de forma segura, sin empujar. Sirve para jugar a las «pilladas» en el recreo sin lastimar a nadie.",
    prior=["Sé correr con control y detenerme.", "Sé que no se empuja a otros."],
    explain=[
        "En un juego con oposición, un jugador intenta impedir que otro logre su meta. En el juego «Pillada de cinta», un jugador es el perseguidor y trata de sacar la cinta de la cintura de los demás. Los otros esquivan. Es un juego de persecución con oposición.",
        "Para jugar con seguridad: sólo se saca la cinta, no se toca el cuerpo, no se empuja, no se agarra la ropa y no se tira a nadie. Se juega a 70 % de la velocidad máxima; si alguien se detiene, se detienen todos. El perseguidor cuenta hasta 3 antes de empezar.",
        "Anticipar significa mirar a los otros y adivinar hacia dónde irán. Si el perseguidor va hacia la derecha, tú puedes ir a la izquierda. Mira siempre hacia dónde corres y mantén la cabeza arriba. Los límites del cuadrado no se cruzan.",
    ],
    vocab=[("oposición", "alguien trata de impedir que logres tu meta"), ("persecución", "juego donde uno persigue y otros escapan"), ("perseguidor", "jugador que trata de sacar la cinta"), ("esquivar", "cambiar de dirección para que no me alcancen"), ("anticipar", "adivinar lo que hará otro y prepararme")],
    worked=[
        W("Reglas de seguridad", "En «Pillada de cinta», un jugador te agarra la camiseta para sacarte la cinta. ¿Qué regla se rompió y qué haces?", ["La regla dice que sólo se saca la cinta, sin agarrar la ropa.", "Digo «alto» y todos se detienen.", "Pido al adulto que repita la regla y seguimos."], "Se rompió la regla de no agarrar la ropa; digo «alto»."),
        W("Contar cintas", "Hay 6 jugadores con cinta y el perseguidor saca 2 en la primera ronda y 3 en la segunda. ¿Cuántas cintas ha sacado en total?", ["En la primera, 2.", "En la segunda, 3.", "2 + 3 = 5."], "5 cintas."),
    ],
    mistakes=[M("Empujar para escapar.", "Se siente apuro.", "Esquiva cambiando de dirección; no se toca a nadie."),
              M("Correr mirando hacia atrás.", "Se quiere ver al perseguidor.", "Mira hacia delante y anticipa; si hay obstáculos, cambia de dirección con calma.")],
    tiers={
        "recovery": [
            ex("En «Pillada de cinta», ¿qué se saca: la cinta o la ropa?", "La cinta", "La regla dice que sólo se saca la cinta."),
            ex("Los jugadores que escapan, ¿esquivan o empujan?", "Esquivan", "Empujar no está permitido."),
            ex("Si dicen «alto», ¿qué hacen todos?", "Se detienen", "Es la señal de parar."),
        ],
        "understand": [
            ex("¿Por qué se juega a menos de la velocidad máxima?", "Para tener control y evitar choques", "Menos velocidad da más control."),
            ex("¿Qué es anticipar?", "Adivinar lo que hará otro", "Se mira y se piensa hacia dónde irá."),
            ex("¿Es un juego de persecución o de lanzar?", "De persecución", "El perseguidor corre tras los otros."),
        ],
        "apply": [
            arith("Hay 8 jugadores con cinta. Si sacan 3 cintas, ¿cuántos siguen con cinta?", "8-3", "Se restan las cintas sacadas.", " jugadores"),
            ex("El perseguidor va hacia tu derecha. ¿Hacia qué lado esquivas?", "A tu izquierda", "Cambias a la dirección contraria."),
            arith("El juego tiene 3 rondas de 30 segundos de acción. ¿Cuántos segundos de acción hay en total?", "3*30", "Se multiplican rondas por segundos.", " segundos"),
        ],
        "reason": [
            ex("Beto se cae porque corre mirando hacia atrás. ¿Qué consejo le das?", "Mirar hacia adelante", "Así ve obstáculos y no se cae."),
            ex("Ana agarra a Caro de la camiseta para sacarle la cinta. ¿Es seguro?", "No", "Agarrar la ropa puede hacer caer."),
        ],
        "challenge": [
            ex("Hay un compañero con una rodilla vendada que no puede correr rápido. Elige: A) que no juegue, B) que sea perseguidor y los demás caminen rápido, C) que corra igual. ¿Cuál es mejor?", "B", "Cambia la regla para incluirlo y mantener la seguridad."),
            arith("Una ronda tiene 30 segundos de acción y 30 de pausa. ¿Cuántos segundos duran 4 rondas completas?", "(30+30)*4", "Cada ronda tiene acción y pausa.", " segundos"),
        ],
    },
    context=[ex("En el patio, unos niños juegan a pillarse y uno empuja fuerte a otro. ¿Qué haces: A) lo empujas también, B) dices «alto» y avisas a un adulto, C) corres?", "B", "Detener el juego y avisar protege a todos.")],
    selfcheck=[
        ex("¿Qué se debe sacar en la pillada de cinta?", "La cinta", "No se toca el cuerpo."),
        ex("¿Se puede empujar para escapar?", "No", "Está prohibido en el juego."),
        ex("¿Qué haces para escapar: esquivar o agarrar?", "Esquivar", "Cambias de dirección."),
    ],
    open_task=task("Con 3 o más personas y un espacio de 4 × 4 m, juega «Pillada de cinta». Pon una cinta o pañuelo en la cintura de cada uno. Reglas: sólo se saca la cinta, no se empuja ni se agarra la ropa, se juega a paso rápido pero sin correr al máximo y todos se detienen si alguien dice «alto». Juega 3 rondas de 30 segundos. Anota cuántas veces esquivaste y cuántas veces dijiste «alto» por una situación insegura.",
                   "En 3 rondas esquivé 5 veces. Dije «alto» una vez porque un compañero corría hacia atrás. Seguimos sin empujar ni agarrar a nadie.",
                   ["cumple las reglas de seguridad", "esquiva sin empujar", "dice «alto» ante una situación insegura"],
                   ["registro de rondas", "observación de un adulto", "relato de una decisión"],
                   ["empujar", "agarrar la ropa", "correr sin mirar"],
                   "Destaca un esquive seguro y pide una anticipación: «mira hacia dónde va el perseguidor antes de moverte»."),
    reinforce="Juega una ronda de 30 segundos caminando rápido para practicar el esquive.",
    extend="Cambia los roles: ahora el perseguidor debe sacar cintas sin correr, solo con pasos rápidos. Explica qué cambia.",
)

register(
    OA3, 4,
    materials="Una pelota blanda, 4 conos, un aro o círculo de cuerda, y una tarjeta de papel donde escribirás una regla. Un adulto como guía.",
    use="Aprenderé a cambiar una regla de un juego para que más personas participen y sea más desafiante, explicando el cambio. Sirve para jugar mejor con todos.",
    prior=["Sé jugar un juego con reglas.", "Sé explicar con mis palabras."],
    explain=[
        "Las reglas se pueden cambiar si todos están de acuerdo. Un buen cambio de regla tiene dos objetivos: que más personas participen y que el juego siga siendo seguro. Antes de cambiar una regla, pregúntate: ¿quién no podía jugar bien? ¿Qué puedo cambiar?",
        "Puedes cambiar el espacio (más grande o más chico), el tiempo (más corto o más largo), el material (pelota más blanda o más grande) o la forma de moverse (caminar en lugar de correr). Por ejemplo, en «Pasar la pelota al aro», si alguien no alcanza, el aro se acerca.",
        "Para explicar la nueva regla, usa tres frases: «Cambiamos…», «porque…» y «así…». Por ejemplo: «Cambiamos el aro a 2 pasos, porque a Ema le costaba, así todos juegan». Prueben la regla una vez; si no resulta, se vuelve a cambiar.",
    ],
    vocab=[("cambiar una regla", "modificar lo que se puede hacer en el juego"), ("participar", "ser parte del juego"), ("desafío", "algo un poco difícil que quiero lograr"), ("acuerdo", "todos dicen que sí"), ("probar", "jugar para ver si resulta")],
    worked=[
        W("Cambiar la distancia", "Juego: lanzar una pelota blanda dentro de un aro a 4 pasos. Ema no llega a lanzar tan lejos. ¿Qué cambio propones?", ["Pienso en quién tiene dificultad: Ema.", "Puedo acercar el aro a 3 pasos para ella.", "Explico: «Cambiamos la distancia porque a Ema le costaba, así todos juegan»."], "Acercar el aro a 3 pasos, con explicación."),
        W("Subir el desafío", "A Beto el juego le parece muy fácil, siempre acierta. ¿Cómo lo haces más desafiante sin riesgos?", ["Pienso en un cambio seguro.", "Aleja el aro 1 paso o lanza con la mano izquierda.", "Pruebo el cambio y veo si resulta."], "Alejar el aro un paso o lanzar con la otra mano."),
    ],
    mistakes=[M("Cambiar la regla para que gane siempre el mismo.", "Se piensa solo en uno mismo.", "Pregunta: ¿el cambio ayuda a que más personas participen?"),
              M("Cambiar una regla sin avisar.", "Se cree que no hace falta preguntar.", "Antes de jugar, explica el cambio y confirma que todos estén de acuerdo.")],
    tiers={
        "recovery": [
            ex("Para cambiar una regla, ¿necesitas avisar o hacerlo en secreto?", "Avisar", "Todos deben saber la regla."),
            ex("Una regla cambiada, ¿debe seguir siendo segura?", "Sí", "La seguridad no se cambia."),
            ex("Si el juego es difícil para alguien, ¿acercas o alejas el aro?", "Acercas", "Acercarlo lo hace más fácil."),
        ],
        "understand": [
            ex("¿Para qué sirve cambiar una regla?", "Para que más personas participen", "Es el objetivo del cambio."),
            ex("Las tres frases para explicar son «Cambiamos…», «porque…» y...", "Así…", "Cierran la explicación diciendo el resultado."),
            ex("Si el cambio no resulta, ¿qué se hace?", "Se cambia de nuevo", "Se prueba y se mejora."),
        ],
        "apply": [
            arith("El aro estaba a 4 pasos y lo acercas 1 paso para que todos lleguen. ¿A cuántos pasos queda?", "4-1", "Se resta lo que lo acercas.", " pasos"),
            arith("El juego duraba 40 segundos y lo alargas 10 segundos para que alcancen todos. ¿Cuántos segundos dura ahora?", "40+10", "Se suma el tiempo extra.", " segundos"),
            ex("Ema usa silla de ruedas. El juego es correr hacia un cono. Elige: A) todos caminan rápido, B) Ema no juega, C) Ema corre aunque no pueda. ¿Qué cambio es mejor para incluirla?", "A", "Todos juegan a la misma velocidad posible para ella."),
        ],
        "reason": [
            ex("Dani cambia la regla para que sólo él gane. ¿Es un buen cambio?", "No", "Debe ayudar a todos a participar."),
            ex("Tras un cambio, un compañero que no jugaba ahora participa. ¿El cambio funcionó?", "Sí", "Más personas participaron."),
        ],
        "challenge": [
            ex("Escribe la explicación de este cambio con las tres frases: se acercó el aro a 3 pasos porque a Ema le costaba. Respuesta modelo.", "Cambiamos el aro a 3 pasos, porque a Ema le costaba, así todos juegan", "Usa «cambiamos», «porque» y «así»."),
            arith("Un juego tiene 6 jugadores y se agrega 1 más. Cada uno hace 5 lanzamientos. ¿Cuántos lanzamientos hay en total?", "(6+1)*5", "Se suman jugadores y luego se multiplican.", " lanzamientos"),
        ],
    },
    context=[ex("En tu casa juegan a lanzar calcetines a un cesto. Tu hermano pequeño no alcanza. ¿Qué cambio haces: A) acercar el cesto para él, B) que no juegue, C) alejarlo para todos?", "A", "Así él participa y es seguro.")],
    selfcheck=[
        ex("Antes de cambiar una regla, ¿qué debes hacer?", "Avisar y ponerse de acuerdo", "Todos deben saber."),
        ex("¿Qué se cambia si el juego es muy fácil: se hace más desafiante o se suprime?", "Se hace más desafiante", "Se sube la dificultad con seguridad."),
        ex("Si el aro estaba a 5 pasos y lo acercas 2, ¿a cuántos pasos queda?", "3", "5 menos 2 son 3."),
    ],
    open_task=task("Juego: lanzar una pelota blanda o calcetines enrollados dentro de un aro o cesto que está a 4 pasos; cada jugador hace 5 lanzamientos. Imagina que un jugador no alcanza y otro siempre acierta. Escribe un cambio para cada uno (por ejemplo, acercar el aro a 3 pasos o alejarlo a 5 pasos) y explica con las tres frases «Cambiamos…, porque…, así…». Pruébalo con un adulto y anota cuántos aciertos hubo.",
                   "Cambiamos el aro a 3 pasos para Ema, porque no alcanzaba, así participa. Para Beto, lo alejamos a 5 pasos, porque siempre acertaba, así es más desafiante. Probamos y hubo 4 aciertos de 5 lanzamientos.",
                   ["propone un cambio claro y seguro", "explica con las tres frases", "prueba el cambio y registra el resultado"],
                   ["tarjeta con la regla nueva", "registro de lanzamientos", "relato oral"],
                   ["cambiar para ganar sólo uno", "cambiar sin avisar", "agregar riesgo"],
                   "Pregunta quién se benefició del cambio y si el cambio fue seguro; sugiere ajustar según resultado."),
    reinforce="Haz 5 lanzamientos con el aro a 3 pasos y luego a 4 pasos; cuenta cuántos aciertos hay en cada distancia.",
    extend="Inventa un juego nuevo con una pelota y un aro; escribe sus 3 reglas y una forma de hacerlo más fácil.",
)

# ---------------------------------------------------------------- OA 04
register(
    OA4, 1,
    materials="Un plano simple del patio dibujado en una hoja (se entrega descrito en el ejercicio), lápiz de colores, tiza y conos. Un adulto camina contigo para recorrer el lugar.",
    use="Aprenderé a mirar un lugar antes de moverme: su suelo, sus límites y sus riesgos. Sirve para jugar en el patio, la plaza o la playa sin lastimarme.",
    prior=["Sé qué es un patio.", "Sé quién es un adulto responsable."],
    explain=[
        "Antes de jugar o hacer ejercicio, hay que leer el lugar. Leer el lugar es mirar tres cosas: la superficie (el suelo), los límites (hasta dónde puedo ir) y los riesgos (cosas que me pueden lastimar). Así decides si el lugar sirve para el juego.",
        "La superficie puede ser cemento, pasto, tierra, baldosa o arena. Si está mojada o con hoyos, resbala y hay que ir más lento. Los límites pueden ser rejas, líneas, conos o el borde del patio. Los riesgos pueden ser un escalón, un portón abierto hacia la calle, un charco o piedras sueltas.",
        "Si encuentras un riesgo, tienes tres opciones: lo avisas a un adulto, lo marcas con un cono o cambias de lugar. Nunca juegas cerca de la calle, de una reja rota ni de un portón abierto. Con un plano puedes dibujar el patio y marcar los riesgos con una equis (X).",
    ],
    vocab=[("superficie", "el suelo donde me muevo"), ("límite", "hasta dónde puedo ir"), ("riesgo", "algo que me puede lastimar"), ("plano", "dibujo del lugar visto desde arriba"), ("avisar", "decirle a un adulto lo que vi")],
    worked=[
        W("Leer el patio", "Describes el patio: suelo de cemento seco, un charco en el centro, una reja alrededor y un portón abierto hacia la calle. ¿Cuáles son superficie, límites y riesgos?", ["Superficie: cemento seco (con un charco).", "Límite: la reja.", "Riesgos: el charco que resbala y el portón abierto hacia la calle."], "Superficie: cemento; límite: reja; riesgos: charco y portón."),
        W("Marcar el plano", "En un plano, el patio es un cuadrado. Pones X en el charco y en el portón. ¿Cuántas X pusiste?", ["Hay dos riesgos.", "Pongo una X por cada uno.", "1 + 1 = 2."], "2 X."),
    ],
    mistakes=[M("Jugar cerca de un portón abierto a la calle.", "Se piensa que no pasa nada.", "Juega lejos de la calle y avisa a un adulto que cierre el portón."),
              M("Correr sobre una superficie mojada.", "No se mira el suelo antes de moverse.", "Camina despacio o cambia de lugar.")],
    tiers={
        "recovery": [
            ex("El suelo donde me muevo se llama...", "Superficie", "Es el terreno."),
            ex("Un charco de agua en el patio, ¿es un riesgo o un límite?", "Un riesgo", "El agua hace resbalar."),
            ex("Una reja que rodea el patio, ¿es un límite o un riesgo?", "Un límite", "Muestra hasta dónde puedo ir."),
        ],
        "understand": [
            ex("¿Por qué se lee el lugar antes de jugar?", "Para saber si es seguro", "Se detectan riesgos."),
            ex("Si ves un riesgo, ¿qué haces primero?", "Avisar a un adulto", "El adulto puede arreglarlo."),
            ex("Un plano es un dibujo del lugar visto desde...", "Arriba", "Se ve completo como desde el cielo."),
        ],
        "apply": [
            ex("El patio tiene: piso seco de baldosas, un escalón alto, una reja baja y piedras sueltas en una esquina. ¿Cuántos riesgos hay?", "2", "El escalón alto y las piedras sueltas."),
            ex("En el patio de una plaza hay: pasto seco, un hoyo grande, un columpio y un banco. ¿Cuál es el riesgo para correr?", "El hoyo grande", "Puede hacer tropezar."),
            arith("En el plano pusiste 3 X para riesgos y 2 líneas para límites. ¿Cuántas marcas hiciste?", "3+2", "Se suman las X y las líneas.", " marcas"),
        ],
        "reason": [
            ex("Ana dice «el cemento mojado es mejor para correr porque brilla». ¿Qué le dices?", "Que resbala y es un riesgo", "El agua hace perder el equilibrio."),
            ex("El balón se fue a la calle por un portón abierto. ¿Corres a buscarlo o pides ayuda a un adulto?", "Pides ayuda a un adulto", "La calle es un riesgo grave."),
        ],
        "challenge": [
            ex("Un lugar tiene pasto, una reja, un charco y un escalón. Ordena de menor a mayor número de riesgos: pasto/charco/escalón. Respuesta: dos riesgos son...", "El charco y el escalón", "El pasto no es un riesgo y los otros dos sí."),
            arith("Un patio tiene 4 conos en las esquinas. Si cada cono marca un límite y pones 2 conos más para un riesgo, ¿cuántos conos usas?", "4+2", "Se suman todos los conos.", " conos"),
        ],
    },
    context=[ex("Vas a la plaza con tu familia. El pasto está seco, pero hay un vidrio roto bajo un árbol. ¿Qué haces: A) lo recoges con las manos, B) avisas a un adulto y juegas lejos, C) corres encima?", "B", "El vidrio corta; un adulto debe sacarlo.")],
    selfcheck=[
        ex("¿Qué tres cosas miras al leer un lugar?", "Superficie, límites y riesgos", "Es la regla de la clase."),
        ex("Un portón abierto hacia la calle, ¿es seguro o un riesgo?", "Un riesgo", "Puede salir una pelota o un niño."),
        ex("En un plano, ¿qué pones sobre un riesgo?", "Una X", "Así se marca."),
    ],
    open_task=task("Dibuja en una hoja un plano del patio o de una sala de tu casa. Usa estas pistas: hay un espacio libre de 4 × 4 m, un charco o una zona mojada, una escalera y una reja con un portón. Marca con X los riesgos, con una línea los límites y con un color la mejor zona para jugar. Escribe una oración que diga por qué elegiste esa zona.",
                   "Dibujé un cuadrado con X en el charco, en la escalera y en el portón. La reja es el límite. Elegí la zona de arriba porque el piso está seco y lejos de la escalera.",
                   ["identifica superficie, límites y riesgos", "marca claramente los riesgos", "justifica la zona elegida"],
                   ["plano dibujado", "explicación oral", "lista de riesgos"],
                   ["no marcar un riesgo", "elegir una zona mojada", "olvidar los límites"],
                   "Pide que explique cada marca y sugiere agregar un riesgo que se pasó por alto."),
    reinforce="Camina por tu patio o sala y nombra en voz alta una superficie, un límite y un riesgo.",
    extend="Compara dos lugares de juego (por ejemplo, patio y plaza) y di cuál tiene menos riesgos y por qué.",
)

register(
    OA4, 2,
    materials="Tres superficies de práctica, que se describen en las tareas: piso liso, pasto o tierra, y arena o una frazada gruesa. Si no hay arena, usa una frazada o colchoneta. Zapatillas bien amarradas y reloj.",
    use="Aprenderé a cambiar mi paso y mi velocidad según el lugar. Sirve para caminar y correr con seguridad en el patio, el parque o la playa.",
    prior=["Sé caminar y correr con control.", "Sé leer un lugar."],
    explain=[
        "Cuando cambias de lugar, tu cuerpo debe cambiar la forma de moverse. En el piso liso y seco puedes caminar y correr normal. En el pasto, el suelo es desparejo, así que conviene dar pasos más cortos y mirar el piso. En la arena suelta, los pies se hunden y cansa más, por eso se avanza más lento.",
        "Si el piso está mojado, resbala. Ahí se camina lento, con pasos cortos y las rodillas un poco dobladas. En una subida, el cuerpo se inclina un poco hacia adelante. En una bajada, se frena con pasos cortos y se evita correr. Se mira siempre dónde se pisa.",
        "En la playa, camina por la arena firme y no entres al agua sin un adulto cerca. Usa gorro y protector solar cuando haya sol. Por seguridad, antes de empezar, revisa que no haya vidrios, piedras o basura en el suelo.",
    ],
    vocab=[("superficie", "el tipo de suelo"), ("desparejo", "con hoyos o con partes más altas y más bajas"), ("paso corto", "paso pequeño para tener más control"), ("arena suelta", "arena blanda donde los pies se hunden"), ("resbalar", "perder el equilibrio porque el suelo no agarra")],
    worked=[
        W("Cambiar el paso", "Pasas del piso liso al pasto desparejo. ¿Cómo cambias tu paso?", ["Miro el suelo para ver los hoyos.", "Doy pasos más cortos y bajo la velocidad.", "Mantengo las rodillas un poco dobladas para equilibrarme."], "Pasos más cortos, más lento y mirando el suelo."),
        W("Comparar tiempos", "Recorres 10 pasos en piso liso en 8 segundos y los mismos 10 pasos en arena suelta en 14 segundos. ¿Cuántos segundos más tardas en la arena?", ["Piso liso: 8 segundos.", "Arena: 14 segundos.", "14 − 8 = 6."], "6 segundos más."),
    ],
    mistakes=[M("Correr en el pasto como en el piso liso.", "No se nota que el suelo es desparejo.", "Mira el suelo y acorta el paso."),
              M("Entrar al agua en la playa sin un adulto.", "Se tiene calor y ganas.", "Entra solo con un adulto responsable cerca; hoy se practica en la arena.")],
    tiers={
        "recovery": [
            ex("En el pasto desparejo, ¿das pasos largos o cortos?", "Cortos", "Dan más control."),
            ex("En el piso mojado, ¿caminas rápido o lento?", "Lento", "El piso mojado hace resbalar."),
            ex("En la arena suelta, ¿cansa más o menos que el piso liso?", "Más", "Los pies se hunden."),
        ],
        "understand": [
            ex("¿Por qué miras el suelo en el pasto?", "Para ver hoyos y no tropezar", "Así se evitan las caídas."),
            ex("Si el suelo resbala, ¿doblas un poco las rodillas o las dejas rígidas?", "Las doblas", "Ayudan a equilibrar."),
            ex("En la playa, ¿entras al agua solo o con un adulto?", "Con un adulto", "El agua puede ser peligrosa."),
        ],
        "apply": [
            arith("Recorres una distancia en 12 segundos en pasto y en 9 segundos en piso liso. ¿Cuántos segundos más tardas en el pasto?", "12-9", "Se resta el menor del mayor.", " segundos"),
            ex("Hay tres superficies: piso seco, piso mojado y arena. ¿Cuál exige ir más lento por resbalar?", "El piso mojado", "El agua quita agarre."),
            arith("Haces 3 intentos de 50 segundos de acción en la arena. ¿Cuántos segundos de acción son?", "3*50", "Se multiplican intentos por segundos.", " segundos"),
        ],
        "reason": [
            ex("Beto dice que corre igual en arena y en cemento. ¿Qué observarías para comprobarlo?", "Cuánto tarda en cada una", "Compararía los tiempos."),
            ex("Hay vidrios en la arena. ¿Corres descalzo o avisas a un adulto?", "Avisas a un adulto", "Los vidrios cortan."),
        ],
        "challenge": [
            ex("Un camino tiene: 5 m de piso liso, 5 m de pasto desparejo y 5 m de piso mojado. ¿Cuántas veces cambias la forma de caminar en un recorrido de ida?", "2", "Cambias al pasar de liso a pasto y de pasto a mojado."),
            arith("En el recorrido anterior, 5 m de cada tramo suman cuántos metros?", "5+5+5", "Se suman los tres tramos.", " m"),
        ],
    },
    context=[ex("Estás en la playa con tu familia y el sol está fuerte. Quieres correr en la arena. ¿Qué haces antes: A) ponerte gorro y protector solar y revisar el suelo, B) correr al agua, C) saltar sobre piedras?", "A", "Te cuidas del sol y evitas objetos.")],
    selfcheck=[
        ex("¿Qué haces con el paso en el pasto?", "Lo acorto", "Se controla mejor."),
        ex("¿Qué superficie cansa más: arena suelta o piso liso?", "Arena suelta", "Los pies se hunden."),
        ex("Si el piso está mojado, ¿corres o caminas?", "Caminas", "Correr en piso mojado hace resbalar."),
    ],
    open_task=task("Elige tres superficies de tu casa o patio (por ejemplo, piso liso, pasto, alfombra o una frazada). Camina 10 pasos en cada una, mide cuántos segundos tardas con un reloj y anota un cambio que hiciste en el paso. Responde: ¿en cuál tardaste más? ¿Por qué?",
                   "Piso liso: 8 s. Pasto: 11 s, pasos más cortos. Frazada: 12 s, pies hundidos. Tardé más en la frazada porque los pies se hunden.",
                   ["cambia el paso según la superficie", "registra los tiempos", "explica la causa"],
                   ["tabla de tiempos", "observación de un adulto", "relato oral"],
                   ["correr en suelo mojado", "no mirar el suelo", "comparar sin medir"],
                   "Reconoce el cambio de paso y pide que explique una decisión de seguridad."),
    reinforce="Camina 10 pasos en piso liso y 10 en pasto, uno más corto que otro; cuenta qué cambia.",
    extend="Planifica con un adulto un recorrido de ida y vuelta en el parque con tres superficies y explica cómo cambiarás el paso.",
)

register(
    OA4, 3,
    materials="Una pelota blanda o calcetines enrollados, un espacio abierto, cuatro conos, una pared sin ventanas cerca y un adulto. En interior, usa un globo o una pelota de espuma.",
    use="Aprenderé a lanzar y recoger una pelota ajustando fuerza y dirección en lugares distintos. Sirve para jugar a la pelota en la plaza, en la playa o en una sala pequeña.",
    prior=["Sé lanzar y recibir a un compañero.", "Sé leer un lugar."],
    explain=[
        "El mismo lanzamiento puede comportarse distinto según el lugar. En una sala pequeña conviene lanzar suave y con una pelota blanda para no romper nada. En un patio grande puedes lanzar con más fuerza. En el pasto la pelota rebota poco y en el cemento rebota más.",
        "En la playa, la pelota se frena en la arena y el viento puede moverla. Por eso se lanza algo más fuerte y se mira dónde cae. Si hay viento, se lanza un poco hacia donde sopla para que no se aleje demasiado. Nunca se lanza hacia el mar, la calle o un vidrio.",
        "Para ajustar fuerza y dirección, pregúntate: ¿qué distancia hay? ¿Qué hay alrededor? ¿Cuánto rebota? Prueba un lanzamiento suave y corrige. Mira el blanco, extiende el brazo hacia él y suelta la pelota a la altura del pecho de tu compañero.",
    ],
    vocab=[("fuerza", "cuánto empujo la pelota"), ("dirección", "hacia dónde va la pelota"), ("rebote", "cuando la pelota sube al tocar el suelo"), ("blanco", "lugar o persona hacia donde lanzo"), ("viento", "aire que mueve las cosas")],
    worked=[
        W("Lanzar en una sala", "Estás en una sala pequeña con muebles. ¿Qué pelota y qué fuerza usas?", ["Elijo una pelota blanda o un globo.", "Lanzo suave y hacia la pared libre.", "Me alejo de ventanas y muebles."], "Pelota blanda y lanzamiento suave hacia la pared libre."),
        W("Corregir un lanzamiento", "Lanzas a un compañero a 4 pasos y la pelota cae a 2 pasos. ¿Qué ajustas?", ["Falta fuerza: llegó 2 pasos de 4.", "Lanzo un poco más fuerte.", "Pruebo otra vez."], "Lanzar con un poco más de fuerza."),
    ],
    mistakes=[M("Lanzar fuerte en una sala pequeña.", "Se usa la misma fuerza que en el patio.", "Adapta la fuerza al espacio: suave y con pelota blanda."),
              M("Lanzar hacia una ventana o la calle.", "No se mira lo que hay alrededor.", "Mira el blanco y lo que hay detrás.")],
    tiers={
        "recovery": [
            ex("En una sala pequeña, ¿lanzas suave o fuerte?", "Suave", "Evita golpear cosas."),
            ex("La pelota que rebota mucho, ¿está en cemento o en arena suelta?", "En cemento", "La arena frena la pelota."),
            ex("Antes de lanzar, ¿miras el blanco o cierras los ojos?", "Miras el blanco", "Dirigirá mejor el lanzamiento."),
        ],
        "understand": [
            ex("¿Por qué se usa una pelota blanda en una sala?", "Para no romper cosas ni lastimar", "No hace daño."),
            ex("En la playa, la arena frena la pelota. ¿Debes lanzar más suave o algo más fuerte?", "Algo más fuerte", "Se frena al caer y no llega lejos."),
            ex("¿Qué es el rebote?", "Cuando la pelota sube al tocar el suelo", "Es el segundo movimiento."),
        ],
        "apply": [
            ex("Tu compañero está a 4 pasos y la pelota cae a 2 pasos. ¿Más o menos fuerza?", "Más fuerza", "No llegó al destino."),
            ex("La pelota pasó 3 pasos más allá de tu compañero. ¿Más o menos fuerza?", "Menos fuerza", "Llegó demasiado lejos."),
            arith("Haces 10 lanzamientos y 7 llegan a tu compañero. ¿Cuántos no llegaron?", "10-7", "Se resta lo logrado.", ""),
        ],
        "reason": [
            ex("Hay viento fuerte hacia el mar y lanzas hacia el mar. ¿Es buena idea?", "No", "La pelota se pierde en el agua."),
            ex("En el pasto la pelota casi no rebota. ¿Dónde esperarías que rebote más: en el pasto o en el cemento?", "En el cemento", "Una superficie dura devuelve más."),
        ],
        "challenge": [
            arith("Lanzas 5 veces desde 3 pasos y 5 veces desde 5 pasos. ¿Cuántos lanzamientos son en total?", "5+5", "Se suman las dos series.", " lanzamientos"),
            ex("Hay 3 lugares: una sala, un patio y la playa. ¿En cuál lanzas más suave: la sala, el patio o la playa?", "La sala", "El espacio es más pequeño."),
        ],
    },
    context=[ex("Estás en casa y quieres practicar con una pelota dura. Tu mamá dice «mejor una blanda». ¿Por qué tiene razón?", "Porque una pelota dura puede romper o lastimar", "En un espacio pequeño la blanda es más segura.")],
    selfcheck=[
        ex("¿Dónde rebota menos la pelota: arena suelta o cemento?", "En la arena suelta", "La arena frena."),
        ex("Si la pelota cae corta, ¿pones más o menos fuerza?", "Más", "A la pelota le faltó alcance."),
        ex("En una sala, ¿qué pelota es mejor?", "Blanda", "Una pelota blanda no daña."),
    ],
    open_task=task("Con una pelota blanda o calcetines enrollados y un adulto, haz 5 lanzamientos suaves hacia una pared libre a 2 pasos y 5 lanzamientos a un compañero a 4 pasos. Anota cuántas veces ajustaste la fuerza (más o menos) y por qué.",
                   "En 10 lanzamientos ajusté la fuerza 3 veces: dos veces puse más porque cayó corta y una menos porque pasó de largo. Me aseguré de que no hubiera ventanas.",
                   ["ajusta fuerza y dirección", "mira el blanco y el entorno", "usa material seguro"],
                   ["tabla de ajustes", "observación de un adulto", "relato oral"],
                   ["lanzar fuerte en espacios pequeños", "ignorar el entorno", "no corregir"],
                   "Destaca el ajuste de fuerza y pide una causa para cada corrección."),
    reinforce="Lanza suavemente a la pared 10 veces y recoge sin dejar rodar la pelota.",
    extend="Prueba lanzar en dos lugares distintos y compara cuántos lanzamientos llegan al blanco en cada uno.",
)

register(
    OA4, 4,
    materials="Un patio o sala, tiza o cinta, 5 conos o botellas vacías, una hoja y un lápiz. Reloj. Una lista de 5 estaciones que se entrega aquí.",
    use="Aprenderé a planificar y hacer una ruta segura con varias estaciones. Sirve para organizar un recorrido de juego en la plaza o en el patio.",
    prior=["Sé leer un lugar.", "Sé caminar, saltar y lanzar con control."],
    explain=[
        "Una ruta es un recorrido con un inicio, un camino y un final. Una ruta segura evita los riesgos y respeta los límites. Antes de hacerla, se dibuja un plano con flechas que muestran el camino y se marcan las estaciones con números.",
        "Las estaciones de hoy son: 1) caminar sobre una línea, 2) cinco saltos con dos pies, 3) lanzar una pelota a la pared, 4) un giro y 5) caminar de vuelta al inicio. Cada estación dura 40 segundos de acción y 40 de pausa. Entre estaciones se camina.",
        "Para planificar, sigue estos pasos: leer el lugar y marcar riesgos, dibujar el plano, poner los conos en el orden del plano, ejecutar la ruta y revisar. Al revisar, responde: ¿respeté los límites?, ¿evité los riesgos?, ¿cambié mi paso según la superficie?",
    ],
    vocab=[("ruta", "recorrido con inicio, camino y final"), ("plan", "dibujo o lista de lo que haré"), ("estación", "lugar donde hago una tarea"), ("revisar", "mirar si lo hice bien"), ("riesgo", "algo que puede lastimar")],
    worked=[
        W("Duración de la ruta", "La ruta tiene 5 estaciones de 40 segundos de acción y 40 de pausa. ¿Cuántos segundos dura la ruta completa?", ["Una estación: 40 + 40 = 80.", "Son 5 estaciones: 80 × 5.", "80 × 5 = 400."], "400 segundos."),
        W("Marcar la ruta", "En el plano ya marcaste un charco con X. Las estaciones deben ir lejos de él. ¿Cómo comprobar?", ["Miro dónde está la X.", "Pongo los conos 2 pasos o más lejos de la X.", "Reviso que el camino no pase por ella."], "Los conos van lejos de la X y la ruta no la cruza."),
    ],
    mistakes=[M("Dibujar la ruta sin marcar los riesgos.", "Se quiere empezar rápido.", "Primero lee el lugar y marca los riesgos; después dibuja."),
              M("Correr entre estaciones.", "Se piensa que es una carrera.", "Camina entre estaciones y revisa el control.")],
    tiers={
        "recovery": [
            ex("Una ruta tiene un inicio, un camino y un...", "Final", "Así se define."),
            ex("Antes de planificar la ruta, ¿marcas los riesgos o los ignoras?", "Los marcas", "Se evitan al planificar."),
            ex("Entre estaciones, ¿caminas o corres?", "Caminas", "Se mantiene el control."),
        ],
        "understand": [
            ex("¿Para qué sirve el plano?", "Para ver el camino y los riesgos antes de moverse", "Ayuda a planificar."),
            ex("Una ruta segura, ¿pasa por los riesgos o los evita?", "Los evita", "Ese es su objetivo."),
            ex("¿Qué se pregunta al revisar?", "Si respeté los límites y evité los riesgos", "Es la pauta."),
        ],
        "apply": [
            arith("Hay 5 estaciones de 40 segundos de acción cada una. ¿Cuántos segundos de acción hay?", "5*40", "Se multiplican estaciones por segundos.", " segundos"),
            arith("Una estación completa dura 40 de acción y 40 de pausa. ¿Cuántos segundos son?", "40+40", "Se suman acción y pausa.", " segundos"),
            ex("Las estaciones son: línea, saltos, lanzar, giro, volver. ¿Cuál es la tercera?", "Lanzar", "Está tercera en la lista."),
        ],
        "reason": [
            ex("Dani dibuja la ruta pasando junto a un portón abierto. ¿Qué le dices?", "Que cambie la ruta para evitarlo", "El portón es un riesgo."),
            ex("En la ruta de Ema, dos conos están pegados a la reja. ¿Qué problema hay?", "Falta espacio de seguridad", "Hay que dejar espacio entre el cono y el límite."),
        ],
        "challenge": [
            arith("Haces la ruta completa 2 veces. Cada vez dura 400 segundos. ¿Cuántos minutos son? Responde en minutos con número entero.", "(400*2)//60", "Se pasa de segundos a minutos (800 ÷ 60 = 13 minutos y 20 segundos).", " minutos"),
            ex("Hay 6 niños y 5 estaciones. Si empiezan juntos en estaciones distintas, ¿cuántos niños esperan en el inicio?", "1", "6 niños menos 5 estaciones ocupadas son 1."),
        ],
    },
    context=[ex("Vas con tu familia a un parque con senderos, un lago y una calle cercana. Quieres hacer una ruta de saltos y lanzamientos. ¿Dónde la haces: A) cerca del lago, B) en el pasto lejos del lago y de la calle, C) al borde de la calle?", "B", "El pasto, lejos del agua y la calle, es más seguro.")],
    selfcheck=[
        ex("¿Qué significa «ruta segura»?", "Una ruta que evita los riesgos y respeta los límites", "Es la definición."),
        ex("Una estación dura 80 s con pausa. ¿Cuántos segundos duran 2 estaciones?", "160", "2 por 80 son 160."),
        ex("¿Se corre o se camina entre estaciones?", "Se camina", "Para mantener el control."),
    ],
    open_task=task("Diseña una ruta segura con estas 5 estaciones: 1) caminar sobre una línea de 2 m, 2) cinco saltos con dos pies, 3) cinco lanzamientos suaves a la pared con una pelota blanda, 4) un giro de vuelta completa, 5) caminar de vuelta al inicio. Dibuja un plano con un cuadrado, números y flechas; marca con X al menos un riesgo ficticio (por ejemplo, un charco) que debe evitar la ruta. Haz la ruta con un adulto y revisa con tres preguntas.",
                   "Dibujé 5 números con flechas y una X en un charco. Mi ruta no pasó por el charco. Respeté los límites sí, evité riesgos sí, caminé entre estaciones sí.",
                   ["dibuja una ruta clara con flechas", "evita el riesgo marcado", "revisa con las tres preguntas"],
                   ["plano dibujado", "observación de un adulto", "respuestas a las preguntas"],
                   ["no marcar riesgos", "pasar por el riesgo", "correr entre estaciones"],
                   "Reconoce el plan y pide un ajuste: «¿qué cambiarías para que sea aún más segura?»."),
    reinforce="Dibuja un plano con 3 estaciones y flechas, y recórrelo caminando.",
    extend="Agrega una sexta estación a tu ruta y calcula cuánto dura en total con 40 segundos de acción y 40 de pausa por estación.",
)

# ---------------------------------------------------------------- OA 05
register(
    OA5, 1,
    materials="Un espacio libre en que quepas con los brazos extendidos girando sin tocar nada, música lenta (opcional) y una tela, pañuelo o toalla pequeña. Todo está descrito en este cuaderno.",
    use="Aprenderé a mover mi cuerpo en distintos niveles (alto, medio y bajo) y tamaños, sin chocar. Sirve para expresar lo que siento y bailar con control.",
    prior=["Sé mover mis brazos y piernas.", "Sé que debo respetar el espacio de otros."],
    explain=[
        "Tu espacio personal es la burbuja que te rodea cuando estiras los brazos. Dentro de ella puedes moverte sin tocar a nadie. Los niveles son tres: alto, cuando tu cuerpo se estira hacia arriba, de puntillas o con los brazos arriba; medio, cuando estás de pie o con las rodillas un poco dobladas; y bajo, cuando estás agachado o cerca del suelo.",
        "El tamaño del movimiento puede ser grande o pequeño. Un movimiento grande usa mucho espacio de tu burbuja. Uno pequeño usa poco. Puedes mover una mano en un círculo grande o en un círculo pequeño. Cambiar el nivel y el tamaño permite mostrar ideas o sensaciones distintas.",
        "Para moverte con control, mantén tus movimientos dentro de la burbuja, respira tranquilo y cuida que tus manos y pies no toquen a otros. Si usas una tela, sujétala por una esquina y muévela suave sin lanzarla a nadie. No hay una forma correcta o incorrecta de moverse, pero sí hay una forma segura.",
    ],
    vocab=[("espacio personal", "burbuja de aire a un brazo de distancia a mi alrededor"), ("nivel alto", "cuerpo estirado hacia arriba"), ("nivel medio", "cuerpo de pie o a medio agachar"), ("nivel bajo", "cuerpo agachado, cerca del suelo"), ("tamaño", "cuánto espacio uso al moverme")],
    worked=[
        W("Pasar por tres niveles", "Debes mostrar los tres niveles en este orden: bajo, medio y alto. ¿Qué haces?", ["Primero me agacho, con las manos cerca del suelo.", "Luego me pongo de pie con las rodillas un poco dobladas.", "Por último estiro los brazos hacia arriba y me pongo de puntillas."], "Agachado, de pie y estirado, en ese orden."),
        W("Tamaño del movimiento", "Dibujas un círculo con la mano. Primero uno grande y luego uno pequeño. ¿Qué cambia?", ["El primer círculo usa más espacio de mi burbuja.", "El segundo usa menos espacio.", "Mi nivel y mi ritmo pueden ser iguales."], "Cambia el tamaño: uno grande y uno pequeño."),
    ],
    mistakes=[M("Moverse fuera de la burbuja y tocar a otros.", "Se hace un movimiento muy grande sin mirar.", "Mide tu burbuja con los brazos y mantente dentro."),
              M("Pensar que hay un único movimiento correcto.", "En otras clases hay una sola respuesta.", "Aquí cada persona puede crear su movimiento, mientras sea seguro.")],
    tiers={
        "recovery": [
            ex("Cuando estás agachado, ¿estás en nivel alto, medio o bajo?", "Bajo", "Estás cerca del suelo."),
            ex("Cuando estás de puntillas con los brazos arriba, ¿qué nivel es?", "Alto", "El cuerpo se estira hacia arriba."),
            ex("Cuando estás de pie normal, ¿qué nivel es?", "Medio", "No estás alto ni bajo."),
        ],
        "understand": [
            ex("¿Qué es el espacio personal?", "La burbuja que me rodea a un brazo de distancia", "Es donde me muevo sin tocar a otros."),
            ex("Un círculo grande con la mano, ¿usa mucho o poco espacio?", "Mucho", "Eso significa «grande»."),
            ex("¿Existe una única forma correcta de moverse en esta clase?", "No", "Hay muchas formas seguras."),
        ],
        "apply": [
            ex("Orden: agachado, de pie, estirado. ¿Qué nivel viene al final?", "Alto", "Estirado es alto."),
            ex("Muestras un nivel bajo y uno alto. ¿Cuántos niveles distintos mostraste?", "2", "Bajo y alto son dos."),
            arith("Haces 3 intentos de 50 segundos de acción. ¿Cuántos segundos te mueves?", "3*50", "Se multiplican intentos por segundos.", " segundos"),
        ],
        "reason": [
            ex("Ana mueve los brazos muy grandes y golpea a Beto. ¿Qué debe hacer?", "Moverse dentro de su burbuja", "Así no toca a otros."),
            ex("Caro dice «mis movimientos son incorrectos porque no son como los de Dani». ¿Qué le dices?", "Que no hay una forma incorrecta si es segura", "Cada persona crea su movimiento."),
        ],
        "challenge": [
            ex("Creas una frase de 3 movimientos con tres niveles distintos. ¿Cuántos niveles usas en total?", "3", "Uno por cada movimiento."),
            ex("Una frase empieza en nivel bajo, sube a medio y baja a bajo. ¿Cuántas veces cambia de nivel?", "2", "Sube una vez y baja otra."),
        ],
    },
    context=[ex("En el cumpleaños de un amigo, la música suena y todos bailan en una sala pequeña. Quieres hacer un movimiento grande con los brazos. ¿Qué haces: A) lo haces igual, B) miras alrededor y lo haces dentro de tu burbuja, C) empujas a los demás?", "B", "Cuidas el espacio de todos.")],
    selfcheck=[
        ex("¿Cuáles son los tres niveles?", "Alto, medio y bajo", "Son los niveles de la clase."),
        ex("¿Qué haces con el espacio personal?", "Lo respeto", "No toco a otros."),
        ex("¿El tamaño del movimiento puede ser grande o pequeño?", "Sí", "Mucho o poco espacio."),
    ],
    open_task=task("Crea una frase de movimiento de 3 posiciones: una en nivel bajo, una en nivel medio y una en nivel alto. Cada una debe tener un tamaño (grande o pequeño). Hazla 3 veces durante 50 segundos de acción con 50 de pausa. Dibuja las 3 posiciones y escribe el tamaño de cada una.",
                   "Posición 1: bajo, pequeña. Posición 2: medio, grande. Posición 3: alto, grande. La repetí 3 veces sin tocar a nadie y dentro de mi burbuja.",
                   ["usa los tres niveles", "cambia el tamaño con intención", "se mueve con control y dentro de su espacio"],
                   ["dibujo de 3 posiciones", "demostración", "relato oral"],
                   ["salirse de la burbuja", "no cambiar de nivel", "copiar sin pensar"],
                   "Destaca lo que más le gustó de su frase y pide un cambio de tamaño o de nivel para probar algo nuevo."),
    reinforce="Estírate en nivel alto durante 3 segundos y luego agáchate a nivel bajo durante 3 segundos, 5 veces.",
    extend="Haz una frase de 5 movimientos que suba y baje de nivel dos veces; dibújala con flechas.",
)

register(
    OA5, 2,
    materials="Una música instrumental lenta y otra rápida, o un adulto que aplauda lento (1 palmada por segundo) y rápido (2 palmadas por segundo). Espacio libre y reloj.",
    use="Aprenderé a mover mi cuerpo al ritmo de un pulso, más lento o más rápido, y a notar la energía de mi movimiento. Sirve para bailar y para expresar cómo me siento.",
    prior=["Sé aplaudir al compás.", "Sé nombrar rápido y lento."],
    explain=[
        "El pulso es el latido constante de la música, como un reloj. Si aplaudes una vez por segundo, el pulso es lento; si aplaudes dos veces por segundo, es rápido. Puedes caminar al pulso: un paso por cada palmada.",
        "La energía es cuánta fuerza usas al moverte. Puede ser suave, como una pluma, o fuerte, como un tambor. Un movimiento lento y suave se siente calmado; uno rápido y fuerte se siente muy activo. Cuida que la fuerza no te haga golpear nada.",
        "Para cambiar el movimiento según el pulso, escucha unos segundos, sigue el pulso con los pies y después agrega los brazos. Al cambiar de lento a rápido, hazlo poco a poco. Si te cansas o te falta aire, baja el ritmo y bebe agua.",
    ],
    vocab=[("pulso", "latido regular de la música"), ("energía", "cuánta fuerza uso al moverme"), ("suave", "con poca fuerza"), ("fuerte", "con mucha fuerza"), ("ritmo", "orden de sonidos lentos y rápidos")],
    worked=[
        W("Pasos al pulso", "El pulso es lento: 1 palmada por segundo. Caminas un paso por palmada durante 10 segundos. ¿Cuántos pasos das? Si luego el pulso es rápido (2 palmadas por segundo) durante 10 segundos, ¿cuántos pasos?", ["Lento: 10 segundos × 1 paso = 10.", "Rápido: 10 segundos × 2 pasos = 20.", "Comparo: 20 es el doble de 10."], "10 pasos con pulso lento y 20 con pulso rápido."),
        W("Energía del movimiento", "Debes mostrar un movimiento suave y uno fuerte con las manos. ¿Cómo lo haces?", ["Suave: muevo las manos despacio, como si acariciaran una pluma.", "Fuerte: empujo el aire con las manos, sin golpear a nadie.", "Mantengo las dos acciones dentro de mi burbuja."], "Manos suaves y manos fuertes, sin tocar nada."),
    ],
    mistakes=[M("Aplaudir y moverse sin seguir el pulso.", "No se escucha el pulso antes de empezar.", "Escucha cuatro pulsos y empieza al quinto."),
              M("Usar fuerza que golpea a otros.", "Energía fuerte se confunde con brusca.", "Fuerte significa con firmeza, sin tocar a nadie.")],
    tiers={
        "recovery": [
            ex("Una palmada por segundo, ¿es pulso lento o rápido?", "Lento", "Es menos frecuente."),
            ex("Dos palmadas por segundo, ¿es pulso lento o rápido?", "Rápido", "Es más frecuente."),
            ex("Mover las manos como si acariciaras una pluma, ¿es suave o fuerte?", "Suave", "Se hace con poca fuerza."),
        ],
        "understand": [
            ex("¿Qué es el pulso?", "El latido regular de la música", "Es un golpe constante, como un reloj."),
            ex("¿Qué es la energía de un movimiento?", "Cuánta fuerza uso", "Puede ser suave o fuerte."),
            ex("Si te falta el aire al bailar, ¿qué haces?", "Bajar el ritmo y beber agua", "Así te recuperas con calma."),
        ],
        "apply": [
            arith("Pulso lento: 1 paso por segundo. ¿Cuántos pasos das en 12 segundos?", "12*1", "Un paso por segundo.", " pasos"),
            arith("Pulso rápido: 2 pasos por segundo. ¿Cuántos pasos das en 6 segundos?", "6*2", "Dos pasos por segundo.", " pasos"),
            ex("Orden: lento 10 s y rápido 10 s. ¿Cuántos segundos dura todo?", "20", "10 más 10 son 20 segundos."),
        ],
        "reason": [
            ex("Beto va rápido, pero la música es lenta. ¿Qué debe cambiar?", "Bajar la velocidad al pulso", "Debe seguir el pulso."),
            ex("Ema golpeó el aire tan fuerte que casi toca a Fito. ¿Qué debe cuidar?", "Su espacio y la fuerza", "Fuerte no es brusco."),
        ],
        "challenge": [
            arith("Haces 4 pasos lentos en 4 segundos y 8 pasos rápidos en 4 segundos. ¿Cuántos pasos diste en total?", "4+8", "Se suman los pasos.", " pasos"),
            ex("El adulto aplaude lento 8 segundos y rápido 8 segundos. Si te mueves un paso por palmada, ¿cuántos pasos más hiciste en el tramo rápido que en el lento?", "8", "16 pasos menos 8 son 8."),
        ],
    },
    context=[ex("En la clase de música la profesora toca un tambor lento y luego rápido. ¿Qué haces con los pies cuando el tambor se acelera?", "Muevo los pies más rápido", "Sigues el pulso.")],
    selfcheck=[
        ex("¿Una palmada por segundo es lenta o rápida?", "Lenta", "Es el pulso lento."),
        ex("En el baile, la energía se describe como suave o fuerte. ¿De qué depende?", "De cuánta fuerza uso", "Define suave o fuerte."),
        ex("Si das un paso por palmada y hay 10 palmadas, ¿cuántos pasos?", "10", "Uno por palmada."),
    ],
    open_task=task("Con un adulto que aplauda, mueve tu cuerpo así: 10 segundos con aplausos lentos (1 por segundo) y pasos suaves, 10 segundos con aplausos rápidos (2 por segundo) y pasos más fuertes, y 10 segundos de nuevo lentos. Repite 3 veces con 40 segundos de pausa. Cuenta cuántos pasos diste en total en cada tramo y di cómo cambió tu energía.",
                   "Tramo lento: 10 pasos. Tramo rápido: 20 pasos. Último tramo lento: 10 pasos. En total 40 pasos por vuelta. Fui suave en el lento y más fuerte en el rápido, sin golpear nada.",
                   ["sigue el pulso lento y rápido", "cambia la energía con intención", "cuida el espacio y la fuerza"],
                   ["registro de pasos", "demostración", "relato oral"],
                   ["no seguir el pulso", "golpear a otros", "no recuperarse"],
                   "Reconoce los cambios de energía y pide notar cómo cambia la respiración en el tramo rápido."),
    reinforce="Camina 10 pasos lentos y 10 rápidos al ritmo de aplausos, contando en voz alta.",
    extend="Inventa un tramo medio (1,5 palmadas por segundo, es decir, 3 palmadas cada 2 segundos) y enséñaselo a alguien.",
)

register(
    OA5, 3,
    materials="Una tela o pañuelo, una hoja y lápiz, y las tarjetas escritas aquí: «viento», «cosquillas», «sorpresa», «calma». Espacio libre y música suave opcional.",
    use="Aprenderé a mostrar una idea o sensación con una frase de movimientos, sin imitarla literalmente. Sirve para expresarme y para entender cómo se expresan otros.",
    prior=["Sé moverme en niveles y tamaños.", "Sé seguir un pulso."],
    explain=[
        "Una frase corporal es una secuencia corta de movimientos con un inicio, un medio y un final. Se puede crear para mostrar una idea (como viento) o una sensación (como cosquillas). No debes imitar la cosa como si fueras actor; debes mostrarla con tu cuerpo usando nivel, tamaño, ritmo y energía.",
        "Por ejemplo, para «viento» podrías empezar en nivel bajo con un movimiento pequeño y lento, subir a nivel alto con un movimiento grande y rápido y terminar en nivel medio con un movimiento suave. No hace falta dibujar el viento con las manos: lo expresas con cómo cambias tu cuerpo.",
        "Para crear tu frase, elige una tarjeta, decide el inicio, el medio y el final, y practica tres veces. Si quieres, puedes usar una tela. Si algún movimiento te da vergüenza, puedes elegir uno más pequeño. Nadie se ríe de la creación de otro; se aplaude al final.",
    ],
    vocab=[("frase corporal", "secuencia corta de movimientos con inicio, medio y final"), ("no literal", "mostrar una idea sin imitarla tal cual"), ("inicio", "primer movimiento"), ("final", "último movimiento"), ("sensación", "lo que siento en el cuerpo")],
    worked=[
        W("Frase para «cosquillas»", "Debes crear una frase de 3 movimientos para «cosquillas». ¿Cómo la haces?", ["Inicio: pequeño y rápido con los dedos, en nivel medio.", "Medio: todo el cuerpo tiembla un poco, rápido.", "Final: me quedo quieto y relajado en nivel bajo."], "Dedos rápidos, cuerpo que tiembla, final quieto."),
        W("Contar movimientos", "Tu frase tiene 3 movimientos y la repites 3 veces. ¿Cuántos movimientos haces?", ["Una vez son 3 movimientos.", "Repito 3 veces: 3 × 3.", "3 × 3 = 9."], "9 movimientos."),
    ],
    mistakes=[M("Imitar la cosa como un actor, por ejemplo soplar y decir «fuuu».", "Se confunde mostrar con imitar.", "Muestra la idea con nivel, tamaño, ritmo o energía."),
              M("Copiar siempre a un compañero.", "Da vergüenza inventar.", "Cambia al menos un movimiento: hazlo tuyo.")],
    tiers={
        "recovery": [
            ex("Una frase corporal tiene inicio, medio y...", "Final", "Son tres partes."),
            ex("¿Cuántos movimientos tiene una frase de inicio, medio y final con un movimiento cada uno?", "3", "Uno por cada parte."),
            ex("Una tela, ¿se sujeta por una esquina o se lanza a otros?", "Se sujeta por una esquina", "Así se cuida a los demás."),
        ],
        "understand": [
            ex("¿Qué significa «no literal»?", "Mostrar sin imitar tal cual", "Usas nivel, tamaño y ritmo."),
            ex("Si un movimiento te da vergüenza, ¿qué puedes hacer?", "Hacerlo más pequeño o cambiarlo", "Puedes elegir un movimiento cómodo."),
            ex("Cuando termina una frase, ¿qué se hace?", "Se aplaude", "Se respeta la creación."),
        ],
        "apply": [
            ex("Tarjeta «calma». Se propone: inicio lento y pequeño, medio suave, final quieto. ¿Cuántas partes tiene la frase?", "3", "Inicio, medio y final."),
            arith("Repites una frase de 3 movimientos 4 veces. ¿Cuántos movimientos haces?", "3*4", "Se multiplican movimientos por repeticiones.", " movimientos"),
            ex("En «viento», pasas de nivel bajo a alto. ¿Cuántos niveles tocaste: bajo, medio, alto?", "Al menos 2: bajo y alto", "Empiezas en bajo y terminas en alto."),
        ],
        "reason": [
            ex("Dani hizo «sorpresa» saltando y gritando «¡boo!». ¿Mostró la idea de forma no literal?", "Parcialmente; usó sonido", "Una frase corporal usa el cuerpo, no sólo palabras."),
            ex("Beto copió la frase de Ana palabra por palabra. ¿Qué debe cambiar?", "Hacerla suya con algún cambio", "Cada uno crea su frase."),
        ],
        "challenge": [
            ex("Crea una frase de 3 movimientos para «viento»: dibuja con palabras los niveles de cada movimiento. Un ejemplo válido es bajo, alto, medio. ¿Cuántos cambios de nivel tiene?", "2", "Hay un cambio entre cada movimiento."),
            arith("Haces la frase 3 veces con 20 segundos de acción y 20 de pausa por vez. ¿Cuántos segundos de acción hay?", "3*20", "Se multiplican veces por segundos.", " segundos"),
        ],
    },
    context=[ex("En una obra de la escuela debes mostrar «viento» sin hablar. ¿Cómo lo haces: A) sólo soplas, B) cambias de nivel y tamaño con tu cuerpo, C) te quedas quieto?", "B", "Usas movimiento, no imitación literal.")],
    selfcheck=[
        ex("¿Qué tiene una frase corporal?", "Inicio, medio y final", "Son sus partes."),
        ex("¿Se imita o se muestra con el cuerpo?", "Se muestra con el cuerpo", "La frase es no literal, no una imitación."),
        ex("¿Se puede ridiculizar a otro?", "No", "Se respeta a todos."),
    ],
    open_task=task("Elige una tarjeta: «viento», «cosquillas», «sorpresa» o «calma». Crea una frase de 3 movimientos con inicio, medio y final. Dibuja los 3 movimientos con flechas y escribe el nivel (alto, medio, bajo), el tamaño (grande, pequeño) y la energía (suave, fuerte) de cada uno. Hazla 3 veces en 20 segundos de acción con 20 de pausa.",
                   "Tarjeta «cosquillas»: 1) nivel medio, pequeño, rápido y suave. 2) nivel medio, grande, temblor rápido. 3) nivel bajo, pequeño, quieto. La hice 3 veces dentro de mi burbuja.",
                   ["crea inicio, medio y final", "usa nivel, tamaño o energía", "mantiene su espacio y respeta a otros"],
                   ["dibujo de la frase", "demostración", "explicación oral"],
                   ["imitar tal cual", "salirse de la burbuja", "ridiculizar a otros"],
                   "Elogia una decisión creativa y pide explicar por qué eligió ese nivel o tamaño."),
    reinforce="Con la tarjeta «calma», haz un movimiento lento y suave de 5 segundos y quédate quieto.",
    extend="Cambia el final de tu frase para que muestre otra sensación y compara las dos versiones.",
)

register(
    OA5, 4,
    materials="Dos frases corporales ya creadas (una tuya y una de un compañero o familiar), música suave opcional, espacio libre y reloj.",
    use="Aprenderé a unir mi frase con la de otra persona en una pequeña danza, respetando que cada uno se mueve distinto. Sirve para crear algo juntos y valorar a los demás.",
    prior=["Sé crear una frase corporal.", "Sé escuchar y esperar mi turno."],
    explain=[
        "Una composición compartida es una danza que une dos o más frases. Cada persona aporta su frase, y entre todos deciden el orden. Puede ser una después de la otra, una al lado de la otra a la vez o una imitando a la otra. Lo importante es que se escuchen.",
        "Cuando unes dos frases, necesitas un acuerdo: ¿quién parte? ¿Cuántas veces se repite? ¿Cómo termina? Si dos ideas son muy diferentes, no hay que cambiarlas: se pueden mostrar una tras otra con una pausa de dos segundos entre medio. Se respeta cada forma de moverse.",
        "Para presentar la composición, quédense a dos brazos de distancia, miren al compañero cuando hace su frase y al terminar sonrían o aplaudan. Si alguien no quiere mostrar un movimiento, se busca una variante en que pueda participar. Nadie se burla de otro.",
    ],
    vocab=[("composición", "danza formada por varias partes unidas"), ("aportar", "dar algo mío al grupo"), ("acuerdo", "decisión que todos aceptan"), ("variante", "forma distinta de hacer lo mismo"), ("presentar", "mostrar a otros lo que hicimos")],
    worked=[
        W("Unir dos frases", "Tu frase tiene 3 movimientos (A) y la de Ema tiene 4 movimientos (B). Deciden hacer A, una pausa de 2 segundos y luego B. ¿Cuántos movimientos hay en total?", ["A tiene 3 movimientos.", "B tiene 4 movimientos.", "3 + 4 = 7."], "7 movimientos (más una pausa de 2 segundos)."),
        W("Resolver un desacuerdo", "Tú quieres empezar con tu frase y Ema también. ¿Cómo lo resuelven?", ["Hablamos con calma, sin gritar.", "Probamos una vez cada orden o echamos suertes sin pelear.", "Aceptamos el que quede y en el siguiente ensayo cambiamos."], "Prueban los dos órdenes y se turnan."),
    ],
    mistakes=[M("Cambiar la frase del compañero sin preguntar.", "Se cree que la propia es mejor.", "Pregunta antes de cambiar: «¿puedo proponer algo?»."),
              M("Reírse de un movimiento distinto.", "Da risa lo que no se conoce.", "Respeta: cada persona se expresa a su manera.")],
    tiers={
        "recovery": [
            ex("Una composición compartida es una danza que...", "Une partes de varias personas", "Cada uno aporta."),
            ex("Cuando termina la presentación, ¿qué haces: te ríes de un compañero o aplaudes?", "Aplaudes", "Se respeta a todos."),
            ex("¿Cuánta distancia se mantiene entre las personas?", "Dos brazos", "Para no chocar."),
        ],
        "understand": [
            ex("¿Por qué se hace un acuerdo antes de presentar?", "Para saber quién parte y cómo termina", "Así se evita la confusión."),
            ex("Si alguien no quiere mostrar un movimiento, ¿qué se busca?", "Una variante", "Así puede participar."),
            ex("¿Se cambia la frase de otro sin preguntar?", "No", "Hay que respetar su aporte."),
        ],
        "apply": [
            arith("La frase A tiene 3 movimientos y la B tiene 4. ¿Cuántos movimientos hay si se hacen ambas una vez?", "3+4", "Se suman los movimientos de las dos frases.", " movimientos"),
            arith("Repiten la composición de 7 movimientos 2 veces. ¿Cuántos movimientos hacen?", "7*2", "Se multiplica por las repeticiones.", " movimientos"),
            arith("La composición tiene una frase de 8 segundos, una pausa de 2 y otra frase de 10 segundos. ¿Cuántos segundos dura?", "8+2+10", "Se suman los tiempos.", " segundos"),
        ],
        "reason": [
            ex("Dani se ríe de los movimientos pequeños de Caro. ¿Qué le dices?", "Que cada persona se expresa a su manera", "Se debe respetar."),
            ex("Dos amigos quieren empezar los dos. ¿Qué es mejor: pelear o probar los dos órdenes?", "Probar los dos órdenes", "Resuelve con calma."),
        ],
        "challenge": [
            ex("Tres frases de 3, 4 y 5 movimientos se hacen una después de otra. ¿Cuántos movimientos hay?", "12", "3 más 4 más 5 son 12."),
            ex("Una composición de 2 personas dura 40 segundos de acción y 40 de pausa por intento, con 3 intentos. ¿Cuántos segundos totales (acción y pausa) dura?", "240", "Cada intento 80 s; 3 por 80 son 240."),
        ],
    },
    context=[ex("En una fiesta de la escuela, tu compañero hace un movimiento diferente al tuyo y otros se ríen. ¿Qué haces: A) te ríes también, B) dices «cada uno baila a su manera» y aplaudes, C) te vas?", "B", "Se valora la diferencia.")],
    selfcheck=[
        ex("¿Qué es una composición compartida?", "Una danza con partes de varias personas", "Cada uno aporta."),
        ex("Si A tiene 2 movimientos y B tiene 5, ¿cuántos suman?", "7", "2 más 5 son 7."),
        ex("¿Qué haces al terminar la presentación?", "Aplaudir", "Se respeta a todos."),
    ],
    open_task=task("Con un compañero o un familiar, unan sus frases. Cada uno usa su frase de 3 o más movimientos. Decidan el orden (quién parte), pongan una pausa de 2 segundos y repitan la composición 2 veces. Anoten cuántos movimientos hay en total y cómo se pusieron de acuerdo. Al final, cada uno dice algo bueno de la frase del otro.",
                   "Mi frase tiene 3 movimientos y la de Ema, 4. Hicimos la mía, 2 segundos de pausa y la de Ema, 2 veces: 14 movimientos. Acordamos probar los dos órdenes. Le dije a Ema que me gustó su final quieto.",
                   ["une dos frases con un acuerdo", "respeta la forma de moverse del otro", "da un comentario positivo"],
                   ["registro de movimientos", "demostración", "relato del acuerdo"],
                   ["cambiar la frase del otro sin preguntar", "burlarse", "no esperar el turno"],
                   "Pide un ejemplo de cómo lograron el acuerdo y refuerza un comentario respetuoso."),
    reinforce="Haz tu frase y luego la de un compañero, uno después del otro, con una pausa de 2 segundos.",
    extend="Agrega un tercer integrante con una frase de 2 movimientos y calcula cuántos movimientos hay en total.",
)
