"""Cuaderno del estudiante, 3.º básico Ciencias Naturales: OA 12 (rotación y traslación de la Tierra) y OA 13 (modelos de fases de la Luna y eclipses)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA12, OA13 = "CN03 OA 12", "CN03 OA 13"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- OA 12
register(
    OA12, 1,
    materials="Una pelota o una naranja grande como modelo de la Tierra, un lápiz largo o palito para el eje (una persona adulta lo atraviesa por la naranja o lo pega a la pelota), plasticina y un papelito. Sin objetos puntiagudos sueltos.",
    use="Aprenderé que la Tierra gira sobre su eje y a mostrarlo con un modelo. Sirve para entender por qué existe el día y la noche.",
    prior=["Sé que la Tierra es un planeta que gira alrededor del Sol.", "Sé que un modelo representa algo real."],
    explain=[
        "La Tierra gira sobre sí misma, como un trompo. Este movimiento se llama rotación. Gira alrededor de una línea imaginaria que pasa por el Polo Norte y el Polo Sur, llamada eje.",
        "La Tierra da una vuelta completa sobre su eje en un día, es decir, en unas 24 horas. Gira de oeste a este. No lo sentimos porque nos movemos junto con ella, igual que no sentimos el movimiento de un tren muy suave cuando vamos adentro.",
        "Puedo hacer un modelo con una pelota y un lápiz como eje. Pego un papelito donde está Chile. Si giro la pelota lentamente sobre su eje, el papelito va pasando por todos los lados de la pelota. Un modelo me ayuda a entender, pero no es igual que la Tierra real: la pelota es muy pequeña comparada con ella.",
    ],
    vocab=[("rotación", "movimiento de la Tierra al girar sobre su eje"), ("eje", "línea imaginaria alrededor de la cual gira la Tierra"), ("polo", "cada extremo del eje de la Tierra: Polo Norte y Polo Sur"), ("modelo", "representación que ayuda a explicar algo"), ("vuelta completa", "giro que vuelve al mismo punto de partida")],
    worked=[
        {"title": "Hacer girar el modelo", "problem": "Giras una pelota sobre un lápiz que la atraviesa y el papelito marca Chile. ¿Qué movimiento de la Tierra muestras?", "steps": ["La pelota gira sobre su eje.", "Eso es la rotación.", "Una vuelta completa representa un día."], "answer": "La rotación; una vuelta es un día"},
        {"title": "Dónde está el eje", "problem": "¿Por qué lugares pasa el eje de la Tierra?", "steps": ["El eje es una línea imaginaria.", "Atraviesa la Tierra de un polo a otro."], "answer": "Por el Polo Norte y el Polo Sur"},
    ],
    mistakes=[
        {"wrong": "Confundir rotación con dar una vuelta alrededor del Sol.", "why": "Ambas son giros de la Tierra.", "fix": "Rotación es girar sobre el eje en un día; la traslación es dar una vuelta alrededor del Sol."},
        {"wrong": "Pensar que sentimos girar a la Tierra.", "why": "Se piensa que un giro tan rápido se nota.", "fix": "No lo sentimos porque nos movemos con la Tierra, a velocidad constante."},
    ],
    tiers={
        "recovery": [
            ex("¿Cómo se llama el movimiento de la Tierra al girar sobre su eje?", "Rotación", "Rotación es girar sobre el propio eje."),
            ex("¿Cuánto tarda la Tierra en dar una vuelta sobre su eje: un día o un año?", "Un día", "Una rotación dura unas 24 horas."),
            ex("Completa: el eje de la Tierra pasa por el Polo Norte y el Polo ___.", "Sur", "Va de un polo al otro."),
        ],
        "understand": [
            ex("¿Qué es el eje de la Tierra?", "Una línea imaginaria alrededor de la cual gira", "Atraviesa de polo a polo."),
            ex("¿Por qué no sentimos que la Tierra gira?", "Porque nos movemos junto con ella", "Todo gira con la misma velocidad."),
            ex("¿Qué representa en el modelo una vuelta completa de la pelota?", "Un día", "La Tierra tarda un día en una rotación."),
        ],
        "apply": [
            arith("En tu modelo, cada vuelta de la pelota es un día. Giras 5 vueltas el lunes y 4 vueltas el martes. ¿Cuántos días representan en total?", "5+4", "Se suman las vueltas: cada una es un día.", " días"),
            arith("La Tierra rota una vez cada 24 horas. ¿Cuántas horas pasan en 2 rotaciones?", "24+24", "Se suman dos veces las 24 horas.", " horas"),
            ex("En tu modelo, ¿dónde debe ir el lápiz que hace de eje: de polo a polo o de lado a lado en el ecuador?", "De polo a polo", "El eje pasa por el Polo Norte y el Polo Sur."),
        ],
        "reason": [
            ex("Un compañero dice: «El eje de la Tierra es un palo grande que se ve desde el espacio». ¿Es cierto?", "No", "El eje es una línea imaginaria."),
            ex("Una pelota con un papelito de Chile gira una vuelta completa y el papelito vuelve al mismo lugar de la pieza. ¿Qué tiempo de la Tierra representa?", "Un día", "Es una rotación completa."),
        ],
        "challenge": [
            arith("Una rotación dura 24 horas. Si desde la medianoche han pasado 12 horas, ¿cuántas horas faltan para completar la rotación?", "24-12", "Se resta lo que ya pasó a las 24 horas.", " horas"),
            ex("¿Cuál es un límite de tu modelo de pelota y lápiz: que la pelota es mucho más pequeña que la Tierra o que la pelota gira?", "Que la pelota es mucho más pequeña que la Tierra", "Un modelo simplifica lo real; girar sí lo muestra bien."),
        ],
    },
    context=[ex("Mariana dice: «El mundo no se mueve porque yo no siento nada». Con lo que sabes, ¿cómo le explicas que la Tierra sí rota?", "Que no lo sentimos porque nos movemos con la Tierra a velocidad constante", "El movimiento uniforme no se siente.")],
    selfcheck=[
        ex("¿Qué se llama rotación?", "El giro de la Tierra sobre su eje", "Rotar es girar sobre sí mismo."),
        ex("¿Cuántas horas dura una rotación aproximadamente?", "24 horas", "Eso es un día."),
        ex("¿Qué es el eje?", "Una línea imaginaria de polo a polo", "Es lo que atraviesa la Tierra."),
    ],
    open_task=task(
        "Si puedes, haz el modelo: una pelota o una naranja con un lápiz como eje y un papelito que marque Chile. Gira lentamente una vuelta y cuenta con una persona de tu casa qué lados pasa el papelito. Si no puedes, usa este dibujo en palabras: una esfera con una línea de arriba a abajo y una flecha curva alrededor. Dibuja el modelo, rotula eje, polos y Chile, y escribe cuánto tiempo representa una vuelta completa.",
        "Dibujé una esfera con una línea de polo a polo. Rotulé eje, Polo Norte y Polo Sur, y Chile. Una vuelta completa representa un día.",
        ["dibuja el eje de polo a polo", "rotula Chile y los polos", "dice que una vuelta es un día"],
        ["dibujo rotulado", "frase sobre el tiempo de una vuelta"],
        ["poner el eje de lado a lado", "decir que una vuelta es un año"],
        "Valora el dibujo y pregunta qué lado del modelo mira al Sol al mediodía de Chile.",
    ),
    reinforce="Haz girar un trompo o una tapa de olla de plástico y compara con la rotación de la Tierra: ¿qué es el eje?",
    extend="Dibuja un trompo girando y marca con una línea su eje, como el eje de la Tierra.",
)

register(
    OA12, 2,
    materials="Una linterna fija sobre una mesa o apoyada en libros, la pelota con eje de la clase anterior, el papelito de Chile y una pieza oscura. No mires al haz de la linterna ni la apuntes a los ojos.",
    use="Aprenderé a explicar el día y la noche con la rotación. Sirve para entender por qué el Sol sale y se pone.",
    prior=["Sé que la Tierra rota sobre su eje en un día.", "Sé que la luz viaja en línea recta."],
    explain=[
        "El Sol siempre ilumina la mitad de la Tierra, la que mira hacia él. En esa mitad es de día. En la otra mitad, que no recibe luz, es de noche. Como la Tierra rota, cada lugar pasa de la parte iluminada a la oscura y otra vez a la iluminada.",
        "Al amanecer, mi lugar entra en la parte iluminada. Al atardecer, sale de ella. Parece que el Sol se mueve por el cielo, de este a oeste, pero en realidad es la Tierra la que gira. El Sol sale por el este y se pone por el oeste.",
        "Puedo comprobarlo con el modelo: la linterna es el Sol y la pelota es la Tierra. Giro la pelota lentamente y miro el papelito de Chile. Cuando está en la zona iluminada, es de día en Chile. Cuando queda en la sombra, es de noche. Al mismo tiempo, en el lado opuesto del mundo es lo contrario: por ejemplo, cuando es mediodía en Chile, en Japón es de noche.",
    ],
    vocab=[("día", "período con luz del Sol en un lugar"), ("noche", "período sin luz del Sol en un lugar"), ("amanecer", "momento en que el Sol aparece en el horizonte"), ("atardecer", "momento en que el Sol se oculta en el horizonte"), ("este y oeste", "direcciones por donde sale y se pone el Sol")],
    worked=[
        {"title": "Modelo con linterna", "problem": "La linterna ilumina la pelota. El papelito de Chile está en la parte iluminada. ¿Qué hora del día representa?", "steps": ["La parte iluminada tiene día.", "El papelito está allí.", "En Chile es de día."], "answer": "Es de día en Chile"},
        {"title": "Lado opuesto", "problem": "En Chile es de día. ¿Qué pasa en el lugar del lado opuesto del mundo?", "steps": ["El Sol ilumina solo la mitad.", "El lado opuesto queda en la oscuridad."], "answer": "Es de noche"},
    ],
    mistakes=[
        {"wrong": "Decir que el Sol da la vuelta alrededor de la Tierra cada día.", "why": "Eso es lo que parece desde el suelo.", "fix": "El Sol no gira alrededor de la Tierra: la rotación de la Tierra hace que lo veamos moverse."},
        {"wrong": "Pensar que de noche el Sol se apaga.", "why": "No se ve, así que parece que no existe.", "fix": "El Sol sigue emitiendo luz; mi lugar quedó en la parte de la Tierra que no lo mira."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué parte de la Tierra tiene día: la que mira al Sol o la que no lo mira?", "La que mira al Sol", "Recibe su luz."),
            ex("¿Por qué lado del cielo sale el Sol?", "Por el este", "Sale por el este y se pone por el oeste."),
            ex("Completa: de noche, mi lugar está en la parte que no ___ el Sol.", "mira", "Está en la zona sin luz."),
        ],
        "understand": [
            ex("¿Cómo explica la rotación el día y la noche?", "Cada lugar entra y sale de la parte iluminada al girar la Tierra", "El giro lleva cada lugar de la luz a la sombra."),
            ex("¿Por qué parece que el Sol se mueve por el cielo?", "Porque la Tierra gira", "Es un movimiento aparente."),
            ex("¿Qué representa la linterna en el modelo?", "El Sol", "Es la fuente de luz."),
        ],
        "apply": [
            ex("En el modelo, el papelito de Chile entra a la zona iluminada. ¿Qué momento del día representa: amanecer o atardecer?", "Amanecer", "Entrar a la luz es salir de la noche."),
            ex("En el modelo, el papelito está en la sombra. ¿Es de día o de noche en Chile?", "De noche", "La sombra representa la noche."),
            ex("Es mediodía en Chile. ¿Es de día o de noche en Japón, casi al otro lado del mundo?", "De noche", "El lado opuesto del mundo está sin luz."),
        ],
        "reason": [
            ex("Un niño dice que de noche el Sol deja de existir. ¿Qué evidencia del modelo lo contradice?", "La linterna sigue encendida y solo el papelito quedó en la sombra", "El Sol sigue alumbrando otra parte."),
            ex("Dos amigos viven en lados opuestos del mundo. ¿Pueden tener ambos día al mismo tiempo?", "No", "El Sol solo ilumina la mitad de la Tierra."),
        ],
        "challenge": [
            ex("Si la Tierra no girara y Chile quedara siempre mirando al Sol, ¿cómo sería en Chile?", "Siempre sería de día", "No cambiaría de la luz a la sombra."),
            ex("La Tierra gira de oeste a este. ¿Hacia qué lado del cielo se ve moverse el Sol durante el día: de este a oeste o de oeste a este?", "De este a oeste", "Al girar la Tierra hacia el este, parece que el Sol se mueve al revés."),
        ],
    },
    context=[ex("Carlos habla por videollamada con su prima en Japón. Para él es de mañana, pero ella dice que es de noche. ¿Qué explica esa diferencia?", "Que la Tierra rota y solo la mitad tiene luz del Sol", "En lados opuestos del mundo, uno tiene día y otro noche.")],
    selfcheck=[
        ex("¿Qué produce el día y la noche?", "La rotación de la Tierra", "El giro cambia qué zona mira al Sol."),
        ex("¿Por dónde sale el Sol?", "Por el este", "La Tierra gira hacia el este."),
        ex("¿Cuándo es de noche en un lugar?", "Cuando queda en la zona sin luz del Sol", "Esa zona no recibe la luz."),
    ],
    open_task=task(
        "Si puedes, usa la linterna y la pelota con el papelito de Chile en una pieza oscura. Gira lentamente la pelota y anota tres posiciones: cuando es de día, cuando amanece y cuando es de noche. Si no puedes, dibuja una pelota con una flecha curva y la luz del Sol llegando desde la izquierda; marca dónde es de día y dónde es de noche y pon a Chile en tres posiciones. Escribe una frase que explique el día y la noche.",
        "Dibujé la luz desde la izquierda. La mitad izquierda es día y la derecha es noche. Chile pasa por la luz y por la sombra al girar. Frase: el día y la noche ocurren porque la Tierra gira.",
        ["dibuja la luz iluminando una mitad", "marca tres posiciones de Chile", "explica con la rotación"],
        ["dibujos de tres posiciones", "frase de explicación"],
        ["decir que el Sol se mueve alrededor de la Tierra", "iluminar toda la pelota"],
        "Valora los dibujos y pregunta qué pasa con la persona que vive en el otro lado del mundo.",
    ),
    reinforce="Con la linterna y la pelota, muestra a alguien de tu casa cómo se produce el día y la noche y pídele que diga cuándo amanece.",
    extend="Anota a qué hora sale y se pone el Sol hoy en tu casa o pregunta a alguien de tu casa.",
)

register(
    OA12, 3,
    materials="Una lámpara o linterna que sirva de Sol puesta en el centro de una pieza, una pelota para la Tierra y una persona de tu casa que ayude. Camina lento, sin correr ni caminar hacia atrás. No mires al haz.",
    use="Aprenderé que la Tierra se traslada alrededor del Sol y cómo se forma el año. Sirve para entender qué son un año y las estaciones.",
    prior=["Sé que la Tierra rota en un día.", "Sé que una órbita es el camino de un cuerpo alrededor de otro."],
    explain=[
        "La Tierra también se mueve alrededor del Sol. Este movimiento se llama traslación. El camino que sigue es su órbita, que es casi un círculo. Una vuelta completa dura unos 365 días, y eso es un año.",
        "Mientras da la vuelta, la Tierra sigue rotando. Su eje está inclinado. Por la inclinación, durante el año llega más luz del Sol a una parte de la Tierra y menos a otra. En Chile eso produce las estaciones: verano, otoño, invierno y primavera. El verano comienza hacia el 21 de diciembre, y el invierno hacia el 21 de junio. Chile está en el hemisferio sur, es decir, en la mitad sur del mundo; en el hemisferio norte, como en Alemania, las estaciones son al revés.",
        "Para hacer el modelo, una persona ayudante sostiene la lámpara al centro. Yo camino lentamente alrededor con la pelota. Una vuelta completa de la pelota alrededor de la lámpara representa un año. Las estaciones no ocurren porque la Tierra esté más cerca o más lejos del Sol, sino por la inclinación del eje.",
    ],
    vocab=[("traslación", "movimiento de la Tierra alrededor del Sol"), ("órbita", "camino que sigue la Tierra alrededor del Sol"), ("año", "tiempo que tarda la Tierra en dar una vuelta al Sol"), ("estación", "cada una de las cuatro partes del año: verano, otoño, invierno y primavera"), ("inclinado", "que no está recto, sino ladeado")],
    worked=[
        {"title": "Una vuelta al Sol", "problem": "En el modelo, caminas una vuelta completa alrededor de la lámpara. ¿Cuánto tiempo real representa?", "steps": ["Una vuelta completa alrededor del Sol es la traslación.", "Dura 365 días.", "Eso es un año."], "answer": "Un año"},
        {"title": "Dos movimientos a la vez", "problem": "Mientras camina alrededor de la lámpara, ¿la pelota puede girar sobre su eje?", "steps": ["La Tierra rota y se traslada a la vez.", "Puedo girar la pelota mientras camino."], "answer": "Sí, rotación y traslación ocurren juntas"},
    ],
    mistakes=[
        {"wrong": "Decir que las estaciones ocurren porque la Tierra se acerca y se aleja del Sol.", "why": "Parece lógico que más cerca sea más calor.", "fix": "Las estaciones se deben a la inclinación del eje y a la posición de la Tierra en su órbita."},
        {"wrong": "Confundir rotación con traslación.", "why": "Ambas son giros.", "fix": "Rotación: sobre su eje, un día. Traslación: alrededor del Sol, un año."},
    ],
    tiers={
        "recovery": [
            ex("¿Cómo se llama el movimiento de la Tierra alrededor del Sol?", "Traslación", "Traslación es dar la vuelta al Sol."),
            ex("¿Cuánto dura una traslación: un día o un año?", "Un año", "Son unos 365 días."),
            ex("Completa: el camino de la Tierra alrededor del Sol se llama ___.", "órbita", "Es el camino alrededor del Sol."),
        ],
        "understand": [
            ex("¿Qué diferencia hay entre rotación y traslación?", "Rotación es girar sobre su eje y traslación es girar alrededor del Sol", "Se distinguen por el centro del giro."),
            ex("¿A qué se debe que existan las estaciones?", "A la inclinación del eje de la Tierra y su movimiento alrededor del Sol", "La inclinación cambia cuánta luz llega."),
            ex("¿Qué representa en el modelo caminar una vuelta completa alrededor de la lámpara?", "Un año", "Es una traslación completa."),
        ],
        "apply": [
            arith("Un año tiene 365 días. ¿Cuántos días hay en 2 años sin contar años bisiestos?", "365+365", "Se suman los días de los dos años.", " días"),
            ex("Es 21 de diciembre en Chile. ¿Qué estación comienza hacia esa fecha?", "El verano", "El verano comienza hacia el 21 de diciembre."),
            ex("Es julio en Chile. ¿Qué estación es?", "Invierno", "El invierno va desde fines de junio hasta fines de septiembre."),
        ],
        "reason": [
            ex("Un compañero dice que es verano porque la Tierra está más cerca del Sol. ¿Qué respuesta le das?", "No, las estaciones se deben a la inclinación del eje", "La distancia no es la causa."),
            ex("En diciembre es verano en Chile. ¿Puede ser invierno en Alemania al mismo tiempo?", "Sí", "Los hemisferios norte y sur tienen estaciones opuestas."),
        ],
        "challenge": [
            ex("En el modelo, una persona camina 3 vueltas alrededor de la lámpara. ¿Cuántos años representa?", "3 años", "Cada vuelta es un año."),
            ex("¿La Tierra primero termina de rotar y después se traslada, o hace los dos movimientos al mismo tiempo?", "Los hace al mismo tiempo", "Gira sobre su eje mientras da la vuelta alrededor del Sol."),
        ],
    },
    context=[ex("Sofía cumple años cada 15 de marzo. Cada cumpleaños, la Tierra ha dado una vuelta completa al Sol. Si hoy cumple 8 años, ¿cuántas traslaciones completas ha hecho la Tierra desde que nació?", "8", "Cada año es una traslación completa.")],
    selfcheck=[
        ex("¿Qué es la traslación?", "El movimiento de la Tierra alrededor del Sol", "Es la vuelta al Sol."),
        ex("¿Cuánto dura una traslación?", "Un año", "Son unos 365 días."),
        ex("¿Qué causa las estaciones?", "La inclinación del eje", "Cambia cuánta luz llega en cada parte del año."),
    ],
    open_task=task(
        "Si puedes, haz el modelo con una lámpara o linterna al centro y una pelota que camina a su alrededor, y marca con papelitos cuatro posiciones: verano, otoño, invierno y primavera. Si no puedes, dibuja el Sol al centro, la órbita como círculo y la Tierra en cuatro puntos. Rotula cada estación en el orden verano, otoño, invierno, primavera y escribe cuánto tiempo representa la vuelta completa.",
        "Dibujé el Sol al centro y la Tierra en cuatro puntos de su órbita: verano, otoño, invierno y primavera. La vuelta completa representa un año.",
        ["dibuja la órbita alrededor del Sol", "ubica cuatro posiciones con las estaciones en orden", "dice que la vuelta es un año"],
        ["dibujo de la órbita", "frase del tiempo"],
        ["dibujar la órbita alrededor de la Tierra", "decir que las estaciones se deben a la distancia"],
        "Valora el orden de las estaciones y pregunta cómo se llama este movimiento.",
    ),
    reinforce="Camina lentamente alrededor de una lámpara apagada con una pelota y di en voz alta «un año» al terminar la vuelta.",
    extend="Averigua en qué meses comienza cada estación en Chile y anótalo.",
)

register(
    OA12, 4,
    materials="Papel y lápiz. Las situaciones están escritas. No es necesario salir de casa ni usar materiales especiales.",
    use="Aprenderé a distinguir qué efectos produce cada movimiento de la Tierra y cuánto dura cada uno. Sirve para no mezclar días, años y estaciones.",
    prior=["Sé qué es la rotación y qué es la traslación.", "Sé que la rotación produce el día y la noche."],
    explain=[
        "Cada movimiento de la Tierra tiene sus efectos y su propio tiempo. La rotación dura un día, unas 24 horas, y produce el día y la noche. La traslación dura un año, unos 365 días, y junto con la inclinación del eje produce las estaciones.",
        "Para no confundirlos, uso una tabla. Rotación: sobre su eje, dura 1 día, efecto: día y noche. Traslación: alrededor del Sol, dura 1 año, efecto: estaciones del año. También hay un movimiento de la Luna: da una vuelta alrededor de la Tierra en alrededor de un mes.",
        "Casi siempre cada cuatro años, un año tiene 366 días en vez de 365, para ajustar el calendario; se llama año bisiesto. Una escala temporal es cuánto dura un fenómeno. El día y la noche cambian cada pocas horas. Las estaciones cambian cada tres meses. Las estaciones no dependen de la rotación: en un solo día no cambia la estación.",
    ],
    vocab=[("efecto", "lo que ocurre como resultado de algo"), ("escala temporal", "cuánto tiempo dura algo"), ("año bisiesto", "año de 366 días que ocurre cada cuatro años"), ("calendario", "forma de organizar los días del año"), ("fenómeno", "algo que ocurre en la naturaleza")],
    worked=[
        {"title": "Efectos y tiempos", "problem": "¿Cuánto dura la rotación y qué efecto produce?", "steps": ["La rotación es el giro sobre el eje.", "Dura un día.", "Produce el día y la noche."], "answer": "Dura un día y produce el día y la noche"},
        {"title": "Cálculo de días", "problem": "¿Cuántas horas hay en 3 días?", "steps": ["Un día tiene 24 horas.", "24 + 24 + 24 = 72."], "answer": "72 horas"},
    ],
    mistakes=[
        {"wrong": "Decir que la rotación produce las estaciones.", "why": "Se confunden las dos escalas de tiempo.", "fix": "La rotación produce el día y la noche; las estaciones se deben a la traslación y a la inclinación del eje."},
        {"wrong": "Pensar que cambia de estación cada día.", "why": "Se confunde el tiempo de un día con el de un año.", "fix": "Una estación dura unos tres meses."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué movimiento produce el día y la noche?", "La rotación", "Cada vuelta sobre el eje es un día."),
            ex("¿Qué movimiento dura un año?", "La traslación", "Es una vuelta alrededor del Sol."),
            ex("Completa: la rotación dura un ___.", "día", "Una vuelta sobre el eje es un día."),
        ],
        "understand": [
            ex("¿Cuál es el efecto de la traslación junto con la inclinación del eje?", "Las estaciones del año", "Cambia cuánta luz recibe cada parte durante el año."),
            ex("¿Cuánto dura un año bisiesto?", "366 días", "Tiene un día extra."),
            ex("¿Por qué las estaciones no se deben a la rotación?", "Porque la rotación dura un día y una estación dura unos tres meses", "Son escalas de tiempo muy distintas."),
        ],
        "apply": [
            arith("¿Cuántas horas hay en 3 días?", "24+24+24", "Cada día tiene 24 horas; se suman tres veces.", " horas"),
            arith("¿Cuántos días hay en 2 años de 365 días?", "365+365", "Se suman los días de los dos años.", " días"),
            ex("Clasifica el efecto: el día y la noche, ¿lo produce la rotación o la traslación?", "La rotación", "Se repite cada día."),
        ],
        "reason": [
            ex("Nicolás dice que si la Tierra rota más rápido, cambia la estación. ¿Está en lo correcto?", "No", "La estación depende de la traslación y de la inclinación."),
            ex("En una semana, ¿cuántas veces rota la Tierra sobre su eje?", "7 veces", "Una rotación por día, 7 días."),
        ],
        "challenge": [
            ex("Si la Tierra no se trasladara pero sí rotara, ¿habría día y noche?", "Sí", "La rotación sola produce día y noche."),
            ex("Si la Tierra se trasladara alrededor del Sol pero no rotara, ¿seguiría completando una vuelta al Sol en un año?", "Sí", "La traslación es independiente de la rotación."),
        ],
    },
    context=[ex("Mariana escribió en una tabla: «Rotación: dura un año; Traslación: dura un día». ¿Qué corrección debe hacer?", "Intercambiar: rotación dura un día y traslación dura un año", "Se invirtieron las duraciones.")],
    selfcheck=[
        ex("¿Cuánto dura la rotación?", "Un día", "Eso son unas 24 horas."),
        ex("¿Qué efecto tiene la traslación?", "Las estaciones del año", "Junto con el eje inclinado."),
        ex("¿Cuántos días tiene un año común?", "365", "Es la duración aproximada de una vuelta al Sol."),
    ],
    open_task=task(
        "Completa una tabla de dos filas, rotación y traslación, con tres columnas: ¿alrededor de qué gira?, ¿cuánto tarda? y ¿qué efecto produce? Después escribe una frase que explique por qué no cambia la estación en un solo día.",
        "Rotación: gira sobre su eje, tarda un día, produce día y noche. Traslación: gira alrededor del Sol, tarda un año, produce las estaciones. Una estación dura unos tres meses, por eso no cambia en un día.",
        ["completa las seis casillas correctamente", "distingue día y año", "explica con las escalas de tiempo"],
        ["tabla completa", "frase de explicación"],
        ["intercambiar día y año", "decir que la rotación produce estaciones"],
        "Valora la tabla y pide que dé un ejemplo de algo que dure un día y algo que dure un año.",
    ),
    reinforce="Escribe en un papel cuántas horas tiene un día y cuántos días tiene un año, y pega el papel donde lo veas.",
    extend="Averigua con una persona de tu casa por qué existe el año bisiesto.",
)

# ---------------------------------------------------------------- OA 13
register(
    OA13, 1,
    materials="Papel y lápices. Si hay Luna visible, observarla a simple vista (nunca con binoculares apuntados al Sol) desde la ventana. Si no, usa los dibujos descritos en esta clase. Esta clase se hace de noche con compañía de una persona adulta.",
    use="Aprenderé que las fases de la Luna son cómo se ve la Luna desde la Tierra en distintos días. Sirve para entender por qué la Luna cambia de forma.",
    prior=["Sé que la Luna no emite luz propia.", "Sé que la Luna gira alrededor de la Tierra."],
    explain=[
        "La Luna no tiene luz propia. Brilla porque refleja la luz del Sol. Siempre hay una mitad de la Luna iluminada por el Sol. Pero desde la Tierra no vemos siempre esa mitad completa, y por eso la Luna parece cambiar de forma.",
        "Las fases de la Luna son las distintas apariencias que vemos durante un ciclo de unos 29 días y medio, alrededor de un mes. Las cuatro fases principales son: Luna nueva, cuando casi no la vemos; cuarto creciente, cuando vemos la mitad iluminada y cada noche más; Luna llena, cuando vemos todo el disco iluminado; y cuarto menguante, cuando vemos la mitad iluminada y cada noche menos.",
        "La Luna es siempre la misma esfera. Lo que cambia es la parte iluminada que vemos. Observar y dibujar la Luna unas noches seguidas ayuda a ver ese ciclo. No hay que mirar el Sol ni hacer observaciones sin compañía de una persona adulta de noche.",
    ],
    vocab=[("fase", "cada aspecto que muestra la Luna durante el ciclo"), ("ciclo", "serie de cambios que se repiten"), ("Luna nueva", "fase en que casi no vemos la Luna"), ("Luna llena", "fase en que vemos todo el disco iluminado"), ("creciente y menguante", "cuando la parte iluminada que vemos aumenta o disminuye")],
    worked=[
        {"title": "Ordenar cuatro dibujos", "problem": "Hay cuatro dibujos: A casi no se ve, B mitad iluminada y aumentando, C toda iluminada, D mitad iluminada y disminuyendo. Ordénalos como un ciclo.", "steps": ["A es Luna nueva.", "B es cuarto creciente.", "C es Luna llena.", "D es cuarto menguante."], "answer": "A, B, C, D: Luna nueva, cuarto creciente, Luna llena, cuarto menguante"},
        {"title": "La misma esfera", "problem": "¿La Luna cambia de tamaño o forma durante el mes?", "steps": ["Siempre es una esfera.", "Siempre la mitad está iluminada.", "Cambia la parte iluminada que vemos."], "answer": "No cambia; cambia la parte iluminada que vemos"},
    ],
    mistakes=[
        {"wrong": "Pensar que la Luna cambia de forma de verdad.", "why": "Se ve distinta cada noche.", "fix": "La Luna es siempre una esfera; cambia lo que vemos de su parte iluminada."},
        {"wrong": "Decir que las fases se deben a la sombra de la Tierra.", "why": "Se confunde con los eclipses.", "fix": "Las fases se deben a cuánta parte iluminada vemos; los eclipses sí necesitan una sombra."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué fase es cuando vemos todo el disco de la Luna iluminado?", "Luna llena", "Se ve toda la cara iluminada."),
            ex("¿Qué fase es cuando casi no vemos la Luna?", "Luna nueva", "La parte que vemos no está iluminada."),
            ex("Completa: la Luna brilla porque refleja la luz del ___.", "Sol", "No tiene luz propia."),
        ],
        "understand": [
            ex("¿Por qué la Luna parece cambiar de forma?", "Porque vemos distintas partes de su mitad iluminada", "Siempre hay una mitad iluminada."),
            ex("¿Cuánto dura aproximadamente el ciclo de las fases?", "Un mes, unos 29 días y medio", "Es el tiempo para volver a la misma fase."),
            ex("¿Qué es una fase de la Luna?", "Cada apariencia que muestra la Luna durante el ciclo", "Es cómo se ve desde la Tierra."),
        ],
        "apply": [
            ex("Ordena las fases principales empezando por la Luna nueva: Luna llena, cuarto menguante, cuarto creciente.", "Luna nueva, cuarto creciente, Luna llena, cuarto menguante", "Es el orden del ciclo."),
            arith("Cada cuarto del ciclo dura aproximadamente 7 días. ¿Cuántos días suman 4 cuartos?", "4*7", "Cuatro cuartos suman 28 días, un poco menos que los 29 días y medio del ciclo, porque cada cuarto dura algo más de 7 días.", " días"),
            ex("Hoy hay Luna llena. ¿Unos 7 días después, qué fase se verá: cuarto creciente o cuarto menguante?", "Cuarto menguante", "Después de la llena la parte iluminada que vemos disminuye."),
        ],
        "reason": [
            ex("Un compañero dice que la Luna llena es la Luna entera y la Luna nueva es una Luna chica. ¿Qué le respondes?", "La Luna es siempre del mismo tamaño; solo cambia lo que vemos iluminado", "Es una apariencia."),
            ex("Una niña dice que la Luna se esconde detrás de la Tierra en Luna nueva. ¿Qué dato de esta clase lo corrige?", "La Luna sigue donde está, solo no vemos su parte iluminada", "No se esconde; la parte iluminada mira hacia el otro lado."),
        ],
        "challenge": [
            ex("Si dibujas la Luna cada noche durante dos semanas, ¿verás que cambia de forma de forma ordenada o desordenada?", "Ordenada", "El ciclo se repite siempre en el mismo orden."),
            ex("Si alumbras una pelota con una linterna, ¿qué parte queda iluminada: la que mira a la linterna o la de atrás?", "La que mira a la linterna", "El Sol ilumina siempre la mitad de la Luna que lo mira."),
        ],
    },
    context=[ex("Valeria dibuja la Luna cada tres o cuatro noches: primero casi nada, después una mitad, luego toda y luego otra mitad. ¿Qué ciclo está registrando?", "Las fases de la Luna", "Cambia lo que se ve de la parte iluminada.")],
    selfcheck=[
        ex("¿La Luna tiene luz propia?", "No", "Refleja la luz del Sol."),
        ex("¿Qué fase muestra todo el disco iluminado?", "Luna llena", "Se ve toda la cara iluminada."),
        ex("¿Cada cuánto se repite el ciclo de las fases?", "Cada mes, aproximadamente", "Unos 29 días y medio."),
    ],
    open_task=task(
        "Dibuja las cuatro fases principales en orden: Luna nueva, cuarto creciente, Luna llena y cuarto menguante. Pinta de amarillo la parte iluminada que se vería en cada una. Si puedes, observa la Luna esta noche con una persona adulta y dibuja lo que ves. Escribe una frase que explique por qué cambia.",
        "Dibujé un círculo oscuro, uno con la mitad amarilla, uno todo amarillo y otro con la mitad amarilla. La Luna siempre es una esfera; cambia lo que vemos iluminado.",
        ["dibuja cuatro fases en orden", "pinta la parte iluminada en cada una", "explica con la parte iluminada"],
        ["cuatro dibujos", "frase de explicación"],
        ["decir que la Luna cambia de forma real", "dibujar la luna llena con una sombra"],
        "Valora el orden y pregunta qué fase vendría después de la llena.",
    ),
    reinforce="Con una pelota y una linterna en una pieza oscura, mira cómo la linterna siempre ilumina una mitad de la pelota.",
    extend="Anota en un calendario las noches en que veas la Luna y dibuja su forma.",
)

register(
    OA13, 2,
    materials="Una linterna o lámpara fija en una mesa, una pelota pequeña o bola de plasticina de 3 a 4 cm como Luna, una pieza oscura y tú mismo como Tierra. No apuntes la luz a los ojos.",
    use="Aprenderé a modelar las posiciones del Sol, la Tierra y la Luna y relacionarlas con las fases. Sirve para explicar por qué se ven las fases.",
    prior=["Sé que la Luna refleja la luz del Sol.", "Sé que la Luna gira alrededor de la Tierra."],
    explain=[
        "La Luna da una vuelta alrededor de la Tierra en unos 27 días. Mientras tanto, la Tierra y la Luna avanzan alrededor del Sol, y por eso las fases se repiten cada unos 29 días y medio. En cada posición, el Sol ilumina la mitad de la Luna que lo mira, pero desde la Tierra vemos un trozo distinto de esa mitad.",
        "Si la Luna está entre el Sol y la Tierra, su mitad iluminada mira hacia el Sol y lejos de nosotros: es Luna nueva. Si la Tierra está entre el Sol y la Luna, vemos toda la mitad iluminada: es Luna llena. Cuando la Luna está al costado, formando una L con el Sol y la Tierra, vemos la mitad iluminada: son los cuartos.",
        "Puedo hacer el modelo con una linterna fija, mi cabeza como Tierra y una pelota como Luna sostenida con el brazo estirado, un poco más arriba que mi cabeza. Giro lentamente sobre mí mismo y miro cómo cambia la parte iluminada de la pelota. Nunca miro directo al haz de la linterna.",
    ],
    vocab=[("posición", "lugar donde está un cuerpo respecto de otros"), ("alineación", "cuando tres cuerpos quedan casi en una misma línea"), ("modelo", "representación para explicar algo"), ("hemisferio", "mitad de una esfera"), ("iluminado", "que recibe luz")],
    worked=[
        {"title": "Luna entre el Sol y la Tierra", "problem": "La Luna está entre el Sol y la Tierra. ¿Qué fase vemos?", "steps": ["El Sol ilumina la cara de la Luna que lo mira.", "Esa cara apunta lejos de la Tierra.", "Desde la Tierra vemos la cara oscura."], "answer": "Luna nueva"},
        {"title": "Tierra entre el Sol y la Luna", "problem": "La Tierra está entre el Sol y la Luna. ¿Qué fase vemos?", "steps": ["El Sol ilumina la cara de la Luna que mira hacia la Tierra.", "Vemos esa cara completa."], "answer": "Luna llena"},
    ],
    mistakes=[
        {"wrong": "Pensar que en la Luna nueva el Sol no ilumina la Luna.", "why": "Se ve oscura, así que parece apagada.", "fix": "El Sol ilumina la mitad que lo mira; esa mitad apunta lejos de nosotros."},
        {"wrong": "Decir que la Luna llena ocurre cuando la Luna está más cerca del Sol.", "why": "Se confunde el orden de las posiciones.", "fix": "En la Luna llena, la Tierra queda entre el Sol y la Luna."},
    ],
    tiers={
        "recovery": [
            ex("Si la Luna está entre el Sol y la Tierra, ¿qué fase vemos?", "Luna nueva", "La cara iluminada mira lejos de nosotros."),
            ex("Si la Tierra está entre el Sol y la Luna, ¿qué fase vemos?", "Luna llena", "Vemos toda la cara iluminada."),
            ex("Completa: la Luna da una vuelta alrededor de la ___.", "Tierra", "La Luna gira alrededor de la Tierra."),
        ],
        "understand": [
            ex("¿Por qué siempre hay una mitad de la Luna iluminada?", "Porque el Sol ilumina la mitad que lo mira", "La luz llega por un lado."),
            ex("¿Qué fase se ve cuando la Luna forma una L con el Sol y la Tierra?", "Un cuarto, con la mitad del disco iluminada", "De la cara que miramos, solo la mitad está iluminada."),
            ex("¿Qué representa tu cabeza en el modelo con la linterna?", "La Tierra", "Mira la Luna desde la Tierra."),
        ],
        "apply": [
            ex("En el modelo, la pelota está a tu derecha formando una L con la linterna. ¿Ves un cuarto o la Luna llena?", "Un cuarto", "De la cara que miras, solo la mitad está iluminada."),
            ex("En el modelo, la pelota queda frente a ti con la linterna a tus espaldas. ¿Qué fase muestra?", "Luna llena", "La Tierra queda entre la linterna y la Luna."),
            ex("En el modelo, la pelota queda entre tú y la linterna. ¿Qué fase muestra?", "Luna nueva", "Su cara iluminada mira a la linterna, lejos de ti."),
        ],
        "reason": [
            ex("Teo dice que en la Luna nueva la Luna desaparece. Según el modelo, ¿qué pasa en realidad?", "Sigue ahí, pero vemos su cara oscura", "La cara iluminada mira hacia el Sol."),
            ex("En el modelo, ¿qué movimiento real de la Luna cambia la parte iluminada que vemos: girar alrededor de la Tierra o apagarse?", "Girar alrededor de la Tierra", "Eso cambia desde dónde vemos su parte iluminada."),
        ],
        "challenge": [
            ex("¿Por qué el modelo con la linterna debe hacerse en una pieza oscura?", "Para que solo la linterna ilumine la pelota", "Otra luz confundiría las fases."),
            ex("¿Cuál es un límite de este modelo: la linterna y la pelota están mucho más cerca que el Sol y la Luna reales, o la pelota es redonda?", "Que están mucho más cerca que los cuerpos reales", "Las distancias y los tamaños del modelo no son reales."),
        ],
    },
    context=[ex("Fernanda mira su modelo: la pelota está entre ella y la linterna y solo ve la parte oscura. ¿Qué fase de la Luna representa su modelo?", "Luna nueva", "La cara iluminada queda lejos de ella.")],
    selfcheck=[
        ex("¿Qué cuerpo queda entre los otros dos en la Luna llena?", "La Tierra", "Está entre el Sol y la Luna."),
        ex("¿Qué cuerpo queda en el medio en la Luna nueva?", "La Luna", "Está entre el Sol y la Tierra."),
        ex("¿Cuántos días tarda la Luna en dar una vuelta a la Tierra, aproximadamente?", "Unos 27 días", "Es un poco menos que el ciclo de las fases, que dura unos 29 días y medio."),
    ],
    open_task=task(
        "Si puedes, haz el modelo con una linterna fija, tu cabeza como Tierra y una pelota como Luna en la mano. Gira sobre ti mismo lentamente y anota la fase que ves en cuatro posiciones. Si no puedes, usa esta lista de posiciones: A, la Luna entre el Sol y la Tierra; B, la Luna a la derecha de la Tierra en L; C, la Tierra entre el Sol y la Luna; D, la Luna a la izquierda en L. Escribe qué fase corresponde a cada posición.",
        "A: Luna nueva. B: un cuarto. C: Luna llena. D: el otro cuarto. La Luna gira alrededor de la Tierra.",
        ["relaciona cada posición con una fase", "explica con la mitad iluminada", "menciona que la Luna gira alrededor de la Tierra"],
        ["registro de las cuatro posiciones", "dibujo del modelo"],
        ["mezclar nueva y llena", "olvidar que el Sol ilumina una mitad"],
        "Valora el dibujo y pide que explique una posición con sus palabras.",
    ),
    reinforce="Con la linterna y una pelota, muestra a alguien de tu casa cómo se ve la Luna llena y la Luna nueva.",
    extend="Averigua qué fase de la Luna hay esta semana y dibuja su posición con respecto al Sol y la Tierra.",
)
