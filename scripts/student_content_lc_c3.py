"""Cuaderno del estudiante, 1.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS01: conocer y disfrutar textos orales breves de la tradición de los pueblos indígenas (contexto de
sensibilización). Los textos de práctica son originales en castellano, creados para este cuaderno y declarados
como tales: NO son textos de ningún pueblo. El texto tradicional real lo aporta el educador/a tradicional o la
comunidad, con su autorización.
"""
from __future__ import annotations

from student_content_lc_c1 import task, w
from student_lessons import ex, register

S1 = "LC01 OA LS01"

NOTE = "Texto de práctica creado para este cuaderno (no pertenece a ningún pueblo)."
RAIN = "Gota a gota cae la lluvia / sobre el techo de mi casa. / Gota a gota cae la lluvia / y la tierra se despierta."

register(
    S1, 1,
    materials="Un adulto que lea en voz alta; hoja y lápiz. Los textos de práctica están escritos aquí.",
    use="Aprenderé a escuchar un texto oral completo antes de opinar. Sirve para disfrutar poemas, canciones y adivinanzas de los pueblos con respeto.",
    prior=["Sé escuchar en silencio.", "Sé que hay textos que se dicen en voz alta y no solo se leen."],
    explain=[
        "Un texto oral es un texto que se dice en voz alta: una canción, un poema, una adivinanza o un trabalenguas. Muchos pueblos originarios tienen textos orales que sus familias y comunidades cuidan y se pasan de voz en voz.",
        "Para escuchar bien, lo primero es oírlo completo, de principio a fin, sin interrumpir. Después puedo decir quién habla, dónde pasa algo y qué se repite. Primero se escucha y después se opina.",
        "Hoy practico con un poema de práctica en castellano que se escribió para este cuaderno. El texto tradicional real lo trae el educador o la educadora tradicional, o una persona de la comunidad, y yo pregunto de qué pueblo es y quién lo comparte.",
    ],
    vocab=[("texto oral", "texto que se dice en voz alta"), ("poema", "texto con ritmo, dividido en versos"), ("verso", "una línea de un poema"), ("escuchar", "oír con atención"), ("tradición", "lo que un pueblo se pasa de generación en generación")],
    worked=[
        w("Escuchar completo", f"{NOTE} «{RAIN}». ¿Cuántos versos tiene (cada / marca el fin de un verso)?", ["Cuento las líneas separadas por /.", "Hay cuatro líneas."], "4 versos"),
        w("Decir de qué trata", "Con el mismo poema, ¿qué cae y dónde?", ["Leo «Gota a gota cae la lluvia».", "Sigo: «sobre el techo de mi casa»."], "cae la lluvia sobre el techo"),
    ],
    mistakes=[
        {"wrong": "Interrumpir para comentar a la mitad del texto.", "why": "Me pierdo partes del texto.", "fix": "Espero el final y luego hablo."},
        {"wrong": "Cambiar palabras del texto porque no las recuerdo.", "why": "Los textos de tradición tienen autoría y se cuidan.", "fix": "Digo «no lo recuerdo» y pido que lo repitan."},
    ],
    tiers={
        "recovery": [
            ex("Un texto oral se dice en voz alta. ¿Verdadero o falso?", "Verdadero", "Eso es un texto oral."),
            ex(f"{NOTE} Poema: «Sale el sol / y abre el día». ¿Cuántos versos tiene?", "2", "Hay dos líneas separadas por /."),
            ex("¿Qué hago primero con un texto: escucharlo completo o interrumpir?", "escucharlo completo", "Primero se escucha todo."),
        ],
        "understand": [
            ex(f"{NOTE} «{RAIN}». ¿Qué cae: la lluvia o la nieve?", "la lluvia", "El poema dice «cae la lluvia»."),
            ex("Una adivinanza, un poema y una canción, ¿son textos orales?", "Sí", "Se dicen o cantan en voz alta."),
            ex("¿Quién trae los textos tradicionales reales: el educador tradicional o un compañero que los inventa?", "el educador tradicional", "Los cuida la comunidad."),
        ],
        "apply": [
            ex(f"{NOTE} «{RAIN}». ¿Qué verso se repite con las mismas palabras?", "«Gota a gota cae la lluvia»", "Aparece al principio y en el tercer verso."),
            ex(f"{NOTE} «{RAIN}». ¿Dónde cae la lluvia?", "sobre el techo de mi casa", "Es lo que dice el segundo verso."),
            ex(f"{NOTE} «{RAIN}». ¿Qué se despierta al final?", "la tierra", "El último verso dice «la tierra se despierta»."),
        ],
        "reason": [
            ex("Ana dice «el poema habla del mar» y el poema solo habla de lluvia, techo y tierra. ¿Qué le dirías?", "que vuelva a escucharlo completo", "El mar no aparece en el texto."),
            ex("Si no recuerdo una palabra de un texto tradicional, ¿la invento o pido que la repitan?", "pido que la repitan", "Un texto tradicional no se cambia."),
        ],
        "challenge": [
            ex(f"{NOTE} «{RAIN}». ¿En cuántos versos aparece la palabra «lluvia»?", "2", "Está en el primer y en el tercer verso."),
            ex(f"{NOTE} «{RAIN}». Ordena: A) la tierra se despierta B) cae la lluvia C) techo de mi casa. ¿Cuál es el orden del texto? Escribe 3 letras.", "B, C, A", "Primero cae la lluvia, luego el techo y al final la tierra."),
        ],
    },
    context=[ex("Un adulto lee en tu casa el poema de la lluvia. Al final preguntas «¿puede repetir?». ¿Fue bien: pedir que lo repitan o completar con tus palabras?", "pedir que lo repitan", "Así no cambio el texto.")],
    selfcheck=[ex("¿Qué es un texto oral?", "un texto que se dice en voz alta", "Se dice y se escucha."), ex("¿Cuándo opino: antes o después de escuchar?", "después", "Primero se escucha completo."), ex("¿Quién comparte los textos reales de un pueblo?", "el educador tradicional o la comunidad", "Ellos los cuidan.")],
    open_task=task(
        "Pide a un adulto que lea el poema de práctica «Gota a gota cae la lluvia / sobre el techo de mi casa. / Gota a gota cae la lluvia / y la tierra se despierta» (creado para este cuaderno). Escucha completo. Después dibuja lo que cae y dónde cae, y escribe una pregunta para el educador/a tradicional o la comunidad sobre un texto oral real: ¿de qué pueblo es y quién lo comparte?",
        "Dibujé la lluvia sobre un techo. Pregunta: ¿de qué pueblo es el texto que nos traerá y quién nos lo comparte?",
        ["escucha completo sin interrumpir", "dice qué cae y dónde", "pregunta pueblo y fuente al educador/a tradicional o la comunidad"],
        ["dibujo", "pregunta escrita"],
        ["interrumpir", "cambiar palabras del texto"],
        "Reconoce que escuchó entero; si completó con palabras propias, vuelve a escuchar y distingue lo que dice el texto.",
    ),
    reinforce="Escucha un poema corto en casa y dime de qué trata en una frase.",
    extend="Pregunta a alguien de tu casa si recuerda una canción o adivinanza que se diga en voz alta y quién se la enseñó.",
)

register(
    S1, 2,
    materials="Un adulto que lea en voz alta; hoja y lápiz. Los textos de práctica están aquí.",
    use="Aprenderé a notar cuando una palabra, un verso o un sonido se repite. Sirve para seguir el ritmo de canciones, adivinanzas y trabalenguas.",
    prior=["Sé escuchar un texto completo.", "Sé aplaudir con el ritmo."],
    explain=[
        "En los textos orales muchas veces algo se repite: una palabra, una línea o un sonido. La repetición ayuda a recordar el texto y le da ritmo. Por eso es una pista importante para escuchar.",
        "Para encontrar una repetición, escucho dos veces. La primera vez entiendo de qué trata. La segunda vez levanto un dedo cada vez que aparece lo que se repite. Así lo cuento sin mirar el papel.",
        "Hoy practico con un trabalenguas y una adivinanza de práctica en castellano. Cuando el educador o la educadora tradicional comparta un texto real, buscaré lo mismo, sin cambiar sus palabras ni su ritmo.",
    ],
    vocab=[("repetición", "algo que se dice otra vez"), ("ritmo", "orden de sonidos fuertes y suaves"), ("trabalenguas", "frase difícil de decir rápido"), ("adivinanza", "pregunta con pistas para descubrir algo"), ("pista", "dato que ayuda")],
    worked=[
        w("Contar una repetición", f"{NOTE} Trabalenguas: «Pipo pela pocas papas, pocas papas pela Pipo». ¿Cuántas veces se dice «papas»?", ["Leo la frase y marco «papas».", "Aparece en «pocas papas» dos veces."], "2 veces"),
        w("Resolver una adivinanza", f"{NOTE} Adivinanza: «Soy de colores, huelo bien y las abejas me visitan en el jardín. ¿Qué soy?».", ["Primera pista: colores.", "Segunda: huelo bien.", "Tercera: las abejas me visitan en el jardín."], "una flor"),
    ],
    mistakes=[
        {"wrong": "Cambiar el orden de las palabras del trabalenguas.", "why": "Ya no tiene el mismo ritmo.", "fix": "Lo digo lento, tal como está, y luego más rápido."},
        {"wrong": "Responder la adivinanza antes de oír todas las pistas.", "why": "Las pistas juntas lo hacen único.", "fix": "Espero la última pista."},
    ],
    tiers={
        "recovery": [
            ex("Si algo se dice otra vez, ¿es una repetición?", "Sí", "Repetir es decir de nuevo."),
            ex(f"{NOTE} «Pipo pela pocas papas». ¿Cuántas palabras tiene?", "4", "Cuento Pipo, pela, pocas, papas: cuatro palabras."),
            ex("Una adivinanza tiene pistas. ¿Verdadero o falso?", "Verdadero", "Las pistas ayudan a descubrir."),
        ],
        "understand": [
            ex("¿Para qué sirve la repetición: para recordar el texto o para olvidarlo?", "para recordar el texto", "Repetir ayuda a la memoria y da ritmo."),
            ex("¿Cuántas veces escucho para encontrar una repetición: una o dos?", "dos", "Primero entiendo y luego cuento."),
            ex("¿Un trabalenguas es difícil de decir rápido o muy fácil?", "difícil de decir rápido", "Esa es su gracia."),
        ],
        "apply": [
            ex(f"{NOTE} «Pipo pela pocas papas, pocas papas pela Pipo». ¿Cuántas veces se dice «pocas»?", "2", "Aparece dos veces."),
            ex(f"{NOTE} «Pipo pela pocas papas, pocas papas pela Pipo». ¿Con qué letra empiezan todas las palabras?", "con p", "Pipo, pela, pocas, papas empiezan con p."),
            ex(f"{NOTE} Adivinanza: «Tengo cuatro patas, ladro y muevo la cola». ¿Qué soy?", "un perro", "Las pistas son cuatro patas, ladrar y mover la cola."),
        ],
        "reason": [
            ex("Un compañero dice «es un gato» en la adivinanza del perro porque tiene cuatro patas. ¿Qué pista no calza?", "ladro", "Los gatos no ladran."),
            ex("¿Por qué no cambio las palabras de un texto de tradición para que me salga más fácil?", "porque tiene autoría y se cuida", "Cambiarlo cambiaría el texto."),
        ],
        "challenge": [
            ex(f"{NOTE} «Pipo pela pocas papas, pocas papas pela Pipo». ¿Cuántas veces aparecen las palabras «pocas papas» seguidas?", "2", "Aparecen en la primera y en la segunda parte."),
            ex(f"{NOTE} «Mi mamá me mima mucho». ¿Cuántas palabras empiezan con m?", "5", "Mi, mamá, me, mima y mucho empiezan con m."),
        ],
    },
    context=[ex("Tu abuela te dice un trabalenguas: «Tres tristes tigres tragaban trigo». ¿Cuántas palabras empiezan con t?", "5", "Tres, tristes, tigres, tragaban y trigo empiezan con t.")],
    selfcheck=[ex("¿Qué repite el trabalenguas «Pipo pela pocas papas»?", "la letra p", "Todas las palabras empiezan con p."), ex("¿Escucho una o dos veces para buscar una repetición?", "dos", "Primero entiendo y luego cuento."), ex("¿Cambio el texto tradicional?", "No", "Se cuida tal como es.")],
    open_task=task(
        "Pide a un adulto que lea el trabalenguas de práctica «Pipo pela pocas papas, pocas papas pela Pipo» (creado para este cuaderno). Levanta un dedo cada vez que oigas «papas». Dibuja tus dedos. Después pregúntale al educador/a tradicional o a una persona de la comunidad si hay juegos de palabras en el pueblo que él/ella conoce y puede compartirnos.",
        "Levanté 2 dedos. Pregunta: ¿tienen un juego de palabras que nos puedan enseñar?",
        ["encuentra la repetición", "no cambia el texto", "pregunta al educador/a tradicional o a la comunidad"],
        ["dibujo de los dedos", "pregunta"],
        ["contar mal", "cambiar palabras"],
        "Celebra el conteo correcto (2); si cambió palabras, pídele repetir despacio tal como es.",
    ),
    reinforce="Cuenta cuántas veces se repite una palabra en una canción corta de tu casa.",
    extend="Inventa tu propio trabalenguas con la letra m (es tuyo, no de ningún pueblo) y enséñaselo a alguien.",
)

register(
    S1, 3,
    materials="Un adulto que lea en voz alta; espacio para moverte. Los gestos están descritos aquí.",
    use="Aprenderé a mostrar con el cuerpo y los gestos lo que entendí de un texto. Sirve para comprender sin depender solo de las palabras.",
    prior=["Sé hacer gestos con las manos y los brazos.", "Sé seguir un ritmo con aplausos."],
    explain=[
        "Entender un texto oral no siempre se dice con palabras. También puedo mostrarlo con el cuerpo: con las manos, los brazos o la cara. Eso se llama expresión corporal o gestual.",
        "Cuando hago un gesto, muestro lo que dice el texto, no lo que se me ocurre. Si el texto dice «arriba», subo los brazos. Si dice «abajo», los bajo. Si dice «aplaudo», aplaudo. Un gesto bien hecho muestra que escuché.",
        "Hay textos tradicionales que se acompañan con movimientos propios del pueblo. Esos movimientos los enseña el educador o la educadora tradicional. Yo no los invento ni los cambio, solo los observo y participo si me invitan.",
    ],
    vocab=[("gesto", "movimiento del cuerpo que muestra algo"), ("expresión corporal", "mostrar con el cuerpo"), ("arriba", "hacia el cielo"), ("abajo", "hacia el suelo"), ("invitar", "pedir a alguien que participe")],
    worked=[
        w("Unir texto y gesto", f"{NOTE} Texto: «Arriba las manos, abajo las manos, aplaudo y me siento». ¿Qué gesto va con «abajo las manos»?", ["Leo «abajo».", "Abajo es hacia el suelo.", "Bajo las manos."], "bajar las manos"),
        w("Contar los gestos", "En el mismo texto, ¿cuántos gestos hay que hacer?", ["Arriba las manos: 1.", "Abajo las manos: 2.", "Aplaudo: 3.", "Me siento: 4."], "4 gestos"),
    ],
    mistakes=[
        {"wrong": "Hacer un gesto que no está en el texto.", "why": "Ya no muestro lo que escuché.", "fix": "Hago solo los gestos que el texto dice."},
        {"wrong": "Cambiar un movimiento tradicional porque me parece raro.", "why": "Tiene un sentido para su pueblo.", "fix": "Lo observo y pregunto."},
    ],
    tiers={
        "recovery": [
            ex("Si el texto dice «arriba las manos», ¿subo o bajo las manos?", "subo las manos", "Arriba es hacia el cielo."),
            ex("Si el texto dice «aplaudo», ¿qué hago con las manos?", "aplaudo", "Hago palmas con las manos."),
            ex("Mostrar con el cuerpo lo que entendí, ¿es un gesto?", "Sí", "El gesto es un movimiento que muestra algo."),
        ],
        "understand": [
            ex("¿Para qué hago un gesto: para mostrar lo que dice el texto o para inventar otra cosa?", "para mostrar lo que dice el texto", "Eso muestra que escuché."),
            ex("¿Quién enseña los movimientos tradicionales de un pueblo?", "el educador tradicional", "Conoce su sentido."),
            ex("Verdadero o falso: puedo cambiar un movimiento tradicional porque me parece raro.", "Falso", "Tiene un sentido que debo respetar."),
        ],
        "apply": [
            ex(f"{NOTE} «Doy una vuelta, doy un paso, levanto un pie». ¿Cuántos gestos hay?", "3", "Hay tres acciones separadas por comas."),
            ex(f"{NOTE} «Doy una vuelta, doy un paso, levanto un pie». ¿Cuál es el segundo gesto?", "dar un paso", "Es el segundo en el texto."),
            ex(f"{NOTE} Une: «abajo» va con A) bajar los brazos B) subir los brazos. ¿Qué letra?", "A", "Abajo significa hacia el suelo."),
        ],
        "reason": [
            ex("Sofía hace un salto que no estaba en el texto. ¿Cumple el texto?", "No", "Mostró algo que el texto no dice."),
            ex("¿Por qué observo antes de participar en un movimiento tradicional?", "para no cambiarlo ni equivocarme", "Debo respetar cómo lo hacen."),
        ],
        "challenge": [
            ex(f"{NOTE} «Arriba las manos, abajo las manos, aplaudo y me siento». Si repito el texto dos veces, ¿cuántos gestos hago en total?", "8", "Cuatro gestos por vuelta, dos vueltas.", calc=None),
            ex(f"{NOTE} «Giro a la derecha, giro a la izquierda». ¿Cuántas direcciones distintas hay?", "2", "Derecha e izquierda."),
        ],
    },
    context=[ex("En una fiesta del curso una persona de la comunidad baila y te invita. Tú no conoces el movimiento. ¿Qué haces: observar y preguntar o inventar uno?", "observar y preguntar", "Respeto el movimiento y aprendo.")],
    selfcheck=[ex("¿Qué es un gesto?", "un movimiento que muestra algo", "Muestra una idea."), ex("¿Inventar un gesto en un texto tradicional es correcto?", "No", "Se respeta el texto."), ex("¿Quién enseña un movimiento tradicional?", "el educador tradicional", "Conoce su sentido y su forma.")],
    open_task=task(
        "Pide a un adulto que lea esto (texto de práctica creado para este cuaderno): «Arriba las manos, abajo las manos, aplaudo y me siento». Haz los cuatro gestos. Después dibuja en tu cuaderno cuatro monitos, uno por gesto. Pregunta al educador/a tradicional si hay un texto o juego del pueblo con gestos que se pueda compartir con respeto.",
        "Dibujé 4 monitos: manos arriba, manos abajo, aplauso y sentado. Pregunta: ¿qué juego con gestos nos pueden enseñar?",
        ["hace solo los gestos del texto", "dibuja los cuatro", "pregunta al educador/a tradicional o la comunidad"],
        ["cuerpo en movimiento", "dibujo"],
        ["inventar gestos", "olvidar uno"],
        "Cuenta con él/ella los cuatro gestos; si agregó uno, vuelve al texto y compara.",
    ),
    reinforce="Haz con el cuerpo cuatro acciones que te diga un adulto: arriba, abajo, aplaudo, sentado.",
    extend="Invita a alguien de casa a hacer los cuatro gestos del texto de práctica contigo.",
)

register(
    S1, 4,
    materials="Un adulto que lea en voz alta; hoja y lápiz. Los textos de práctica están aquí.",
    use="Aprenderé a relacionar un texto con algo que me pasó, sin cambiar el texto ni apropiarme de él. Sirve para entender mejor y respetar su autoría.",
    prior=["Sé contar algo que me pasó.", "Sé distinguir lo que dice un texto de lo que pienso yo."],
    explain=[
        "Un texto oral me puede recordar algo de mi vida: un día de lluvia, una comida o un juego. Eso se llama relacionar con mi experiencia. Es bueno hacerlo, pero siempre vuelvo al texto para no olvidar lo que dice.",
        "Un texto de tradición tiene autoría: pertenece a las personas que lo cuidan. Yo puedo decir «esto me recuerda…», pero no digo «este texto es mío», ni lo cambio, ni lo uso en otro lugar sin permiso.",
        "La fórmula es: primero digo qué dice el texto, después qué me recuerda y al final vuelvo al texto. Si hay una palabra que no conozco, pregunto al educador o a la educadora tradicional.",
    ],
    vocab=[("experiencia", "algo que viví"), ("relacionar", "unir dos cosas parecidas"), ("autoría", "de quién es un texto"), ("apropiarse", "decir que algo ajeno es mío"), ("recordar", "traer algo a la memoria")],
    worked=[
        w("Relacionar y volver", f"{NOTE} Texto: «El sol sale despacio, la mañana se despierta». Me recuerda un día de campamento. ¿Qué hago después?", ["Digo qué dice el texto: el sol sale y la mañana se despierta.", "Cuento lo que me recuerda.", "Vuelvo al texto y leo de nuevo."], "volver al texto"),
        w("Frase correcta", "Elige: A) «Este texto lo inventé yo» B) «Este texto me recuerda mi casa». ¿Cuál respeta la autoría?", ["A dice que es mío.", "B solo cuenta lo que me recuerda.", "Elijo B."], "B"),
    ],
    mistakes=[
        {"wrong": "Decir «este texto es mío» porque me gustó.", "why": "Tiene autoría de un pueblo o una persona.", "fix": "Digo «me recuerda…»."},
        {"wrong": "Contar mi experiencia y olvidar qué dice el texto.", "why": "Dejé de hablar del texto.", "fix": "Después de contar, vuelvo al texto."},
    ],
    tiers={
        "recovery": [
            ex("Si un texto me recuerda mi casa, ¿estoy relacionando con mi experiencia?", "Sí", "Uno el texto con algo que viví."),
            ex("¿De quién es un texto de tradición: de quien lo cuida o mío porque me gustó?", "de quien lo cuida", "Tiene autoría y se respeta."),
            ex("¿Qué frase uso: «me recuerda» o «es mío»?", "«me recuerda»", "Respeta la autoría."),
        ],
        "understand": [
            ex("Verdadero o falso: puedo cambiar un texto de tradición porque me gustó otra versión.", "Falso", "No me pertenece."),
            ex("¿Qué hago después de contar mi experiencia?", "vuelvo al texto", "Así no olvido lo que dice."),
            ex("¿Qué es autoría?", "de quién es un texto", "Dice a quién pertenece."),
        ],
        "apply": [
            ex(f"{NOTE} Texto: «La lluvia moja la calle». Elige lo que dice el texto: A) la lluvia moja la calle B) hace frío.", "A", "Solo A está en el texto."),
            ex(f"{NOTE} Texto: «La lluvia moja la calle». Elige lo que es mi experiencia: A) la lluvia moja la calle B) ayer me mojé camino a la escuela.", "B", "B cuenta algo que viví."),
            ex("Ordena: A) vuelvo al texto B) digo qué dice C) cuento lo que me recuerda. Escribe 3 letras.", "B, C, A", "Primero el texto, luego mi experiencia y vuelvo."),
        ],
        "reason": [
            ex("Luis dice «este canto lo inventé yo». Si es un canto de tradición, ¿qué le dirías?", "que pertenece a quien lo cuida", "Los cantos de tradición tienen autoría."),
            ex("¿Por qué pregunto si no conozco una palabra del texto?", "para no inventar su significado", "Preguntar cuida el texto."),
        ],
        "challenge": [
            ex(f"{NOTE} Texto: «El sol sale despacio». Marta dice «sale muy rápido». ¿Contradice el texto?", "Sí", "El texto dice despacio."),
            ex("Una compañera cuenta su experiencia y olvida volver al texto. ¿Qué parte del orden le falta?", "volver al texto", "Es la última parte."),
        ],
    },
    context=[ex("En casa, un adulto te dice un verso de una canción que le cantaban a él. Te recuerda tu cuna. ¿Qué dices: «me recuerda mi cuna» o «es mi canción»?", "«me recuerda mi cuna»", "Respeta la autoría.")],
    selfcheck=[ex("¿Qué orden sigo?", "texto, experiencia y volver al texto", "Es la fórmula."), ex("¿Digo «es mío» de un texto de tradición?", "No", "Tiene autoría de otros."), ex("¿Qué es relacionar?", "unir con algo parecido", "Es conectar ideas.")],
    open_task=task(
        "Pide a un adulto que lea este texto de práctica (creado para este cuaderno): «El sol sale despacio, la mañana se despierta». Dibuja lo que dice el texto y, aparte, dibuja algo que te recuerde. Escribe «Dice…» y «Me recuerda…». Pregunta al educador/a tradicional cómo se puede compartir un texto del pueblo con respeto a su autoría.",
        "Dice: el sol sale despacio. Me recuerda: una mañana en la playa. Pregunta: ¿cómo mencionamos de quién es el texto?",
        ["separa lo que dice el texto de su experiencia", "vuelve al texto", "pregunta al educador/a tradicional o a la comunidad"],
        ["dos dibujos", "frases escritas"],
        ["decir que el texto es suyo", "no volver al texto"],
        "Marca con color «Dice» y «Me recuerda»; si mezcló ambos, ayúdale a separarlos.",
    ),
    reinforce="Elige una canción que te gusta y di en una frase qué te recuerda.",
    extend="Cuenta en casa qué es la autoría de un texto con un ejemplo.",
)

register(
    S1, 5,
    materials="Un adulto que lea en voz alta dos veces; hoja y lápiz. Los textos están escritos aquí.",
    use="Aprenderé a escuchar otra vez con un propósito, por ejemplo, buscar un personaje o contar algo. Sirve para notar más cosas en el texto.",
    prior=["Sé escuchar un texto completo.", "Sé contar hasta 10."],
    explain=[
        "Cuando escucho un texto por segunda vez, ya no hace falta que entienda todo. Ahora busco algo concreto: un personaje, un lugar, una palabra que se repite o un sonido. Eso se llama escuchar con un propósito.",
        "El propósito me dice qué mirar o contar. Si mi propósito es contar animales, levanto un dedo cada vez que aparece uno. Si es encontrar el lugar, escucho dónde pasa. Cada propósito me muestra una parte distinta.",
        "Con textos de tradición también escucho dos veces: una para disfrutar y otra para notar. No cambio el texto ni lo grabo sin permiso. Si quiero escucharlo más veces, lo pido a quien lo comparte.",
    ],
    vocab=[("propósito", "lo que quiero buscar al escuchar"), ("personaje", "quien aparece en un texto"), ("lugar", "dónde ocurre algo"), ("segunda escucha", "escuchar otra vez"), ("notar", "darme cuenta de algo")],
    worked=[
        w("Propósito: animales", f"{NOTE} Texto: «El gato mira la luna, la luna mira el mar, el mar mira al cielo, el cielo mira al gato». ¿Cuántos animales hay?", ["Busco animales.", "Solo aparece el gato."], "1 animal"),
        w("Propósito: paisaje", "En el mismo texto, ¿cuántas cosas del paisaje se nombran (luna, mar, cielo)?", ["Cuento luna.", "Sigo con mar.", "Termino con cielo."], "3 cosas del paisaje"),
    ],
    mistakes=[
        {"wrong": "Escuchar la segunda vez sin buscar nada.", "why": "No noto más cosas.", "fix": "Antes de escuchar, elijo un propósito."},
        {"wrong": "Querer buscar tres cosas a la vez.", "why": "Me confundo.", "fix": "Busco una cosa en cada escucha."},
    ],
    tiers={
        "recovery": [
            ex("Un propósito es lo que quiero buscar al escuchar. ¿Verdadero o falso?", "Verdadero", "Es mi objetivo al escuchar."),
            ex(f"{NOTE} «El gato mira la luna». ¿Quién mira?", "el gato", "El gato es quien mira."),
            ex(f"{NOTE} «El gato mira la luna». ¿Qué mira?", "la luna", "Lo que se mira es la luna."),
        ],
        "understand": [
            ex("¿Cuántas cosas busco en cada escucha: una o tres?", "una", "Así no me confundo."),
            ex("Si mi propósito es contar animales, ¿qué hago al oír uno?", "levanto un dedo", "Marco cada animal."),
            ex("¿La segunda escucha sirve para notar más cosas?", "Sí", "Con un propósito se nota más."),
        ],
        "apply": [
            ex(f"{NOTE} «El gato mira la luna, la luna mira el mar, el mar mira al cielo, el cielo mira al gato». ¿Cuántas veces aparece la palabra «mira»?", "4", "Aparece una vez en cada parte."),
            ex(f"{NOTE} Mismo texto. ¿Qué mira el mar?", "al cielo", "El texto dice «el mar mira al cielo»."),
            ex(f"{NOTE} Mismo texto. ¿Quién mira al gato?", "el cielo", "El último verso dice «el cielo mira al gato»."),
        ],
        "reason": [
            ex("Alguien cuenta tres animales en el texto del gato. ¿Qué pasó?", "contó de más", "Solo hay un animal."),
            ex("¿Por qué no grabo un texto de tradición sin permiso para escucharlo más veces?", "porque pertenece a quien lo comparte", "Hay que pedir permiso."),
        ],
        "challenge": [
            ex(f"{NOTE} Mismo texto. Ordena: A) el mar B) el gato C) la luna. ¿En qué orden aparecen? Escribe 3 letras.", "B, C, A", "Aparecen gato, luna y mar."),
            ex(f"{NOTE} Mismo texto. ¿Con qué palabra termina el texto?", "gato", "El último verso termina con gato."),
        ],
    },
    context=[ex("Tu abuelo te cuenta una vez una historia corta con un perro, un río y una piedra. Escuchas de nuevo y cuentas solo los lugares. ¿Cuántos lugares hay?", "1", "Solo el río es un lugar; el perro y la piedra no.")],
    selfcheck=[ex("¿Qué es un propósito?", "lo que quiero buscar al escuchar", "Es mi objetivo."), ex("¿Cuántas cosas busco por escucha?", "una", "Así no me confundo."), ex("¿Puedo grabar un texto tradicional sin permiso?", "No", "Se pide permiso.")],
    open_task=task(
        "Pide a un adulto que lea dos veces este texto de práctica (creado para este cuaderno): «El gato mira la luna, la luna mira el mar, el mar mira al cielo, el cielo mira al gato». La primera vez disfrútalo. La segunda vez elige un propósito: A) contar cuántas veces se dice «mira» B) anotar los cuatro nombres que aparecen. Escribe tu resultado y una pregunta para el educador/a tradicional.",
        "Elegí A. Conté 4 veces «mira». Pregunta: ¿cuándo se dice este tipo de texto en el pueblo?",
        ["elige un solo propósito", "da un resultado correcto", "pregunta al educador/a tradicional o a la comunidad"],
        ["resultado escrito", "pregunta"],
        ["buscar varias cosas", "contar mal"],
        "Valida el propósito elegido y el conteo (A: 4; B: gato, luna, mar, cielo).",
    ),
    reinforce="Escucha un poema corto dos veces y busca un personaje la segunda vez.",
    extend="Explica a alguien de casa qué es un propósito para escuchar.",
)

register(
    S1, 6,
    materials="Hoja, lápiz y colores. El texto de práctica está escrito aquí.",
    use="Aprenderé a compartir lo que entendí de un texto de forma oral, corporal o con un dibujo. Sirve para mostrar mi comprensión y escuchar la de otros.",
    prior=["Sé escuchar un texto completo.", "Sé hacer un dibujo o un gesto."],
    explain=[
        "Compartir mi comprensión es contar a otros qué entendí. Puedo hacerlo hablando, con gestos o con un dibujo. Cualquiera de las tres formas vale si muestra la idea del texto.",
        "Cuando comparto, digo la idea principal, nombro de dónde viene el texto y reconozco lo que no sé. Por ejemplo: «Entendí que cae la lluvia. Es un texto de práctica. No sé qué otros textos hay en el pueblo». Eso es honesto.",
        "También escucho cómo comparten los demás y no me burlo. Si el texto es de tradición, termino con una pregunta o un agradecimiento para quien lo compartió, el educador o la educadora tradicional o la comunidad.",
    ],
    vocab=[("compartir", "mostrar a otros"), ("idea principal", "lo más importante del texto"), ("agradecer", "decir gracias"), ("honesto", "que dice la verdad, también lo que no sabe"), ("comprensión", "lo que entendí")],
    worked=[
        w("Idea principal", f"{NOTE} Texto: «Gota a gota cae la lluvia y la tierra se despierta». ¿Cuál es la idea principal?", ["Leo qué pasa: cae lluvia.", "Y qué pasa después: la tierra se despierta."], "la lluvia despierta la tierra"),
        w("Compartir con honestidad", "Elige: A) «Entendí que cae lluvia; no sé más» B) «Lo sé todo». ¿Cuál es honesta?", ["A reconoce lo que no sé.", "B exagera."], "A"),
    ],
    mistakes=[
        {"wrong": "Reírme de cómo comparte otra persona.", "why": "No cuido a quien participa.", "fix": "Escucho y agradezco."},
        {"wrong": "Decir que lo sé todo del texto.", "why": "No siempre es verdad.", "fix": "Digo lo que entendí y lo que debo preguntar."},
    ],
    tiers={
        "recovery": [
            ex("Puedo compartir con palabras, gestos o dibujos. ¿Verdadero o falso?", "Verdadero", "Las tres formas valen."),
            ex("¿Digo gracias a quien compartió el texto?", "Sí", "Se agradece a quien enseña."),
            ex("¿Me río de cómo comparte otro o lo escucho?", "lo escucho", "Se respeta a quien participa."),
        ],
        "understand": [
            ex("¿Qué es la idea principal: lo más importante del texto o un detalle?", "lo más importante del texto", "Resume de qué trata."),
            ex("¿Qué es ser honesto al compartir?", "decir también lo que no sé", "No exagero lo que sé."),
            ex("¿Qué agrego al final si el texto es de tradición?", "una pregunta o un gracias", "Reconozco a quien lo compartió."),
        ],
        "apply": [
            ex(f"{NOTE} «Sale el sol y abre el día». ¿Cuál es la idea principal: A) el sol abre el día B) hace frío?", "A", "A resume el texto."),
            ex("Elige la forma que muestra bien la idea de «el sol sale»: A) dibujo del sol saliendo B) dibujo de un perro.", "A", "A muestra lo que dice."),
            ex("Ordena: A) agradezco B) digo la idea C) nombro de dónde viene. Escribe 3 letras.", "B, C, A", "Idea, procedencia y gracias."),
        ],
        "reason": [
            ex("Daniel comparte con un dibujo y otro compañero se ríe. ¿Qué haces?", "pedir respeto y escuchar", "Cada forma vale."),
            ex("¿Por qué menciono de dónde viene el texto?", "para reconocer a quien lo comparte", "Cuido su autoría."),
        ],
        "challenge": [
            ex("Una compañera dice «Entendí que cae lluvia. Es de práctica. No sé de otros textos». ¿Cuántas partes honestas tiene (idea, procedencia, lo que no sabe)?", "3", "Dice las tres cosas."),
            ex("Una respuesta tiene la idea y el gracias, pero no la procedencia. ¿Cuántas de las 3 partes tiene?", "2", "Tiene idea y gracias."),
        ],
    },
    context=[ex("Después de que un abuelo comparte un texto, tu curso lo agradece. Tú dices una idea del texto con un dibujo. ¿Cuál de las formas (palabras, gestos, dibujos) usaste?", "dibujo", "Mostraste con una imagen.")],
    selfcheck=[ex("¿Cómo puedo compartir?", "con palabras, gestos o dibujos", "Hay varias formas."), ex("¿Qué digo si no sé algo?", "que lo preguntaré", "Soy honesto y pregunto."), ex("¿A quién agradezco?", "a quien compartió el texto", "Reconozco su aporte.")],
    open_task=task(
        "Pide a un adulto que lea este texto de práctica (creado para este cuaderno): «Sale el sol y abre el día, las flores se despiertan». Comparte lo que entendiste de una de estas formas: A) un dibujo B) un gesto C) una frase. Incluye una parte honesta («no sé…») y una pregunta para el educador/a tradicional o la comunidad.",
        "Hice un dibujo del sol y flores abiertas. Dije: entendí que el sol despierta las flores; no sé qué otros textos del pueblo hablan del sol. Pregunta: ¿pueden compartirnos uno?",
        ["muestra la idea del texto", "dice algo que no sabe", "pregunta a la comunidad o al educador/a tradicional"],
        ["dibujo, gesto o frase", "pregunta"],
        ["burlarse", "decir que lo sabe todo"],
        "Elogia la forma elegida y la honestidad; si exageró lo que sabe, ayúdale a agregar «no sé…».",
    ),
    reinforce="Comparte con dibujo un poema corto que escuches en casa.",
    extend="Enseña a alguien de casa las tres formas de compartir lo que se entendió.",
)
