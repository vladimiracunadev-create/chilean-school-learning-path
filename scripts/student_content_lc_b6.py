"""Cuaderno del estudiante, 1.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR02 (sonidos propios de la lengua indígena) y OA LR03 (palabras, frases, toponimia y
antroponimia significativas), contexto de rescate y revitalización de la lengua.

Los ejercicios usan palabras, mapas y nombres de práctica en castellano. El saludo «mari mari»
(mapuzugun) es el único término de lengua indígena. El modelo de los sonidos y los significados
reales los dan el educador/a tradicional, los mayores y la comunidad.
"""
from __future__ import annotations

from student_lessons import ex, register

OA2 = "LC01 OA LR02"
OA3 = "LC01 OA LR03"

MAPA2 = "Mapa de práctica: Estero Hondo (al norte), Lomas del Espino (en el centro), Cuesta Larga (al sur) e Isla Chica (al oeste)."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ LR02
register(
    OA2, 1,
    materials="Este cuaderno y lápiz. Las frases de práctica están en castellano; los sonidos de la lengua los modela el educador/a tradicional o un mayor.",
    use="Aprenderé a escuchar con cuidado antes de repetir y a encontrar un sonido dentro de una frase. Sirve para reconocer los sonidos de una lengua que se está recuperando.",
    prior=["Sé escuchar en silencio.", "Sé decir con qué sonido empieza una palabra."],
    explain=[
        "En una lengua que se está recuperando, a veces solo quedan unos pocos hablantes. Por eso escuchar bien es muy importante: cada sonido que oyes bien ayuda a que la lengua siga viva. Primero escuchas, después repites.",
        "Reconocer un sonido en el contexto es encontrarlo dentro de una frase, no solo suelto. Por ejemplo, en «Mamá mira la luna» el sonido «m» está al comienzo de dos palabras: Mamá y mira.",
        "Cuando el sonido es de una lengua indígena, el modelo es un hablante o un mayor. Tú escuchas varias veces, observas y esperas su permiso para ensayar. No lo cambias por un sonido del castellano.",
    ],
    vocab=[("hablante", "persona que habla la lengua"), ("contexto", "la frase donde está el sonido"), ("reconocer", "darse cuenta de que es el mismo sonido"), ("modelo", "persona que dice el sonido correcto"), ("recuperar", "volver a tener algo")],
    worked=[
        {"title": "Buscar un sonido en una frase", "problem": "Busca el sonido «m» al comienzo de las palabras de la frase «Mamá mira la luna».", "steps": ["Leo palabra por palabra: Mamá, mira, la, luna.", "Mamá empieza con «m».", "Mira empieza con «m».", "La y luna no."], "answer": "2 palabras"},
        {"title": "Esperar al modelo", "problem": "Un mayor dice un sonido de su lengua. ¿Qué haces antes de ensayarlo?", "steps": ["Escucho varias veces.", "Observo cómo lo dice.", "Espero su permiso para ensayar."], "answer": "Escuchar, observar y esperar su permiso"},
    ],
    mistakes=[
        {"wrong": "Repetir un sonido nuevo sin haberlo escuchado bien.", "why": "Lo cambias por uno que ya conoces.", "fix": "Escucha varias veces antes."},
        {"wrong": "Pensar que todos los sonidos de una lengua indígena se parecen al castellano.", "why": "Puede haber sonidos distintos.", "fix": "Escucha al hablante sin comparar."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué haces primero con un sonido de una lengua indígena: escuchar o repetir?", "Escuchar", "Se escucha primero."),
            ex("¿Quién es el modelo para un sonido de su lengua: un hablante o un compañero?", "Un hablante", "Él habla la lengua."),
            ex("En «sol», ¿con qué sonido empieza?", "S", "La palabra empieza con la «s»."),
        ],
        "understand": [
            ex("¿Por qué escuchar bien ayuda a una lengua que se recupera?", "Porque cada sonido bien oído la mantiene viva", "Se conserva la forma de hablar."),
            ex("¿Qué es reconocer un sonido en contexto?", "Encontrarlo dentro de una frase", "Está en una frase, no suelto."),
            ex("¿Se cambia un sonido nuevo por uno del castellano?", "No", "Puede ser distinto."),
        ],
        "apply": [
            ex("En la frase «Pedro pinta un pato», cuenta cuántas palabras empiezan con «p».", "3", "Pedro, pinta y pato."),
            ex("En la frase «La luna lleva luz», cuenta cuántas palabras empiezan con «l».", "4", "La, luna, lleva y luz empiezan con «l»."),
            ex("En la frase «Sapo sale al sol», cuenta cuántas palabras tienen «s» al comienzo.", "3", "Sapo, sale y sol."),
        ],
        "reason": [
            ex("Un niño dice que reconoció un sonido nuevo pero lo escuchó una sola vez. ¿Qué debería hacer?", "Escuchar más veces", "Una vez no basta."),
            ex("Una niña pide al mayor que repita el sonido. ¿Hizo bien?", "Sí", "Repetir ayuda a oír mejor."),
        ],
        "challenge": [
            ex("En «Mi mamá me mira», ¿cuántas palabras empiezan con «m»?", "4", "Mi, mamá, me y mira."),
            ex("Escribe una frase corta en la que tres palabras empiecen con el mismo sonido.", "Cualquier frase con tres palabras que empiecen igual", "Se acepta una frase que lo cumpla."),
        ],
    },
    context=[ex("Un mayor de la comunidad dice un sonido de su lengua. Un niño lo repite rápido, antes de escuchar. ¿Qué podrías recomendarle?", "Escuchar varias veces antes de repetir", "Así oye mejor.")],
    selfcheck=[
        ex("¿Se repite antes o después de escuchar?", "Después", "Primero se escucha."),
        ex("¿Quién es el modelo?", "El hablante o mayor", "Él conoce el sonido."),
        ex("En «mira», ¿con qué sonido empieza?", "M", "Empieza con la «m»."),
    ],
    open_task=task(
        "Con un adulto, juega a encontrar sonidos. Él dice estas tres frases despacio: «Mamá mira la luna», «Pedro pinta un pato», «Sapo sale al sol». Tú dices cuántas palabras empiezan con el primer sonido de la frase. Anota los tres números. Pregunta al educador/a tradicional, a un mayor o a la comunidad: ¿qué sonidos de nuestra lengua debemos escuchar primero y quién nos los puede modelar?",
        "Mamá mira la luna: 2. Pedro pinta un pato: 3. Sapo sale al sol: 3. Mi pregunta: ¿qué sonidos de nuestra lengua debemos escuchar primero?",
        ["escucha antes de decir", "cuenta bien", "pregunta al educador/a tradicional"],
        ["tres números", "pregunta escrita"],
        ["repetir sin escuchar", "comparar con el castellano"],
        "Valora la escucha cuidadosa y la pregunta a quien habla la lengua.",
    ),
    reinforce="Pide a un familiar tres frases y cuenta cuántas palabras empiezan con el primer sonido.",
    extend="Inventa dos frases de cuatro palabras que empiecen con el mismo sonido.",
)

register(
    OA2, 2,
    materials="Este cuaderno, lápiz y tu mano para sentir el aire. Los sonidos de práctica son del castellano.",
    use="Aprenderé a observar cómo se produce un sonido con el aire, los labios y la garganta, sin caricaturizar. Sirve para ensayar con seriedad los sonidos de una lengua.",
    prior=["Sé decir sonidos del castellano.", "Sé observar con atención."],
    explain=[
        "Los sonidos se hacen con el aire que sale de los pulmones y con la boca. Si pones tu mano frente a la boca y dices «p», sientes un golpecito de aire. Si dices «s», sientes un soplido continuo y suave.",
        "Si pones los dedos suavemente en tu garganta y dices «m» o «a», sientes una vibración. Con la «s» y la «p» no la sientes. Observar estas diferencias te sirve para notar cómo se hace cada sonido.",
        "Observar no es imitar con burla. Los sonidos de una lengua indígena se ensayan con seriedad y siguiendo al hablante. No se exageran ni se usan para hacer reír.",
    ],
    vocab=[("aire", "lo que sale al hablar"), ("vibración", "temblor que se siente en la garganta"), ("garganta", "parte del cuello por donde pasa la voz"), ("golpecito de aire", "salida breve de aire"), ("soplido", "salida continua de aire")],
    worked=[
        {"title": "Sentir el aire", "problem": "Pon la mano frente a la boca y di «pa». ¿Qué sientes?", "steps": ["Digo «pa» frente a la mano.", "Siento un golpecito de aire.", "Es el aire de la «p»."], "answer": "Un golpecito de aire"},
        {"title": "Sentir la vibración", "problem": "Toca tu garganta con dos dedos y di «mmm». ¿Qué sientes?", "steps": ["Pongo los dedos suavemente.", "Digo «mmm» largo.", "Siento un temblor."], "answer": "Una vibración"},
    ],
    mistakes=[
        {"wrong": "Apretar la garganta fuerte para sentir.", "why": "Puede incomodar o dañar.", "fix": "Toca suave con dos dedos."},
        {"wrong": "Hacer ruidos exagerados para imitar.", "why": "Es caricaturizar.", "fix": "Ensaya con calma y seriedad."},
    ],
    tiers={
        "recovery": [
            ex("Pones la mano frente a la boca y dices «p». ¿Sientes aire?", "Sí", "La «p» sale con aire."),
            ex("¿Qué sientes en la garganta al decir «mmm»?", "Una vibración", "Se siente un temblor."),
            ex("¿Con qué tocas tu garganta: suave o fuerte?", "Suave", "Se hace con cuidado."),
        ],
        "understand": [
            ex("¿Por qué observar el aire ayuda a ensayar un sonido?", "Porque muestra cómo se produce", "El aire es parte del sonido."),
            ex("¿Es respetuoso exagerar un sonido para hacer reír?", "No", "Eso es caricaturizar."),
            ex("¿La «s» tiene golpecito de aire o soplido continuo?", "Soplido continuo", "Es aire que sale suave y largo."),
        ],
        "apply": [
            ex("Di «sss» y «mmm». ¿Con cuál sientes vibración en la garganta?", "Con «mmm»", "La «m» vibra y la «s» no."),
            ex("Di «pa», «ta» y «ka» con la mano frente a la boca. ¿Cuántos sonidos dan golpecito de aire?", "3", "Los tres empiezan con un golpe de aire."),
            ex("Di «aaa». ¿Estás con la boca abierta o cerrada?", "Abierta", "La «a» se hace con la boca abierta."),
        ],
        "reason": [
            ex("Un niño dice que no hay aire en la «p» porque no lo vio. ¿Cómo puede comprobarlo?", "Con la mano frente a la boca", "El aire se siente."),
            ex("Una niña toca su garganta con cuidado y dice que la «m» vibra. ¿Observó bien?", "Sí", "Notó la vibración."),
        ],
        "challenge": [
            ex("Dices 4 sonidos: «m», «s», «a» y «p», con dos dedos suaves en la garganta. ¿Cuántos hacen vibrar la garganta?", "2", "Vibran la «m» y la «a»; la «s» y la «p» no."),
            ex("Escribe qué observaste en tu boca al decir «ssss».", "Por ejemplo, el aire sale por los dientes", "Describe una observación real."),
        ],
    },
    context=[ex("Un niño imita muy fuerte y gracioso a un hablante para hacer reír. ¿Qué podrías decirle?", "Que observe y ensaye con seriedad", "El respeto es lo principal.")],
    selfcheck=[
        ex("¿La «m» vibra?", "Sí", "Se siente en la garganta."),
        ex("¿Se caricaturiza un sonido?", "No", "Se respeta a las personas."),
        ex("¿Dónde sientes el aire de «p»?", "En la mano", "La mano frente a la boca."),
    ],
    open_task=task(
        "Pon la mano frente a la boca y di despacio «pa», «sa» y «ma». Anota en qué sonido sentiste golpecito de aire, en cuál soplido y en cuál no sentiste aire en la mano. Después toca suave tu garganta y anota en cuáles sentiste vibración. Pregunta al educador/a tradicional o a la comunidad: ¿cómo debemos observar y ensayar los sonidos de nuestra lengua sin burlarnos?",
        "En «pa» sentí un golpecito; en «sa» un soplido; en «ma» casi nada de aire en la mano y sentí vibración. Mi pregunta: ¿cómo ensayamos los sonidos de nuestra lengua sin burlarnos?",
        ["observa aire y vibración", "no exagera", "pregunta al educador/a tradicional"],
        ["tres observaciones", "pregunta escrita"],
        ["caricaturizar", "apretar la garganta"],
        "Valora la observación cuidadosa y el respeto.",
    ),
    reinforce="Siente el aire de tres sonidos con la mano frente a la boca.",
    extend="Compara con un familiar qué sonidos te hacen sentir vibración.",
)

register(
    OA2, 3,
    materials="Este cuaderno y lápiz. Las tarjetas de práctica están escritas en los ejercicios.",
    use="Aprenderé a unir un sonido o palabra con su significado cuando esa palabra fue verificada. Sirve para saber qué dice una palabra de la lengua y no solo cómo suena.",
    prior=["Sé que las palabras tienen significado.", "Sé que algunas palabras son saludos."],
    explain=[
        "Una palabra tiene un sonido y un significado. Para aprender una palabra de la lengua indígena necesitas las dos cosas: cómo suena y qué quiere decir. Las tarjetas de significado ayudan: de un lado va la palabra y del otro el dibujo.",
        "Una palabra verificada es la que un hablante competente o la comunidad confirmó. «Mari mari», por ejemplo, es un saludo en mapuzugun. Si una palabra no está verificada, no se usa ni se supone su significado.",
        "Nunca inventes un significado. Si no sabes qué quiere decir una palabra, escribe una pregunta en la tarjeta y llévala al educador/a tradicional.",
    ],
    vocab=[("tarjeta de significado", "ficha con palabra y dibujo"), ("verificada", "confirmada por un hablante o la comunidad"), ("significado", "lo que quiere decir"), ("suponer", "creer sin saber"), ("saludo", "palabra para recibir a alguien")],
    worked=[
        {"title": "Unir palabra y significado", "problem": "Tarjeta: palabra «mari mari»; dibujo: dos personas se saludan; fuente: la educadora. ¿Qué significa en la tarjeta?", "steps": ["Miro el dibujo.", "Dos personas se saludan.", "Significa saludo."], "answer": "Saludo"},
        {"title": "Palabra sin verificar", "problem": "Una tarjeta tiene una palabra y un dibujo pero ninguna fuente. ¿La puedes usar?", "steps": ["No sé quién la verificó.", "No puedo usarla todavía.", "Pregunto al educador/a tradicional."], "answer": "No; falta la verificación"},
    ],
    mistakes=[
        {"wrong": "Suponer el significado de una palabra por su dibujo.", "why": "El dibujo puede no ser exacto.", "fix": "Confirma con el educador/a tradicional."},
        {"wrong": "Hacer tarjetas sin fuente.", "why": "No se sabe quién verificó.", "fix": "Escribe la fuente."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué dos cosas tiene una palabra: sonido y qué más?", "Significado", "Una palabra suena y significa."),
            ex("Según el ejemplo de la tarjeta, ¿qué palabra de la lengua mapuche se explica como saludo?", "«mari mari»", "Es un saludo en mapuzugun."),
            ex("¿Qué es una tarjeta de significado?", "Una ficha con palabra y dibujo", "Une palabra y significado."),
        ],
        "understand": [
            ex("¿Qué significa «verificada»?", "Confirmada por un hablante o la comunidad", "Alguien que sabe la validó."),
            ex("¿Por qué no se supone el significado?", "Porque puede ser falso", "Se debe confirmar."),
            ex("¿Qué escribes en una tarjeta si no sabes algo?", "Una pregunta", "Así se pregunta después."),
        ],
        "apply": [
            ex("Tarjeta: palabra «luna»; dibujo: un círculo en el cielo; fuente: mamá. ¿Cuál es la fuente?", "Mamá", "La tarjeta lo dice."),
            ex("Tienes 6 tarjetas y 4 tienen fuente. ¿Cuántas faltan por verificar?", "2", "6 − 4 = 2."),
            ex("Ordena: a) dibujo, b) palabra, c) fuente. Escribe las letras como van en la tarjeta: palabra, dibujo, fuente.", "b, a, c", "Primero va la palabra."),
        ],
        "reason": [
            ex("Un niño usa una palabra de una tarjeta sin fuente porque el dibujo le pareció claro. ¿Está bien?", "No", "Sin verificación no se usa."),
            ex("Una niña escribe «¿qué significa esta palabra?» en su tarjeta. ¿Hizo bien?", "Sí", "Dejó una pregunta honesta."),
        ],
        "challenge": [
            ex("Si cada niña del grupo hace 2 tarjetas y son 5 niñas, ¿cuántas tarjetas hay?", "10", "2 + 2 + 2 + 2 + 2 = 10."),
            ex("Haz una tarjeta de práctica para «agua»: escribe palabra, dibujo y fuente.", "Cualquier tarjeta con los tres datos", "Debe tener los tres."),
        ],
    },
    context=[ex("La educadora tradicional te dice una palabra. Quieres hacer la tarjeta. ¿Qué anotas además del dibujo?", "La palabra y la fuente", "Se registra de quién viene.")],
    selfcheck=[
        ex("En el ejemplo de la educadora, ¿«mari mari» sirve para saludar o para despedirse?", "Para saludar", "Lo explicó la educadora."),
        ex("¿Se supone un significado?", "No", "Se confirma con quien sabe."),
        ex("¿Qué dice la fuente?", "Quién la verificó", "Es quien confirmó."),
    ],
    open_task=task(
        "Haz tres tarjetas de práctica en castellano: «sol», «agua» y «mano». En cada una escribe la palabra, dibuja su significado y anota quién te confirmó que está bien (un adulto de tu casa). Agrega una cuarta tarjeta con «mari mari» solo si tu educador/a tradicional te lo enseñó, con su significado y fuente. Pregunta al educador/a tradicional o a la comunidad: ¿qué palabras de nuestra lengua podemos incluir en las tarjetas y quién las verifica?",
        "Hice las tarjetas de sol, agua y mano con dibujos y fuente: mi papá. Mi pregunta: ¿qué palabras de nuestra lengua incluimos en las tarjetas y quién las verifica?",
        ["palabra, dibujo y fuente", "no supone significados", "pregunta al educador/a tradicional"],
        ["tres tarjetas", "pregunta escrita"],
        ["tarjetas sin fuente", "suponer significados"],
        "Valora las tarjetas completas y la verificación por la comunidad.",
    ),
    reinforce="Haz una tarjeta de significado para una palabra de tu casa.",
    extend="Haz tarjetas para tres palabras y ordénalas por su primera letra.",
)

register(
    OA2, 4,
    materials="Este cuaderno y lápiz. Las palabras de práctica están en castellano.",
    use="Aprenderé a contrastar sonidos con cuidado y a no escribir los sonidos de otra lengua con letras del castellano como si fueran iguales. Sirve para respetar cómo suena cada lengua.",
    prior=["Sé que una letra y un sonido son distintos.", "Sé escuchar con atención."],
    explain=[
        "Contrastar es comparar dos cosas para ver qué las diferencia. En castellano, «vaca» y «baca» empiezan con letras distintas pero con el mismo sonido. En cambio, «pata» y «bata» empiezan con sonidos distintos.",
        "Esto nos enseña que las letras no siempre muestran bien los sonidos. Con una lengua indígena pasa lo mismo: sus sonidos no siempre se pueden escribir con las letras del castellano sin cambiarlos.",
        "Por eso, cuando escuches un sonido nuevo, no le pongas una letra «parecida». Escúchalo con cuidado y pregunta cómo lo escribe y lo dice la comunidad. Cada pueblo tiene formas de escribir su lengua.",
    ],
    vocab=[("contrastar", "comparar para ver diferencias"), ("mismo sonido", "suena igual aunque se escriba distinto"), ("letra parecida", "letra que se cree que sirve pero no es igual"), ("escribir", "poner los sonidos en letras"), ("comunidad", "personas que comparten una cultura")],
    worked=[
        {"title": "Mismo sonido, letras distintas", "problem": "¿«vaca» y «baca» empiezan con el mismo sonido?", "steps": ["Digo «vaca».", "Digo «baca».", "Suenan igual al comienzo."], "answer": "Sí, aunque se escriben distinto"},
        {"title": "Sonidos distintos", "problem": "¿«pata» y «bata» empiezan con el mismo sonido?", "steps": ["Digo «pata» y «bata» con dos dedos suaves en la garganta.", "Con la «b» siento vibración y con la «p» no.", "Son sonidos distintos."], "answer": "No, son distintos"},
    ],
    mistakes=[
        {"wrong": "Pensar que si dos palabras empiezan con letras distintas, suenan distinto.", "why": "A veces el sonido es igual.", "fix": "Escucha el sonido antes de mirar la letra."},
        {"wrong": "Escribir con una letra parecida un sonido nuevo.", "why": "Lo cambias.", "fix": "Pregunta cómo se escribe en la lengua."},
    ],
    tiers={
        "recovery": [
            ex("¿«casa» y «caza» suenan igual en Chile?", "Sí", "En Chile la «s» y la «z» suenan igual."),
            ex("¿Contrastar es comparar o ignorar?", "Comparar", "Se buscan diferencias."),
            ex("¿Escribes un sonido nuevo con una letra parecida?", "No", "Se pregunta cómo se escribe."),
        ],
        "understand": [
            ex("¿Por qué «vaca» y «baca» empiezan con el mismo sonido?", "Porque la «v» y la «b» suenan igual en castellano", "Son letras distintas con un solo sonido."),
            ex("¿Las letras siempre muestran bien los sonidos?", "No", "A veces dos letras tienen un sonido."),
            ex("¿Quién enseña cómo escribir los sonidos de una lengua indígena?", "La comunidad", "Ella conoce cómo se escribe."),
        ],
        "apply": [
            ex("¿«pata» y «bata» empiezan con el mismo sonido o con sonidos distintos?", "Distintos", "La «p» y la «b» no suenan igual."),
            ex("¿«queso» y «kilo» empiezan con el mismo sonido?", "Sí", "La «qu» y la «k» suenan igual."),
            ex("¿«mesa» y «misa» cambian en el primer sonido o en el segundo?", "En el segundo", "Cambian la «e» y la «i»."),
        ],
        "reason": [
            ex("Un niño dice que «vaca» y «baca» suenan distinto porque se escriben distinto. ¿Tiene razón?", "No", "El sonido es igual."),
            ex("Una niña pregunta cómo se escribe un sonido nuevo en vez de ponerle una letra. ¿Hizo bien?", "Sí", "Preguntó a quien sabe."),
        ],
        "challenge": [
            ex("Tienes tres pares: vaca/baca, pata/bata y casa/caza. ¿En cuántos pares las dos palabras empiezan con el mismo sonido?", "2", "Vaca/baca y casa/caza empiezan igual; pata/bata no."),
            ex("Escribe un par de palabras que empiecen con letras distintas pero con el mismo sonido.", "Por ejemplo, queso y kilo", "El sonido es igual."),
        ],
    },
    context=[ex("Un niño oye un sonido nuevo de la lengua y escribe la letra «j» porque le pareció parecido. ¿Qué podrías decirle?", "Que pregunte cómo se escribe en la lengua", "La letra puede no representar bien el sonido.")],
    selfcheck=[
        ex("¿Contrastar es comparar?", "Sí", "Se buscan diferencias."),
        ex("¿Qué haces con un sonido nuevo?", "Pregunto cómo se escribe", "No se adivina."),
        ex("¿Suenan igual vaca y baca?", "Sí", "Comparten el sonido."),
    ],
    open_task=task(
        "Con un adulto compara estos tres pares de palabras: «vaca / baca», «pata / bata» y «queso / kilo». Escribe en cada par si el sonido del comienzo es igual o distinto. Pregunta al educador/a tradicional o a la comunidad: ¿cómo se escribe nuestra lengua y qué sonidos no se pueden escribir con letras del castellano?",
        "Vaca y baca: igual. Pata y bata: distinto. Queso y kilo: igual. Mi pregunta: ¿cómo se escribe nuestra lengua?",
        ["compara sonidos", "distingue letra y sonido", "pregunta a la comunidad"],
        ["tres respuestas", "pregunta escrita"],
        ["guiarse por la letra", "poner letras parecidas"],
        "Valora la comparación y recuerda que la comunidad enseña cómo se escribe.",
    ),
    reinforce="Compara dos pares de palabras en voz alta con un familiar.",
    extend="Busca un par de palabras con letras distintas y sonido igual.",
)

register(
    OA2, 5,
    materials="Este cuaderno y lápiz. Las prácticas son con palabras del castellano; los sonidos de la lengua los enseña el educador/a tradicional.",
    use="Aprenderé a ensayar un sonido con apoyo, respetando mi etapa de aprendizaje y la de mis compañeros. Sirve para avanzar sin presión y con respeto.",
    prior=["Sé escuchar un sonido.", "Sé que equivocarse es parte de aprender."],
    explain=[
        "Reproducir un sonido con apoyo es repetirlo mientras alguien te ayuda. Primero escuchas, luego lo dices muy bajito, después lo dices junto al hablante y al final lo dices solo. Cada paso es una etapa.",
        "Cada persona está en una etapa distinta. Algunos tardan más y eso no es un problema. Lo que importa es seguir ensayando con paciencia. Los hablantes y mayores también valoran tu esfuerzo.",
        "Respetar tu etapa significa no compararte con otros. Respetar la etapa de los demás significa no reírte si alguien se equivoca. Una lengua se recupera entre todos, ensayando y ayudándose.",
    ],
    vocab=[("etapa", "momento del aprendizaje"), ("paciencia", "calma para esperar"), ("esfuerzo", "trabajo para lograr algo"), ("apoyo", "ayuda de otra persona"), ("avance", "mejora poco a poco")],
    worked=[
        {"title": "Pasos de una etapa", "problem": "Ordena los pasos: a) decirlo solo, b) decirlo junto al hablante, c) escuchar, d) decirlo bajito.", "steps": ["Primero escucho.", "Luego bajito.", "Después con el hablante.", "Al final solo."], "answer": "c, d, b, a"},
        {"title": "Respetar la etapa de otro", "problem": "Un compañero se equivoca al ensayar y otros se ríen. ¿Qué haces?", "steps": ["No me río.", "Le digo «inténtalo otra vez».", "Todos estamos aprendiendo."], "answer": "Lo animo y no me río"},
    ],
    mistakes=[
        {"wrong": "Compararme con quien lo dice mejor.", "why": "Cada uno está en una etapa distinta.", "fix": "Fíjate en tu propio avance."},
        {"wrong": "Reírme de quien se equivoca.", "why": "Hace que otros tengan miedo de ensayar.", "fix": "Anímalo."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué haces primero para reproducir un sonido?", "Escuchar", "Siempre se escucha antes."),
            ex("¿Qué haces si alguien se equivoca: animarlo o reírte?", "Animarlo", "Animar ayuda a aprender."),
            ex("¿Todos están en la misma etapa?", "No", "Cada uno aprende a su ritmo."),
        ],
        "understand": [
            ex("¿Qué es el apoyo al ensayar?", "La ayuda de otra persona", "Un hablante o mayor te acompaña."),
            ex("¿Por qué es mejor no compararte con otros?", "Porque cada uno tiene su propia etapa", "Compararte con otros desanima."),
            ex("¿Qué se necesita para aprender una lengua: paciencia o apuro?", "Paciencia", "Se aprende de a poco."),
        ],
        "apply": [
            ex("Ordena: a) decirlo solo, b) escuchar, c) decirlo bajito, d) decirlo con el hablante. Escribe las letras.", "b, c, d, a", "Se avanza de escuchar a decir solo."),
            ex("Ensayas un sonido 4 veces el lunes y 3 veces el martes. ¿Cuántas veces ensayaste?", "7", "4 + 3 = 7."),
            ex("En un grupo de 6 niños, 2 ya dicen el sonido solos y los demás lo dicen con apoyo. ¿Cuántos lo dicen con apoyo?", "4", "6 − 2 = 4."),
        ],
        "reason": [
            ex("Una niña teme equivocarse y no ensaya. ¿Qué le dirías?", "Que equivocarse es parte de aprender", "Todos se equivocan al aprender."),
            ex("Un niño se burla del sonido de otro. ¿Qué pasa con la clase?", "Los demás pueden tener miedo de ensayar", "La burla frena el aprendizaje."),
        ],
        "challenge": [
            ex("Si ensayas 2 veces cada día durante 4 días, ¿cuántas veces ensayas en total?", "8", "2 + 2 + 2 + 2 = 8."),
            ex("Escribe una frase para animar a quien ensaya.", "Cualquier frase amable", "Debe animar con amabilidad."),
        ],
    },
    context=[ex("El mayor enseña un sonido y Rosa lo dice con otro sonido. Ella se pone roja. ¿Qué puede decir el curso?", "Que está aprendiendo y puede intentar otra vez", "Todos estamos en etapas distintas.")],
    selfcheck=[
        ex("¿Se compara uno con los demás?", "No", "Cada etapa es distinta."),
        ex("¿Qué se necesita?", "Paciencia", "Se aprende de a poco."),
        ex("Si un compañero falla al ensayar un sonido, ¿qué le dices?", "Lo animo", "Ayuda a seguir aprendiendo."),
    ],
    open_task=task(
        "Elige un sonido del castellano que te cueste, por ejemplo la «r» de «perro» o la «ch» de «chico», y ensáyalo cuatro veces, primero escuchando a un adulto, luego bajito, luego con él y luego solo. Marca cada paso con una rayita. Anota cómo te sentiste. Pregunta al educador/a tradicional o a la comunidad: ¿qué sonido de nuestra lengua debo ensayar primero y quién me ayuda?",
        "Ensayé la «r» de perro en cuatro pasos y puse cuatro rayitas. Me sentí tranquilo. Mi pregunta: ¿qué sonido de nuestra lengua debo ensayar primero?",
        ["sigue los pasos", "respeta su etapa", "pregunta a la comunidad"],
        ["cuatro rayitas", "pregunta escrita"],
        ["compararse", "reírse de otros"],
        "Valora el proceso por etapas y la paciencia.",
    ),
    reinforce="Ensaya un sonido tres días y marca cuántas veces lo hiciste.",
    extend="Anima a un familiar que esté aprendiendo algo nuevo.",
)

# ================================================================ LR03
register(
    OA3, 1,
    materials="Este cuaderno y lápiz. Las expresiones de práctica son del castellano; las de la lengua las enseña el educador/a tradicional.",
    use="Aprenderé que cada palabra o frase tiene un significado y una ocasión de uso, y que en una lengua que se recupera es importante usarla bien. Sirve para decir la palabra correcta en el momento correcto.",
    prior=["Sé qué es un saludo.", "Sé que las palabras tienen sentido."],
    explain=[
        "Una palabra no se usa en cualquier momento. «Hasta luego» se dice al despedirse, «por favor» al pedir algo y «de nada» al responder un agradecimiento. Cada expresión tiene su ocasión.",
        "En una lengua que se está recuperando, es muy valioso usar las palabras en la ocasión correcta. «Mari mari» es un saludo en mapuzugun y se usa al encontrarse con alguien. Otras palabras y frases se aprenden con los mayores y los educadores tradicionales.",
        "Una buena práctica es tener una ficha con tres datos: la palabra, su significado y su ocasión. Y siempre escribir quién te la enseñó. Así cuidas la palabra y reconoces a la persona que te la compartió.",
    ],
    vocab=[("expresión", "frase corta usada en una situación"), ("ocasión", "momento adecuado"), ("despedirse", "decir adiós"), ("ficha", "tarjeta de datos"), ("compartir", "dar a conocer")],
    worked=[
        {"title": "Palabra y ocasión", "problem": "Une: «hasta luego», «por favor», «de nada» con: al pedir algo, al despedirse, al responder gracias.", "steps": ["«Hasta luego» se dice al irse.", "«Por favor» se dice al pedir.", "«De nada» responde a gracias."], "answer": "hasta luego: al despedirse; por favor: al pedir algo; de nada: al responder gracias"},
        {"title": "Saludo y ocasión", "problem": "¿Cuándo dices «mari mari» según el ejemplo de la educadora mapuche?", "steps": ["Es un saludo.", "Los saludos se usan al encontrarse.", "Lo digo cuando veo llegar a alguien."], "answer": "Al encontrarme con alguien"},
    ],
    mistakes=[
        {"wrong": "Decir una expresión en el momento equivocado.", "why": "Cambia el sentido de lo que quieres decir.", "fix": "Pregunta cuándo se usa."},
        {"wrong": "No anotar quién me enseñó la palabra.", "why": "Se pierde la fuente.", "fix": "Escribe su nombre en la ficha."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué dices al irte: «hasta luego» o «por favor»?", "Hasta luego", "Es una despedida."),
            ex("¿Qué respondes cuando te dan las gracias: «de nada» o «buenos días»?", "De nada", "Es la respuesta a gracias."),
            ex("¿Para qué sirve «mari mari»?", "Para saludar", "Es un saludo."),
        ],
        "understand": [
            ex("¿Qué es la ocasión de una expresión?", "El momento adecuado para usarla", "Dice cuándo se dice."),
            ex("¿Por qué conviene saber quién te enseñó una palabra?", "Para reconocer y volver a preguntar", "Es la fuente."),
            ex("¿Cuáles son los tres datos de una ficha?", "Palabra, significado y ocasión", "Son los datos básicos."),
        ],
        "apply": [
            ex("Pides un lápiz prestado. ¿Qué dices al pedirlo: «por favor» o «hasta luego»?", "Por favor", "Se usa al pedir."),
            ex("Completa: «Cuando me voy de la casa de mi amiga digo ______».", "Hasta luego", "Es la despedida."),
            ex("Tienes 3 fichas con 3 datos cada una. ¿Cuántos datos hay en total?", "9", "3 + 3 + 3 = 9."),
        ],
        "reason": [
            ex("Un niño dice «hasta luego» al llegar. ¿Está bien la ocasión?", "No", "Es una despedida."),
            ex("Una niña pregunta cuándo se usa una palabra nueva. ¿Hizo bien?", "Sí", "Preguntó por la ocasión."),
        ],
        "challenge": [
            ex("Escribe una ocasión para decir «de nada».", "Cuando alguien me agradece", "Responde a un gracias."),
            ex("Hay 5 expresiones y 3 tienen ocasión escrita. ¿Cuántas faltan?", "2", "5 − 3 = 2."),
        ],
    },
    context=[ex("El educador tradicional enseña una palabra nueva y dice cuándo se usa. Tomás la usa en otra ocasión. ¿Qué podrías decirle?", "Que la use en la ocasión que explicó el educador", "Cada palabra tiene su ocasión.")],
    selfcheck=[
        ex("¿Qué dices al despedirte?", "Hasta luego", "Es la despedida."),
        ex("¿Qué haces con el nombre de quien te enseñó una palabra?", "Lo anoto en la ficha", "Se anota la fuente."),
        ex("¿«Mari mari» es saludo o despedida?", "Saludo", "Lo explicó la educadora."),
    ],
    open_task=task(
        "Haz tres fichas de uso con «hasta luego», «por favor» y «de nada». En cada una escribe el significado, la ocasión y quién te la enseñó (un adulto de tu casa). Dibuja la ocasión. Luego agrega una ficha con la palabra que el educador/a tradicional te enseñó, si ya lo hizo. Pregunta al educador/a tradicional o a la comunidad: ¿qué palabras de nuestra lengua conviene aprender primero y en qué ocasión se usan?",
        "Hasta luego: se dice al irse (dibujé una puerta). Me lo enseñó mi mamá. Mi pregunta: ¿qué palabras de nuestra lengua aprendo primero y cuándo se usan?",
        ["significado y ocasión", "fuente", "pregunta a la comunidad"],
        ["tres fichas", "pregunta escrita"],
        ["decir en la ocasión equivocada", "no anotar la fuente"],
        "Valora las fichas y el cuidado de la ocasión.",
    ),
    reinforce="Haz una ficha de uso para una expresión que digas en tu casa.",
    extend="Escribe tres ocasiones distintas en que se dice «gracias».",
)

register(
    OA3, 2,
    materials="Este cuaderno y lápiz. El mapa de práctica está escrito en los ejercicios.",
    use="Aprenderé a relacionar el nombre de un lugar con el territorio y a preguntar por su historia. Sirve para respetar los nombres de la tierra, especialmente los de origen indígena.",
    prior=["Sé que los lugares tienen nombre.", "Sé leer palabras cortas con ayuda de un adulto."],
    explain=[
        "El nombre de un lugar suele decir algo: cómo es, qué hay o qué pasó allí. «Estero Hondo» dice que hay un estero profundo. «Cuesta Larga» dice que la subida es larga. Los nombres nos ayudan a recordar el territorio.",
        "En Chile muchos nombres de lugares vienen de lenguas indígenas. Esos nombres son parte de la memoria de los pueblos. Para conocer su significado hay que preguntar a personas de la comunidad. No se adivinan.",
        "Un mapa permite ubicar los lugares. Para leerlo, buscas el nombre y la dirección. En un mapa el norte se dibuja arriba, el sur abajo, el este a la derecha y el oeste a la izquierda. Cuando una lengua se está recuperando, volver a usar sus nombres de lugares es una forma de recuperar la memoria del territorio.",
    ],
    vocab=[("estero", "arroyo pequeño de agua"), ("cuesta", "subida larga de un camino"), ("lomas", "cerros bajos y suaves"), ("territorio", "tierra donde vive una comunidad"), ("memoria", "lo que se recuerda")],
    worked=[
        {"title": "Leer un nombre", "problem": MAPA2 + " ¿Qué te cuenta «Cuesta Larga»?", "steps": ["Cuesta es una subida.", "Larga dice cuánto mide.", "Cuenta que hay una subida larga."], "answer": "Hay una subida larga"},
        {"title": "Ubicar", "problem": MAPA2 + " ¿Qué lugar está al norte?", "steps": ["Busco la palabra norte.", "Dice Estero Hondo.", "Esa es la respuesta."], "answer": "Estero Hondo"},
    ],
    mistakes=[
        {"wrong": "Inventar el significado de un nombre indígena de lugar.", "why": "Puede ser falso.", "fix": "Pregunta a la comunidad."},
        {"wrong": "Leer mal la dirección del mapa.", "why": "Ubicas mal el lugar.", "fix": "Busca la palabra exacta de la dirección."},
    ],
    tiers={
        "recovery": [
            ex(MAPA2 + " ¿Qué lugar está al sur?", "Cuesta Larga", "El mapa lo dice."),
            ex(MAPA2 + " ¿Qué lugar está al oeste?", "Isla Chica", "El mapa lo dice."),
            ex("¿Cómo llamamos a la tierra donde vive y se mueve una comunidad?", "El territorio", "Es el lugar propio de la comunidad."),
        ],
        "understand": [
            ex("¿Por qué los nombres de lugares son parte de la memoria?", "Porque cuentan cómo es el lugar o qué pasó", "Guardan información del lugar."),
            ex("¿Cómo se sabe qué significa un nombre indígena de lugar?", "Preguntando a la comunidad", "Ella lo sabe."),
            ex("¿Qué es un estero?", "Un arroyo pequeño de agua", "Es agua que corre."),
        ],
        "apply": [
            ex(MAPA2 + " ¿Cuántos lugares tiene el mapa?", "4", "Son cuatro lugares."),
            ex(MAPA2 + " ¿Qué lugar está en el centro?", "Lomas del Espino", "El mapa lo dice."),
            ex(MAPA2 + " ¿Dónde crees que hay un estero: en Estero Hondo o en Isla Chica?", "En Estero Hondo", "El nombre lo dice."),
        ],
        "reason": [
            ex(MAPA2 + " Un niño dice que Isla Chica está al norte. ¿Tiene razón?", "No", "Está al oeste."),
            ex("Una niña pregunta a una persona mayor por qué un cerro tiene su nombre. ¿Hizo bien?", "Sí", "Preguntó a quien conoce."),
        ],
        "challenge": [
            ex(MAPA2 + " Si caminas desde Lomas del Espino hacia el sur, ¿a qué lugar llegas?", "A Cuesta Larga", "Cuesta Larga está al sur."),
            ex("Escribe un nombre de un lugar de tu barrio y qué te cuenta.", "Cualquier nombre con su explicación", "Debe ser real y conocido."),
        ],
    },
    context=[ex("La educadora quiere contar por qué un lugar tiene su nombre en la lengua. Un niño dice «yo creo que significa…». ¿Qué debería hacer?", "Escuchar a la educadora", "Ella conoce la historia.")],
    selfcheck=[
        ex(MAPA2 + " ¿Qué lugar está en la parte de más al norte?", "Estero Hondo", "El mapa lo pone al norte."),
        ex("¿Se adivina un nombre indígena de lugar?", "No", "Se pregunta a la comunidad."),
        ex("¿Qué cuenta un nombre de lugar?", "Cómo es o qué pasó", "Guarda la memoria del lugar."),
    ],
    open_task=task(
        "Dibuja un mapa muy simple con tres lugares de tu barrio, por ejemplo la plaza, el río o la escuela. Escribe sus nombres y dónde queda cada uno en tu dibujo (arriba, abajo, a la derecha o a la izquierda de tu casa). Pregunta a un adulto por qué un lugar se llama así. Pregunta al educador/a tradicional o a la comunidad: ¿qué lugares de nuestro territorio tienen nombre en la lengua y qué cuentan esos nombres?",
        "Dibujé la plaza arriba, el río a la izquierda y la escuela a la derecha. La plaza se llama así por una feria. Mi pregunta: ¿qué lugares tienen nombre en la lengua?",
        ["mapa con tres lugares", "direcciones", "pregunta a la comunidad"],
        ["mapa", "pregunta escrita"],
        ["inventar significados", "confundir direcciones"],
        "Valora el mapa y recuerda que los significados los explica la comunidad.",
    ),
    reinforce="Dibuja el camino de tu casa a la escuela con los nombres de los lugares.",
    extend="Averigua por qué dos lugares de tu barrio se llaman así.",
)

register(
    OA3, 3,
    materials="Este cuaderno y lápiz. Las historias de nombres de práctica son inventadas.",
    use="Aprenderé que los nombres de las personas guardan historias, que cada persona decide si las cuenta, y que los nombres se cuidan. Sirve para respetar la memoria de las familias.",
    prior=["Sé decir mi nombre.", "Sé que los nombres vienen de alguien."],
    explain=[
        "Los nombres de las personas pueden recordar a una abuela, un lugar, un animal o algo que pasó. Así, cada nombre guarda memoria. En las familias se transmiten nombres y apellidos de generación en generación.",
        "Cada pueblo tiene sus formas de dar nombres. Si una lengua se está recuperando, muchos nombres vuelven a usarse. El significado de un nombre indígena lo explica la familia o la comunidad, no se adivina por cómo suena.",
        "La historia de un nombre es privada. Se cuenta si la persona quiere. Si alguien no quiere contarla, se respeta. Y los nombres nunca se usan para burlarse.",
    ],
    vocab=[("memoria", "lo que se recuerda"), ("generación", "grupo de personas de la misma edad en la familia"), ("transmitir", "pasar de unos a otros"), ("privado", "que cada uno decide si comparte"), ("burla", "risa para dañar")],
    worked=[
        {"title": "Un nombre con memoria", "problem": "Marcos se llama así por su tío Marcos, que le enseñó a pescar. ¿A quién recuerda su nombre?", "steps": ["Leo la historia.", "Dice que es por su tío.", "Recuerda a su tío Marcos."], "answer": "A su tío Marcos"},
        {"title": "Respetar la decisión", "problem": "Le preguntas a una amiga por su nombre y no quiere contarlo. ¿Qué haces?", "steps": ["Acepto su decisión.", "No insisto.", "No hago bromas."], "answer": "Acepto y no insisto"},
    ],
    mistakes=[
        {"wrong": "Insistir cuando alguien no quiere contar su historia.", "why": "Es privada.", "fix": "Acepta su decisión."},
        {"wrong": "Adivinar el significado de un nombre indígena.", "why": "Puedes decir algo falso.", "fix": "Pregunta a la familia o comunidad."},
    ],
    tiers={
        "recovery": [
            ex("¿Un nombre puede recordar a alguien?", "Sí", "Puede recordar a una persona."),
            ex("Marcos lleva el nombre de su tío. ¿A quién recuerda?", "A su tío", "Ese es el origen."),
            ex("¿Haces bromas con los nombres?", "No", "Se respetan los nombres."),
        ],
        "understand": [
            ex("¿Por qué la historia de un nombre es privada?", "Porque cada persona decide si la cuenta", "Es suya y de su familia."),
            ex("¿Quién explica el significado de un nombre indígena?", "La familia o la comunidad", "Ellos lo conocen."),
            ex("¿Qué significa transmitir un nombre?", "Pasarlo de unos a otros", "Va de una generación a otra."),
        ],
        "apply": [
            ex("Un amigo no quiere contar por qué se llama así. ¿Qué haces: insistir o aceptar?", "Aceptar", "Se respeta a las personas."),
            ex("En un curso hay 4 niños y 3 niñas que quieren contar la historia de su nombre. ¿Cuántos quieren contarla?", "7", "4 + 3 = 7."),
            ex("De 7 compañeros, 5 contaron la historia de su nombre y el resto no. ¿Cuántos no la contaron?", "2", "7 − 5 = 2."),
        ],
        "reason": [
            ex("Un niño cuenta la historia del nombre de un compañero sin permiso. ¿Qué hizo mal?", "Contó algo privado", "Era del compañero."),
            ex("Una niña pregunta con respeto y acepta que no le cuenten. ¿Fue respetuosa?", "Sí", "Aceptó su decisión."),
        ],
        "challenge": [
            ex("Escribe tu nombre y una cosa que sepas de él, o escribe «lo preguntaré».", "Cualquier respuesta", "Cada uno sabe distinto."),
            ex("Si cada uno de 3 hermanos lleva el nombre de un abuelo distinto, ¿cuántos abuelos recuerdan?", "3", "Uno por cada hermano."),
        ],
    },
    context=[ex("La educadora tradicional cuenta la historia de su nombre. Después un niño la imita para hacer reír. ¿Qué podrías decirle?", "Que no se burle", "El nombre merece respeto.")],
    selfcheck=[
        ex("¿Un nombre guarda memoria?", "Sí", "Puede recordar a alguien."),
        ex("¿Se insiste si no quieren contar?", "No", "Se respeta a las personas."),
        ex("¿Se adivina un nombre indígena?", "No", "Se pregunta a la comunidad."),
    ],
    open_task=task(
        "Pregunta a un adulto de tu casa quién eligió tu nombre y por qué. Escribe o dibuja lo que te cuente. Si no lo sabe o prefieres no compartirlo, dibuja tu nombre con colores y escribe «lo guardo». No tienes que mostrar tu historia si no quieres. Pregunta al educador/a tradicional o a la comunidad: ¿cómo se dan los nombres en nuestro pueblo y cómo debemos cuidarlos?",
        "Mi abuela eligió mi nombre porque era el de su hermana. Dibujé a las dos. Mi pregunta: ¿cómo se dan los nombres en nuestro pueblo?",
        ["pregunta con respeto", "acepta lo que le cuentan", "pregunta a la comunidad"],
        ["dibujo o frase", "pregunta escrita"],
        ["insistir", "burlarse"],
        "Valora el respeto y recuerda que no hay obligación de compartir.",
    ),
    reinforce="Pregunta a un familiar por su nombre y escúchalo.",
    extend="Haz un árbol con nombres de tu familia, solo si quieres compartirlo.",
)

register(
    OA3, 4,
    materials="Este cuaderno y lápiz. La expresión que se usa la valida el educador/a tradicional.",
    use="Aprenderé a hacer una interacción breve usando una expresión solo si fue verificada y en el contexto correcto. Sirve para conversar con respeto en una lengua que se recupera.",
    prior=["Sé saludar y despedirme.", "Sé que cada expresión tiene su ocasión."],
    explain=[
        "Una interacción breve es una conversación corta de dos o tres turnos: uno saluda, el otro responde y se agradece. Para hacerla bien miras a la persona, hablas claro y esperas.",
        "En una lengua que se está recuperando, las expresiones deben haber sido verificadas por un hablante o por la comunidad. Si no lo están, no se usan. «Mari mari» es un saludo en mapuzugun que se puede usar si el educador/a tradicional lo enseñó en tu curso.",
        "Si la otra persona dice algo que no entiendes, no finjas. Agradece y después pregunta qué significa. Aprender lleva tiempo, y los hablantes valoran la honestidad.",
    ],
    vocab=[("turno", "momento de hablar"), ("verificada", "confirmada"), ("contexto", "situación"), ("fingir", "hacer como que entiendo"), ("agradecer", "decir gracias")],
    worked=[
        {"title": "Tres turnos", "problem": "Ordena: a) agradezco, b) la persona responde, c) yo saludo.", "steps": ["Primero saludo.", "Luego responde.", "Al final agradezco."], "answer": "c, b, a"},
        {"title": "No entender la respuesta", "problem": "Una persona te responde algo que no entiendes. ¿Qué haces?", "steps": ["No finjo.", "Agradezco.", "Pregunto después."], "answer": "Agradezco y pregunto después"},
    ],
    mistakes=[
        {"wrong": "Usar una expresión que nadie verificó.", "why": "Puede estar mal.", "fix": "Usa solo lo que el educador validó."},
        {"wrong": "Fingir que entiendes.", "why": "No aprendes y puedes equivocarte.", "fix": "Pregunta."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántos turnos tiene una interacción de saludo, respuesta y gracias?", "3", "Son tres turnos."),
            ex("¿Qué haces si no entiendes la respuesta?", "Agradezco y pregunto después", "No se finge."),
            ex("¿Miras a la persona al saludar?", "Sí", "Mirar es una muestra de respeto."),
        ],
        "understand": [
            ex("¿Por qué usar solo expresiones verificadas?", "Para no usar la lengua equivocadamente", "Quien conoce la lengua las confirmó."),
            ex("¿Qué es fingir?", "Hacer como que entiendo", "No es honesto."),
            ex("¿Por qué valoran los hablantes la honestidad?", "Porque ayuda a aprender de verdad", "Preguntar enseña más que fingir."),
        ],
        "apply": [
            ex("Llega el educador y tú lo saludas con la expresión que él enseñó. ¿Cuál usas: la validada o una inventada?", "La validada", "Se usa lo verificado."),
            ex("Hay 4 niños que saludan al educador con 3 turnos cada uno. ¿Cuántos turnos hay en total?", "12", "3 + 3 + 3 + 3 = 12."),
            ex("De 8 niños, 5 usaron la expresión validada. ¿Cuántos no?", "3", "8 − 5 = 3."),
        ],
        "reason": [
            ex("Un niño inventa una respuesta en la lengua para parecer experto. ¿Qué puede pasar?", "Decir algo equivocado", "Sin verificar puede estar mal."),
            ex("Una niña dice «gracias, ¿me explica después?». ¿Actuó bien?", "Sí", "Fue honesta al preguntar."),
        ],
        "challenge": [
            ex("Escribe una frase para agradecer cuando no entiendes la respuesta.", "Cualquier frase de agradecimiento", "Debe agradecer con respeto."),
            ex("Cuenta los pasos: mirar, saludar, esperar, agradecer. ¿Cuántos pasos son?", "4", "Son cuatro pasos."),
        ],
    },
    context=[ex("Un visitante habla con tu curso en su lengua. Un niño responde con una frase que oyó en un video. ¿Qué le dirías?", "Que use solo lo verificado", "El video puede no ser del mismo pueblo.")],
    selfcheck=[
        ex("¿Se finge entender?", "No", "Se pregunta a la comunidad."),
        ex("¿Qué expresión usas?", "La verificada", "Se usa lo confirmado."),
        ex("Cuando termina la conversación breve, ¿qué dices a la otra persona?", "Gracias", "Se agradece a quien comparte."),
    ],
    open_task=task(
        "Con un adulto haz tres interacciones breves de saludo: saluda, espera la respuesta y agradece. Si el educador/a tradicional ya te enseñó una expresión, úsala; si no, usa un saludo en castellano. Anota cuántos turnos tuvo cada interacción y cómo cuidaste el respeto. Pregunta al educador/a tradicional o a la comunidad: ¿qué se responde a nuestro saludo y cuándo se usa?",
        "Saludé a mi mamá, a mi tío y a mi abuela. En cada una hubo tres turnos. Mi pregunta: ¿qué se responde al saludo de nuestra lengua y cuándo se usa?",
        ["respeta turnos", "usa expresiones verificadas", "pregunta a la comunidad"],
        ["tres interacciones", "pregunta escrita"],
        ["fingir", "inventar"],
        "Valora la interacción cuidada y la honestidad.",
    ),
    reinforce="Haz una interacción de saludo con alguien de tu casa y agradece.",
    extend="Explica a un familiar por qué no se debe fingir que se entiende.",
)
