"""Cuaderno del estudiante, 1.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LF05 (símbolos de escritura ancestral) y OA LF06 (tecnologías para escuchar lengua y conocer
escritura ancestral), contexto de fortalecimiento de la lengua.

Los símbolos de práctica (△ ○ □) son figuras sin significado cultural, creadas para entrenar la
observación. No se atribuye significado a ningún símbolo real: eso lo enseña el educador/a
tradicional o la comunidad. Las fichas de sitios web son inventadas y no llevan enlaces.
"""
from __future__ import annotations

from student_lessons import ex, register

OA5 = "LC01 OA LF05"
OA6 = "LC01 OA LF06"

FICHA = "Ficha de práctica: soporte: una vasija de greda; dibujo: △ ○ ○; fuente: museo del pueblo; pueblo: se pregunta al educador/a tradicional."
SIMB = "Símbolos de práctica (sin significado cultural): △ ○ ○ □"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ LF05
register(
    OA5, 1,
    materials="Este cuaderno y lápiz. La ficha de procedencia de práctica está escrita en los ejercicios; las reproducciones reales las trae el educador/a tradicional con autorización.",
    use="Aprenderé a mirar un símbolo de la escritura ancestral preguntando primero de qué pueblo es, en qué soporte está y quién es la fuente. Sirve para no confundir ni mezclar los símbolos de pueblos distintos.",
    prior=["Sé describir una figura.", "Sé que cada pueblo tiene su propia cultura."],
    explain=[
        "Un símbolo es un dibujo o signo que tiene un significado para un grupo de personas. Algunos pueblos originarios tienen símbolos de escritura ancestral, que se hicieron en distintos soportes: madera, cerámica, piedra o tejido. El soporte es aquello sobre lo que está el símbolo.",
        "La procedencia dice de dónde viene el símbolo: de qué pueblo, en qué soporte y quién lo muestra, por ejemplo un museo, una comunidad o un educador tradicional. Sin procedencia no se sabe qué es y se corre el riesgo de mezclar pueblos distintos.",
        "Antes de mirar un símbolo, haz tres preguntas: ¿de qué pueblo es?, ¿en qué soporte está?, ¿quién lo muestra? Si no tienes la respuesta, no inventes: pregunta al educador o educadora tradicional o a la comunidad.",
    ],
    vocab=[("símbolo", "signo con significado para un grupo"), ("soporte", "material donde está el símbolo"), ("procedencia", "de dónde viene algo"), ("fuente", "quién muestra o cuida el símbolo"), ("escritura ancestral", "signos con significado que los pueblos originarios usan desde hace mucho tiempo")],
    worked=[
        {"title": "Leer una ficha", "problem": FICHA + " ¿Cuál es el soporte?", "steps": ["Busco la palabra soporte.", "Dice: una vasija de greda.", "Ese es el material."], "answer": "Una vasija de greda"},
        {"title": "Falta el pueblo", "problem": FICHA + " ¿Qué pueblo hizo la vasija?", "steps": ["Busco el pueblo en la ficha.", "Dice que se pregunta al educador/a tradicional.", "No lo adivino."], "answer": "No lo sé; pregunto al educador/a tradicional"},
    ],
    mistakes=[
        {"wrong": "Decir de qué pueblo es un símbolo sin saberlo.", "why": "Mezclas pueblos y das información falsa.", "fix": "Revisa la ficha o pregunta al educador/a tradicional."},
        {"wrong": "Mirar un símbolo sin saber su fuente.", "why": "No sabes si fue mostrado con autorización.", "fix": "Anota siempre quién lo muestra."},
    ],
    tiers={
        "recovery": [
            ex(FICHA + " ¿Cuál es la fuente?", "El museo del pueblo", "La ficha pone museo como fuente."),
            ex("¿Qué es un soporte?", "El material donde está el símbolo", "Puede ser madera, cerámica, piedra o tejido."),
            ex("¿Qué es la procedencia?", "De dónde viene el símbolo", "Dice pueblo, soporte y fuente."),
        ],
        "understand": [
            ex("¿Por qué es importante conocer el pueblo de un símbolo?", "Para no mezclar pueblos distintos", "Cada pueblo tiene sus propios símbolos."),
            ex("¿Cuáles son las tres preguntas antes de mirar un símbolo?", "Pueblo, soporte y fuente", "Con ellas se conoce la procedencia."),
            ex("Si no conoces el pueblo de un símbolo, ¿qué haces?", "Pregunto al educador/a tradicional", "No se adivina."),
        ],
        "apply": [
            ex(FICHA + " ¿Qué dibujo aparece en la vasija de práctica?", "△ ○ ○", "La ficha lo muestra."),
            ex("Hay 3 fichas de símbolos: una en madera, una en greda y una en tela. ¿Cuántos soportes distintos hay?", "3", "Cada ficha tiene un soporte diferente."),
            ex("Una ficha dice: soporte, piedra; fuente, una comunidad. ¿Qué dato falta para tener la procedencia completa?", "El pueblo", "Falta el dato del pueblo."),
        ],
        "reason": [
            ex("Un niño ve un dibujo en una vasija y dice que es de cierto pueblo porque se parece a otro dibujo. ¿Es buena razón?", "No", "Parecerse no demuestra de qué pueblo es."),
            ex("Una niña anota pueblo, soporte y fuente antes de mirar. ¿Hizo bien?", "Sí", "Así conoce la procedencia."),
        ],
        "challenge": [
            ex("En la sala hay 4 reproducciones y solo 2 tienen ficha de procedencia. ¿Cuántas debes dejar sin interpretar?", "2", "4 − 2 = 2 sin ficha."),
            ex("Escribe una ficha de procedencia de práctica con soporte, fuente y pueblo para un objeto de tu casa.", "Cualquier ficha con los tres datos", "Debe incluir pueblo (o se pregunta), soporte y fuente."),
        ],
    },
    context=[ex("El educador tradicional muestra una reproducción de un símbolo, pero no sabes de qué pueblo es. Un compañero dice: «Seguro es del mismo pueblo de la clase pasada». ¿Qué respondes?", "Que no lo sabemos y hay que preguntar", "No se asume el pueblo.")],
    selfcheck=[
        ex("¿Qué es el soporte?", "El material donde está el símbolo", "Es madera, greda, piedra o tela."),
        ex("¿Qué preguntas haces antes de mirar un símbolo?", "Pueblo, soporte y fuente", "Son los tres datos de procedencia."),
        ex("¿Se adivina el pueblo de un símbolo?", "No", "Se pregunta a quien sabe."),
    ],
    open_task=task(
        "Mira la ficha de práctica: «" + FICHA + "». Copia sus cuatro datos (soporte, dibujo, fuente y pueblo) y dibuja la vasija con su dibujo. Luego haz una ficha igual para un objeto de tu casa, por ejemplo una taza, un tejido o un plato. Pregunta al educador/a tradicional o a la comunidad: ¿qué símbolos de escritura ancestral de nuestro pueblo podemos mirar y quién los muestra?",
        "Soporte: greda. Dibujo: triángulo y dos círculos. Fuente: museo. Pueblo: lo pregunto. Mi pregunta: ¿qué símbolos de nuestro pueblo podemos mirar?",
        ["anota soporte y fuente", "dice que el pueblo se pregunta", "pregunta al educador/a tradicional"],
        ["ficha copiada", "dibujo", "pregunta escrita"],
        ["adivinar el pueblo", "no anotar la fuente"],
        "Valora la ficha completa y recuerda que el pueblo lo informa quien conoce el símbolo.",
    ),
    reinforce="Haz una ficha de procedencia para tres objetos de tu casa.",
    extend="Compara dos fichas y di en qué soportes se diferencian.",
)

register(
    OA5, 2,
    materials="Este cuaderno y lápiz. " + SIMB + ".",
    use="Aprenderé a describir la forma de un símbolo sin inventarle un significado. Sirve para observar con cuidado y respetar lo que significa para su pueblo.",
    prior=["Sé nombrar figuras como triángulo y círculo.", "Sé que un símbolo tiene procedencia."],
    explain=[
        "Describir un símbolo es decir cómo es: qué figuras tiene, cuántas, cómo están puestas y de qué color son. Eso se puede ver con los ojos. Por ejemplo, en los símbolos de práctica △ ○ ○ □ hay un triángulo, dos círculos y un cuadrado.",
        "El significado es distinto de la forma. El significado de un símbolo real lo conoce su pueblo, y solo se aprende preguntando a quien lo sabe. Si inventas qué significa, puedes decir algo falso o irrespetuoso.",
        "Una buena descripción tiene dos partes: lo que veo, y una pregunta sobre lo que no puedo ver. Por ejemplo: «Veo un triángulo y dos círculos. ¿Qué significa para su pueblo?». Así observas sin inventar.",
    ],
    vocab=[("describir", "decir cómo es algo"), ("forma", "figura que se ve"), ("significado", "lo que quiere decir un símbolo"), ("inventar", "decir algo que no sé"), ("observar", "mirar con atención")],
    worked=[
        {"title": "Describir sin interpretar", "problem": SIMB + ". Describe qué ves.", "steps": ["Cuento las figuras.", "Veo un triángulo, dos círculos y un cuadrado.", "No digo qué significan."], "answer": "Un triángulo, dos círculos y un cuadrado"},
        {"title": "Distinguir forma y significado", "problem": "Un niño dice: «El triángulo significa montaña». ¿Es una descripción o una interpretación?", "steps": ["Montaña no se ve en el triángulo.", "Es una idea del niño.", "Es una interpretación inventada."], "answer": "Es una interpretación inventada"},
    ],
    mistakes=[
        {"wrong": "Decir qué significa un símbolo sin saberlo.", "why": "Se inventa un significado.", "fix": "Describe y pregunta qué significa."},
        {"wrong": "Describir solo una figura y olvidar las demás.", "why": "La descripción queda incompleta.", "fix": "Cuenta todas las figuras."},
    ],
    tiers={
        "recovery": [
            ex(SIMB + ". ¿Cuántos círculos hay?", "2", "Se ven dos ○."),
            ex(SIMB + ". ¿Cuántos triángulos hay?", "1", "Solo hay un △."),
            ex("¿Describir es decir cómo es algo o inventar qué significa?", "Decir cómo es", "Describir es lo que se ve."),
        ],
        "understand": [
            ex("¿Es lo mismo la forma que el significado?", "No", "La forma se ve; el significado lo enseña el pueblo."),
            ex("¿Quién enseña el significado de un símbolo real?", "Su pueblo o el educador/a tradicional", "Ellos lo conocen."),
            ex("¿Por qué no hay que inventar significados?", "Porque puede ser falso", "Solo quien lo sabe puede explicarlo."),
        ],
        "apply": [
            ex(SIMB + ". ¿Cuántas figuras hay en total?", "4", "1 + 2 + 1 = 4."),
            ex(SIMB + ". ¿Cuál figura aparece dos veces?", "El círculo", "Hay dos ○."),
            ex("Mira esta fila: ○ ○ △ ○. ¿En qué lugar está el triángulo?", "En el tercero", "Es la tercera figura."),
        ],
        "reason": [
            ex("Una niña dice: «Veo tres figuras: un triángulo y dos círculos, ¿qué significan?». ¿Hizo una buena observación?", "Sí", "Describió y preguntó."),
            ex("Un niño dice «los círculos son ojos» sin que nadie se lo haya enseñado. ¿Qué debería hacer?", "Preguntar en vez de inventar", "Es una suposición sin fuente."),
        ],
        "challenge": [
            ex("Dibuja y describe una fila con tres figuras distintas. Escribe cuántas figuras distintas hay.", "3", "Si son tres distintas, hay 3."),
            ex("Escribe una descripción de dos figuras y una pregunta sobre su significado.", "Cualquier frase con descripción y pregunta", "Debe describir y preguntar."),
        ],
    },
    context=[ex("El educador tradicional muestra un símbolo y un compañero dice: «Eso significa un animal». Nadie lo sabe. ¿Qué podrías proponer?", "Describir y preguntarle al educador/a tradicional", "Se evita inventar.")],
    selfcheck=[
        ex(SIMB + ". ¿Cuántos cuadrados hay?", "1", "Se ve un □."),
        ex("¿Se inventa el significado de un símbolo?", "No", "Se pregunta a quien sabe."),
        ex("¿Qué dos partes tiene una buena descripción?", "Lo que veo y una pregunta", "Describe y pregunta."),
    ],
    open_task=task(
        "Describe estos símbolos de práctica: " + SIMB + ". Escribe cuántas figuras hay y cómo se llaman. Dibuja una fila nueva con los mismos símbolos en otro orden. Luego escribe una pregunta que haga alguien curioso sin inventar el significado. Pregunta al educador/a tradicional o a la comunidad: ¿qué símbolos de nuestro pueblo podemos describir y cuáles tienen un significado que debemos aprender de las personas mayores?",
        "Veo un triángulo, dos círculos y un cuadrado: cuatro figuras. Mi fila: ○ □ ○ △. Pregunta: ¿qué significan para su pueblo? Mi pregunta: ¿qué símbolos podemos describir?",
        ["describe las figuras", "no inventa significado", "pregunta al educador/a tradicional"],
        ["descripción", "fila dibujada", "pregunta escrita"],
        ["inventar significados", "olvidar figuras"],
        "Reconoce la descripción precisa y la pregunta sin invención.",
    ),
    reinforce="Describe cuatro figuras de un mantel o un tejido de tu casa.",
    extend="Haz una fila de cinco figuras y cuenta cuántas son distintas.",
)

register(
    OA5, 3,
    materials="Este cuaderno y lápiz. Las situaciones están escritas en los ejercicios.",
    use="Aprenderé a preguntar cuándo corresponde reproducir un símbolo y por qué algunos símbolos se resguardan. Sirve para no copiar lo que no se debe copiar.",
    prior=["Sé que los símbolos tienen procedencia.", "Sé pedir permiso."],
    explain=[
        "Reproducir un símbolo es copiarlo: dibujarlo, pintarlo o imprimirlo. No siempre corresponde. Algunos símbolos pertenecen a un pueblo o a una familia y solo se reproducen cuando ellos lo permiten, en ciertas ocasiones y de cierta manera.",
        "Resguardar significa cuidar algo importante para que no se pierda ni se use mal. Cuando una comunidad resguarda un símbolo, pide respeto: no se copia para decorar, no se vende y no se cambia sin permiso.",
        "Antes de copiar un símbolo, haz tres preguntas: ¿quién es su dueño?, ¿se puede reproducir?, ¿en qué ocasión? Si no tienes la respuesta, no lo copies. Pregunta al educador o educadora tradicional o a la comunidad.",
    ],
    vocab=[("reproducir", "copiar o volver a hacer"), ("resguardar", "cuidar algo importante"), ("permiso", "autorización para usar algo"), ("dueño", "quien tiene el derecho sobre algo"), ("ocasión", "momento adecuado")],
    worked=[
        {"title": "Pedir permiso", "problem": "Quieres dibujar un símbolo que viste en una vasija del museo. ¿Qué haces primero?", "steps": ["No lo copio todavía.", "Pregunto a quien lo muestra si se puede.", "Si me dicen que no, no lo copio."], "answer": "Preguntar si se puede reproducir"},
        {"title": "Decorar sin permiso", "problem": "Una niña quiere pintar un símbolo ancestral en su mochila porque le gusta cómo se ve. ¿Es lo correcto?", "steps": ["Lo usa solo por decoración.", "No preguntó a su dueño.", "Debe preguntar antes."], "answer": "No; debe pedir permiso a su dueño"},
    ],
    mistakes=[
        {"wrong": "Copiar un símbolo porque se ve bonito.", "why": "Puede pertenecer a un pueblo que lo resguarda.", "fix": "Pregunta antes de copiarlo."},
        {"wrong": "Cambiar un símbolo para que quede mejor.", "why": "Altera algo que tiene significado.", "fix": "No lo cambies; respétalo como es."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué significa resguardar?", "Cuidar algo importante", "Se protege para que no se pierda ni se use mal."),
            ex("Antes de copiar un símbolo ancestral, ¿qué haces: preguntar o dibujar?", "Preguntar", "Se pide permiso."),
            ex("¿Quién puede decir si un símbolo se puede reproducir?", "El pueblo o el educador/a tradicional", "Ellos son quienes lo resguardan."),
        ],
        "understand": [
            ex("¿Por qué una comunidad resguarda un símbolo?", "Porque es importante y quiere que se use con respeto", "Es parte de su cultura."),
            ex("¿Se puede copiar un símbolo solo porque se ve bonito?", "No", "La belleza no da permiso."),
            ex("¿Es lo mismo mirar un símbolo que copiarlo?", "No", "Mirar y reproducir son acciones distintas."),
        ],
        "apply": [
            ex("Una amiga quiere imprimir un símbolo en 10 poleras para vender. ¿Qué debe hacer primero?", "Pedir permiso", "Debe hablar con el pueblo."),
            ex("Hay 3 símbolos y se permite copiar solo 1. ¿Cuántos no se pueden copiar?", "2", "3 − 1 = 2."),
            ex("La educadora dice «este símbolo no se copia». ¿Lo dibujas?", "No", "Se respeta la indicación."),
        ],
        "reason": [
            ex("Un niño dice: «Si es del pasado, es de todos y lo puedo copiar». ¿Tiene razón?", "No", "Los pueblos siguen siendo sus dueños."),
            ex("Una niña pregunta: «¿Puedo dibujarlo en mi cuaderno solo para aprender?». ¿Hizo bien?", "Sí", "Pidió permiso antes de reproducirlo."),
        ],
        "challenge": [
            ex("Tres niños quieren copiar un símbolo. Solo uno pidió permiso. ¿Cuántos deben esperar?", "2", "Los que no pidieron permiso deben esperar."),
            ex("Escribe una pregunta para pedir permiso de copiar un símbolo.", "Cualquier pregunta respetuosa", "Debe pedir permiso con respeto."),
        ],
    },
    context=[ex("Tu curso quiere pintar un mural con símbolos ancestrales. Nadie ha preguntado si se puede. ¿Qué paso falta?", "Preguntar a la comunidad si se puede", "Antes se pide permiso.")],
    selfcheck=[
        ex("¿Qué es reproducir?", "Copiar o volver a hacer", "Es dibujar o imprimir."),
        ex("¿Qué haces antes de copiar?", "Pregunto", "Se pide permiso."),
        ex("¿Quién resguarda un símbolo?", "Su pueblo", "Es de su cultura."),
    ],
    open_task=task(
        "Imagina estas tres situaciones: 1) copiar un símbolo en tu cuaderno para aprender, 2) pintarlo en una polera para vender, 3) usarlo de decoración en una fiesta. Escribe para cada una si primero debes preguntar o no y a quién preguntarías. Pregunta al educador/a tradicional o a la comunidad: ¿qué símbolos podemos reproducir, cuáles no y en qué ocasiones?",
        "En las tres situaciones primero pregunto, al educador/a tradicional. Mi pregunta: ¿qué símbolos podemos reproducir, cuáles no y cuándo?",
        ["reconoce que debe preguntar", "dice a quién", "pregunta al educador/a tradicional"],
        ["tres respuestas", "pregunta escrita"],
        ["copiar por decorar", "cambiar el símbolo"],
        "Valora que reconoció que debe preguntar y que el permiso lo da la comunidad.",
    ),
    reinforce="Explica a un familiar por qué no se copian símbolos sin permiso.",
    extend="Escribe una regla de tres frases para tu curso sobre copiar símbolos.",
)

register(
    OA5, 4,
    materials="Este cuaderno, lápiz y colores. Se trabaja con símbolos de práctica, no con símbolos ancestrales reales.",
    use="Aprenderé a valorar un símbolo de la escritura ancestral sin apropiármelo. Sirve para mostrar respeto: agradecer, decir su origen y no usarlo como mío.",
    prior=["Sé pedir permiso.", "Sé describir un símbolo."],
    explain=[
        "Valorar es reconocer que algo es importante. Un símbolo ancestral es importante para un pueblo porque guarda su historia. Lo valoras escuchando, cuidando y diciendo de quién es.",
        "Apropiarse es usar algo de otros como si fuera tuyo. No es respetuoso decir «este símbolo es mío», ni cambiar su forma, ni usarlo en productos sin permiso. En cambio, sí es respetuoso decir «este símbolo es del pueblo...» y agradecer.",
        "Una respuesta respetuosa puede ser un dibujo tuyo inspirado en tu propio territorio, un agradecimiento, un compromiso o una pregunta. Lo que hagas debe decir de dónde viene lo que aprendiste.",
    ],
    vocab=[("valorar", "reconocer que algo es importante"), ("apropiarse", "usar algo de otros como si fuera mío"), ("agradecer", "decir gracias"), ("compromiso", "promesa de hacer algo"), ("origen", "de dónde viene")],
    worked=[
        {"title": "Frase que valora", "problem": "Elige la frase que valora: A) «Este símbolo es mío». B) «Gracias por mostrarnos este símbolo de su pueblo».", "steps": ["A dice que es mío.", "B agradece y nombra su origen.", "B valora."], "answer": "B"},
        {"title": "Propio y respetuoso", "problem": "Una niña dibuja un símbolo inventado por ella con su nombre y cuenta que el símbolo ancestral lo vio con permiso. ¿Se apropió?", "steps": ["Su dibujo es suyo y no copia el real.", "Nombra el origen de lo aprendido.", "No se apropió."], "answer": "No se apropió"},
    ],
    mistakes=[
        {"wrong": "Decir que un símbolo ancestral es mío.", "why": "Es de un pueblo.", "fix": "Di de quién es y agradece."},
        {"wrong": "Cambiar el símbolo para que quede a mi gusto.", "why": "Se pierde su significado.", "fix": "Respeta su forma o crea algo propio distinto."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué significa apropiarse de un símbolo?", "Usarlo como si fuera mío", "Es tomar lo que es de otros."),
            ex("¿Qué dices a quien te muestra un símbolo?", "Gracias", "Agradecer es respeto."),
            ex("¿Qué es el origen de un símbolo?", "De dónde viene", "Es su pueblo y su historia."),
        ],
        "understand": [
            ex("¿Por qué no es respetuoso cambiar un símbolo?", "Porque se pierde su significado", "Cambiar altera su sentido."),
            ex("¿Qué significa valorar un símbolo?", "Reconocer que es importante", "Se cuida y se agradece."),
            ex("¿Puedes hacer un dibujo propio sin copiar un símbolo ancestral?", "Sí", "Un dibujo propio no copia."),
        ],
        "apply": [
            ex("Elige la frase respetuosa: A) «Este símbolo lo inventé yo». B) «Aprendí este símbolo de la comunidad». Escribe la letra.", "B", "B dice de dónde viene."),
            ex("Hay 5 niños. Tres agradecen y dos no. ¿Cuántos agradecen?", "3", "Son tres según lo contado."),
            ex("Escribe una frase de agradecimiento para quien mostró el símbolo.", "Cualquier frase que diga gracias", "Se acepta un agradecimiento."),
        ],
        "reason": [
            ex("Una niña usa un símbolo ancestral en su mochila sin preguntar y dice que le gusta. ¿Valoró el símbolo?", "No", "Lo usó sin permiso."),
            ex("Un niño dice «gracias por compartir este símbolo del pueblo» y no lo copia. ¿Valoró el símbolo?", "Sí", "Agradeció y respetó su origen."),
        ],
        "challenge": [
            ex("Tienes 3 formas de responder: agradecer, preguntar y comprometerte a cuidar. Si un niño usa las 3, ¿cuántas formas usó?", "3", "Usó las tres."),
            ex("Escribe un compromiso de una frase para cuidar los símbolos ancestrales.", "Cualquier compromiso respetuoso", "Debe comprometerse a respetar."),
        ],
    },
    context=[ex("Después de ver símbolos ancestrales, Ema dice que los usará en su logotipo de un negocio. ¿Qué podrías decirle?", "Que primero debe preguntar a la comunidad", "Los símbolos no se usan comercialmente sin permiso.")],
    selfcheck=[
        ex("¿Qué dices a quien comparte un símbolo?", "Gracias", "Se agradece a quien comparte."),
        ex("¿Se dice «este símbolo es mío»?", "No", "Pertenece a un pueblo."),
        ex("¿De dónde viene un símbolo ancestral?", "De un pueblo", "Tiene origen en un pueblo."),
    ],
    open_task=task(
        "Haz un dibujo tuyo de tres figuras que representen cosas de tu territorio (por ejemplo una montaña, un río y un árbol), sin copiar ningún símbolo ancestral. Escribe una frase de agradecimiento a las personas que te enseñaron sobre los símbolos y un compromiso para cuidarlos. Pregunta al educador/a tradicional o a la comunidad: ¿cómo podemos mostrar nuestro aprecio por los símbolos de su pueblo sin apropiarnos de ellos?",
        "Dibujé una montaña, un río y un árbol. Escribí: «Gracias por enseñarme. Me comprometo a no copiar sin permiso». Mi pregunta: ¿cómo mostramos aprecio sin apropiarnos?",
        ["dibujo propio", "agradece y se compromete", "pregunta al educador/a tradicional"],
        ["dibujo", "frase de agradecimiento", "pregunta escrita"],
        ["copiar símbolos", "decir que son suyos"],
        "Valora el dibujo propio y el compromiso de respeto.",
    ),
    reinforce="Haz un dibujo con símbolos propios y escribe un gracias para quien te enseña.",
    extend="Escribe tres reglas para el curso sobre cómo cuidar los símbolos.",
)

# ================================================================ LF06
SITIO_A = "Sitio A: publicado por la escuela de la comunidad; nombra a la educadora que habla; dice la fecha y que tiene autorización."
SITIO_B = "Sitio B: no dice quién lo publica, no tiene fecha y no explica de dónde viene el audio."

register(
    OA6, 1,
    materials="Este cuaderno y lápiz. Las fichas de sitios están escritas en los ejercicios; no se necesita internet.",
    use="Aprenderé a comprobar quién publica un recurso digital y para qué antes de usarlo. Sirve para escuchar lengua y ver escritura con fuentes confiables.",
    prior=["Sé que en internet hay muchos sitios.", "Sé que algunos datos pueden ser falsos."],
    explain=[
        "Los recursos tecnológicos, como computadores, tabletas o teléfonos, sirven para escuchar sonidos de una lengua o ver símbolos de escritura ancestral. Pero no todo lo que hay en internet es correcto ni está autorizado.",
        "Antes de usar un recurso, revisa tres cosas: quién lo publica, para qué lo publica y si tiene permiso de las personas que hablan. Un sitio confiable dice su autor, la fecha y la comunidad de donde viene el contenido.",
        "Si no puedes responder estas preguntas, no uses el recurso en clase. Pide ayuda al profesor o al educador tradicional. Es mejor un recurso que ellos recomienden que uno desconocido.",
    ],
    vocab=[("recurso digital", "contenido que se ve o escucha en una pantalla"), ("autor", "quien publica el recurso"), ("fuente confiable", "origen del que se puede fiar"), ("autorización", "permiso de quien habla o es dueño"), ("fecha", "día en que se publicó")],
    worked=[
        {"title": "Comparar dos sitios", "problem": SITIO_A + " " + SITIO_B + " ¿Cuál es más confiable?", "steps": ["El sitio A dice quién publica y tiene autorización.", "El sitio B no dice nada.", "El A es más confiable."], "answer": "El sitio A"},
        {"title": "Qué hacer sin información", "problem": "Un recurso no dice quién lo publica. ¿Qué haces?", "steps": ["No lo uso en clase.", "Pido ayuda al profesor.", "Pregunto al educador/a tradicional."], "answer": "No lo uso y pido ayuda"},
    ],
    mistakes=[
        {"wrong": "Usar un audio solo porque aparece primero en una búsqueda.", "why": "Puede no tener autorización ni ser correcto.", "fix": "Revisa quién lo publica."},
        {"wrong": "Creer que todo lo que está en internet es verdadero.", "why": "Hay errores y contenidos sin permiso.", "fix": "Comprueba la fuente."},
    ],
    tiers={
        "recovery": [
            ex(SITIO_A + " ¿Quién publica?", "La escuela de la comunidad", "El sitio lo dice."),
            ex(SITIO_B + " ¿Dice quién lo publica?", "No", "No lo informa."),
            ex("¿Qué es un autor?", "Quien publica el recurso", "Es quien lo hizo o publicó."),
        ],
        "understand": [
            ex("¿Por qué conviene saber quién publica un recurso?", "Para saber si es confiable", "El autor da confianza."),
            ex("¿Qué tres cosas revisas antes de usar un recurso?", "Quién publica, para qué y si tiene permiso", "Con eso lo valoras."),
            ex("¿Está autorizado un audio que no dice de dónde viene?", "No se sabe", "Sin información no hay certeza."),
        ],
        "apply": [
            ex(SITIO_A + " " + SITIO_B + " ¿Cuál tiene fecha?", "El sitio A", "El sitio B no tiene fecha."),
            ex("Hay 4 recursos: 2 con autor y fecha y 2 sin datos. ¿Cuántos puedes usar sin dudar?", "2", "Solo los que informan."),
            ex("Una ficha dice «autor: escuela; autorización: sí; fecha: sí». ¿Es confiable?", "Sí", "Tiene los datos."),
        ],
        "reason": [
            ex("Un niño usa el audio del sitio B porque suena bien. ¿Es buena razón?", "No", "Sonar bien no prueba que sea correcto."),
            ex("Una niña pide ayuda al educador tradicional para elegir un sitio. ¿Es una buena decisión?", "Sí", "Él conoce la lengua."),
        ],
        "challenge": [
            ex("Hay 5 sitios y solo 3 informan su autor. ¿Cuántos no lo informan?", "2", "5 − 3 = 2."),
            ex("Escribe tres preguntas para revisar un recurso digital.", "Quién lo publica, para qué y si tiene permiso", "Son las tres revisiones."),
        ],
    },
    context=[ex("Quieres que tu curso escuche un audio de una lengua indígena que encontraste en internet. No dice quién lo grabó. ¿Qué haces?", "Preguntar al profesor o educador tradicional antes de usarlo", "Sin fuente no es seguro.")],
    selfcheck=[
        ex("¿Todo lo de internet es correcto?", "No", "Hay errores y falta permiso."),
        ex("¿Qué revisas primero?", "Quién publica", "Es el autor."),
        ex("¿A quién pides ayuda?", "Al profesor o educador tradicional", "Ellos orientan con conocimiento."),
    ],
    open_task=task(
        "Con un adulto, mira cualquier video o sitio que ya tengan en casa (por ejemplo, un video de cuentos infantiles) y completa una ficha: quién lo publica, para qué lo publica y si dice la fecha. Si no puedes encontrar los datos, anótalo. Luego escribe una pregunta para el educador/a tradicional o la comunidad: ¿qué recursos digitales confiables podemos usar para escuchar la lengua de su pueblo?",
        "El video es de un canal de cuentos. Lo publica un canal, es para niños y tiene fecha. Mi pregunta: ¿qué recursos confiables podemos usar para escuchar la lengua del pueblo?",
        ["revisa quién publica", "anota para qué", "pregunta al educador/a tradicional"],
        ["ficha", "pregunta escrita"],
        ["usar sin revisar", "creer todo"],
        "Valora la revisión de la fuente y recuerda consultar a quien conoce la lengua.",
    ),
    reinforce="Elige un video de tu casa y di quién lo publica.",
    extend="Haz una lista de tres preguntas para revisar un sitio.",
)

register(
    OA6, 2,
    materials="Este cuaderno y lápiz. El guion del audio de práctica lo lee un adulto en voz alta.",
    use="Aprenderé a escuchar un audio con un propósito y a reconocer un sonido o una expresión que fue verificada. Sirve para escuchar con atención usando tecnología.",
    prior=["Sé escuchar con atención.", "Sé revisar quién publica un recurso."],
    explain=[
        "Escuchar con foco es escuchar buscando algo concreto. Por ejemplo, contar cuántas veces suena una palabra o notar un sonido que te llama la atención. Con un audio puedes volver a escuchar las veces que quieras.",
        "Para reconocer una expresión verificada necesitas que el audio tenga una fuente confiable y que el educador o educadora tradicional confirme lo que dice. Si no hay verificación, escuchas con atención, pero no repites ni usas lo que oíste.",
        "Cuida los audífonos y el volumen: ponlo bajito para escuchar sin dañar tus oídos. Y si el audio es la voz de una persona, escúchalo con respeto y pregunta antes de grabarlo o compartirlo.",
    ],
    vocab=[("audio", "grabación de sonidos o voces"), ("foco", "lo que busco al escuchar"), ("verificada", "confirmada por quien conoce la lengua"), ("volumen", "fuerza del sonido"), ("compartir", "mostrar a otros")],
    worked=[
        {"title": "Contar una palabra", "problem": "Un adulto lee este guion de práctica: «Hola, hola, buen día. Hola a todos». Cuenta cuántas veces suena «hola».", "steps": ["Hago una marca por cada «hola».", "Suena dos veces al comienzo.", "Suena una vez al final."], "answer": "3 veces"},
        {"title": "Audio sin verificar", "problem": "Escuchas un audio sin fuente conocida. ¿Repites lo que oyes?", "steps": ["No sé si es correcto.", "Puedo escucharlo con atención.", "No lo repito hasta que alguien lo verifique."], "answer": "No; espero la verificación"},
    ],
    mistakes=[
        {"wrong": "Repetir un audio sin verificar.", "why": "Puedes repetir algo equivocado.", "fix": "Espera a que el educador/a tradicional lo verifique."},
        {"wrong": "Subir el volumen al máximo.", "why": "Daña los oídos.", "fix": "Escucha con volumen bajo."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué es un audio?", "Una grabación de sonidos o voces", "Se escucha, no se ve."),
            ex("¿Con qué volumen escuchas con audífonos: bajito o al máximo?", "Bajito", "Cuida tus oídos."),
            ex("¿Qué es escuchar con foco?", "Escuchar buscando algo concreto", "Tiene un propósito."),
        ],
        "understand": [
            ex("¿Por qué no repites un audio no verificado?", "Porque puede estar equivocado", "No sabes si es correcto."),
            ex("¿Quién confirma una expresión de la lengua?", "El educador/a tradicional", "Él conoce la lengua."),
            ex("¿Puedes escuchar un audio muchas veces?", "Sí", "Así notas más cosas."),
        ],
        "apply": [
            ex("Un adulto lee: «Sol, sol, sol de la mañana». Cuenta cuántas veces suena «sol».", "3", "Se dice tres veces."),
            ex("El guion dice: «Mucho gusto. Mucho gusto, amiga». Cuenta cuántas veces suena «gusto».", "2", "Aparece dos veces."),
            ex("Escuchas 3 audios y solo 1 está verificado. ¿Cuántos no debes repetir?", "2", "3 − 1 = 2."),
        ],
        "reason": [
            ex("Una niña escucha con foco y cuenta una palabra. Otro solo escucha de fondo. ¿Quién escuchó con propósito?", "La niña que contó", "Tenía algo concreto que buscar."),
            ex("Un niño grabó la voz de la educadora sin avisar. ¿Qué debió hacer?", "Pedir permiso", "La voz se graba con autorización."),
        ],
        "challenge": [
            ex("Escucha: «Uno, dos, tres, uno, dos». Cuenta cuántas veces suena «uno».", "2", "Suena al comienzo y a la mitad."),
            ex("Escribe un foco de escucha para un audio.", "Por ejemplo, contar una palabra", "Debe ser algo concreto."),
        ],
    },
    context=[ex("La profesora pone un audio de la educadora tradicional. Un niño dice «yo lo repito en el recreo» sin que nadie lo haya verificado. ¿Qué le dirías?", "Que primero se verifique con el educador/a tradicional", "Primero se confirma.")],
    selfcheck=[
        ex("¿Qué volumen usas?", "Bajito", "Cuida los oídos."),
        ex("¿Qué es verificar?", "Confirmar que está bien", "Lo confirma quien conoce la lengua."),
        ex("¿Qué haces antes de grabar una voz?", "Pedir permiso", "La voz es de la persona."),
    ],
    open_task=task(
        "Pide a un adulto que lea en voz alta: «Hola, hola, buen día. Hola a todos». Cuenta cuántas veces suena «hola» con marcas. Luego pídele que lo lea otra vez y busca otro foco: cuántas palabras tiene en total. Anota tus dos resultados. Pregunta al educador/a tradicional o a la comunidad: ¿qué audios de su pueblo podemos escuchar y quién los verifica?",
        "Conté tres «hola» y siete palabras en total. Mi pregunta: ¿qué audios del pueblo podemos escuchar y quién los verifica?",
        ["escucha con foco", "anota resultados", "pregunta al educador/a tradicional"],
        ["dos resultados", "pregunta escrita"],
        ["escuchar sin propósito", "repetir lo no verificado"],
        "Valora el foco de escucha y recuerda que lo verifica quien conoce la lengua.",
    ),
    reinforce="Escucha una canción de tu casa y cuenta cuántas veces suena una palabra.",
    extend="Propón dos focos de escucha distintos para el mismo audio.",
)

register(
    OA6, 3,
    materials="Este cuaderno y lápiz. Las imágenes de práctica son figuras escritas aquí.",
    use="Aprenderé a observar un símbolo en una pantalla sin copiarlo fuera de contexto. Sirve para conocer escritura ancestral cuidando su procedencia.",
    prior=["Sé que un símbolo tiene procedencia.", "Sé que no todo se puede copiar."],
    explain=[
        "En una pantalla puedes ver imágenes de símbolos de escritura ancestral. Verlos es distinto de copiarlos. Mientras observas, mira la figura, el soporte y la fuente, y apunta lo que ves.",
        "Una imagen digital puede estar recortada o mezclada con otras. Por eso un símbolo en pantalla puede perder su contexto: ya no se sabe si es de madera, de cerámica o de un tejido. Si falta la información, no la completes tú.",
        "Si quieres guardar o copiar una imagen, pregunta antes. No la uses en tareas, juegos o productos fuera de contexto. Siempre anota el pueblo, la fuente y la fecha.",
    ],
    vocab=[("pantalla", "superficie donde se ven imágenes"), ("recortar", "cortar una parte de una imagen"), ("contexto", "información que rodea a algo"), ("copiar", "hacer otra igual"), ("guardar", "conservar un archivo")],
    worked=[
        {"title": "Observar sin copiar", "problem": "En una pantalla ves " + SIMB + ". ¿Qué anotas sin copiarlos?", "steps": ["Describo las figuras.", "Anoto el soporte si lo dice.", "No las dibujo."], "answer": "Anoto la descripción y la fuente, no las copio"},
        {"title": "Imagen sin información", "problem": "Ves un símbolo recortado, sin pueblo ni fuente. ¿Qué haces?", "steps": ["No sé de dónde viene.", "No invento el pueblo.", "Pregunto al educador/a tradicional."], "answer": "No lo uso y pregunto de dónde viene"},
    ],
    mistakes=[
        {"wrong": "Guardar una imagen sin saber su fuente.", "why": "Se pierde el contexto.", "fix": "Anota pueblo y fuente."},
        {"wrong": "Usar el símbolo para un juego o un fondo de pantalla.", "why": "Se usa fuera de contexto.", "fix": "Pregunta antes."},
    ],
    tiers={
        "recovery": [
            ex(SIMB + ". ¿Cuántas figuras ves?", "4", "1 + 2 + 1 = 4."),
            ex("¿Es lo mismo ver un símbolo que copiarlo?", "No", "Ver no es reproducir."),
            ex("¿Debes anotar el pueblo y la fuente de una imagen?", "Sí", "Así conservas el contexto."),
        ],
        "understand": [
            ex("¿Por qué una imagen recortada pierde información?", "Porque se corta el contexto", "Falta el soporte y la fuente."),
            ex("¿Qué es el contexto?", "La información que rodea a algo", "Dice dónde y por qué."),
            ex("¿Puedes poner un símbolo ancestral de fondo de pantalla sin preguntar?", "No", "Sería usarlo fuera de contexto."),
        ],
        "apply": [
            ex("Ves " + SIMB + ". ¿Cuántos círculos describes?", "2", "Hay dos ○."),
            ex("Una imagen tiene pueblo, fuente y fecha. ¿Cuántos datos de contexto tiene?", "3", "Son tres según lo contado."),
            ex("Hay 4 imágenes y 2 tienen fuente. ¿Cuántas no tienen fuente?", "2", "4 − 2 = 2."),
        ],
        "reason": [
            ex("Un niño dice que el símbolo de una imagen recortada es de un pueblo conocido. ¿Puede saberlo?", "No", "Sin información no se sabe."),
            ex("Una niña anota la fuente de una imagen. ¿Hizo bien?", "Sí", "Conserva el contexto."),
        ],
        "challenge": [
            ex("Escribe tres datos de contexto que debe tener una imagen de un símbolo.", "Por ejemplo: pueblo, soporte y fuente (también vale la fecha)", "Son datos clave del contexto."),
            ex("Escribe una pregunta para el educador tradicional sobre una imagen sin información.", "Cualquier pregunta sobre su origen", "Debe preguntar su origen."),
        ],
    },
    context=[ex("Tu compañero quiere usar un símbolo ancestral como avatar de su juego. ¿Qué podrías decirle?", "Que primero pregunte a la comunidad", "Es un uso fuera de contexto.")],
    selfcheck=[
        ex("¿Qué haces con un símbolo en pantalla?", "Observo sin copiar", "Observar es distinto de copiar."),
        ex("¿Qué anotas?", "Pueblo y fuente", "Son el contexto."),
        ex("¿Qué pasa si falta información?", "Pregunto", "No se inventa."),
    ],
    open_task=task(
        "Mira " + SIMB + " y escribe una descripción de dos líneas: qué figuras hay y cuántas. Inventa una ficha con pueblo («se pregunta»), soporte («pantalla») y fuente («este cuaderno»). Luego explica en una frase por qué no debes usarlos de fondo de pantalla. Pregunta al educador/a tradicional o a la comunidad: ¿qué imágenes de su escritura ancestral podemos mirar en pantallas y con qué cuidados?",
        "Hay un triángulo, dos círculos y un cuadrado. Ficha: pueblo, se pregunta; soporte, pantalla; fuente, este cuaderno. No los uso de fondo porque no tengo permiso. Mi pregunta: ¿qué imágenes podemos mirar?",
        ["describe sin copiar", "ficha completa", "pregunta al educador/a tradicional"],
        ["descripción", "ficha", "pregunta escrita"],
        ["usarlos fuera de contexto", "inventar el pueblo"],
        "Valora la observación sin copiar y la ficha.",
    ),
    reinforce="Observa una imagen en una pantalla de tu casa y describe sus figuras.",
    extend="Haz una ficha de contexto para una imagen de práctica.",
)

register(
    OA6, 4,
    materials="Este cuaderno y lápiz. El guion de práctica lo lee un adulto; no se graba a nadie.",
    use="Aprenderé a usar audio o mi propia voz con consentimiento, sin registrar a otras personas. Sirve para practicar sin faltar el respeto a nadie.",
    prior=["Sé pedir permiso.", "Sé escuchar con foco."],
    explain=[
        "Reproducir con consentimiento quiere decir que lo haces con permiso de la persona o comunidad. Puedes usar un audio autorizado o tu propia voz para practicar. No debes grabar a otras personas sin que lo sepan.",
        "El consentimiento es el sí de una persona, dicho con libertad. Una persona puede decir que sí, que no o que más adelante. Si dice que no, se respeta. No se insiste ni se graba a escondidas.",
        "Para practicar sin registrar a nadie, puedes escuchar un audio autorizado y repetir bajito, o decir algo con tu propia voz sin grabarlo. Así cuidas tu aprendizaje y la privacidad de los demás.",
    ],
    vocab=[("consentimiento", "el sí libre de una persona"), ("privacidad", "lo que cada persona decide mantener propio"), ("grabar", "guardar una voz o imagen"), ("autorizado", "con permiso"), ("insistir", "pedir una y otra vez")],
    worked=[
        {"title": "Pedir consentimiento", "problem": "Quieres grabar a la educadora para repasar en casa. ¿Qué haces primero?", "steps": ["Le pregunto con respeto.", "Escucho su respuesta.", "Si dice que no, no grabo."], "answer": "Pedir su permiso y aceptar la respuesta"},
        {"title": "Practicar sin grabar", "problem": "No tienes permiso para grabar. ¿Cómo practicas?", "steps": ["Escucho en clase con atención.", "Repito bajito en casa lo que recuerdo.", "No grabo."], "answer": "Escuchar con atención y repetir sin grabar"},
    ],
    mistakes=[
        {"wrong": "Grabar a escondidas.", "why": "Falta el consentimiento y la privacidad.", "fix": "Pregunta y respeta la respuesta."},
        {"wrong": "Insistir cuando alguien dice no.", "why": "El no también debe respetarse.", "fix": "Agradece y no grabes."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué es el consentimiento?", "El sí libre de una persona", "Es el permiso dado con libertad."),
            ex("Si una persona dice no a que la grabes, ¿qué haces?", "No grabo", "Se respeta el no."),
            ex("¿Puedes grabar a escondidas?", "No", "Falta el consentimiento."),
        ],
        "understand": [
            ex("¿Por qué se respeta la privacidad?", "Porque cada persona decide sobre su voz", "La voz es de cada uno."),
            ex("¿Se puede usar tu propia voz para practicar?", "Sí", "Es tu voz."),
            ex("¿Qué es un audio autorizado?", "Uno que se puede usar con permiso", "Alguien lo permitió."),
        ],
        "apply": [
            ex("Hay 5 personas. 3 dicen sí a ser grabadas y 2 dicen no. ¿A cuántas puedes grabar?", "3", "Solo a las que dijeron sí."),
            ex("Pides permiso a 4 personas y todas dicen que no. ¿Cuántas grabaciones haces?", "0", "Ninguna, porque nadie aceptó."),
            ex("Practicas 2 veces cada día durante 3 días sin grabar. ¿Cuántas veces practicaste en total?", "6", "2 + 2 + 2 = 6."),
        ],
        "reason": [
            ex("Un niño dice «si es solo para mí, puedo grabar sin avisar». ¿Tiene razón?", "No", "Igual falta el permiso."),
            ex("Una niña agradece cuando le dicen no y practica sin grabar. ¿Actuó con respeto?", "Sí", "Aceptó la respuesta."),
        ],
        "challenge": [
            ex("Escribe una frase para pedir permiso de grabar una voz.", "Cualquier frase respetuosa", "Debe pedir permiso con amabilidad."),
            ex("Hay 6 niños: 2 piden permiso y 4 graban sin pedir. ¿Cuántos actuaron mal?", "4", "Los que grabaron sin pedir."),
        ],
    },
    context=[ex("En clase, Tomás graba con el teléfono la voz de la educadora sin avisar. Después se la muestra a otros. ¿Qué podrías decirle?", "Que debió pedir permiso y no compartirla", "Faltó el consentimiento.")],
    selfcheck=[
        ex("¿Qué haces antes de grabar?", "Pido permiso", "Se necesita consentimiento."),
        ex("¿Qué haces si dicen no?", "No grabo", "Se respeta su decisión."),
        ex("¿Practicas con tu propia voz?", "Sí", "La voz es tuya."),
    ],
    open_task=task(
        "Practica con tu propia voz, sin grabar, la frase «Hola, buen día» tres veces. Anota cuántas veces la dijiste y cómo te sentiste. Luego escribe una frase que pida permiso a un adulto para grabar su voz, y anota qué harás si responde que no. Pregunta al educador/a tradicional o a la comunidad: ¿podemos grabar sus voces y cómo cuidamos esas grabaciones?",
        "Dije «Hola, buen día» tres veces y me sentí tranquilo. Pregunta: «¿Me permite grabar su voz?». Si dice que no, agradezco. Mi pregunta: ¿cómo cuidamos las grabaciones?",
        ["practica con su voz", "pide permiso", "pregunta al educador/a tradicional"],
        ["nota de práctica", "frase de permiso", "pregunta escrita"],
        ["grabar sin pedir", "insistir"],
        "Valora el consentimiento y el respeto a la respuesta.",
    ),
    reinforce="Practica una frase en voz baja sin grabar a nadie.",
    extend="Escribe dos formas amables de pedir permiso.",
)

register(
    OA6, 5,
    materials="Este cuaderno y lápiz. La ficha de procedencia de práctica está escrita en los ejercicios.",
    use="Aprenderé a guardar la procedencia de un recurso: el enlace, el pueblo y el responsable. Sirve para que otros puedan comprobar de dónde viene lo que usé.",
    prior=["Sé revisar quién publica un recurso.", "Sé qué es una fuente."],
    explain=[
        "Guardar la procedencia es anotar de dónde viene un recurso para poder volver a él. Los datos principales son el enlace o lugar donde está, el pueblo del que habla y el responsable, es decir, la persona o institución que lo publicó.",
        "Anotar la procedencia es parte de una buena tarea. Si en tu cuaderno escribes «audio de saludo, pueblo: se pregunta, responsable: escuela de la comunidad, lugar: biblioteca», otra persona podrá encontrarlo y confiar en tu trabajo.",
        "En este cuaderno no escribes enlaces reales: cuando uses uno en clase, el profesor o el educador tradicional te ayudará a anotarlo. Lo importante es aprender a dar crédito a quienes comparten su cultura.",
    ],
    vocab=[("procedencia", "de dónde viene un recurso"), ("responsable", "persona o institución que publica"), ("enlace", "dirección para encontrar un recurso"), ("crédito", "reconocimiento a quien hizo algo"), ("tarea", "trabajo que hago")],
    worked=[
        {"title": "Completar una ficha", "problem": "Completa: recurso: audio de saludo; pueblo: se pregunta; responsable: escuela de la comunidad; lugar: biblioteca. ¿Quién es el responsable?", "steps": ["Busco la palabra responsable.", "Dice: escuela de la comunidad.", "Esa es la respuesta."], "answer": "La escuela de la comunidad"},
        {"title": "Dar crédito", "problem": "Usaste una imagen en tu tarea. ¿Qué escribes al final?", "steps": ["Escribo qué es.", "Escribo quién la publicó.", "Escribo dónde la encontré."], "answer": "Qué es, quién la publicó y dónde la encontré"},
    ],
    mistakes=[
        {"wrong": "Usar un recurso sin anotar de dónde viene.", "why": "Nadie podrá comprobarlo.", "fix": "Anota responsable y lugar."},
        {"wrong": "Decir que un recurso es mío si lo publicó otro.", "why": "No se da crédito.", "fix": "Escribe quién lo publicó."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué datos guardas de la procedencia: enlace, pueblo y responsable?", "Sí", "Son los tres datos."),
            ex("¿Quién es el responsable de un recurso?", "Quien lo publica", "Es la persona o institución."),
            ex("¿Para qué anotas la procedencia?", "Para poder volver a encontrarlo", "Permite comprobar de dónde viene."),
        ],
        "understand": [
            ex("¿Qué es dar crédito?", "Reconocer a quien hizo algo", "Se dice quién lo hizo."),
            ex("¿Por qué anotar el pueblo del recurso?", "Para no mezclar pueblos", "Cada pueblo es distinto."),
            ex("¿Dónde escribes un enlace real: en este cuaderno o con ayuda del profesor?", "Con ayuda del profesor", "Se anota con apoyo."),
        ],
        "apply": [
            ex("Ficha: recurso, audio; responsable, escuela; lugar, biblioteca. ¿Dónde está el recurso?", "En la biblioteca", "El lugar lo dice."),
            ex("Tienes 3 recursos y anotas 3 datos de cada uno. ¿Cuántos datos anotas en total?", "9", "3 + 3 + 3 = 9."),
            ex("Ordena: a) lugar, b) responsable, c) pueblo. Escribe las letras en el orden de la ficha: pueblo, responsable, lugar.", "c, b, a", "Así es el orden pedido."),
        ],
        "reason": [
            ex("Un niño dice que su imagen es suya y no anota la fuente. ¿Qué falta?", "Dar crédito", "Falta decir quién la publicó."),
            ex("Una niña anota pueblo, responsable y lugar. ¿Hizo bien?", "Sí", "Dio crédito a la fuente."),
        ],
        "challenge": [
            ex("Si 4 niños anotan cada uno 3 datos de procedencia, ¿cuántos datos hay en total?", "12", "3 + 3 + 3 + 3 = 12."),
            ex("Escribe una ficha de procedencia de práctica de un libro de tu casa.", "Cualquier ficha con tres datos", "Debe tener datos."),
        ],
    },
    context=[ex("Tu curso presenta un afiche con un audio y una imagen. No anotaron de dónde vienen. ¿Qué falta?", "Anotar la procedencia", "Falta dar crédito.")],
    selfcheck=[
        ex("Al anotar la procedencia de un recurso, ¿escribes de dónde viene?", "Sí", "La procedencia es su origen."),
        ex("¿Quién es el responsable?", "Quien lo publica", "Es la persona o institución."),
        ex("Si usas un dibujo ajeno, ¿escribes quién lo hizo?", "Sí", "Así das crédito a su autor."),
    ],
    open_task=task(
        "Elige un libro, una canción o un juguete de tu casa y haz su ficha de procedencia: qué es, quién lo hizo o lo publicó y dónde lo guardas. Luego escribe cómo darías crédito a la educadora o al educador tradicional que te enseñe algo sobre la lengua de su pueblo. Pregunta al educador/a tradicional o a la comunidad: ¿cómo quieren que anotemos y reconozcamos lo que nos enseñan?",
        "Mi libro de cuentos: lo publicó una editorial, lo guardo en mi repisa. Daría crédito escribiendo el nombre de la educadora. Mi pregunta: ¿cómo quieren que anotemos lo que nos enseñan?",
        ["anota qué es y quién lo hizo", "dice cómo dar crédito", "pregunta al educador/a tradicional"],
        ["ficha", "frase de crédito", "pregunta escrita"],
        ["no anotar la fuente", "decir que es suyo"],
        "Valora la ficha y el cuidado de dar crédito.",
    ),
    reinforce="Haz fichas de procedencia para dos objetos de tu casa.",
    extend="Explica a un familiar por qué importa decir de dónde viene un audio.",
)
