"""Student material for 1.º básico Educación Física y Salud, OA 01 (habilidades motrices) y OA 02 (relaciones espaciales y temporales)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


OA1, OA2 = "EF01 OA 01", "EF01 OA 02"

# ---------------------------------------------------------------- OA 01
register(
    OA1, 1,
    materials="Un espacio de 4 × 4 m (patio o sala sin muebles en el centro), cuatro conos o cuatro botellas plásticas vacías, un reloj o cronómetro y un adulto que diga las señales. Zapatillas bien amarradas.",
    use="Aprenderé a caminar, correr y detenerme con control del cuerpo. Sirve para jugar en el patio sin chocar con nadie y sin caerme.",
    prior=["Sé caminar y correr.", "Sé qué es un compañero y qué es un cono."],
    explain=[
        "Caminar es avanzar con un pie siempre apoyado en el suelo. Correr es avanzar más rápido, con un momento en que los dos pies están en el aire. Detenerse es dejar de avanzar y quedar quieto, con los dos pies apoyados y las rodillas un poco dobladas para no caerte.",
        "Tener control significa que tu cuerpo hace lo que tú quieres: vas hacia donde miras, no chocas con nadie y paras cuando suena la señal. Correr muy rápido sin control es peligroso. Lo importante en esta clase no es llegar primero, sino frenar bien.",
        "Para frenar con equilibrio, baja la velocidad en los últimos pasos, separa un poco los pies, dobla las rodillas, mantén los brazos a los lados y mira al frente. Cuando estás quieto, cuenta mentalmente hasta tres antes de moverte de nuevo. En las estaciones de juego, un intento puede durar 40 segundos de acción y 40 segundos de pausa.",
    ],
    vocab=[("locomoción", "moverse de un lugar a otro, como caminar o correr"), ("control", "hacer que mi cuerpo vaya y pare donde quiero"), ("equilibrio", "quedar firme sin caerme"), ("señal", "palabra o sonido que dice qué hacer"), ("trayectoria", "el camino que sigue mi cuerpo")],
    worked=[
        W("Juego del semáforo", "Reglas: verde = correr, amarillo = caminar, rojo = detenerte y contar hasta 3. El adulto dice «verde», luego «amarillo» y luego «rojo». ¿Qué haces en cada señal?",
          ["Con «verde» corro mirando al frente y esquivando a los demás.", "Con «amarillo» bajo la velocidad y camino.", "Con «rojo» freno, separo los pies, doblo las rodillas y cuento 1, 2, 3."], "Corro, camino y me detengo en equilibrio, en ese orden."),
        W("Cuánto dura el circuito", "En la estación haces 40 segundos de acción y 40 de pausa, y repites eso 3 veces. ¿Cuántos segundos haces acción en total?",
          ["Cada intento tiene 40 segundos de acción.", "Hay 3 intentos, así que sumo 40 + 40 + 40.", "40 + 40 + 40 = 120."], "120 segundos de acción (2 minutos)."),
    ],
    mistakes=[M("Seguir corriendo varios pasos después de la señal de rojo.", "Se piensa que parar tarde no importa.", "Baja la velocidad antes y detente en el lugar donde suena la señal."),
              M("Mirar al suelo mientras corres.", "Cuesta dirigir el cuerpo si no se ve el camino.", "Mira al frente y esquiva a los compañeros con la vista.")],
    tiers={
        "recovery": [
            ex("En el semáforo, el adulto dice «rojo». ¿Qué haces? A) correr, B) caminar, C) detenerte.", "C", "Rojo siempre significa detenerse y quedar en equilibrio."),
            ex("En el semáforo, la señal «amarillo» pide caminar. ¿Vas más rápido o más lento que en «verde»?", "Más lento", "Caminar es más lento que correr."),
            ex("Para frenar sin caerte, ¿doblas un poco las rodillas o las dejas rígidas?", "Las doblas", "Las rodillas dobladas ayudan a quedar estable."),
        ],
        "understand": [
            ex("¿Cuál es la diferencia entre caminar y correr: en cuál hay un momento con los dos pies en el aire?", "Al correr", "Al caminar siempre hay un pie apoyado; al correr no."),
            ex("Tienes control si vas hacia donde miras y paras cuando suena la señal. Un niño sigue deslizándose tres pasos después del «rojo». ¿Tuvo control?", "No", "No se detuvo donde indicaba la señal."),
            ex("¿Para qué sirve contar hasta tres cuando quedas quieto?", "Para comprobar que estás en equilibrio", "Si te mantienes tres segundos sin moverte, el equilibrio es firme."),
        ],
        "apply": [
            ex("Hay 4 conos en las esquinas de un cuadrado de 4 × 4 m. Corres de un cono al siguiente y debes parar junto a cada uno. ¿Cuántas veces te detienes si pasas por los 4 conos?", "4 veces", "Hay una detención por cada cono."),
            ex("Reglas nuevas: «verde» = correr, «amarillo» = caminar, «rojo» = parar. El adulto dice: verde, rojo, amarillo, verde. ¿Cuántas veces corres?", "2 veces", "«Verde» aparece dos veces en la lista."),
            arith("Una estación tiene 40 segundos de acción y 40 de pausa por intento. ¿Cuántos segundos dura un intento completo (acción y pausa)?", "40+40", "Se suman la acción y la pausa.", " segundos"),
        ],
        "reason": [
            ex("Ana dice: «gana quien corre más rápido y para más lejos». Según esta clase, ¿qué está mal en su idea?", "Lo importante es el control, no la velocidad", "Frenar en el lugar correcto muestra control y evita choques."),
            ex("Dos niños frenan: Beto se queda quieto y firme con las rodillas dobladas; Caro frena y se tambalea. ¿Quién mostró mejor control?", "Beto", "Quedó estable sin tambalearse."),
        ],
        "challenge": [
            arith("El adulto da estas señales: verde 10 segundos, amarillo 10 segundos y rojo 5 segundos. Repite todo 2 veces. ¿Cuántos segundos dura el juego?", "(10+10+5)*2", "Primero se suma una ronda y luego se duplica.", " segundos"),
            ex("En un patio hay 6 niños corriendo en un cuadrado pequeño y 2 chocan. Propón una regla que baje el riesgo. Aceptable: «correr solo mirando al frente y esquivando», «caminar si hay mucha gente» o «ser menos niños por cuadrado».", "Una de las reglas aceptables", "Cualquier regla que dé espacio o baje la velocidad reduce los choques."),
        ],
    },
    context=[ex("Estás en el patio y suena el timbre del recreo: salen muchos niños corriendo hacia ti por el pasillo. ¿Qué haces: A) corres más fuerte, B) caminas o te detienes a un lado mirando al frente, C) cierras los ojos?", "B", "Caminar y mirar evita chocar con quienes vienen.")],
    selfcheck=[
        ex("¿Qué pide la señal «amarillo» en el semáforo de esta clase?", "Caminar", "Amarillo está definido como caminar."),
        ex("Para frenar con equilibrio, ¿miras al frente o al suelo?", "Al frente", "Mirar al frente ayuda a mantener el equilibrio y ver el camino."),
        ex("Si 3 intentos duran 40 segundos de acción cada uno, ¿cuántos segundos de acción son en total?", "120", "3 veces 40 segundos son 120 segundos."),
    ],
    open_task=task("Con ayuda de un adulto marca un cuadrado de 4 × 4 m con 4 objetos (conos, botellas vacías o zapatos). Juega el semáforo una vez: el adulto dice 8 señales en este orden: verde, amarillo, rojo, verde, rojo, amarillo, verde, rojo. En cada «rojo» queda quieto 3 segundos. Hay 3 «rojos». Cuenta en cuántos te detuviste con equilibrio y di cómo lo lograste.",
                   "Me detuve con equilibrio 3 de 3 veces: bajé la velocidad, separé los pies, doblé las rodillas y conté hasta tres sin moverme.",
                   ["alterna correr, caminar y detenerse según la señal", "se detiene sin tambalearse ni deslizarse", "mira al frente y no choca con nadie"],
                   ["observación de un adulto con la lista de señales", "relato oral del niño", "dibujo del recorrido con flechas"],
                   ["no detenerse en «rojo»", "correr mirando al suelo", "frenar con las rodillas rígidas"],
                   "Felicita lo que cumplió (por ejemplo, un frenado estable) y pide un solo ajuste: «la próxima vez baja la velocidad dos pasos antes del rojo»."),
    reinforce="Camina 10 pasos lentos y detente 3 segundos, 3 veces seguidas, mirando al frente.",
    extend="Inventa una cuarta luz (por ejemplo, azul = caminar en puntillas) y explica cómo mantienes el control.",
)

register(
    OA1, 2,
    materials="Una línea de tiza o cinta de 2 m en el suelo, una alfombra o pasto seco como superficie, zapatillas amarradas y espacio de 4 × 4 m.",
    use="Aprenderé a saltar con los dos pies juntos varias veces seguidas en una dirección y a caer sin perder el equilibrio. Sirve para saltar la cuerda y jugar en la plaza sin lastimarte.",
    prior=["Sé saltar en el mismo lugar.", "Sé qué significa adelante."],
    explain=[
        "Un salto con dos pies tiene tres partes: preparación, vuelo y aterrizaje. En la preparación doblas las rodillas y llevas los brazos atrás. En el vuelo estiras el cuerpo y empujas con los dos pies al mismo tiempo. En el aterrizaje caes con los dos pies a la vez.",
        "Para aterrizar estable, cae sobre la punta y luego sobre todo el pie, dobla las rodillas como si te sentaras en una silla pequeña y abre un poco los pies, a la altura de los hombros. Los brazos ayudan a equilibrarte. Un buen aterrizaje es silencioso.",
        "Saltar consecutivamente en una dirección es hacer varios saltos seguidos, sin parar, sin desviarte. Puedes saltar hacia adelante por encima de una línea, sin pisarla. Antes de saltar, revisa que el suelo esté seco y sin piedras ni objetos.",
    ],
    vocab=[("aterrizar", "caer al suelo después de un salto"), ("consecutivo", "uno después de otro, sin pausa"), ("dos pies", "ambos pies despegan y caen juntos"), ("rodillas flexionadas", "rodillas dobladas que amortiguan el golpe"), ("dirección", "hacia dónde avanzo")],
    worked=[
        W("Aterrizar estable", "Saltas desde una marca hacia adelante. ¿Cómo debes caer para quedar estable?", ["Despego con los dos pies a la vez.", "Estiro el cuerpo en el aire y miro al frente.", "Caigo con los dos pies, abro un poco las piernas, doblo las rodillas y mantengo los brazos abiertos 3 segundos."], "Caigo con dos pies, rodillas dobladas y equilibrio por 3 segundos."),
        W("Contar saltos", "Debes dar 5 saltos seguidos con dos pies en cada uno de 3 intentos. ¿Cuántos saltos haces en total?", ["En un intento son 5 saltos.", "Hay 3 intentos: 5 + 5 + 5.", "5 + 5 + 5 = 15."], "15 saltos."),
    ],
    mistakes=[M("Caer con las piernas estiradas.", "El impacto no se amortigua y duele.", "Dobla las rodillas al caer, como si te sentaras."),
              M("Saltar con un pie y luego con el otro.", "Se cree que es lo mismo.", "En esta clase los dos pies despegan juntos y caen juntos.")],
    tiers={
        "recovery": [
            ex("Un salto con dos pies, ¿despega con un pie o con los dos al mismo tiempo?", "Con los dos", "Así se define este salto."),
            ex("Al aterrizar, ¿doblas las rodillas o las dejas rectas?", "Las doblas", "Las rodillas dobladas amortiguan el golpe."),
            ex("Antes de saltar debes revisar el suelo. ¿Debe estar seco o mojado?", "Seco", "Un suelo mojado resbala."),
        ],
        "understand": [
            ex("Un aterrizaje silencioso, ¿suele ser suave o duro?", "Suave", "Si no hace ruido, las rodillas absorbieron el golpe."),
            ex("¿Qué hacen los brazos durante el aterrizaje?", "Ayudan a mantener el equilibrio", "Se abren o se mueven para no caer."),
            ex("Los tres momentos de un salto son preparación, vuelo y aterrizaje. ¿Cuál viene en medio?", "Vuelo", "Primero se prepara, luego se vuela, al final se cae."),
        ],
        "apply": [
            arith("Haces 5 saltos de dos pies por intento y 3 intentos. ¿Cuántos saltos son?", "5*3", "Se multiplican saltos por intentos.", " saltos"),
            ex("Hay una línea de 2 m en el suelo. Saltas con los dos pies por encima de ella, de lado a lado, 4 veces. Si pisas la línea una vez, ¿cuántos saltos limpios hiciste?", "3", "4 saltos menos 1 con pisada dan 3 limpios."),
            ex("Aterrizas y cuentas «1, 2, 3» sin moverte ni mover los pies. ¿Cuántos segundos mantuviste el equilibrio?", "3 segundos", "Cada número cuenta casi un segundo."),
        ],
        "reason": [
            ex("Beto salta y cae con las piernas estiradas y hace mucho ruido. ¿Qué le recomiendas?", "Doblar las rodillas al caer", "Así amortigua y cae en silencio."),
            ex("Caro salta tres veces seguidas en línea recta y Dani salta en zigzag. Para «consecutivo en una dirección», ¿quién cumple?", "Caro", "Ella mantuvo la misma dirección."),
        ],
        "challenge": [
            arith("En una carrera de saltos haces 4 intentos de 6 saltos y luego 1 intento de 4 saltos. ¿Cuántos saltos en total?", "4*6+4", "Primero se multiplica y luego se suma el último intento.", " saltos"),
            ex("Quieres saltar sobre una línea de 1 m y caer estable. Ordena: A) aterrizo con rodillas dobladas, B) doblo las rodillas, C) empujo con los dos pies. ¿Cuál es el orden correcto?", "B, C, A", "Primero preparo, luego empujo y al final aterrizo."),
        ],
    },
    context=[ex("En el patio hay una línea de tiza de 2 m y un charco de agua pegado al final. Quieres saltar la línea 5 veces. ¿Qué haces antes: A) saltar igual, B) avisar al adulto y buscar un lugar seco, C) correr rápido?", "B", "Un suelo mojado hace resbalar al aterrizar.")],
    selfcheck=[
        ex("¿Con cuántos pies despegas en un salto de esta clase?", "Con dos", "Es un salto con dos pies juntos."),
        ex("¿Qué haces con las rodillas al caer?", "Las doblo", "Amortiguan el golpe."),
        ex("Si haces 3 intentos de 5 saltos, ¿cuántos saltos son?", "15", "3 por 5 son 15."),
    ],
    open_task=task("Dibuja una línea de 2 m en el suelo con tiza, cinta o una cuerda. Haz 3 intentos de 5 saltos con los dos pies, en una sola dirección, sin pisar la línea. Después de cada intento cuenta «1, 2, 3» en equilibrio. Anota cuántos saltos fueron seguidos y cuántas veces quedaste estable.",
                   "Intento 1: 5 saltos seguidos y estable. Intento 2: 5 saltos, pisé la línea una vez. Intento 3: 5 saltos y estable. Quedé estable 2 de 3 veces.",
                   ["despega y cae con los dos pies a la vez", "aterriza con rodillas dobladas y sin desequilibrarse", "mantiene la dirección sin pisar la línea"],
                   ["registro con 3 intentos", "observación de un adulto", "relato del niño sobre su aterrizaje"],
                   ["caer con piernas estiradas", "saltar con un pie", "desviarse de la línea"],
                   "Destaca un aterrizaje bien logrado y pide un ajuste concreto, como mirar al frente o doblar más las rodillas."),
    reinforce="Salta 3 veces seguidas con los dos pies y mantén el equilibrio 3 segundos en el último aterrizaje.",
    extend="Salta hacia adelante, un cuarto de vuelta a la derecha y vuelve a saltar; explica cómo mantienes el equilibrio al caer.",
)

register(
    OA1, 3,
    materials="Una pelota blanda o un par de calcetines enrollados, una pared o un compañero, una marca a 3 pasos de distancia y reloj. Superficie plana lejos de ventanas y de otros niños.",
    use="Aprenderé a lanzar una pelota a un compañero y a recibirla con las manos. Sirve para jugar a la pelota con amigos y no perder el balón.",
    prior=["Sé qué es una pelota.", "Sé mirar a mi compañero."],
    explain=[
        "Para lanzar a un compañero, mira hacia él, lleva el brazo atrás, da un paso con el pie contrario a la mano que lanza y suelta la pelota a la altura del pecho de tu compañero. Tu mano sigue el movimiento hacia donde quieres que llegue la pelota.",
        "Para recibir, mira la pelota todo el camino. Pon las manos adelante, con los dedos abiertos y los pulgares juntos, formando una copa. Cuando la pelota llega, dobla un poco los brazos hacia ti para amortiguar y atrápala contra el pecho.",
        "La fuerza debe ser la justa: si lanzas muy fuerte, tu compañero no alcanza a recibirla; si lanzas muy flojo, cae antes. Se empieza cerca, a 3 pasos, y si resulta bien, se aleja un paso. Usa siempre una pelota blanda.",
    ],
    vocab=[("lanzar", "enviar una pelota con la mano"), ("recibir", "atrapar la pelota con las manos"), ("trayectoria", "el camino que hace la pelota en el aire"), ("fuerza", "cuánto empujo la pelota"), ("copa", "manos juntas con dedos abiertos, listas para atrapar")],
    worked=[
        W("Lanzar bien", "Vas a lanzar la pelota a un compañero que está a 3 pasos. ¿Cuáles son los pasos?", ["Lo miro a él, no a la pelota.", "Llevo el brazo atrás y doy un paso con el pie contrario.", "Suelto la pelota a la altura de su pecho y sigo el movimiento con la mano."], "Mirar, brazo atrás con paso, soltar a la altura del pecho."),
        W("Recibir bien", "La pelota viene hacia ti. ¿Cómo la atrapas?", ["Miro la pelota hasta que llega.", "Pongo las manos como copa, con los dedos abiertos.", "Cuando llega, doblo los brazos y la llevo al pecho."], "Atrapo con manos en copa y la llevo al pecho."),
    ],
    mistakes=[M("Lanzar mirando al suelo.", "Cuesta dirigir el lanzamiento sin ver al compañero.", "Mira al compañero y suelta la pelota a la altura de su pecho."),
              M("Atrapar con los brazos rígidos.", "La pelota rebota y se escapa.", "Dobla los brazos al recibir para amortiguar.")],
    tiers={
        "recovery": [
            ex("Antes de lanzar, ¿miras a tu compañero o al techo?", "A tu compañero", "Así diriges la pelota hacia él."),
            ex("Para recibir, ¿tus manos forman una copa o un puño?", "Una copa", "La copa deja espacio para atrapar."),
            ex("Para practicar, ¿conviene una pelota blanda o una dura?", "Blanda", "La pelota blanda no lastima."),
        ],
        "understand": [
            ex("Si lanzas demasiado fuerte, ¿qué le pasa a tu compañero?", "No alcanza a recibir la pelota", "La pelota llega muy rápido y se escapa."),
            ex("Doblar los brazos al recibir sirve para...", "Amortiguar la pelota", "El movimiento suaviza el impacto."),
            ex("En el lanzamiento, ¿cuándo sueltas la pelota: a la altura de tus rodillas o del pecho de tu compañero?", "Del pecho de tu compañero", "Es la altura donde más fácil se atrapa."),
        ],
        "apply": [
            arith("Haces 10 lanzamientos y atrapas 7. ¿Cuántos no atrapaste?", "10-7", "Se resta lo atrapado del total.", ""),
            ex("Empiezas a 3 pasos y, si atrapas 3 veces seguidas, te alejas 1 paso. Atrapaste 3 seguidas. ¿A cuántos pasos lanzarás ahora?", "4 pasos", "3 pasos más 1 paso son 4."),
            ex("Tu compañero está a 3 pasos, frente a ti. Tienes la pelota en la mano derecha. ¿Qué pie das adelante al lanzar: el derecho o el izquierdo?", "El izquierdo", "Se adelanta el pie contrario a la mano que lanza."),
        ],
        "reason": [
            ex("La pelota cae siempre antes de llegar a Caro. ¿Cuál es la causa más probable?", "Se lanzó con muy poca fuerza", "Una pelota que cae antes no tuvo fuerza para llegar."),
            ex("Dani cierra los ojos al recibir y se le cae la pelota. ¿Qué debe hacer?", "Mirar la pelota hasta que llegue", "Ver el camino permite poner las manos en el lugar correcto."),
        ],
        "challenge": [
            arith("Tu meta es 15 pases buenos. Ya hiciste 9. ¿Cuántos te faltan?", "15-9", "Se resta lo hecho de la meta.", " pases"),
            ex("Lanzas a un compañero que se mueve despacio hacia la derecha. ¿Lanzas hacia donde está ahora o hacia donde estará? Explica con una palabra: ahora/estará.", "Hacia donde estará", "La pelota tarda en llegar, así que debe llegar al lugar adonde él irá."),
        ],
    },
    context=[ex("En el recreo un niño te lanza una pelota de tenis muy dura desde 10 pasos. ¿Qué haces: A) la atrapas con la cara, B) le dices que use una pelota blanda y se acerque, C) corres?", "B", "Una pelota dura y lejana puede lastimar; se pide material blando y cercanía.")],
    selfcheck=[
        ex("¿Qué forma deben tener tus manos para recibir?", "De copa", "Con dedos abiertos y pulgares juntos."),
        ex("Si lanzas 8 veces y atrapan 5, ¿cuántas no atraparon?", "3", "8 menos 5 son 3."),
        ex("¿Se empieza lanzando desde cerca o desde lejos?", "Desde cerca", "Cerca es más fácil para controlar la fuerza."),
    ],
    open_task=task("Con una pelota blanda o calcetines enrollados y un adulto o hermano a 3 pasos, haz 10 lanzamientos. Anota cuántos llegaron a su pecho y cuántos recibiste tú. Si logras 3 seguidos, alarga 1 paso. Escribe una cosa que haces para atrapar bien.",
                   "De 10 lanzamientos, 8 llegaron al pecho de mi compañero. Yo atrapé 7. Alargué un paso a 4 pasos. Para atrapar bien miro la pelota y hago una copa con las manos.",
                   ["mira al compañero al lanzar", "recibe con manos en copa y brazos flexionados", "ajusta la fuerza según la distancia"],
                   ["registro de 10 lanzamientos", "observación de un adulto", "explicación oral del niño"],
                   ["lanzar mirando a otro lado", "atrapar con brazos rígidos", "lanzar sin avisar"],
                   "Reconoce los lanzamientos bien dirigidos y propone un ajuste: «mira la pelota hasta que toca tus manos»."),
    reinforce="Lanza y atrapa la pelota hacia arriba 5 veces contigo mismo, sin moverte.",
    extend="Haz 10 pases con un compañero y, en cada pase, aleja un poco más al compañero hasta que ya no logres recibir; anota la distancia.",
)

register(
    OA1, 4,
    materials="Una frazada gruesa, alfombra o colchoneta de unos 2 m, sin muebles alrededor. Para suspensiones, solo si hay un adulto: una barra baja de plaza con pies cerca del suelo; si no hay, usa la variante de plancha. Reloj.",
    use="Aprenderé a girar, a rodar de lado y a colgarme con control. Sirve para moverme con seguridad en juegos de plaza y gimnasia.",
    prior=["Sé qué es dar una vuelta.", "Sé que debo dejar espacio entre las personas."],
    explain=[
        "Girar es dar una vuelta con el cuerpo sin moverte de lugar. Una vuelta completa vuelve a la misma posición; media vuelta termina mirando para el lado contrario. Para girar con control, mira un punto fijo, mantén los brazos cerca del cuerpo y detente apoyando los dos pies.",
        "La rodada lateral se hace sobre una superficie blanda y limpia: acuéstate de lado con los brazos estirados sobre la cabeza y el cuerpo largo como un tronco; luego rueda hacia el otro lado. No se hace en cemento ni cerca de muebles. La rodada hacia adelante solo se practica con colchoneta y un adulto presente.",
        "Colgarse de una barra se llama suspensión. Solo se hace en una barra baja de plaza, con los pies cerca del suelo, con las dos manos y un adulto al lado. Se cuenta cinco segundos y se baja con control. En las estaciones de esta clase, un intento puede durar 20 segundos de acción y 20 de pausa. Si no hay barra, haz la plancha: manos y pies en el suelo por cinco segundos. Deja siempre dos brazos de distancia entre personas.",
    ],
    vocab=[("giro", "vuelta del cuerpo en el mismo lugar"), ("rodada lateral", "rodar de lado con el cuerpo estirado"), ("suspensión", "colgarse de una barra sin apoyar los pies"), ("distancia segura", "espacio libre entre personas, dos brazos estirados"), ("colchoneta", "superficie blanda para rodar")],
    worked=[
        W("Media vuelta y vuelta completa", "Estás mirando a la puerta. Haces media vuelta. ¿Hacia dónde miras? Si haces una vuelta completa, ¿hacia dónde miras?", ["La media vuelta me deja mirando al lado contrario de la puerta.", "Una vuelta completa vuelve a la posición de partida.", "Entonces vuelvo a mirar la puerta."], "Media vuelta: espalda a la puerta; vuelta completa: miro la puerta."),
        W("Tiempo de la estación", "En la estación haces 20 segundos de acción y 20 de pausa, 3 veces. ¿Cuántos segundos haces acción en total?", ["Un intento tiene 20 segundos de acción.", "20 + 20 + 20 = 60.", "Son 60 segundos, o 1 minuto."], "60 segundos de acción."),
    ],
    mistakes=[M("Rodar en el suelo duro del patio.", "No se piensa en el golpe del suelo.", "Rueda solo sobre colchoneta o frazada gruesa en una superficie blanda."),
              M("Colgarse de un mueble o de una rama.", "Parece lo mismo que una barra de plaza.", "Solo cuélgate de una barra baja hecha para eso y con un adulto.")],
    tiers={
        "recovery": [
            ex("Media vuelta, ¿termina mirando al mismo lado o al lado contrario?", "Al lado contrario", "Media vuelta cambia el lado hacia el que miras."),
            ex("La rodada lateral se hace sobre una superficie ¿dura o blanda?", "Blanda", "El suelo blando evita golpes."),
            ex("Para colgarte de una barra, ¿debe haber un adulto contigo?", "Sí", "La supervisión evita caídas."),
        ],
        "understand": [
            ex("¿Por qué se dejan dos brazos de distancia entre personas al rodar o girar?", "Para no chocar", "Con ese espacio nadie golpea a otro."),
            ex("En la rodada lateral, ¿el cuerpo va encogido o largo como un tronco?", "Largo como un tronco", "El cuerpo estirado rueda recto."),
            ex("¿Qué significa «suspensión»?", "Colgarse de una barra", "Es mantener el cuerpo colgando sin apoyar los pies."),
        ],
        "apply": [
            ex("Estás mirando a la ventana de la sala. Haces una vuelta completa. ¿Hacia dónde miras al final?", "A la ventana", "Una vuelta completa vuelve al punto de partida."),
            arith("Cuentas 5 segundos de suspensión en cada uno de 3 intentos. ¿Cuántos segundos colgado en total?", "5*3", "Se multiplica el tiempo por los intentos.", " segundos"),
            ex("Estiras los brazos a los lados y con una mano tocas a tu compañero. ¿Debes alejarte antes de girar?", "Sí", "Si tus brazos estirados tocan a alguien, no hay distancia segura."),
        ],
        "reason": [
            ex("Beto quiere rodar en el cemento del patio «porque es más rápido». ¿Es buena idea?", "No", "El cemento duro puede lastimar; hay que usar una superficie blanda."),
            ex("No hay barra baja. ¿Qué puedes hacer en lugar de colgarte para trabajar los brazos de forma segura?", "La plancha con manos y pies en el suelo por 5 segundos", "Es una variante segura sin altura."),
        ],
        "challenge": [
            arith("Haces 20 segundos de acción y 20 de pausa durante 3 intentos. ¿Cuántos segundos dura todo, incluyendo las pausas?", "(20+20)*3", "Cada intento tiene acción y pausa.", " segundos"),
            ex("Orden de un mini-circuito: A) rodada lateral, B) giro de vuelta completa, C) plancha de 5 s. Lo haces dos veces: A, B, C, A, B, C. ¿Cuántas acciones haces en total?", "6", "3 acciones por 2 repeticiones son 6."),
        ],
    },
    context=[ex("En casa hay una alfombra delgada, pero con la esquina de una mesa de vidrio a 50 cm. ¿Haces rodadas ahí: A) sí, B) no, muevo la mesa o cambio de lugar con un adulto?", "B", "La mesa muy cerca puede golpearte; se necesita espacio libre.")],
    selfcheck=[
        ex("¿Qué distancia segura se deja entre personas?", "Dos brazos", "Es el espacio para no golpear a otro."),
        ex("¿Se puede rodar de lado en cemento?", "No", "El suelo duro lastima."),
        ex("Una suspensión de 5 s repetida 2 veces, ¿cuántos segundos son?", "10", "2 por 5 son 10."),
    ],
    open_task=task("Con un adulto, en una alfombra o frazada sin muebles cerca, haz 3 rodadas laterales hacia la derecha y 3 hacia la izquierda (6 en total), con el cuerpo largo. Luego haz 3 giros de una vuelta completa mirando un punto fijo y 1 plancha de 5 segundos. Cuenta cuántas veces mantuviste el control.",
                   "Hice 6 rodadas, 5 con el cuerpo largo y una encogida. Hice 3 giros mirando la lámpara. Sostuve la plancha 5 segundos. Mantuve el control 9 de 10 veces.",
                   ["usa superficie blanda y deja distancia segura", "mantiene el cuerpo largo al rodar", "termina cada acción estable"],
                   ["registro con conteos", "observación de un adulto", "dibujo del espacio usado"],
                   ["rodar sobre suelo duro", "hacer suspensión sin adulto", "no dejar distancia"],
                   "Destaca un buen control y sugiere un ajuste: «alarga más los brazos sobre la cabeza al rodar»."),
    reinforce="Haz 2 giros de media vuelta mirando un punto fijo y quédate en equilibrio 3 segundos.",
    extend="Gira una vuelta completa y luego camina sobre una línea de 2 m sin salirte; explica cómo mantuviste el control.",
)

register(
    OA1, 5,
    materials="Cinco estaciones marcadas con cinta o tiza en un espacio de 4 × 4 m, una pelota blanda, una frazada para rodar y reloj. Un adulto da la señal de inicio y de cambio.",
    use="Aprenderé a unir caminar sobre una línea, saltar, lanzar, girar y rodar en un circuito, con control y seguridad. Sirve para jugar y practicar varias habilidades seguidas.",
    prior=["Sé caminar, saltar y lanzar con control.", "Sé dejar distancia segura."],
    explain=[
        "Un circuito es un camino con varias estaciones; en cada una haces una acción distinta. Hoy hay cinco estaciones: 1) caminar sobre una línea manteniendo el equilibrio, 2) tres saltos con dos pies, 3) lanzar la pelota a un compañero o a una pared y recibirla, 4) un giro de una vuelta y 5) una rodada lateral sobre la frazada.",
        "En cada estación trabajas 30 segundos y descansas 30 segundos mientras el adulto te dice el cambio. No se corre entre estaciones: se camina. Quien espera su turno se queda fuera del cuadrado, a dos brazos de distancia, y observa un criterio.",
        "Al terminar cada estación, revisa tu control con tres preguntas: ¿miré al frente?, ¿terminé estable?, ¿respeté la distancia? Si una respuesta es «no», repite esa estación más lento. En esta clase importa más el control que la velocidad.",
    ],
    vocab=[("circuito", "recorrido con varias estaciones"), ("estación", "lugar donde hago una acción"), ("enlazar", "hacer una acción después de otra sin perder el control"), ("criterio", "lo que se mira para saber si está bien hecho"), ("turno", "momento en que me toca")],
    worked=[
        W("Duración del circuito", "Cada una de las 5 estaciones dura 30 segundos de acción y 30 de pausa. ¿Cuántos segundos dura el circuito completo?", ["En una estación: 30 + 30 = 60 segundos.", "Son 5 estaciones: 60 × 5.", "60 × 5 = 300 segundos."], "300 segundos (5 minutos)."),
        W("Revisar mi control", "Terminas la estación de saltos y te tambaleaste al caer. ¿Qué haces?", ["Respondo las tres preguntas: miré al frente, sí; estable, no; distancia, sí.", "Lo que falló fue la estabilidad.", "Repito la estación más lento y con las rodillas más dobladas."], "Repito los saltos más lento, con rodillas más dobladas."),
    ],
    mistakes=[M("Correr entre estaciones para ganar tiempo.", "Se piensa que es una carrera.", "Camina entre estaciones; el circuito es de control."),
              M("Esperar el turno dentro del cuadrado.", "Se quiere ver más de cerca.", "Espera afuera, a dos brazos de distancia.")],
    tiers={
        "recovery": [
            ex("La estación 1 pide caminar sobre una línea. ¿Qué mantienes?", "El equilibrio", "El objetivo es no salirse de la línea."),
            ex("En el circuito, entre estaciones, ¿corres o caminas?", "Caminas", "Se camina para mantener el control."),
            ex("Mientras esperas tu turno, ¿te quedas dentro del cuadrado o fuera?", "Fuera", "Dentro estorbarías a quien se mueve."),
        ],
        "understand": [
            ex("¿Para qué sirven las tres preguntas finales (miré al frente, terminé estable, respeté la distancia)?", "Para revisar mi control", "Permiten ver qué cuidar."),
            ex("¿Qué es un circuito?", "Un recorrido con varias estaciones", "En cada estación hay una acción."),
            ex("Si te equivocaste en la estación de giro, ¿qué haces: repetir más lento o saltarla?", "Repetir más lento", "Se corrige con más control."),
        ],
        "apply": [
            arith("Hay 5 estaciones de 30 segundos de acción cada una. ¿Cuántos segundos de acción hay en total?", "5*30", "Se multiplica el tiempo de acción por las estaciones.", " segundos"),
            arith("Cada estación tiene 30 segundos de acción y 30 de pausa. ¿Cuánto dura una estación completa?", "30+30", "Se suman acción y pausa.", " segundos"),
            ex("En la estación 3 haces 6 lanzamientos y recibes 4. ¿Cuántos no recibiste?", "2", "6 menos 4 son 2."),
        ],
        "reason": [
            ex("Ana terminó primero porque corrió entre estaciones, pero chocó con un cono. Según el circuito, ¿qué debe cambiar?", "Caminar y cuidar el control", "Chocar muestra falta de control, no importa ser primero."),
            ex("Un niño quiere hacer la rodada lateral en el cemento por no ensuciar la frazada. ¿Qué le dices?", "Que ruede sobre la frazada", "El suelo duro puede lastimar."),
        ],
        "challenge": [
            ex("Ordena las estaciones: giro, saltos, línea, rodada, lanzar. Según el circuito de hoy, ¿cuál es el orden?", "Línea, saltos, lanzar, giro, rodada", "Es el orden en que se explicaron las cinco estaciones."),
            arith("Hiciste el circuito 2 veces. Cada vuelta dura 300 segundos. ¿Cuántos minutos son en total? Responde en minutos.", "(300*2)//60", "Se suman los segundos y se pasan a minutos.", " minutos"),
        ],
    },
    context=[ex("Hay 6 niños para el circuito y solo un cuadrado de 4 × 4 m. ¿Cuántos deberían estar dentro a la vez para tener espacio: A) todos, B) uno o dos, C) cinco?", "B", "Con más niños no hay distancia segura en 4 × 4 m.")],
    selfcheck=[
        ex("¿Cuántas estaciones tiene el circuito?", "5", "Línea, saltos, lanzar, giro y rodada."),
        ex("¿Se corre o se camina entre estaciones?", "Se camina", "Así se mantiene el control."),
        ex("¿Qué pregunta de control pide mirar hacia adelante?", "¿Miré al frente?", "Es la primera pregunta de control."),
    ],
    open_task=task("Haz el circuito de 5 estaciones: 1) caminar sobre una línea de 2 m, 2) 3 saltos con dos pies, 3) 5 lanzamientos con recibo a un compañero o a la pared, 4) 1 giro de vuelta completa, 5) 1 rodada lateral en la frazada. Trabaja 30 segundos y descansa 30 en cada estación. Al terminar, responde sí o no a las tres preguntas de control para cada estación.",
                   "Línea: sí, sí, sí. Saltos: sí, no, sí. Lancé y recibí 4 de 5. Giro: sí, sí, sí. Rodada: sí, sí, sí. Repetiré los saltos más lento.",
                   ["enlaza las cinco acciones con control", "respeta las pausas y la distancia", "revisa su desempeño con las tres preguntas"],
                   ["tabla de sí/no por estación", "observación de un adulto", "relato oral"],
                   ["correr entre estaciones", "no revisar el control", "olvidar la distancia segura"],
                   "Nombra primero lo que salió bien y elige una estación para mejorar con un consejo concreto."),
    reinforce="Haz solo las estaciones de la línea y de los saltos, dos veces, con descanso de 30 segundos.",
    extend="Cambia el orden de las estaciones y explica qué estación te resulta más difícil después de girar.",
)

# ---------------------------------------------------------------- OA 02
register(
    OA2, 1,
    materials="Una pulsera de papel o cinta para la mano derecha, dos flechas de papel (una que apunta a la derecha y otra a la izquierda) y un espacio libre. Música lenta con pulso claro si la hay.",
    use="Aprenderé a distinguir mi derecha y mi izquierda, arriba y abajo, usando mi propio cuerpo. Sirve para seguir instrucciones en los juegos y para saber dónde quedan las cosas.",
    prior=["Sé nombrar mis manos y pies.", "Sé qué es arriba y qué es abajo."],
    explain=[
        "Tu cuerpo es el punto de partida para ubicar las cosas. Tienes un lado derecho y un lado izquierdo. La mano derecha y el pie derecho están del mismo lado; igual la izquierda. Para recordarlo, ponte una pulsera de papel en la mano derecha.",
        "Arriba es hacia el cielo o el techo; abajo es hacia el suelo. Tu cabeza está arriba de tu cuerpo y tus pies están abajo. Cuando levantas los brazos, los llevas arriba. Cuando tocas el suelo, vas hacia abajo.",
        "Tu derecha y tu izquierda son partes de tu cuerpo y no cambian. Si te das la vuelta, tu mano derecha sigue siendo derecha, aunque ahora esté al otro lado de la sala. Para seguir una orden como «mano derecha arriba», levanta la mano con pulsera por sobre la cabeza.",
    ],
    vocab=[("derecha", "el lado de mi cuerpo donde tengo la pulsera"), ("izquierda", "el lado de mi cuerpo sin pulsera"), ("arriba", "hacia el techo o el cielo"), ("abajo", "hacia el suelo"), ("ubicación", "el lugar donde está algo")],
    worked=[
        W("Seguir una orden", "El adulto dice: «mano derecha arriba, pie izquierdo adelante». ¿Qué haces?", ["Busco mi pulsera: esa es la mano derecha.", "Levanto esa mano por sobre mi cabeza.", "Pongo el pie del otro lado adelante: el izquierdo."], "Mano con pulsera arriba y pie sin pulsera adelante."),
        W("Mano arriba, mano abajo", "Levantas la mano derecha y bajas la izquierda. Luego bajas la derecha y subes la izquierda. ¿Cuál queda arriba al final?", ["Primero arriba: derecha; abajo: izquierda.", "Después cambian: abajo derecha; arriba izquierda.", "Al final la mano que está arriba es la izquierda."], "La mano izquierda."),
    ],
    mistakes=[M("Confundir derecha e izquierda al darse vuelta.", "Se mira dónde queda la pared, no el cuerpo.", "Mira tu pulsera: la mano derecha siempre es la de la pulsera."),
              M("Subir las dos manos cuando se pide solo una.", "Se oye «mano» y no se escucha cuál.", "Escucha primero qué lado y después qué dirección.")],
    tiers={
        "recovery": [
            ex("Te pones una pulsera en la mano derecha. ¿Cuál es tu mano izquierda: la que tiene pulsera o la que no?", "La que no tiene pulsera", "Es la otra mano."),
            ex("¿Hacia dónde va «arriba»: al techo o al suelo?", "Al techo", "Arriba es hacia el cielo o el techo."),
            ex("¿Hacia dónde va «abajo»: al techo o al suelo?", "Al suelo", "Abajo es hacia el suelo."),
        ],
        "understand": [
            ex("Si te das la vuelta, ¿tu mano derecha cambia a izquierda?", "No", "La mano derecha sigue siendo derecha."),
            ex("¿Qué parte del cuerpo suele estar abajo: la cabeza o los pies?", "Los pies", "Los pies tocan el suelo."),
            ex("Para saber derecha o izquierda, ¿miras tu cuerpo o la pared?", "Tu cuerpo", "El cuerpo es la referencia."),
        ],
        "apply": [
            ex("Orden: «pie derecho adelante, mano izquierda arriba». ¿Qué mano levantas?", "La izquierda", "La orden nombra la mano izquierda."),
            ex("Orden: «toca con la mano derecha tu rodilla izquierda». ¿Qué mano usas y qué rodilla tocas?", "Mano derecha, rodilla izquierda", "Se sigue cada palabra de la orden."),
            ex("Estás de pie con los brazos arriba. El adulto dice «baja la mano izquierda». ¿Cuántas manos quedan arriba?", "1", "Solo queda la derecha arriba."),
        ],
        "reason": [
            ex("Ana dice «mi derecha cambió a izquierda porque me di vuelta». ¿Está bien lo que dice?", "No", "El lado de tu cuerpo no cambia, solo hacia dónde miras."),
            ex("Beto levantó las dos manos cuando se pidió «mano derecha arriba». ¿Qué debe corregir?", "Levantar solo la mano derecha", "La orden nombra una sola mano."),
        ],
        "challenge": [
            ex("Secuencia: «derecha arriba, izquierda arriba, derecha abajo». Al final, ¿qué mano sigue arriba?", "La izquierda", "La derecha bajó al final y la izquierda quedó."),
            ex("Orden: «pie derecho adelante, luego pie derecho vuelve atrás, luego pie izquierdo adelante». ¿Qué pie queda adelante al terminar?", "El izquierdo", "El derecho volvió atrás y el izquierdo sigue adelante."),
        ],
    },
    context=[ex("En el patio la profesora dice: «los niños con pulsera en la derecha van hacia la puerta». Tú tienes la pulsera en tu mano derecha. ¿Vas hacia la puerta?", "Sí", "La pulsera está en tu mano derecha.")],
    selfcheck=[
        ex("¿Dónde te pones la pulsera para saber tu derecha?", "En la mano derecha", "Esa es su función."),
        ex("¿Qué es lo contrario de arriba?", "Abajo", "Son direcciones opuestas."),
        ex("Si levantas la mano izquierda, ¿cuántas manos quedan abajo?", "1", "La otra mano sigue abajo."),
    ],
    open_task=task("Ponte una pulsera de papel en la mano derecha. Ejecuta con un adulto esta lista de 6 órdenes: 1) mano derecha arriba, 2) mano izquierda arriba, 3) mano derecha abajo, 4) pie izquierdo adelante, 5) pie derecho adelante, 6) toca tu rodilla derecha con la mano izquierda. Anota cuántas hiciste bien sin mirar la pulsera.",
                   "Hice bien 5 de 6. Me equivoqué en la orden 3 porque bajé la izquierda. Miré mi pulsera y entendí.",
                   ["distingue derecha e izquierda", "distingue arriba y abajo", "sigue la orden completa"],
                   ["lista marcada con aciertos", "observación de un adulto", "dibujo de las seis posiciones"],
                   ["cambiar derecha por izquierda", "mover ambas partes del cuerpo", "no escuchar la orden completa"],
                   "Destaca las órdenes bien hechas y recomienda mirar la pulsera solo cuando dudes, con meta de acertar sin ella."),
    reinforce="Levanta la mano derecha y di «derecha»; luego la izquierda y di «izquierda». Hazlo 5 veces.",
    extend="Haz una secuencia de 4 posiciones (por ejemplo, derecha arriba, izquierda abajo, ...) y enséñasela a alguien de tu casa.",
)

register(
    OA2, 2,
    materials="Un aro (o un círculo dibujado con cuerda o tiza de unos 60 cm), tres conos o botellas vacías, un cojín o pañuelo y un espacio libre de 4 × 4 m.",
    use="Aprenderé a ubicarme dentro, fuera, entre y al lado de objetos. Sirve para seguir instrucciones de juego y para explicar dónde está algo.",
    prior=["Sé qué es un aro o un círculo.", "Sé nombrar derecha e izquierda."],
    explain=[
        "Dentro significa en el interior de algo; fuera, en el exterior. Si estás en el aro, estás dentro; si tus pies están en el suelo y no en el aro, estás fuera. Entre es estar en el medio de dos cosas, y al lado es estar junto, en un costado.",
        "Cuando se habla de lugar, siempre se necesita un objeto de referencia. Por ejemplo, «al lado del cono» es el lugar junto al cono. «Entre los dos conos» es el espacio que queda entre uno y otro. Mira bien cuál es el objeto de referencia antes de moverte.",
        "En el juego «La casa del aro» seguirás órdenes de ubicación. Muévete caminando, con cuidado, y detente en el lugar justo. Todos deben respetar la distancia segura y no empujar a nadie al buscar su lugar.",
    ],
    vocab=[("dentro", "en el interior de algo"), ("fuera", "en el exterior de algo"), ("entre", "en el medio de dos cosas"), ("al lado", "junto a algo, en un costado"), ("objeto de referencia", "la cosa que uso para decir dónde estoy")],
    worked=[
        W("Dónde me ubico", "Hay dos conos separados por 1 m. La orden dice «ponte entre los conos». ¿Dónde te paras?", ["Busco los dos conos.", "Me muevo al espacio que queda en el medio.", "Compruebo que un cono quede a cada lado de mí."], "En el espacio que queda entre ambos conos."),
        W("Juego «La casa del aro»", "Reglas: 1) camina libre por el cuadrado; 2) cuando el adulto diga una orden (dentro del aro, fuera del aro, al lado del aro), te ubicas en ese lugar; 3) si llegas y hay otra persona, te pones al lado. El adulto dice «fuera del aro». ¿Qué haces?", ["Escucho la ubicación: fuera.", "Camino hacia cualquier lugar que no sea el aro.", "Me detengo en equilibrio y compruebo que mis pies no están en el aro."], "Me detengo en cualquier lugar fuera del aro."),
    ],
    mistakes=[M("Pararse sobre el borde del aro y decir que está dentro.", "No hay una línea clara para dentro y fuera.", "Dentro es con los dos pies adentro del aro; fuera es con los dos pies afuera."),
              M("Confundir «entre» con «al lado».", "Se piensa que es lo mismo.", "Entre es en el medio de dos cosas; al lado es junto a una cosa.")],
    tiers={
        "recovery": [
            ex("Si tus dos pies están en el interior del aro, ¿estás dentro o fuera?", "Dentro", "El interior del aro es dentro."),
            ex("Si estás en el suelo, a dos pasos del aro, ¿estás dentro o fuera?", "Fuera", "No estás en el interior."),
            ex("Estás en el medio de dos conos. ¿Estás entre ellos o al lado de uno?", "Entre ellos", "Estar en el medio es entre."),
        ],
        "understand": [
            ex("¿Qué necesitas para decir «al lado»: un objeto de referencia o nada?", "Un objeto de referencia", "Al lado siempre es al lado de algo."),
            ex("¿«Entre» necesita uno o dos objetos?", "Dos", "Entre es en el medio de dos cosas."),
            ex("En «La casa del aro», si el adulto dice «dentro del aro», ¿vas al aro o te alejas?", "Voy al aro", "Dentro es en el interior."),
        ],
        "apply": [
            ex("En la mesa hay un cojín, una pelota y un vaso en fila, en ese orden. ¿Qué está entre el cojín y el vaso?", "La pelota", "Está en el medio de los dos."),
            ex("Hay 3 conos en fila: rojo, amarillo, azul. ¿Qué cono queda entre los otros dos?", "El amarillo", "Está en el medio de rojo y azul."),
            ex("Hay 4 niños y 1 aro. 2 están dentro del aro y el resto fuera. ¿Cuántos están fuera?", "2", "4 menos 2 son 2."),
        ],
        "reason": [
            ex("Dani dice «estoy entre el cono» porque está pegado a un solo cono. ¿Qué palabra le corresponde?", "Al lado", "Está junto a un solo cono."),
            ex("En el juego, llegas a tu lugar y ya hay un compañero dentro del aro. ¿Qué haces?", "Me pongo al lado del aro sin empujar", "Se respeta el espacio de todos."),
        ],
        "challenge": [
            ex("Hay un aro en el centro, un cono a la izquierda del aro y otro a la derecha. Te paras entre el cono y el aro, al lado del aro. ¿Estás dentro del aro?", "No", "Estás junto a él, no en su interior."),
            ex("Orden doble: «primero dentro del aro, luego fuera del aro y al lado del cono». ¿Cuántos lugares debes visitar?", "2", "Visitas primero el aro y luego un lugar fuera, junto al cono."),
        ],
    },
    context=[ex("En la sala hay una mesa y dos sillas. Tu profesora dice: «guarda el cuaderno entre las dos sillas». ¿Lo dejas debajo de la mesa o en el espacio del medio de las sillas?", "En el espacio del medio de las sillas", "Entre es en el medio de dos cosas.")],
    selfcheck=[
        ex("¿Qué palabra usas para el interior de algo?", "Dentro", "Es lo contrario de fuera."),
        ex("Si estás en el medio de dos conos, ¿qué palabra usas?", "Entre", "Estás en el medio."),
        ex("Si estás junto a un cono, ¿qué palabra usas?", "Al lado", "Es un costado."),
    ],
    open_task=task("Usa un aro (o un círculo de cuerda), dos conos (o botellas) y un cojín. Pon el aro en el centro, un cono a cada lado del aro y el cojín al final de la fila. Con un adulto, ejecuta las órdenes: 1) dentro del aro, 2) fuera del aro, 3) entre el aro y un cono, 4) al lado del cojín. Cuenta cuántas ubicaciones hiciste bien.",
                   "Hice 4 de 4: dentro del aro con los dos pies, fuera caminando, entre el aro y el cono con espacio a cada lado, y al lado del cojín.",
                   ["se ubica según cada palabra", "usa el objeto de referencia", "se mueve con cuidado y sin empujar"],
                   ["registro de 4 órdenes", "observación de un adulto", "dibujo del plano con aro, conos y cojín"],
                   ["confundir entre con al lado", "pararse en el borde del aro", "empujar a otros"],
                   "Reconoce qué ubicaciones hizo bien y practica una más con palabras de referencia."),
    reinforce="Con un aro, métete dentro y sal fuera cinco veces diciendo «dentro» y «fuera».",
    extend="Inventa 3 órdenes de ubicación con tu cojín y un cono, y pídele a alguien que las cumpla.",
)

register(
    OA2, 3,
    materials="Un compañero o adulto, una cuerda o marca en el suelo, un espacio de 4 × 4 m y un cono. Cinta o tiza para marcar pasos de distancia.",
    use="Aprenderé a moverme delante, detrás, cerca y lejos de un compañero. Sirve para jugar en pareja y respetar el espacio del otro.",
    prior=["Sé qué es una fila.", "Sé dar pasos del mismo tamaño."],
    explain=[
        "Delante es el lado hacia donde mira una persona. Detrás es el lado opuesto, el de su espalda. Si dos niños están en fila, el primero está delante y el último está detrás. Para saber quién está delante, mira hacia dónde mira la fila.",
        "Cerca y lejos se pueden medir en pasos. En esta clase, cerca es una distancia de 1 paso y lejos es una distancia de 5 pasos. Si tu compañero está a 2 pasos, no estás ni cerca ni lejos: estás a distancia media. Los pasos deben ser de tamaño normal, no gigantes.",
        "En el juego «La sombra», uno es el guía y otro es la sombra. La sombra va detrás del guía a 1 paso y copia su movimiento. A la señal «lejos», la sombra se queda quieta y el guía sigue caminando hasta quedar a 5 pasos de ella. A la señal «cerca», la sombra camina hasta quedar a 1 paso. Se juega caminando, sin empujar y mirando por dónde se va.",
    ],
    vocab=[("delante", "el lado hacia donde mira alguien"), ("detrás", "el lado de la espalda"), ("cerca", "a 1 paso de distancia en este juego"), ("lejos", "a 5 pasos de distancia en este juego"), ("guía", "quien dirige el movimiento")],
    worked=[
        W("Fila de cuatro", "Ana, Beto, Caro y Dani están en fila, todos mirando a la puerta, en ese orden de la puerta hacia atrás: Ana, Beto, Caro, Dani. ¿Quién está delante de Caro y quién está detrás de ella?", ["La puerta está delante. Ana es la primera.", "Delante de Caro está Beto.", "Detrás de Caro está Dani."], "Delante: Beto; detrás: Dani."),
        W("Juego «La sombra»", "Reglas: 1) el guía camina lento y la sombra va detrás a 1 paso; 2) la sombra copia lo que hace el guía; 3) a la señal «lejos», la sombra se queda quieta mientras el guía camina hasta quedar a 5 pasos de ella; 4) a la señal «cerca», la sombra camina hasta quedar a 1 paso. El adulto dice «lejos». ¿Qué haces si eres la sombra?", ["Estoy detrás del guía, a 1 paso.", "Me quedo quieta y cuento en voz baja los 4 pasos que camina el guía, hasta quedar a 5 pasos.", "Sigo mirando al guía para copiar su movimiento."], "Me quedo quieta hasta que el guía queda a 5 pasos y sigo mirándolo."),
    ],
    mistakes=[M("Pegarse al guía y pisarle los talones.", "Se quiere estar cerca de más.", "Cerca es 1 paso; deja ese espacio."),
              M("Decir que delante es siempre «hacia la pared».", "No se mira hacia dónde mira la persona.", "Delante es hacia donde mira la persona.")],
    tiers={
        "recovery": [
            ex("Si miras la puerta, la puerta está ¿delante o detrás de ti?", "Delante", "Delante es hacia donde miras."),
            ex("En una fila, el último, ¿está delante o detrás de los demás?", "Detrás", "El último queda al final."),
            ex("En este juego, «cerca» son ¿1 paso o 5 pasos?", "1 paso", "Así lo definimos."),
        ],
        "understand": [
            ex("En este juego, «lejos» son ¿1 paso o 5 pasos?", "5 pasos", "Lejos es mayor distancia."),
            ex("En «La sombra», ¿quién copia los movimientos?", "La sombra", "El guía los dirige."),
            ex("¿Por qué se miden cerca y lejos en pasos?", "Para saber la distancia con una medida igual para todos", "Los pasos dan una medida."),
        ],
        "apply": [
            ex("Ema, Fito y Gaby están en fila mirando a la puerta; Ema es la primera. ¿Quién está detrás de Fito?", "Gaby", "Gaby va después de Fito en la fila."),
            arith("Estás a 5 pasos de tu compañero y avanzas 4 pasos. ¿A cuántos pasos quedas?", "5-4", "Se restan los pasos que avanzas.", " paso"),
            ex("Estás a 1 paso detrás del guía. A la señal «lejos», el guía camina hasta quedar a 5 pasos de ti. ¿Cuántos pasos camina el guía?", "4", "De 1 a 5 hay 4 pasos de diferencia."),
        ],
        "reason": [
            ex("Beto está a 3 pasos de Caro. ¿Está cerca, lejos o a distancia media, según el juego?", "A distancia media", "3 no es 1 ni 5."),
            ex("Dani pisó los talones del guía. ¿Estaba demasiado cerca o demasiado lejos?", "Demasiado cerca", "A 1 paso no se pisan los talones; faltó espacio."),
        ],
        "challenge": [
            arith("Empiezas a 1 paso del guía. «Lejos» deja la distancia en 5 pasos (cambia en 4) y «cerca» la vuelve a 1 paso (cambia en 4). Se dice lejos, cerca, lejos. ¿Cuántos pasos cambió la distancia en total?", "4+4+4", "Cada señal obliga a dar 4 pasos.", " pasos"),
            ex("Hay 3 niños en fila y uno se pone delante del primero. ¿Cuántos hay detrás del que llegó?", "3", "Los 3 originales quedan detrás."),
        ],
    },
    context=[ex("En el pasillo del colegio la fila avanza y quieres alcanzar a tu amigo, que va 5 pasos delante. ¿Corres para pegarte o caminas hasta quedar a 1 o 2 pasos?", "Caminas hasta quedar a 1 o 2 pasos", "Así no empujas ni chocas.")],
    selfcheck=[
        ex("¿Qué significa «detrás»?", "El lado de la espalda", "Es lo contrario de delante."),
        ex("¿Cuántos pasos son «cerca» en el juego?", "1", "Está definido así."),
        ex("¿Cuántos pasos son «lejos» en el juego?", "5", "Está definido así."),
    ],
    open_task=task("Con un compañero o un adulto, juega «La sombra» durante 3 rondas de 40 segundos de acción y 40 de pausa. Reglas: el guía camina lento, la sombra va a 1 paso detrás; cuando el adulto diga «lejos», la sombra espera quieta hasta que el guía queda a 5 pasos; con «cerca», la sombra camina hasta quedar a 1 paso. Después cambia el rol. Anota cuántas veces cumpliste la distancia correcta.",
                   "En 3 rondas me dijeron 6 veces «lejos» o «cerca». Cumplí 5. Me quedé a 2 pasos una vez, pero lo corregí.",
                   ["mantiene 1 paso detrás del guía", "ajusta la distancia según la señal", "copia movimientos sin empujar"],
                   ["registro de aciertos", "observación de un adulto", "relato de los dos roles"],
                   ["pisarle los talones", "no cumplir los 5 pasos", "correr en lugar de caminar"],
                   "Elogia la distancia correcta y pide mejorar un detalle, como contar los pasos en voz baja."),
    reinforce="Camina 5 pasos hacia delante, da media vuelta y camina 5 pasos de regreso, contando en voz alta.",
    extend="Con un compañero, pongan una marca a 5 pasos y vean cuántos pasos de cada uno hacen falta.",
)

register(
    OA2, 4,
    materials="Un pañuelo o trozo de tela, un aplauso o un silbido suave que dé un adulto, una línea de tiza o cuerda de 3 m y un espacio libre de 4 × 4 m.",
    use="Aprenderé a distinguir antes, durante y después en una secuencia de movimientos. Sirve para seguir un juego con varias señales y para ordenar lo que hago.",
    prior=["Sé qué son primero y último.", "Sé seguir una señal."],
    explain=[
        "Antes, durante y después hablan del tiempo. «Antes» es lo que ocurre primero. «Durante» es lo que ocurre mientras algo pasa. «Después» es lo que ocurre cuando ya terminó. Por ejemplo: antes de la señal estás quieto, durante la señal te mueves y después te detienes.",
        "En el juego «Señal y acción» el adulto da una señal sonora o muestra un pañuelo. Antes de la señal, te quedas quieto con las rodillas un poco dobladas. Durante la señal (mientras suena o mientras el pañuelo está arriba), caminas. Después de la señal, te detienes y cuentas hasta tres. Una ronda puede durar 40 segundos de movimiento y 40 de pausa.",
        "Si hay varias señales seguidas, las ordenas con palabras: primero, luego, por último. Escuchar bien es importante: si empiezas antes de tiempo o sigues después del final, no cumples la secuencia. Muévete siempre sin empujar y a una distancia segura.",
    ],
    vocab=[("antes", "lo que ocurre primero"), ("durante", "lo que ocurre mientras algo sucede"), ("después", "lo que ocurre cuando termina"), ("secuencia", "acciones en orden"), ("señal", "sonido o gesto que me dice qué hacer")],
    worked=[
        W("Ordenar la secuencia", "En el juego, el pañuelo sube, se mantiene arriba unos segundos y baja. ¿Qué haces antes, durante y después?", ["Antes de que suba el pañuelo, estoy quieto.", "Mientras el pañuelo está arriba, camino por el cuadrado.", "Cuando el pañuelo baja, me detengo y cuento hasta tres."], "Antes: quieto. Durante: camino. Después: me detengo."),
        W("Contar el tiempo", "Una ronda dura 40 segundos de acción y 40 de pausa, y haces 3. ¿Cuántos segundos se mueve el cuerpo en total?", ["Cada ronda tiene 40 segundos de movimiento.", "40 + 40 + 40.", "El total es 120 segundos."], "120 segundos."),
    ],
    mistakes=[M("Empezar a caminar antes de la señal.", "Hay ganas de partir primero.", "Espera quieto y parte cuando suene o suba el pañuelo."),
              M("Seguir caminando después de que termina la señal.", "No se mira cuándo termina.", "Mira o escucha y detente apenas la señal acabe.")],
    tiers={
        "recovery": [
            ex("Si algo ocurre primero, ¿es antes o después?", "Antes", "Antes es lo que ocurre primero."),
            ex("Si estás caminando mientras el pañuelo está arriba, ¿es antes, durante o después?", "Durante", "Estás moviéndote mientras ocurre."),
            ex("Cuando el pañuelo baja, ¿te detienes antes o después de la señal?", "Después", "La señal ya terminó."),
        ],
        "understand": [
            ex("¿Qué haces antes de la señal en el juego?", "Quedarme quieto", "Es la regla de inicio."),
            ex("¿Qué es una secuencia?", "Acciones en orden", "Primero una, luego otra."),
            ex("Si sigues caminando cuando acabó la señal, ¿actuaste durante o después de ella?", "Después de ella", "Debías haberte detenido."),
        ],
        "apply": [
            ex("Pasos del adulto: 1) aplauso, 2) tres saltos, 3) detenerse. ¿Qué haces después de los tres saltos?", "Me detengo", "El paso 3 viene después."),
            ex("En una ronda ordenas: caminar, aplaudir, sentarte. ¿Qué haces antes de sentarte?", "Aplaudir", "El aplauso va justo antes de sentarte."),
            arith("Una ronda tiene 3 señales de 10 segundos cada una. ¿Cuántos segundos dura la ronda?", "3*10", "Se multiplican señales por segundos.", " segundos"),
        ],
        "reason": [
            ex("Caro partió antes de la señal. ¿Qué parte de la secuencia no respetó?", "El antes", "Debía estar quieta antes de la señal."),
            ex("Dani sigue saltando mientras todos se detuvieron porque terminó la señal. ¿Respetó el «después»?", "No", "Debía haberse detenido."),
        ],
        "challenge": [
            ex("El adulto dice: «antes de saltar, aplaude; durante el salto, di tu nombre en voz baja; después, quédate quieto». Escribe las tres acciones en orden.", "Aplaudir, saltar diciendo mi nombre, quedarme quieto", "Se ordenan según antes, durante y después."),
            arith("Haces 2 rondas con tres señales (aplauso, salto, quieto). Cada señal dura 10 segundos. ¿Cuántos segundos son en total?", "2*3*10", "Se multiplican rondas, señales y segundos.", " segundos"),
        ],
    },
    context=[ex("En la clase de música la profesora levanta el pañuelo y todos cantan. Cuando lo baja, se callan. ¿Cantan antes, durante o después de que el pañuelo está arriba?", "Durante", "Cantan mientras está arriba.")],
    selfcheck=[
        ex("¿Qué palabra usas para lo que ocurre mientras suena la señal?", "Durante", "Es lo que sucede en ese tiempo."),
        ex("¿Qué haces antes de la señal?", "Estoy quieto", "Esperas sin moverte."),
        ex("¿Qué haces después de la señal?", "Me detengo", "La señal terminó."),
    ],
    open_task=task("Con un adulto, juega «Señal y acción» 3 rondas. En cada ronda el adulto sube un pañuelo, lo mantiene arriba 10 segundos y lo baja. Tú te quedas quieto antes, caminas durante y te detienes después, contando hasta tres. Anota con una palomita las tres partes que hiciste bien en cada ronda.",
                   "Ronda 1: antes ✓, durante ✓, después ✓. Ronda 2: antes ✓, durante ✓, después ✗ (seguí caminando). Ronda 3: todo ✓.",
                   ["espera quieto antes de la señal", "se mueve solo durante la señal", "se detiene después de la señal"],
                   ["tabla con palomitas", "observación de un adulto", "dibujo de tres momentos"],
                   ["partir antes", "seguir después", "no mirar la señal"],
                   "Reconoce las rondas correctas y propone mirar el pañuelo para detenerte justo al bajar."),
    reinforce="Haz una ronda: quédate quieto, camina 10 segundos y detente, diciendo en voz baja antes, durante y después.",
    extend="Inventa una secuencia con 4 señales (por ejemplo, aplauso, salto, giro, quieto) y pídele a alguien que la haga.",
)

register(
    OA2, 5,
    materials="Una línea de 4 m marcada con tiza o cuerda, un cono al final, música con ritmo lento y rápido si la hay (o un adulto que aplauda lento y rápido) y reloj.",
    use="Aprenderé a moverme rápido o lento sin salirme del camino. Sirve para cambiar de velocidad en un juego sin perder el control.",
    prior=["Sé caminar sobre una línea.", "Sé qué es rápido y qué es lento."],
    explain=[
        "Rápido es hacer algo en poco tiempo; lento es tardar mucho. Puedes caminar rápido o caminar lento. Si un aplauso suena despacio, haces pasos lentos. Si suena rápido, haces pasos rápidos.",
        "La trayectoria es el camino que sigues. En esta clase, tu trayectoria es la línea del suelo. Si cambias de velocidad, tus pies deben seguir en la línea. Ir rápido no significa salirse del camino ni empujar.",
        "Para controlar el cambio de velocidad, escucha el ritmo y ajusta tus pasos poco a poco. Si el cambio es brusco, te puedes tambalear. Un paso lento dura 2 segundos y uno rápido dura 1 segundo. Cuenta en voz baja para medirlo.",
    ],
    vocab=[("rápido", "algo que tarda poco"), ("lento", "algo que tarda mucho"), ("ritmo", "la velocidad de los sonidos o pasos"), ("trayectoria", "el camino que sigo"), ("control", "ir donde quiero y detenerme cuando quiero")],
    worked=[
        W("Pasos lentos y rápidos", "Haces 6 pasos lentos de 2 segundos cada uno. ¿Cuánto tardas? Luego haces 6 pasos rápidos de 1 segundo. ¿Cuánto tardas?", ["Lentos: 6 × 2 = 12 segundos.", "Rápidos: 6 × 1 = 6 segundos.", "Comparo: 12 es más que 6."], "12 segundos lento y 6 segundos rápido."),
        W("Seguir la línea", "El aplauso empieza lento y luego rápido. ¿Qué haces con los pies?", ["Camino por la línea con pasos lentos.", "Al oír el aplauso rápido, acelero poco a poco.", "Mis pies siguen sobre la línea y miro al frente."], "Cambio de lento a rápido sin salirme de la línea."),
    ],
    mistakes=[M("Acelerar de golpe y salirse de la línea.", "Se piensa que rápido es lo mismo que sin cuidado.", "Aumenta la velocidad poco a poco y mira al frente."),
              M("Quedarse lento cuando el ritmo es rápido.", "No se escucha el cambio.", "Escucha el aplauso y cambia el paso.")],
    tiers={
        "recovery": [
            ex("Si tardas poco en llegar, ¿fuiste rápido o lento?", "Rápido", "Tardar poco es ser rápido."),
            ex("Si tardas mucho, ¿fuiste rápido o lento?", "Lento", "Tardar mucho es ser lento."),
            ex("Un aplauso despacio, ¿pide pasos lentos o rápidos?", "Lentos", "El ritmo despacio es lento."),
        ],
        "understand": [
            ex("¿Qué es la trayectoria?", "El camino que sigo", "Es la ruta de mi cuerpo."),
            ex("Si vas rápido, ¿puedes salirte del camino?", "No, debes seguir en la línea", "Control es mantener la trayectoria."),
            ex("¿Cómo se cambia de velocidad con control: de golpe o poco a poco?", "Poco a poco", "El cambio brusco hace perder el equilibrio."),
        ],
        "apply": [
            arith("Un paso lento dura 2 segundos. ¿Cuánto duran 5 pasos lentos?", "5*2", "Se multiplican pasos por segundos.", " segundos"),
            arith("Un paso rápido dura 1 segundo. ¿Cuánto duran 8 pasos rápidos?", "8*1", "Se multiplican pasos por segundos.", " segundos"),
            ex("El aplauso es lento, lento, rápido, rápido. ¿Cuántos pasos rápidos haces?", "2", "Dos veces suena rápido."),
        ],
        "reason": [
            ex("Beto fue más rápido que Ana, pero salió de la línea 3 veces. Ana fue más lenta y no salió. ¿Quién tuvo mejor control de la trayectoria?", "Ana", "Se mantuvo en el camino."),
            ex("La línea mide 4 m y la recorres lento en 12 s y rápido en 6 s. ¿Cuántos segundos menos tardas rápido?", "6", "12 menos 6 son 6 segundos."),
        ],
        "challenge": [
            arith("Recorres: 4 pasos lentos de 2 segundos y luego 4 pasos rápidos de 1 segundo. ¿Cuántos segundos tardas en total?", "4*2+4*1", "Se suman los tiempos de ambos tramos.", " segundos"),
            ex("El adulto dice: «lento, lento, rápido, lento». ¿Cuántas veces cambias de velocidad entre un paso y el siguiente?", "2", "Hay un cambio de lento a rápido y otro de rápido a lento."),
        ],
    },
    context=[ex("Al salir de clase, el pasillo está lleno y el piso mojado. ¿Cómo caminas: A) rápido y esquivando, B) lento y mirando el suelo, C) corriendo?", "B", "Con el piso mojado, la lentitud previene caídas.")],
    selfcheck=[
        ex("¿Cuántos segundos dura un paso lento?", "2", "Así se definió en la clase."),
        ex("¿Cuántos segundos dura un paso rápido?", "1", "Así se definió en la clase."),
        ex("¿Qué debes mantener al cambiar de velocidad?", "La trayectoria", "Los pies siguen en la línea."),
    ],
    open_task=task("Marca una línea de 4 m en el suelo. Con un adulto que aplauda lento y rápido, haz 3 recorridos de 50 segundos de acción y 50 de pausa. En cada recorrido camina lento, luego rápido y luego lento de nuevo, sin salirte de la línea. Anota cuántas veces te saliste.",
                   "En los 3 recorridos me salí 1 vez, cuando aceleré muy rápido. En los otros dos cambié de velocidad poco a poco y mantuve la línea.",
                   ["cambia de velocidad según el ritmo", "mantiene los pies en la línea", "avanza con control y mira al frente"],
                   ["registro de salidas de la línea", "observación de un adulto", "dibujo de la trayectoria"],
                   ["acelerar de golpe", "salirse de la línea", "no escuchar el ritmo"],
                   "Destaca los cambios con control y pide acelerar más gradualmente."),
    reinforce="Camina la línea 3 veces: una lenta, una normal y una rápida, sin salirte.",
    extend="Haz el recorrido con un compañero que va delante a su ritmo, y ajusta tu velocidad para mantener 2 pasos de distancia.",
)
