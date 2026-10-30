"""Student material for 1.º básico Matemática, OA 15 (líneas), OA 16 (duración), OA 17 (secuencia temporal) y OA 18 (longitud)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA15, OA16, OA17, OA18 = "MA01 OA 15", "MA01 OA 16", "MA01 OA 17", "MA01 OA 18"
DAYS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MONTHS = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def day_after(day: str, steps: int = 1) -> str:
    return DAYS[(DAYS.index(day) + steps) % 7]


def month_after(month: str, steps: int = 1) -> str:
    return MONTHS[(MONTHS.index(month) + steps) % 12]


# ---------------------------------------------------------------- OA 15
register(
    OA15, 1,
    materials="Un cordel o lana de 1 metro, una cinta o lápiz y una hoja; los recorridos están descritos en este cuaderno.",
    use="Aprenderé a distinguir una línea recta de una línea curva siguiendo recorridos. Sirve para describir caminos y dibujos.",
    prior=["Sé qué es una línea.", "Sé caminar siguiendo una indicación."],
    explain=[
        "Una línea recta no cambia de dirección: va siempre derecho, como una regla. Una línea curva cambia de dirección poco a poco, como un camino con una vuelta. Si estiras un cordel, queda recto; si lo dejas con una vuelta, queda curvo.",
        "Para decidir si una línea es recta, apoya una regla: si toda la línea toca la regla, es recta. Si se separa, es curva. También puedes seguirla con el dedo: si debes ir girando, es curva.",
        "Hay líneas rectas que son horizontales (acostadas), verticales (paradas) o inclinadas. Las curvas pueden ser suaves, como una colina, o cerradas, como un círculo. Todas son líneas.",
    ],
    vocab=[("línea recta", "línea que va siempre derecho"), ("línea curva", "línea que va girando"), ("regla", "instrumento para dibujar rectas"), ("recorrido", "camino que sigo"), ("dirección", "hacia dónde va")],
    worked=[
        {"title": "Recta o curva", "problem": "Un camino sigue derecho sin vueltas. ¿Es recta o curva?", "steps": ["No cambia de dirección.", "Si apoyo una regla, toca toda la línea.", "Es recta."], "answer": "Recta"},
        {"title": "Una curva", "problem": "Un camino tiene una vuelta como una S. ¿Es recta o curva?", "steps": ["Cambia de dirección.", "La regla no tocaría toda la línea.", "Es curva."], "answer": "Curva"},
    ],
    mistakes=[
        {"wrong": "Decir que una línea inclinada es curva.", "why": "Se confunde inclinada con curva.", "fix": "Una línea inclinada que va derecho sigue siendo recta."},
        {"wrong": "Decir que una línea con una esquina es curva.", "why": "Se confunde esquina con vuelta.", "fix": "Una esquina es un cambio brusco de dirección: son dos rectas juntas, no una curva."},
    ],
    tiers={
        "recovery": [ex("El borde de una regla, ¿es recta o curva?", "Recta", "No cambia de dirección."), ex("El borde de una pelota vista de frente, ¿es recta o curva?", "Curva", "El borde va girando todo el tiempo."), ex("Un cordel bien estirado, ¿es recto o curvo?", "Recto", "No tiene vueltas.")],
        "understand": [
            ex("¿Qué hago para comprobar si una línea es recta?", "Apoyo una regla y veo si la toca toda", "Una recta calza con la regla."),
            ex("¿Cambia de dirección una línea recta?", "No", "Va siempre derecho."),
            ex("¿Una línea curva tiene vueltas?", "Sí", "Va cambiando de dirección poco a poco."),
        ],
        "apply": [
            ex("Dibuja una línea recta horizontal y una vertical.", "Una acostada y una parada", "Ambas son rectas."),
            ex("Dibuja una línea curva de lado a lado de la hoja.", "Una curva suave", "No debe ser derecha."),
            ex("Clasifica: borde de una puerta, camino con muchas vueltas, lápiz, rueda.", "Rectas: puerta y lápiz. Curvas: camino con vueltas y rueda", "Bordes derechos son rectos."),
        ],
        "reason": [
            ex("Ana dice que una escalera dibujada con escalones es una línea curva. ¿Qué error comete?", "Los escalones tienen esquinas, no son curvas", "Una curva gira poco a poco."),
            ex("¿Puede una línea ser recta y estar inclinada?", "Sí", "Va derecho aunque esté inclinada."),
        ],
        "challenge": [
            ex("Con tres rectas, ¿puedes formar una figura cerrada? ¿Cuál?", "Sí, un triángulo", "Tres rectas que se juntan."),
            ex("¿Cuántas rectas necesitas para formar un cuadrado?", "4", "Cuatro lados rectos."),
        ],
    },
    context=[ex("Una hormiga camina desde la puerta hasta el pan en línea recta. Otra da vueltas hasta llegar. ¿Qué hormiga recorrió un camino curvo?", "La que dio vueltas", "Cambió de dirección.")],
    selfcheck=[ex("El lado de un libro cerrado, ¿es recto o curvo?", "Recto", "El borde va derecho sin girar."), ex("¿El borde de una moneda es recto o curvo?", "Curvo", "El borde va girando todo el tiempo."), ex("¿Con qué compruebo una recta?", "Con una regla", "Una recta debe calzar con la regla.")],
    open_task=task("En una hoja, dibuja un camino con 3 tramos rectos y 2 tramos curvos. Marca con rojo los rectos y con azul los curvos. Explica cómo sabes cuál es cuál.", "Dibujé una recta, una curva, otra recta, otra curva y una recta. Los rojos calzan con la regla; los azules no.", ["3 rectas y 2 curvas", "los marca con colores", "explica cómo decide"], ["dibujo", "explicación"], ["usar rectas con esquinas como curvas", "no distinguir con regla"], "Pide comprobar con una regla."),
    reinforce="Traza con lana una recta y una curva sobre la mesa.",
    extend="Busca en tu casa tres objetos con bordes rectos y tres con bordes curvos.",
)

register(
    OA15, 2,
    materials="Objetos de la sala o de la casa y una cinta; la lista de lugares se describe en este cuaderno.",
    use="Aprenderé a encontrar líneas rectas y curvas en mi entorno. Sirve para observar los objetos con más atención.",
    prior=["Sé distinguir una línea recta de una curva.", "Sé nombrar objetos."],
    explain=[
        "Las líneas están en todas partes. El borde de una mesa es recto. El borde de un plato es curvo. Una puerta tiene rectas verticales y horizontales. Una rueda de bicicleta es una curva cerrada.",
        "Para buscar líneas, recorre un objeto con el dedo y pregúntate si cambia de dirección. Si va derecho, es recta; si va girando, es curva. Algunos objetos tienen ambos tipos: un paraguas abierto tiene varillas rectas y un borde curvo.",
        "Anota lo que encuentras en una tabla de dos columnas: rectas y curvas. Al final cuenta cuántas encontraste de cada tipo y compara.",
    ],
    vocab=[("entorno", "lo que me rodea"), ("borde", "el límite de un objeto"), ("recorrer", "seguir con el dedo"), ("tabla", "cuadro con columnas para ordenar"), ("clasificar", "ordenar según un criterio")],
    worked=[
        {"title": "Buscar líneas", "problem": "Busca líneas en una puerta.", "steps": ["Los lados de la puerta son rectas verticales.", "El borde de arriba es una recta horizontal.", "La manilla puede tener una curva."], "answer": "Rectas: lados y borde; curva: manilla"},
        {"title": "Clasificar en una tabla", "problem": "Clasifica: borde de mesa, plato, cuaderno, reloj redondo.", "steps": ["Borde de mesa: recta.", "Plato: curva.", "Cuaderno: recta.", "Reloj redondo: curva."], "answer": "Rectas: mesa y cuaderno. Curvas: plato y reloj"},
    ],
    mistakes=[
        {"wrong": "Decir que un objeto tiene sólo un tipo de línea.", "why": "No se mira todo el objeto.", "fix": "Revisa todos los bordes: pueden tener rectas y curvas."},
        {"wrong": "Contar dos veces el mismo borde.", "why": "Se pierde el control.", "fix": "Marca cada borde que cuentas."},
    ],
    tiers={
        "recovery": [ex("El borde de un pizarrón, ¿es recta o curva?", "Recta", "El borde va derecho sin girar."), ex("El borde de una taza vista desde arriba, ¿es recta o curva?", "Curva", "El borde de la taza es redondo."), ex("El borde de una ventana rectangular, ¿es recta o curva?", "Recta", "Tiene lados derechos.")],
        "understand": [
            ex("¿Puede un objeto tener rectas y curvas?", "Sí", "Por ejemplo, un paraguas."),
            ex("¿Para qué sirve una tabla de dos columnas?", "Para ordenar las rectas y las curvas", "Se ve cuántas hay de cada una."),
            ex("¿Cómo recorro un borde para clasificarlo?", "Con el dedo, mirando si cambia de dirección", "Si va girando, es curvo."),
        ],
        "apply": [
            ex("Clasifica: libro, pelota, regla, moneda.", "Rectas: libro y regla. Curvas: pelota y moneda", "Libro y regla tienen bordes derechos."),
            ex("Clasifica: borde del pupitre, aro, hoja de papel, rueda.", "Rectas: pupitre y hoja. Curvas: aro y rueda", "Los aros y ruedas son redondos."),
            ex("En un paraguas abierto, ¿qué tiene líneas rectas y qué curvas?", "Rectas: las varillas. Curvas: el borde", "El borde del paraguas va girando."),
        ],
        "reason": [
            ex("Beto dice que un reloj redondo tiene sólo rectas. ¿Qué error comete?", "Su borde es curvo; sólo las manecillas son rectas", "El reloj tiene rectas y curvas."),
            ex("¿Por qué conviene marcar los bordes que cuentas?", "Para no contar dos veces", "Así se mantiene el control."),
        ],
        "challenge": [
            ex("Un objeto tiene 4 bordes rectos y 1 curvo. ¿Cuántos bordes tiene en total?", "5", "4 + 1 = 5."),
            ex("En una sala hay 3 objetos con bordes rectos y 2 con curvos. ¿Cuántos objetos hay en total?", "5", "3 + 2 = 5."),
        ],
    },
    context=[arith("En una mochila hay 3 cuadernos (bordes rectos) y 2 pelotitas (bordes curvos). ¿Cuántos objetos hay?", "3+2", "Se juntan los dos grupos.")],
    selfcheck=[ex("¿El borde de una galleta redonda es recto o curvo?", "Curvo", "El borde va girando todo el tiempo."), ex("¿El borde de una hoja de cuaderno es recto o curvo?", "Recto", "Tiene lados derechos."), ex("¿Qué usas para anotar los resultados?", "Una tabla", "Ordena por tipo.")],
    open_task=task("Recorre tu pieza o tu sala y encuentra 3 objetos con líneas rectas y 3 con líneas curvas. Anótalos en una tabla de dos columnas y cuenta cuántos hay en cada una.", "Rectas: mesa, libro, puerta (3). Curvas: plato, reloj, pelota (3). Total: 6 objetos.", ["3 y 3 objetos", "los ordena en tabla", "cuenta cada columna"], ["tabla", "conteo"], ["poner un objeto en la columna equivocada", "no contar"], "Pide recorrer el borde con el dedo."),
    reinforce="Busca líneas rectas y curvas en las letras de tu nombre.",
    extend="Busca un objeto que tenga una línea recta y una curva y descríbelo.",
)

register(
    OA15, 3,
    materials="Una hoja en blanco, una regla y lápiz de color; las instrucciones de dibujo están en cada ejercicio.",
    use="Aprenderé a dibujar líneas rectas y curvas en distintas posiciones: horizontales, verticales e inclinadas. Sirve para dibujar con precisión.",
    prior=["Sé distinguir rectas y curvas.", "Sé usar la regla."],
    explain=[
        "Las rectas pueden estar en distintas posiciones. Una recta horizontal va de lado a lado, como el horizonte. Una vertical va de arriba abajo, como un poste. Una inclinada está entre las dos, como un techo de casa.",
        "Para dibujar una recta, apoya la regla y desliza el lápiz por el borde. Para dibujar una curva, mueve la mano en forma de arco sin levantar el lápiz. Una curva puede girar a la derecha, a la izquierda o ambas.",
        "Mira tu dibujo y comprueba: ¿las rectas tocan la regla? ¿Las curvas no tienen picos? Si quedó una esquina, borra y vuelve a intentar con más suavidad.",
    ],
    vocab=[("horizontal", "acostada, de lado a lado"), ("vertical", "parada, de arriba abajo"), ("inclinada", "ni horizontal ni vertical"), ("arco", "curva suave"), ("trazo", "línea dibujada")],
    worked=[
        {"title": "Dibujar rectas", "problem": "Dibuja una recta horizontal, una vertical y una inclinada.", "steps": ["Apoyo la regla acostada y trazo una horizontal.", "La giro parada y trazo una vertical.", "La giro en diagonal y trazo una inclinada."], "answer": "Tres rectas en tres posiciones"},
        {"title": "Dibujar una curva", "problem": "Dibuja una curva suave sin levantar el lápiz.", "steps": ["Parto en un punto.", "Muevo la mano en arco.", "Termino sin picos."], "answer": "Una curva suave"},
    ],
    mistakes=[
        {"wrong": "Dibujar una recta sin regla y que quede torcida.", "why": "No se apoya la regla.", "fix": "Usa la regla para las rectas."},
        {"wrong": "Hacer picos en una curva.", "why": "Se levanta el lápiz o se frena.", "fix": "Dibuja la curva en un solo movimiento suave."},
    ],
    tiers={
        "recovery": [ex("¿Cómo es una línea horizontal?", "Acostada, de lado a lado", "Como el horizonte."), ex("¿Cómo es una línea vertical?", "Parada, de arriba abajo", "Como un poste."), ex("¿Qué usas para dibujar una recta?", "Una regla", "Guía el lápiz.")],
        "understand": [
            ex("¿Es una recta inclinada una recta?", "Sí", "Va derecho aunque esté inclinada."),
            ex("¿Cómo dibujo una curva sin picos?", "Con un solo movimiento suave", "No se levanta el lápiz."),
            ex("¿Cuál es la posición de la línea de un poste?", "Vertical", "Va de arriba abajo."),
        ],
        "apply": [
            ex("Dibuja un techo con dos rectas inclinadas.", "Una casita con techo en forma de punta", "Las dos rectas inclinadas se juntan arriba."),
            ex("Dibuja una ola con una curva.", "Una curva en forma de colina", "La ola es una curva suave."),
            ex("Dibuja una escalera con 3 rectas horizontales y 2 verticales.", "Escalera con tres peldaños", "Rectas en dos posiciones."),
        ],
        "reason": [
            ex("Lucía dice que una recta inclinada es curva. ¿Qué error comete?", "Es recta aunque esté inclinada", "Una recta inclinada no gira."),
            ex("¿Por qué una curva con picos no es una curva suave?", "Porque cambia de dirección de golpe", "Los picos son esquinas."),
        ],
        "challenge": [
            ex("Dibuja una figura con 2 rectas y 2 curvas.", "Por ejemplo, un pez con 2 curvas en el cuerpo y 2 rectas en la cola", "Cuenta cada tipo."),
            ex("Un triángulo tiene 3 rectas y un cuadrado tiene 4. ¿Cuántas rectas hay si dibujas los dos?", "7", "3 + 4 = 7."),
        ],
    },
    context=[ex("Para dibujar una montaña con rectas inclinadas, ¿cuántas rectas necesitas para un pico?", "2", "Una sube y otra baja.")],
    selfcheck=[ex("¿Cómo se llama una recta parada?", "Vertical", "Va de arriba abajo."), ex("¿Cómo se llama una recta acostada?", "Horizontal", "Va de lado a lado."), ex("¿Qué debe tener una curva suave?", "Ningún pico", "Una curva suave no tiene esquinas.")],
    open_task=task("Dibuja una casa con una puerta, una ventana y un camino. Usa rectas horizontales, verticales e inclinadas, y al menos dos curvas. Marca con colores un ejemplo de cada tipo.", "Casa con cuadrado (rectas horizontales y verticales), techo (rectas inclinadas), camino curvo y sol curvo. Marqué en rojo una horizontal, en verde una vertical, en azul una inclinada y en negro una curva.", ["usa las tres posiciones", "incluye curvas", "marca ejemplos"], ["dibujo", "colores"], ["rectas torcidas", "no marcar"], "Pide trazar con regla y comprobar."),
    reinforce="Dibuja un paisaje con colinas curvas y casas con rectas.",
    extend="Dibuja un patrón repetido que alterne rectas y curvas.",
)

register(
    OA15, 4,
    materials="Una hoja, lápices de colores y una regla; las figuras que se forman se describen en cada ejercicio.",
    use="Aprenderé a combinar líneas rectas y curvas para formar dibujos. Sirve para crear imágenes y letras.",
    prior=["Sé dibujar rectas y curvas.", "Sé reconocer figuras."],
    explain=[
        "Con líneas rectas y curvas puedes formar muchos dibujos. Un sol usa un círculo (curva cerrada) y rayos (rectas). Un árbol usa rectas para el tronco y curvas para las hojas.",
        "Para componer un dibujo, primero piensa qué quieres y qué líneas necesitas. Luego dibuja primero las rectas con regla y después las curvas. Al terminar, cuenta cuántas rectas y cuántas curvas usaste.",
        "Las letras también son combinaciones: la «L» tiene dos rectas, la «O» tiene una curva cerrada y la «S» tiene dos curvas. Puedes buscar letras que usen sólo rectas o sólo curvas.",
    ],
    vocab=[("componer", "armar un dibujo juntando líneas"), ("curva cerrada", "curva que vuelve a su inicio"), ("rayo", "recta que sale de un punto"), ("combinar", "mezclar distintos tipos"), ("figura", "dibujo con forma")],
    worked=[
        {"title": "Un sol", "problem": "Dibuja un sol e identifica las líneas.", "steps": ["Un círculo es una curva cerrada.", "Los rayos son rectas.", "Cuento: 1 curva y 8 rectas si hago 8 rayos."], "answer": "1 curva cerrada y 8 rectas"},
        {"title": "Letras", "problem": "¿Cuántas rectas y curvas tiene la letra «L»?", "steps": ["Una recta vertical.", "Una recta horizontal.", "No hay curvas."], "answer": "2 rectas y 0 curvas"},
    ],
    mistakes=[
        {"wrong": "Contar un círculo como varias líneas.", "why": "Se piensa en trozos.", "fix": "Un círculo es una sola curva cerrada."},
        {"wrong": "Usar sólo curvas para un dibujo con edificios.", "why": "No se analiza la forma.", "fix": "Los edificios necesitan rectas."},
    ],
    tiers={
        "recovery": [ex("¿Cuántas curvas cerradas tiene la letra «O»?", "1", "Es una sola curva."), ex("¿Cuántas rectas tiene la letra «T» mayúscula?", "2", "Una horizontal y una vertical."), ex("¿Cuántas rectas tiene la letra «L» mayúscula?", "2", "Una vertical y una horizontal.")],
        "understand": [
            ex("¿Qué líneas tiene un sol dibujado con rayos?", "Una curva cerrada y rectas", "Círculo y rayos."),
            ex("¿Qué líneas necesita un árbol simple?", "Rectas para el tronco y curvas para las hojas", "Se combinan rectas y curvas."),
            ex("¿Qué tipo de línea es un círculo?", "Curva cerrada", "Vuelve a su inicio."),
        ],
        "apply": [
            ex("Dibuja un pez con rectas y curvas. Cuenta cuántas de cada tipo usaste.", "Por ejemplo: cuerpo con 2 curvas y cola con 2 rectas", "Cada tipo se cuenta aparte."),
            ex("Dibuja la letra «E» mayúscula y cuenta sus rectas.", "4 rectas", "Una vertical y tres horizontales."),
            ex("Dibuja la letra «S» y cuenta sus curvas.", "2 curvas", "Una arriba y otra abajo."),
        ],
        "reason": [
            ex("Marta dice que una casa necesita sólo curvas. ¿Qué error comete?", "Necesita rectas para paredes y techo", "Las paredes son rectas."),
            ex("¿Por qué la letra «O» no tiene rectas?", "Porque es una curva cerrada", "Todo su borde gira."),
        ],
        "challenge": [
            ex("Forma la palabra «OSO» con rectas y curvas. ¿Cuántas curvas hay?", "4", "O (1), S (2) y O (1)."),
            ex("Una figura tiene 3 rectas y 3 curvas. ¿Cuántas líneas tiene en total?", "6", "3 + 3 = 6."),
        ],
    },
    context=[ex("Un niño dibuja un barco con 6 rectas y 2 curvas. ¿Cuántas líneas dibujó?", "8", "6 + 2 = 8.")],
    selfcheck=[ex("¿Cuántas curvas tiene la letra «C»?", "1", "Es una sola curva."), ex("¿Cuántas rectas tiene la letra «H» mayúscula?", "3", "Dos verticales y una horizontal."), ex("¿Se puede dibujar un sol con rectas y curvas?", "Sí", "Círculo y rayos.")],
    open_task=task("Dibuja un animal o una casa combinando rectas y curvas. Cuenta cuántas rectas y cuántas curvas usaste, y escribe la suma total de líneas.", "Dibujé un gato con 5 curvas (cabeza y cuerpo) y 3 rectas (bigotes). Total: 8 líneas.", ["combina rectas y curvas", "cuenta cada tipo", "suma el total"], ["dibujo", "conteo", "suma"], ["contar un círculo como varias", "olvidar el total"], "Pide marcar cada tipo con colores."),
    reinforce="Escribe tu nombre y marca las rectas y las curvas de cada letra.",
    extend="Diseña un logo para tu curso usando tres rectas y tres curvas.",
)

# ---------------------------------------------------------------- OA 16
register(
    OA16, 1,
    materials="Un reloj de tu casa (sólo para observar) y aplausos o pulsos; los eventos están descritos en cada ejercicio.",
    use="Aprenderé a medir cuánto dura algo con una unidad que yo elijo, como aplausos o pulsos. Sirve para comparar cuánto tarda cada cosa.",
    prior=["Sé contar hasta 20.", "Sé qué significa tardar más o menos."],
    explain=[
        "El tiempo se puede medir con una unidad que repites, como un aplauso cada vez. Si aplaudes mientras alguien se pone el abrigo y cuentas 8 aplausos, el evento duró 8 aplausos.",
        "La unidad debe ser siempre la misma y debe repetirse parejo: un aplauso cada vez, a la misma velocidad. Si cambias de unidad o de velocidad, no puedes comparar.",
        "Además de aplausos, puedes usar pulsos de la mano, vasos que se llenan o veces que cae una gota. Lo importante es contar bien y empezar y terminar cuando empieza y termina el evento.",
    ],
    vocab=[("duración", "cuánto tiempo dura algo"), ("unidad", "lo que repito para medir"), ("aplauso", "una palmada"), ("pulso", "un golpecito de la mano dado a ritmo parejo"), ("evento", "algo que ocurre")],
    worked=[
        {"title": "Medir con aplausos", "problem": "Dani se pone el abrigo y cuento 8 aplausos. ¿Cuánto duró?", "steps": ["La unidad es un aplauso.", "Cuento mientras se viste.", "Termina en el aplauso 8."], "answer": "8 aplausos"},
        {"title": "Empezar y terminar bien", "problem": "¿Cuándo empiezo a contar?", "steps": ["Cuando empieza el evento.", "Termino cuando acaba.", "Cuento sin saltar aplausos."], "answer": "Al empezar y hasta que termina el evento"},
    ],
    mistakes=[
        {"wrong": "Contar aplausos a ritmos distintos.", "why": "La unidad no es pareja.", "fix": "Aplaude siempre con el mismo ritmo."},
        {"wrong": "Empezar a contar antes del evento.", "why": "Se pierde el inicio.", "fix": "Comienza cuando el evento empieza."},
    ],
    tiers={
        "recovery": [ex("Una niña camina hasta la puerta y cuento 5 aplausos. ¿Cuánto duró?", "5 aplausos", "Cada aplauso es una unidad."), ex("Un niño dibuja un círculo en 7 aplausos. ¿Cuánto duró?", "7 aplausos", "Cuento la unidad."), ex("Una niña tarda 3 aplausos en cerrar su mochila. ¿Cuánto duró?", "3 aplausos", "La duración es el conteo.")],
        "understand": [
            ex("¿Qué es una unidad de tiempo?", "Lo que repito para medir", "Por ejemplo un aplauso."),
            ex("¿Por qué el ritmo del aplauso debe ser parejo?", "Para que cada unidad dure lo mismo", "Así se puede comparar."),
            ex("¿Cuándo empiezo a contar?", "Cuando empieza el evento", "Así mido toda la duración."),
        ],
        "apply": [
            ex("Luis tardó 12 aplausos en armar una torre. ¿Cuánto duró?", "12 aplausos", "Se mide en aplausos."),
            ex("Sofía tardó 9 aplausos en lavarse las manos. ¿Cuánto duró?", "9 aplausos", "Se mide en aplausos."),
            ex("Camila se ató los cordones en 6 pulsos. ¿Cuánto duró?", "6 pulsos", "La unidad ahora es el pulso."),
        ],
        "reason": [
            ex("Pablo contó 5 aplausos rápidos y su amigo 5 lentos para el mismo evento. ¿Es justo?", "No; las unidades no duran lo mismo", "Hay que usar el mismo ritmo."),
            ex("¿Puedo comparar 8 aplausos con 8 pulsos?", "No; las unidades son distintas", "Cada unidad dura lo suyo."),
        ],
        "challenge": [
            ex("Cuento 4 aplausos para lavarme las manos y 4 más para secarlas. ¿Cuántos en total?", "8 aplausos", "4 + 4 = 8."),
            ex("Un evento dura 10 aplausos. Otro dura 4 menos. ¿Cuánto dura el otro?", "6 aplausos", "10 − 4 = 6."),
        ],
    },
    context=[ex("Mientras la profesora escribe la fecha en la pizarra, cuento 11 aplausos. ¿Cuánto duró?", "11 aplausos", "El conteo es la duración.")],
    selfcheck=[ex("Una unidad de tiempo que puedes usar es...", "Aplausos o pulsos", "Se repiten parejo."), ex("¿Cuándo termino de contar?", "Cuando el evento acaba", "Para medirlo completo."), ex("¿Qué mido con aplausos?", "La duración", "Cuánto tarda algo.")],
    open_task=task("Mide con aplausos tres actividades de tu casa: lavarte las manos, guardar un juguete y beber un vaso de agua. Escribe cuántos aplausos duró cada una y cuál duró más.", "Manos: 9 aplausos. Juguete: 6 aplausos. Agua: 12 aplausos. Duró más beber el agua (12).", ["usa la misma unidad", "cuenta cada evento", "compara con un número"], ["tabla de 3 eventos", "conclusión"], ["ritmo distinto", "no empezar al inicio"], "Pide repetir la medición para ver si da lo mismo."),
    reinforce="Mide con pulsos cuánto tardas en decir tu nombre.",
    extend="Busca otra unidad (como pasos) para medir la duración de recorrer la sala.",
)

register(
    OA16, 2,
    materials="Dos eventos y una unidad común descritos en cada ejercicio; aplausos o pulsos.",
    use="Aprenderé que para comparar dos duraciones debo usar la misma unidad. Sirve para saber cuál evento duró más.",
    prior=["Sé medir una duración con aplausos.", "Sé comparar números."],
    explain=[
        "Para comparar cuánto duran dos eventos, mídelos con la misma unidad. Si uno dura 8 aplausos y el otro 5 aplausos, el primero duró más. Si uno se mide en aplausos y otro en pulsos, no se pueden comparar.",
        "Después de medir, compara los números con cuidado: el mayor número indica el evento que duró más, si la unidad es la misma. La diferencia (8 − 5 = 3) dice cuánto más duró.",
        "Para estar seguro, repite la medición dos veces. Si da casi lo mismo, la medición es confiable. Si cambia mucho, revisa el ritmo del aplauso.",
    ],
    vocab=[("misma unidad", "la misma medida para ambos"), ("comparar", "decir cuál duró más"), ("duró más", "tuvo mayor número de unidades"), ("diferencia", "cuánto más duró uno que otro"), ("confiable", "que se puede creer")],
    worked=[
        {"title": "Misma unidad", "problem": "Ana tardó 8 aplausos y Beto 5 aplausos en vestirse. ¿Quién tardó más?", "steps": ["Los dos usan aplausos.", "8 es mayor que 5.", "Ana tardó más. Diferencia: 8 − 5 = 3."], "answer": "Ana, 3 aplausos más"},
        {"title": "Unidad distinta", "problem": "Un evento dura 8 aplausos y otro 6 pulsos. ¿Cuál duró más?", "steps": ["Las unidades son distintas.", "No se puede comparar directamente."], "answer": "No se puede comparar"},
    ],
    mistakes=[
        {"wrong": "Comparar números con unidades distintas.", "why": "No se fija la unidad.", "fix": "Mide ambos con la misma unidad."},
        {"wrong": "Decir que el número mayor es lo que dura menos.", "why": "Se piensa que más unidades es más rápido.", "fix": "Más unidades significa más duración."},
    ],
    tiers={
        "recovery": [ex("Evento A: 7 aplausos. Evento B: 4 aplausos. ¿Cuál duró más?", "A", "7 es mayor que 4."), ex("Evento A: 3 aplausos. Evento B: 9 aplausos. ¿Cuál duró menos?", "A", "3 es menor que 9."), ex("Evento A: 6 aplausos. Evento B: 6 aplausos. ¿Duraron lo mismo?", "Sí", "Los números son iguales.")],
        "understand": [
            ex("¿Qué necesito para comparar dos duraciones?", "Medirlas con la misma unidad", "Si no, no se comparan."),
            ex("Si uno dura 10 y otro 6 en la misma unidad, ¿cuánto más dura el primero?", "4", "10 − 6 = 4."),
            ex("¿Más unidades significa más o menos duración?", "Más duración", "Se contó más tiempo."),
        ],
        "apply": [
            ex("Armar una torre: 12 aplausos. Armar un puzle: 15 aplausos. ¿Qué duró más?", "El puzle", "15 es mayor que 12."),
            ex("Beber agua: 5 pulsos. Comer una galleta: 8 pulsos. ¿Cuánto más dura comer?", "3 pulsos", "8 − 5 = 3."),
            ex("Atarse un zapato: 7 aplausos. Atarse el otro: 7 aplausos. ¿Cuál duró más?", "Ninguno; duraron lo mismo", "Los dos números son iguales."),
        ],
        "reason": [
            ex("Lola dice que 5 pulsos duran más que 3 aplausos porque 5 es mayor. ¿Qué error comete?", "Las unidades son distintas", "No se pueden comparar."),
            ex("¿Por qué repito la medición?", "Para ver si da lo mismo y confiar en ella", "Si cambia mucho, hay que revisar."),
        ],
        "challenge": [
            ex("Un evento dura 6 aplausos. Otro dura 6 aplausos más. ¿Cuánto dura el otro?", "12 aplausos", "6 + 6 = 12."),
            ex("Dos eventos suman 15 aplausos y uno dura 9. ¿Cuánto dura el otro?", "6", "15 − 9 = 6."),
        ],
    },
    context=[ex("En el recreo, Pedro tardó 14 aplausos en dar una vuelta al patio corriendo y Mari tardó 11. ¿Quién llegó antes y por cuánto?", "Mari; por 3 aplausos", "Menos aplausos es menos tiempo: 14 − 11 = 3.")],
    selfcheck=[ex("12 aplausos y 9 aplausos, ¿cuál duró menos?", "9 aplausos", "9 es menor."), ex("¿Se comparan aplausos con pulsos?", "No", "Las unidades son distintas."), ex("¿Cuánto más es 10 que 7?", "3", "10 − 7 = 3.")],
    open_task=task("Mide con aplausos cuánto tardas en ponerte un zapato y en ponerte una chaqueta. Anota los dos números, escribe cuál duró más y cuánto más.", "Zapato: 6 aplausos. Chaqueta: 10 aplausos. Duró más la chaqueta, 4 aplausos más.", ["usa la misma unidad", "compara con signo o palabra", "calcula la diferencia"], ["dos mediciones", "diferencia"], ["cambiar de unidad", "no calcular la diferencia"], "Pide repetir la medición."),
    reinforce="Compara con aplausos dos actividades de tu rutina.",
    extend="Mide una actividad con aplausos y con pulsos y compara cuántos salen de cada uno.",
)

register(
    OA16, 3,
    materials="Cuatro eventos con sus duraciones en aplausos escritos en cada ejercicio; lápiz.",
    use="Aprenderé a ordenar varios eventos de los que duran menos a los que duran más. Sirve para organizar actividades por su tiempo.",
    prior=["Sé comparar dos duraciones.", "Sé ordenar números hasta 20."],
    explain=[
        "Para ordenar duraciones, mide todos con la misma unidad y ordena los números. De menor a mayor: el primero es el que dura menos y el último el que dura más.",
        "Por ejemplo: lavarse las manos 8 aplausos, guardar un juguete 5, comer una galleta 12, ponerse la chaqueta 10. Ordenados de menos a más: guardar (5), lavarse (8), chaqueta (10), galleta (12).",
        "Puedes hacer una tabla con los eventos y sus aplausos y ordenarla. Al final, comprueba que cada número sea mayor que el anterior, así sabes que no te equivocaste.",
    ],
    vocab=[("ordenar", "poner en fila según un criterio"), ("de menos a más", "del evento más corto al más largo"), ("de más a menos", "del más largo al más corto"), ("más corto", "dura menos"), ("más largo", "dura más")],
    worked=[
        {"title": "Ordenar eventos", "problem": "Ordena de menos a más: lavarse 8, guardar 5, galleta 12, chaqueta 10.", "steps": ["El menor es 5 (guardar).", "Luego 8 (lavarse).", "Luego 10 (chaqueta).", "Último 12 (galleta)."], "answer": "Guardar, lavarse, chaqueta, galleta"},
        {"title": "El más largo", "problem": "¿Cuál es el más largo del ejemplo anterior?", "steps": ["El que tiene más aplausos.", "Es la galleta con 12."], "answer": "Comer la galleta"},
    ],
    mistakes=[
        {"wrong": "Ordenar por el nombre del evento en vez de la duración.", "why": "No se mira el número.", "fix": "Ordena por el número de aplausos."},
        {"wrong": "Invertir el orden.", "why": "No se lee si piden de menos a más o de más a menos.", "fix": "Antes de ordenar, lee el sentido."},
    ],
    tiers={
        "recovery": [ex("Ordena de menos a más: 4, 9, 6 aplausos.", "4, 6, 9", "El menor va primero."), ex("Ordena de más a menos: 3, 8, 5 aplausos.", "8, 5, 3", "El mayor va primero."), ex("¿Cuál es el más corto: 7, 2 o 11 aplausos?", "2 aplausos", "Es el menor.")],
        "understand": [
            ex("¿Qué significa «de menos a más»?", "Del que dura menos al que dura más", "Empieza por el más corto."),
            ex("¿Cuál duró más: 12 o 10 aplausos?", "12", "Es el mayor."),
            ex("¿Con qué unidad debo medir para ordenar?", "La misma para todos", "Así se compara."),
        ],
        "apply": [
            ex("Ordena de menos a más: peinarse 7, lavarse los dientes 9, ponerse zapatos 5, vestirse 14.", "Zapatos, peinarse, dientes, vestirse", "5, 7, 9 y 14."),
            ex("Ordena de más a menos: dibujar 13, borrar 4, pintar 16, recortar 9.", "Pintar, dibujar, recortar, borrar", "16, 13, 9 y 4."),
            ex("De estos eventos (3, 8, 5, 12 aplausos), ¿cuál duró lo mismo que 8 + 4 aplausos?", "El de 12", "8 + 4 = 12."),
        ],
        "reason": [
            ex("Mateo escribió 5, 12, 8 para ordenar de menos a más. ¿Está bien?", "No; es 5, 8, 12", "8 es menor que 12."),
            ex("Ana ordenó por nombre alfabético. ¿Sirve para ordenar duraciones?", "No", "Se ordena por el número."),
        ],
        "challenge": [
            ex("Hay cuatro eventos. Dos duran lo mismo. ¿Cuántas duraciones distintas hay?", "3", "Dos eventos repiten una duración."),
            ex("Tres eventos duran 5, 10 y 15 aplausos. ¿Cuánto dura todo si ocurren uno tras otro?", "30 aplausos", "5 + 10 + 15 = 30."),
        ],
    },
    context=[ex("En la mañana, Sofi tardó: 6 aplausos en peinarse, 15 en desayunar y 9 en vestirse. ¿Qué actividad duró más y cuál menos?", "Desayunar duró más; peinarse duró menos", "15 es mayor y 6 es menor.")],
    selfcheck=[ex("Ordena de menos a más: 8, 3, 6.", "3, 6, 8", "El menor va primero."), ex("El más largo es el que tiene...", "Más aplausos", "Más aplausos es mayor duración."), ex("Ordena de más a menos: 2, 5, 4.", "5, 4, 2", "El mayor va primero.")],
    open_task=task("Mide con aplausos cuatro actividades de tu casa. Anótalas en una tabla y ordénalas de menos a más. Marca la más larga y la más corta.", "Peinarme 6, cepillar dientes 12, guardar libros 8, vestirme 20. Orden: peinarme, libros, dientes, vestirme. Más larga: vestirme. Más corta: peinarme.", ["cuatro actividades con medida", "orden correcto", "marca extremos"], ["tabla", "orden"], ["no usar la misma unidad", "invertir orden"], "Pide comprobar que cada número sea mayor que el anterior."),
    reinforce="Ordena las actividades de tu mañana por su duración.",
    extend="Inventa un evento que dure entre 8 y 12 aplausos y ubícalo en tu orden.",
)

register(
    OA16, 4,
    materials="Un plan de medición descrito en cada ejercicio; aplausos o pulsos.",
    use="Aprenderé a diseñar una medición justa: misma unidad, mismo ritmo, mismo inicio y fin. Sirve para comparar de verdad dos eventos.",
    prior=["Sé medir y comparar duraciones.", "Sé que la unidad debe ser la misma."],
    explain=[
        "Una medición es justa si todos los eventos se miden de la misma manera. Hay cuatro condiciones: misma unidad (aplausos), mismo ritmo (parejo), mismo inicio (cuando comienza) y mismo final (cuando termina).",
        "Si dos niños compiten por armar una torre, ambos deben armar la misma torre y medirse con el mismo ritmo de aplausos. Si una torre es más fácil, la comparación no es justa.",
        "Para diseñar, escribe un plan: qué evento, qué unidad, quién cuenta, cuándo empieza y cuándo termina. Después mide y revisa si algo hizo la comparación injusta.",
    ],
    vocab=[("justa", "que trata igual a todos"), ("plan", "pasos escritos antes de hacer"), ("condición", "algo que se debe cumplir"), ("inicio", "cuando comienza"), ("final", "cuando termina")],
    worked=[
        {"title": "Una medición justa", "problem": "Dos niños arman la misma torre de 6 cubos. Cuento aplausos a ritmo parejo para cada uno. ¿Es justa?", "steps": ["Misma torre.", "Misma unidad y ritmo.", "Mismo inicio y fin."], "answer": "Sí, es justa"},
        {"title": "Una medición injusta", "problem": "Uno arma una torre de 4 cubos y el otro una de 8. ¿Es justa la comparación?", "steps": ["Las torres son distintas.", "El segundo tiene más trabajo."], "answer": "No es justa"},
    ],
    mistakes=[
        {"wrong": "Medir a uno con aplausos y a otro con pasos.", "why": "La unidad no es la misma.", "fix": "Usa la misma unidad para todos."},
        {"wrong": "Cambiar el ritmo entre mediciones.", "why": "No se mantiene el ritmo.", "fix": "Practica un ritmo parejo antes de medir."},
    ],
    tiers={
        "recovery": [ex("¿Qué debe ser igual en una medición justa: la unidad o el color del lápiz?", "La unidad", "Es la condición clave."), ex("¿Qué debe ser igual: el ritmo o el nombre del niño?", "El ritmo", "Sirve para comparar."), ex("¿Debe empezar el conteo al inicio del evento?", "Sí", "Para medirlo entero.")],
        "understand": [
            ex("¿Cuántas condiciones tiene una medición justa?", "4", "Unidad, ritmo, inicio y final."),
            ex("¿Es justo comparar una torre de 4 cubos con otra de 8?", "No", "El trabajo no es igual."),
            ex("¿Qué escribo en un plan de medición?", "Evento, unidad, quién cuenta, inicio y final", "Así todos miden igual."),
        ],
        "apply": [
            ex("Diseña un plan para comparar quién se lava más rápido las manos.", "Misma cantidad de jabón, misma unidad, mismo inicio al abrir la llave y fin al cerrarla", "Se cuidan las condiciones."),
            ex("Dos niños arman un puzle de 10 piezas. ¿Qué debes cuidar?", "Que sea el mismo puzle y contar con el mismo ritmo", "Así es justa."),
            ex("Un niño midió con aplausos y otro con pulsos. ¿Qué cambian para ser justos?", "Usar la misma unidad", "Ambos aplausos o ambos pulsos."),
        ],
        "reason": [
            ex("Lucía dice que la torre del que terminó antes es más fácil. ¿Qué debería revisar?", "Que ambos tengan la misma torre", "Si no, la comparación no es justa."),
            ex("¿Por qué conviene decidir de antemano cuándo termina el evento?", "Para que todos midan lo mismo", "Así se evitan dudas al medir."),
        ],
        "challenge": [
            ex("Escribe un plan completo para comparar quién guarda más rápido 5 libros.", "Mismos 5 libros, misma unidad, ritmo parejo, inicio al tocar el primero y final al soltar el último", "Cumple las cuatro condiciones."),
            ex("Dos niños tardaron 7 y 10 aplausos en un evento justo. ¿Cuánto más tardó el segundo?", "3 aplausos", "10 − 7 = 3."),
        ],
    },
    context=[ex("En el patio, dos niños corren de una línea a otra. Uno parte antes. ¿Es justa la medición? ¿Cómo arreglarla?", "No; deben partir al mismo tiempo", "Deben partir en el mismo momento.")],
    selfcheck=[ex("¿Qué es una medición justa?", "La que trata igual a todos", "Todos se miden en las mismas condiciones."), ex("¿Qué debe ser igual: el evento o la persona?", "El evento", "Se compara el mismo trabajo."), ex("¿Se puede cambiar el ritmo a mitad de la medición?", "No", "Debe ser parejo.")],
    open_task=task("Diseña un plan para comparar quién de tus dos familiares se demora menos en guardar 6 juguetes. Escribe la unidad, el ritmo, cómo empiezan y cómo terminan y qué cuidarás para que sea justo. Si puedes, mídelo y anota los números.", "Unidad: aplausos a ritmo parejo. Ambos guardan los mismos 6 juguetes. Empiezan al decir «ya» y terminan al soltar el último. Resultados: 12 y 9 aplausos.", ["plan con las cuatro condiciones", "mismos juguetes", "resultados con la misma unidad"], ["plan", "mediciones"], ["distintos juguetes", "inicio desparejo"], "Pide revisar el plan con otra persona."),
    reinforce="Mide dos veces la misma actividad y compara los números.",
    extend="Propón un plan para comparar tres actividades de un día.",
)

# ---------------------------------------------------------------- OA 17
register(
    OA17, 1,
    materials="Tarjetas con rutinas de un día (despertar, desayunar, ir al colegio) descritas en cada ejercicio.",
    use="Aprenderé a ordenar lo que hago en un día usando antes, durante y después. Sirve para organizar mi rutina.",
    prior=["Sé qué es una rutina.", "Sé decir primero y luego."],
    explain=[
        "Los eventos ocurren en un orden en el tiempo. Lo primero que pasa es el comienzo; lo último es el final. Para ordenar, usa las palabras antes, durante, después, primero, luego y al final.",
        "Antes significa que ya ocurrió: antes de ir al colegio, desayuno. Durante significa que ocurre al mismo tiempo: durante la clase, escribimos. Después significa que viene más tarde: después del recreo, volvemos a la sala.",
        "Para ordenar una rutina, haz una lista con números: 1, 2, 3. Pregúntate qué sucede primero y qué se necesita para el siguiente paso. Así no te equivocas.",
    ],
    vocab=[("rutina", "lo que hago cada día"), ("antes", "ya ocurrió"), ("después", "ocurre más tarde"), ("durante", "ocurre al mismo tiempo"), ("orden", "primero, segundo, tercero")],
    worked=[
        {"title": "Ordenar una rutina", "problem": "Ordena: ir al colegio, despertar, desayunar.", "steps": ["Primero despierto.", "Luego desayuno.", "Después voy al colegio."], "answer": "Despertar, desayunar, ir al colegio"},
        {"title": "Antes y después", "problem": "¿Qué ocurre antes de desayunar?", "steps": ["Desayuno después de despertar.", "Antes de desayunar, me despierto."], "answer": "Despertar"},
    ],
    mistakes=[
        {"wrong": "Poner almorzar antes de desayunar.", "why": "No se piensa en el orden del día.", "fix": "Desayuno va en la mañana; almuerzo, al mediodía."},
        {"wrong": "Usar «durante» para algo que ya pasó.", "why": "Se confunden las palabras.", "fix": "Durante es al mismo tiempo; antes ya pasó."},
    ],
    tiers={
        "recovery": [ex("¿Qué pasa primero: despertar o desayunar?", "Despertar", "Hay que estar despierto para desayunar."), ex("¿Qué pasa después: almorzar o ir a dormir?", "Ir a dormir", "Dormir ocurre de noche."), ex("¿Qué pasa antes de ir al colegio: desayunar o volver a casa?", "Desayunar", "Volver a casa es después.")],
        "understand": [
            ex("¿Qué significa «después»?", "Más tarde", "Después ocurre más tarde."),
            ex("¿Qué significa «antes»?", "Ya ocurrió", "Antes pasó primero."),
            ex("¿Qué significa «durante»?", "Al mismo tiempo", "Mientras ocurre otra cosa."),
        ],
        "apply": [
            ex("Ordena: ir al colegio, despertar, volver a casa, desayunar.", "Despertar, desayunar, ir al colegio, volver a casa", "Primero la mañana y después el regreso."),
            ex("Ordena: ir a dormir, despertar, almorzar, cenar.", "Despertar, almorzar, cenar, ir a dormir", "Es el orden de un día."),
            ex("¿Qué puedes hacer durante el recreo?", "Por ejemplo, jugar", "Ocurre al mismo tiempo que el recreo."),
        ],
        "reason": [
            ex("Pía dice que se duerme antes de cenar. ¿Es el orden habitual?", "No; primero se cena", "La cena va antes de dormir."),
            ex("¿Por qué conviene numerar una rutina?", "Para no equivocar el orden", "Cada número es un lugar."),
        ],
        "challenge": [
            ex("Ordena estas cuatro acciones de la noche: ponerse pijama, dormir, cenar, apagar la luz.", "Cenar, ponerse pijama, apagar la luz, dormir", "Dormir es lo último."),
            ex("Primero me despierto, después me visto y al final desayuno. ¿Qué hago entre despertar y desayunar?", "Me visto", "Está en el medio."),
        ],
    },
    context=[ex("Una niña se despertó, se vistió, desayunó y se fue al colegio. ¿Qué hizo antes de desayunar?", "Se despertó y se vistió", "Esos pasos fueron antes.")],
    selfcheck=[ex("¿Qué va primero: despertar o vestirse?", "Despertar", "Hay que estar despierto para vestirse."), ex("¿Qué significa «luego»?", "Más tarde", "Luego quiere decir después."), ex("¿Qué usas para ordenar una rutina?", "Números", "1, 2, 3...")],
    open_task=task("Ordena tu rutina de la mañana con cuatro actividades (por ejemplo despertar, vestirse, desayunar, ir al colegio). Numéralas y dibuja una al lado de cada número. Usa antes y después en dos frases.", "1 despertar, 2 vestirme, 3 desayunar, 4 ir al colegio. Antes de desayunar me visto. Después de desayunar voy al colegio.", ["cuatro actividades ordenadas", "dibuja cada una", "usa antes y después"], ["lista", "dibujos", "frases"], ["orden ilógico", "no usar las palabras pedidas"], "Pide contar la rutina a otra persona."),
    reinforce="Cuenta tu día con las palabras primero, luego y al final.",
    extend="Ordena la rutina de un fin de semana y compárala con la de un día de colegio.",
)

register(
    OA17, 2,
    materials="Un calendario de una semana descrito en cada ejercicio; lápiz.",
    use="Aprenderé el orden de los días de la semana. Sirve para saber qué día viene y planear actividades.",
    prior=["Sé ordenar una rutina.", "Sé contar hasta 7."],
    explain=[
        "La semana tiene 7 días: lunes, martes, miércoles, jueves, viernes, sábado y domingo. Después del domingo vuelve a comenzar con el lunes. Es un ciclo que se repite.",
        "Para encontrar el día siguiente, recuerda el orden: después del martes viene el miércoles. Para el día anterior, vuelve uno atrás: antes del jueves está el miércoles. Hoy, mañana y ayer cambian cada día.",
        "Hay días de colegio (de lunes a viernes) y días de descanso (sábado y domingo). Puedes marcar en un calendario los días de actividades para recordarlos y preparar con tiempo lo que necesitas.",
    ],
    vocab=[("semana", "7 días seguidos"), ("ayer", "el día anterior a hoy"), ("hoy", "el día en que estamos"), ("mañana", "el día siguiente a hoy"), ("ciclo", "algo que vuelve a empezar")],
    worked=[
        {"title": "El día siguiente", "problem": "¿Qué día viene después del miércoles?", "steps": ["El orden es lunes, martes, miércoles, jueves.", "Después del miércoles viene el jueves."], "answer": "Jueves"},
        {"title": "Después del domingo", "problem": "¿Qué día viene después del domingo?", "steps": ["El domingo es el último de la semana.", "Vuelve a comenzar con el lunes."], "answer": "Lunes"},
    ],
    mistakes=[
        {"wrong": "Empezar a contar la semana desde el sábado.", "why": "No se sigue el orden del calendario.", "fix": "En este cuaderno la semana va de lunes a domingo."},
        {"wrong": "Saltarse un día.", "why": "No se recita el orden completo.", "fix": "Recita todos los días en voz alta."},
    ],
    tiers={
        "recovery": [ex("¿Qué día viene después del lunes?", day_after("lunes"), "Es el siguiente."), ex("¿Qué día viene después del viernes?", day_after("viernes"), "Es el siguiente."), ex("¿Qué día viene antes del jueves?", day_after("jueves", -1), "Es el anterior.")],
        "understand": [
            ex("¿Cuántos días tiene una semana?", "7", "De lunes a domingo."),
            ex("¿Cuál es el último día de la semana en este calendario?", "Domingo", "Después vuelve el lunes."),
            ex("Si hoy es martes, ¿qué día es mañana?", day_after("martes"), "El día siguiente."),
        ],
        "apply": [
            ex("Si hoy es sábado, ¿qué día es mañana?", day_after("sábado"), "Después del sábado viene el domingo."),
            ex("Si hoy es miércoles, ¿qué día fue ayer?", day_after("miércoles", -1), "El día anterior."),
            ex("Si hoy es jueves, ¿qué día será dentro de 3 días?", day_after("jueves", 3), "Viernes, sábado y domingo."),
        ],
        "reason": [
            ex("Mateo dice que después del domingo viene el sábado. ¿Qué error comete?", "Viene el lunes", "La semana vuelve a empezar."),
            ex("¿Por qué lunes a viernes son días de colegio y sábado y domingo no?", "Porque son días de descanso", "Es la organización de la semana escolar."),
        ],
        "challenge": [
            ex("Hoy es lunes. ¿Qué día será dentro de 7 días?", "Lunes", "Una semana completa vuelve al mismo día."),
            ex("Hoy es viernes. ¿Cuántos días faltan para el lunes?", "3", "Sábado, domingo y lunes."),
        ],
    },
    context=[ex("Tengo educación física los martes y los jueves. Hoy es lunes. ¿Cuántos días faltan para mi próxima clase?", "1", "Mañana es martes.")],
    selfcheck=[ex("¿Qué día viene después del jueves?", day_after("jueves"), "Es el siguiente."), ex("¿Qué día viene antes del domingo?", day_after("domingo", -1), "Es el anterior."), ex("¿Cuántos días de descanso tiene la semana escolar?", "2", "Sábado y domingo.")],
    open_task=task("Dibuja una tabla de la semana con los 7 días en orden. Marca con colores los días de colegio y los de descanso y escribe una actividad que haces cada día.", "Lunes a viernes (colegio): lunes tareas, martes educación física, miércoles música, jueves lectura, viernes juego. Sábado: plaza. Domingo: familia.", ["siete días en orden", "marca colegio y descanso", "una actividad por día"], ["tabla", "colores", "actividades"], ["saltarse un día", "orden equivocado"], "Pide recitar los días y señalar cada uno."),
    reinforce="Canta los días de la semana en orden tres veces.",
    extend="Averigua qué día será dentro de 10 días a partir de hoy.",
)

register(
    OA17, 3,
    materials="Un calendario de un año descrito en cada ejercicio; lápiz.",
    use="Aprenderé el orden de los meses del año. Sirve para saber en qué mes ocurren las cosas y planear el año.",
    prior=["Sé los días de la semana.", "Sé contar hasta 12."],
    explain=[
        "El año tiene 12 meses: enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre y diciembre. Después de diciembre vuelve a empezar enero. Es otro ciclo.",
        "Para encontrar el mes siguiente, recuerda el orden: después de marzo viene abril. Para el mes anterior, vuelve uno atrás: antes de julio está junio. Un mes tiene muchas semanas y días.",
        "Las estaciones van cambiando durante el año. Puedes marcar en una tabla de 12 casillas qué pasa cada mes: cumpleaños, vacaciones, fiestas. Así organizas el año completo y ves cuánto falta para cada celebración.",
    ],
    vocab=[("mes", "una parte del año con varias semanas"), ("año", "12 meses seguidos"), ("calendario", "tabla con los meses y los días"), ("estación", "parte del año con clima propio"), ("ciclo", "algo que se repite")],
    worked=[
        {"title": "Mes siguiente", "problem": "¿Qué mes viene después de marzo?", "steps": ["El orden: enero, febrero, marzo, abril.", "Después de marzo viene abril."], "answer": "Abril"},
        {"title": "Fin del año", "problem": "¿Qué mes viene después de diciembre?", "steps": ["Diciembre es el último.", "Vuelve a empezar con enero."], "answer": "Enero"},
    ],
    mistakes=[
        {"wrong": "Saltarse un mes.", "why": "No se recita completo.", "fix": "Recita todos los meses en orden."},
        {"wrong": "Pensar que un año tiene 10 meses.", "why": "Se confunde con la decena.", "fix": "Un año tiene 12 meses."},
    ],
    tiers={
        "recovery": [ex("¿Qué mes viene después de enero?", month_after("enero"), "Es el siguiente."), ex("¿Qué mes viene después de junio?", month_after("junio"), "Es el siguiente."), ex("¿Qué mes viene antes de octubre?", month_after("octubre", -1), "Es el anterior.")],
        "understand": [
            ex("¿Cuántos meses tiene un año?", "12", "De enero a diciembre."),
            ex("¿Cuál es el primer mes?", "Enero", "Comienza el año."),
            ex("¿Cuál es el último mes?", "Diciembre", "Termina el año."),
        ],
        "apply": [
            ex("¿Qué mes viene después de agosto?", month_after("agosto"), "Es el siguiente."),
            ex("¿Qué mes viene antes de mayo?", month_after("mayo", -1), "Es el anterior."),
            ex("¿Qué mes será 3 meses después de noviembre?", month_after("noviembre", 3), "Diciembre, enero y febrero."),
        ],
        "reason": [
            ex("Ema dice que después de diciembre viene noviembre. ¿Qué error comete?", "Viene enero", "El año vuelve a empezar."),
            ex("¿Por qué conviene una tabla de 12 casillas para el año?", "Porque hay 12 meses", "Una casilla por mes."),
        ],
        "challenge": [
            ex("Mi cumpleaños es en abril. ¿Cuántos meses faltan desde enero?", "3", "Febrero, marzo y abril."),
            ex("¿Cuántos meses hay entre marzo y septiembre sin contarlos?", "5", "Abril, mayo, junio, julio y agosto."),
        ],
    },
    context=[ex("El colegio empieza en marzo y las vacaciones de invierno son en julio. ¿Cuántos meses hay entre marzo y julio sin contarlos?", "3", "Abril, mayo y junio.")],
    selfcheck=[ex("¿Qué mes viene después de septiembre?", month_after("septiembre"), "Es el siguiente."), ex("¿Qué mes viene antes de febrero?", month_after("febrero", -1), "Es el anterior."), ex("¿Cuántas casillas necesita una tabla con todos los meses?", "12", "Una casilla por cada mes.")],
    open_task=task("Dibuja una tabla de 12 casillas con los meses del año en orden. Escribe en cada casilla algo que ocurre ese mes (cumpleaños, fiesta, vacaciones). Marca tu mes de cumpleaños.", "Enero: vacaciones. Febrero: playa. Marzo: inicio de clases... Septiembre: fiestas patrias... Diciembre: Navidad. Mi cumpleaños: abril.", ["12 meses en orden", "una actividad por mes", "marca su cumpleaños"], ["tabla", "marca"], ["saltar un mes", "orden equivocado"], "Pide recitar los meses señalando cada casilla."),
    reinforce="Recita los meses en voz alta señalando un calendario.",
    extend="Averigua qué mes será dentro de 5 meses a partir de hoy.",
)

register(
    OA17, 4,
    materials="Un calendario de Chile descrito en cada ejercicio: 1 de enero, 21 de mayo, 18 de septiembre, 25 de diciembre; lápiz.",
    use="Aprenderé a leer fechas escritas y a ubicar algunas fechas significativas de Chile. Sirve para entender un calendario y recordar celebraciones.",
    prior=["Sé los días y los meses.", "Sé leer números del 1 al 31."],
    explain=[
        "Una fecha tiene un número y un mes: «18 de septiembre» es el día 18 del mes de septiembre. El número dice el día del mes y el mes dice dónde está en el año. A veces se agrega el día de la semana.",
        "En Chile hay fechas importantes: el 1 de enero es Año Nuevo, el 21 de mayo se recuerda el Combate Naval de Iquique (Glorias Navales), el 18 de septiembre se celebra la Independencia (Fiestas Patrias) y el 25 de diciembre es Navidad. Cada una se ubica en su mes.",
        "Para leer una fecha, busca primero el mes en el calendario, luego el número. Para ordenar fechas, mira primero el mes y, si es el mismo, el número del día.",
    ],
    vocab=[("fecha", "día y mes de un suceso"), ("significativa", "importante para las personas"), ("Año Nuevo", "1 de enero"), ("Fiestas Patrias", "18 de septiembre"), ("Navidad", "25 de diciembre")],
    worked=[
        {"title": "Leer una fecha", "problem": "Lee «18 de septiembre».", "steps": ["El número es 18: es el día.", "El mes es septiembre.", "Es el día 18 del mes de septiembre."], "answer": "Día 18, mes septiembre"},
        {"title": "Ordenar fechas", "problem": "Ordena de la primera a la última: 25 de diciembre, 1 de enero, 18 de septiembre.", "steps": ["Enero es el primer mes.", "Septiembre viene después.", "Diciembre es el último."], "answer": "1 de enero, 18 de septiembre, 25 de diciembre"},
    ],
    mistakes=[
        {"wrong": "Leer «18 de septiembre» como mes 18.", "why": "Se confunden día y mes.", "fix": "El número es el día y el nombre es el mes."},
        {"wrong": "Ordenar por el día y no por el mes.", "why": "Se mira el primer número.", "fix": "Primero ordena por mes."},
    ],
    tiers={
        "recovery": [ex("En «21 de mayo», ¿cuál es el mes?", "Mayo", "Va después de «de»."), ex("En «21 de mayo», ¿cuál es el día?", "21", "Es el número."), ex("¿Qué mes es el de Navidad?", "Diciembre", "Se celebra el 25 de diciembre.")],
        "understand": [
            ex("¿Qué fecha es Año Nuevo?", "1 de enero", "Comienza el año."),
            ex("¿Qué se celebra el 18 de septiembre?", "Las Fiestas Patrias", "Es la Independencia de Chile."),
            ex("¿Qué mes viene primero: mayo o septiembre?", "Mayo", "Está antes en el año."),
        ],
        "apply": [
            ex("Ordena de la primera a la última: 21 de mayo, 25 de diciembre, 1 de enero, 18 de septiembre.", "1 de enero, 21 de mayo, 18 de septiembre, 25 de diciembre", "Se ordena por mes."),
            ex("¿Cuántos meses hay entre el 1 de enero y el 18 de septiembre sin contar los extremos?", "7", "Febrero a agosto."),
            ex("Escribe la fecha de tu cumpleaños con día y mes.", "Por ejemplo, 12 de abril", "Número y mes."),
        ],
        "reason": [
            ex("Luis dice que 25 de diciembre viene antes que 1 de enero. ¿Tiene razón?", "No; el 1 de enero viene antes dentro del mismo año", "Enero es el primer mes."),
            ex("¿Por qué dos fechas con el mismo número pueden ser distintas?", "Porque están en meses distintos", "El mes cambia la fecha."),
        ],
        "challenge": [
            ex("¿Cuántos meses pasan entre el 21 de mayo y el 25 de diciembre sin contar los extremos?", "6", "Junio a noviembre."),
            ex("Si hoy es 17 de septiembre, ¿qué fecha es mañana?", "18 de septiembre", "El día siguiente."),
        ],
    },
    context=[ex("El curso hace un acto el 18 de septiembre. Si hoy es 15 de septiembre, ¿cuántos días faltan?", "3", "16, 17 y 18.")],
    selfcheck=[ex("¿Qué mes es el 1 de enero?", "Enero", "Es el primer mes."), ex("¿Qué fecha es Navidad?", "25 de diciembre", "Es el último mes."), ex("¿Se ordena primero por día o por mes?", "Por mes", "El mes decide la época del año.")],
    open_task=task("Dibuja un calendario con las cuatro fechas (1 de enero, 21 de mayo, 18 de septiembre y 25 de diciembre) en orden. Escribe al lado de cada fecha qué se celebra y cuántos meses hay entre cada una y la siguiente, sin contar los extremos.", "1 de enero: Año Nuevo. Entre el 1 de enero y el 21 de mayo hay 3 meses (febrero, marzo y abril). 21 de mayo: Glorias Navales. Entre el 21 de mayo y el 18 de septiembre hay 3 meses. 18 de septiembre: Fiestas Patrias. Entre el 18 de septiembre y el 25 de diciembre hay 2 meses. 25 de diciembre: Navidad.", ["cuatro fechas en orden", "dice qué se celebra", "cuenta los meses que hay entre fechas"], ["calendario", "frases", "diferencias"], ["ordenar por el día", "contar mal los meses"], "Pide recitar las fechas y contar los meses con los dedos."),
    reinforce="Lee en voz alta cinco fechas de tu calendario.",
    extend="Averigua otra fecha significativa de tu familia o tu comunidad y ubícala.",
)

# ---------------------------------------------------------------- OA 18
register(
    OA18, 1,
    materials="Objetos de la sala (lápiz, goma, cuaderno, regla) descritos en cada ejercicio.",
    use="Aprenderé a describir si un objeto es largo o corto. Sirve para elegir lo que necesito y hablar de tamaños.",
    prior=["Sé nombrar objetos.", "Sé comparar cantidades."],
    explain=[
        "La longitud es lo largo que es algo. Las palabras largo y corto sirven para describirla. Un lápiz nuevo es largo y una goma es corta. Un riel de cortina es largo y una tecla es corta.",
        "Largo y corto siempre se dicen respecto de otro objeto: un lápiz es largo comparado con una goma, pero corto comparado con una regla. Por eso hay que decir «más largo que» o «más corto que».",
        "Para decidir cuál es más largo, ponlos lado a lado, con un extremo alineado, y mira cuál sobresale. El que sobresale es el más largo. También puedes decir cuánto mide algo contando cubitos iguales puestos en fila: un lápiz de 18 cubitos es más largo que una goma de 5 cubitos.",
    ],
    vocab=[("longitud", "lo largo que es algo"), ("largo", "que mide mucho"), ("corto", "que mide poco"), ("más largo que", "que mide más que otro"), ("más corto que", "que mide menos que otro")],
    worked=[
        {"title": "Describir", "problem": "Un lápiz mide más que una goma. ¿Cuál es más largo?", "steps": ["Los comparo.", "El lápiz sobresale.", "El lápiz es más largo."], "answer": "El lápiz"},
        {"title": "Respecto de otro", "problem": "El lápiz, ¿es largo o corto?", "steps": ["Depende de con qué se compare.", "Frente a una goma es largo; frente a una regla es corto."], "answer": "Depende del objeto con que se compare"},
    ],
    mistakes=[
        {"wrong": "Decir que algo es largo sin compararlo.", "why": "Largo y corto son relativos.", "fix": "Di «más largo que»."},
        {"wrong": "Comparar sin alinear.", "why": "Un extremo puede engañar.", "fix": "Alinea un extremo antes de comparar."},
    ],
    tiers={
        "recovery": [ex("Un lápiz y una goma: ¿cuál es más largo?", "El lápiz", "El lápiz mide más que la goma."), ex("Una regla de 30 cubitos y un lápiz de 15 cubitos: ¿cuál es más corto?", "El lápiz", "Ese objeto mide menos que el otro."), ex("Un riel de cortina y un botón: ¿cuál es largo?", "El riel", "El riel mide mucho más.")],
        "understand": [
            ex("¿Qué palabras usamos para hablar de la longitud?", "Largo y corto", "Describen cuánto mide."),
            ex("¿Es un lápiz siempre largo?", "No; depende con qué se compare", "Largo es relativo."),
            ex("¿Qué hago para comparar dos objetos?", "Los pongo lado a lado alineando un extremo", "Así veo cuál sobresale."),
        ],
        "apply": [
            ex("Un lápiz mide 18 cubitos y un cuaderno mide 24 cubitos de alto. ¿Cuál es más largo?", "El cuaderno", "24 es mayor que 18."),
            ex("Una cuchara mide 16 cubitos y un tenedor 17 cubitos. ¿Cuál es más largo?", "El tenedor", "17 es mayor que 16."),
            ex("Un hilo de 20 cubitos y uno de 10 cubitos. ¿Cuál es más corto?", "El de 10 cubitos", "10 < 20."),
        ],
        "reason": [
            ex("Pedro dice que su lápiz es largo. ¿Qué debe agregar?", "Más largo que qué", "Largo es relativo."),
            ex("¿Por qué hay que alinear un extremo?", "Para que la comparación sea justa", "Si no, parece que uno es más largo."),
        ],
        "challenge": [
            ex("Un palito mide más que otro y menos que un tercero. ¿Cuál es el más largo de los tres?", "El tercero", "El del medio mide menos que él."),
            ex("Dos objetos miden 12 cubitos y 9 cubitos. ¿Cuánto más largo es el primero?", "3 cubitos", "12 − 9 = 3."),
        ],
    },
    context=[ex("En una tienda hay dos cintas: una de 30 cubitos y otra de 18 cubitos. ¿Cuál es más corta?", "La de 18 cubitos", "18 < 30.")],
    selfcheck=[ex("¿Cuál es más corto: una cuerda de 15 cubitos o una de 8 cubitos?", "La de 8 cubitos", "Ese objeto mide menos que el otro."), ex("¿Cómo comparo dos longitudes?", "Alineando un extremo", "Veo cuál sobresale."), ex("¿Largo es relativo?", "Sí", "Depende de otro objeto.")],
    open_task=task("Elige tres objetos de tu casa (por ejemplo, lápiz, regla y cuchara). Compáralos de a pares alineándolos y escribe tres frases: «X es más largo que Y» o «X es más corto que Y».", "El lápiz es más largo que la cuchara. La regla es más larga que el lápiz. La cuchara es más corta que la regla.", ["compara de a pares", "alinea", "escribe tres frases coherentes"], ["tres frases", "demostración"], ["comparar sin alinear", "frases contradictorias"], "Pide demostrar con los objetos."),
    reinforce="Compara tus dedos entre sí: ¿cuál es el más largo?",
    extend="Busca un objeto largo y uno corto en tu casa y descríbelos.",
)

register(
    OA18, 2,
    materials="Dos objetos para alinear en cada ejercicio (lápices, palitos o cintas); una mesa plana.",
    use="Aprenderé a comparar longitudes alineando los objetos por un extremo. Sirve para saber con seguridad cuál es más largo.",
    prior=["Sé qué es largo y corto.", "Sé usar más largo que y más corto que."],
    explain=[
        "Para comparar dos longitudes con seguridad, alinea los objetos: pon uno junto al otro con un extremo en la misma línea. El que sobresale en el otro extremo es el más largo. Si no sobresale ninguno, tienen la misma longitud.",
        "Si no alineas, puedes equivocarte. Un palito más corto puede parecer más largo si lo pones más adelante. Por eso la línea de salida debe ser la misma.",
        "Anota tu conclusión con las palabras más largo que, más corto que o igual de largo que. Si hay dudas, repite la comparación con calma y fíjate bien en dónde empieza cada objeto.",
    ],
    vocab=[("alinear", "poner en la misma línea de salida"), ("sobresalir", "pasarse del otro"), ("extremo", "punta del objeto"), ("igual de largo", "tienen la misma longitud"), ("línea de salida", "donde empiezan los dos")],
    worked=[
        {"title": "Alinear", "problem": "Un lápiz y un palito se alinean. El lápiz sobresale. ¿Cuál es más largo?", "steps": ["Alineo un extremo.", "El lápiz sobresale.", "El lápiz es más largo."], "answer": "El lápiz"},
        {"title": "Igual de largo", "problem": "Dos palitos alineados no sobresalen. ¿Qué concluyo?", "steps": ["Ninguno de los dos sobresale.", "Miden lo mismo."], "answer": "Igual de largos"},
    ],
    mistakes=[
        {"wrong": "No alinear y adelantar un objeto.", "why": "El extremo engaña.", "fix": "Pon ambos en la misma línea de salida."},
        {"wrong": "Decir más largo al que está más lejos.", "why": "Se confunde posición con longitud.", "fix": "Compara sólo después de alinear."},
    ],
    tiers={
        "recovery": [ex("Dos cintas alineadas: A sobresale. ¿Cuál es más larga?", "A", "La cinta A sobresale."), ex("Dos cintas alineadas: ninguna sobresale. ¿Qué concluyes?", "Son igual de largas", "No hay diferencia."), ex("Dos palitos alineados: B no sobresale y A sí. ¿Cuál es más corto?", "B", "El palito B no sobresale.")],
        "understand": [
            ex("¿Qué es alinear?", "Poner en la misma línea de salida", "Para comparar parejo."),
            ex("¿Por qué no basta con mirar sin alinear?", "Porque un objeto adelantado parece más largo", "Se compara mal."),
            ex("¿Qué significa «igual de largo que»?", "Que miden lo mismo", "Ninguno de los dos sobresale."),
        ],
        "apply": [
            ex("Un lápiz mide 14 cubitos y una regla 30 cubitos. Escribe la frase de comparación.", "El lápiz es más corto que la regla", "14 es menor que 30."),
            ex("Alineas un zapato de 20 cubitos con uno de 18 cubitos. ¿Cuál sobresale?", "El de 20 cubitos", "Es el más largo."),
            ex("Dos cuerdas de 15 cubitos y 15 cubitos. ¿Qué concluyes al alinearlas?", "Son igual de largas", "15 = 15."),
        ],
        "reason": [
            ex("Ana adelantó un palito para que pareciera más largo. ¿Cómo lo corriges?", "Alineándolos", "Así se ve la diferencia real."),
            ex("Si A es más largo que B y B es más largo que C, ¿cuál es más corto?", "C", "Es el menor."),
        ],
        "challenge": [
            ex("Alineas tres palitos y sobresalen en este orden: el primero 3 cubitos más que el segundo y el segundo 2 cubitos más que el tercero. ¿Cuánto más largo es el primero que el tercero?", "5 cubitos", "3 + 2 = 5."),
            ex("Dos palitos alineados: uno mide 8 cubitos y el otro 5 cubitos. ¿Cuánto sobresale el más largo?", "3 cubitos", "8 − 5 = 3."),
        ],
    },
    context=[ex("Para elegir el lápiz más largo entre dos, un niño los pone uno frente al otro con la punta del mismo lado. ¿Hizo bien?", "Sí; alineó", "Así compara parejo.")],
    selfcheck=[ex("¿Qué debes hacer antes de comparar?", "Alinear", "Para comparar parejo."), ex("Si nada sobresale, ¿qué concluyes?", "Son igual de largos", "No hay diferencia."), ex("El que sobresale es...", "El más largo", "Pasa al otro.")],
    open_task=task("Compara tres objetos de tu casa alineándolos dos a dos. Escribe las tres comparaciones y ordénalos de más largo a más corto.", "Lápiz vs cuchara: el lápiz sobresale. Cuchara vs tenedor: iguales. Lápiz vs tenedor: el lápiz sobresale. Orden: lápiz, cuchara y tenedor (iguales).", ["alinea", "tres comparaciones", "ordena"], ["comparaciones", "orden"], ["no alinear", "orden inconsistente"], "Pide demostrar con los objetos."),
    reinforce="Compara tus pies descalzos alineando los talones.",
    extend="Busca dos objetos que sean igual de largos y comprueba alineándolos.",
)

register(
    OA18, 3,
    materials="Tres objetos para ordenar en cada ejercicio (lápiz, regla, cuchara u otros); una mesa plana.",
    use="Aprenderé a ordenar tres longitudes del más corto al más largo. Sirve para organizar objetos por su largo.",
    prior=["Sé comparar dos longitudes alineando.", "Sé ordenar tres números."],
    explain=[
        "Para ordenar tres objetos por longitud, compara de a dos. Primero compara el objeto 1 con el 2, luego el 2 con el 3 y finalmente el 1 con el 3 si es necesario. Con eso encuentras el orden.",
        "El orden de más corto a más largo (de menor a mayor longitud) pone primero el que sobresale menos. Si ordenas del más largo al más corto, ocurre al revés.",
        "Después de ordenar, comprueba: alinea los tres por un extremo y mira que cada uno sobresalga más que el anterior. Si algo no calza, revisa las comparaciones de a dos y corrige el orden.",
    ],
    vocab=[("ordenar", "poner en fila según la longitud"), ("más corto", "el que mide menos"), ("más largo", "el que mide más"), ("el del medio", "el que no es ni el más largo ni el más corto"), ("comprobar", "revisar que el orden sea correcto")],
    worked=[
        {"title": "Ordenar tres", "problem": "Un lápiz mide 15 cubitos, una regla 30 cubitos y una goma 5 cubitos. Ordénalos del más corto al más largo.", "steps": ["Comparo: 5 < 15 < 30.", "El más corto es la goma.", "Luego el lápiz.", "El más largo es la regla."], "answer": "Goma, lápiz, regla"},
        {"title": "El del medio", "problem": "En el ejemplo, ¿cuál es el del medio?", "steps": ["Ni el más corto ni el más largo.", "Es el lápiz."], "answer": "El lápiz"},
    ],
    mistakes=[
        {"wrong": "Ordenar sin comparar los tres.", "why": "Se compara sólo un par.", "fix": "Compara de a dos hasta tener el orden completo."},
        {"wrong": "Invertir el orden.", "why": "No se lee el sentido pedido.", "fix": "Lee si piden del más corto al más largo o al revés."},
    ],
    tiers={
        "recovery": [ex("Tres cintas miden 10, 25 y 15 cubitos. ¿Cuál es la más corta?", "La de 10 cubitos", "Es la menor."), ex("Las mismas cintas. ¿Cuál es la más larga?", "La de 25 cubitos", "Es la mayor."), ex("Las mismas cintas. ¿Cuál es la del medio?", "La de 15 cubitos", "Ni la más corta ni la más larga.")],
        "understand": [
            ex("¿Cómo encuentro el orden de tres objetos?", "Comparando de a dos", "Así se llega al orden completo."),
            ex("¿Qué significa «del más corto al más largo»?", "Empezar por el que mide menos", "La longitud va creciendo."),
            ex("¿Qué se hace para comprobar el orden?", "Alinear los tres por un extremo", "Cada uno debe sobresalir más."),
        ],
        "apply": [
            ex("Ordena del más corto al más largo: 20, 8 y 14 cubitos.", "8, 14, 20", "El menor va primero."),
            ex("Ordena del más largo al más corto: 5, 30 y 12 cubitos.", "30, 12, 5", "El mayor va primero."),
            ex("Ordena del más corto al más largo: cuchara 15 cubitos, tenedor 17 cubitos, cuchillo 20 cubitos.", "Cuchara, tenedor, cuchillo", "15 < 17 < 20."),
        ],
        "reason": [
            ex("Ema dice: A es más corto que B y B más corto que C, pero A es más largo que C. ¿Es posible?", "No", "Si A < B < C, entonces A < C."),
            ex("Si el objeto del medio mide 12 cubitos, ¿puede el más corto medir 15 cubitos?", "No", "El más corto debe medir menos de 12."),
        ],
        "challenge": [
            ex("Tres palitos suman 30 cubitos. El más corto mide 5 y el del medio 10. ¿Cuánto mide el más largo?", "15 cubitos", "30 − 5 − 10 = 15."),
            ex("Ordena de más corto a más largo: lápiz 17 cubitos, goma 5 cubitos, regla 30 cubitos, tijera 20 cubitos.", "Goma, lápiz, tijera, regla", "5 < 17 < 20 < 30."),
        ],
    },
    context=[ex("En la mesa hay tres lápices: uno de 12 cubitos, uno de 18 cubitos y uno de 9 cubitos. Ordénalos de menor a mayor.", "9, 12, 18", "Se compara de a dos.")],
    selfcheck=[ex("Ordena del más corto al más largo: 7, 3 y 5 cubitos.", "3, 5, 7", "El menor va primero."), ex("¿Cuál es el del medio entre 4, 9 y 6 cubitos?", "6 cubitos", "Ni el menor ni el mayor."), ex("¿Qué haces para comprobar tu orden?", "Alineo los tres", "Veo cuánto sobresale cada uno.")],
    open_task=task("Elige tres objetos de tu casa y ordénalos del más corto al más largo comparándolos de a dos. Escribe cada comparación y el orden final.", "Comparaciones: cuchara más corta que lápiz; lápiz más corto que regla; cuchara más corta que regla. Orden: cuchara, lápiz, regla.", ["tres comparaciones", "orden final", "comprobación con los tres alineados"], ["comparaciones", "orden"], ["comparar sólo dos pares", "orden inconsistente"], "Pide mostrar con los objetos reales."),
    reinforce="Ordena tres lápices de colores por longitud.",
    extend="Ordena cuatro objetos por longitud y explica cuántas comparaciones necesitaste.",
)

register(
    OA18, 4,
    materials="Una cinta, un cordel y tres objetos de la sala que no se pueden mover; descripciones en cada ejercicio.",
    use="Aprenderé a comparar longitudes de objetos que no puedo mover, usando una cinta o cordel como intermediario. Sirve para comparar cosas fijas, como una puerta y una ventana.",
    prior=["Sé alinear para comparar.", "Sé ordenar longitudes."],
    explain=[
        "A veces no puedes acercar dos objetos para compararlos, como el alto de una puerta y el largo de una mesa. Para eso usas un intermediario: una cinta o un cordel que sí puedes mover.",
        "Mide el primer objeto con la cinta, marcando el largo. Luego lleva la cinta al segundo objeto y compara. Si la cinta sobra, el segundo es más corto; si falta, es más largo; si calza, son igual de largos.",
        "Para que la comparación sea justa, usa siempre el mismo intermediario y marca bien el extremo. Después escribe tu conclusión con más largo que, más corto que o igual de largo que.",
    ],
    vocab=[("intermediario", "objeto que sirve para pasar la medida"), ("cinta", "tira que puedo mover y marcar"), ("marcar", "señalar el largo"), ("calzar", "ajustarse justo"), ("fijo", "que no se puede mover")],
    worked=[
        {"title": "Comparar con una cinta", "problem": "Compara el alto de la puerta con el largo de una mesa.", "steps": ["Mido el alto de la puerta con la cinta y marco el largo.", "Llevo la cinta a la mesa.", "La cinta sobra, entonces la mesa es más corta."], "answer": "La mesa es más corta que la puerta"},
        {"title": "Igual de largo", "problem": "La cinta calza justo con ambos objetos.", "steps": ["Calza con el primero.", "Calza con el segundo."], "answer": "Son igual de largos"},
    ],
    mistakes=[
        {"wrong": "Estimar a ojo sin intermediario.", "why": "Los ojos pueden engañar.", "fix": "Usa la cinta para comparar."},
        {"wrong": "No marcar el largo en la cinta.", "why": "Se pierde la medida.", "fix": "Marca el extremo con un lápiz."},
    ],
    tiers={
        "recovery": [ex("La cinta marcada con la puerta sobra al llegar a la mesa. ¿Cuál es más corto?", "La mesa", "La cinta cubre más que la mesa."), ex("La cinta marcada con la puerta falta al llegar a la ventana. ¿Cuál mide más, la puerta o la ventana?", "La ventana", "Necesita más cinta."), ex("La cinta calza justo con ambos. ¿Qué concluyes?", "Son igual de largos", "Miden lo mismo.")],
        "understand": [
            ex("¿Para qué sirve un intermediario?", "Para comparar objetos que no se pueden mover", "Pasa la medida."),
            ex("¿Qué hago después de medir con la cinta?", "La llevo al otro objeto y comparo", "Veo si sobra o falta."),
            ex("¿Por qué marco el largo en la cinta?", "Para no perder la medida", "Es la referencia."),
        ],
        "apply": [
            ex("Mides la altura de una mesa con una cinta. Al comparar con un librero, la cinta no alcanza. ¿Cuál es más alto?", "El librero", "A la cinta le falta largo."),
            ex("Mides el largo de una mesa con un cordel. Al comparar con un pizarrón, el cordel sobra. ¿Cuál es más largo?", "La mesa", "El cordel cubre más que el pizarrón."),
            ex("Mides un pasillo con una cinta. Al comparar con el patio, calza justo. ¿Qué concluyes?", "Miden lo mismo", "La cinta calza justo con ambos."),
        ],
        "reason": [
            ex("Luis dice que la puerta es más alta que la ventana sin medir. ¿Qué le falta?", "Comparar con una cinta", "Los ojos pueden engañar."),
            ex("¿Por qué puedo usar la misma cinta para comparar varios objetos?", "Porque conserva la medida", "Siempre mide lo mismo."),
        ],
        "challenge": [
            ex("Una cinta mide 15 cubitos. Una mesa mide 20 cubitos. ¿Cuánto falta a la cinta?", "5 cubitos", "20 − 15 = 5."),
            ex("Una puerta mide 20 cubitos de alto y una ventana 12 cubitos. ¿Cuánto más alta es la puerta?", "8 cubitos", "20 − 12 = 8."),
        ],
    },
    context=[ex("Para saber si un librero cabe bajo una ventana, un niño mide el librero con un cordel y lo compara con la altura bajo la ventana. ¿Qué hizo?", "Usó un intermediario", "El cordel pasa la medida.")],
    selfcheck=[ex("Si la cinta sobra, el objeto comparado es...", "Más corto", "La cinta cubre más."), ex("Si la cinta falta, el objeto comparado es...", "Más largo", "Necesita más cinta."), ex("¿Qué usas para comparar objetos fijos?", "Una cinta o cordel", "Se usa un intermediario.")],
    open_task=task("Con un cordel, compara el largo de tu cama con el de una puerta cerrada (alto) o una mesa. Marca el cordel, llévalo al otro objeto y escribe qué pasó y qué concluyes.", "Medí mi cama con el cordel y marqué. En la mesa, el cordel sobraba. Concluyo: la mesa es más corta que mi cama.", ["usa un intermediario", "marca la medida", "concluye con más largo/más corto"], ["cordel marcado", "frase"], ["comparar a ojo", "no marcar"], "Pide repetir con otra cinta para confirmar."),
    reinforce="Compara dos objetos fijos de tu casa con una lana.",
    extend="Ordena cuatro objetos fijos de tu casa por longitud usando un cordel.",
)
