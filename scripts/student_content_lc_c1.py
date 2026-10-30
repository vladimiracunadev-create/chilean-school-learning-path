"""Cuaderno del estudiante, 1.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR05 y LS05: valorar el significado y la importancia cultural de los símbolos de la escritura ancestral.
Todo ejercicio usa fichas de práctica inventadas solo para entrenar la mirada (se declara en cada una) y
hechos generales: las tablillas con signos de Rapa Nui y los cordeles con nudos de los Andes. El significado
de cada símbolo real lo enseña el educador/a tradicional o la comunidad.
"""
from __future__ import annotations

from student_lessons import ex, register

LR5, LS5 = "LC01 OA LR05", "LC01 OA LS05"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def w(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


# ------------------------------------------------------------------ LR05
register(
    LR5, 1,
    materials="Hoja, lápiz y las fichas de práctica escritas en este cuaderno. Las fichas son inventadas para practicar: no son símbolos reales de ningún pueblo.",
    use="Aprenderé a preguntar de dónde viene un símbolo antes de opinar sobre él. Sirve para respetar a las personas y a los pueblos que lo crearon.",
    prior=["Sé nombrar materiales: madera, tela, cuerda, piedra, papel.", "Sé que hay pueblos originarios en Chile."],
    explain=[
        "Un símbolo es un dibujo o una marca que quiere decir algo para un grupo de personas. Algunos pueblos originarios tienen símbolos en tejidos, en tablillas de madera o en cordeles con nudos. Cada pueblo tiene los suyos.",
        "La procedencia dice de dónde viene un objeto. Tiene tres datos: el pueblo, el soporte y la fuente. El soporte es el material donde está el símbolo, como madera, tela o cordel. La fuente es quien nos muestra o nos cuenta eso: un museo, un libro o una persona de la comunidad.",
        "Hoy hay lenguas originarias que casi no se hablan, y muchas comunidades trabajan para recuperarlas. Por eso, antes de decir qué significa un símbolo, primero leo su ficha. Si falta un dato, lo anoto como pregunta y se lo consulto al educador o a la educadora tradicional.",
    ],
    vocab=[("símbolo", "dibujo o marca que quiere decir algo"), ("procedencia", "de dónde viene algo y quién lo muestra"), ("soporte", "material donde está el símbolo"), ("fuente", "persona, libro o lugar que da la información"), ("revitalizar", "ayudar a que una lengua vuelva a usarse")],
    worked=[
        w("Leer una ficha", "Ficha de práctica (inventada): Pueblo: rapanui. Soporte: tablilla de madera. Fuente: sala de un museo. ¿Cuál es el soporte?", ["Busco la palabra «Soporte» en la ficha.", "Leo lo que dice al lado: tablilla de madera.", "El soporte es el material donde están los signos."], "tablilla de madera"),
        w("Ver qué falta", "Ficha de práctica (inventada): Soporte: tela. Fuente: un libro. No dice el pueblo. ¿Qué dato falta?", ["Reviso los tres datos: pueblo, soporte, fuente.", "Soporte y fuente aparecen, pero el pueblo no.", "Anoto una pregunta: ¿de qué pueblo es esta tela?"], "falta el pueblo"),
    ],
    mistakes=[
        {"wrong": "Decir qué significa un símbolo apenas lo veo.", "why": "No sé de qué pueblo es ni quién lo explica.", "fix": "Primero leo pueblo, soporte y fuente; si falta algo, pregunto."},
        {"wrong": "Pensar que todos los pueblos originarios usan los mismos símbolos.", "why": "Cada pueblo tiene su historia y sus propias formas de marcar y de tejer.", "fix": "Escribo siempre el nombre del pueblo al lado del símbolo."},
    ],
    tiers={
        "recovery": [
            ex("Una tablilla de madera con signos tallados viene de Rapa Nui. ¿Cuál es el soporte: madera o tela?", "madera", "El soporte es el material donde están los signos, y aquí es la madera."),
            ex("En los Andes hay cordeles con nudos. ¿Cuál es su soporte: cordel o piedra?", "cordel", "El soporte es el material de la cuerda con nudos."),
            ex("¿Qué palabra dice de dónde viene un objeto: procedencia, color o tamaño?", "procedencia", "Procedencia significa de dónde viene algo y quién lo muestra."),
        ],
        "understand": [
            ex("Ficha de práctica: Pueblo: aymara. Soporte: tejido. Fuente: un taller de la comunidad. ¿Qué dato dice quién nos cuenta sobre el tejido?", "la fuente: un taller de la comunidad", "La fuente es quien muestra o cuenta la información."),
            ex("Verdadero o falso: todos los pueblos originarios usan los mismos símbolos.", "Falso", "Cada pueblo tiene sus propios símbolos y su propia historia."),
            ex("Un afiche muestra un dibujo y no dice de qué pueblo es. ¿Falta la procedencia?", "Sí", "Sin el nombre del pueblo no sé de dónde viene el dibujo."),
        ],
        "apply": [
            ex("Ficha de práctica: «Foto de un cordel con nudos en un museo regional. Pueblo andino. Fuente: el museo». ¿Cuál es el soporte?", "un cordel", "El soporte es el material y aquí la ficha habla de un cordel con nudos."),
            ex("Ordena. A: anoto lo que veo. B: leo pueblo, soporte y fuente. C: pregunto lo que no sé. ¿Qué letra va primero?", "B", "Primero leo la ficha para saber de dónde viene el símbolo."),
            ex("Una tarjeta dice: «Dibujo en una manta», sin pueblo ni fuente. ¿Qué dos datos faltan?", "el pueblo y la fuente", "La tarjeta solo da el soporte, que es la manta."),
        ],
        "reason": [
            ex("Lucía dice: «Este dibujo es de un pueblo, porque me parece bonito». ¿Qué le falta a Lucía?", "una fuente que lo diga", "Que algo me parezca bonito no prueba de qué pueblo es."),
            ex("Dos papeles dicen cosas distintas sobre el mismo dibujo y ninguno tiene fuente. ¿A quién conviene consultar: a un educador tradicional o a quien adivine más rápido?", "a un educador tradicional", "El educador o la comunidad conocen y cuidan ese saber."),
        ],
        "challenge": [
            ex("Una ficha trae 4 datos: pueblo, soporte, fuente y color favorito de quien la mira. ¿Cuál NO es un dato de procedencia?", "el color favorito", "Lo que le gusta a quien mira no dice de dónde viene el objeto."),
            ex("Ficha de práctica: Pueblo: no se sabe. Soporte: tablilla de madera. Fuente: un libro. ¿Qué frase es correcta: «Es de cualquier pueblo» o «Falta saber el pueblo y lo preguntaré»?", "Falta saber el pueblo y lo preguntaré", "Cuando falta un dato no se inventa, se pregunta."),
        ],
    },
    context=[ex("En la sala de tu escuela hay una foto de una tablilla de madera con signos de Rapa Nui. Debajo solo dice «Año de la foto: hoy». ¿Qué dato de procedencia falta además del pueblo y del soporte?", "la fuente", "El pueblo y el soporte ya se saben; falta quién muestra o cuenta eso.")],
    selfcheck=[ex("¿Cómo se llama el material donde está el símbolo?", "soporte", "El soporte es el material."), ex("¿Qué hago si en la ficha falta un dato?", "pregunto", "No invento, anoto la pregunta y la consulto."), ex("¿Quién conoce y cuida el saber sobre los símbolos de su pueblo?", "el educador tradicional o la comunidad", "Son quienes lo transmiten y lo resguardan.")],
    open_task=task(
        "Elige una de estas dos fichas de práctica y complétala en tu cuaderno con tres líneas: «Pueblo», «Soporte» y «Fuente». Ficha A: una tablilla de madera con signos de Rapa Nui vista en un libro. Ficha B: un cordel con nudos de los Andes visto en un museo. Después escribe una pregunta que le harías al educador/a tradicional o a una persona de la comunidad.",
        "Ficha A. Pueblo: rapanui. Soporte: madera. Fuente: un libro. Pregunta: ¿se puede mostrar esta tablilla a otros cursos?",
        ["escribe pueblo, soporte y fuente", "no inventa el significado", "formula una pregunta para el educador/a tradicional o la comunidad"],
        ["dibujo o escritura de la ficha", "pregunta escrita o dicha en voz alta"],
        ["escribir qué significan los signos sin fuente", "dejar un dato en blanco sin preguntar"],
        "Reconoce que anotó los tres datos y que dejó el significado a cargo de quien enseña en la comunidad; si inventó un significado, pídele que lo cambie por una pregunta.",
    ),
    reinforce="Nombra tres soportes distintos (madera, tela, cordel) y di con tus palabras qué es la fuente.",
    extend="Mira un objeto de tu casa y anota su procedencia: qué es, de qué material es y quién te contó de dónde viene.",
)

register(
    LR5, 2,
    materials="Hoja, lápiz de color y las figuras de práctica escritas aquí. Las figuras son inventadas para practicar la mirada; no son símbolos de ningún pueblo.",
    use="Aprenderé a describir lo que veo en una marca o dibujo sin inventar lo que significa. Sirve para mirar con respeto los símbolos de otros pueblos.",
    prior=["Conozco figuras: círculo, cuadrado, triángulo, raya.", "Sé contar hasta 10."],
    explain=[
        "Describir es decir lo que se ve con los ojos: cuántas rayas hay, qué forma tiene, de qué color es y en qué material está. Una descripción no necesita saber el significado. Por eso todos podemos describir, aunque no conozcamos la lengua.",
        "El significado es otra cosa: es la idea que el símbolo tiene para las personas que lo crearon. Ese significado lo explican la comunidad y el educador o la educadora tradicional. Si no conozco la escritura de un pueblo, no puedo saber lo que dicen sus signos. Eso muestra que no se puede adivinar.",
        "Cuando una lengua o una escritura casi se pierde, recuperar su saber lleva mucho tiempo y cuidado. Yo ayudo describiendo con exactitud lo que veo y guardando mis preguntas. Así no pongo en el símbolo cosas que son solo mías.",
    ],
    vocab=[("describir", "decir lo que veo con detalle"), ("significado", "la idea que tiene un símbolo para su pueblo"), ("forma", "cómo es el contorno de algo"), ("detalle", "una parte pequeña que se puede observar"), ("adivinar", "decir algo sin saberlo con seguridad")],
    worked=[
        w("Describir una figura", "Figura de práctica: ■ con 3 rayas por dentro: ■|||. ¿Cómo la describo?", ["Veo un cuadrado.", "Cuento las rayas de adentro: 1, 2, 3.", "Digo: un cuadrado con tres rayas, sin decir qué significa."], "un cuadrado con tres rayas"),
        w("Separar lo que veo de lo que pienso", "Frase: «Esta figura es un cuadrado con dos puntos y quiere decir alegría». ¿Qué parte describe y cuál inventa?", ["«Un cuadrado con dos puntos» se ve con los ojos.", "«Quiere decir alegría» no se ve; es una idea que no tengo cómo comprobar.", "Me quedo con la parte que describe."], "describe: un cuadrado con dos puntos; inventa: quiere decir alegría"),
    ],
    mistakes=[
        {"wrong": "Decir «esto significa lluvia» al ver tres rayas.", "why": "Parece lluvia a mis ojos, pero el pueblo puede pensar otra cosa.", "fix": "Digo «veo tres rayas» y pregunto qué significa."},
        {"wrong": "Contar mal las partes del dibujo.", "why": "Miré rápido y no marqué cada parte.", "fix": "Cuento tocando cada parte con el lápiz, una por una."},
    ],
    tiers={
        "recovery": [
            ex("Figura de práctica: ▲ ▲ ▲. ¿Cuántos triángulos hay?", "3", "Se cuenta un triángulo por cada ▲ y son tres."),
            ex("Figura de práctica: ● con una raya a cada lado: |●|. ¿Cuántas rayas hay?", "2", "Hay una raya a la izquierda y una a la derecha."),
            ex("¿Qué se dice con los ojos: la descripción o el significado?", "la descripción", "Describir es decir lo que se ve."),
        ],
        "understand": [
            ex("Frase: «Es una cruz roja en una tela». ¿Es una descripción o un significado?", "una descripción", "Dice lo que se ve: una cruz roja en una tela."),
            ex("Frase: «Es el símbolo del sol». Si no hay fuente, ¿es descripción o suposición?", "suposición", "No se ve en la imagen y nadie lo ha confirmado."),
            ex("¿Quién explica el significado de un símbolo de su pueblo: cualquiera que lo mire o la comunidad?", "la comunidad", "El significado pertenece al pueblo que lo creó."),
        ],
        "apply": [
            ex("Figura de práctica: ■■ con un punto en cada cuadrado: ■•■•. Escribe la descripción con números: ¿cuántos cuadrados y cuántos puntos?", "2 cuadrados y 2 puntos", "Hay dos cuadrados y en cada uno hay un punto."),
            ex("Figura de práctica: una raya larga con 4 rayitas cortas abajo. ¿Cuántas rayas hay en total contando la larga?", "5", "Una raya larga más cuatro cortas dan cinco rayas."),
            ex("Elige la mejor descripción de ▲● : A) «Un triángulo y un círculo» B) «Un cerro y un sol».", "A", "A dice lo que se ve; B ya inventa lo que sería."),
        ],
        "reason": [
            ex("Pedro mira la figura ▲▲ y dice «son dos cerros». ¿Qué le dirías para cuidar la descripción?", "que diga «dos triángulos»", "Lo que se ve son triángulos; ser cerros sería una idea suya."),
            ex("No conoces la escritura de un pueblo y ves signos en una tablilla. ¿Puedes adivinar lo que dicen?", "No", "Adivinar no es saber y puede faltarle el respeto al pueblo."),
        ],
        "challenge": [
            ex("Figura de práctica: ●●● ▲▲. Escribe cuántas formas hay en total y cuántas son círculos.", "5 formas y 3 círculos", "Tres círculos más dos triángulos suman cinco formas."),
            ex("Ana describe: «Hay dos rayas y quiere decir amistad». Escribe la frase corregida, sin lo que no se ve.", "«Hay dos rayas»", "Lo de la amistad es una idea; se pregunta a la comunidad."),
        ],
    },
    context=[ex("Un amigo te muestra una foto de un tejido con rombos de color rojo en una fila de 4. Describe con una frase corta lo que se ve sin decir qué significa.", "Hay una fila de 4 rombos rojos.", "Se dice la cantidad, la forma y el color, sin significado.")],
    selfcheck=[ex("¿Qué hago primero: describo o invento un significado?", "describo", "Primero se mira y se dice lo que se ve."), ex("¿Quién conoce el significado de un símbolo de su pueblo?", "la comunidad", "Es su saber y ellos lo explican."), ex("Si veo ▲▲▲, ¿cuántos triángulos digo que hay?", "3", "Se cuentan tres triángulos.")],
    open_task=task(
        "Elige una figura de práctica: A) ▲▲● B) ■|||. Haz un dibujo de la figura y escribe debajo una descripción corta con números y colores. Después escribe una pregunta que podrías hacerle al educador/a tradicional o a la comunidad sobre símbolos reales.",
        "Figura A: dos triángulos y un círculo. Pregunta: ¿cómo cuidan ustedes los dibujos de sus tejidos?",
        ["describe lo que ve con números y formas", "no inventa significado", "propone una pregunta a la comunidad"],
        ["dibujo de la figura", "descripción escrita o dicha"],
        ["escribir «significa…» sin fuente", "olvidar contar alguna parte"],
        "Valora que separó lo que ve de lo que piensa; si escribió un significado, invítalo a convertirlo en pregunta para quien enseña en la comunidad.",
    ),
    reinforce="Describe tres figuras simples de tu cuaderno diciendo solo cuántas son y cómo se ven.",
    extend="Observa un dibujo de la ropa de alguien de tu casa y descríbelo en una frase, sin decir qué «quiere decir».",
)

register(
    LR5, 3,
    materials="Hoja, lápiz y los casos escritos en este cuaderno. No necesitas fotos ni materiales especiales.",
    use="Aprenderé a preguntar si se puede copiar o usar un símbolo antes de hacerlo. Sirve para no faltarle el respeto a ningún pueblo.",
    prior=["Sé que un símbolo viene de un pueblo.", "Sé pedir permiso con palabras amables."],
    explain=[
        "Reproducir es copiar o dibujar de nuevo algo que ya existe. Algunos símbolos se usan todos los días. Otros pertenecen a una comunidad y solo se usan en ciertas ocasiones. No lo sabemos mirando solamente.",
        "Resguardar significa cuidar algo para que no se pierda ni se use mal. Muchos pueblos resguardan sus saberes, sus lenguas y sus símbolos. Por eso la regla es: pregunto antes de copiar, y si no hay respuesta, no copio.",
        "Quien puede decir cuándo corresponde usar un símbolo es el educador o la educadora tradicional, o la persona que la comunidad indique. Yo puedo decir: «¿Puedo dibujar esto en mi cuaderno? ¿Cuándo corresponde usarlo?». Es una pregunta amable y cuida el saber de todos.",
    ],
    vocab=[("reproducir", "copiar o dibujar de nuevo algo"), ("resguardar", "cuidar para que no se pierda ni se use mal"), ("permiso", "una respuesta de «sí» de quien corresponde"), ("ocasión", "momento especial en que se usa algo"), ("corresponde", "es lo adecuado según quien sabe")],
    worked=[
        w("Antes de copiar", "Quiero dibujar en mi cuaderno un símbolo que vi en una foto de un libro. ¿Qué hago primero?", ["Miro si la foto dice el pueblo y la fuente.", "Anoto una pregunta para el educador o la educadora.", "Espero la respuesta antes de dibujar el símbolo real."], "preguntar antes de copiar"),
        w("Si nadie responde", "Mandé mi pregunta, pero aún no hay respuesta. ¿Copio el símbolo igual?", ["Releo la regla: pregunto antes de copiar.", "Sin respuesta, no tengo permiso.", "Mientras tanto dibujo una figura de práctica mía."], "no copio hasta tener respuesta"),
    ],
    mistakes=[
        {"wrong": "Pensar que si está en internet o en un libro se puede copiar siempre.", "why": "Que esté a la vista no significa que sea para todos los usos.", "fix": "Pregunto a quien corresponde antes de usarlo."},
        {"wrong": "Usar un símbolo solo porque me gusta cómo se ve.", "why": "Puede tener una ocasión de uso importante para su pueblo.", "fix": "Pregunto cuándo corresponde usarlo."},
    ],
    tiers={
        "recovery": [
            ex("Quiero copiar un símbolo en mi cuaderno. ¿Qué hago primero: pregunto o copio?", "pregunto", "Primero se pide permiso a quien corresponde."),
            ex("¿Qué palabra significa «cuidar para que no se pierda ni se use mal»: resguardar o borrar?", "resguardar", "Resguardar es cuidar los saberes y los símbolos."),
            ex("¿Cuál es una pregunta amable: «¿Puedo dibujar esto?» o «Dame eso ya»?", "«¿Puedo dibujar esto?»", "Una pregunta amable pide permiso con respeto."),
        ],
        "understand": [
            ex("Verdadero o falso: si un símbolo se ve en un libro, se puede usar siempre y en cualquier lugar.", "Falso", "Verlo no da permiso ni dice en qué ocasión se usa."),
            ex("¿Quién puede decir cuándo corresponde usar un símbolo: el educador tradicional o un compañero que no lo sabe?", "el educador tradicional", "Quien conoce ese saber puede orientar su uso."),
            ex("Si nadie me da permiso, ¿copio el símbolo igual o espero?", "espero", "Sin permiso no se copia."),
        ],
        "apply": [
            ex("Escribe una pregunta corta para pedir permiso de dibujar un tejido de la sala. Empieza con «¿Puedo…». Elige la frase correcta: A) «¿Puedo dibujarlo en mi cuaderno?» B) «Lo dibujaré aunque no quieran».", "A", "A pide permiso; B ignora lo que otros piensan."),
            ex("Caso: Clara quiere pintar un símbolo en un cartel para la fiesta del curso. ¿Qué debe hacer antes?", "preguntar si corresponde", "Algunos símbolos tienen ocasiones de uso especiales."),
            ex("Ordena: A) copio B) recibo la respuesta C) pregunto. ¿En qué orden? Escribe las 3 letras.", "C, B, A", "Pregunto, recibo respuesta y recién después copio."),
        ],
        "reason": [
            ex("Tomás dice: «Si lo dibujo bonito, nadie se enoja». ¿Tiene razón? Responde Sí o No.", "No", "Que quede bonito no reemplaza el permiso de quien lo cuida."),
            ex("Un símbolo se usa en una ocasión especial de una comunidad. ¿Por qué conviene preguntar antes de ponerlo en un juego del recreo?", "porque puede perder su sentido o faltar el respeto", "Cambiar su uso sin saberlo puede ser una falta de respeto."),
        ],
        "challenge": [
            ex("Recibes 3 respuestas: A) «Sí, puedes dibujarlo» B) «No, por ahora» C) ninguna respuesta. ¿Con cuál puedo copiar el símbolo?", "A", "Solo A es un permiso; B es un no y C no es permiso."),
            ex("La escuela quiere hacer un mural con símbolos reales. Ordena de primera a última acción: A) pintar B) hablar con el educador tradicional C) escribir la pregunta.", "C, B, A", "Se escribe la pregunta, se conversa y luego se decide pintar."),
        ],
    },
    context=[ex("Tu curso hará una invitación para la fiesta de fin de año y alguien propone copiar un símbolo que vio en una foto. ¿Qué dos acciones propones antes de copiar?", "preguntar al educador tradicional y esperar su respuesta", "Se pregunta a quien corresponde y se respeta su respuesta.")],
    selfcheck=[ex("¿Qué significa resguardar?", "cuidar para que no se pierda ni se use mal", "Es cuidar los saberes."), ex("¿Qué hago si no me dan permiso?", "no copio", "Sin permiso no se reproduce."), ex("¿A quién le pregunto cuándo corresponde usar un símbolo?", "al educador tradicional o a la comunidad", "Ellos guardan ese saber.")],
    open_task=task(
        "Escribe en tu cuaderno una pequeña tarjeta con esta frase y complétala: «Antes de copiar el símbolo que vi, le voy a preguntar a ______ si puedo ______ y cuándo corresponde usarlo». Puedes elegir a quién preguntar: A) al educador/a tradicional de tu escuela B) a una persona de la comunidad que te indique tu profesor/a.",
        "Antes de copiar el símbolo que vi, le voy a preguntar al educador tradicional si puedo dibujarlo en mi cuaderno y cuándo corresponde usarlo.",
        ["completa la frase con una persona que corresponde", "incluye el permiso y la ocasión de uso", "no copia el símbolo real sin respuesta"],
        ["tarjeta escrita", "pregunta dicha en voz alta"],
        ["decidir solo sin preguntar", "preguntar a alguien que no sabe"],
        "Reconoce el cuidado en la pregunta; si copió el símbolo real, pídele que lo borre y espere la respuesta de la comunidad.",
    ),
    reinforce="Practica en voz alta la pregunta «¿Puedo dibujar esto y cuándo corresponde usarlo?» con alguien de tu casa.",
    extend="Cuenta a alguien de tu casa por qué es importante preguntar antes de copiar un símbolo de otro pueblo.",
)

register(
    LR5, 4,
    materials="Hoja, lápiz y las frases escritas en este cuaderno. Puedes responder dibujando o hablando.",
    use="Aprenderé a responder con respeto cuando veo un símbolo de otro pueblo: agradecer, describir y preguntar. Sirve para convivir y aprender juntos.",
    prior=["Sé decir gracias y por favor.", "Sé describir lo que veo y pedir permiso."],
    explain=[
        "Una respuesta respetuosa tiene tres partes. Primero agradezco a quien me mostró el símbolo. Después digo qué veo, sin inventar su significado. Por último hago una pregunta honesta sobre lo que no sé.",
        "Valorar un símbolo es reconocer que es importante para el pueblo que lo creó, aunque yo no lo entienda aún. No hace falta apropiarme de él ni usarlo como adorno. Apropiarme sería actuar como si fuera mío, sin permiso.",
        "Cuando una lengua o una escritura está en recuperación, cada persona puede ayudar con cuidado: escuchar, preguntar y respetar las respuestas. Mi trabajo es aprender de quien enseña en la comunidad y no hablar por ella.",
    ],
    vocab=[("agradecer", "decir gracias por lo que me enseñan"), ("valorar", "reconocer que algo es importante"), ("apropiarse", "usar algo ajeno como si fuera mío"), ("respuesta respetuosa", "agradezco, describo y pregunto"), ("comunidad", "grupo de personas que comparte su historia y su saber")],
    worked=[
        w("Responder con tres partes", "Una persona de la comunidad te muestra un tejido con rayas. ¿Qué respondes?", ["Agradezco: «Gracias por mostrármelo».", "Describo: «Veo muchas rayas rojas».", "Pregunto: «¿Puedo saber de qué pueblo es y cuándo se usa?»."], "Gracias; veo muchas rayas rojas; ¿de qué pueblo es y cuándo se usa?"),
        w("Elegir la respuesta que valora", "Dos respuestas: A) «Qué raro, no sirve» B) «Gracias, me gustaría aprender más». ¿Cuál valora?", ["Reviso si A reconoce lo importante del símbolo: no.", "Reviso si B agradece y quiere aprender: sí.", "Elijo B."], "B"),
    ],
    mistakes=[
        {"wrong": "Decir «qué raro» sobre un símbolo de otro pueblo.", "why": "Lo que no conozco no es raro; es algo que aún no sé.", "fix": "Digo «no lo conozco todavía, ¿me cuentas?»."},
        {"wrong": "Decir el significado como si lo supiera.", "why": "No tengo la fuente ni la voz de la comunidad.", "fix": "Describo y pregunto."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál es la primera parte de una respuesta respetuosa: agradecer, adivinar o reírse?", "agradecer", "Se empieza agradeciendo a quien enseñó."),
            ex("¿Cuál frase agradece: «Gracias por mostrármelo» o «Ya lo sabía»?", "«Gracias por mostrármelo»", "Esa frase reconoce lo que me enseñaron."),
            ex("¿Cuántas partes tiene una respuesta respetuosa: 1, 2 o 3?", "3", "Son agradecer, describir y preguntar."),
        ],
        "understand": [
            ex("Verdadero o falso: valorar un símbolo es usarlo como adorno sin preguntar.", "Falso", "Valorar es reconocer su importancia, no apropiarse de él."),
            ex("¿Qué significa apropiarse de un símbolo: cuidarlo o usarlo como si fuera mío?", "usarlo como si fuera mío", "Apropiarse es tomar algo ajeno sin permiso."),
            ex("¿Quién debe explicar el símbolo: la comunidad o yo adivinando?", "la comunidad", "Ella es la fuente del saber."),
        ],
        "apply": [
            ex("Te muestran una manta con cuadrados azules. Completa: «Gracias. Veo ______ azules. ¿Puedo preguntar ______?». Elige las palabras: A) cuadrados / de qué pueblo es B) lunas / nada.", "A", "A describe lo que se ve y hace una pregunta."),
            ex("Ordena: A) pregunto B) agradezco C) describo. ¿Cuál es el orden de la respuesta respetuosa? Escribe las 3 letras.", "B, C, A", "Se agradece, se describe y luego se pregunta."),
            ex("Mira esta respuesta: «Gracias. Veo tres rayas. ¿Puedo saber cuándo se usa?». ¿Cuántas partes de la respuesta respetuosa tiene?", "3", "Tiene agradecimiento, descripción y pregunta."),
        ],
        "reason": [
            ex("Una compañera dice «Eso no sirve para nada» ante un símbolo. ¿Qué podrías decirle con respeto en una frase?", "«Es importante para ese pueblo; preguntemos»", "Se valora el símbolo y se propone preguntar."),
            ex("¿Por qué es mejor decir «veo tres rayas» que «esto significa lluvia»?", "porque lo primero se ve y lo segundo es inventado", "Describir no atribuye un significado que no sé."),
        ],
        "challenge": [
            ex("¿Cuántas de las tres partes de la respuesta respetuosa (agradecer, describir, preguntar) faltan en la frase «Ya lo vi antes»?", "faltan 3 partes", "Ninguna de las tres partes está completa en esa frase."),
            ex("Dos amigos ven un símbolo. Ana dice «gracias y veo dos puntos». Beto dice «gracias, veo dos puntos, ¿de qué pueblo es?». ¿Quién tiene la respuesta más completa?", "Beto", "Beto agrega la pregunta."),
        ],
    },
    context=[ex("El educador tradicional visita tu curso y muestra un tejido. Tu compañera dice «Qué raro». Escribe una frase amable para ayudarla.", "«Gracias, lo veo por primera vez; ¿nos cuenta de qué pueblo es?»", "Cambia «raro» por agradecimiento y pregunta.")],
    selfcheck=[ex("¿Cuáles son las tres partes de la respuesta respetuosa?", "agradecer, describir y preguntar", "Esas tres partes forman la respuesta."), ex("¿Apropiarse es cuidar o usar sin permiso?", "usar sin permiso", "Es tomar algo ajeno."), ex("¿Quién da el significado de un símbolo?", "la comunidad", "Es su saber.")],
    open_task=task(
        "Elige una situación: A) una persona de la comunidad te muestra un tejido con rayas rojas y negras. B) tu profesor/a te muestra la foto de una tablilla de madera con signos de Rapa Nui. Escribe o di tu respuesta de tres partes: gracias, lo que ves y una pregunta. Puedes dibujar en vez de escribir.",
        "Situación A: «Gracias por mostrarnos el tejido. Veo rayas rojas y negras. ¿Puede contarnos de qué pueblo es?».",
        ["agradece", "describe sin inventar significado", "hace una pregunta a la comunidad o al educador/a tradicional"],
        ["respuesta oral o escrita", "dibujo de lo que ve"],
        ["decir «qué raro»", "dar un significado sin fuente"],
        "Marca con tres vistos buenos las partes que están y pide la que falte; recuerda que el significado lo cuenta quien pertenece al pueblo.",
    ),
    reinforce="Di en voz alta «gracias, veo…, ¿me cuentas…?» con un objeto de tu casa.",
    extend="Enseña a alguien de tu casa las tres partes de una respuesta respetuosa.",
)

# ------------------------------------------------------------------ LS05
register(
    LS5, 1,
    materials="Lápiz, hoja y las tarjetas de práctica escritas aquí. Las tarjetas son inventadas para este ejercicio.",
    use="Aprenderé a decir de qué pueblo es un símbolo, en qué material está y quién me lo muestra. Sirve para conocer con respeto cómo escribían o marcaban algunos pueblos.",
    prior=["Sé que en Chile viven distintos pueblos originarios.", "Sé nombrar materiales: madera, tela, cuerda."],
    explain=[
        "Algunos pueblos originarios han marcado o escrito con símbolos. En Rapa Nui hay tablillas de madera con signos tallados. En los Andes hay cordeles con nudos que guardan información. Cada pueblo tiene su forma.",
        "Para mirar un símbolo con respeto me hago tres preguntas. ¿De qué pueblo es? ¿En qué material está, o sea, cuál es su soporte? ¿Quién me lo muestra, o sea, cuál es su fuente? Con esos datos sé de dónde viene.",
        "Si no sé una respuesta, no la invento. Escribo una pregunta y se la hago al educador o a la educadora tradicional, o a la comunidad. Ellos conocen lo que significa y cómo se cuida.",
    ],
    vocab=[("símbolo", "marca o dibujo que quiere decir algo"), ("pueblo", "grupo con su historia, su lengua y su cultura"), ("soporte", "material donde está el símbolo"), ("fuente", "quien o dónde me dicen la información"), ("tablilla", "pieza plana y delgada, aquí de madera")],
    worked=[
        w("Tres preguntas", "Tarjeta de práctica: «Cordel con nudos. Pueblo andino. Lo muestra un museo». ¿Cuál es el soporte?", ["Busco el material: cordel.", "El pueblo es andino.", "La fuente es un museo."], "cordel"),
        w("Dato que falta", "Tarjeta de práctica: «Tablilla de madera con signos. Lo muestra un libro». ¿Qué dato no está?", ["Veo soporte: tablilla de madera.", "Veo fuente: un libro.", "No dice el pueblo."], "el pueblo"),
    ],
    mistakes=[
        {"wrong": "Pensar que un símbolo vale solo porque es antiguo.", "why": "Vale por lo que significa para su pueblo.", "fix": "Pregunto qué importancia tiene para su pueblo."},
        {"wrong": "Mezclar los pueblos: «todos escribían en madera».", "why": "No todos los pueblos usaron el mismo soporte.", "fix": "Anoto cuál pueblo y cuál soporte."},
    ],
    tiers={
        "recovery": [
            ex("Tarjeta de práctica: «Tablilla de madera con signos». ¿Cuál es el soporte?", "tablilla de madera", "El soporte es el material que lleva los signos."),
            ex("En los Andes hay cordeles con nudos. ¿Cuál es el soporte?", "cordel", "La cuerda es el material en que están los nudos."),
            ex("¿Cómo se llama quien o lo que me da la información: fuente o dibujo?", "fuente", "Fuente es de dónde viene la información."),
        ],
        "understand": [
            ex("Verdadero o falso: todos los pueblos usan el mismo soporte para sus símbolos.", "Falso", "Hay madera, cordel, tela y otros soportes."),
            ex("¿Qué dato dice a qué grupo de personas pertenece el símbolo: pueblo o soporte?", "pueblo", "El pueblo es el grupo que lo creó."),
            ex("En Rapa Nui hay tablillas con signos tallados. ¿Son de madera o de papel?", "madera", "Las tablillas son de madera."),
        ],
        "apply": [
            ex("Tarjeta de práctica: «Tela con rayas. Fuente: un taller. Pueblo: no se dice». ¿Qué pregunta escribes?", "¿De qué pueblo es la tela?", "Falta el pueblo, así que se pregunta."),
            ex("Tarjeta: «Cordel con nudos. Pueblo andino. Fuente: una revista». ¿Cuántos datos tiene en total (pueblo, soporte, fuente)?", "3", "Tiene los tres datos."),
            ex("Une: Rapa Nui con A) tablillas de madera B) cordeles con nudos. ¿Qué letra va?", "A", "Rapa Nui tiene tablillas de madera con signos."),
        ],
        "reason": [
            ex("Marta dice que un cordel con nudos es de Rapa Nui. ¿Qué datos de su ficha conviene revisar?", "el pueblo y la fuente", "Sin pueblo ni fuente en la ficha, no se puede asegurar de dónde viene."),
            ex("¿Por qué es mejor escribir una pregunta que inventar la respuesta?", "porque inventar puede ser falso", "Una pregunta cuida la verdad y el respeto."),
        ],
        "challenge": [
            ex("Tarjeta A: pueblo rapanui, madera. Tarjeta B: pueblo andino, cordel. ¿Cuántos soportes distintos hay?", "2", "Hay madera y cordel."),
            ex("Una tarjeta dice solo «símbolo bonito». ¿Cuántos datos de procedencia tiene?", "0", "No dice pueblo, soporte ni fuente."),
        ],
    },
    context=[ex("Tu profesora trae una tarjeta que dice: «Tablilla de madera, Rapa Nui, fuente: un libro». Di en voz alta los tres datos usando las palabras pueblo, soporte y fuente.", "pueblo: Rapa Nui; soporte: tablilla de madera; fuente: un libro", "Se nombran los tres datos en orden.")],
    selfcheck=[ex("¿Cuál es el material donde está el símbolo?", "soporte", "Soporte es el material."), ex("¿Qué hago si falta un dato?", "pregunto", "No invento, pregunto."), ex("¿Quién conoce lo que significa un símbolo de su pueblo?", "la comunidad", "Ellos lo saben.")],
    open_task=task(
        "Escoge una de estas tarjetas y dibuja el soporte: A) tablilla de madera de Rapa Nui B) cordel con nudos de los Andes. Escribe «pueblo», «soporte» y «fuente» debajo y anota una pregunta para el educador/a tradicional o la comunidad.",
        "Dibujé un cordel con 4 nudos. Pueblo: andino. Soporte: cordel. Fuente: mi libro. Pregunta: ¿para qué se usaba?",
        ["identifica el soporte", "escribe pueblo y fuente", "formula una pregunta"],
        ["dibujo del soporte", "pregunta escrita"],
        ["inventar el significado", "dejar la fuente en blanco"],
        "Revisa que anotó los tres datos; si inventó el significado, pídele cambiarlo por una pregunta.",
    ),
    reinforce="Nombra tres soportes y di un ejemplo con cada uno.",
    extend="Cuenta a alguien de tu casa qué es una tablilla de Rapa Nui y qué es un cordel con nudos de los Andes.",
)

register(
    LS5, 2,
    materials="Hoja, lápiz y las figuras de práctica escritas aquí. No son símbolos reales.",
    use="Aprenderé a describir las formas de un símbolo sin inventar lo que significa. Sirve para mirar con atención y respeto.",
    prior=["Reconozco figuras simples.", "Sé contar hasta 10."],
    explain=[
        "Cuando miro un símbolo, puedo fijarme en su forma, su color, su tamaño y cuántas partes tiene. Eso es describir. Todas las personas pueden describir lo que ven.",
        "Lo que significa un símbolo es otra cosa. Ese significado lo sabe el pueblo que lo creó. Si lo invento, puedo equivocarme y dañar el respeto hacia ese pueblo. Por eso mejor pregunto.",
        "Voy a practicar con figuras inventadas. Primero cuento las partes. Después digo cómo son. Al final escribo una pregunta que le haría a la comunidad. Así entreno mis ojos y mi respeto.",
    ],
    vocab=[("forma", "cómo se ve el contorno"), ("parte", "un pedacito de la figura"), ("describir", "decir lo que se ve"), ("inventar", "decir algo que no sé si es verdad"), ("preguntar", "pedir información a quien sabe")],
    worked=[
        w("Contar partes", "Figura de práctica: ● ● ▲. ¿Cuántas partes tiene?", ["Cuento los círculos: 2.", "Cuento los triángulos: 1.", "2 más 1 son 3."], "3 partes"),
        w("Elegir describir", "Frase A: «Hay un cuadrado rojo». Frase B: «Es la casa de un amigo». ¿Cuál describe?", ["A habla de forma y color, que se ven.", "B dice algo que no se ve.", "Describe la frase A."], "A"),
    ],
    mistakes=[
        {"wrong": "Decir «es un animal» al ver una figura con puntas.", "why": "A mí me parece, pero el pueblo puede pensar otra cosa.", "fix": "Digo «tiene tres puntas»."},
        {"wrong": "No contar las partes y decir «muchas».", "why": "No miré con atención.", "fix": "Cuento una por una."},
    ],
    tiers={
        "recovery": [
            ex("Figura de práctica: ■ ■. ¿Cuántos cuadrados hay?", "2", "Se cuentan dos cuadrados."),
            ex("Figura de práctica: ▲ ▲ ▲ ▲. ¿Cuántos triángulos hay?", "4", "Hay cuatro triángulos."),
            ex("Describir es decir lo que se ve. ¿Verdadero o falso?", "Verdadero", "Eso es exactamente describir."),
        ],
        "understand": [
            ex("«Es redondo y rojo». ¿Es descripción o significado?", "descripción", "Dice forma y color."),
            ex("«Significa que va a llover». ¿Se puede ver en la figura?", "No", "El significado no se ve."),
            ex("¿Quién sabe lo que significa un símbolo de un pueblo: el pueblo o cualquiera?", "el pueblo", "Es su saber."),
        ],
        "apply": [
            ex("Figura de práctica: ● ● ● ■. ¿Cuántas formas hay en total?", "4", "Tres círculos y un cuadrado suman cuatro."),
            ex("Figura de práctica: ■ ■ ▲ ▲ ▲. ¿Cuántos triángulos más que cuadrados hay?", "1", "Hay 3 triángulos y 2 cuadrados."),
            ex("Elige la mejor descripción de ▲▲: A) «Dos triángulos» B) «Dos montañas».", "A", "A dice lo que se ve."),
        ],
        "reason": [
            ex("Si ves una figura y no sabes qué significa, ¿qué es mejor: preguntar o adivinar?", "preguntar", "Preguntar cuida el respeto."),
            ex("Lola dice «la figura ●| es una luna». ¿Qué cambiarías?", "«un círculo con una raya»", "Eso describe lo que se ve."),
        ],
        "challenge": [
            ex("Figura de práctica: ■■■ ●●. ¿Cuántas formas hay y cuántas son círculos?", "5 formas y 2 círculos", "Tres cuadrados y dos círculos son cinco formas."),
            ex("Dos amigos describen ▲●: uno dice «un triángulo y un círculo»; el otro dice «una fiesta». ¿Quién describe?", "el primero", "El segundo dice una idea que no se ve."),
        ],
    },
    context=[ex("Tu amiga te enseña un dibujo que hizo con 3 cuadrados y 1 círculo. Descríbelo diciendo cuántas formas hay.", "Hay 4 formas: 3 cuadrados y 1 círculo", "Se cuentan y se nombran las formas.")],
    selfcheck=[ex("¿Qué hago primero con un símbolo: describo o invento?", "describo", "Se mira antes de pensar."), ex("¿Cuántas partes tiene ■▲●?", "3", "Es una de cada forma."), ex("¿A quién pregunto el significado?", "a la comunidad o al educador tradicional", "Ellos lo saben.")],
    open_task=task(
        "Elige una figura de práctica: A) ■ ■ ▲ B) ● ● ● ■. Dibújala y escribe: cuántas formas tiene, cuáles son y una pregunta para el educador/a tradicional o la comunidad sobre símbolos reales.",
        "Figura A: tiene 3 formas, dos cuadrados y un triángulo. Pregunta: ¿cómo cuidan los dibujos de sus telas?",
        ["cuenta bien las partes", "describe sin inventar significado", "hace una pregunta a quien corresponde"],
        ["dibujo", "descripción escrita u oral"],
        ["contar mal", "decir un significado sin fuente"],
        "Felicita la precisión del conteo; si puso significado, invítalo a transformarlo en pregunta.",
    ),
    reinforce="Describe en voz alta cinco figuras que dibujes tú.",
    extend="Observa un patrón de una tela de tu casa y cuéntalo: cuántas formas hay en una fila.",
)

register(
    LS5, 3,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a preguntar cuándo corresponde copiar o usar un símbolo. Sirve para cuidar lo que es valioso para otros.",
    prior=["Sé pedir permiso con respeto.", "Sé que algunos símbolos son importantes para su pueblo."],
    explain=[
        "Un símbolo puede ser muy importante para un pueblo. Algunos se usan en fiestas o ceremonias, otros en la vida diaria. No siempre se pueden copiar o usar en cualquier lugar.",
        "Por eso, antes de copiar un símbolo, pregunto. Pregunto si puedo dibujarlo y cuándo corresponde usarlo. La respuesta me la da el educador o la educadora tradicional, o una persona de la comunidad.",
        "Si la respuesta es no, o si aún no hay respuesta, no copio. Puedo dibujar mis propias figuras de práctica. Así aprendo sin dañar. Respetar también es una forma de valorar.",
    ],
    vocab=[("copiar", "dibujar igual que otro"), ("permiso", "un sí de quien corresponde"), ("ceremonia", "momento especial y respetuoso de un grupo"), ("cuidar", "proteger para que no se dañe"), ("respeto", "tratar con cuidado lo que es importante para otros")],
    worked=[
        w("Preguntar antes", "Quiero dibujar un símbolo del libro. ¿Qué pregunto?", ["Pienso en quién sabe: el educador tradicional.", "Pregunto: «¿Puedo dibujarlo y cuándo corresponde usarlo?»."], "¿Puedo dibujarlo y cuándo corresponde usarlo?"),
        w("Si me dicen que no", "Me dijeron que todavía no puedo dibujarlo. ¿Qué hago?", ["Acepto la respuesta.", "Dibujo una figura de práctica mía en su lugar."], "no lo dibujo y uso una figura de práctica"),
    ],
    mistakes=[
        {"wrong": "Copiar sin avisar «porque es solo un dibujo».", "why": "Puede ser importante para su pueblo.", "fix": "Pregunto primero."},
        {"wrong": "Enojarme si dicen que no.", "why": "La respuesta cuida lo valioso.", "fix": "Agradezco y busco otra forma de aprender."},
    ],
    tiers={
        "recovery": [
            ex("Antes de copiar un símbolo, ¿pregunto o copio?", "pregunto", "Primero se pide permiso."),
            ex("¿Quién me puede decir cuándo usar un símbolo: el educador tradicional o nadie?", "el educador tradicional", "Es quien conoce ese saber."),
            ex("Si dicen «no», ¿copio igual o acepto?", "acepto", "Se respeta la respuesta."),
        ],
        "understand": [
            ex("¿Por qué no siempre se pueden copiar los símbolos?", "porque algunos son importantes para su pueblo", "Pueden tener usos especiales."),
            ex("Verdadero o falso: preguntar es una forma de respetar.", "Verdadero", "Preguntar muestra cuidado."),
            ex("¿Qué es mejor dibujar si no tengo permiso: un símbolo real o una figura mía de práctica?", "una figura mía de práctica", "Así aprendo sin dañar."),
        ],
        "apply": [
            ex("Tienes que pedir permiso. Elige la frase: A) «¿Puedo dibujarlo?» B) «Lo copio ya».", "A", "A pide permiso."),
            ex("Ordena: A) copio B) pregunto C) espero. ¿Cuál es el orden correcto? Escribe 3 letras.", "B, C, A", "Pregunto, espero y recién copio si me dicen que sí."),
            ex("Si me dicen «sí, pero solo en tu cuaderno», ¿puedo ponerlo en un cartel de la escuela?", "No", "El permiso fue solo para el cuaderno."),
        ],
        "reason": [
            ex("Si un símbolo se usa en una ceremonia, ¿por qué conviene preguntar antes de dibujarlo en un juego?", "porque puede perder su sentido", "Usarlo en un juego cambia su sentido."),
            ex("Andrés dice «si no responden, copio». ¿Está bien?", "No", "Sin respuesta no hay permiso."),
        ],
        "challenge": [
            ex("Hay 3 tarjetas: una con «sí», una con «no» y una sin respuesta. ¿Con cuántas puedo copiar?", "1", "Solo con la que dice sí."),
            ex("Camilo pidió permiso y le dijeron «sí, solo para mirar». ¿Puede copiar?", "No", "El permiso fue solo para mirar."),
        ],
    },
    context=[ex("En tu clase quieren hacer un cartel con un símbolo del libro. Escribe una pregunta corta para el educador tradicional.", "¿Podemos dibujar este símbolo y cuándo corresponde usarlo?", "La pregunta pide permiso y la ocasión de uso.")],
    selfcheck=[ex("¿Qué hago antes de copiar?", "pregunto", "Es la regla."), ex("¿Y si dicen que no?", "acepto", "Se respeta la respuesta."), ex("¿A quién pregunto?", "al educador tradicional o a la comunidad", "Ellos conocen ese saber.")],
    open_task=task(
        "Escribe una tarjeta con la pregunta «¿Puedo ______ y cuándo corresponde usarlo?». Completa con una de estas opciones: A) dibujar el símbolo de la tablilla de Rapa Nui del libro B) copiar el dibujo de la tela de la sala. Preséntala al educador/a tradicional o a una persona de la comunidad que tu profesor/a indique.",
        "¿Puedo dibujar el símbolo del libro y cuándo corresponde usarlo?",
        ["completa la pregunta", "reconoce que el permiso es de quien corresponde", "acepta la respuesta"],
        ["tarjeta escrita", "pregunta dicha"],
        ["copiar antes de preguntar", "no esperar la respuesta"],
        "Reconoce la pregunta bien hecha; si copió el símbolo real antes, recuerda que se espera la respuesta.",
    ),
    reinforce="Practica la pregunta de permiso en voz alta tres veces.",
    extend="Cuenta en casa qué harías si te dicen que todavía no puedes copiar un símbolo.",
)

register(
    LS5, 4,
    materials="Hoja, lápiz y las frases escritas en este cuaderno. Puedes responder hablando o dibujando.",
    use="Aprenderé a valorar un símbolo de otro pueblo sin quedarme con él. Sirve para convivir con respeto y aprender juntos.",
    prior=["Sé decir gracias.", "Sé describir y preguntar."],
    explain=[
        "Valorar un símbolo es reconocer que importa para su pueblo. No hace falta entenderlo todo para valorarlo. Basta con tratarlo con cuidado y con interés.",
        "Apropiarme de un símbolo sería usarlo como si fuera mío, por ejemplo para decorar un cuaderno o hacer una broma. Eso no es respeto. En cambio, puedo agradecer, describir lo que veo y preguntar a la comunidad.",
        "Mi respuesta respetuosa tiene tres partes: gracias, lo que veo y una pregunta. Cuando la hago, las personas que me muestran sus saberes saben que los cuido. Así aprendemos juntos.",
    ],
    vocab=[("valorar", "reconocer que algo importa"), ("apropiarse", "usar como mío algo ajeno"), ("agradecer", "decir gracias"), ("broma", "cosa que se hace para reír"), ("convivir", "vivir y aprender juntos")],
    worked=[
        w("Respuesta de tres partes", "Te muestran una tela con un dibujo. ¿Qué dices?", ["Digo gracias.", "Describo: «Veo un dibujo con rayas».", "Pregunto: «¿De qué pueblo es?»."], "Gracias; veo un dibujo con rayas; ¿de qué pueblo es?"),
        w("Elegir con respeto", "A) Usarlo para disfrazarme. B) Preguntar cómo se cuida. ¿Cuál valora?", ["A usa el símbolo como juego.", "B muestra interés y cuidado.", "Elijo B."], "B"),
    ],
    mistakes=[
        {"wrong": "Usar un símbolo de otro pueblo como disfraz.", "why": "Es apropiarse y puede dañar.", "fix": "Pregunto y aprendo cómo se cuida."},
        {"wrong": "No decir nada por vergüenza.", "why": "No agradezco ni aprendo.", "fix": "Digo gracias y una pregunta simple."},
    ],
    tiers={
        "recovery": [
            ex("¿Con qué palabra empiezo mi respuesta: gracias o nada?", "gracias", "Se empieza agradeciendo."),
            ex("¿Cuántas partes tiene la respuesta respetuosa?", "3", "Son agradecer, describir y preguntar."),
            ex("Valorar un símbolo es reconocer que importa. ¿Verdadero o falso?", "Verdadero", "Eso es valorar."),
        ],
        "understand": [
            ex("¿Qué es apropiarse: usar algo ajeno como si fuera mío o cuidarlo?", "usar algo ajeno como si fuera mío", "Es lo contrario de respetar."),
            ex("¿Usar un símbolo como disfraz es respetuoso?", "No", "Puede dañar el sentido del símbolo."),
            ex("¿Hace falta entenderlo todo para valorar un símbolo?", "No", "Basta con tratarlo con cuidado."),
        ],
        "apply": [
            ex("Elige la respuesta respetuosa: A) «Gracias, veo rayas, ¿me cuentas?» B) «Qué raro».", "A", "A agradece, describe y pregunta."),
            ex("Ordena: A) preguntar B) agradecer C) describir. Escribe 3 letras.", "B, C, A", "Se agradece, se describe y se pregunta."),
            ex("En la frase «Gracias, veo dos puntos», ¿qué parte falta?", "la pregunta", "Tiene gracias y descripción."),
        ],
        "reason": [
            ex("Tu amigo quiere dibujar un símbolo en su mochila para que se vea lindo. ¿Qué le propones?", "preguntar primero si corresponde", "El símbolo puede tener un valor especial."),
            ex("¿Por qué agradecer es importante cuando alguien me muestra su saber?", "porque reconoce lo que me enseñó", "El agradecimiento valora la enseñanza."),
        ],
        "challenge": [
            ex("Hay tres frases: «Gracias», «Veo rayas», «¿De qué pueblo es?». ¿Cuál es la pregunta?", "«¿De qué pueblo es?»", "Es la que busca información."),
            ex("Una respuesta tiene agradecimiento y pregunta pero no descripción. ¿Cuántas partes tiene?", "2", "Tiene dos de las tres."),
        ],
    },
    context=[ex("En una exposición de tu escuela una persona de la comunidad muestra un tejido. Dices: «Gracias. Veo rayas rojas». ¿Qué parte de la respuesta falta?", "la pregunta", "Falta preguntar algo que no sabes.")],
    selfcheck=[ex("¿Qué es valorar?", "reconocer que algo importa", "Eso es valorar."), ex("¿Qué es apropiarse?", "usar algo ajeno como mío", "Eso no es respetuoso."), ex("¿Cómo termino mi respuesta?", "con una pregunta", "Se cierra preguntando.")],
    open_task=task(
        "Elige una situación: A) una persona de la comunidad te muestra una tela con dibujos. B) tu profesor/a te muestra una foto de una tablilla con signos de Rapa Nui. Escribe o di tu respuesta de tres partes y dibuja algo que hayas visto.",
        "Situación B: «Gracias por mostrarnos. Veo una tablilla con muchos signos. ¿Qué nos puede contar sobre ella?».",
        ["agradece", "describe", "pregunta a la comunidad o al educador/a tradicional"],
        ["respuesta oral o escrita", "dibujo"],
        ["decir que es raro", "inventar significado"],
        "Reconoce las tres partes; si falta alguna, ayúdale a agregarla.",
    ),
    reinforce="Practica «gracias, veo…, ¿me cuentas…?» tres veces.",
    extend="Explica en casa la diferencia entre valorar y apropiarse con un ejemplo tuyo.",
)
