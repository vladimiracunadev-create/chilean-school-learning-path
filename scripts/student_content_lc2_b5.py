"""Cuaderno del estudiante, 2.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR02 (medio natural y mensajes de la naturaleza, contexto de revitalización).

Los textos, familias y personajes de práctica están en castellano, son inventados y no pertenecen
a ningún pueblo. Los mensajes de la naturaleza de práctica son observaciones cotidianas (nubes,
viento, flores) y no describen creencias de ningún pueblo. Las únicas palabras de mapuzugun son
«mari mari», «mapu», «ko», «antü» y «kuyen»; puma y cóndor (quechua) y copihue (mapuche) se
mencionan como préstamos al castellano de Chile. La escritura, la pronunciación y el uso de cada
palabra indígena los confirma el educador/a tradicional o la comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


LR02 = "LC02 OA LR02"

SENAL = "Cuando el cielo se llena de nubes grises y el viento se enfría, en mi casa decimos que va a llover."

register(
    LR02, 1,
    materials="Este cuaderno y lápiz. Las palabras de la lista son pocas y muy conocidas; el educador/a tradicional puede completar y corregir.",
    use="Aprenderé a reconocer las palabras que ya conozco para hablar de la naturaleza, y los avisos que mi familia lee en el cielo o en las plantas. Sirve para darse cuenta de que la lengua y el territorio están presentes.",
    prior=["Sé nombrar elementos de la naturaleza.", "Sé que ko, mapu, antü y kuyen son palabras de mapuzugun."],
    explain=[
        "El medio natural es el lugar con cielo, tierra, agua, plantas y animales. Para hablar de él tenemos palabras de muchos orígenes. En castellano de Chile usamos puma y cóndor, que vienen del quechua, y copihue, que viene del mapuzugun. También hay palabras muy conocidas en mapuzugun: mapu (tierra), ko (agua), antü (sol) y kuyen (luna).",
        "Un mensaje de la naturaleza es una señal que se ve y avisa algo. Por ejemplo, si el cielo se llena de nubes grises y el viento se enfría, mucha gente piensa que va a llover. Estas señales las aprenden las familias mirando durante muchos años. No todas las familias ni comunidades leen las mismas señales.",
        "Para activar tu memoria, pregunta en casa: ¿qué palabras usamos para hablar del agua, la tierra, el sol o la luna? ¿Qué señales de la naturaleza conocemos? Anótalas con el nombre de quien te las dijo. No importa si pocas personas saben palabras de una lengua indígena: lo importante es no juzgar y seguir aprendiendo.",
    ],
    vocab=[("medio natural", "lugar con cielo, tierra, agua, plantas y animales"), ("mensaje", "señal que avisa algo"), ("préstamo", "palabra que una lengua toma de otra"), ("memoria", "lo que recordamos"), ("territorio", "lugar donde vive o vivió un pueblo")],
    worked=[
        {"title": "Clasificar palabras", "problem": "Clasifica estas palabras en cielo, tierra o agua: antü (sol), mapu (tierra), ko (agua), kuyen (luna).", "steps": ["Antü y kuyen están en el cielo.", "Mapu es tierra.", "Ko es agua."], "answer": "Cielo: antü y kuyen; tierra: mapu; agua: ko"},
        {"title": "Una señal de la familia", "problem": f"Lees: «{SENAL}». ¿Cuál es la señal y qué avisa?", "steps": ["La señal son las nubes grises y el viento frío.", "Lo que avisa es que va a llover."], "answer": "Nubes grises y viento frío; avisa lluvia"},
    ],
    mistakes=[
        {"wrong": "Pensar que todas las familias leen las mismas señales.", "why": "Cada lugar y cada familia tiene su experiencia.", "fix": "Di de qué familia o lugar es la señal."},
        {"wrong": "Burlarse de quien conoce pocas palabras indígenas.", "why": "Hay muchas razones por las que se dejan de usar.", "fix": "Respeta y aprende junto con el grupo."},
    ],
    tiers={
        "recovery": [
            ex("«Ko» en mapuzugun quiere decir agua. ¿Qué elemento de la naturaleza nombra?", "Agua", "Así lo dice la lista."),
            ex("«Mapu» quiere decir tierra. ¿Qué elemento nombra?", "Tierra", "Así lo dice la lista."),
            ex("Un mensaje de la naturaleza es una señal que avisa algo. Nubes grises y viento frío avisan lluvia. ¿Qué avisan?", "Lluvia", "Es lo que dice la señal."),
        ],
        "understand": [
            ex("Clasifica «kuyen» (luna): ¿cielo o tierra?", "Cielo", "La luna está en el cielo."),
            ex("Puma y cóndor vienen del quechua. ¿De qué lengua viene «copihue»?", "Del mapuzugun", "No está en la lista del quechua."),
            ex("¿Por qué no se burla de quien sabe pocas palabras de una lengua indígena?", "Porque hay muchas razones por las que se dejan de usar", "No se juzga a nadie."),
        ],
        "apply": [
            ex("Palabras: antü, mapu, ko, kuyen. ¿Cuántas nombran algo del cielo?", "2", "Antü y kuyen."),
            ex(f"Lee: «{SENAL}». ¿Qué cosa se enfría?", "El viento", "El texto lo dice."),
            arith("En el cuaderno anotaste 4 palabras para el agua, 3 para la tierra y 2 para el sol. ¿Cuántas palabras anotaste?", "4+3+2", "Se suman los tres grupos."),
        ],
        "reason": [
            ex("Sol dice que todas las familias saben que las nubes grises avisan lluvia. ¿Por qué no se puede afirmar eso?", "Porque cada familia tiene su experiencia", "No todas leen las mismas señales."),
            ex("Una niña anotó una señal que le contó su vecina y escribió su nombre. ¿Qué hizo bien?", "Anotó la fuente", "Dijo quién le enseñó."),
        ],
        "challenge": [
            ex("Mira esta lista: copihue, ko, cóndor, antü, puma, mapu. ¿Cuántas vienen del mapuzugun?", "4: copihue, ko, antü y mapu", "Cóndor y puma son del quechua; las otras cuatro vienen del mapuzugun."),
            ex("Camila escribe: «El puma, el cóndor y el copihue están en la naturaleza». ¿Cuántos elementos de la naturaleza nombra?", "3", "Puma, cóndor y copihue."),
        ],
    },
    context=[ex("En tu familia, cuando huele a tierra mojada, dicen que ha llovido. Si lo anotas, ¿qué dato agregas?", "Quién me lo dijo", "Se cita la fuente.")],
    selfcheck=[
        ex("¿Qué quiere decir «antü»?", "Sol", "Es una palabra de mapuzugun."),
        ex("¿Qué es un mensaje de la naturaleza?", "Una señal que avisa algo", "Avisa lo que puede pasar."),
        ex("¿Qué anotas al lado de una señal?", "Quién me la dijo", "Es la fuente."),
    ],
    open_task=task(
        "Haz una lista con tres columnas: cielo, tierra y agua. Escribe en cada una dos palabras de este grupo (mapu, ko, antü, kuyen, nube, río, cerro, lluvia). Después pregunta a un adulto de tu casa una señal de la naturaleza que él conozca (por ejemplo, cómo sabe que va a llover) y anótala con su nombre.",
        "Cielo: antü (sol), nube. Tierra: mapu, cerro. Agua: ko, río. Señal: mi papá dice que cuando el cielo se pone gris va a llover (papá Juan).",
        ["clasifica sin error", "usa las palabras dadas", "anota una señal con el nombre de quien la dijo"],
        ["lista de tres columnas", "señal anotada"],
        ["clasificar mal antü o kuyen", "no anotar quién dijo la señal"],
        "Reconoce que clasificó y que anotó la fuente. Si la palabra tiene dudas, el educador la confirma.",
    ),
    reinforce="Mira el cielo y anota qué nubes o qué sol ves hoy.",
    extend="Haz un mapa de palabras con «naturaleza» al centro y cinco palabras que conozcas alrededor.",
)

register(
    LR02, 2,
    materials="Este cuaderno y lápiz. Un adulto lee el texto de práctica en voz alta.",
    use="Aprenderé a escuchar un mensaje de la naturaleza y a preguntar su significado, su pronunciación y cuándo se usa. Sirve para aprender de una fuente de la comunidad con respeto.",
    prior=["Sé las tres preguntas: significado, pronunciación y contexto.", "Sé escuchar completo."],
    explain=[
        "Un mensaje de la naturaleza se escucha con tres preguntas. El significado: ¿qué avisa? La pronunciación: ¿cómo se dice la palabra o la frase? El contexto: ¿cuándo y dónde se usa? Una misma señal puede avisar cosas distintas según el lugar. Por eso el contexto es importante.",
        "Escucha este texto de práctica: «Doña Rosa, personaje inventado, dice: cuando las nubes grises suben desde el mar, hay que guardar la ropa». El significado: viene lluvia. El contexto: un lugar cerca del mar. La pronunciación, si hubiera una palabra indígena, la diría ella, que es la fuente.",
        "Si la fuente dice una palabra en una lengua indígena, no la cambies. Repítela solo si te invita a hacerlo y anótala como te la muestre. Si no entiendes, pide que repita. No discutas el significado ni lo cambies: tú aprendes de quien sabe.",
    ],
    vocab=[("mensaje", "señal que avisa algo"), ("significado", "lo que avisa la señal"), ("contexto", "cuándo y dónde se usa"), ("pronunciación", "cómo se dice una palabra"), ("fuente comunitaria", "persona de la comunidad que enseña")],
    worked=[
        {"title": "Tres preguntas al mensaje", "problem": "Doña Rosa, personaje inventado, dice: «Cuando las nubes grises suben desde el mar, hay que guardar la ropa». ¿Cuáles son el significado y el contexto?", "steps": ["Significado: viene lluvia.", "Contexto: un lugar cerca del mar.", "La pronunciación, si hay una palabra indígena, la dice ella."], "answer": "Significado: viene lluvia; contexto: cerca del mar"},
        {"title": "Cambiar de contexto", "problem": "Un niño dice que esa misma señal avisa lluvia en una ciudad lejos del mar. ¿Qué debe preguntar?", "steps": ["La señal vino de un lugar cerca del mar.", "En otro lugar puede cambiar.", "Debe preguntar si sirve en su lugar."], "answer": "Si la señal sirve también en su lugar"},
    ],
    mistakes=[
        {"wrong": "Creer que una señal avisa lo mismo en todos los lugares.", "why": "El contexto cambia el significado.", "fix": "Pregunta dónde y cuándo se usa."},
        {"wrong": "Cambiar la palabra de la fuente por otra que te suena mejor.", "why": "La palabra es de la comunidad.", "fix": "Anota lo que te dice la fuente."},
    ],
    tiers={
        "recovery": [
            ex("«Cuando las nubes grises suben desde el mar, hay que guardar la ropa». ¿Qué avisa?", "Lluvia", "Es el significado."),
            ex("En la frase anterior, ¿dónde se usa la señal: cerca del mar o en el desierto?", "Cerca del mar", "El texto dice «desde el mar»."),
            ex("Si no entiendes lo que dice la fuente, ¿qué haces?", "Pido que repita", "Así aprendes mejor."),
        ],
        "understand": [
            ex("El significado de una señal es lo que avisa. En «el viento frío avisa que baja la temperatura», ¿qué avisa?", "Que baja la temperatura", "Dice lo que avisa."),
            ex("¿Por qué importa el contexto de una señal?", "Porque puede avisar cosas distintas según el lugar", "El lugar cambia el significado."),
            ex("¿Quién dice la pronunciación de una palabra indígena: la fuente o un compañero?", "La fuente", "Ella conoce la lengua."),
        ],
        "apply": [
            ex("Lee: «Si el sol sale con halo, mi abuela guarda las herramientas». Escribe la señal y qué hace la abuela.", "Señal: el sol con halo; la abuela guarda las herramientas", "Se separa señal y acción."),
            ex("Ficha: «Señal: nubes grises. Significado: lluvia. Contexto: cerca del mar. Fuente: Doña Rosa». ¿Cuál es el contexto?", "Cerca del mar", "La ficha lo dice."),
            arith("Escuchas 3 mensajes por día durante 2 días. ¿Cuántos mensajes escuchas?", "3*2", "Se suman 3 mensajes dos días."),
        ],
        "reason": [
            ex("Tomás dijo que la señal de Doña Rosa sirve igual en la cordillera. ¿Qué debió preguntar?", "Si sirve también en su lugar", "El contexto puede cambiar."),
            ex("Una niña cambió la palabra de Doña Rosa por otra que le gustaba más. ¿Qué error cometió?", "Cambió la palabra de la fuente", "La palabra es de la comunidad."),
        ],
        "challenge": [
            ex("Lee: «Doña Rosa dice que cuando las nubes suben desde el mar hay que guardar la ropa. No sé cómo se dice “nube” en su lengua». Escribe la fuente, el mensaje y el límite.", "Fuente: Doña Rosa; mensaje: nubes desde el mar avisan lluvia; límite: no sé cómo se dice «nube»", "Separa quién, qué y lo que falta."),
            ex("Dos fichas: A) «Señal: nubes grises. Significado: lluvia. Contexto: cerca del mar. Fuente: Doña Rosa». B) «Señal: nubes. Significado: no sé». ¿Cuál es más completa?", "A", "Tiene las tres preguntas respondidas."),
        ],
    },
    context=[ex("Una vecina te dice que cuando florece cierto árbol, empieza la primavera. ¿Qué dos preguntas le haces?", "¿Qué significa y dónde se usa?", "Son el significado y el contexto.")],
    selfcheck=[
        ex("¿Cuáles son las tres preguntas?", "Significado, pronunciación y contexto", "Son las tres."),
        ex("¿Por qué importa el contexto?", "Porque cambia el significado", "Depende del lugar."),
        ex("¿Quién es la fuente?", "La persona de la comunidad que enseña", "Ella conoce la lengua."),
    ],
    open_task=task(
        "Pide a un adulto que te lea este texto inventado: «La señora Marta dice que, en su pueblo del interior, cuando el viento del cerro cambia de dirección, hay que cerrar el gallinero porque viene lluvia». Completa una ficha con: señal, significado, contexto y fuente. Escribe una pregunta que le harías a la señora Marta sobre cómo se dice una de las palabras en su lengua, sin inventar ninguna.",
        "Señal: el viento cambia de dirección. Significado: viene lluvia. Contexto: un pueblo del interior. Fuente: la señora Marta. Pregunta: ¿cómo se dice «lluvia» en su lengua?",
        ["completa señal, significado, contexto y fuente", "escribe una pregunta", "no inventa palabras en lengua indígena"],
        ["ficha de cuatro datos", "pregunta"],
        ["inventar la palabra en lengua indígena", "no escribir el contexto"],
        "Reconoce la ficha completa. La señora Marta es un personaje inventado.",
    ),
    reinforce="Pregunta a alguien mayor una señal de la naturaleza y anota qué avisa y cuándo se usa.",
    extend="Haz una ficha con tres señales que conozcas y completa señal, significado y contexto.",
)

register(
    LR02, 3,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé a describir mi entorno usando mis palabras y las palabras confirmadas, en situaciones seguras. Sirve para unir lo que veo con la lengua con respeto.",
    prior=["Sé describir con Veo, Es y Está.", "Sé qué significan mapu, ko, antü y kuyen."],
    explain=[
        "Puedes describir el medio natural que te rodea con oraciones claras en castellano. Si quieres agregar una palabra de una lengua indígena, ponla entre paréntesis después de la palabra en castellano y solo si la fuente la confirmó. Por ejemplo: «El agua (ko) del río está fría». Así no cambias la palabra ni inventas.",
        "Una situación pertinente es una situación adecuada. Un buen momento puede ser una actividad del curso donde todos practican, o cuando el educador tradicional visita y te invita a decir la palabra. No se usa para bromear ni para cambiar las palabras. Se usa con calma y con respeto.",
        "Practica en voz baja con un adulto de tu casa. Si te equivocas, pregunta y vuelve a intentar. Tu objetivo no es hablar perfecto, sino usar la lengua con cuidado y mostrar que la quieres aprender.",
    ],
    vocab=[("describir", "decir cómo es algo"), ("paréntesis", "signos ( ) que encierran una palabra"), ("pertinente", "adecuado para la situación"), ("confirmada", "revisada por quien sabe"), ("practicar", "hacer varias veces para aprender")],
    worked=[
        {"title": "Describir con una palabra confirmada", "problem": "Escribe una oración sobre el sol con la palabra confirmada «antü».", "steps": ["Escribo una idea completa: El sol brilla fuerte.", "Pongo «antü» entre paréntesis después de «sol»: El sol (antü) brilla fuerte."], "answer": "El sol (antü) brilla fuerte"},
        {"title": "Elegir la situación", "problem": "¿Dónde es pertinente decir «ko» en voz alta: a) en una actividad del curso donde practican, b) para burlarte de alguien que toma agua?", "steps": ["En a) practican con respeto.", "En b) se burla.", "Es pertinente la a)."], "answer": "La a) en una actividad del curso"},
    ],
    mistakes=[
        {"wrong": "Cambiar el orden de las palabras para formar oraciones en una lengua indígena.", "why": "La gramática de esa lengua la conocen sus hablantes.", "fix": "Escribe en castellano y pon la palabra confirmada entre paréntesis."},
        {"wrong": "Usar la palabra para bromear.", "why": "Es una lengua viva.", "fix": "Úsala en situaciones de práctica o con la fuente."},
    ],
    tiers={
        "recovery": [
            ex("«Antü» es sol. ¿Qué palabra va entre paréntesis en «El sol (___) brilla»?", "antü", "Antü es sol."),
            ex("«Ko» es agua. ¿Qué palabra va en «El agua (___) está fría»?", "ko", "Ko es agua."),
            ex("«Kuyen» es luna. ¿Qué palabra va en «La luna (___) sale de noche»?", "kuyen", "Kuyen es luna."),
        ],
        "understand": [
            ex("¿Por qué ponemos la palabra confirmada entre paréntesis?", "Para no cambiar la palabra y unirla a su significado", "Así se evita inventar."),
            ex("¿Cuál es una situación pertinente: una actividad del curso con práctica o una broma?", "Una actividad del curso con práctica", "Se usa con respeto."),
            ex("¿Quién conoce la gramática de una lengua indígena?", "Los hablantes", "Ellos conocen la lengua."),
        ],
        "apply": [
            ex("Escribe una oración sobre la tierra con «mapu» entre paréntesis. Elige: a) «La tierra (mapu) está seca», b) «Mapu tierra seca». Letra:", "a", "Es una oración clara con la palabra confirmada."),
            ex("En «La luna (kuyen) alumbra el patio», ¿cuántas palabras hay en castellano, sin contar kuyen?", "5", "La, luna, alumbra, el y patio."),
            arith("Escribes 2 oraciones sobre el sol, 3 sobre el agua y 1 sobre la luna. ¿Cuántas oraciones son?", "2+3+1", "Se suman los tres grupos."),
        ],
        "reason": [
            ex("Un niño escribió «ko mapu» para decir «agua de la tierra». ¿Qué error cometió?", "Inventó una expresión en mapuzugun", "No conoce la gramática."),
            ex("Una niña dice «El sol (antü) brilla» en el patio durante una actividad del curso. ¿Qué hizo bien?", "Usó la palabra confirmada en una situación de práctica", "Respetó la palabra y el contexto."),
        ],
        "challenge": [
            ex("Ordena las palabras y escribe la oración con «ko» entre paréntesis después de «agua»: «agua / el / del / está / río / fría».", "El agua (ko) del río está fría", "Mantiene la palabra confirmada."),
            ex("Dos oraciones: A) «El sol (antü) calienta la tierra (mapu)». B) «Antü calienta mapu». ¿Cuál no inventa gramática?", "A", "Está en castellano con palabras confirmadas."),
        ],
    },
    context=[ex("Haces un cartel para la sala: «El agua da vida». Quieres agregar «ko». ¿Cómo lo escribes?", "El agua (ko) da vida", "Palabra confirmada entre paréntesis.")],
    selfcheck=[
        ex("¿Dónde pones la palabra indígena confirmada?", "Entre paréntesis", "Así no cambias la oración."),
        ex("En Lengua y Cultura: ¿Qué haces si te equivocas?", "Pregunto y vuelvo a intentar", "Se aprende practicando."),
        ex("¿Se usa para bromear?", "No", "Se usa con respeto."),
    ],
    open_task=task(
        "Mira desde tu ventana o tu patio. Escribe tres oraciones en castellano: una sobre el sol o el cielo, otra sobre el agua y otra sobre la tierra. En cada una, pon entre paréntesis la palabra confirmada (antü, ko o mapu). Practica en voz baja con un adulto, en un lugar seguro, si el educador te enseñó cómo se dicen.",
        "El sol (antü) brilla. El agua (ko) está fría. La tierra (mapu) está seca. Practiqué con mi hermana, en voz baja.",
        ["escribe tres oraciones completas", "usa antü, ko y mapu con su significado", "practica en un lugar seguro"],
        ["tres oraciones", "práctica con un adulto"],
        ["juntar palabras en mapuzugun sin saber la gramática", "cambiar el significado"],
        "Reconoce las oraciones y la práctica. La pronunciación la enseña el educador tradicional.",
    ),
    reinforce="Escribe una oración sobre el cielo de hoy con antü o kuyen entre paréntesis.",
    extend="Escribe cuatro oraciones sobre tu barrio con una palabra confirmada en cada una.",
)

register(
    LR02, 4,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé a registrar un mensaje de la naturaleza cuando dos fuentes lo cuentan de maneras distintas, sin decidir cuál es la única correcta. Sirve para respetar que las comunidades y familias pueden leer la naturaleza de formas diferentes.",
    prior=["Sé qué es una variante.", "Sé anotar la fuente."],
    explain=[
        "Dos familias de un mismo lugar pueden contar un mensaje de la naturaleza de maneras distintas. Una puede decir que el aviso de lluvia son las nubes grises. Otra puede decir que es el viento frío. Las dos se fijan en señales reales y ninguna se equivoca solo por ser distinta.",
        "Para registrar, haz una ficha con estos datos: señal, significado, quién la dijo, de qué lugar o comunidad es y cómo la dijo. Si hay dos formas de decirlo, haz dos fichas. No juntes todo en una sola respuesta ni decidas cuál es la «verdadera».",
        "Al final puedes comparar. Anota qué se parece y qué cambia. Y escribe una pregunta que le harías a cada fuente para entender por qué lo dice así. Ese es el modo de aprender con respeto.",
    ],
    vocab=[("variante", "otra forma de decir lo mismo"), ("registro", "anotación que guarda un dato"), ("ficha", "hoja con datos ordenados"), ("semejanza", "lo que se parece"), ("diferencia", "lo que cambia")],
    worked=[
        {"title": "Dos fichas", "problem": "La familia Rojas dice que el aviso de lluvia son las nubes grises. La familia Soto dice que es el viento frío. Registra las dos.", "steps": ["Ficha 1: señal nubes grises, significado lluvia, fuente familia Rojas.", "Ficha 2: señal viento frío, significado lluvia, fuente familia Soto.", "No digo cuál es la verdadera."], "answer": "Dos fichas, una por familia, sin decidir cuál es la verdadera"},
        {"title": "Comparar", "problem": "Con las dos fichas anteriores, ¿qué se parece y qué cambia?", "steps": ["Se parece en el significado: las dos avisan lluvia.", "Cambia la señal: nubes grises o viento frío."], "answer": "Se parece el significado; cambia la señal"},
    ],
    mistakes=[
        {"wrong": "Decidir que una familia está equivocada.", "why": "Cada familia observa desde su experiencia.", "fix": "Registra las dos con sus fuentes."},
        {"wrong": "Juntar las dos señales en una sola ficha sin decir quién dijo cada una.", "why": "Se pierde la fuente.", "fix": "Haz una ficha por fuente."},
    ],
    tiers={
        "recovery": [
            ex("La familia Rojas dice que el aviso son las nubes grises. ¿Quién es la fuente?", "La familia Rojas", "Ella lo dijo."),
            ex("Si dos fuentes dicen cosas distintas, ¿haces una ficha o dos?", "Dos fichas", "Una por cada fuente."),
            ex("¿Es correcto decir que una de las dos familias se equivoca solo por decirlo distinto?", "No", "Cada una observa desde su experiencia."),
        ],
        "understand": [
            ex("Las dos familias dicen que avisa lluvia. ¿Qué se parece entre ellas?", "El significado", "Las dos dicen lluvia."),
            ex("¿Qué cambia entre ellas: la señal o el significado?", "La señal", "Una dice nubes y otra viento."),
            ex("¿Por qué anotas la fuente en cada ficha?", "Para saber quién lo dijo", "Se reconoce a cada fuente."),
        ],
        "apply": [
            ex("Ficha 1: «Señal: sol rojo al amanecer. Significado: viento. Fuente: Don Luis». Ficha 2: «Señal: viento del sur. Significado: frío. Fuente: Doña Elena». ¿Cuántas fuentes hay?", "2", "Don Luis y Doña Elena."),
            ex("En la ficha 1, ¿qué avisa el sol rojo al amanecer?", "Viento", "La ficha lo dice."),
            arith("Tienes 3 fichas con 4 datos cada una. ¿Cuántos datos en total?", "3*4", "Se suman 4 datos tres veces."),
        ],
        "reason": [
            ex("Beto borró una ficha porque «era distinta» a la suya. ¿Qué perdió?", "Información de otra fuente", "Cada ficha tiene valor."),
            ex("Una niña escribió «las dos familias tienen razón: son variantes». ¿Qué hizo bien?", "No juzgó y registró las dos", "Respetó las variantes."),
        ],
        "challenge": [
            ex("Lee: «La familia Rojas mira las nubes. La familia Soto mira el viento». Escribe una semejanza y una diferencia.", "Semejanza: las dos observan la naturaleza; diferencia: miran señales distintas", "Se comparan sin jerarquizar."),
            ex("Escribe una pregunta que le harías a la familia Soto para entender su señal.", "¿Por qué el viento frío avisa lluvia en su lugar?", "Pregunta por el porqué sin juzgar."),
        ],
    },
    context=[ex("Tu abuela y tu tío dicen señales distintas para lo mismo. ¿Cómo lo registras?", "Con dos fichas, una por cada persona", "No se descarta ninguna.")],
    selfcheck=[
        ex("¿Qué haces cuando dos fuentes dicen cosas distintas?", "Registro las dos", "No se descarta ninguna."),
        ex("¿Qué anotas siempre?", "Quién lo dijo", "Es la fuente."),
        ex("¿Qué comparas?", "Qué se parece y qué cambia", "Semejanzas y diferencias."),
    ],
    open_task=task(
        "Registra estas dos señales inventadas en dos fichas con señal, significado, fuente y lugar. Señal A: «Cuando florece el árbol del patio, el abuelo Jorge, de la costa, dice que empieza la primavera». Señal B: «Cuando vuelven los pájaros, la tía Ema, del valle, dice que empieza la primavera». Luego escribe una semejanza, una diferencia y una pregunta para cada persona.",
        "Ficha A: árbol florece; empieza la primavera; abuelo Jorge; costa. Ficha B: vuelven los pájaros; empieza la primavera; tía Ema; valle. Semejanza: las dos avisan primavera. Diferencia: la señal. Preguntas: ¿Cómo lo aprendió? ¿Desde cuándo lo observa?",
        ["completa dos fichas", "escribe una semejanza y una diferencia", "escribe preguntas respetuosas", "no dice cuál es la verdadera"],
        ["dos fichas", "comparación"],
        ["decidir cuál es la verdadera", "olvidar la fuente"],
        "Reconoce que registró las dos sin jerarquizar. Los personajes son inventados.",
    ),
    reinforce="Pregunta a dos personas distintas cómo saben que va a llover y anota sus respuestas por separado.",
    extend="Compara tus dos fichas y escribe una pregunta para cada fuente.",
)

register(
    LR02, 5,
    materials="Este cuaderno, lápiz y lápices de colores.",
    use="Aprenderé a crear un recurso pequeño sobre mensajes de la naturaleza, reconociendo a quienes me enseñaron y sin reemplazar a los hablantes. Sirve para aportar a la revitalización con respeto.",
    prior=["Sé registrar una señal con su fuente.", "Sé hacer una tarjeta de palabra."],
    explain=[
        "Un afiche de mensajes de la naturaleza es un cartel con tres señales de tu entorno. Cada señal lleva su dibujo, su significado y el nombre de quien te la contó. Puedes agregar una palabra confirmada, como antü, ko, mapu o kuyen, si la fuente la confirmó. Así el afiche ayuda a recordar sin cambiar nada.",
        "El afiche debe reconocer a todas las personas que ayudaron. Escribe «Señales contadas por» y los nombres, siempre con su permiso. También debes escribir tu nombre como autor o autora. Y agrega una frase que diga: «Este afiche no reemplaza a los hablantes: para aprender bien, escucha a las personas de tu comunidad».",
        "Antes de mostrarlo, revísalo: ¿las palabras confirmadas están bien escritas?, ¿cada señal tiene su fuente?, ¿hay permiso de las personas?, ¿dice que no reemplaza a los hablantes? Muéstralo a quien te enseñó para que lo revise.",
    ],
    vocab=[("afiche", "cartel con imágenes y texto"), ("autoría", "quién hizo el afiche"), ("permiso", "aprobación para usar el nombre o el saber"), ("hablante", "persona que habla una lengua"), ("aportar", "ayudar con algo")],
    worked=[
        {"title": "Armar una señal del afiche", "problem": "Tu mamá te contó que cuando el cielo se pone gris, va a llover. Arma el recuadro del afiche.", "steps": ["Dibujo un cielo gris.", "Escribo el significado: va a llover.", "Escribo la fuente: mamá, con su permiso.", "Agrego «ko» (agua) solo si el educador la confirmó."], "answer": "Recuadro con dibujo de cielo gris, significado «va a llover» y fuente «mamá, con su permiso»"},
        {"title": "Revisión final", "problem": "Tu afiche tiene tres señales y fuentes, pero no dice que no reemplaza a los hablantes. ¿Está listo?", "steps": ["Reviso la lista de cuatro preguntas.", "Falta la frase de no reemplazo.", "Todavía no está listo."], "answer": "No, falta la frase de que no reemplaza a los hablantes"},
    ],
    mistakes=[
        {"wrong": "Poner el nombre de una persona en el afiche sin su permiso.", "why": "Su nombre y su saber son suyos.", "fix": "Pregunta si quiere que aparezca su nombre."},
        {"wrong": "Hacer un afiche con palabras indígenas inventadas.", "why": "Las palabras son de la comunidad.", "fix": "Usa solo palabras confirmadas."},
    ],
    tiers={
        "recovery": [
            ex("Un afiche de mensajes de la naturaleza tiene tres señales. Si cada una tiene su dibujo, ¿cuántos dibujos hay?", "3", "Hay un dibujo por señal."),
            ex("¿Qué escribes junto a cada señal: quién te la contó o el color del papel?", "Quién te la contó", "Es la fuente."),
            ex("¿Qué frase agregas para cuidar la lengua?", "Este afiche no reemplaza a los hablantes", "Reconoce a quienes hablan."),
        ],
        "understand": [
            ex("¿Por qué pides permiso para escribir el nombre de una persona?", "Porque su nombre y su saber son suyos", "Es de ella."),
            ex("¿Por qué solo pones palabras confirmadas?", "Para no inventar ni cambiar la lengua", "La comunidad las confirma."),
            ex("Las cuatro preguntas de revisión son: palabras bien escritas, fuente por señal, permiso y frase de no reemplazo. ¿Cuántas son?", "4", "Se cuentan cuatro."),
        ],
        "apply": [
            ex("Afiche A: tres señales con fuente, permiso y frase. Afiche B: dos señales sin fuente. ¿Cuál está mejor hecho?", "A", "El afiche A cumple todo."),
            arith("Un curso hace 5 afiches con 3 señales cada uno. ¿Cuántas señales hay?", "5*3", "Se suman 3 señales cinco veces."),
            ex("Recuadro: «Señal: nubes grises. Significado: ___. Fuente: papá». Completa el significado.", "lluvia", "Nubes grises avisan lluvia."),
        ],
        "reason": [
            ex("Luis puso en su afiche el nombre de su vecina sin avisarle. ¿Qué debió hacer?", "Pedir permiso", "Su nombre es suyo."),
            ex("Ema dice que su afiche reemplaza a la clase del educador. ¿Qué le dices?", "Que solo es un apoyo", "Los hablantes enseñan mejor."),
        ],
        "challenge": [
            ex("Tres compañeros: Ana usó una palabra confirmada. Beto inventó una palabra. Camila no puso fuente. ¿Quién cuidó mejor la lengua?", "Ana", "Solo ella usó una palabra confirmada."),
            ex("Tu afiche está listo. ¿Qué dos personas lo ven primero: quien te contó la señal y el educador, o solo tus amigos?", "Quien te contó la señal y el educador", "Son las fuentes."),
        ],
    },
    context=[ex("Tu curso hará una exposición. ¿Qué línea escribes al final del afiche para reconocer a la comunidad?", "Señales contadas por... con su permiso", "Reconoce a las fuentes.")],
    selfcheck=[
        ex("¿Qué lleva cada señal del afiche?", "Dibujo, significado y fuente", "Son sus partes."),
        ex("¿Reemplaza un afiche a un hablante?", "No", "Es solo un apoyo."),
        ex("¿Qué haces con el nombre de una persona?", "Pido permiso", "El nombre es suyo."),
    ],
    open_task=task(
        "Haz un afiche con tres señales de tu entorno (por ejemplo: cielo gris avisa lluvia, un árbol florecido avisa primavera, viento frío avisa que baja la temperatura). Para cada una escribe el dibujo, el significado y quién te la contó (con su permiso). Si quieres, agrega una palabra confirmada: antü, ko, mapu o kuyen. Abajo escribe: «Autor/a: tu nombre. Este afiche no reemplaza a los hablantes». Muéstralo a quien te contó las señales.",
        "Afiche: cielo gris — lluvia (mamá); árbol florecido — primavera (abuelo); viento frío — baja la temperatura (tía). Palabra: ko (agua). Autor: yo. Este afiche no reemplaza a los hablantes.",
        ["tres señales con dibujo, significado y fuente", "pide permiso para los nombres", "usa solo palabras confirmadas", "incluye la frase de no reemplazo"],
        ["afiche terminado"],
        ["olvidar la fuente", "inventar palabras", "poner nombres sin permiso"],
        "Reconoce el afiche y que lo mostró a las fuentes. La escritura de las palabras la confirma el educador.",
    ),
    reinforce="Haz un recuadro con una señal que conozcas: dibujo, significado y quién te la contó.",
    extend="Prepara una frase para presentar tu afiche al curso diciendo quién te enseñó.",
)
