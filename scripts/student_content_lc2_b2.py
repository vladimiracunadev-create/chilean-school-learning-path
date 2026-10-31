"""Cuaderno del estudiante, 2.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LF01 (relatos orales en lengua indígena, contexto de fortalecimiento) y
OA LF02 (descripción del medio natural en lengua indígena).

Los relatos y descripciones de práctica están en castellano, son inventados y no pertenecen a
ningún pueblo. Solo se usan pocas palabras de mapuzugun muy conocidas (mari mari, mapu, ko, antü,
kuyen) y siempre con la indicación de que el educador/a tradicional o la comunidad confirma su
escritura, pronunciación y uso. Este cuaderno no inventa palabras ni gramática de ninguna lengua.
"""
from __future__ import annotations

from student_lessons import arith, ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


LF01 = "LC02 OA LF01"
LF02 = "LC02 OA LF02"

AVISO = "La lengua y los relatos de un pueblo los enseña su educador/a tradicional o su comunidad."

RELATO = ("Una tarde, la niña Alba fue al río con su abuelo. Primero vieron una garza quieta en la orilla. "
          "Después el abuelo le mostró cómo lavar una olla. Más tarde empezó a llover y corrieron bajo un árbol. "
          "Al final volvieron a casa y tomaron té caliente.")
DESC = ("Hay un río ancho junto a un cerro verde. El agua es fría y clara. "
        "Sobre el cerro vuela un cóndor grande. Cerca de la orilla crecen juncos altos.")

# ================================================================ LF01
register(
    LF01, 1,
    materials="Este cuaderno y lápiz. Los relatos de práctica están escritos aquí en castellano. Un adulto puede leerlos en voz alta.",
    use="Aprenderé a reconocer quién cuenta un relato, para qué lo cuenta y en qué momento. Sirve para escuchar relatos de una lengua indígena con respeto, aunque no entienda todas las palabras.",
    prior=["Sé escuchar un relato completo.", "Sé que la fuente es quien enseña."],
    explain=[
        "Un relato oral es una historia que se cuenta con la voz. Tiene voces: quien relata y, a veces, los personajes. También tiene un propósito, que es para qué se cuenta: para enseñar, para recordar, para cuidar a los niños o para compartir una alegría. Y tiene un contexto, que es cuándo y dónde se cuenta. Los relatos son importantes porque guardan lo que una comunidad quiere recordar y enseñar. Por qué es importante cada relato lo explica su propia comunidad.",
        "Hablamos de fortalecimiento de una lengua cuando muchas personas todavía la usan y se quiere que siga viva en la casa, en la escuela y en la comunidad. En ese caso, los relatos en esa lengua los cuentan hablantes de la comunidad. Una fuente validada es una persona o recurso que la comunidad reconoce como confiable.",
        "Cuando escuchas, no necesitas entender cada palabra. Fíjate en la voz, en el propósito y en el contexto. Anota quién relató y pide permiso antes de repetir un relato que no es tuyo. Si no entiendes, pregunta; no inventes lo que falta.",
    ],
    vocab=[("relato", "historia que se cuenta con la voz"), ("voz", "quien habla en un relato"), ("propósito", "para qué se cuenta algo"), ("contexto", "cuándo y dónde se cuenta algo"), ("fuente validada", "persona o recurso que la comunidad reconoce como confiable")],
    worked=[
        {"title": "Voz, propósito y contexto", "problem": f"Un educador tradicional cuenta en el patio, antes del recreo, este relato de práctica: «{RELATO}». Lo cuenta para enseñar a cuidar el río. ¿Cuál es la voz, el propósito y el contexto?", "steps": ["La voz es el educador tradicional, que relata.", "El propósito es enseñar a cuidar el río.", "El contexto es el patio, antes del recreo."], "answer": "Voz: el educador; propósito: enseñar a cuidar el río; contexto: el patio antes del recreo"},
        {"title": "Cuando no se entiende", "problem": "Escuchas un relato y hay una palabra que no entiendes. ¿Qué haces?", "steps": ["No invento lo que quiere decir.", "Espero a que termine el relato.", "Después pregunto a quien lo relató."], "answer": "Esperar a que termine y preguntar a quien relató"},
    ],
    mistakes=[
        {"wrong": "Interrumpir el relato para preguntar cada palabra.", "why": "Quien relata pierde el hilo y el relato se corta.", "fix": "Escucha entero y pregunta al final."},
        {"wrong": "Pensar que si no entiendes todas las palabras, no sirve escuchar.", "why": "Puedes aprender mucho de la voz, el ritmo y el contexto.", "fix": "Escucha con atención y anota lo que sí entendiste."},
    ],
    tiers={
        "recovery": [
            ex("Quien cuenta el relato con su voz se llama...: ¿relator o espectador?", "Relator", "Relator es quien cuenta el relato."),
            ex("Un abuelo cuenta una historia para que los niños aprendan a cuidar el fuego del hogar. ¿Cuál es el propósito?", "Enseñar a cuidar el fuego del hogar", "El propósito es para qué se cuenta."),
            ex("Contexto es cuándo y dónde se cuenta. Si se cuenta de noche junto a la estufa, ¿cuál es el contexto?", "De noche junto a la estufa", "Dice cuándo y dónde."),
        ],
        "understand": [
            ex("Fortalecer una lengua es hacer que siga viva en la casa, la escuela y la comunidad. ¿Para qué sirve escuchar relatos en esa lengua?", "Para que la lengua siga viva", "Los relatos mantienen la lengua en uso."),
            ex("Una fuente validada es una persona o recurso que la comunidad reconoce como confiable. ¿Cuál es una fuente validada: un educador tradicional o un video sin autor?", "Un educador tradicional", "La comunidad lo reconoce como confiable."),
            ex("Un relato puede guardar lo que una comunidad quiere recordar y enseñar. ¿Por qué es importante cuidar los relatos?", "Porque guardan lo que la comunidad quiere recordar y enseñar", "Los relatos son importantes para la comunidad a la que pertenecen."),
        ],
        "apply": [
            ex(f"Lee: «{RELATO}» ¿Qué animal vieron primero?", "Una garza", "El texto dice que primero vieron una garza quieta en la orilla."),
            ex("Ficha: «Relata: Doña Rosa. Para: cuidar a los niños. Cuándo: antes de dormir». ¿Cuál es el propósito?", "Cuidar a los niños", "La ficha dice «Para: cuidar a los niños»."),
            ex("Escucha cuatro relatos: A (para enseñar), B (para recordar), C (para enseñar), D (para compartir una alegría). ¿Cuántos relatos son para enseñar?", "2", "Son A y C."),
        ],
        "reason": [
            ex("Pablo cree que si no entiende todo, no puede aprender del relato. ¿Qué le dices?", "Que puede aprender de la voz, el ritmo y el contexto", "No se necesita entender cada palabra para escuchar con respeto."),
            ex("Una niña repite un relato de una comunidad sin avisar. ¿Qué debió hacer antes?", "Pedir permiso", "El relato es de la comunidad."),
        ],
        "challenge": [
            ex("Dos fichas: 1) «Relata: un amigo. Contexto: el recreo. Fuente: no sé». 2) «Relata: una educadora tradicional. Contexto: la sala. Fuente: la comunidad». ¿Cuál ficha tiene fuente validada?", "La ficha 2", "La educadora tradicional es reconocida por la comunidad."),
            ex("Un relato se cuenta cada invierno cuando la familia se reúne. ¿Qué dato cambia si ahora se cuenta en verano: el contexto o el propósito?", "El contexto", "Cambió cuándo se cuenta, no para qué."),
        ],
    },
    context=[ex("Tu curso invita a una abuela de la comunidad a contar un relato. Al llegar ella, ¿qué dato anotas primero: su nombre o el color de su ropa?", "Su nombre", "Su nombre dice quién relata y es la fuente.")],
    selfcheck=[
        ex("¿Qué es el propósito de un relato?", "Para qué se cuenta", "Es la razón por la que se cuenta."),
        ex("En Lengua y Cultura: ¿Qué es el contexto?", "Cuándo y dónde se cuenta", "Es el momento y el lugar."),
        ex("Si no entiendes una palabra, ¿qué haces?", "Espero y pregunto al final", "No se interrumpe ni se inventa."),
    ],
    open_task=task(
        f"Pide a un adulto que lea en voz alta este relato inventado: «{RELATO}». Escucha sin interrumpir. Después completa tres líneas: Voz (quién relata), Propósito (si fue contado para enseñar o para compartir) y Contexto (cuándo y dónde lo contaría esa persona). {AVISO}",
        "Voz: mi tío. Propósito: compartir un recuerdo del río. Contexto: en la mesa, después del almuerzo.",
        ["escucha entero sin interrumpir", "escribe voz, propósito y contexto", "no inventa datos que no oyó"],
        ["tres líneas escritas"],
        ["interrumpir para preguntar cada palabra", "inventar un propósito que no se dijo"],
        "Reconoce la escucha atenta y pregunta qué datos puso con certeza y cuáles dedujo. Aclara que el relato es inventado.",
    ),
    reinforce="Escucha un cuento corto de tu casa y anota quién lo cuenta y para qué.",
    extend="Pregunta a un adulto cuándo le contaban relatos cuando era niño y anota su respuesta.",
)

register(
    LF01, 2,
    materials="Este cuaderno y lápiz. Un adulto puede leer en voz alta los relatos de práctica.",
    use="Aprenderé a sacar la información importante de un relato y a ordenar lo que pasó, sin traducir palabra por palabra. Sirve para comprender el sentido del relato y no solo las palabras sueltas.",
    prior=["Sé quién relata y para qué.", "Sé contar qué pasó primero y qué pasó después."],
    explain=[
        "Para comprender un relato fíjate en la información: quién es el personaje, dónde ocurre y qué pasa. También fíjate en la secuencia, que es el orden en que pasan las cosas: primero, después, más tarde y al final. Esas palabras te ayudan a no perderte.",
        "Cuando alguien traduce un relato, no basta cambiar cada palabra por otra. Las lenguas dicen las ideas de maneras distintas. Por ejemplo, en castellano decimos «llueve a cántaros» y no hablamos de cántaros de verdad: queremos decir que llueve mucho. Por eso se traduce el sentido y no solo las palabras.",
        "Si el relato está en una lengua indígena, la mejor ayuda es el educador o educadora tradicional o un recurso hecho por la comunidad, con apoyo de imágenes, gestos y palabras conocidas. Tú cuentas lo que entendiste y dices qué parte no entendiste.",
    ],
    vocab=[("información", "datos importantes del relato"), ("secuencia", "orden en que pasan las cosas"), ("sentido", "idea que quiere decir el texto"), ("traducir", "decir en otra lengua lo mismo que se dijo"), ("apoyo", "ayuda para comprender")],
    worked=[
        {"title": "Ordenar la secuencia", "problem": f"Del relato «{RELATO}» ordena estos hechos: A) tomaron té caliente, B) vieron una garza, C) empezó a llover. ¿Cuál es el orden?", "steps": ["Primero vieron la garza (B).", "Más tarde empezó a llover (C).", "Al final tomaron té caliente (A)."], "answer": "B, C, A"},
        {"title": "No traducir palabra por palabra", "problem": "Un amigo dice «está lloviendo a cántaros» y alguien lo traduce literalmente como «caen cántaros del cielo». ¿Qué sentido se pierde?", "steps": ["«A cántaros» es una forma de decir «mucho».", "La traducción literal habla de cántaros de verdad.", "Se pierde el sentido: llueve muy fuerte."], "answer": "Se pierde que quiere decir que llueve mucho"},
    ],
    mistakes=[
        {"wrong": "Cambiar cada palabra por otra y creer que ya entendiste.", "why": "Las lenguas dicen las ideas de maneras distintas y el sentido se puede perder.", "fix": "Cuenta la idea con tus palabras y pregunta si es correcta."},
        {"wrong": "Ordenar los hechos de cualquier forma.", "why": "La secuencia cambia el significado del relato.", "fix": "Fíjate en primero, después, más tarde y al final."},
    ],
    tiers={
        "recovery": [
            ex(f"En el relato «{RELATO}», ¿quién acompañó a Alba al río?", "Su abuelo", "El texto dice «fue al río con su abuelo»."),
            ex("La secuencia es el orden en que pasan las cosas. ¿Cuál palabra indica el primer hecho: «al final» o «primero»?", "Primero", "Primero marca el comienzo."),
            ex("«Llueve a cántaros» quiere decir que llueve mucho. ¿Hay cántaros reales que caen del cielo?", "No", "Es una forma de decir que llueve mucho."),
        ],
        "understand": [
            ex(f"En el relato de práctica «{RELATO}», ¿qué hicieron cuando empezó a llover?", "Corrieron bajo un árbol", "Eso dice el texto."),
            ex("Un niño dice «estoy en las nubes» para decir que no estaba atento. ¿Está en el cielo de verdad?", "No", "Es una forma de decir que está distraído."),
            ex("¿Qué es mejor para comprender un relato en lengua indígena: la ayuda de la comunidad o adivinar el significado?", "La ayuda de la comunidad", "Así evitas equivocarte."),
        ],
        "apply": [
            ex(f"Ordena los hechos del relato «{RELATO}»: A) volvieron a casa, B) el abuelo mostró cómo lavar una olla, C) vieron una garza. Escribe las letras en orden.", "C, B, A", "Primero la garza, después la olla y al final volvieron a casa."),
            arith("Alba escuchó un relato de 5 hechos. Ya contó 3 hechos en orden. ¿Cuántos hechos le faltan por contar?", "5-3", "Se restan los hechos ya contados."),
            ex("Alguien dice «me tomó el pelo». ¿Qué quiere decir: a) me hizo una broma o b) me tocó el pelo con la mano? Responde con la letra.", "a", "Es una forma de decir que le hicieron una broma; no es el sentido literal."),
        ],
        "reason": [
            ex("Teo tradujo cada palabra de un relato y su sentido cambió. ¿Cómo podría hacerlo mejor?", "Preguntando el sentido a quien conoce la lengua", "Quien conoce la lengua sabe qué quiere decir."),
            ex("En un relato, un personaje llegó al cerro después de cruzar el río. Un niño dijo que llegó antes de cruzar. ¿Qué palabra le ayudaría a corregir?", "Después", "Después marca el orden de lo que pasó."),
        ],
        "challenge": [
            ex("Lee: «Primero, Sol buscó leña. Después, encendió una estufa con ayuda de su tío. Más tarde, hizo té. Al final, durmió». ¿Cuántos hechos hay y cuál es el último?", "4; durmió", "Se cuentan buscar leña, encender, hacer té y dormir."),
            ex("Un amigo oyó «te saqué un peso de encima» y entendió que le quitó dinero. ¿Cuál es el sentido real: quitar una preocupación o quitar dinero?", "Quitar una preocupación", "Es una expresión con sentido distinto al literal."),
        ],
    },
    context=[ex("Una abuela cuenta un relato y usa una expresión que no entiendes. ¿Qué haces al terminar?", "Le pregunto qué quiso decir", "Preguntar evita inventar.")],
    selfcheck=[
        ex("¿Qué es la secuencia?", "El orden en que pasan las cosas", "Primero, después, más tarde y al final."),
        ex("¿Se puede traducir siempre palabra por palabra?", "No", "El sentido puede cambiar."),
        ex("¿Qué haces si no entiendes una parte?", "Pregunto y no invento", "La comunidad puede explicarla."),
    ],
    open_task=task(
        "Pide a un adulto que lea este relato inventado: «Primero, Lía subió al cerro con su mamá. Después vieron un zorro que cruzaba el camino. Más tarde, descansaron bajo una roca. Al final, bajaron y cenaron sopa». Escribe los cuatro hechos en orden con las palabras primero, después, más tarde y al final. Agrega qué te pareció lo más importante.",
        "Primero subieron al cerro. Después vieron un zorro. Más tarde descansaron bajo una roca. Al final bajaron y cenaron sopa. Lo más importante fue ver el zorro.",
        ["escribe los cuatro hechos", "usa primero, después, más tarde y al final", "dice qué le pareció importante"],
        ["cuatro frases ordenadas"],
        ["alterar el orden", "agregar hechos que no están"],
        "Reconoce el orden correcto y pregunta qué dato lo hizo importante. Aclara que el relato es inventado.",
    ),
    reinforce="Cuenta a un adulto lo que hiciste hoy usando primero, después y al final.",
    extend="Busca en tu casa una expresión que no se entiende literal, como «llueve a cántaros», y pregunta qué quiere decir.",
)

register(
    LF01, 3,
    materials="Este cuaderno, lápiz y regla.",
    use="Aprenderé a usar con cuidado una palabra de una lengua indígena: respetando cómo se dice, cómo se escribe y cuándo se usa. Sirve para no cambiar ni inventar palabras.",
    prior=["Sé que la lengua la enseña la comunidad.", "Sé contar letras de una palabra."],
    explain=[
        "Cuando usas una palabra de una lengua indígena, cuida tres cosas: la pronunciación, que es cómo se dice; la grafía, que es cómo se escribe; y el contexto, que es cuándo y con quién se usa. Cada lengua tiene sus propios sonidos y letras. Por eso no se cambia una letra para que se parezca al castellano.",
        "Un ejemplo muy conocido en mapuzugun es el saludo «mari mari». Se usa para saludar. Escríbelo igual que lo ve el educador o educadora tradicional y di cómo se pronuncia según su voz. Existen distintas formas de escribir algunas lenguas indígenas y la comunidad decide cuál usar.",
        "Para usar bien una palabra: escúchala de la fuente, repítela después de que la persona te lo pida, y úsala en la situación que ella indique. Si no estás seguro, no la uses. Más vale preguntar que decir algo que cambie el sentido.",
    ],
    vocab=[("pronunciación", "cómo se dice una palabra"), ("grafía", "cómo se escribe una palabra"), ("saludo", "palabra o gesto para recibir a alguien"), ("pertinente", "adecuado para la situación"), ("variante", "otra forma de decir o escribir la misma cosa")],
    worked=[
        {"title": "Contar letras", "problem": "El saludo «mari mari» tiene dos palabras. ¿Cuántas letras tiene en total, sin contar el espacio?", "steps": ["«mari» tiene 4 letras: m, a, r, i.", "La segunda «mari» también tiene 4.", "4 + 4 = 8."], "answer": "8 letras"},
        {"title": "Cuándo usarlo", "problem": "Llega la educadora tradicional a tu curso y ella saluda con «mari mari». ¿Cuándo es pertinente que lo repitas?", "steps": ["Ella saluda en el momento de recibir.", "Si ella te invita a repetirlo, lo repito.", "Lo escribo igual y lo digo con respeto."], "answer": "Cuando ella te invita a repetir el saludo"},
    ],
    mistakes=[
        {"wrong": "Escribir la palabra como suena en castellano, cambiando letras.", "why": "Cada lengua tiene sus propias letras y sonidos.", "fix": "Copia la palabra tal como te la muestra el educador o educadora tradicional."},
        {"wrong": "Usar el saludo en tono de burla.", "why": "Es una palabra de una lengua viva y se usa con respeto.", "fix": "Úsalo en una situación de saludo real."},
    ],
    tiers={
        "recovery": [
            ex("«Mari mari» es un saludo en mapuzugun. ¿Para qué sirve?", "Para saludar", "Es un saludo."),
            ex("La grafía es cómo se escribe una palabra. El educador escribió «mari mari». ¿Cuál copias: «mari mari» o «mary mary»?", "mari mari", "Se copia tal como lo escribe quien enseña."),
            ex("¿La pronunciación se refiere a cómo se dice o a cómo se escribe una palabra?", "Cómo se dice", "Pronunciación es el sonido."),
        ],
        "understand": [
            ex("Si la educadora no te invita a repetir un saludo, ¿lo repites igual?", "No, espero la invitación", "Se usa cuando corresponde."),
            ex("¿Por qué no se cambia una letra de una palabra indígena para que sea más fácil?", "Porque cada lengua tiene sus propias letras y sonidos", "Cambiarla altera la palabra."),
            ex("¿Es respetuoso usar «mari mari» para burlarte de alguien?", "No", "Es una palabra de una lengua viva."),
        ],
        "apply": [
            arith("«mari mari» tiene 4 letras en cada palabra. ¿Cuántas letras hay en las dos palabras juntas?", "4+4", "Se suman las letras de cada palabra."),
            ex("Copia la palabra exactamente como está: «mari». ¿Cuántas vocales tiene?", "2", "Las vocales de «mari» son la a y la i: dos."),
            ex("La educadora saluda a tu curso con «mari mari». Elige la mejor respuesta: a) repetir en voz baja cuando te invita, b) reírte. Escribe la letra.", "a", "Es respetuoso y espera la invitación."),
        ],
        "reason": [
            ex("Un niño escribió «mari mari» como «mary mary» porque se parece al inglés. ¿Qué error tiene?", "Cambió la grafía", "Cada lengua tiene sus propias letras."),
            ex("Dos personas escriben una palabra de manera distinta y las dos son de la comunidad. ¿Cómo lo explicas?", "Porque existen variantes", "Una lengua puede escribirse de más de una forma."),
        ],
        "challenge": [
            ex("Debían copiar «mari mari». Alicia copió «mari mari». Beto copió «marimari». Camila copió «mari mari». ¿Quiénes copiaron bien?", "Alicia y Camila", "Beto juntó las palabras."),
            ex("Un compañero quiere usar «mari mari» en un chiste. ¿Qué tres cosas cuidas: pronunciación, grafía y contexto o solo la pronunciación?", "Pronunciación, grafía y contexto", "Los tres aspectos importan."),
        ],
    },
    context=[ex("Un día llega una visita de la comunidad y no sabes cómo saludar. ¿Qué haces: inventar un saludo o pedir que te enseñen?", "Pedir que me enseñen", "Solo la comunidad enseña bien su lengua.")],
    selfcheck=[
        ex("¿Qué es la grafía?", "Cómo se escribe una palabra", "Es la forma escrita."),
        ex("¿Qué es la pronunciación?", "Cómo se dice una palabra", "Es el sonido."),
        ex("¿Qué haces si no estás seguro de usar una palabra?", "No la uso y pregunto", "Más vale preguntar."),
    ],
    open_task=task(
        "Copia en tu cuaderno la palabra «mari mari» exactamente como está escrita aquí. Cuenta cuántas letras tiene cada palabra y cuántas en total. Escribe dos situaciones inventadas: una donde es pertinente saludar con «mari mari» y otra donde no lo sería. Cuando venga el educador/a tradicional, pregúntale cómo se pronuncia y cuándo se usa.",
        "Copié «mari mari». Cada palabra tiene 4 letras y juntas 8. Pertinente: cuando el educador saluda y me invita a repetir. No pertinente: para bromear en el recreo. Le preguntaré cómo se pronuncia.",
        ["copia sin cambiar letras", "cuenta 4 y 4 y 8", "escribe dos situaciones", "agrega una pregunta al educador"],
        ["palabra copiada", "dos situaciones"],
        ["cambiar la grafía", "usar el saludo para burlarse"],
        "Reconoce que copió con cuidado y pide que escriba la pregunta para el educador. Recuerda que la pronunciación la enseña la fuente.",
    ),
    reinforce="Copia «mari mari» tres veces con mucho cuidado y revisa que sean idénticas.",
    extend="Pregunta a un adulto cómo saludaba su abuela y anota el saludo tal como te lo dice.",
)

register(
    LF01, 4,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé a contar lo que comprendí de un relato diciendo de dónde viene y qué parte no sé. Sirve para compartir sin inventar y cuidar la palabra de quien relató.",
    prior=["Sé ordenar los hechos de un relato.", "Sé que la fuente tiene permiso."],
    explain=[
        "Comunicar es contar a otros lo que comprendiste. Cuando cuentas un relato que escuchaste, di de dónde viene. Puedes decir: «Esto lo contó la señora X, con su permiso». Esa frase se llama citar la fuente. Además, puedes decir qué parte no entendiste: eso se llama decir los límites.",
        "Los límites son importantes. Si cuentas solo lo que escuchaste, nadie se confunde. Si agregas cosas que no oíste, el relato cambia y la fuente queda mal. Por eso no inventes finales ni cambies personajes.",
        "También se puede devolver. Devolver es compartir lo que hiciste con la persona que relató: puedes leerle tu resumen y preguntar si lo contaste bien. Así la comunidad cuida su relato y tú aprendes con respeto.",
    ],
    vocab=[("comunicar", "contar a otros lo que comprendiste"), ("citar la fuente", "decir quién enseñó o contó"), ("límite", "lo que no sé o no puedo decir"), ("devolver", "compartir con quien enseñó lo que hiciste"), ("resumen", "texto breve con lo más importante")],
    worked=[
        {"title": "Citar la fuente", "problem": f"Escuchaste «{RELATO}» contado por Don Mateo, personaje inventado, con su permiso. Cuéntalo en una frase citando la fuente.", "steps": ["Digo quién lo contó: Don Mateo.", "Digo que tuve su permiso.", "Resumo lo más importante."], "answer": "Don Mateo contó, con su permiso, que Alba fue al río con su abuelo y volvieron a casa"},
        {"title": "Decir los límites", "problem": "No entendiste cómo termina un relato porque hablaban muy rápido. ¿Cómo lo dices al compartirlo?", "steps": ["No invento el final.", "Digo: «No entendí el final».", "Pregunto a la persona que relató."], "answer": "Digo que no entendí el final y le pregunto a quien relató"},
    ],
    mistakes=[
        {"wrong": "Contar un relato sin decir quién lo contó.", "why": "La fuente merece reconocimiento y el relato tiene dueños.", "fix": "Empieza diciendo quién lo contó y que tuviste permiso."},
        {"wrong": "Inventar el final cuando no lo recuerdas.", "why": "Cambias el relato y la fuente queda mal representada.", "fix": "Di «no recuerdo el final» y pregunta."},
    ],
    tiers={
        "recovery": [
            ex("Citar la fuente es decir quién enseñó o contó. Si Doña Elena contó un relato, ¿a quién citas?", "A Doña Elena", "Ella es la fuente."),
            ex("Los límites son lo que no sé. Si olvidaste el final, ¿lo inventas o dices que no lo recuerdas?", "Digo que no lo recuerdo", "No se inventa."),
            ex("Devolver es compartir con quien relató lo que hiciste. ¿A quién le muestras tu resumen: a quien relató o a nadie?", "A quien relató", "Así comprueba que lo contaste bien."),
        ],
        "understand": [
            ex("«Esto lo contó la señora Rosa, con su permiso». ¿Qué dos cosas dice esta frase?", "Quién contó y que hubo permiso", "Cita la fuente y el permiso."),
            ex("¿Por qué no se debe inventar un final?", "Porque cambia el relato", "El relato debe quedar como se escuchó."),
            ex("¿Para qué sirve decir qué parte no entendí?", "Para no confundir a otros", "Nadie cree que lo supe todo."),
        ],
        "apply": [
            ex("Resume en una frase: «Una tarde la niña fue al río. Primero vio una garza. Al final volvió a casa». Elige la mejor frase: a) «La niña vio una garza en el río y volvió a casa», b) «La niña no fue al río». Letra:", "a", "Resume lo más importante sin cambiar nada."),
            ex("Elige la frase que cita bien: a) «Mi vecina Rosa, con su permiso, me contó este relato», b) «Este relato lo inventé yo». Letra:", "a", "Dice quién lo contó y el permiso."),
            arith("Un curso comparte 3 relatos por semana durante 4 semanas. ¿Cuántos relatos comparten en total?", "3*4", "Se suman 3 relatos cuatro veces."),
        ],
        "reason": [
            ex("Luis contó un relato como si fuera suyo. ¿Qué dos cosas no hizo?", "Citar la fuente y pedir permiso", "No dijo quién lo contó ni preguntó."),
            ex("Una niña leyó su resumen a la abuela que relató y la abuela corrigió un nombre. ¿Qué hizo bien la niña?", "Devolver su resumen para revisarlo", "Así corrigió un error con quien conoce el relato."),
        ],
        "challenge": [
            ex("Lee: «Hoy Doña Elena nos contó un relato corto. Nos dio permiso para repetirlo en clases. No entendí una palabra del final». Escribe dos datos de la fuente y un límite.", "Fuente: Doña Elena; permiso: sí; límite: no entendí una palabra del final", "Cita a la fuente, el permiso y lo que no entendió."),
            ex("Dos amigos cuentan el mismo relato. Marta dice: «Don Luis lo contó y yo no entendí el final». Beto dice: «Lo inventé». ¿Quién comunicó con respeto?", "Marta", "Marta cita la fuente y dice su límite."),
        ],
    },
    context=[ex("Quieres contar en la feria escolar el relato que oíste. ¿Qué es lo primero que dices?", "Quién lo contó y que tuve su permiso", "Se reconoce a la fuente.")],
    selfcheck=[
        ex("¿Qué es citar la fuente?", "Decir quién enseñó o contó", "Reconoce a quien enseñó."),
        ex("En Lengua y Cultura: ¿Qué es un límite?", "Lo que no sé", "Es lo que no entendí o no recuerdo."),
        ex("¿Qué haces si no recuerdas el final?", "Digo que no lo recuerdo", "No se inventa."),
    ],
    open_task=task(
        "Lee este relato inventado: «Una noche, el niño Rafa miró las estrellas desde el patio con su mamá. Ella le dijo que se ven mejor cuando se apagan las luces. Después fueron a dormir». Escribe un resumen de dos frases. Empieza con: «Este relato lo inventé para practicar, no pertenece a ningún pueblo». Agrega una pregunta que harías a un educador tradicional sobre cómo cuida su comunidad sus relatos.",
        "Este relato lo inventé para practicar, no pertenece a ningún pueblo. Rafa miró las estrellas con su mamá y ella le dijo que se ven mejor sin luces. Después fueron a dormir. Pregunta: ¿Cómo cuida su comunidad sus relatos?",
        ["empieza con la frase indicada", "resume en dos frases", "no agrega hechos nuevos", "escribe una pregunta al educador"],
        ["resumen de dos frases", "pregunta"],
        ["inventar un final", "atribuir el relato a un pueblo"],
        "Reconoce el resumen con límites claros y que no atribuyó el relato a ningún pueblo.",
    ),
    reinforce="Cuenta a alguien de tu casa un cuento que escuchaste hoy diciendo quién te lo contó.",
    extend="Escribe una frase para agradecer a quien te contó un relato.",
)

# ================================================================ LF02
register(
    LF02, 1,
    materials="Este cuaderno y lápiz. Las descripciones están escritas aquí en castellano. Las palabras de mapuzugun son muy conocidas, pero el educador/a tradicional confirma su escritura y su pronunciación.",
    use="Aprenderé a escuchar cómo se describe un lugar de la naturaleza y a reconocer quién lo describe y desde dónde. Sirve para prestar atención a las palabras que una comunidad usa para su territorio.",
    prior=["Sé nombrar elementos de la naturaleza.", "Sé que la fuente enseña."],
    explain=[
        "El medio natural es el lugar con sus ríos, cerros, plantas, animales y cielo. Describir es decir cómo es algo: su color, su tamaño, dónde está y qué hace. Las personas de una comunidad describen su territorio con las palabras de su lengua y con los nombres que le dieron.",
        "En mapuzugun hay palabras muy conocidas para elementos de la naturaleza. «Mapu» quiere decir tierra, «ko» quiere decir agua, «antü» quiere decir sol y «kuyen» quiere decir luna. Estas palabras se escriben de distintas maneras según la grafía; el educador o educadora tradicional te dice cuál usa su comunidad y cómo se pronuncian.",
        "Para escuchar una descripción, fíjate en tres cosas: quién describe, qué lugar describe y para qué lo hace. No cambies los nombres de los lugares. Si no los entiendes, pregunta.",
    ],
    vocab=[("medio natural", "lugar con ríos, cerros, plantas, animales y cielo"), ("describir", "decir cómo es algo"), ("mapu", "tierra, en mapuzugun"), ("ko", "agua, en mapuzugun"), ("antü", "sol, en mapuzugun")],
    worked=[
        {"title": "Quién, qué lugar y para qué", "problem": f"Una educadora tradicional dice a los niños: «{DESC}». Lo describe para enseñarles a reconocer el lugar de la excursión. ¿Quién, qué lugar y para qué?", "steps": ["Quien describe es la educadora tradicional.", "El lugar tiene un río, un cerro verde, un cóndor y juncos.", "Lo hace para enseñar a reconocer el lugar de la excursión."], "answer": "Describe la educadora; el lugar es un río junto a un cerro; para reconocer el lugar de la excursión"},
        {"title": "Palabras conocidas", "problem": "Escuchas «ko» y «antü» en un relato. Según la lista del cuaderno, ¿qué dos elementos nombran?", "steps": ["«Ko» quiere decir agua.", "«Antü» quiere decir sol.", "Confirmo la escritura y la pronunciación con el educador."], "answer": "Agua y sol"},
    ],
    mistakes=[
        {"wrong": "Cambiar el nombre de un lugar por otro más fácil.", "why": "El nombre es de la comunidad y tiene sentido para ella.", "fix": "Usa el nombre que dice quien enseña."},
        {"wrong": "Pensar que las palabras de la lista valen para todas las lenguas indígenas.", "why": "Cada lengua tiene sus propias palabras.", "fix": "Di que son palabras en mapuzugun."},
    ],
    tiers={
        "recovery": [
            ex("Describir es decir cómo es algo. Si dices «el río es ancho y frío», ¿estás describiendo?", "Sí", "Dices cómo es el río."),
            ex("«Mapu» en mapuzugun quiere decir tierra. ¿Qué quiere decir «mapu»?", "Tierra", "Así lo dice la lista."),
            ex("«Ko» en mapuzugun quiere decir agua. ¿Qué quiere decir «ko»?", "Agua", "Así lo dice la lista."),
        ],
        "understand": [
            ex("«Antü» es sol y «kuyen» es luna. ¿Cuál de las dos palabras nombra el astro que suele verse de noche?", "Kuyen", "La luna es la que suele verse de noche."),
            ex("¿Por qué el educador debe confirmar la escritura de las palabras?", "Porque se escriben de distintas maneras según la grafía", "La comunidad dice qué forma usa."),
            ex("¿Qué es el medio natural?", "El lugar con ríos, cerros, plantas, animales y cielo", "Es el entorno de la naturaleza."),
        ],
        "apply": [
            ex(f"En «{DESC}», ¿qué animal vuela sobre el cerro?", "Un cóndor", "El texto dice que sobre el cerro vuela un cóndor grande."),
            ex("Empareja con la lista: mapu, ko, antü, kuyen. ¿Cuál de las cuatro palabras nombra el agua?", "Ko", "Ko es agua."),
            ex("En una descripción se nombran un río, un cerro, un cóndor y juncos. ¿Cuántos elementos de la naturaleza son?", "4", "Se cuentan cuatro."),
        ],
        "reason": [
            ex("Un niño dice que «ko» es sol. ¿Qué dato debe revisar?", "La lista del cuaderno o preguntar al educador", "Ko es agua, no sol."),
            ex("Un compañero cambió el nombre de un cerro por uno inventado. ¿Qué le dices?", "Que use el nombre que dice quien enseña", "El nombre pertenece a la comunidad."),
        ],
        "challenge": [
            ex("Una descripción dice: «El río es ancho. El cerro es verde. El cóndor es grande». ¿Qué datos se usan: tamaño y color, o solo el lugar?", "Tamaño y color", "Ancho y grande son tamaño; verde es color."),
            ex("Tres fichas: A) «Describe un guía. Lugar: un río». B) «Describe una educadora tradicional. Lugar: un cerro. Para enseñar». C) «Describe un desconocido sin nombre». ¿Cuál es la fuente más clara?", "La B", "Dice quién describe, el lugar y el propósito."),
        ],
    },
    context=[ex("En una excursión una guía local nombra un cerro con un nombre que no conoces. ¿Qué haces?", "Le pregunto cómo se llama y lo anoto", "El nombre lo dice la comunidad.")],
    selfcheck=[
        ex("¿Qué quiere decir «mapu»?", "Tierra", "Es una palabra en mapuzugun."),
        ex("¿Qué quiere decir «antü»?", "Sol", "Es una palabra en mapuzugun."),
        ex("¿Quién confirma la escritura y la pronunciación?", "El educador o educadora tradicional", "La comunidad es la fuente."),
    ],
    open_task=task(
        "Pide a un adulto que lea esta descripción inventada: «La quebrada es angosta y tiene piedras grises. El agua corre despacio. En la orilla hay un sauce verde». Escucha y escribe: 1) quién describe, 2) qué lugar describe y 3) tres elementos de la naturaleza que nombra. Agrega una pregunta para el educador tradicional sobre cómo se dice «agua» en la lengua de su pueblo.",
        "1) Describe el adulto. 2) Una quebrada. 3) Piedras, agua y sauce. Pregunta: ¿cómo se dice «agua» en su lengua y cómo se escribe?",
        ["dice quién describe", "dice el lugar", "nombra tres elementos", "escribe una pregunta al educador"],
        ["tres respuestas escritas", "pregunta"],
        ["inventar la palabra en lengua indígena", "nombrar elementos que no están"],
        "Reconoce la escucha atenta. Recuerda que la palabra en la lengua del pueblo la enseña el educador tradicional.",
    ),
    reinforce="Mira desde tu ventana y di en voz alta tres cosas de la naturaleza que ves.",
    extend="Escribe una oración que describa un árbol de tu barrio con su color y tamaño.",
)

register(
    LF02, 2,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé a sacar la información de una descripción de la naturaleza: qué elementos hay, cómo son y dónde están. Sirve para comprender un mensaje sobre el territorio sin traducir palabra por palabra.",
    prior=["Sé que describir es decir cómo es algo.", "Sé qué es una fuente."],
    explain=[
        "Una descripción del medio natural dice qué hay, cómo es y dónde está. Por ejemplo: «Hay un río ancho junto a un cerro verde». Aquí hay dos elementos: un río y un cerro. Del río dice que es ancho. Del cerro dice que es verde. Y dice dónde: el río está junto al cerro.",
        "Muchas veces una descripción lleva un mensaje. El mensaje es la idea que quiere dejar la persona que habla. Por ejemplo: «El río está crecido hoy, no te acerques solo». El mensaje es: ten cuidado. Para hallar el mensaje pregunta: ¿qué quiere que sepa o haga esta persona? Algunas comunidades también leen mensajes en la naturaleza, como señales del tiempo. Cuáles son y qué significan lo enseña cada comunidad: no los adivines.",
        "Si la descripción está en una lengua indígena, la comunidad o el educador tradicional ayuda a entender el mensaje y el sentido. No traduzcas solo palabra por palabra. Cuenta con tus palabras lo que comprendiste y confirma con la persona.",
    ],
    vocab=[("elemento", "cada cosa que se nombra"), ("mensaje", "idea que alguien quiere dejar"), ("lugar", "dónde está algo"), ("oralidad", "decir las cosas con la voz"), ("territorio", "lugar donde vive o vivió un pueblo")],
    worked=[
        {"title": "Elementos, cómo son y dónde están", "problem": f"En «{DESC}», anota los elementos, cómo son y dónde están.", "steps": ["Elementos: río, cerro, cóndor, juncos.", "Cómo son: río ancho, cerro verde, agua fría y clara, cóndor grande, juncos altos.", "Dónde: el río junto al cerro, el cóndor sobre el cerro y los juncos cerca de la orilla."], "answer": "4 elementos con sus características y su lugar"},
        {"title": "Hallar el mensaje", "problem": "Una guía dice: «El cerro tiene el suelo suelto después de la lluvia. Pisa con cuidado». ¿Cuál es el mensaje?", "steps": ["Describe: el suelo está suelto.", "Pide: pisar con cuidado.", "El mensaje es tener cuidado al caminar."], "answer": "Tener cuidado al caminar por el cerro"},
    ],
    mistakes=[
        {"wrong": "Nombrar un elemento pero olvidar dónde está.", "why": "El lugar completa la descripción.", "fix": "Después de cada elemento pregunta: ¿cómo es y dónde está?"},
        {"wrong": "Quedarse en las palabras y no buscar el mensaje.", "why": "Las descripciones muchas veces quieren decir algo más.", "fix": "Pregunta qué quiere que sepa o haga quien habla."},
    ],
    tiers={
        "recovery": [
            ex(f"En «{DESC}», ¿cómo es el agua?", "Fría y clara", "El texto lo dice."),
            ex("En «Hay un río ancho junto a un cerro verde», ¿cuántos elementos se nombran?", "2", "Se nombran el río y el cerro."),
            ex("El mensaje es la idea que alguien quiere dejar. Si te dicen «no te acerques solo al río crecido», ¿qué te piden?", "Tener cuidado", "Esa frase pide cuidado."),
        ],
        "understand": [
            ex("«El cóndor vuela sobre el cerro». ¿Dónde está el cóndor?", "Sobre el cerro", "Lo dice la frase."),
            ex("En «Crecen juncos altos cerca de la orilla», ¿cómo son los juncos?", "Altos", "El texto lo dice."),
            ex("«El camino está resbaloso, camina despacio». ¿Cuál es el mensaje?", "Caminar despacio por el camino resbaloso", "La frase pide cuidado."),
        ],
        "apply": [
            ex("Lee: «La playa es larga. La arena es dorada. Hay gaviotas blancas». ¿Cuántos elementos hay: playa, arena y gaviotas?", "3", "Se nombran la playa, la arena y las gaviotas."),
            ex("Con la descripción anterior, ¿de qué color es la arena?", "Dorada", "El texto lo dice."),
            arith("En un cerro viven 2 cóndores y llegan 3 más. ¿Cuántos cóndores hay en total?", "2+3", "Se suman los cóndores."),
        ],
        "reason": [
            ex("Una niña tradujo cada palabra de una descripción y no entendió el mensaje. ¿Qué debió hacer?", "Pedir ayuda a la comunidad y contar con sus palabras", "La comunidad ayuda a entender el sentido."),
            ex("Un niño dice que el río estaba «contento». ¿Es un dato de la descripción o una interpretación suya?", "Una interpretación suya", "La descripción no lo dice."),
        ],
        "challenge": [
            ex("Lee: «La laguna es redonda y azul. Alrededor hay cerros de piedra. Un zorro bebe agua. Hoy sopla viento fuerte». ¿Qué dos datos son de la laguna?", "Es redonda y azul", "Se dicen de la laguna."),
            ex("Dos amigos oyen la descripción de la laguna. Teo dice «hay cerros de piedra». Sol dice «hay un volcán». ¿Quién dice algo que está en el texto?", "Teo", "El volcán no se nombra."),
        ],
    },
    context=[ex("Una guía te dice: «El sol está fuerte, usen sombrero». ¿Cuál es el mensaje?", "Protegerse del sol", "Pide cuidarse del sol.")],
    selfcheck=[
        ex("¿Qué tres cosas dice una descripción?", "Qué hay, cómo es y dónde está", "Eso completa la descripción."),
        ex("¿Qué es un mensaje?", "La idea que alguien quiere dejar", "Es lo que quiere comunicar."),
        ex("¿Se traduce siempre palabra por palabra?", "No", "El sentido puede cambiar."),
    ],
    open_task=task(
        "Lee esta descripción inventada: «El volcán de la foto es alto y tiene nieve arriba. Al pie hay un bosque oscuro. Por el bosque pasa un arroyo pequeño». Escribe una tabla de tres columnas con los tres elementos: qué hay, cómo es y dónde está. Después escribe un mensaje que le darías a un compañero que irá de excursión.",
        "Volcán: alto, con nieve arriba. Bosque: oscuro, al pie del volcán. Arroyo: pequeño, por el bosque. Mensaje: abrígate porque arriba hace frío.",
        ["nombra tres elementos", "escribe cómo es cada uno", "escribe dónde está cada uno", "escribe un mensaje"],
        ["tabla de tres filas", "mensaje"],
        ["agregar elementos que no están", "olvidar dónde está cada elemento"],
        "Reconoce la tabla completa y pregunta cómo eligió el mensaje. La descripción es inventada.",
    ),
    reinforce="Describe en tres frases algo que ves por la ventana: qué es, cómo es y dónde está.",
    extend="Inventa una descripción de una playa o un cerro de cuatro frases y pide a alguien que busque los elementos.",
)

register(
    LF02, 3,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé a describir un lugar de mi entorno con frases ordenadas y a usar con cuidado las palabras de una lengua indígena. Sirve para hablar del lugar donde vivo con respeto.",
    prior=["Sé qué hay, cómo es y dónde está.", "Sé que ko, mapu, antü y kuyen son palabras de mapuzugun."],
    explain=[
        "Para describir un lugar puedes usar tres frases modelo: «Veo...», «Es...» y «Está...». Por ejemplo: «Veo un árbol. Es alto y verde. Está junto al patio». Así tu descripción tiene qué hay, cómo es y dónde está. Usa palabras que tú conozcas bien.",
        "Si quieres usar una palabra de una lengua indígena, como «ko» para agua, hazlo solo si el educador o educadora tradicional te lo permite y te confirma cómo escribirla y decirla. No mezcles palabras para que suene «más indígena»: eso no es respetuoso. Puedes decir la frase en castellano y escribir la palabra confirmada al lado.",
        "Cuando termines tu descripción, léela y revisa: ¿dice qué hay? ¿dice cómo es? ¿dice dónde está? Si falta algo, agrégalo. También revisa que no hayas cambiado el nombre de ningún lugar.",
    ],
    vocab=[("describir", "decir cómo es algo"), ("frase modelo", "inicio de frase que ayuda a ordenar lo que dices"), ("mezclar", "poner palabras de una lengua en otra sin cuidado"), ("revisar", "leer de nuevo para corregir"), ("confirmar", "comprobar con la persona que sabe")],
    worked=[
        {"title": "Describir con las tres frases", "problem": "Describe un árbol de tu patio con «Veo...», «Es...» y «Está...». El árbol es alto, verde y está junto al muro.", "steps": ["Veo un árbol.", "Es alto y verde.", "Está junto al muro."], "answer": "Veo un árbol. Es alto y verde. Está junto al muro."},
        {"title": "Usar una palabra con cuidado", "problem": "Quieres escribir en un cartel la palabra «ko» al lado de «agua». ¿Qué debes hacer antes?", "steps": ["Pregunto al educador si puedo usar la palabra.", "Confirmo cómo se escribe y se dice.", "Si dice que sí, la uso con su guía; si no, uso castellano."], "answer": "Preguntar y confirmar con el educador tradicional antes de usarla"},
    ],
    mistakes=[
        {"wrong": "Mezclar palabras indígenas al azar para que suene más interesante.", "why": "Es poco respetuoso y puede cambiar el sentido.", "fix": "Usa castellano y escribe una palabra confirmada solo con permiso."},
        {"wrong": "Describir sin decir dónde está.", "why": "El lugar completa la descripción.", "fix": "Usa «Está...» para decir dónde."},
    ],
    tiers={
        "recovery": [
            ex("Las tres frases modelo son «Veo...», «Es...» y «Está...». ¿Con cuál dices cómo es algo?", "Es...", "«Es» dice cómo es."),
            ex("¿Con cuál frase modelo dices dónde está algo: «Veo...», «Es...» o «Está...»?", "Está...", "«Está» dice el lugar."),
            ex("Antes de usar la palabra «ko», ¿qué debes hacer?", "Preguntar al educador", "Él confirma el uso."),
        ],
        "understand": [
            ex("Completa: «Veo una piedra. Es gris. ___ junto al río». ¿Con qué palabra completas para decir el lugar?", "Está", "«Está junto al río» dice dónde."),
            ex("¿Por qué no se mezclan palabras indígenas al azar?", "Porque es poco respetuoso y cambia el sentido", "Cada palabra tiene su sentido."),
            ex("Una descripción dice «Veo un cerro. Es verde». ¿Qué le falta?", "Dónde está", "Falta el lugar."),
        ],
        "apply": [
            ex("Ordena para formar una frase: «junto / está / río / el / árbol / al». ¿Cuál es una frase correcta?", "El árbol está junto al río", "Ordena las palabras con sentido."),
            ex("Describe con «Veo..., Es..., Está...» este dato: una vaca, blanca, en el potrero. Escribe las tres frases.", "Veo una vaca. Es blanca. Está en el potrero.", "Dice qué hay, cómo es y dónde está."),
            arith("En tu descripción escribiste 3 frases por cada lugar y describiste 4 lugares. ¿Cuántas frases son?", "3*4", "Se suman 3 frases cuatro veces."),
        ],
        "reason": [
            ex("Una niña escribió «Veo ko en la casa» sin preguntar a nadie. ¿Qué error tiene?", "No confirmó con el educador y mezcló la palabra", "Debe consultar antes de usarla."),
            ex("Para saber si falta algo en tu descripción, ¿qué haces al final?", "Leerla y revisar qué hay, cómo es y dónde está", "Revisar completa la descripción."),
        ],
        "challenge": [
            ex("Una descripción dice: «Veo un puente. Está sobre el río. Es de madera». Ordénala con Veo, Es y Está. ¿Cuál es el orden correcto?", "Veo un puente. Es de madera. Está sobre el río.", "Sigue el orden Veo, Es, Está."),
            ex("Beto escribió «Veo mapu y antü». No consultó al educador. Si luego el educador lo confirma, ¿qué quiere decir su frase?", "Veo tierra y sol", "Mapu es tierra y antü es sol."),
        ],
    },
    context=[ex("Tu curso quiere escribir un cartel con las palabras «agua» y «ko». ¿Qué paso falta antes de colgarlo?", "Confirmar la escritura con el educador", "La grafía la confirma la comunidad.")],
    selfcheck=[
        ex("¿Qué frase modelo dice dónde está algo?", "Está...", "Es la que indica el lugar."),
        ex("¿Qué haces antes de usar una palabra indígena?", "Preguntar y confirmar", "Se confirma con el educador."),
        ex("¿Qué revisas al terminar?", "Qué hay, cómo es y dónde está", "Es lo que completa la descripción."),
    ],
    open_task=task(
        "Mira tu patio, tu ventana o tu calle. Escribe tres frases: «Veo...», «Es...» y «Está...» sobre un elemento de la naturaleza que ves (un árbol, una planta, el cielo, una piedra). Después revisa si dice qué hay, cómo es y dónde está. Agrega una pregunta al educador sobre cómo se dice ese elemento en la lengua de su pueblo, sin escribir una palabra que no hayas confirmado.",
        "Veo un árbol. Es alto y verde. Está junto al patio. Revisé: hay, cómo es y dónde está. Pregunta: ¿cómo se dice «árbol» en su lengua y cómo se escribe?",
        ["escribe tres frases", "dice qué hay, cómo es y dónde está", "agrega una pregunta", "no escribe palabras indígenas sin confirmar"],
        ["tres frases", "pregunta"],
        ["mezclar palabras al azar", "omitir el lugar"],
        "Reconoce la descripción ordenada y la pregunta honesta. Refuerza que la palabra en lengua indígena la confirma quien enseña.",
    ),
    reinforce="Describe un objeto de tu pieza con las tres frases: Veo, Es, Está.",
    extend="Describe dos lugares de tu barrio con seis frases y revisa que cada una tenga dónde está.",
)

register(
    LF02, 4,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé a compartir una descripción del medio natural diciendo de dónde viene y qué no sé. Sirve para devolver lo aprendido con respeto a quien lo enseñó.",
    prior=["Sé describir con Veo, Es y Está.", "Sé citar la fuente."],
    explain=[
        "Cuando compartes una descripción que aprendiste de una comunidad, di quién te la enseñó y que tuviste permiso. Por ejemplo: «Esto me lo explicó Don Mateo, con su permiso». Así reconoces la fuente. Si usaste una palabra en mapuzugun, dilo: «La palabra la confirmó el educador».",
        "También di lo que no sabes. Si no recuerdas un nombre o no entendiste un mensaje, dilo con honestidad. Eso se llama decir los límites. Nadie espera que lo sepas todo. Lo importante es no inventar.",
        "Después de compartir, puedes devolver. Devolver es mostrar a quien te enseñó lo que hiciste, por ejemplo un cartel o un dibujo, y preguntarle si lo hiciste bien. Si te corrige, agradece y cambia lo que haga falta.",
    ],
    vocab=[("compartir", "contar a otros lo que aprendiste"), ("fuente", "persona que enseñó"), ("límite", "lo que no sé"), ("devolver", "mostrar a quien enseñó lo que hiciste"), ("corregir", "cambiar para que quede bien")],
    worked=[
        {"title": "Frase para compartir", "problem": "Don Mateo, personaje inventado, te explicó cómo es un cerro de su zona. Escribe una frase para compartirlo con tu curso.", "steps": ["Digo quién me lo explicó.", "Digo que tuve su permiso.", "Digo lo que entendí."], "answer": "Esto me lo explicó Don Mateo, con su permiso: el cerro es alto y verde"},
        {"title": "Decir los límites", "problem": "No recuerdas el nombre de un río. ¿Qué dices?", "steps": ["No lo invento.", "Digo que no lo recuerdo.", "Pregunto de nuevo a quien lo dijo."], "answer": "Digo que no recuerdo el nombre y lo pregunto"},
    ],
    mistakes=[
        {"wrong": "Compartir sin decir quién enseñó.", "why": "La fuente merece reconocimiento.", "fix": "Empieza diciendo quién te lo enseñó."},
        {"wrong": "Cambiar lo que dijo la persona para que suene mejor.", "why": "La descripción es de la comunidad.", "fix": "Cuenta lo que entendiste sin agregar."},
    ],
    tiers={
        "recovery": [
            ex("Al compartir lo que te explicó una persona, ¿qué dato dices primero: quién te lo explicó o el color del cielo?", "Quién me lo explicó", "Es el reconocimiento de la fuente."),
            ex("Devolver es mostrar a quien te enseñó lo que hiciste. ¿A quién le muestras tu cartel?", "A quien me enseñó", "Para ver si lo hice bien."),
            ex("Si no recuerdas un nombre, ¿lo inventas o dices que no lo recuerdas?", "Digo que no lo recuerdo", "No se inventa."),
        ],
        "understand": [
            ex("«La palabra la confirmó el educador». ¿Qué cuenta esta frase sobre la palabra?", "Que alguien que sabe la revisó", "El educador la confirmó."),
            ex("¿Por qué conviene decir lo que no sabes?", "Para no confundir con datos inventados", "Es honesto y respetuoso."),
            ex("Una persona te corrige en tu cartel. ¿Qué haces: agradecer y cambiar, o discutir?", "Agradecer y cambiar", "Corregir ayuda a hacer bien el trabajo."),
        ],
        "apply": [
            ex("Elige la frase que cita bien: a) «Esto me lo explicó Doña Rosa, con su permiso», b) «Esto lo sé todo yo». Letra:", "a", "Dice la fuente y el permiso."),
            arith("Un curso hizo 5 carteles y cada uno tiene 3 datos con su fuente. ¿Cuántos datos con fuente hay?", "5*3", "Se suman 3 datos cinco veces."),
            ex("Doña Rosa explicó: «El río es angosto y frío». Escribe una frase para compartirla citando la fuente.", "Doña Rosa explicó, con su permiso, que el río es angosto y frío", "Cita la fuente, el permiso y el dato."),
        ],
        "reason": [
            ex("Marta dijo «el río tiene un nombre muy bonito» pero no dijo cuál ni quién se lo dijo. ¿Qué dato falta?", "El nombre y quién se lo dijo", "Falta la fuente."),
            ex("Beto agregó un detalle que la persona no había dicho para que fuera más bonita su descripción. ¿Qué error cometió?", "Agregó algo que no oyó", "Cambió la descripción."),
        ],
        "challenge": [
            ex("Lee: «Don Luis nos explicó cómo es la laguna: es redonda y azul. Nos dio permiso. No entendí el nombre del cerro». Escribe la fuente, el dato y el límite.", "Fuente: Don Luis; dato: la laguna es redonda y azul; límite: no entendí el nombre del cerro", "Separa quién, qué y lo que no sabe."),
            ex("Dos carteles: uno dice «Fuente: Doña Rosa, con permiso» y el otro no tiene fuente. ¿Cuál cuida mejor a la comunidad?", "El primero", "Reconoce a quien enseñó."),
        ],
    },
    context=[ex("Vas a exponer el cartel del medio natural. Una abuela de la comunidad te ayudó. ¿Cómo la nombras?", "La nombro como fuente y digo que tuve su permiso", "Se reconoce su ayuda.")],
    selfcheck=[
        ex("¿Qué es devolver?", "Mostrar a quien enseñó lo que hice", "Es compartir con ella el resultado."),
        ex("¿Qué dices si no sabes un dato?", "Que no lo sé", "No se inventa."),
        ex("¿Qué dices primero al compartir?", "Quién me lo enseñó", "Se reconoce la fuente."),
    ],
    open_task=task(
        "Con esta descripción inventada: «La caleta es pequeña. Los botes están en la arena. Hay gaviotas sobre las rocas». Prepara una presentación de tres frases: 1) Quién te la contó (usa el nombre inventado Doña Rosa), 2) La descripción en una frase y 3) Un límite (algo que no sabes). Practica en voz alta frente a un adulto.",
        "Esto me lo contó Doña Rosa, con su permiso. La caleta es pequeña, tiene botes en la arena y gaviotas sobre las rocas. No sé cómo se llama la caleta.",
        ["cita la fuente", "resume la descripción", "dice un límite", "habla en voz alta"],
        ["tres frases", "práctica oral con un adulto"],
        ["no citar la fuente", "inventar el nombre de la caleta"],
        "Reconoce que citó la fuente y dijo un límite. Doña Rosa es un personaje inventado: en la vida real cita a la persona que te enseña.",
    ),
    reinforce="Cuenta a alguien en casa algo que aprendiste hoy y di quién te lo enseñó.",
    extend="Haz un cartel con una descripción de tres frases y una línea que diga «Fuente:» con el nombre de quien te ayudó.",
)
