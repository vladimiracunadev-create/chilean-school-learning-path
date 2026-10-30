"""Student material for 1.º básico Educación Física y Salud, OA 11 (comportamientos seguros en la actividad física)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


OA11 = "EF01 OA 11"

register(
    OA11, 1,
    materials="Un espacio de 4 × 4 m, un reloj con segundos y una pelota blanda o un calcetín enrollado. Un adulto que dé las señales.",
    use="Aprenderé a calentar el cuerpo jugando antes de hacer ejercicio. Sirve para preparar mis articulaciones y mi atención y para no lastimarme.",
    prior=["Sé nombrar cuello, hombros, muñecas, rodillas y tobillos.", "Sé seguir una señal."],
    explain=[
        "Calentar es preparar el cuerpo para moverse. Cuando calientas, tus músculos y articulaciones se mueven mejor y tu atención se enciende. Las articulaciones son las partes donde se doblan los huesos: cuello, hombros, codos, muñecas, caderas, rodillas y tobillos.",
        "En el juego «El espejo» un guía hace un movimiento lento y los demás lo copian: girar los hombros 5 veces, girar las muñecas 5 veces, doblar las rodillas 5 veces y girar los tobillos 5 veces. Luego se camina 20 segundos y se trota suave 20 segundos. Todo es suave, sin tirones.",
        "Un buen calentamiento dura unos 3 minutos (puedes repetir «El espejo» y caminar y trotar suave un rato más) y sube el esfuerzo poco a poco. Se hace dentro de los límites, a dos brazos de distancia. Si algo duele, se detiene y se avisa. Calentar jugando es divertido y también es una regla de seguridad.",
    ],
    vocab=[("calentar", "preparar el cuerpo antes de moverse fuerte"), ("articulación", "parte donde se doblan los huesos"), ("atención", "estar pendiente de lo que hago"), ("guía", "quien muestra el movimiento"), ("tirón", "movimiento brusco que puede lastimar")],
    worked=[
        W("Contar movimientos", "En «El espejo» haces 4 movimientos de 5 repeticiones cada uno. ¿Cuántas repeticiones haces?", ["Hay 4 movimientos.", "Cada uno se repite 5 veces: 4 × 5.", "4 × 5 = 20."], "20 repeticiones."),
        W("Seguir al guía", "El guía gira los hombros hacia atrás despacio. ¿Cómo lo copias?", ["Miro al guía.", "Giro los hombros hacia atrás, despacio.", "Cuento hasta 5 sin tirones."], "Giro los hombros hacia atrás, despacio, 5 veces."),
    ],
    mistakes=[M("Saltar a jugar sin calentar.", "Se quiere empezar rápido.", "Dedica unos 3 minutos a calentar."),
              M("Hacer movimientos bruscos.", "Se piensa que más fuerte calienta más.", "Los movimientos son suaves y controlados.")],
    tiers={
        "recovery": [
            ex("Calentar sirve para preparar el cuerpo ¿antes o después del ejercicio fuerte?", "Antes", "Se hace para prepararse."),
            ex("La rodilla, ¿es una articulación?", "Sí", "Ahí se doblan los huesos de la pierna."),
            ex("Los movimientos del calentamiento son ¿suaves o bruscos?", "Suaves", "Los tirones pueden lastimar."),
        ],
        "understand": [
            ex("¿Para qué sirve calentar?", "Para preparar músculos y articulaciones", "El cuerpo se mueve mejor y se lastima menos."),
            ex("En «El espejo», ¿quién muestra el movimiento?", "El guía", "Los demás lo copian."),
            ex("Si algo te duele al calentar, ¿qué haces?", "Parar y avisar", "El dolor es una señal de alerta."),
        ],
        "apply": [
            arith("Haces 4 movimientos de 5 repeticiones. ¿Cuántas repeticiones son?", "4*5", "Se multiplican movimientos por repeticiones.", " repeticiones"),
            arith("Caminas 20 segundos y trotas suave 20 segundos. ¿Cuántos segundos son?", "20+20", "Se suman los dos tramos.", " segundos"),
            ex("Orden del calentamiento: hombros, muñecas, rodillas, tobillos. ¿Cuál es el tercero?", "Rodillas", "Está en tercer lugar de la lista."),
        ],
        "reason": [
            ex("Beto salta al juego sin calentar y se tuerce el tobillo. ¿Qué pudo hacer antes?", "Calentar los tobillos y el cuerpo", "El calentamiento prepara las articulaciones."),
            ex("Ana hace los círculos de hombros con tirones fuertes. ¿Qué debe cambiar?", "Hacerlos suaves y controlados", "Los tirones pueden lesionar."),
        ],
        "challenge": [
            arith("Un calentamiento: 4 movimientos de 5 repeticiones (20) y 40 segundos de caminar y trotar. Si cada repetición dura 3 segundos, ¿cuántos segundos duran las 20 repeticiones?", "20*3", "Se multiplican repeticiones por segundos.", " segundos"),
            ex("Cuenta las articulaciones de esta lista: cuello, hombros, codos, muñecas, caderas, rodillas, tobillos. ¿Cuántas son?", "7", "Se cuenta cada una."),
        ],
    },
    context=[ex("Llegas al parque con tus primos y quieren jugar de inmediato a pillarse. ¿Qué propones: A) empezar a correr al máximo, B) un calentamiento de 3 minutos como «El espejo», C) sentarse?", "B", "Calentar primero previene lesiones.")],
    selfcheck=[
        ex("¿Qué es una articulación?", "Parte donde se doblan los huesos", "Como la rodilla o el codo."),
        ex("¿Cuánto dura, más o menos, un buen calentamiento?", "3 minutos", "Da tiempo de preparar el cuerpo."),
        ex("Si duele algo, ¿sigues o avisas?", "Avisas", "El dolor es una alerta."),
    ],
    open_task=task("Con un adulto como guía, haz «El espejo»: 5 giros de hombros, 5 de muñecas, 5 flexiones suaves de rodillas y 5 giros de tobillos. Luego camina 20 segundos y trota suave 20 segundos (si quieres llegar a 3 minutos, repite el juego). Cuenta cuántas repeticiones hiciste y marca si cada movimiento fue suave (sí/no).",
                   "Hice 20 repeticiones y caminé y troté 40 segundos. Los 4 movimientos fueron suaves, sin tirones. No sentí dolor.",
                   ["copia los movimientos del guía", "hace movimientos suaves", "avisa si siente dolor"],
                   ["lista con 4 movimientos", "observación de un adulto", "relato oral"],
                   ["movimientos bruscos", "saltarse una articulación", "no avisar un dolor"],
                   "Destaca los movimientos suaves y pide nombrar la articulación que más costó mover."),
    reinforce="Gira los hombros 5 veces hacia atrás y 5 hacia adelante, despacio.",
    extend="Inventa un calentamiento de 3 minutos con una canción hablada tuya y enséñaselo a alguien.",
)

register(
    OA11, 2,
    materials="Cuatro conos o botellas vacías, una pelota blanda, un reloj y un adulto que da instrucciones. Las instrucciones están escritas en esta clase.",
    use="Aprenderé a escuchar una instrucción y a mostrar la regla antes de empezar. Sirve para jugar seguro y entender qué hacer.",
    prior=["Sé quedarme en silencio un momento.", "Sé repetir lo que oigo."],
    explain=[
        "Escuchar una instrucción es mirar a quien habla, esperar a que termine y entender qué hacer, cómo y cuándo. Para comprobar que entendiste, usas tres pasos: repites la regla con tus palabras, la muestras con el cuerpo y esperas la señal para partir.",
        "Por ejemplo, la instrucción es: «cuando oigas dos palmadas, camina hasta el cono azul y detente». Repites: «dos palmadas, camino al cono azul y me detengo». Luego lo muestras caminando un paso. Recién cuando suena la señal, partes.",
        "Si no entendiste, preguntas antes de partir: «¿puede repetir?». Preguntar no es malo; es seguro. Partir sin saber la regla puede causar choques o errores. Si cambia la instrucción, vuelves a repetirla y a mostrarla.",
    ],
    vocab=[("instrucción", "lo que me dicen que haga"), ("comprobar", "revisar que entendí"), ("señal de partida", "sonido o gesto que dice cuándo empezar"), ("repetir", "decir otra vez con mis palabras"), ("regla", "lo que se puede y no se puede hacer")],
    worked=[
        W("Comprobar una instrucción", "La instrucción es: «con una palmada trota al cono rojo; con dos palmadas camina al cono azul». ¿Cómo la compruebas?", ["Repito: «una palmada trota al rojo, dos palmadas camino al azul».", "Lo muestro con un paso para cada una.", "Espero la señal para partir."], "Repito, muestro y espero la señal."),
        W("Contar palmadas", "Se dan 3 palmadas en la primera ronda y 2 en la segunda. ¿Cuántas palmadas hay en total?", ["Primera ronda: 3.", "Segunda ronda: 2.", "3 + 2 = 5."], "5 palmadas."),
    ],
    mistakes=[M("Partir antes de la señal.", "Se quiere llegar primero.", "Espera la señal con el cuerpo quieto."),
              M("No preguntar cuando no se entiende.", "Da vergüenza.", "Pregunta «¿puede repetir?»; es lo más seguro.")],
    tiers={
        "recovery": [
            ex("Para escuchar, ¿miras a quien habla o miras para otro lado?", "Miras a quien habla", "Así entiendes mejor."),
            ex("Si no entiendes, ¿partes igual o preguntas?", "Preguntas", "Es más seguro."),
            ex("En la regla «con una palmada trota al cono rojo», ¿la palmada es la señal de partida o de descanso?", "Partida", "Indica cuándo empezar a trotar."),
        ],
        "understand": [
            ex("¿Cuáles son los tres pasos para comprobar una instrucción?", "Repetir, mostrar y esperar la señal", "Así se confirma que se entendió."),
            ex("¿Por qué es peligroso partir sin saber la regla?", "Porque puede haber choques o errores", "No sabes hacia dónde ir."),
            ex("Si cambia la instrucción, ¿qué haces?", "Repetirla y mostrarla de nuevo", "Hay que comprobar otra vez."),
        ],
        "apply": [
            ex("Regla: «con 1 palmada trota; con 2 palmadas camina». Suenan 2 palmadas. ¿Qué haces?", "Caminas", "Dos palmadas significa caminar."),
            ex("Regla: «con 3 palmadas, quédate quieto». Suenan 3 palmadas. ¿Qué haces?", "Te quedas quieto", "La regla lo dice."),
            arith("Suenan 2 palmadas, luego 1 y luego 3. ¿Cuántas palmadas son en total?", "2+1+3", "Se suman.", " palmadas"),
        ],
        "reason": [
            ex("Beto parte al oír la primera palmada, aunque la regla pedía esperar dos. ¿Qué debió hacer?", "Esperar la señal completa", "La regla se cumple completa."),
            ex("Caro no entendió y se quedó callada. ¿Qué debió hacer?", "Preguntar «¿puede repetir?»", "Preguntar es seguro."),
        ],
        "challenge": [
            ex("Regla: «una palmada trota al cono rojo, dos palmadas camina al azul, tres palmadas quédate quieto». Suenan 1, 3 y 2 palmadas en ese orden. ¿Qué haces en el orden de las señales?", "Trotas al rojo, te quedas quieto, caminas al azul", "Cada número tiene su acción."),
            arith("Haces 4 rondas de 50 segundos de acción. ¿Cuántos segundos son?", "4*50", "Se multiplican.", " segundos"),
        ],
    },
    context=[ex("En la clase de Educación Física la profesora explica un juego nuevo, pero tú estabas mirando a otro lado. ¿Qué haces: A) partes igual, B) le pides que lo repita, C) imitas a otro?", "B", "Pedir la instrucción evita errores.")],
    selfcheck=[
        ex("¿Qué haces antes de partir?", "Repites la regla y la muestras", "Se comprueba que se entendió."),
        ex("¿Partes antes de la señal?", "No", "Debes esperar la señal para partir."),
        ex("¿Qué dices si no entiendes?", "¿Puede repetir?", "Es la forma segura."),
    ],
    open_task=task("Con un adulto, practica esta regla: «una palmada: trota al cono rojo; dos palmadas: camina al cono azul; tres palmadas: quédate quieto». Antes de partir, repite la regla con tus palabras y muéstrala con un paso. Luego el adulto da 6 señales: 1, 2, 3, 2, 1, 3. Anota cuántas hiciste bien y si esperaste siempre la señal.",
                   "Repetí la regla y la mostré. Hice bien 5 de 6 señales. En una confundí el azul con el rojo. Esperé la señal las 6 veces.",
                   ["repite y muestra la regla", "espera la señal", "cumple la acción de cada señal"],
                   ["registro de 6 señales", "observación de un adulto", "relato oral"],
                   ["partir antes", "no repetir la regla", "confundir señales"],
                   "Reconoce que comprobó la regla y pide una estrategia para no confundir los conos."),
    reinforce="Repite la regla de las 3 palmadas con tus palabras y hazla una vez.",
    extend="Inventa una regla con 4 señales distintas y pide a alguien que la compruebe con los tres pasos.",
)

register(
    OA11, 3,
    materials="Una pelota blanda, 4 conos, una cuerda corta, un aro y un adulto. No se usan objetos duros ni pesados. Una caja para guardar los implementos.",
    use="Aprenderé a llevar y usar los materiales del juego con cuidado y con un adulto cerca. Sirve para no lastimarme ni lastimar a otros.",
    prior=["Sé llevar un objeto en la mano.", "Sé esperar mi turno."],
    explain=[
        "Un implemento es un objeto que se usa en un juego: pelota, cono, cuerda, aro. Se usa bajo supervisión, es decir, con un adulto que mira y puede ayudar. Antes de usarlo, el adulto lo revisa para ver que esté en buen estado.",
        "Para transportar, lleva un implemento a la vez, caminando, con las dos manos si es grande. No lo lances sin permiso ni lo uses como arma. Una cuerda no se enrolla en el cuello ni se jala a otra persona. Una pelota blanda se lanza solo cuando el compañero está mirando y listo.",
        "Al terminar, devuelves el implemento a la caja y cuentas que estén todos. Si uno se rompe o queda en el suelo, avisas. Ningún implemento se usa sin autorización. El orden evita tropiezos.",
    ],
    vocab=[("implemento", "objeto que se usa en un juego"), ("supervisión", "un adulto que mira y puede ayudar"), ("transportar", "llevar de un lugar a otro"), ("autorización", "permiso del adulto"), ("revisar", "mirar que esté en buen estado")],
    worked=[
        W("Guardar los materiales", "Sacaste 4 conos, 1 pelota y 1 aro. Al terminar devuelves todo. ¿Cuántos implementos debes contar?", ["Cuento los conos: 4.", "Sumo la pelota y el aro: 4 + 1 + 1.", "4 + 1 + 1 = 6."], "6 implementos."),
        W("Usar la cuerda con seguridad", "Tienes una cuerda de 2 m. ¿Cómo la usas?", ["La uso solo para saltar en un lugar libre.", "No la enrollo en el cuello ni la jalo a otro.", "Cuando termino, la guardo en la caja."], "Solo para saltar, sin enrollarla ni jalar a otros."),
    ],
    mistakes=[M("Lanzar la pelota sin avisar.", "Se quiere jugar rápido.", "Espera a que el compañero esté mirando y listo."),
              M("Dejar los implementos en el suelo.", "Se olvida guardarlos.", "Devuélvelos a la caja y cuenta.")],
    tiers={
        "recovery": [
            ex("Los implementos se usan con ¿supervisión o sin adulto?", "Con supervisión", "El adulto cuida."),
            ex("Para transportar un cono, ¿caminas o corres?", "Caminas", "Caminar evita tropiezos con el material."),
            ex("Al terminar, ¿guardas los materiales o los dejas en el suelo?", "Los guardas", "Guardar el material evita tropezones."),
        ],
        "understand": [
            ex("¿Qué es un implemento?", "Un objeto que se usa en un juego", "Como una pelota o un aro."),
            ex("¿Por qué el adulto revisa el material antes?", "Para ver que esté en buen estado", "Un objeto roto puede lastimar."),
            ex("¿Puedes enrollar una cuerda en el cuello de alguien?", "No", "Enrollar una cuerda es peligroso."),
        ],
        "apply": [
            arith("Sacaste 4 conos, 1 pelota y 1 aro. ¿Cuántos implementos son?", "4+1+1", "Se suman.", " implementos"),
            arith("Devuelves 5 de 6 implementos. ¿Cuántos faltan?", "6-5", "Se resta.", " implemento"),
            ex("Lanzas una pelota blanda a un compañero que está mirando para otro lado. ¿Esperas o lanzas?", "Esperas a que mire", "Debe estar listo."),
        ],
        "reason": [
            ex("Beto dice «uso la cuerda como látigo, es divertido». ¿Qué respondes?", "Que es peligroso y no se hace", "Una cuerda mal usada puede lastimar."),
            ex("Falta un cono al terminar. ¿Qué haces?", "Avisar y buscarlo con el adulto", "Hay que encontrarlo para que nadie tropiece."),
        ],
        "challenge": [
            arith("Cada uno de 3 niños lleva 2 conos. ¿Cuántos conos llevan entre todos?", "3*2", "Se multiplican.", " conos"),
            ex("Reglas para la pelota: 1) mirar al compañero, 2) esperar que esté listo, 3) lanzar suave. Si cumples dos, ¿cuántas te faltan?", "1", "3 menos 2 es 1."),
        ],
    },
    context=[ex("En la plaza encuentras una pelota dura y un palo en el suelo. No hay adulto cerca. ¿Qué haces: A) jugar con el palo, B) avisar a un adulto, C) lanzar la pelota?", "B", "No se usan objetos sin supervisión.")],
    selfcheck=[
        ex("¿Con quién usas los implementos?", "Con un adulto cerca", "Es la supervisión."),
        ex("¿Qué haces con el material al terminar?", "Lo guardas y cuentas", "Así no quedan en el suelo."),
        ex("¿Se usa la cuerda para jalar a otro?", "No", "Una cuerda mal usada puede lastimar."),
    ],
    open_task=task("Con un adulto, saca de una caja 4 conos, 1 pelota blanda, 1 aro y 1 cuerda. Cuenta cuántos implementos son. Lleva cada uno al cuadrado caminando. Haz 5 lanzamientos suaves a un compañero que te mira. Al final guarda todo y cuenta de nuevo. Anota si faltó alguno.",
                   "Eran 7 implementos. Los llevé caminando. Hice 5 lanzamientos suaves con mi compañero mirando. Guardé los 7 y no faltó ninguno.",
                   ["transporta con cuidado", "usa el material bajo supervisión", "guarda y cuenta"],
                   ["registro de la cuenta", "observación de un adulto", "relato oral"],
                   ["correr con material", "lanzar sin avisar", "olvidar guardar"],
                   "Reconoce el cuidado y pide explicar por qué se cuenta al guardar."),
    reinforce="Lleva un cono caminando de un lado a otro y devuélvelo a su lugar, 3 veces.",
    extend="Haz una lista de 5 reglas para usar implementos y pide a un adulto que las revise.",
)

register(
    OA11, 4,
    materials="Cuatro conos o botellas para formar un cuadrado de 4 × 4 m, una cuerda en el suelo como línea central, un reloj y un adulto. Una hoja y lápiz.",
    use="Aprenderé a mantenerme dentro de los límites y a guardar una distancia segura de otros. Sirve para evitar choques y caídas.",
    prior=["Sé qué es un límite.", "Sé medir una distancia con los brazos."],
    explain=[
        "Un límite es una marca que dice hasta dónde se puede ir. Puede ser una línea, un cono, una cuerda o un muro. Dentro de los límites juegas; fuera de ellos no. Así el juego queda controlado y protegido. Ningún juego se hace fuera del cuadrado.",
        "La distancia segura es el espacio libre entre tú y los demás. Se mide con los brazos: si estiras los dos brazos a los lados y no tocas a nadie, la distancia es suficiente. Si los brazos de dos personas se tocan, están demasiado cerca.",
        "Si alguien se acerca demasiado, te alejas con calma y avisas con amabilidad. Si sales del límite sin querer, vuelves caminando y avisas. En el juego «Burbujas», caminan por el cuadrado manteniendo su burbuja libre. Si una burbuja choca con otra, se detienen y ajustan.",
    ],
    vocab=[("límite", "marca que dice hasta dónde se puede ir"), ("distancia segura", "espacio libre de dos brazos entre personas"), ("burbuja", "espacio personal alrededor de mí"), ("ajustar", "cambiar un poco para que quede bien"), ("zona segura", "lugar permitido y sin riesgos")],
    worked=[
        W("Mantenerse dentro del cuadrado", "Tu cuadrado es de 4 × 4 m. Una pelota rueda fuera. ¿Qué haces?", ["No salgo corriendo detrás de la pelota.", "Aviso al adulto.", "El adulto indica cuándo es seguro salir a buscarla."], "Aviso y espero la autorización del adulto."),
        W("Medir el borde del cuadrado", "Los 4 lados del cuadrado miden 4 m cada uno. ¿Cuántos metros mide la vuelta completa?", ["Hay 4 lados.", "Cada lado mide 4 m: 4 × 4.", "4 × 4 = 16."], "16 metros."),
    ],
    mistakes=[M("Salir del límite para recoger la pelota.", "Se quiere seguir jugando.", "Avisa y espera al adulto."),
              M("Jugar pegado a otros.", "No se piensa en el espacio.", "Mantén los dos brazos de distancia.")],
    tiers={
        "recovery": [
            ex("Un límite dice hasta dónde se puede ¿jugar o dormir?", "Jugar", "Marca la zona del juego."),
            ex("La distancia segura entre personas son ¿dos brazos o un dedo?", "Dos brazos", "Esa distancia evita choques."),
            ex("Si la pelota sale del cuadrado, ¿avisas o corres tras ella?", "Avisas", "Salir sin permiso es inseguro."),
        ],
        "understand": [
            ex("¿Por qué se juega dentro del cuadrado?", "Para controlar el juego y evitar riesgos", "Fuera hay más peligros."),
            ex("¿Cómo se mide la distancia segura?", "Estirando los dos brazos sin tocar a nadie", "Así se comprueba el espacio."),
            ex("¿Qué haces si alguien se acerca demasiado?", "Te alejas con calma y avisas", "Se resuelve con respeto."),
        ],
        "apply": [
            arith("Un cuadrado tiene 4 lados de 4 m. ¿Cuántos metros mide su borde?", "4*4", "Se multiplican lados por metros.", " m"),
            ex("Hay 6 niños y el cuadrado es pequeño. Para tener distancia segura, ¿cuántos juegan a la vez: 2 o 6?", "2", "Con 6 no hay espacio."),
            arith("Dos niños se separan 2 pasos y luego otros 2 pasos. ¿Cuántos pasos hay entre el primero y el tercero?", "2+2", "Se suman las distancias.", " pasos"),
        ],
        "reason": [
            ex("Ema dice «el límite es solo una sugerencia». ¿Qué le dices?", "Que el límite protege y se respeta", "Respetar el límite evita accidentes."),
            ex("Beto corre hacia el borde y casi choca con la reja. ¿Qué debió hacer?", "Frenar antes del límite", "Los límites son para no lastimarse."),
        ],
        "challenge": [
            arith("Haces 3 vueltas completas al borde del cuadrado de 16 m, caminando. ¿Cuántos metros caminas?", "3*16", "Se multiplican vueltas por metros.", " m"),
            ex("Hay un cuadrado de 4 × 4 m y se dibuja una línea central. ¿Cuántas zonas de juego hay?", "2", "La línea divide el cuadrado en dos."),
        ],
    },
    context=[ex("Juegas en el patio y se rompe la reja de un costado del cuadrado. ¿Qué haces: A) juegas cerca de la reja rota, B) avisas a un adulto y cambias de zona, C) saltas la reja?", "B", "Una reja rota es un riesgo.")],
    selfcheck=[
        ex("¿Qué distancia se guarda entre personas?", "Dos brazos", "Esa distancia evita choques."),
        ex("¿Qué haces si la pelota sale del cuadrado?", "Avisas y esperas", "Salir sin permiso es inseguro."),
        ex("¿Cuántos metros mide el borde de un cuadrado de 4 m de lado?", "16", "4 por 4 son 16."),
    ],
    open_task=task("Con cuatro conos y una cuerda arma un cuadrado de 4 × 4 m. Juega «Burbujas» con un adulto: caminan 40 segundos manteniendo dos brazos de distancia y sin salirse. Haz 3 rondas. Anota cuántas veces tu burbuja chocó con otra y cuántas veces saliste del límite.",
                   "En las 3 rondas mi burbuja chocó 1 vez y me alejé con calma. No salí del límite.",
                   ["se mantiene dentro del límite", "guarda dos brazos de distancia", "ajusta con calma"],
                   ["registro de choques y salidas", "observación de un adulto", "dibujo del cuadrado"],
                   ["salir sin avisar", "acercarse demasiado", "correr hacia el borde"],
                   "Reconoce el control y pide una estrategia para mantener la distancia."),
    reinforce="Camina por el cuadrado 20 segundos manteniendo dos brazos de distancia con un adulto.",
    extend="Dibuja un plano de tu patio con los límites y las zonas seguras.",
)

register(
    OA11, 5,
    materials="Tarjetas con las condiciones inseguras escritas aquí: «piso mojado», «un cordón desamarrado», «un niño que empuja», «un objeto en el suelo», «un compañero se cae y llora». Un adulto, un pito o una señal de voz y una hoja.",
    use="Aprenderé a detener el juego, avisar a un adulto y volver a jugar cuando es seguro. Sirve para cuidar a todos.",
    prior=["Sé que debo avisar a un adulto.", "Sé usar la palabra «alto»."],
    explain=[
        "Una condición insegura es algo que puede causar un accidente: piso mojado, un cordón desamarrado, un niño que empuja, un objeto en el suelo, un compañero que se cae. Si la ves, sigues tres pasos: detener, avisar y reanudar.",
        "Detener: dices «alto» fuerte y todos paran. Avisar: te acercas caminando a un adulto y explicas con calma qué viste, dónde y quién necesita ayuda. Reanudar: solo cuando el adulto dice que es seguro, y después de arreglar el problema, vuelven a jugar.",
        "Si alguien se lastima, no lo muevas, no toques la sangre y llama al adulto de inmediato. Tampoco juegas mientras tanto. El botiquín lo maneja solo un adulto. Avisar a tiempo es valiente y cuida a todos.",
    ],
    vocab=[("condición insegura", "algo que puede causar un accidente"), ("detener", "parar el juego"), ("avisar", "decirle a un adulto lo que pasa"), ("reanudar", "volver a jugar"), ("botiquín", "caja con elementos de primeros auxilios que maneja un adulto")],
    worked=[
        W("Piso mojado", "Ves un charco en el patio donde juegan. ¿Qué haces con los tres pasos?", ["Detengo: digo «alto».", "Aviso: camino hasta el adulto y le cuento del charco.", "Reanudo: cuando el adulto lo seca o cambia el lugar, seguimos."], "Detener, avisar y reanudar cuando el adulto lo diga."),
        W("Contar condiciones", "En el patio hay 3 condiciones inseguras: un charco, un cordón desamarrado y un objeto en el suelo. Arreglas 2. ¿Cuántas quedan?", ["Había 3.", "Arreglé 2.", "3 − 2 = 1."], "1 condición."),
    ],
    mistakes=[M("Seguir jugando mientras alguien está lastimado.", "Se piensa que no es grave.", "Todos paran y se avisa al adulto."),
              M("Tocar el botiquín sin adulto.", "Se quiere ayudar.", "El botiquín lo maneja un adulto; tú avisas.")],
    tiers={
        "recovery": [
            ex("Al ver un riesgo, ¿qué palabra dices para detener el juego?", "Alto", "Es la señal de parar."),
            ex("Luego de detener, ¿avisas a un adulto o te vas?", "Avisas a un adulto", "Él decide qué hacer."),
            ex("¿Quién maneja el botiquín: un niño o un adulto?", "Un adulto", "Contiene elementos que requieren cuidado."),
        ],
        "understand": [
            ex("¿Cuáles son los tres pasos?", "Detener, avisar y reanudar", "Es la secuencia de la clase."),
            ex("¿Cuándo se reanuda el juego?", "Cuando el adulto dice que es seguro", "Primero se arregla el problema."),
            ex("¿Qué es una condición insegura?", "Algo que puede causar un accidente", "Como un piso mojado."),
        ],
        "apply": [
            ex("Un niño empuja a otro. ¿Cuál es el primer paso?", "Detener el juego", "Se para primero."),
            ex("Ves un cordón desamarrado en tu zapatilla. ¿Qué haces?", "Paras y lo amarras", "Amarrar el cordón evita tropezar."),
            arith("Hay 5 condiciones inseguras y se arreglan 3. ¿Cuántas quedan?", "5-3", "Se resta.", " condiciones"),
        ],
        "reason": [
            ex("Beto dice «si aviso me van a retar». ¿Qué le respondes?", "Avisar cuida a todos y es valiente", "Avisar es lo correcto."),
            ex("Un compañero se cae y llora. Ema sigue jugando. ¿Qué debió hacer?", "Detenerse y avisar a un adulto", "Alguien necesita ayuda."),
        ],
        "challenge": [
            ex("Tarjetas: piso mojado, cordón, niño que empuja, objeto en el suelo, compañero se cae. ¿Cuántas tarjetas hay en total?", "5", "Se cuentan las cinco."),
            arith("Un juego se detuvo 20 segundos para arreglar un charco y luego se retomó 40 segundos. ¿Cuántos segundos duró la secuencia?", "20+40", "Se suman.", " segundos"),
        ],
    },
    context=[ex("En el recreo un niño se cae y se golpea la rodilla; sangra un poco. ¿Qué haces: A) lo levantas rápido, B) detienes el juego y caminas rápido a avisar a un adulto, C) sigues jugando?", "B", "Avisa y deja que un adulto atienda.")],
    selfcheck=[
        ex("¿Qué dices para detener el juego?", "Alto", "Es la señal."),
        ex("¿A quién avisas?", "A un adulto", "Él sabe qué hacer."),
        ex("¿Cuándo vuelven a jugar?", "Cuando es seguro y el adulto lo dice", "Es la regla."),
    ],
    open_task=task("Con las cinco tarjetas de esta clase («piso mojado», «un cordón desamarrado», «un niño que empuja», «un objeto en el suelo», «un compañero se cae y llora»), escribe para cada una qué haces con los tres pasos: detener, avisar, reanudar. Luego haz el simulacro con un adulto: él muestra una tarjeta y tú dices «alto», caminas a avisar y esperas la autorización. Anota cuántas veces cumpliste los 3 pasos.",
                   "Piso mojado: dije alto, avisé y esperé a que lo secaran. Cordón: lo amarré. Empujón: dije alto y avisé. Objeto: avisé. Compañero: avisé y no lo toqué. Cumplí los 3 pasos en 5 de 5.",
                   ["detiene el juego", "avisa a un adulto con calma", "reanuda solo con autorización"],
                   ["hoja con cinco respuestas", "simulacro observado", "relato oral"],
                   ["seguir jugando", "tocar el botiquín", "no avisar"],
                   "Reconoce los pasos cumplidos y pregunta qué dirá exactamente al adulto."),
    reinforce="Practica decir «alto», caminar hasta un adulto y explicar un riesgo en una oración.",
    extend="Haz un afiche con los tres pasos y píntalo para tu casa o sala.",
)
