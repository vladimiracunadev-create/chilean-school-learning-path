"""Cuaderno del estudiante, 2.º básico Ciencias Naturales: OA 11 (ciclo del agua) y OA 12 (tiempo atmosférico)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA11, OA12 = "CN02 OA 11", "CN02 OA 12"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- OA 11
register(
    OA11, 1,
    materials="Hoja, lápices de colores y este cuaderno con las cuatro etapas del ciclo del agua. Si quieres observar, un vaso transparente con agua y una ventana con sol.",
    use="Aprenderé que el agua de la Tierra cambia y circula siempre en un ciclo. Sirve para entender de dónde viene la lluvia y a dónde va el agua de los ríos.",
    prior=["Sé que el agua puede ser líquida, sólida o gas.", "Sé que el agua se evapora con el calor."],
    explain=[
        "El agua de la Tierra se mueve en un ciclo. Un ciclo es una serie de pasos que se repite una y otra vez. El agua sube al cielo, cae como lluvia o nieve, llega a los ríos, lagos y mares, y vuelve a subir.",
        "Las etapas son cuatro: evaporación, condensación, precipitación y acumulación. El Sol calienta el agua de los mares y los ríos y la evapora. Arriba el vapor se enfría y forma nubes. Luego el agua cae. Después se junta en ríos, lagos, mares y bajo la tierra.",
        "El agua no se crea en las nubes. Las nubes se forman con agua que ya existía y que subió como vapor. Es la misma agua que cambia de lugar y de estado. Por eso el ciclo no tiene un comienzo fijo: puedo partir en cualquier etapa.",
    ],
    vocab=[("ciclo", "serie de pasos que se repite"), ("evaporación", "el agua líquida pasa al aire como vapor"), ("condensación", "el vapor se enfría y forma gotitas, como en las nubes"), ("precipitación", "agua que cae del cielo, como lluvia, nieve o granizo"), ("acumulación", "agua que se junta en ríos, lagos, mares y bajo la tierra")],
    worked=[
        {"title": "Ordenar las etapas", "problem": "Ordena estas etapas del ciclo, partiendo en la evaporación: precipitación, acumulación, evaporación, condensación.", "steps": ["Parto con evaporación: el agua sube como vapor.", "Después el vapor se enfría: condensación.", "Luego el agua cae: precipitación.", "Finalmente se junta en ríos y mares: acumulación."], "answer": "Evaporación, condensación, precipitación, acumulación"},
        {"title": "¿De dónde viene el agua de la nube?", "problem": "Fernanda dice que las nubes fabrican el agua. ¿Es correcto?", "steps": ["Las nubes se forman con vapor de agua que subió.", "Ese vapor venía de mares, ríos y suelo mojado.", "El agua ya existía y solo cambió de estado y lugar."], "answer": "No; el agua de las nubes ya existía y subió como vapor"},
    ],
    mistakes=[
        {"wrong": "Decir que el agua se crea en las nubes.", "why": "Se ve el agua caer del cielo y se piensa que nace allí.", "fix": "Las nubes se forman con vapor que subió; el agua cambia de lugar y de estado."},
        {"wrong": "Dibujar solo flechas sin escribir qué pasa en cada etapa.", "why": "Se memoriza el dibujo sin comprender los procesos.", "fix": "Escribe junto a cada flecha qué le pasa al agua: se evapora, se enfría, cae, se junta."},
    ],
    tiers={
        "recovery": [
            ex("¿Cómo se llama la etapa en que el agua líquida sube al aire como vapor?", "Evaporación", "Evaporar es pasar de líquido a vapor."),
            ex("¿Cómo se llama la etapa en que el agua cae del cielo?", "Precipitación", "La lluvia, la nieve y el granizo son precipitaciones."),
            ex("Completa: el ciclo del agua es una serie de pasos que se ___.", "repite", "Un ciclo siempre vuelve a empezar."),
        ],
        "understand": [
            ex("¿Qué astro del cielo calienta el agua para que se evapore?", "El Sol", "El calor del Sol evapora el agua."),
            ex("¿Qué pasa con el vapor de agua cuando sube y se enfría?", "Se condensa y forma gotitas", "Condensar es pasar de vapor a gotitas de agua líquida."),
            ex("¿Por qué se dice que el agua es la misma en todo el ciclo?", "Porque solo cambia de estado y de lugar", "El agua no se crea ni se destruye en el ciclo."),
        ],
        "apply": [
            ex("Ordena las etapas del ciclo con números del 1 al 4, partiendo en evaporación: acumulación, evaporación, precipitación, condensación.", "1 evaporación, 2 condensación, 3 precipitación, 4 acumulación", "Así se ordena el ciclo: el agua sube, forma nubes, cae y se junta."),
            ex("Una charca se seca al sol y el agua sube al cielo. ¿En qué etapa del ciclo está esa agua?", "En la evaporación", "El agua líquida pasa al aire como vapor."),
            ex("La lluvia cae sobre el cerro y llega al río. Nombra las dos etapas que ocurren.", "Precipitación y acumulación", "Primero cae y después se junta en el río."),
        ],
        "reason": [
            ex("Pablo dice: «El agua del río se acaba cuando llega al mar». ¿Qué le respondes con el ciclo?", "Que el agua del mar se evapora y vuelve a formar nubes", "El agua sigue en el ciclo y no se acaba."),
            ex("Camila dibujó solo flechas: mar, nube, lluvia. ¿Qué le falta escribir para explicar el ciclo?", "Qué le pasa al agua en cada flecha: evapora, condensa, cae", "Un buen ciclo explica cada proceso."),
        ],
        "challenge": [
            ex("Un charco, un lago y una nube tienen agua. ¿En cuál de los tres el agua se formó porque el vapor se enfrió?", "En la nube", "En la nube el vapor se enfrió, se condensó y formó gotitas."),
            ex("Si el ciclo no tiene un comienzo fijo, ¿en qué etapa se puede partir al explicarlo?", "En cualquiera", "Es un círculo y todas las etapas se conectan."),
        ],
    },
    context=[ex("Un día de sol, la ropa mojada se seca en el patio y por la noche llueve. Escribe qué etapa del ciclo ocurre cuando se seca la ropa y cuál cuando llueve.", "Evaporación y precipitación", "El agua de la ropa se evapora y la lluvia es una precipitación.")],
    selfcheck=[
        ex("¿Cuántas etapas tiene el ciclo que aprendiste?", "Cuatro", "Son evaporación, condensación, precipitación y acumulación."),
        ex("¿Qué etapa forma las nubes?", "La condensación", "El vapor se enfría y forma gotitas."),
        ex("¿Se crea agua nueva en las nubes?", "No", "Se forma con agua que ya existía."),
    ],
    open_task=task(
        "Dibuja un paisaje con mar, nube, montaña y río. Pon cuatro flechas y escribe al lado de cada una qué le pasa al agua: «se evapora», «se enfría y forma nube», «cae» y «se junta». Usa los nombres de las etapas.",
        "Del mar sale una flecha hacia arriba: evaporación. En la nube: condensación. De la nube cae lluvia: precipitación. En el río y el mar: acumulación.",
        ["incluye las cuatro etapas", "escribe qué pasa en cada flecha", "usa las palabras del vocabulario"],
        ["dibujo con flechas", "etiquetas escritas", "frase sobre dónde empieza"],
        ["solo flechas sin explicar", "decir que el agua se crea en las nubes"],
        "Reconoce el dibujo ordenado y pide que explique con sus palabras qué pasa en cada flecha.",
    ),
    reinforce="Escribe cada etapa en una tarjeta, mézclalas y ordénalas formando un círculo.",
    extend="Explica a alguien de tu casa cómo el agua del mar puede terminar en tu vaso. Cuenta los pasos con ayuda de un dibujo.",
)

register(
    OA11, 2,
    materials="Una bolsa de plástico transparente con cierre, un poco de agua, cinta adhesiva y una ventana con sol. Sin calentar el agua. Este cuaderno trae los datos por si no puedes hacerlo.",
    use="Aprenderé cómo el agua se evapora y se condensa en la naturaleza. Sirve para entender cómo se forman las nubes y por qué se empañan los vidrios.",
    prior=["Sé que el vapor de agua es invisible.", "Sé que el cambio de gas a líquido se llama condensar."],
    explain=[
        "El Sol calienta el agua de los mares, ríos y lagos. Parte de esa agua se evapora y sube al aire como vapor de agua. También se evapora la que está en el suelo húmedo y en las plantas.",
        "El vapor sube. Mientras más arriba, más frío es el aire. Cuando el vapor se enfría, se condensa: forma gotitas muy pequeñas de agua líquida. Muchísimas gotitas juntas forman una nube.",
        "Puedo ver algo parecido en una bolsa cerrada con un poco de agua y puesta al sol: dentro se forman gotitas en la parte alta. Es un modelo pequeño: el agua se evapora abajo y se condensa arriba, sin salir de la bolsa.",
    ],
    vocab=[("evaporación", "paso del agua líquida a vapor"), ("condensación", "paso del vapor a gotitas de agua"), ("nube", "muchas gotitas de agua juntas en el aire"), ("vapor", "agua en estado gaseoso, invisible"), ("modelo", "una versión pequeña que muestra cómo funciona algo")],
    worked=[
        {"title": "La bolsa al sol", "problem": "Pones 3 cucharadas de agua en una bolsa cerrada pegada a una ventana soleada. Después de 3 horas hay gotitas arriba. ¿Qué etapas ocurrieron?", "steps": ["El agua de abajo se evaporó con el calor del sol.", "El vapor subió dentro de la bolsa y se enfrió arriba.", "Se condensó y formó gotitas."], "answer": "Primero evaporación y luego condensación"},
        {"title": "Cómo se forma una nube", "problem": "Explica cómo se forma una nube con tres pasos.", "steps": ["El Sol evapora agua del mar.", "El vapor sube y se enfría.", "El vapor se condensa y forma gotitas que juntas hacen la nube."], "answer": "Evaporación, el vapor sube, condensación y nube"},
    ],
    mistakes=[
        {"wrong": "Decir que las gotas de la bolsa vienen de afuera.", "why": "No se tiene en cuenta que la bolsa está cerrada.", "fix": "Las gotas se forman con el agua de adentro: se evaporó y se condensó."},
        {"wrong": "Pensar que la nube es vapor de agua.", "why": "Se confunde el vapor con las gotitas.", "fix": "El vapor es invisible; la nube se ve porque tiene gotitas de agua líquida."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué calienta el agua de los mares para que se evapore?", "El Sol", "El calor del Sol evapora el agua."),
            ex("Cuando el vapor se enfría y forma gotitas, ¿qué proceso ocurre?", "Condensación", "Condensar es pasar de vapor a gotitas."),
            ex("Completa: muchas gotitas de agua juntas forman una ___.", "nube", "Las nubes están hechas de gotitas de agua."),
        ],
        "understand": [
            ex("¿Por qué el vapor se enfría cuando sube?", "Porque arriba el aire es más frío", "Mientras más alto, más frío es el aire."),
            ex("¿Por qué la nube se ve, si el vapor no se ve?", "Porque la nube tiene gotitas de agua líquida", "Las gotitas reflejan la luz y se ven; el vapor no."),
            ex("En la bolsa al sol, ¿dónde se evapora el agua y dónde se condensa?", "Se evapora abajo y se condensa arriba", "El agua tibia sube como vapor y se enfría arriba."),
        ],
        "apply": [
            ex("Una olla tiene agua tibia y una tapa fría. Aparecen gotas en la tapa. ¿Qué procesos ocurrieron, en orden?", "Evaporación y condensación", "El agua se evaporó y el vapor se condensó en la tapa."),
            ex("La bolsa tenía 30 mL de agua al comienzo y 30 mL en total al final, entre agua de abajo y gotitas de arriba. ¿Se perdió agua?", "No", "El agua solo cambió de lugar y de estado."),
            ex("Un espejo frío se empaña. ¿Qué proceso ocurre: evaporación o condensación?", "Condensación", "El vapor del aire se enfría en el espejo y forma gotitas."),
        ],
        "reason": [
            ex("Daniel dice: «La bolsa tiene gotas arriba, entonces entró agua desde afuera». La bolsa estaba cerrada. ¿Qué evidencia dice que está equivocado?", "Que la bolsa estaba cerrada y no entró agua", "Con la bolsa cerrada, las gotas salieron del agua de adentro."),
            ex("Una laguna pequeña se ve grande el lunes. Después de una semana de mucho calor y sin lluvia se ve más chica. ¿Qué pudo pasar con parte de su agua?", "Se evaporó", "Con calor, más agua pasa al aire como vapor."),
        ],
        "challenge": [
            ex("Explica en una frase cómo se forma una nube usando las palabras «evapora» y «condensa».", "El agua se evapora, sube, se enfría y se condensa formando una nube", "Así se juntan ambos procesos."),
            ex("Si el aire no se enfriara nunca al subir, ¿se formarían nubes? Explica.", "No, porque el vapor necesita enfriarse para condensarse", "Sin enfriamiento no hay condensación ni gotitas."),
        ],
    },
    context=[ex("En un día frío, el vidrio de la ventana de la cocina se empaña por dentro mientras se hierve agua. Un adulto cocina. ¿Qué dos procesos explican las gotas del vidrio?", "Evaporación del agua de la olla y condensación en el vidrio frío", "El vapor sube de la olla y se enfría al tocar el vidrio.")],
    selfcheck=[
        ex("¿Qué proceso lleva el agua al aire como vapor?", "La evaporación", "El agua líquida se evapora."),
        ex("¿Qué proceso forma las gotitas de las nubes?", "La condensación", "El vapor se enfría y se condensa."),
        ex("¿De qué está hecha una nube?", "De gotitas de agua", "Son muchas gotitas juntas."),
    ],
    open_task=task(
        "Observa o imagina la bolsa al sol: 3 cucharadas de agua, pegada a una ventana con sol, 3 horas. Dibuja la bolsa al inicio y al final, con flechas que muestren hacia dónde va el agua. Escribe «evaporación» y «condensación» donde corresponda y una frase que diga por qué se parece a una nube.",
        "Al inicio: agua abajo. Al final: gotitas arriba. Flecha hacia arriba: evaporación. Gotitas en la parte alta: condensación. Se parece a una nube porque el vapor se enfría y forma gotitas.",
        ["dibuja inicio y final", "ubica evaporación y condensación", "relaciona con las nubes"],
        ["dos dibujos", "etiquetas", "frase explicativa"],
        ["decir que el agua viene de afuera", "confundir los nombres de los procesos"],
        "Valora el uso de ambos nombres y pide que explique por qué las gotitas se forman arriba.",
    ),
    reinforce="Dibuja un vaso con agua fría y gotas por fuera y explica por qué se parece a una nube.",
    extend="Cuenta a alguien de tu casa por qué en mañanas frías aparece neblina cerca del suelo.",
)

register(
    OA11, 3,
    materials="Una maceta o bandeja con tierra, una regadera pequeña, una botella con agujeros en la tapa (hecha por un adulto), un plato y este cuaderno. Trabajar afuera o sobre una bandeja.",
    use="Aprenderé que el agua cae como precipitación y se acumula en ríos, lagos, mares y bajo la tierra. Sirve para entender a dónde va la lluvia.",
    prior=["Sé que el agua escurre hacia abajo.", "Sé que la lluvia, la nieve y el granizo caen del cielo."],
    explain=[
        "Cuando las gotitas de una nube se juntan y se hacen pesadas, caen. Eso es la precipitación. Puede caer como lluvia, como nieve o como granizo. En lugares muy fríos, el agua se acumula como hielo en glaciares.",
        "Después, el agua se acumula. Parte escurre por las laderas y forma ríos que llegan a lagos y al mar. Otra parte entra en la tierra y forma agua subterránea. La nieve de las montañas también se derrite en primavera y alimenta los ríos.",
        "La acumulación no es un final. El agua de los ríos, lagos y mares se evapora de nuevo con el Sol, y el ciclo continúa. Lo que cambia es dónde está el agua y en qué estado.",
    ],
    vocab=[("precipitación", "agua que cae de las nubes como lluvia, nieve o granizo"), ("acumulación", "agua que se junta en un lugar"), ("glaciar", "gran masa de hielo en lugares muy fríos"), ("agua subterránea", "agua que está bajo la tierra"), ("río", "agua que corre por un cauce hacia el mar o un lago")],
    worked=[
        {"title": "A dónde va la lluvia", "problem": "Llueve en un cerro con pasto. Cuenta tres lugares donde puede terminar el agua.", "steps": ["Una parte escurre por la ladera y forma un arroyo.", "Otra parte entra en la tierra como agua subterránea.", "El arroyo llega a un río y el río, al mar."], "answer": "Arroyo y río, agua subterránea y mar"},
        {"title": "La nieve y la primavera", "problem": "En las montañas cae nieve en invierno. ¿Qué le pasa en primavera y a dónde llega esa agua?", "steps": ["En primavera sube la temperatura.", "La nieve se derrite y pasa a agua líquida.", "El agua baja y alimenta los ríos."], "answer": "Se derrite y llega a los ríos"},
    ],
    mistakes=[
        {"wrong": "Pensar que el agua que cae en la tierra se pierde.", "why": "No se ve a dónde va.", "fix": "Parte entra en el suelo, parte escurre a ríos, y parte se evapora."},
        {"wrong": "Creer que solo hay precipitación cuando llueve.", "why": "Se piensa que solo la lluvia cae.", "fix": "Granizo y nieve también son precipitaciones."},
    ],
    tiers={
        "recovery": [
            ex("Nombra tres tipos de precipitación.", "Lluvia, nieve y granizo", "Son las formas en que el agua cae del cielo."),
            ex("¿Cómo se llama el agua que se junta en ríos, lagos y mares?", "Acumulación", "Acumular es juntar."),
            ex("Completa: la nieve de las montañas se derrite y alimenta los ___.", "ríos", "El agua derretida baja por los cauces."),
        ],
        "understand": [
            ex("¿Por qué caen las gotitas de una nube?", "Porque se juntan y se hacen pesadas", "Cuando son pesadas, no pueden seguir flotando."),
            ex("¿Qué es el agua subterránea?", "Agua que está bajo la tierra", "Entra en el suelo y se acumula bajo él."),
            ex("¿El agua deja de existir cuando llega al mar?", "No", "Se evapora de nuevo y el ciclo continúa."),
        ],
        "apply": [
            ex("Cae granizo sobre un patio. ¿Qué tipo de precipitación es?", "Granizo", "Es una precipitación de bolitas de hielo."),
            ex("En un cerro con nieve, empieza la primavera. ¿Qué debería pasar con el caudal del río de abajo?", "Aumenta", "La nieve derretida suma agua al río."),
            arith("Un tambor recoge el agua de lluvia que cae del techo. En la mañana junta 40 litros y en la tarde 30 litros. ¿Cuántos litros tiene?", "40+30", "Se suma el agua que se acumuló en cada momento.", " litros"),
        ],
        "reason": [
            ex("Un niño dice que cuando llueve toda el agua se pierde. ¿Qué le explicas del ciclo?", "Que parte entra en la tierra, parte llega a ríos y parte se evapora", "El agua tiene varios destinos y vuelve al ciclo."),
            ex("En un balde con 12 litros de lluvia se evaporan 2 litros en un día de sol. ¿Cuántos litros quedan?", "10 litros", "12 − 2 = 10 litros; la evaporación saca agua del balde."),
        ],
        "challenge": [
            ex("¿En qué se parece una acumulación de agua en un lago con una en un glaciar?", "En que las dos son agua acumulada, una líquida y otra sólida", "Las dos guardan agua, pero en distinto estado."),
            ex("Explica el recorrido de una gota: nube, cerro, río, mar.", "Cae como lluvia, escurre por el cerro, llega al río y al mar", "Sigue la pendiente hacia abajo."),
        ],
    },
    context=[ex("En el sur de Chile llueve mucho en invierno. El río cercano a la casa de Matías se pone más ancho. ¿Qué etapa del ciclo explica que haya más agua en el río?", "La precipitación", "Cae más agua y escurre al río.")],
    selfcheck=[
        ex("¿Qué es precipitación?", "Agua que cae de las nubes", "Puede ser lluvia, nieve o granizo."),
        ex("¿A dónde llega el agua que escurre por un cerro?", "A ríos y al mar", "Escurre hacia abajo."),
        ex("¿Qué pasa con la nieve en primavera?", "Se derrite", "Sube la temperatura."),
    ],
    open_task=task(
        "Dibuja un cerro con nieve arriba, un río abajo y un mar. Muestra con flechas el recorrido de una gota de lluvia y de otra de nieve derretida. Escribe una frase que diga a dónde llegan y qué pasa con ellas después.",
        "La gota de lluvia escurre por el cerro, llega al río y al mar. La nieve derretida baja al río. Después el agua se evapora de nuevo.",
        ["muestra el recorrido con flechas", "incluye río y mar", "dice que el agua se evapora de nuevo"],
        ["dibujo con flechas", "frase de explicación", "rótulos"],
        ["dibujar el agua sin salida", "olvidar la nieve derretida"],
        "Reconoce el recorrido y pide que explique qué pasa con el agua cuando llega al mar.",
    ),
    reinforce="Con una regadera sobre una bandeja con tierra, mira hacia dónde escurre el agua y dibuja lo que ves.",
    extend="Averigua el nombre de un río de tu región y escribe a dónde llega.",
)

register(
    OA11, 4,
    materials="Una hoja, lápices, una calculadora o papel para cuentas y este cuaderno. Todos los datos de agua vienen en los enunciados.",
    use="Aprenderé por qué el agua es un recurso preciado y qué acciones cotidianas ayudan a cuidarla. Sirve para decidir cómo usar el agua en casa y en el colegio.",
    prior=["Sé que el agua cambia y circula en un ciclo.", "Sé sumar, restar y multiplicar con números pequeños."],
    explain=[
        "El agua es un recurso: algo de la naturaleza que usamos para vivir. La necesitamos para beber, cocinar, lavar y regar. Es preciada porque sin agua no hay vida. Aunque el ciclo la hace volver, el agua limpia y fácil de usar no siempre alcanza.",
        "La mayor parte del agua de la Tierra es salada y no sirve para beber ni regar. Solo una parte pequeña es agua dulce. En muchas zonas de Chile hay años con poca lluvia, por eso es importante usarla con cuidado.",
        "Cada persona puede cuidar el agua con acciones simples: cerrar la llave mientras se lavan los dientes, avisar si hay una llave que gotea, ducharse en menos tiempo y regar con regadera en la tarde. Cuidar el agua es una acción que repito cada día.",
    ],
    vocab=[("recurso", "algo de la naturaleza que usamos para vivir"), ("preciado", "muy valioso, que hay que cuidar"), ("agua dulce", "agua que sirve para beber, no es salada"), ("cuidar", "usar con atención para que no se pierda"), ("gotear", "perder agua en gotas")],
    worked=[
        {"title": "Llave cerrada al lavar los dientes", "problem": "En este ejemplo, una llave abierta gasta 5 litros por minuto. Si te lavas los dientes 2 minutos con la llave abierta, ¿cuánta agua gastas? ¿Y si cierras la llave y solo usas 1 litro?", "steps": ["Con la llave abierta: 5 × 2 = 10 litros.", "Con la llave cerrada usas 1 litro.", "Ahorras 10 − 1 = 9 litros."], "answer": "Gastas 10 litros con la llave abierta; ahorras 9 litros al cerrarla"},
        {"title": "Elegir una acción", "problem": "Sofía ve que el patio está seco. ¿Cuál es una forma cuidadosa de regar: a pleno sol del mediodía con la manguera abierta, o con regadera en la tarde?", "steps": ["Al mediodía el sol evapora mucha agua.", "En la tarde hay menos calor y se evapora menos.", "La regadera usa solo el agua necesaria."], "answer": "Con regadera en la tarde"},
    ],
    mistakes=[
        {"wrong": "Pensar que el agua nunca se acaba porque el ciclo la devuelve.", "why": "Se confunde la existencia de agua con el agua dulce disponible.", "fix": "El agua dulce y limpia es poca y no está en todos los lugares ni en todos los años."},
        {"wrong": "Creer que cuidar el agua es solo tarea de los adultos.", "why": "Se piensa que solo importan las grandes decisiones.", "fix": "Cada persona puede cuidar el agua con acciones cotidianas."},
    ],
    tiers={
        "recovery": [
            ex("¿Para qué usamos el agua en la casa? Nombra dos usos.", "Beber y lavar, por ejemplo", "El agua se usa para beber, cocinar, lavar y regar."),
            ex("¿Es mejor cerrar o dejar abierta la llave mientras te lavas los dientes?", "Cerrarla", "Con la llave cerrada no se gasta agua inútilmente."),
            ex("Completa: el agua es un recurso ___ porque sin ella no hay vida.", "preciado", "Preciado significa muy valioso."),
        ],
        "understand": [
            ex("¿Qué es un recurso?", "Algo de la naturaleza que usamos para vivir", "El agua es un recurso."),
            ex("¿Por qué no sirve el agua del mar para beber?", "Porque es salada", "El agua dulce es la que se puede beber."),
            ex("¿Por qué cuidar el agua si el ciclo la devuelve?", "Porque el agua dulce y limpia no siempre alcanza", "Solo una parte pequeña del agua es dulce y está disponible."),
        ],
        "apply": [
            arith("Una llave abierta gasta 5 litros por minuto en este ejemplo. ¿Cuántos litros gasta en 3 minutos?", "5*3", "Se multiplican los litros por minuto por los minutos.", " litros"),
            arith("Una llave que gotea pierde 2 litros por día en este ejemplo. ¿Cuántos litros pierde en 7 días?", "2*7", "Se multiplican los litros diarios por los días.", " litros"),
            ex("Hay una maceta seca. Nombra una forma de regarla cuidando el agua.", "Con regadera, en la tarde o mañana temprano", "Se usa solo el agua necesaria y se evapora menos."),
        ],
        "reason": [
            ex("Un compañero dice: «Cerrar la llave por unos segundos no sirve». Si la llave gasta 5 litros por minuto, ¿cuántos litros se pueden ahorrar si cierras la llave durante 2 minutos de lavado?", "10 litros", "5 × 2 = 10: ese es el agua que no sale."),
            ex("En una casa, la llave de la cocina gotea 3 litros al día. En el colegio, la de un baño gotea 5 litros al día. ¿Cuál pierde más agua en un día y cuánto más?", "La del colegio; 2 litros más", "5 − 3 = 2 litros más al día."),
        ],
        "challenge": [
            ex("Propón dos acciones para cuidar el agua en el colegio.", "Cerrar bien las llaves y avisar si hay una que gotea", "Son acciones que cualquier estudiante puede hacer."),
            ex("Una familia junta 20 litros de agua de la lluvia en un balde y la usa para regar. ¿Qué cuidado del agua hace?", "La reutiliza", "Usa agua de lluvia en vez de agua tratada de la llave."),
        ],
    },
    context=[ex("En la casa de Antonia se bañan 4 personas. En este ejemplo, cada una usa 40 litros en la ducha. Si cada persona acorta la ducha y usa 30 litros, ¿cuántos litros ahorra la familia en total?", "40 litros", "Cada persona ahorra 10 litros y 4 × 10 = 40 litros.")],
    selfcheck=[
        ex("¿Por qué el agua es un recurso preciado?", "Porque sin agua no hay vida", "Todos los seres vivos la necesitan."),
        ex("Nombra una acción para cuidar el agua en casa.", "Cerrar la llave al lavarse los dientes", "Evita gastar agua que no se usa."),
        ex("¿El agua de mar sirve para beber?", "No", "Es agua muy salada."),
    ],
    open_task=task(
        "Mira esta lista de acciones diarias con agua: lavar los dientes con la llave abierta, cerrar la llave mientras te enjabonas las manos, regar el patio al mediodía con manguera, avisar de una llave que gotea. Elige las dos que ayudan a cuidar el agua y cambia las otras dos por una acción mejor. Escribe un compromiso: «Yo voy a… todos los días».",
        "Ayudan a cuidar el agua: cerrar la llave mientras te enjabonas y avisar de una llave que gotea. Las otras se cambian por: cerrar la llave al lavar los dientes y regar en la tarde con regadera. Yo voy a cerrar la llave al lavarme los dientes todos los días.",
        ["distingue las acciones que cuidan y las que no", "propone cambios concretos", "escribe un compromiso personal posible"],
        ["lista corregida", "compromiso escrito", "dibujo de la acción elegida"],
        ["elegir acciones que gastan agua", "proponer compromisos que no puede cumplir un niño"],
        "Valora un compromiso realista y pide que cuente cómo sabrá si lo cumplió.",
    ),
    reinforce="Haz un cartel con una frase para recordar cerrar la llave al lavarse los dientes.",
    extend="Mide con ayuda de un adulto cuántos litros caben en un balde y calcula cuántos baldes llenaría una llave que gotea 2 litros al día en 10 días.",
)

# ---------------------------------------------------------------- OA 12
register(
    OA12, 1,
    materials="Una hoja para el registro del tiempo (tabla con columnas «cielo», «lluvia», «viento», «temperatura»), un lápiz y una ventana. Si no puedes salir, usa los registros de este cuaderno.",
    use="Aprenderé a mirar el tiempo atmosférico con criterios: cielo, lluvia, viento y temperatura. Sirve para describir cómo está el día sin adivinar.",
    prior=["Sé que el Sol da luz y calor.", "Sé leer números como 18 °C."],
    explain=[
        "El tiempo atmosférico es cómo está la atmósfera en un lugar y en un momento. Se describe con el cielo (despejado o nublado), la lluvia, el viento y la temperatura. El tiempo puede cambiar en pocas horas.",
        "No es lo mismo tiempo atmosférico que estación del año. El verano es una estación y dura meses. Un día lluvioso en verano sigue siendo un día de verano. Hoy puede llover y mañana estar despejado.",
        "Para describirlo bien, miro lo que pasa en vez de adivinar. No debo decir la temperatura solo por la ropa que lleva la gente. Una persona puede estar con abrigo o con polera por gusto. Mejor uso un registro con datos observados.",
    ],
    vocab=[("tiempo atmosférico", "cómo está el día en un lugar: cielo, lluvia, viento y temperatura"), ("nubosidad", "cuántas nubes hay en el cielo"), ("despejado", "cielo con pocas o ninguna nube"), ("registro", "tabla donde anoto lo que observo"), ("temperatura", "qué tan caliente o frío está el aire")],
    worked=[
        {"title": "Describir el día", "problem": "Hoy el cielo está lleno de nubes grises, no llueve, hay poco viento y el termómetro marca 14 °C. Describe el tiempo.", "steps": ["Cielo: nublado.", "Lluvia: no hay.", "Viento: poco.", "Temperatura: 14 °C."], "answer": "Nublado, sin lluvia, poco viento y 14 °C"},
        {"title": "Estación o tiempo", "problem": "Es enero y hoy llueve fuerte. Marcos dice que ya no es verano. ¿Tiene razón?", "steps": ["Enero está en el verano en Chile.", "La lluvia describe el tiempo de hoy.", "Un día lluvioso no cambia la estación."], "answer": "No; sigue siendo verano, solo hoy llueve"},
    ],
    mistakes=[
        {"wrong": "Decir que hace frío porque una persona lleva abrigo.", "why": "La ropa depende del gusto y no solo de la temperatura.", "fix": "Mide o lee la temperatura en el termómetro."},
        {"wrong": "Decir que como llovió hoy ya es invierno.", "why": "Se confunde tiempo con estación.", "fix": "La estación depende de la época del año y de muchos días, no de un solo día."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué cosas se miran para describir el tiempo atmosférico? Nombra dos.", "Cielo y temperatura, por ejemplo", "También se miran lluvia y viento."),
            ex("El cielo no tiene ninguna nube. ¿Cómo se dice?", "Despejado", "Despejado es sin nubes."),
            ex("Completa: la temperatura se mide en grados ___.", "Celsius", "Se escribe °C."),
        ],
        "understand": [
            ex("¿Qué es el tiempo atmosférico?", "Cómo está el día en un lugar: cielo, lluvia, viento y temperatura", "Es una descripción del momento."),
            ex("¿El tiempo atmosférico puede cambiar en un mismo día?", "Sí", "Puede estar despejado en la mañana y nublado en la tarde."),
            ex("¿Cuánto dura una estación: unas horas o varios meses?", "Varios meses", "Una estación dura una parte del año."),
        ],
        "apply": [
            ex("Registro del lunes: cielo con muchas nubes, lluvia suave, poco viento, 9 °C. Escribe una descripción en una frase.", "Nublado, con lluvia suave, poco viento y 9 °C", "Se usan las cuatro observaciones."),
            ex("Registro del martes: cielo despejado, sin lluvia, viento fuerte, 22 °C. ¿Hay lluvia?", "No", "El registro dice sin lluvia."),
            arith("Lunes 9 °C y martes 22 °C. ¿Cuántos grados subió la temperatura?", "22-9", "Se resta la temperatura más baja a la más alta.", " °C"),
        ],
        "reason": [
            ex("Rosa dice: «Hay mucho calor porque Juan va de polera». El termómetro marca 6 °C. ¿Qué evidencia contradice a Rosa?", "El termómetro marca 6 °C, que es frío", "La temperatura se mide, no se adivina por la ropa."),
            ex("Es julio y por la mañana está despejado y tibio. Ana dice: «Ya no es invierno». ¿Tiene razón?", "No", "Un día despejado no cambia la estación."),
        ],
        "challenge": [
            ex("Hoy 12 °C a las 8:00 y 19 °C a las 15:00, cielo despejado. ¿Cuánto cambió la temperatura en el día?", "7 °C", "19 − 12 = 7 °C."),
            ex("Explica con tus palabras por qué se necesitan varios días de observación para hablar de una estación.", "Porque un solo día puede ser distinto de los demás", "Un día solo muestra el tiempo de ese día."),
        ],
    },
    context=[ex("Antes de ir al colegio, Tomás mira el cielo, ve que hay nubes oscuras, el árbol del patio se mueve y el termómetro de su abuela dice 11 °C. ¿Qué tres datos puede anotar en su registro?", "Cielo nublado, hay viento y 11 °C", "Observó el cielo, el viento y la temperatura; la lluvia todavía no cae, así que no la anota.")],
    selfcheck=[
        ex("¿La temperatura se mide con un termómetro o con un reloj?", "Con un termómetro", "El termómetro mide qué tan caliente está algo."),
        ex("Un solo día de lluvia en verano, ¿cambia la estación?", "No", "La estación dura meses."),
        ex("¿Qué se anota para describir el cielo?", "Si está despejado o nublado", "Se describe la nubosidad."),
    ],
    open_task=task(
        "Copia esta tabla y complétala para hoy mirando por la ventana. Si no puedes, usa este registro de ejemplo: cielo con algunas nubes, sin lluvia, viento suave, 17 °C. Después escribe una frase que describa el día sin usar la palabra «bonito».",
        "Cielo: algunas nubes. Lluvia: no. Viento: suave. Temperatura: 17 °C. El día está parcialmente nublado, sin lluvia, con viento suave y 17 °C.",
        ["completa las cuatro columnas", "usa datos observados", "escribe una frase descriptiva"],
        ["tabla completa", "frase del día", "dibujo del cielo"],
        ["decir la temperatura por la ropa", "mezclar el tiempo con la estación"],
        "Valora que use datos en vez de opiniones y pregunta cómo sabe que no hay lluvia.",
    ),
    reinforce="Durante tres días, anota el cielo en una tabla con dibujos de sol, nube y lluvia.",
    extend="Escribe una frase para explicar a un compañero la diferencia entre el tiempo de hoy y la estación en que estamos.",
)

register(
    OA12, 2,
    materials="Tarjetas con los dibujos y descripciones de lluvia, granizo y nieve de este cuaderno, y lápices. Sin salir a tocar granizo en tormentas.",
    use="Aprenderé a reconocer y diferenciar lluvia, granizo y nieve. Sirve para describir el tiempo cuando cae agua del cielo.",
    prior=["Sé que el agua puede ser líquida o sólida.", "Sé que las nubes tienen gotitas de agua."],
    explain=[
        "Las precipitaciones son agua que cae de las nubes. La lluvia son gotas de agua líquida. Puede ser suave o fuerte. Cae cuando las gotitas de las nubes se juntan y se hacen pesadas.",
        "El granizo son bolitas de hielo, duras. Cae en tormentas y puede hacer ruido al golpear un techo. La nieve son copos blancos y livianos de hielo. Cae cuando hace mucho frío y se acumula como una capa blanca.",
        "Para diferenciarlas me fijo en cómo caen y cómo son al llegar: la lluvia moja, el granizo es duro como una piedrita y la nieve es suave y se derrite al calentarse. En Chile, la nieve cae en la cordillera y en el sur; el granizo es poco frecuente.",
    ],
    vocab=[("precipitación", "agua que cae de las nubes"), ("lluvia", "gotas de agua líquida que caen"), ("granizo", "bolitas de hielo duras que caen en tormentas"), ("nieve", "copos blancos de hielo que caen con mucho frío"), ("copo", "pedacito blanco y liviano de nieve")],
    worked=[
        {"title": "Reconocer una precipitación", "problem": "Cae algo del cielo: son bolitas blancas y duras que rebotan en el suelo y suenan en el techo. ¿Qué es?", "steps": ["Son duras y rebotan: no son gotas.", "No son copos suaves.", "Las bolitas de hielo duras son granizo."], "answer": "Granizo"},
        {"title": "Cuándo cae nieve", "problem": "Una tarde la temperatura es de −2 °C y caen cosas blancas, livianas y suaves. ¿Qué precipitación es?", "steps": ["Son blancas y livianas.", "Hace mucho frío, bajo 0 °C.", "Eso es nieve."], "answer": "Nieve"},
    ],
    mistakes=[
        {"wrong": "Llamar lluvia a todo lo que cae del cielo.", "why": "Se usa una sola palabra para cosas distintas.", "fix": "Mira si es líquido (lluvia), bolitas duras (granizo) o copos suaves (nieve)."},
        {"wrong": "Pensar que la nieve y el granizo son lo mismo.", "why": "Los dos son hielo.", "fix": "El granizo es duro, en bolitas; la nieve son copos suaves."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál precipitación son gotas de agua líquida?", "La lluvia", "La lluvia son gotas de agua."),
            ex("¿Cuál precipitación son bolitas de hielo duras?", "El granizo", "El granizo es duro y redondo."),
            ex("¿Cuál precipitación son copos blancos y livianos?", "La nieve", "La nieve cae en copos."),
        ],
        "understand": [
            ex("¿Por qué se llama precipitación a la lluvia, la nieve y el granizo?", "Porque todas son agua que cae de las nubes", "Precipitar es caer."),
            ex("¿Qué diferencia hay entre granizo y nieve?", "El granizo son bolitas duras y la nieve son copos suaves", "Cambia cómo se forman y cómo llegan al suelo."),
            ex("¿La lluvia es agua líquida o sólida?", "Líquida", "La lluvia son gotas de agua líquida."),
        ],
        "apply": [
            ex("Descripción: copos blancos, livianos, caen en una montaña con −4 °C. ¿Qué precipitación es?", "Nieve", "Son copos y hace mucho frío."),
            ex("Descripción: gotas finas que mojan el patio, 12 °C. ¿Qué precipitación es?", "Lluvia", "Son gotas de agua líquida."),
            ex("Descripción: bolitas de hielo del tamaño de arvejas que rebotan en el suelo durante una tormenta. ¿Qué precipitación es?", "Granizo", "Son bolitas de hielo duras."),
        ],
        "reason": [
            ex("Luz dice: «Si cae algo blanco del cielo, siempre es nieve». ¿Qué evidencia le muestra que puede equivocarse?", "Que el granizo también es blanco y es de bolitas duras", "Hay que mirar cómo es lo que cae: copos o bolitas."),
            ex("Si la temperatura del suelo es de 15 °C, ¿es probable que la nieve se acumule? Explica.", "No", "Con 15 °C la nieve se derrite al llegar al suelo."),
        ],
        "challenge": [
            ex("Clasifica estas oraciones: A «gotas que mojan», B «bolitas duras que suenan en el techo», C «copos suaves que se acumulan». Escribe qué precipitación es cada una.", "A lluvia, B granizo, C nieve", "Cada característica corresponde a una precipitación."),
            ex("¿En qué se parecen y en qué se diferencian la lluvia y la nieve?", "Las dos caen de las nubes; la lluvia es líquida y la nieve es sólida", "Ambas son precipitaciones en distinto estado."),
        ],
    },
    context=[ex("En un viaje a la cordillera en invierno, Elena ve que caen copos blancos que se acumulan en el suelo, mientras en la ciudad llueve. ¿Qué precipitación hay en la cordillera?", "Nieve", "En la cordillera hace más frío y caen copos.")],
    selfcheck=[
        ex("¿Qué precipitación son bolitas de hielo?", "Granizo", "Es duro y redondo."),
        ex("¿La nieve es agua sólida o líquida?", "Sólida", "Son copos de hielo."),
        ex("¿Qué tienen en común lluvia, granizo y nieve?", "Todas caen de las nubes", "Las tres son precipitaciones."),
    ],
    open_task=task(
        "Haz una tabla con tres columnas: lluvia, granizo y nieve. Para cada una dibuja cómo es y escribe una palabra sobre cómo se siente al caer o tocarla. Después escribe una frase que explique cuál cae con más frío.",
        "Lluvia: gotas, moja. Granizo: bolitas duras, golpea. Nieve: copos livianos, suave. La nieve cae con más frío.",
        ["diferencia las tres", "usa dibujos y palabras", "relaciona la nieve con el frío"],
        ["tabla de tres columnas", "dibujos", "frase final"],
        ["mezclar granizo y nieve", "decir que la lluvia es sólida"],
        "Reconoce las diferencias bien marcadas y pide que cuente cómo se da cuenta de cuál precipitación es.",
    ),
    reinforce="Haz tres tarjetas con dibujos de lluvia, granizo y nieve, y pide que otra persona las clasifique con tu descripción.",
    extend="Averigua en qué zona de Chile es más frecuente la nieve y escribe una frase.",
)

register(
    OA12, 3,
    materials="Una tabla en papel con columnas de «viento» y «temperatura», lápiz de color y una ventana. Los datos vienen en este cuaderno. No uses termómetros de mercurio.",
    use="Aprenderé a describir el viento y la temperatura. Sirve para saber cómo vestirse y para contar cómo está el día.",
    prior=["Sé que la temperatura se mide en grados Celsius.", "Sé que el aire se puede mover."],
    explain=[
        "El viento es aire que se mueve. No lo veo, pero veo lo que hace: si las hojas apenas se mueven, el viento es suave; si se mueven las ramas grandes y vuela el polvo, el viento es fuerte. También puedo decir de dónde viene.",
        "La temperatura dice qué tan caliente o frío está el aire. Se mide con un termómetro en grados Celsius. En este cuaderno usaremos esta regla: menos de 10 °C es frío, entre 10 °C y 20 °C es templado, y más de 20 °C es caluroso.",
        "Hay que leer el termómetro y no adivinar. La sensación puede engañar: con viento fuerte siento más frío, pero la temperatura del aire es la misma. Por eso, para describir el día, uso un termómetro y miro cómo se mueven las cosas.",
    ],
    vocab=[("viento", "aire que se mueve"), ("brisa", "viento suave"), ("temperatura", "qué tan caliente o frío está el aire"), ("grado Celsius", "unidad de la temperatura, °C"), ("termómetro", "instrumento que mide la temperatura")],
    worked=[
        {"title": "Describir el viento", "problem": "En el patio las hojas de un árbol se mueven suavemente y las ramas grandes no se mueven. ¿Cómo es el viento?", "steps": ["Las hojas se mueven un poco.", "Las ramas grandes no se mueven.", "Es un viento suave, una brisa."], "answer": "Viento suave o brisa"},
        {"title": "Clasificar una temperatura", "problem": "El termómetro marca 7 °C. Con la regla del cuaderno, ¿es frío, templado o caluroso?", "steps": ["La regla: menos de 10 °C es frío.", "7 es menor que 10.", "Por lo tanto, es frío."], "answer": "Frío"},
    ],
    mistakes=[
        {"wrong": "Decir que la temperatura bajó porque el viento está fuerte.", "why": "El viento cambia la sensación, no la temperatura del aire.", "fix": "Lee el termómetro: la temperatura puede ser la misma aunque se sienta más frío."},
        {"wrong": "Decir que no hay viento porque no se ve.", "why": "El aire es invisible.", "fix": "Mira lo que mueve: hojas, ramas, banderas."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué es el viento?", "Aire que se mueve", "El viento es aire en movimiento."),
            ex("¿Con qué instrumento se mide la temperatura?", "Con un termómetro", "El termómetro mide qué tan caliente está el aire."),
            ex("Completa: la temperatura se escribe en grados ___.", "Celsius", "Se escribe °C."),
        ],
        "understand": [
            ex("¿Cómo sabes que hay viento si no lo ves?", "Porque veo cómo mueve hojas y ramas", "El viento se nota por lo que mueve."),
            ex("Con la regla del cuaderno, ¿cuántos grados tiene el límite entre frío y templado?", "10 °C", "Menos de 10 °C es frío."),
            ex("¿Qué pasa con la temperatura del aire cuando hay viento fuerte: cambia siempre o solo se siente distinto?", "Se siente distinta, pero puede ser la misma", "El viento cambia la sensación."),
        ],
        "apply": [
            ex("Un termómetro marca 24 °C. Con la regla del cuaderno, ¿es frío, templado o caluroso?", "Caluroso", "24 es mayor que 20."),
            ex("Un termómetro marca 15 °C. ¿Es frío, templado o caluroso?", "Templado", "15 está entre 10 y 20."),
            ex("En una bandera se ve que apenas se mueve. ¿El viento es suave o fuerte?", "Suave", "Se mueve poco."),
        ],
        "reason": [
            ex("Ana dice: «Hoy la temperatura bajó mucho porque se siente helado». El termómetro marca 16 °C, igual que ayer. ¿Qué puede estar pasando?", "Hay viento y se siente más frío, pero la temperatura es la misma", "El viento cambia la sensación, no el valor medido."),
            arith("A las 8:00 el termómetro marca 8 °C y a las 15:00 marca 18 °C. ¿Cuántos grados subió?", "18-8", "Se resta la temperatura de la mañana a la de la tarde.", " °C"),
        ],
        "challenge": [
            ex("Ordena de menor a mayor: 22 °C, 5 °C, 13 °C, 18 °C.", "5 °C, 13 °C, 18 °C, 22 °C", "Se comparan los números de menor a mayor."),
            ex("Hoy hay viento fuerte y 4 °C; ayer hubo brisa y 4 °C. ¿Cuál día se sintió más frío?", "Hoy", "El viento hace sentir más frío con la misma temperatura."),
        ],
    },
    context=[ex("Camila va a la plaza y ve que las ramas grandes de los árboles se mueven mucho y el termómetro de la farmacia marca 9 °C. ¿Cómo describe el viento y la temperatura?", "Viento fuerte y temperatura fría", "Las ramas grandes se mueven y 9 °C es menos de 10 °C.")],
    selfcheck=[
        ex("¿Qué mide el termómetro?", "La temperatura", "Mide qué tan caliente o frío está el aire."),
        ex("¿Qué es una brisa?", "Un viento suave", "Mueve poco las hojas."),
        ex("Con la regla del cuaderno, 12 °C ¿es frío o templado?", "Templado", "Está entre 10 y 20."),
    ],
    open_task=task(
        "Copia esta tabla y complétala. Lunes: hojas apenas se mueven, 11 °C. Martes: ramas grandes se mueven, 8 °C. Miércoles: no se mueve nada, 23 °C. Escribe para cada día si el viento es suave, fuerte o no hay, y si la temperatura es fría, templada o calurosa.",
        "Lunes: viento suave, templado. Martes: viento fuerte, frío. Miércoles: sin viento, caluroso.",
        ["clasifica el viento según lo que mueve", "clasifica la temperatura con la regla", "usa los datos de la tabla"],
        ["tabla completa", "dibujo de un día", "frase final"],
        ["confundir la sensación con la temperatura", "olvidar la regla de 10 y 20 °C"],
        "Valora el uso de la regla y pide que explique cómo decidió la clasificación de cada día.",
    ),
    reinforce="Mira durante un día qué cosas mueve el viento y haz una lista con dibujos.",
    extend="Anota la temperatura de tres momentos del día y escribe una frase sobre cuándo hace más calor.",
)

register(
    OA12, 4,
    materials="Una tabla en papel con los meses del año, lápices de colores y este cuaderno, que trae un registro de ejemplo de una ciudad de Chile central. Los datos son de ejemplo para practicar.",
    use="Aprenderé a describir cómo cambia el tiempo atmosférico a lo largo del año. Sirve para saber qué ropa usar y qué actividades hacer en cada época.",
    prior=["Sé qué es el tiempo atmosférico.", "Sé leer una tabla de datos."],
    explain=[
        "El tiempo atmosférico cambia a lo largo del año. En Chile, el verano va desde cerca del 21 de diciembre hasta cerca del 20 de marzo, el otoño hasta cerca del 21 de junio, el invierno hasta cerca del 22 de septiembre y la primavera hasta cerca del 21 de diciembre. Cada estación suele tener un tiempo típico.",
        "En Chile central, el verano suele ser más caluroso y con poca lluvia. En invierno hay más lluvia y más frío. Pero esto es una tendencia: en un día de verano puede haber nubes, y en uno de invierno puede salir el sol.",
        "Para ver cambios en el año, anoto datos varios meses. Si hago una tabla con la temperatura de cada mes, puedo ver cuándo sube y cuándo baja. Un solo mes no basta para saber cómo cambia el año.",
    ],
    vocab=[("estación", "época del año con un clima típico"), ("tendencia", "lo que suele pasar casi siempre"), ("registro anual", "tabla con datos de todo el año"), ("cambio", "diferencia entre un momento y otro"), ("promedio", "número que resume varios datos")],
    worked=[
        {"title": "Leer una tabla de temperaturas", "problem": "Datos de ejemplo de una ciudad: enero 25 °C, abril 17 °C, julio 9 °C, octubre 16 °C. ¿En qué mes hace más frío y en cuál más calor?", "steps": ["Comparo los números: 25, 17, 9 y 16.", "El menor es 9, en julio.", "El mayor es 25, en enero."], "answer": "Más frío en julio y más calor en enero"},
        {"title": "Cambio entre estaciones", "problem": "Con los mismos datos, ¿cuántos grados baja la temperatura entre enero y julio?", "steps": ["Enero: 25 °C.", "Julio: 9 °C.", "Resto: 25 − 9 = 16."], "answer": "Baja 16 °C"},
    ],
    mistakes=[
        {"wrong": "Decir que en todo el año el tiempo es igual.", "why": "No se compara entre meses.", "fix": "Mira la tabla de todos los meses: hay cambios de temperatura y lluvia."},
        {"wrong": "Decir que como un día de julio estuvo caluroso, el invierno no es frío.", "why": "Se usa un solo día para decidir.", "fix": "Mira el patrón de muchos días."},
    ],
    tiers={
        "recovery": [
            ex("En Chile, ¿el verano empieza cerca del 21 de diciembre?", "Sí", "En el hemisferio sur el verano comienza hacia el 21 de diciembre."),
            ex("¿En qué estación suele haber más lluvia en Chile central?", "En invierno", "En Chile central llueve más en invierno."),
            ex("Completa: una tabla con datos de todo el año es un registro ___.", "anual", "Anual quiere decir de todo el año."),
        ],
        "understand": [
            ex("¿Por qué el tiempo cambia durante el año?", "Porque cambian las estaciones y su tiempo típico", "Cada estación tiene un patrón de tiempo."),
            ex("¿Qué quiere decir «tendencia»?", "Lo que suele pasar casi siempre", "No siempre pasa, pero es lo más común."),
            ex("¿Un día de lluvia en enero cambia la estación a invierno?", "No", "Sigue siendo verano."),
        ],
        "apply": [
            arith("Datos de ejemplo: enero 28 °C y julio 11 °C. ¿Cuántos grados baja la temperatura entre enero y julio?", "28-11", "Se resta la temperatura baja a la alta.", " °C"),
            ex("En una tabla de ejemplo, la lluvia mensual es: enero 0 mm, abril 20 mm, julio 80 mm, octubre 30 mm. ¿En qué mes llueve más?", "Julio", "80 es el número mayor."),
            ex("Con los mismos datos de lluvia, ¿en qué mes no llueve nada?", "Enero", "Tiene 0 mm."),
        ],
        "reason": [
            ex("Pedro dice: «El 15 de julio hizo 21 °C, así que en invierno nunca hace frío». Pero la mayoría de los días de julio marcó menos de 10 °C. ¿Cuál es el error?", "Usó un solo día en vez del patrón de muchos días", "El invierno se describe con la mayoría de los días."),
            ex("Una tabla muestra temperaturas: enero 26 °C, abril 18 °C, julio 10 °C, octubre 17 °C. ¿Qué mes se parece más a abril en temperatura?", "Octubre", "17 °C es el valor más cercano a 18 °C."),
        ],
        "challenge": [
            ex("Un niño dice: «Los datos de ejemplo me muestran que enero es el mes más cálido en cualquier lugar del planeta». ¿Por qué eso no se puede afirmar?", "Porque son datos de una sola ciudad", "Otros lugares pueden tener otro patrón."),
            ex("Con los datos enero 25 °C, abril 17 °C, julio 9 °C, octubre 16 °C, ¿entre qué dos meses sube la temperatura de nuevo después de bajar?", "Entre julio y octubre", "De 9 a 16 °C sube."),
        ],
    },
    context=[ex("En la casa de Valentina, en febrero ella usa polera y sale al patio con sol; en julio usa abrigo y paraguas. ¿Qué cambios del año se pueden anotar para esos dos meses?", "En febrero más calor y poca lluvia; en julio más frío y más lluvia", "Es el patrón típico de Chile central.")],
    selfcheck=[
        ex("¿En qué estación suele hacer más frío?", "Invierno", "Es la estación más fría."),
        ex("¿Una tabla con varios meses ayuda a ver los cambios del año?", "Sí", "Se comparan los datos."),
        ex("¿Un solo día muestra todo el año?", "No", "Hay que mirar muchos datos."),
    ],
    open_task=task(
        "Con estos datos de ejemplo, dibuja una tabla y colorea cada mes con un color según la temperatura: enero 27 °C, abril 18 °C, julio 8 °C, octubre 16 °C. Escribe cuál es el mes más frío, cuál es el más cálido, y una frase que describa cómo cambia el año.",
        "El mes más frío es julio (8 °C) y el más cálido, enero (27 °C). La temperatura baja de enero a julio y vuelve a subir hacia octubre.",
        ["ubica el mes más frío y el más cálido", "describe el patrón del año", "usa los datos de la tabla"],
        ["tabla coloreada", "dos datos marcados", "frase de patrón"],
        ["afirmar sin mirar los datos", "decir que no hay cambios"],
        "Valora el uso de la tabla y pregunta qué dato más agregaría para estar más seguro del patrón.",
    ),
    reinforce="Haz un dibujo de cuatro cuadros con el tiempo típico de verano, otoño, invierno y primavera.",
    extend="Pregunta a un adulto qué recuerda del tiempo de su infancia en tu zona y compáralo con lo que ves hoy.",
)
