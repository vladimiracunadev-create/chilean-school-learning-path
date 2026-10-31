"""Student material for 5.º básico Matemática, OA 24 (posibilidad de un evento: seguro, posible, poco posible, imposible)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA24 = "MA05 OA 24"

BOLSA_A = "Bolsa A: 8 fichas, todas rojas."
BOLSA_B = "Bolsa B: 10 fichas, 5 rojas y 5 azules."
BOLSA_C = "Bolsa C: 12 fichas, 1 roja y 11 azules."
BOLSA_D = "Bolsa D: 10 fichas, todas azules."
DADO = "Un dado normal tiene 6 caras con los números 1, 2, 3, 4, 5 y 6."
RULETA = "Ruleta de 8 sectores iguales: 3 amarillos, 4 verdes y 1 rojo. Se gira la flecha y se mira en qué sector cae."
TARJ = "Una bolsa tiene 12 tarjetas numeradas del 1 al 12, una de cada número. Se saca una tarjeta sin mirar."
INICIAL = "Una bolsa tiene 10 fichas: 4 rojas, 5 azules y 1 verde. Se saca una ficha sin mirar."
LANZ = "Lucía lanzó un dado normal 12 veces y anotó estos resultados: 3, 5, 1, 6, 2, 3, 4, 5, 6, 1, 2, 3."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


REGLA = "Regla de este cuaderno: seguro es cuando todos los resultados cumplen el evento; imposible, cuando ninguno lo cumple; poco posible, cuando lo cumplen solo 1 o 2 resultados entre muchos; posible, cuando lo cumple la mitad o más, pero no todos. En los casos intermedios, como 3 de 12, este cuaderno no te pide clasificar."

register(
    OA24, 1,
    materials="Lápiz y papel. Todas las bolsas, dados y fichas están descritos con palabras y números dentro de cada ejercicio.",
    use="Aprenderé a describir qué tan posible es que ocurra un evento usando las palabras seguro, posible, poco posible e imposible. Sirve para hablar con precisión del azar.",
    prior=["Sé contar y comparar cantidades.", "Sé qué es un resultado: lo que ocurre al hacer un experimento."],
    explain=[
        "Un experimento aleatorio es uno en que no puedes saber el resultado antes de hacerlo, porque depende del azar. Sacar una ficha de una bolsa sin mirar o lanzar un dado son experimentos aleatorios. Un evento es lo que quieres que ocurra, por ejemplo «sacar una ficha roja».",
        "Para describir qué tan posible es un evento usamos cuatro palabras. Es seguro si ocurre siempre. Es imposible si no puede ocurrir nunca. Es posible si puede ocurrir y también no ocurrir. Es poco posible si puede ocurrir, pero casi siempre no ocurre.",
        "Para decidir, mira qué hay en la bolsa. Si todas las fichas son rojas, sacar roja es seguro y sacar azul es imposible. Si hay muchas de cada color, sacar cada color es posible. Si hay solo una roja entre muchas azules, sacar roja es poco posible. " + REGLA,
    ],
    vocab=[("experimento aleatorio", "experimento cuyo resultado depende del azar"), ("evento", "lo que queremos que ocurra en el experimento"), ("seguro", "ocurre siempre, en todos los resultados"), ("imposible", "no ocurre en ningún resultado"), ("poco posible", "ocurre en muy pocos resultados"), ("posible", "puede ocurrir y puede no ocurrir")],
    worked=[
        {"title": "Un evento seguro y uno imposible", "problem": BOLSA_A + " Sin mirar, se saca una ficha. Describe «sacar una ficha roja» y «sacar una ficha azul».", "steps": ["Las 8 fichas son rojas, así que en todos los resultados sale roja.", "Ninguna ficha es azul, así que en ningún resultado sale azul."], "answer": "Sacar roja es seguro y sacar azul es imposible"},
        {"title": "Un evento poco posible", "problem": BOLSA_C + " Sin mirar, se saca una ficha. Describe «sacar la ficha roja».", "steps": ["Solo 1 de las 12 fichas es roja.", "Puede ocurrir, pero en casi todos los resultados no ocurre."], "answer": "Sacar la ficha roja es poco posible"},
    ],
    mistakes=[
        {"wrong": "Decir que sacar roja es seguro porque en la bolsa hay fichas rojas.", "why": "Se mira que haya rojas, pero no si hay fichas de otros colores.", "fix": "Es seguro solo si todas las fichas son rojas."},
        {"wrong": "Decir que sacar un resultado que es muy raro es imposible.", "why": "Se confunde poco posible con imposible.", "fix": "Si puede ocurrir aunque sea una vez, no es imposible."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál de estas es un experimento aleatorio? A) Lanzar un dado y mirar el número. B) Contar los dedos de tu mano.", "A", "El número del dado depende del azar; los dedos ya se conocen."),
            ex("En un evento imposible, ¿en cuántos resultados ocurre el evento?", "En ninguno", "Imposible significa que no puede ocurrir nunca."),
            ex(BOLSA_A + " Evento: sacar una ficha roja. ¿Es seguro, posible, poco posible o imposible?", "Seguro", "Las 8 fichas son rojas."),
        ],
        "understand": [
            ex(BOLSA_A + " Evento: sacar una ficha azul. ¿Es seguro, posible, poco posible o imposible?", "Imposible", "No hay ninguna ficha azul."),
            ex(BOLSA_B + " Evento: sacar una ficha roja. ¿Es seguro, posible, poco posible o imposible?", "Posible", "Hay 5 rojas de 10: puede ocurrir y puede no ocurrir."),
            ex(BOLSA_C + " Evento: sacar la ficha roja. ¿Es seguro, posible, poco posible o imposible?", "Poco posible", "Solo 1 de 12 fichas es roja."),
        ],
        "apply": [
            ex(DADO + " Se lanza el dado. Evento: sale un número menor que 7. ¿Es seguro, posible, poco posible o imposible?", "Seguro", "Los seis números son menores que 7."),
            ex(DADO + " Se lanza el dado. Evento: sale el número 9. ¿Es seguro, posible, poco posible o imposible?", "Imposible", "Ninguna cara tiene un 9."),
            ex(DADO + " Se lanza el dado. Evento: sale el número 6. ¿Es seguro, posible, poco posible o imposible?", "Poco posible", "Solo 1 de las 6 caras tiene un 6."),
        ],
        "reason": [
            ex("Luis dice: «En la bolsa B hay fichas rojas, así que sacar roja es seguro». ¿Qué error tiene?", "Hay también fichas azules; es posible, no seguro", "Para ser seguro, todas las fichas tendrían que ser rojas."),
            ex("Ana dice que en la bolsa C sacar una ficha azul es imposible porque hay una roja. ¿Tiene razón?", "No; hay 11 azules, así que es posible", "Imposible significa que no hay ninguna ficha azul."),
        ],
        "challenge": [
            ex("Una bolsa tiene 9 fichas verdes y 1 amarilla. ¿Cuál evento es seguro? A) sacar verde B) sacar verde o amarilla C) sacar amarilla", "B", "Cualquier ficha es verde o amarilla."),
            ex("A la bolsa A (8 fichas rojas) le agregas 1 ficha azul. ¿Sacar azul sigue siendo imposible? Responde sí o no y explica.", "No; ahora hay una ficha azul y puede salir", "Imposible es cuando no hay ninguna ficha azul."),
        ],
    },
    context=[ex("Para sortear un libro se ponen en una caja 20 papeles, uno con el nombre de cada estudiante del curso. Se saca un papel sin mirar. Para tu nombre, ¿sacarlo es seguro, posible, poco posible o imposible?", "Poco posible", "Tu nombre está en solo 1 de los 20 papeles.")],
    selfcheck=[
        ex(BOLSA_D + " Evento: sacar una ficha roja. ¿Es seguro, posible, poco posible o imposible?", "Imposible", "Las 10 fichas son azules."),
        ex(DADO + " Se lanza el dado. Evento: sale un número entre 1 y 6. ¿Es seguro, posible, poco posible o imposible?", "Seguro", "Todas las caras tienen un número entre 1 y 6."),
        ex(BOLSA_B + " Evento: sacar una ficha azul. ¿Es seguro, posible, poco posible o imposible?", "Posible", "Hay 5 azules de 10 fichas."),
    ],
    open_task=task(
        "Una caja tiene 6 cubos azules. Escribe un evento seguro y un evento imposible para sacar un cubo sin mirar. Después imagina cómo cambiarías la caja para que sacar un cubo rojo sea poco posible, y escribe qué pondrías en ella.",
        "Seguro: sacar un cubo azul. Imposible: sacar un cubo rojo. Para que sacar rojo sea poco posible, pondría 1 cubo rojo y 11 azules.",
        ["escribe un evento seguro y uno imposible", "usa las palabras con su sentido", "propone una caja con pocos cubos rojos entre muchos azules"],
        ["evento seguro", "evento imposible", "nueva caja"],
        ["decir seguro cuando solo hay algunos", "confundir poco posible con imposible"],
        "Pide contar cuántos cubos de cada color hay en la caja nueva. Reconoce que use las cuatro palabras con precisión.",
    ),
    reinforce="Con una bolsa de tela y tapas de botellas del mismo color, di qué es seguro e imposible al sacar una sin mirar.",
    extend="Inventa tres bolsas con fichas y escribe un evento seguro, uno posible y uno imposible para cada una.",
)

register(
    OA24, 2,
    materials="Lápiz y papel. Las ruletas, bolsas y la recta están descritas con palabras en cada ejercicio; puedes dibujarlas.",
    use="Aprenderé a pasar de una descripción con palabras a una ruleta, una bolsa o una recta de posibilidad. Sirve para ver que son formas distintas de decir lo mismo.",
    prior=["Sé las palabras seguro, posible, poco posible e imposible.", "Sé qué es un evento."],
    explain=[
        "Una situación de azar se puede mostrar de varias maneras. Con palabras: «sacar roja es poco posible». Con una bolsa: 1 ficha roja y 11 azules. Con una ruleta: una ruleta con sectores iguales, donde pocos son rojos. Las tres dicen lo mismo.",
        "Una ruleta es un círculo dividido en sectores iguales con una flecha que gira. Como todos los sectores son iguales, cada uno tiene la misma posibilidad. Si hay 8 sectores y 1 es rojo, caer en rojo es poco posible.",
        "La recta de posibilidad ordena las cuatro palabras. A la izquierda va imposible, que nunca ocurre. Luego poco posible, después posible y, a la derecha, seguro, que siempre ocurre. Cuanto más a la derecha, más fácil es que el evento ocurra. " + REGLA,
    ],
    vocab=[("ruleta", "círculo con sectores iguales y una flecha que gira"), ("sector", "cada parte igual de una ruleta"), ("recta de posibilidad", "línea que ordena imposible, poco posible, posible y seguro"), ("representación", "forma de mostrar una situación, como palabras, un dibujo o una bolsa")],
    worked=[
        {"title": "De la ruleta a las palabras", "problem": RULETA + " Describe «cae en verde» y «cae en rojo».", "steps": ["Hay 4 sectores verdes de 8: la mitad.", "Hay 1 sector rojo de 8: solo uno."], "answer": "Caer en verde es posible; caer en rojo es poco posible"},
        {"title": "De las palabras a la bolsa", "problem": "Se pide una bolsa donde «sacar una ficha roja» sea imposible. ¿Sirve una bolsa con 3 fichas azules y 4 verdes?", "steps": ["En la bolsa no hay ninguna ficha roja.", "Entonces en ningún resultado sale roja."], "answer": "Sí sirve; sacar roja es imposible"},
    ],
    mistakes=[
        {"wrong": "Pensar que en una ruleta cae más en el sector más cercano a la flecha.", "why": "Se piensa que la flecha elige por cercanía.", "fix": "Los sectores son iguales, y lo que cuenta es cuántos sectores cumplen el evento."},
        {"wrong": "Poner posible a la izquierda de poco posible en la recta.", "why": "Se ordena sin pensar en qué tan fácil es que ocurra.", "fix": "De izquierda a derecha: imposible, poco posible, posible, seguro."},
    ],
    tiers={
        "recovery": [
            ex("En la recta de posibilidad, ¿qué palabra va en el extremo izquierdo, donde el evento nunca ocurre?", "Imposible", "Es el punto donde el evento no puede ocurrir."),
            ex("En la recta de posibilidad, ¿qué palabra va en el extremo derecho, donde el evento siempre ocurre?", "Seguro", "Es el punto donde el evento ocurre en todos los resultados."),
            ex("Una ruleta tiene 6 sectores iguales, todos azules. Evento: la flecha cae en azul. ¿Seguro, posible, poco posible o imposible?", "Seguro", "Todos los sectores son azules."),
        ],
        "understand": [
            ex(RULETA + " Evento: cae en rojo. ¿Seguro, posible, poco posible o imposible?", "Poco posible", "Solo 1 sector de 8 es rojo."),
            ex(RULETA + " Evento: cae en verde. ¿Seguro, posible, poco posible o imposible?", "Posible", "4 sectores de 8 son verdes: la mitad."),
            ex(RULETA + " Evento: cae en morado. ¿Seguro, posible, poco posible o imposible?", "Imposible", "Ningún sector es morado."),
        ],
        "apply": [
            ex("Se busca una bolsa donde sacar una ficha roja sea poco posible. ¿Cuál sirve? A) 10 fichas rojas B) 1 roja y 11 azules C) 6 rojas y 6 azules D) 12 azules", "B", "Solo 1 de las 12 fichas es roja."),
            ex("Se busca una bolsa donde sacar una ficha roja sea imposible. ¿Cuál sirve? A) 7 rojas B) 3 rojas y 4 azules C) 7 azules D) 1 roja y 6 azules", "C", "Solo la bolsa C no tiene fichas rojas."),
            ex("Se busca una bolsa donde sacar una ficha roja sea seguro. ¿Cuál sirve? A) 5 rojas y 1 azul B) 6 rojas C) 6 azules D) 3 rojas y 3 azules", "B", "Solo en B todas las fichas son rojas."),
        ],
        "reason": [
            ex("Bolsa X: 4 rojas y 4 azules. Bolsa Y: 1 roja y 7 azules. Evento: sacar una ficha roja. ¿Cómo es el evento en X y en Y?", "En X es posible y en Y es poco posible", "En X hay la mitad de rojas; en Y solo 1 de 8."),
            ex("Sofía dibujó una ruleta de 8 sectores iguales, todos azules, y dice que «caer en azul es posible». Con la regla de este cuaderno, ¿cómo lo describirías?", "Seguro, porque todos los sectores son azules", "Si todos los sectores cumplen, el evento es seguro."),
        ],
        "challenge": [
            ex("Una ruleta tiene 10 sectores iguales: 1 rojo y 9 azules. Clasifica en orden «cae en rojo», «cae en azul» y «cae en verde».", "Poco posible, posible, imposible", "Rojo 1 de 10; azul 9 de 10, no todos; verde ninguno."),
            ex("Ordena de izquierda a derecha en la recta de posibilidad las cuatro palabras: seguro, posible, imposible, poco posible.", "Imposible, poco posible, posible, seguro", "Va de lo que nunca ocurre a lo que siempre ocurre."),
        ],
    },
    context=[ex("En una caja hay 12 lápices: 11 negros y 1 rojo. Sin mirar, sacas un lápiz. Clasifica «sacar el lápiz rojo».", "Poco posible", "Solo 1 de los 12 lápices es rojo.")],
    selfcheck=[
        ex("¿Qué palabra va entre «poco posible» y «seguro» en la recta de posibilidad?", "Posible", "El orden es imposible, poco posible, posible, seguro."),
        ex("Una ruleta de 4 sectores iguales tiene 2 verdes y 2 azules. Evento: cae en azul. ¿Seguro, posible, poco posible o imposible?", "Posible", "La mitad de los sectores son azules."),
        ex("Una bolsa tiene 12 fichas amarillas. Evento: sacar una ficha amarilla. ¿Seguro, posible, poco posible o imposible?", "Seguro", "Todas las fichas son amarillas."),
    ],
    open_task=task(
        "Dibuja una recta de posibilidad con las cuatro palabras. Luego dibuja una ruleta de 8 sectores iguales pintados con dos colores (1 sector de un color y 7 del otro, o 4 y 4) y ubica sobre la recta un evento de cada color, explicando por qué va ahí.",
        "Ruleta: 7 sectores azules y 1 verde. «Cae en verde» va en poco posible porque es 1 de 8. «Cae en azul» va en posible porque 7 de 8 no son todos.",
        ["recta con el orden correcto", "ruleta con 8 sectores iguales", "ubica ambos eventos y explica con el número de sectores"],
        ["recta", "ruleta", "explicación"],
        ["ordenar mal las palabras", "dibujar sectores desiguales"],
        "Pide contar cuántos sectores tiene cada color. Reconoce que relacione el dibujo con la palabra.",
    ),
    reinforce="Dibuja tres ruletas distintas y escribe una palabra de posibilidad para caer en un color de cada una.",
    extend="Escribe una situación con un dado y otra con una bolsa que se describan con la misma palabra, por ejemplo poco posible.",
)

register(
    OA24, 3,
    materials="Lápiz y papel. Las tarjetas están descritas con sus números dentro de cada ejercicio.",
    use="Aprenderé una estrategia para decidir qué tan posible es un evento: listar los resultados, contar cuáles cumplen y justificar. Sirve para dar razones y no adivinar.",
    prior=["Sé las cuatro palabras de posibilidad.", "Sé reconocer números pares, impares y de una cifra."],
    explain=[
        "Una buena estrategia tiene tres pasos. Primero, escribe todos los resultados posibles. Segundo, cuenta cuántos de ellos cumplen el evento. Tercero, compara: si ninguno cumple es imposible, si todos cumplen es seguro, si solo 1 o 2 entre muchos es poco posible y, si la mitad o más pero no todos, es posible.",
        "Justificar es explicar por qué elegiste una palabra, usando números. Por ejemplo: «Sacar un número par es posible porque 6 de las 12 tarjetas son pares y las otras 6 no». Una justificación sin números, como «porque sí», no sirve.",
        "El azar no tiene memoria. Si una tarjeta salió dos veces seguidas, eso no significa que no volverá a salir ni que saldrá otra vez. Si devuelves la tarjeta a la bolsa, el siguiente intento empieza igual que el primero. " + REGLA,
    ],
    vocab=[("resultado", "cada cosa que puede salir en el experimento"), ("cumple el evento", "es uno de los resultados que queremos"), ("justificar", "explicar una decisión con razones y números"), ("devolver", "volver a poner lo sacado, para que todo quede igual")],
    worked=[
        {"title": "Contar resultados que cumplen", "problem": TARJ + " Describe el evento «sale un número par».", "steps": ["Los pares del 1 al 12 son 2, 4, 6, 8, 10 y 12: son 6 de 12.", "Ni todos ni casi ninguno: puede ocurrir y puede no ocurrir."], "answer": "Es posible, porque 6 de las 12 tarjetas son pares"},
        {"title": "Un resultado entre muchos", "problem": TARJ + " Describe el evento «sale el número 12».", "steps": ["Hay una sola tarjeta con 12.", "1 de 12 tarjetas cumple el evento."], "answer": "Es poco posible, porque solo 1 de las 12 tarjetas es la del 12"},
    ],
    mistakes=[
        {"wrong": "Decir «salió el 7 dos veces, así que ahora es seguro que no sale».", "why": "Se cree que el azar recuerda lo que ocurrió antes.", "fix": "Si devuelves la tarjeta, sacar 7 sigue siendo poco posible."},
        {"wrong": "Justificar solo con «porque hay muchas tarjetas».", "why": "No se cuentan los resultados que cumplen.", "fix": "Escribe cuántas tarjetas cumplen y cuántas hay en total."},
    ],
    tiers={
        "recovery": [
            ex(TARJ + " ¿Cuántos resultados posibles hay en total?", "12", "Hay una tarjeta de cada número del 1 al 12."),
            ex(TARJ + " ¿Cuántas tarjetas tienen un número mayor que 9?", "3", "Son las tarjetas 10, 11 y 12."),
            ex(TARJ + " Evento: sale un número menor que 13. ¿Seguro, posible, poco posible o imposible?", "Seguro", "Todos los números del 1 al 12 son menores que 13."),
        ],
        "understand": [
            ex(TARJ + " Evento: sale el número 15. ¿Seguro, posible, poco posible o imposible?", "Imposible", "No existe la tarjeta 15."),
            ex(TARJ + " Evento: sale un número impar. ¿Seguro, posible, poco posible o imposible?", "Posible", "Son 6 impares de 12: 1, 3, 5, 7, 9 y 11."),
            ex(TARJ + " Evento: sale el número 4. ¿Seguro, posible, poco posible o imposible?", "Poco posible", "Solo 1 tarjeta de las 12 tiene un 4."),
        ],
        "apply": [
            ex(TARJ + " Evento: sale un número mayor que 10. ¿Seguro, posible, poco posible o imposible?", "Poco posible", "Solo 2 tarjetas cumplen: la 11 y la 12."),
            ex(TARJ + " Evento: sale un número de una sola cifra. ¿Seguro, posible, poco posible o imposible?", "Posible", "Son 9 tarjetas, del 1 al 9, de las 12."),
            ex(TARJ + " Evento: sale un número que termina en 0. ¿Seguro, posible, poco posible o imposible?", "Poco posible", "Solo la tarjeta 10 termina en 0."),
        ],
        "reason": [
            ex("Tomás dice: «El 7 salió las dos últimas veces, así que ahora es seguro que no sale 7». Las tarjetas se devuelven a la bolsa. ¿Qué respondes?", "Está equivocado; sacar el 7 sigue siendo poco posible", "Al devolver la tarjeta vuelven a estar las 12 tarjetas."),
            ex("Valeria dice: «Sale un número mayor que 6 es seguro porque hay muchos números grandes». Con las tarjetas del 1 al 12, ¿es correcto?", "No; las tarjetas 1 a 6 no cumplen, por lo que es posible", "Ocurre en 6 de 12, no en todas."),
        ],
        "challenge": [
            ex(TARJ + " Quitas todas las tarjetas con número impar. Ahora, ¿cómo es el evento «sale un número par»?", "Seguro", "Quedan solo las pares, y todas cumplen."),
            ex(TARJ + " Quitas todas las tarjetas con número menor que 12. ¿Qué tarjeta queda y cómo es «sale 12»?", "Queda la 12 y sale con seguridad", "Es la única tarjeta, así que sale siempre."),
        ],
    },
    context=[ex("Se sortea un libro entre 30 estudiantes: hay 30 papeles con un nombre cada uno, y se saca uno sin mirar. Para tu nombre, ¿sacarlo es seguro, posible, poco posible o imposible?", "Poco posible", "Tu nombre está en solo 1 de los 30 papeles.")],
    selfcheck=[
        ex(TARJ + " Evento: sale un número mayor que 0. ¿Seguro, posible, poco posible o imposible?", "Seguro", "Los 12 números son mayores que 0."),
        ex(TARJ + " Evento: sale un número menor que 1. ¿Seguro, posible, poco posible o imposible?", "Imposible", "Ninguna tarjeta tiene un número menor que 1."),
        ex("En la estrategia de tres pasos, ¿en qué paso se cuenta cuántos resultados cumplen el evento: primero, segundo o tercero?", "Segundo", "Primero se listan, segundo se cuentan y tercero se compara."),
    ],
    open_task=task(
        "Una bolsa tiene 10 tarjetas numeradas del 1 al 10, una de cada número. Elige tres eventos distintos para sacar una tarjeta sin mirar, de modo que cumplan 0, 1, 5 o 10 tarjetas, y clasifica cada uno con una de las cuatro palabras. Justifica cada uno con la cantidad de tarjetas que cumplen.",
        "«Sale un número par»: posible, 5 de 10. «Sale el 10»: poco posible, 1 de 10. «Sale un número mayor que 10»: imposible, 0 de 10.",
        ["usa tres eventos distintos", "cada palabra va con su justificación numérica", "cuenta bien las tarjetas que cumplen"],
        ["tres eventos", "palabras", "conteos"],
        ["justificar sin números", "contar mal las tarjetas"],
        "Pide escribir la lista de tarjetas que cumplen cada evento. Reconoce la justificación con números.",
    ),
    reinforce="Con tarjetas numeradas del 1 al 10 hechas de papel, escribe una lista de eventos y cuántas tarjetas los cumplen.",
    extend="Escribe un evento con tarjetas del 1 al 20 que sea poco posible y otro que sea posible, justificando con números.",
)

register(
    OA24, 4,
    materials="Lápiz y papel. La bolsa y sus cambios están descritos con palabras dentro de cada ejercicio.",
    use="Aprenderé a ver cómo cambia la posibilidad cuando se agregan o se sacan fichas de una bolsa. Sirve para entender cómo se puede cambiar un experimento para lograr lo que queremos.",
    prior=["Sé decidir si un evento es seguro, posible, poco posible o imposible.", "Sé contar fichas por color."],
    explain=[
        "A veces cambia la condición del experimento: se agregan fichas, se quitan o se cambian por otro color. Cuando eso pasa, hay que volver a contar. La palabra que usabas antes puede cambiar, o puede seguir igual.",
        "Si agregas una ficha de un color que no estaba, el evento «sacar ese color» deja de ser imposible. Si quitas todas las fichas de un color, el evento «sacar ese color» pasa a ser imposible. Si dejas solo un color, sacar ese color pasa a ser seguro.",
        "Un método ordenado: escribe cómo queda la bolsa después del cambio, cuenta las fichas de cada color y decide con la regla. No uses la bolsa antigua. " + REGLA,
    ],
    vocab=[("agregar", "poner más fichas"), ("quitar", "sacar fichas y dejarlas fuera"), ("cambio de condición", "algo que se modifica en el experimento"), ("bolsa nueva", "cómo queda la bolsa después del cambio")],
    worked=[
        {"title": "Agregar una ficha de un color nuevo", "problem": INICIAL + " Agregas 1 ficha amarilla. Describe «sacar una ficha amarilla».", "steps": ["Antes no había amarillas: era imposible.", "Ahora hay 1 amarilla entre 11 fichas."], "answer": "Pasa de imposible a poco posible"},
        {"title": "Quitar fichas", "problem": INICIAL + " Quitas las 4 rojas y la verde. Describe «sacar una ficha azul».", "steps": ["Quedan solo las 5 azules.", "Todas las fichas cumplen el evento."], "answer": "Sacar azul es seguro"},
    ],
    mistakes=[
        {"wrong": "Usar la bolsa original después de agregar o quitar fichas.", "why": "No se tiene en cuenta la condición nueva.", "fix": "Escribe primero cómo queda la bolsa y cuenta de nuevo."},
        {"wrong": "Pensar que agregar muchas fichas de un color hace que sea seguro sacarlo.", "why": "Se ignora que siguen las fichas de otros colores.", "fix": "Es seguro solo si ya no queda ninguna ficha de otro color."},
    ],
    tiers={
        "recovery": [
            ex(INICIAL + " Evento: sacar la ficha verde. ¿Seguro, posible, poco posible o imposible?", "Poco posible", "Solo 1 ficha de 10 es verde."),
            ex(INICIAL + " Evento: sacar una ficha azul. ¿Seguro, posible, poco posible o imposible?", "Posible", "5 de 10 fichas son azules."),
            ex(INICIAL + " Evento: sacar una ficha amarilla. ¿Seguro, posible, poco posible o imposible?", "Imposible", "No hay ninguna ficha amarilla."),
        ],
        "understand": [
            ex(INICIAL + " Agregas 1 ficha amarilla. ¿Cómo es ahora «sacar una ficha amarilla»?", "Poco posible", "Hay 1 amarilla entre 11 fichas."),
            ex(INICIAL + " Sacas la ficha verde y la dejas fuera. ¿Cómo es ahora «sacar una ficha verde»?", "Imposible", "Ya no queda ninguna ficha verde."),
            ex(INICIAL + " Quitas todas las fichas rojas y todas las azules. ¿Cómo es ahora «sacar una ficha verde»?", "Seguro", "Solo queda la verde."),
        ],
        "apply": [
            ex(INICIAL + " Quitas las 4 rojas. ¿Cómo es ahora «sacar una ficha roja»?", "Imposible", "No queda ninguna ficha roja."),
            ex(INICIAL + " Quitas las 5 azules y las 4 rojas, y agregas 5 fichas verdes. ¿Cómo es «sacar una ficha verde»?", "Seguro", "Quedan solo 6 fichas, todas verdes."),
            ex(INICIAL + " Cambias las 5 fichas azules por 5 fichas verdes. ¿Cómo es «sacar una ficha verde»?", "Posible", "Habría 6 verdes de 10 fichas, y no todas son verdes."),
        ],
        "reason": [
            ex("Camila quiere que sacar verde sea seguro en la bolsa inicial y dice que basta agregar 9 fichas verdes. ¿Tiene razón?", "No; siguen las rojas y azules, por lo que sería posible", "Para ser seguro, no puede quedar ninguna ficha de otro color."),
            ex(INICIAL + " Pablo saca una ficha roja y no la devuelve. Dice que sacar azul sigue siendo posible. ¿Tiene razón?", "Sí; quedan 5 azules entre 9 fichas, así que puede ocurrir y no ocurrir", "Hay fichas azules y de otros colores."),
        ],
        "challenge": [
            ex(INICIAL + " ¿Cuáles son las únicas fichas que hay que quitar para que «sacar roja» sea imposible y «sacar azul» siga siendo posible?", "Las 4 rojas", "Con 5 azules y 1 verde, azul sigue ocurriendo en algunos resultados."),
            ex(INICIAL + " Quitas las fichas azules y las verdes. Solo quedan las rojas. ¿Cómo es «sacar roja» y cómo es «sacar azul»?", "Sacar roja es seguro y sacar azul es imposible", "Todas las fichas que quedan son rojas."),
        ],
    },
    context=[ex("En una urna del colegio hay 15 papeles blancos y 1 azul. Se va a sacar uno sin mirar, pero antes agregan 14 papeles azules más. ¿Cómo es «sacar un papel azul» antes y después?", "Antes es poco posible y después es posible", "Antes hay 1 azul de 16; después hay 15 azules de 30, la mitad.")],
    selfcheck=[
        ex("Una bolsa tiene 6 fichas rojas. Agregas 1 ficha azul. ¿Cómo es ahora «sacar una ficha azul»?", "Poco posible", "Hay 1 azul entre 7 fichas."),
        ex("Una bolsa tiene 3 fichas rojas y 3 azules. Quitas las 3 rojas. ¿Cómo es «sacar azul»?", "Seguro", "Quedan solo azules."),
        ex("Una bolsa tiene 4 fichas rojas y 4 azules. Agregas 1 ficha verde. ¿Sacar verde es imposible?", "No; es poco posible", "Ahora hay 1 verde entre 9 fichas."),
    ],
    open_task=task(
        "Tienes una bolsa con 3 fichas azules y 3 rojas. Escribe un cambio que haga que sacar azul sea seguro, otro que lo haga imposible y otro que lo deje posible (que queden al menos tantas azules como rojas, y alguna roja). Para cada cambio escribe cómo queda la bolsa y la palabra.",
        "Quito las 3 rojas: quedan 3 azules y sacar azul es seguro. Quito las 3 azules: sacar azul es imposible. Agrego 1 azul: 4 azules y 3 rojas, sacar azul es posible.",
        ["tres cambios distintos", "describe cómo queda la bolsa", "usa la palabra correcta"],
        ["tres cambios", "bolsa nueva", "palabras"],
        ["no contar la bolsa nueva", "pensar que agregar una ficha hace seguro el evento"],
        "Pide contar de nuevo las fichas después de cada cambio. Reconoce que describa la bolsa nueva.",
    ),
    reinforce="Con fichas de dos colores de papel, prueba qué pasa al quitar y agregar, y anota cómo cambia la palabra.",
    extend="Inventa una bolsa con tres colores y escribe dos cambios que conviertan un evento imposible en poco posible.",
)

register(
    OA24, 5,
    materials="Lápiz y papel. Si tienes una moneda, úsala en la actividad final; si no, usa dos papelitos marcados «cara» y «sello».",
    use="Aprenderé a comprobar mis decisiones con resultados reales, a compararlas y a comunicarlas con las palabras correctas. Sirve para saber qué dicen los datos y qué no.",
    prior=["Sé clasificar eventos con las cuatro palabras.", "Sé leer una lista de resultados."],
    explain=[
        "Los resultados que ocurren de verdad sirven para comprobar una idea, pero con cuidado. Si un resultado ocurrió aunque fuera una vez, el evento no es imposible. Si un resultado no ocurrió en pocos intentos, eso no prueba que sea imposible.",
        "Para decidir si algo es imposible o seguro no basta mirar cuántas veces salió; hay que mirar cómo es el experimento. Un dado normal tiene solo las caras de 1 a 6, así que sacar un 7 es imposible aunque lo lances muchas veces. Sacar un número del 1 al 6 es seguro.",
        "Para comunicar, escribe una frase completa con la palabra de posibilidad, el evento y una razón con números. Por ejemplo: «Sacar 6 en el dado es poco posible, porque una de las seis caras tiene el 6». Comparar dos eventos significa decir cuál se acerca más a seguro.",
    ],
    vocab=[("comprobar", "revisar si una idea coincide con lo que se observa"), ("comparar", "decir en qué se parecen o se diferencian dos cosas"), ("comunicar", "explicar con palabras claras una conclusión"), ("registro", "lista de resultados que se anotan")],
    worked=[
        {"title": "Un resultado que sí salió", "problem": LANZ + " El 4 salió una vez. ¿Sacar un 4 puede ser imposible?", "steps": ["Si un resultado salió, el evento puede ocurrir.", "Un evento que puede ocurrir no es imposible."], "answer": "No es imposible; con el dado es poco posible"},
        {"title": "Un resultado que no salió", "problem": LANZ + " No salió ningún 7. ¿Hay que lanzar más veces para saber si el 7 es imposible?", "steps": ["Un dado normal solo tiene las caras 1 a 6.", "Por cómo es el dado, el 7 no puede salir."], "answer": "Sacar 7 es imposible por cómo es el dado"},
    ],
    mistakes=[
        {"wrong": "Decir que, como el 6 salió dos veces seguidas, ahora es seguro que sale otra vez.", "why": "Se piensa que una racha corta asegura el siguiente resultado.", "fix": "Cada lanzamiento empieza igual; sacar 6 sigue siendo poco posible."},
        {"wrong": "Decir que un evento posible tiene que ocurrir en cada serie de intentos.", "why": "Se confunde posible con seguro.", "fix": "Posible significa que puede ocurrir, no que siempre ocurre."},
    ],
    tiers={
        "recovery": [
            ex(LANZ + " ¿Cuántas veces salió el 6?", "2", "Salió en el cuarto y en el noveno lanzamiento."),
            ex(LANZ + " ¿Qué número salió más veces?", "3", "El 3 salió 3 veces; los otros salieron 2 veces o menos."),
            ex(LANZ + " ¿Qué número salió una sola vez?", "4", "Solo hay un 4 en la lista."),
        ],
        "understand": [
            ex(LANZ + " Como el 4 salió, ¿sacar un 4 puede ser imposible?", "No; si salió, puede ocurrir", "Imposible significa que no puede ocurrir nunca."),
            ex(DADO + " Evento: sale un número mayor que 6. ¿Seguro, posible, poco posible o imposible?", "Imposible", "Ninguna cara tiene un número mayor que 6."),
            ex(DADO + " Evento: sale un número entre 1 y 6. ¿Seguro, posible, poco posible o imposible?", "Seguro", "Todas las caras cumplen."),
        ],
        "apply": [
            ex(LANZ + " ¿Cuántas veces salió un número par?", "5", "Salieron 6, 2, 4, 6 y 2: son 5 veces."),
            ex(LANZ + " ¿Cuántas veces salió un 1 o un 2?", "4", "El 1 salió 2 veces y el 2 salió 2 veces."),
            ex(LANZ + " Lucía dice: «Como el 3 salió más veces, en el siguiente lanzamiento el 3 es seguro». Con el dado normal, ¿cómo es «sale 3»?", "Poco posible", "Solo una cara de seis tiene el 3."),
        ],
        "reason": [
            ex("Mario dice: «Como el 4 salió una sola vez en el registro de Lucía, nunca más saldrá 4». ¿Es correcto?", "No; sacar 4 sigue siendo poco posible", "Cada lanzamiento empieza igual y el 4 sigue en una cara."),
            ex("Sara dice: «Un evento posible tiene que ocurrir al menos una vez en 12 intentos». ¿Es verdad?", "No; posible significa que puede ocurrir, no que ocurre siempre en una serie", "El azar puede no mostrar el evento en una serie corta."),
        ],
        "challenge": [
            ex("Ordena de menos a más posible: A) sale un número menor que 7, B) sale el 6, C) sale el 0. Se usa el dado normal.", "C, B, A", "C es imposible, B es poco posible y A es seguro."),
            ex("Completa: «Si todas las caras de un dado tienen el número 2, sacar 2 es ___ y sacar 5 es ___».", "Seguro; imposible", "Todas las caras son 2 y ninguna es 5."),
        ],
    },
    context=[ex("En una caja hay 2 libros de cuentos y 2 de ciencias. Sin mirar, sacas un libro. Clasifica «sacar un libro de ciencias».", "Posible", "2 de los 4 libros son de ciencias: la mitad.")],
    selfcheck=[
        ex(LANZ + " ¿Cuántos lanzamientos hizo Lucía en total?", "12", "La lista tiene 12 resultados."),
        ex("Un dado normal se lanza 3 veces y no sale el 5. ¿Eso prueba que sacar 5 es imposible?", "No", "El dado tiene una cara con 5."),
        ex("¿Qué palabra describe «sale un número mayor que 6» con un dado normal?", "Imposible", "El dado solo llega hasta el 6."),
    ],
    open_task=task(
        "Lanza una moneda 10 veces y anota cada resultado como cara (C) o sello (S). Si no tienes moneda, saca 10 veces un papelito marcado «cara» o «sello» de una bolsa y devuélvelo siempre. Clasifica con una palabra «sale cara», «sale cara y sello a la vez» y «sale cara o sello». Escribe cuántas veces salió cara y compara con lo que esperabas.",
        "Resultados: C S S C C S C S S C. Salió cara 5 veces. «Sale cara» es posible; «cara y sello a la vez» es imposible; «cara o sello» es seguro.",
        ["registra 10 resultados", "clasifica los tres eventos correctamente", "cuenta las veces que salió cara", "compara con lo que esperaba sin decir que debía salir exactamente la mitad"],
        ["lista de 10", "tres palabras", "conteo y comparación"],
        ["creer que un resultado distinto de la mitad es un error", "clasificar según lo que salió y no según la moneda"],
        "Pide contar de nuevo las caras del registro. Reconoce que clasifique por cómo es la moneda y no por la serie.",
    ),
    reinforce="Anota 10 resultados de lanzar un dado o una moneda y marca qué eventos salieron y cuáles no.",
    extend="Escribe un párrafo de tres frases que explique por qué un resultado que no salió no prueba que sea imposible.",
)
