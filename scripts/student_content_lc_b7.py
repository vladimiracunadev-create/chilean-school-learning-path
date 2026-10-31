"""Cuaderno del estudiante, 1.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR04 (relatos, experiencia y conocimiento cultural), contexto de rescate y revitalización.

El relato de práctica está en castellano e incluye solo el saludo «mari mari» (mapuzugun) dicho
como saludo. Es un texto inventado para entrenar la comprensión; no pertenece a ningún pueblo.
Los relatos tradicionales y su información cultural los comparten el educador/a tradicional y la comunidad.
"""
from __future__ import annotations

from student_lessons import ex, register

OA = "LC01 OA LR04"

RELATO_B = ("Una mañana de niebla, Tomás y su abuela subieron al cerro. La abuela llevaba una cesta con duraznos. "
            "Al llegar arriba, ella saludó con un «mari mari» a un vecino que cuidaba ovejas. El vecino les regaló un poco de queso. "
            "Tomás dijo gracias y bajaron cuando se despejó la niebla.")


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


register(
    OA, 1,
    materials=f"Este cuaderno y lápiz. Relato de práctica que un adulto puede leerte: «{RELATO_B}»",
    use="Aprenderé a escuchar un relato completo, aunque tenga una palabra en lengua indígena, y a decir quiénes son los personajes, dónde ocurre y qué pasa. Sirve para comprender los relatos que comparten los mayores.",
    prior=["Sé escuchar un texto completo.", "Sé responder quién, dónde y qué."],
    explain=[
        "Un relato cuenta una historia con personajes, un lugar y un acontecimiento. Los personajes son quienes actúan, el lugar es dónde pasa, y el acontecimiento es lo que ocurre. Al escuchar el relato completo puedes seguir las tres cosas.",
        "Algunos relatos mezclan castellano con palabras de una lengua indígena. En el relato de práctica, la abuela dice «mari mari», que es un saludo en mapuzugun. Aunque no conozcas todas las palabras de una lengua, puedes entender el relato por lo que pasa.",
        "Los relatos de los pueblos los comparten los mayores y los educadores tradicionales. Los escuchas sin interrumpir, y al terminar preguntas por las palabras que no conoces. No las inventas.",
    ],
    vocab=[("personaje", "quien actúa en el relato"), ("lugar", "dónde ocurre"), ("acontecimiento", "lo que pasa"), ("niebla", "nube baja que no deja ver bien"), ("cesta", "canasto donde se lleva algo")],
    worked=[
        {"title": "Personajes", "problem": f"Relato: «{RELATO_B}» ¿Quiénes son los personajes?", "steps": ["Busco quiénes hacen cosas.", "Suben Tomás y su abuela.", "Aparece también un vecino."], "answer": "Tomás, su abuela y el vecino"},
        {"title": "Lugar y acontecimiento", "problem": f"Relato: «{RELATO_B}» ¿Dónde ocurre y qué pasa?", "steps": ["Suben al cerro.", "La abuela saluda a un vecino.", "El vecino les regala queso."], "answer": "En el cerro; el vecino les regala queso"},
    ],
    mistakes=[
        {"wrong": "Interrumpir el relato para preguntar por una palabra.", "why": "Pierdes el hilo y falta respeto a quien cuenta.", "fix": "Pregunta al final del relato."},
        {"wrong": "Inventar qué significa una palabra que no conoces.", "why": "Puedes cambiar el sentido.", "fix": "Pregunta a quien lo contó."},
    ],
    tiers={
        "recovery": [
            ex(f"Relato: «{RELATO_B}» ¿Con quién subió Tomás al cerro?", "Con su abuela", "El relato lo dice."),
            ex(f"Relato: «{RELATO_B}» ¿Qué llevaba la abuela en la cesta?", "Duraznos", "La cesta tenía duraznos."),
            ex("¿Interrumpes mientras alguien cuenta un relato?", "No", "Se escucha completo."),
        ],
        "understand": [
            ex("En un relato, ¿cómo se llama el sitio donde pasan las cosas?", "El lugar", "Es el sitio de la historia."),
            ex("¿Qué es un acontecimiento?", "Lo que pasa", "Es el hecho principal."),
            ex("¿Se puede entender un relato aunque tenga una palabra desconocida?", "Sí, por lo que pasa", "El resto da pistas."),
        ],
        "apply": [
            ex(f"Relato: «{RELATO_B}» ¿Cómo estaba la mañana?", "Con niebla", "El relato empieza con niebla."),
            ex(f"Relato: «{RELATO_B}» ¿A quién saludó la abuela?", "A un vecino", "Saludó a un vecino que cuidaba ovejas."),
            ex(f"Relato: «{RELATO_B}» ¿Cuántos personajes hay: Tomás, la abuela y el vecino?", "3", "Son tres personajes."),
        ],
        "reason": [
            ex("Una niña dice que el relato pasó en la playa. ¿Qué parte no escuchó bien?", "Que fueron al cerro", "El lugar es el cerro."),
            ex("Un niño dice que «mari mari» es el nombre del vecino. ¿Por qué se equivoca?", "Porque es un saludo", "La abuela lo usa para saludar."),
        ],
        "challenge": [
            ex(f"Relato: «{RELATO_B}» Cuenta cuántas oraciones tiene (separadas por punto).", "5", "Hay cinco oraciones."),
            ex("Escribe en una frase quiénes, dónde y qué del relato de práctica.", "Tomás y su abuela subieron al cerro y el vecino les regaló queso", "Debe incluir personajes, lugar y hecho."),
        ],
    },
    context=[ex("Un mayor cuenta un relato y mezcla una palabra de la lengua. Un niño lo interrumpe cada vez para preguntar. ¿Qué podrías sugerirle?", "Esperar al final para preguntar", "Escuchar completo permite entender mejor.")],
    selfcheck=[
        ex(f"Relato: «{RELATO_B}» ¿Dónde ocurre?", "En el cerro", "Subieron al cerro."),
        ex("¿Quiénes actúan en un relato?", "Los personajes", "Ellos hacen lo que pasa."),
        ex("¿Cuándo preguntas por una palabra?", "Al final", "Después de escuchar completo."),
    ],
    open_task=task(
        "Pide a un adulto que te lea el relato de práctica «" + RELATO_B + "». Escucha completo y dibuja tres cosas: los personajes, el lugar y lo que pasa. Escribe una frase para cada dibujo. Pregunta al educador/a tradicional o a la comunidad: ¿qué relato de nuestro pueblo puedo escuchar y quién me lo puede contar?",
        "Dibujé a Tomás, la abuela y el vecino; el cerro con niebla; y al vecino dando queso. Mi pregunta: ¿qué relato de nuestro pueblo puedo escuchar?",
        ["escucha completo", "dice personajes, lugar y acontecimiento", "pregunta a la comunidad"],
        ["tres dibujos con frases", "pregunta escrita"],
        ["interrumpir", "inventar significados"],
        "Valora que siguió el relato y que preguntó a quien cuenta relatos.",
    ),
    reinforce="Escucha un cuento de tu casa y di quiénes son los personajes.",
    extend="Cuenta el relato de práctica con tus palabras a un familiar.",
)

register(
    OA, 2,
    materials=f"Este cuaderno y lápiz. Relato de práctica: «{RELATO_B}»",
    use="Aprenderé a recuperar información cultural que el relato dice con claridad, sin agregar lo que no dice. Sirve para saber con exactitud lo que cuenta.",
    prior=["Sé escuchar un relato completo.", "Sé quiénes son los personajes."],
    explain=[
        "Información explícita es la que el relato dice con claridad. En el relato de práctica, se dice que la abuela llevaba duraznos y que saludó con «mari mari». No hay que adivinar: está escrito.",
        "También hay información cultural, es decir, algo sobre cómo viven las personas. En este relato inventado se ve que la abuela saluda a su vecino al encontrarlo. Ese dato lo dice el relato. No sabemos si todos los pueblos lo hacen igual, y no hace falta inventar más.",
        "Si el relato no dice algo, no lo inventes. Anota que no lo dice y pregúntalo a quien lo cuenta. Así aprendes de verdad y no mezclas lo que sabes con lo que supones.",
    ],
    vocab=[("información explícita", "dicha con claridad en el relato"), ("información cultural", "dato sobre cómo vive un grupo"), ("costumbre", "algo que se hace seguido"), ("suponer", "creer sin saber"), ("vecino", "persona que vive cerca")],
    worked=[
        {"title": "Detalle explícito", "problem": f"Relato: «{RELATO_B}» ¿Qué le regaló el vecino?", "steps": ["Busco la palabra vecino.", "Dice: «les regaló un poco de queso».", "Esa es la respuesta."], "answer": "Un poco de queso"},
        {"title": "Lo que no dice", "problem": f"Relato: «{RELATO_B}» ¿Cómo se llama el cerro?", "steps": ["Busco el nombre del cerro.", "El relato solo dice «el cerro».", "No lo sé; pregunto."], "answer": "El relato no lo dice; hay que preguntar"},
    ],
    mistakes=[
        {"wrong": "Responder algo que el relato no dice.", "why": "Es inventar.", "fix": "Busca la frase que lo demuestra."},
        {"wrong": "Creer que una costumbre del relato es de todos los pueblos.", "why": "Cada pueblo tiene las suyas.", "fix": "Di solo lo que el relato cuenta."},
    ],
    tiers={
        "recovery": [
            ex(f"Relato: «{RELATO_B}» ¿Qué cuidaba el vecino?", "Ovejas", "El relato lo dice."),
            ex(f"Relato: «{RELATO_B}» ¿Qué dijo Tomás al recibir el queso?", "Gracias", "El relato lo dice."),
            ex("¿Información explícita es la que se dice o la que se adivina?", "La que se dice", "Es lo dicho con claridad."),
        ],
        "understand": [
            ex("¿Qué es información cultural?", "Un dato sobre cómo vive un grupo", "Cuenta costumbres de un grupo."),
            ex("¿Qué haces si el relato no dice algo?", "Pregunto a quien lo cuenta", "No se inventa."),
            ex("¿Por qué no decir que una costumbre es de todos los pueblos?", "Porque cada pueblo tiene las suyas", "Hay diferencias entre pueblos."),
        ],
        "apply": [
            ex(f"Relato: «{RELATO_B}» ¿Qué hicieron cuando se despejó la niebla?", "Bajaron", "El relato lo dice."),
            ex(f"Relato: «{RELATO_B}» ¿Qué costumbre se ve cuando la abuela llega arriba?", "Saludar al vecino", "Ella saluda al encontrarlo."),
            ex(f"Relato: «{RELATO_B}» ¿Cuántos alimentos se nombran en el relato? Escribe el número.", "2", "Se nombran duraznos y queso."),
        ],
        "reason": [
            ex("Un niño dice que el vecino era el abuelo de Tomás. ¿El relato lo dice?", "No", "Solo dice un vecino."),
            ex("Una niña dice que el relato muestra la costumbre de agradecer. ¿Tiene razón?", "Sí", "Tomás dijo gracias."),
        ],
        "challenge": [
            ex(f"Relato: «{RELATO_B}» Escribe un detalle explícito que no se haya preguntado.", "Por ejemplo, subieron una mañana de niebla", "Debe estar en el relato."),
            ex(f"Relato: «{RELATO_B}» ¿Qué palabra de lengua indígena aparece y qué es?", "«mari mari», un saludo", "La abuela la usa para saludar."),
        ],
    },
    context=[ex("Un mayor cuenta un relato y un niño agrega: «y también tenían un caballo». El mayor no lo dijo. ¿Qué debe hacer el niño?", "No agregar lo que no se dijo", "Solo se dice lo que cuenta el relato.")],
    selfcheck=[
        ex(f"Relato: «{RELATO_B}» ¿Qué llevaba la abuela?", "Una cesta con duraznos", "El relato lo dice."),
        ex("¿Se inventan datos del relato?", "No", "Se pregunta a quien sabe."),
        ex("En Lengua y Cultura: ¿Qué es una costumbre?", "Algo que se hace seguido", "Se repite en el tiempo."),
    ],
    open_task=task(
        "Un adulto te lee el relato «" + RELATO_B + "». Escribe o dibuja tres datos que el relato dice con claridad. Escribe un dato que el relato no dice y que te gustaría preguntar. Pregunta al educador/a tradicional o a la comunidad: ¿qué costumbres de nuestro pueblo aparecen en sus relatos y cómo debo hablar de ellas?",
        "Datos: la abuela llevaba duraznos; el vecino cuidaba ovejas; el vecino regaló queso. No dice cómo se llama el cerro. Mi pregunta: ¿qué costumbres aparecen en los relatos del pueblo?",
        ["recupera datos explícitos", "separa lo que no dice", "pregunta a la comunidad"],
        ["tres datos", "un dato no dicho", "pregunta escrita"],
        ["inventar datos", "generalizar costumbres"],
        "Valora la precisión y la pregunta a la comunidad.",
    ),
    reinforce="Con un cuento de tu casa en mano, localiza tres datos claros que el cuento diga.",
    extend="Escribe dos preguntas que el relato de práctica no responde.",
)

register(
    OA, 3,
    materials=f"Este cuaderno y lápiz. Relato de práctica: «{RELATO_B}»",
    use="Aprenderé a relacionar el relato con mi experiencia sin reemplazar lo que cuenta el relato. Sirve para comprender mejor y respetar el relato.",
    prior=["Sé qué dice el relato.", "Sé contar algo que me pasó."],
    explain=[
        "Relacionar es buscar algo parecido en tu vida. En el relato de práctica, la abuela saluda a un vecino y el vecino regala queso. Tal vez a ti un vecino te ha regalado algo, o tú has saludado a una persona mayor.",
        "Para hacerlo bien, primero dices lo que dice el relato y después tu experiencia. Mantén separadas las dos cosas. Tu experiencia ayuda a comprender, pero no cambia el relato.",
        "Si el relato es de un pueblo, además dices de dónde viene y agradeces a quien lo compartió. Nunca digas que es tuyo ni lo cambies para que se parezca más a tu vida.",
    ],
    vocab=[("relacionar", "unir el relato con mi vida"), ("separar", "mantener cada cosa aparte"), ("regalar", "dar algo sin pedir nada a cambio"), ("experiencia", "lo que viví"), ("agradecer", "decir gracias")],
    worked=[
        {"title": "Relacionar con cuidado", "problem": f"Relato: «{RELATO_B}» Ema dice: «En el relato, la abuela saluda al vecino. A mí me pasó que saludé a mi vecina y me sonrió». ¿Lo hace bien?", "steps": ["Dice primero lo del relato.", "Luego cuenta su experiencia.", "Las mantiene separadas."], "answer": "Sí, relaciona con cuidado"},
        {"title": "Cambiar el relato", "problem": "Pedro cuenta el relato pero dice que la abuela llevaba un perro porque él tiene uno. ¿Qué hizo mal?", "steps": ["El relato no dice eso.", "Pedro mezcló su vida con el relato.", "Debió contar su experiencia aparte."], "answer": "Cambió el relato con su experiencia"},
    ],
    mistakes=[
        {"wrong": "Mezclar mi experiencia con el relato.", "why": "El relato queda cambiado.", "fix": "Cuenta cada cosa por separado."},
        {"wrong": "Decir que un relato de la comunidad es mío.", "why": "No lo creé.", "fix": "Di quién lo compartió."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué dices primero: lo que dice el relato o tu experiencia?", "Lo que dice el relato", "El relato va primero."),
            ex("¿Cambias el relato para que se parezca a tu vida?", "No", "El relato no se cambia."),
            ex(f"Relato: «{RELATO_B}» ¿Quién saluda al vecino?", "La abuela", "El relato lo dice."),
        ],
        "understand": [
            ex("¿Por qué mantener separadas el relato y tu experiencia?", "Para no cambiar el relato", "Cada cosa queda clara."),
            ex("¿Qué haces si el relato es de un pueblo?", "Digo de dónde viene y agradezco", "Se da crédito."),
            ex("¿Tu experiencia cambia lo que dice el relato?", "No", "Solo ayuda a comprenderlo."),
        ],
        "apply": [
            ex("Completa la frase: «En el relato, el vecino _______ queso». Escribe la palabra.", "Regaló", "El vecino les regaló queso."),
            ex("Escribe una frase que empiece con «A mí me pasó que…» sobre saludar a alguien.", "Cualquier frase que empiece con «A mí me pasó que»", "Es una experiencia propia."),
            ex("Ordena: a) mi experiencia, b) lo que dice el relato, c) gracias a quien lo compartió. Escribe las letras en orden.", "b, a, c", "Primero el relato, luego mi vida y el agradecimiento."),
        ],
        "reason": [
            ex("Una niña cuenta su experiencia y olvida el relato. ¿Qué le falta?", "Decir qué dice el relato", "El relato es el centro."),
            ex("Un niño dice «esta historia la creé yo» sobre un relato de la comunidad. ¿Está bien?", "No", "Es de la comunidad."),
        ],
        "challenge": [
            ex("Hay 4 niños que relacionan bien y 3 que cambian el relato. ¿Cuántos niños son en total?", "7", "4 + 3 = 7."),
            ex("Escribe una frase de dos partes: lo que dice el relato y lo que te pasó.", "Cualquier frase con ambas partes", "Debe tener las dos."),
        ],
    },
    context=[ex("Después de un relato de la educadora tradicional, Luis cuenta algo suyo y dice que el relato «es parecido a uno que inventé». ¿Qué podrías decirle?", "Que el relato es de la comunidad", "No lo inventó él.")],
    selfcheck=[
        ex("¿Qué va primero?", "El relato", "Es el centro."),
        ex("¿Mezclas el relato con tu vida?", "No", "Se mantiene separado."),
        ex("¿A quién agradeces?", "A quien lo compartió", "Se da crédito."),
    ],
    open_task=task(
        "Un adulto te lee de nuevo el relato «" + RELATO_B + "». Escribe o dibuja algo parecido que te haya pasado, por ejemplo saludar a un vecino o recibir un regalo. Escribe una frase de dos partes: «En el relato…» y «A mí me pasó…». Pregunta al educador/a tradicional o a la comunidad: ¿cómo relaciono un relato de nuestro pueblo con mi vida sin cambiarlo?",
        "En el relato, el vecino regala queso. A mí me pasó que mi vecina me regaló una manzana. Mi pregunta: ¿cómo relaciono un relato del pueblo con mi vida sin cambiarlo?",
        ["dos partes separadas", "no cambia el relato", "pregunta a la comunidad"],
        ["frase", "dibujo", "pregunta escrita"],
        ["mezclar", "apropiarse"],
        "Valora la separación entre relato y experiencia.",
    ),
    reinforce="Cuenta un cuento y luego algo parecido que te haya pasado.",
    extend="Relaciona el relato con dos experiencias distintas.",
)

register(
    OA, 4,
    materials=f"Este cuaderno y lápiz. Relato de práctica: «{RELATO_B}»",
    use="Aprenderé a explicar qué aprendí de un relato y qué debo preguntar, reconociendo mis límites. Sirve para ser honesto sobre lo que sé y lo que no sé.",
    prior=["Sé qué dice el relato.", "Sé que hay cosas que solo la comunidad conoce."],
    explain=[
        "Al terminar un relato puedes explicar qué aprendiste. Del relato de práctica puedes aprender que es bueno saludar al encontrarte con un vecino y agradecer cuando te regalan algo. Eso lo sacas del relato, no lo inventas.",
        "También puedes decir qué no sabes. Reconocer límites es decir con honestidad: «Esto no lo sé». En los relatos de un pueblo, hay palabras y significados que solo conoce la comunidad. No los inventas.",
        "Una buena despedida del relato tiene tres partes: lo que aprendí, lo que debo preguntar y un gracias. Con eso muestras que comprendiste y que respetas a quien compartió.",
    ],
    vocab=[("aprender", "saber algo nuevo"), ("límite", "lo que no sé"), ("honestidad", "decir la verdad"), ("preguntar", "pedir información"), ("despedida", "cierre")],
    worked=[
        {"title": "Qué aprendí", "problem": f"Relato: «{RELATO_B}» Escribe qué aprendiste.", "steps": ["Releo la parte del vecino.", "El vecino regala queso y Tomás agradece.", "Aprendí a agradecer."], "answer": "Que hay que agradecer cuando alguien da algo"},
        {"title": "Qué debo preguntar", "problem": "Hay una palabra en el relato que no conoces. ¿Qué dices?", "steps": ["No invento su significado.", "Digo «no lo sé».", "Pregunto a quien lo contó."], "answer": "Digo que no lo sé y pregunto"},
    ],
    mistakes=[
        {"wrong": "Decir que entendí todo cuando no es cierto.", "why": "No es honesto.", "fix": "Di qué no sabes."},
        {"wrong": "No agradecer a quien contó.", "why": "Quien cuenta comparte algo valioso.", "fix": "Termina con un gracias."},
    ],
    tiers={
        "recovery": [
            ex("Cuando acaba el relato, ¿qué palabra de cortesía le dices a quien lo contó?", "Gracias", "Se agradece a quien comparte."),
            ex("Si no sabes algo del relato, ¿lo inventas o lo preguntas?", "Lo pregunto", "Preguntar evita errores."),
            ex("¿Dices «no lo sé» cuando no lo sabes?", "Sí", "Es una muestra de honestidad."),
        ],
        "understand": [
            ex("En Lengua y Cultura: ¿Qué es un límite?", "Lo que no sé", "Es reconocer qué falta."),
            ex("¿Por qué no se inventan los significados?", "Porque pueden ser falsos", "Solo la comunidad los conoce."),
            ex("¿Cuáles son las tres partes de la despedida?", "Lo que aprendí, lo que pregunto y gracias", "Esas son las tres partes."),
        ],
        "apply": [
            ex("Completa: «Aprendí que hay que ______ cuando alguien me da algo». Escribe la palabra.", "Agradecer", "Tomás dijo gracias."),
            ex("Escribe una pregunta que el relato de práctica no responde.", "Por ejemplo: ¿cómo se llama el cerro?", "El relato no lo dice."),
            ex("Cuenta: aprendí, pregunto, gracias. ¿Cuántas partes tiene la despedida?", "3", "Son tres partes."),
        ],
        "reason": [
            ex("Un niño dice que entendió todo el relato del pueblo, pero no conoce una palabra. ¿Es honesto?", "No", "No reconoce su límite."),
            ex("Una niña dice «no sé qué significa esa palabra, ¿me ayuda?». ¿Hizo bien?", "Sí", "Reconoció su límite."),
        ],
        "challenge": [
            ex("Si 4 niños dicen cada uno una cosa que aprendieron y una que preguntan, ¿cuántas frases hay en total?", "8", "2 + 2 + 2 + 2 = 8."),
            ex("Escribe una frase que diga qué aprendiste y qué preguntarías del relato.", "Cualquier frase con ambas ideas", "Debe tener aprendizaje y pregunta."),
        ],
    },
    context=[ex("La educadora tradicional termina un relato. Un niño dice: «Ya sé todo sobre ese pueblo». ¿Qué le dirías?", "Que un relato no enseña todo y hay que seguir preguntando", "Hay mucho más que aprender de la comunidad.")],
    selfcheck=[
        ex("¿Qué dices si no sabes?", "No lo sé", "Es una forma honesta."),
        ex("¿A quién preguntas?", "A quien contó el relato", "Quien lo cuenta lo sabe."),
        ex("Al cerrar tu comentario sobre el relato, ¿qué agradeces?", "Que hayan compartido el relato", "Se agradece a quien comparte."),
    ],
    open_task=task(
        "Un adulto te lee otra vez el relato «" + RELATO_B + "». Escribe o dibuja una cosa que aprendiste y una pregunta que el relato no responde. Termina con un agradecimiento para quien lo leyó. Pregunta al educador/a tradicional o a la comunidad: ¿qué relato de nuestro pueblo puedo escuchar y qué debo preguntar después?",
        "Aprendí a agradecer. Pregunta: ¿cómo se llama el cerro? Gracias por leerlo. Mi pregunta: ¿qué relato de nuestro pueblo puedo escuchar?",
        ["dice qué aprendió", "dice qué debe preguntar", "agradece"],
        ["frase o dibujo", "pregunta escrita"],
        ["decir que lo sabe todo", "no agradecer"],
        "Valora la honestidad y el agradecimiento.",
    ),
    reinforce="Después de un cuento, di una cosa que aprendiste y una pregunta.",
    extend="Haz un cartel con tres frases: aprendí, pregunto y gracias.",
)
