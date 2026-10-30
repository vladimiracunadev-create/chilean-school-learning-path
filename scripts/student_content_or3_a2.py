"""Cuaderno del estudiante, 3.º básico Orientación: OA 03 (sexualidad como vínculo, intimidad y origen de la vida) y OA 04 (autocuidado y protección)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA3, OA4 = "OR03 OA 03", "OR03 OA 04"


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 03
lesson(
    OA3, 1,
    "Una hoja y un lápiz. Las tarjetas con situaciones de personajes están escritas en los ejercicios. Nadie tiene que contar nada de su cuerpo ni de su familia.",
    "Aprenderé que la sexualidad es parte de ser persona y que tiene varias dimensiones, no solo el cuerpo. Sirve para entender mejor cómo cuidarnos y respetarnos.",
    ["Sé que mi cuerpo y mis emociones son míos.", "Sé que hay cosas privadas que no tengo que contar."],
    [
        "La sexualidad es una parte de ser persona que existe durante toda la vida. No es solo el cuerpo. Tiene varias dimensiones. La dimensión del cuerpo: cómo somos y cómo lo cuidamos. La dimensión de los afectos: lo que sentimos por otros, como cariño o amistad. La dimensión social: cómo nos relacionamos y qué reglas de respeto usamos. Y la dimensión de los valores: qué decisiones tomamos con cuidado y respeto.",
        "Por ejemplo, aprender a lavarte con cuidado es cuidar tu cuerpo. Querer a un amigo y alegrarte con él es parte de los afectos. Pedir permiso antes de abrazar es respeto en lo social. Decidir no hacer algo que te incomoda es parte de tus valores y de tu libertad.",
        "En esta clase no se cuentan cosas personales. Usamos personajes inventados. Si algo te inquieta o tienes preguntas, puedes hablar con una persona adulta de confianza, de tu casa o de la escuela. Preguntar está bien.",
    ],
    [("sexualidad", "parte de ser persona que incluye cuerpo, afectos, relaciones y valores"), ("dimensión", "una parte o aspecto de algo"), ("afecto", "cariño o sentimiento hacia otros"), ("respeto", "tratar bien a los demás y a mí"), ("íntimo", "muy personal; cada uno decide si lo cuenta")],
    [
        W("Dimensión del cuerpo", "Eli se lava las manos antes de comer y se cepilla los dientes. ¿De qué dimensión se trata?", ["Eli cuida cómo es su cuerpo.", "No habla de sentimientos ni de otros.", "Es la dimensión del cuerpo."], "La dimensión del cuerpo"),
        W("Dimensión de los afectos", "Joaquín se alegra mucho cuando ve a su amigo y le dice que lo quiere. ¿De qué dimensión se trata?", ["Joaquín siente cariño.", "Eso son los afectos.", "No es solo el cuerpo."], "La dimensión de los afectos"),
    ],
    [
        M("Pensar que la sexualidad es solo cómo es el cuerpo.", "Se habla del tema solo con partes del cuerpo.", "También incluye afectos, relaciones respetuosas y valores."),
        M("Creer que tengo que contar cosas mías para participar.", "Pensamos que hay que responder todo.", "Puedes usar personajes y decir «prefiero no contar»."),
    ],
    R=[
        ex("La sexualidad ¿es solo el cuerpo o tiene varias dimensiones?", "Tiene varias dimensiones", "Incluye cuerpo, afectos, relaciones y valores."),
        ex("«Sentir cariño por un amigo» ¿es una dimensión de los afectos o del cuerpo?", "De los afectos", "Es un sentimiento hacia otra persona."),
        ex("Si algo te inquieta, ¿con quién puedes hablar?", "Con una persona adulta de confianza", "Preguntar está bien y alguien puede ayudarte."),
    ],
    U=[
        ex("¿Qué dimensión es «pedir permiso antes de abrazar»: social o del cuerpo?", "Social", "Es una regla de respeto entre personas."),
        ex("Si un compañero te pide que cuentes algo íntimo, ¿estás obligado?", "No", "Lo íntimo se cuenta solo si uno quiere."),
        ex("¿La sexualidad existe solo cuando se es adulto?", "No, existe durante toda la vida", "Es parte de ser persona desde siempre."),
    ],
    A=[
        ex("Rita se ríe y conversa con su abuela, y la quiere mucho. ¿A qué dimensión corresponde?", "A los afectos", "Es cariño hacia otra persona."),
        ex("¿Cómo clasificas «decidir decir que no a algo que me incomoda»: valores, cuerpo o afectos?", "Valores", "Es una decisión tomada con cuidado y respeto."),
        ex("Un niño dice que la sexualidad es «solo anatomía». Escribe una dimensión que le falta nombrar.", "Los afectos, lo social o los valores", "Hay más que el cuerpo."),
    ],
    Z=[
        ex("En un cuento, Mateo cuida su cuerpo, quiere a sus amigos, pide permiso y dice que no cuando algo lo incomoda. ¿Cuántas dimensiones aparecen?", "4", "Cuerpo, afectos, social y valores."),
        ex("Un compañero se burla de otro por sus sentimientos. ¿Está respetando la dimensión social?", "No", "Burlarse no es tratar con respeto."),
    ],
    D=[
        arith("En una lista hay 3 situaciones del cuerpo, 4 de los afectos y 2 sociales. ¿Cuántas situaciones hay en total?", "3+4+2", "Se suman las de cada dimensión."),
        ex("Dos personajes: uno se cuida el cuerpo y no respeta a nadie; otro se cuida y trata con respeto. ¿Cuál vive mejor la sexualidad como parte de ser persona?", "El que se cuida y trata con respeto", "Cuerpo y respeto van juntos."),
    ],
    context=[ex("En clase, la profesora dice: «Hoy hablaremos de sexualidad con personajes inventados». Carlos piensa: «No tengo que contar nada mío». ¿Tiene razón?", "Sí", "Nadie debe contar cosas íntimas.")],
    selfcheck=[ex("En Orientación: ¿la sexualidad incluye los afectos?", "Sí", "Es una de sus dimensiones."), ex("¿Hay que contar cosas íntimas para participar?", "No", "Se puede usar un personaje."), ex("¿Preguntar a un adulto de confianza está bien?", "Sí", "Es una forma de aprender y cuidarse.")],
    task=T("Lee cuatro tarjetas: (1) Ana se cepilla los dientes, (2) Beto abraza a su amigo con permiso, (3) Cata dice «no» a algo que la incomoda, (4) Diego quiere mucho a su perro. Asigna a cada tarjeta una dimensión: cuerpo, afectos, social o valores. Si dudas, explica por qué.", "(1) cuerpo; (2) social (pide permiso); (3) valores; (4) afectos.", ["asigna una dimensión a cada tarjeta", "justifica con una frase", "no cuenta cosas íntimas propias"], ["lista escrita o dibujada"], ["reducir todo a la dimensión del cuerpo", "contar algo personal"], "Reconoce la clasificación y pregunta por qué eligió esa dimensión."),
    reinforce="Escribe una situación de personaje inventado para cada dimensión.",
    extend="Explica con tus palabras por qué la sexualidad no es solo el cuerpo.",
)

lesson(
    OA3, 2,
    "Una hoja y un lápiz. Los casos con personajes inventados están escritos en los ejercicios.",
    "Aprenderé a reconocer vínculos respetuosos de distintos tipos, con cariño y cuidado. Sirve para reconocer cuándo una relación es buena para mí.",
    ["Sé que hay afectos y relaciones.", "Sé que merezco respeto."],
    [
        "Un vínculo es la unión afectiva entre personas. Hay muchos vínculos: amistad, familia, vecinos, compañeros. Las familias son diversas. Hay familias con una persona adulta, con dos o con más; con abuelos, tíos, madres, padres o personas que adoptan. Ninguna es mejor que otra, y no hay que suponer cómo es la de otra persona.",
        "Un vínculo es respetuoso cuando hay cuidado, escucha y libertad. La gente se trata bien, acepta un «no», y nadie hace sentir miedo. También hay amor entre dos personas adultas, que es compromiso, cuidado y respeto mutuo. El amor no es control, no es dañar ni obligar a otro.",
        "Algunas señales dicen que un vínculo no es respetuoso: gritos y burlas, amenazas, esconder cosas o forzar. Si algo así pasa, no es tu culpa. Cuéntalo a una persona adulta de confianza.",
    ],
    [("vínculo", "unión afectiva entre personas"), ("familia", "grupo de personas que se cuidan y se quieren"), ("diverso", "distinto; de muchas formas"), ("amor", "cuidado y respeto hacia otra persona"), ("mutuo", "de los dos lados")],
    [
        W("Vínculo respetuoso", "Rosa y Lalo son amigos. Se escuchan, se turnan y, cuando uno dice «no quiero», el otro respeta. ¿Es un vínculo respetuoso?", ["Se escuchan.", "Respetan el «no».", "Ninguno hace sentir miedo."], "Sí, es un vínculo respetuoso"),
        W("Señal de alerta", "Un niño le dice a otro: «Si no haces lo que digo, no serás mi amigo, y no se lo cuentes a nadie». ¿Es un vínculo respetuoso?", ["Hay una amenaza.", "Le pide esconder algo.", "El amigo no es libre. No es respetuoso."], "No, no es respetuoso"),
    ],
    [
        M("Pensar que hay una familia mejor que otras.", "Se mira solo la familia que uno conoce.", "Las familias son distintas y todas merecen respeto."),
        M("Creer que amar es mandar o controlar a otro.", "Se mezclan el cariño y el control.", "Amar es cuidar y respetar la libertad del otro."),
    ],
    R=[
        ex("¿Un vínculo respetuoso incluye aceptar un «no»?", "Sí", "Respetar la libertad del otro es parte del cuidado."),
        ex("¿Hay familias con una persona adulta y otras con dos o más?", "Sí", "Las familias son diversas."),
        ex("Si alguien te hace sentir miedo en una relación, ¿es tu culpa?", "No", "El miedo no es culpa de quien lo siente."),
    ],
    U=[
        ex("¿Por qué no se debe decir que una familia es mejor que otra?", "Porque las familias son diversas y todas merecen respeto", "Cada familia cuida a su manera."),
        ex("¿El amor entre personas incluye el control?", "No", "El amor es cuidado y respeto, no mando."),
        ex("Si en un vínculo hay burlas y amenazas, ¿qué conviene hacer?", "Contarlo a un adulto de confianza", "No tienes que resolverlo solo."),
    ],
    A=[
        ex("Camila vive con su abuela y su tío. Una compañera dice que la familia de Camila «no es de verdad». ¿Qué le responderías?", "Que las familias son distintas y todas son de verdad", "Cada familia tiene derecho a ser respetada."),
        ex("Eli pide permiso para abrazar a una amiga y ella dice «hoy no». Eli dice «bueno». ¿Fue un vínculo respetuoso?", "Sí", "Aceptó el «no» sin enojarse."),
        ex("Escribe una señal que muestra que un vínculo es respetuoso.", "Escucharse, aceptar el «no» o cuidar al otro", "Son señales de respeto."),
    ],
    Z=[
        ex("Un niño dice: «Mi amigo me pegó, pero lo hace porque me quiere». ¿Eso es cuidado?", "No", "Pegar daña y no es una forma de querer."),
        ex("Una niña dice: «Mi vecina vive sola y la quiero mucho; es parte de mi comunidad». ¿Eso es un vínculo?", "Sí", "Hay afecto y cuidado entre personas."),
    ],
    D=[
        arith("En una exposición sobre vínculos hay 8 dibujos de amistades, 14 de familias y 6 de vecinos y compañeros. ¿Cuántos dibujos hay en total?", "8+14+6", "Se suman los dibujos de cada grupo; todos los vínculos valen."),
        ex("Un cuento muestra a dos personas adultas que se cuidan y se respetan. Otro, a dos que se gritan y se controlan. ¿En cuál hay amor como cuidado y respeto?", "En el primero", "Cuidar y respetar es la base de un vínculo."),
    ],
    context=[ex("Un día se pide dibujar a la familia. Un niño dibuja a sus abuelos y a su perro. Otro dice: «Esa no es una familia». La profesora dice: «Las familias son distintas». ¿Tiene razón?", "Sí", "No hay una sola forma de familia.")],
    selfcheck=[ex("En Orientación: ¿las familias son todas iguales?", "No", "Las familias son muy diversas."), ex("¿Se puede obligar a alguien a demostrar cariño?", "No", "El cariño se da con libertad."), ex("¿Aceptar un «no» es parte del respeto?", "Sí", "Respeta la libertad.")],
    task=T("Lee tres vínculos de personajes: (A) dos amigas se escuchan y se turnan; (B) un niño amenaza a otro para que no hable; (C) una abuela y su nieto se cuidan y se quieren. Marca cuál o cuáles son respetuosos y explica con una señal. Después escribe una frase que respete a todas las familias.", "A y C son respetuosos: se escuchan y se cuidan. B no, porque hay amenaza. Frase: «Todas las familias merecen respeto».", ["identifica los vínculos respetuosos", "nombra la señal", "no jerarquiza familias"], ["respuesta escrita"], ["decir que una familia es mejor", "confundir control con amor"], "Reconoce las señales y revisa que la frase sobre familias no jerarquice."),
    reinforce="Escribe tres señales de un vínculo respetuoso.",
    extend="Explica por qué «lo hago porque te quiero» no justifica dañar a alguien.",
)

lesson(
    OA3, 3,
    "Una hoja y un lápiz. Las tarjetas están escritas en los ejercicios. Puedes dibujar una silueta sin detalles o no dibujar.",
    "Aprenderé qué es la intimidad, el consentimiento y los límites. Sirve para decir «no» cuando algo me incomoda y respetar el «no» de otros.",
    ["Sé que mi cuerpo es mío.", "Sé que un vínculo respetuoso acepta un «no»."],
    [
        "La intimidad es lo que es muy personal. Las partes íntimas del cuerpo son las que cubren la ropa interior o el traje de baño. Son privadas. Nadie debe pedirte que las muestres. Nadie debe mirarlas, tocarlas ni sacarles fotos. La única excepción son los cuidados de salud, como una revisión médica, que se hacen con una persona de confianza presente. Esto vale para personas desconocidas y también para personas que conoces.",
        "El consentimiento es decir «sí» o «no» con libertad. Un «no» se respeta siempre y no hay que dar explicaciones. Un «sí» dicho por miedo o presión no es un permiso. Tú puedes cambiar de idea. Y debes respetar el «no» de los demás.",
        "Si alguien te mira, te toca o te pide algo que te incomoda, parar, alejarte y contárselo a un adulto de confianza es lo correcto. Los secretos que incomodan no se guardan. No es tu culpa, y avisar no es acusar. Una sorpresa de cumpleaños sí se puede guardar, porque pronto se cuenta y alegra a todos.",
    ],
    [("intimidad", "lo muy personal y privado"), ("consentimiento", "decir sí o no con libertad"), ("límite", "lo que no acepto o no acepto hacer"), ("privado", "que no se comparte sin mi permiso"), ("presión", "insistir para que alguien diga que sí")],
    [
        W("Respetar el no", "Tomás quiere abrazar a su prima, pero ella dice «hoy prefiero no». ¿Qué debe hacer Tomás?", ["Ella dijo «no».", "El «no» se respeta siempre.", "Puede ofrecer un saludo con la mano."], "Aceptar el no y no insistir"),
        W("Sorpresa o secreto", "Un niño te cuenta: «Un chico mayor me mostró algo que me asustó y me pidió que no lo cuente». ¿Ese secreto se debe guardar?", ["Dio miedo.", "Esconder algo que incomoda no es una sorpresa.", "Hay que contárselo a un adulto de confianza."], "No, hay que contárselo a un adulto de confianza"),
    ],
    [
        M("Pensar que un adulto conocido siempre tiene permiso de tocar mi cuerpo.", "Se confunde confianza con permiso.", "Mi cuerpo es mío: puedo decir no incluso a personas que conozco."),
        M("Guardar un secreto que me incomoda porque me lo pidieron.", "Se piensa que contarlo es acusar.", "Los secretos que incomodan se cuentan. Avisar no es acusar."),
    ],
    R=[
        ex("¿Las partes íntimas son las que cubre la ropa interior o el traje de baño?", "Sí", "Por eso son privadas."),
        ex("¿Un «no» se respeta siempre?", "Sí", "Es parte del consentimiento."),
        ex("Un secreto que te incomoda, ¿se guarda o se cuenta a un adulto de confianza?", "Se cuenta a un adulto de confianza", "Callar puede dejar a alguien sin ayuda."),
    ],
    U=[
        ex("En Orientación: ¿Qué es el consentimiento?", "Decir sí o no con libertad", "Un sí por miedo no vale."),
        ex("¿Puedes cambiar de idea después de decir «sí»?", "Sí", "Tienes derecho a cambiar de idea."),
        ex("Si te piden una foto íntima, ¿qué haces?", "Digo no, me alejo y se lo cuento a un adulto de confianza", "Nadie debe pedirla y es importante avisar."),
    ],
    A=[
        ex("Pía no quiere dar un beso de despedida y se siente presionada. Escribe una frase para decir «no» con cortesía.", "Hoy prefiero saludar con la mano", "Dice el límite con respeto."),
        ex("Rafa dice «sí» solo porque le dan miedo las amenazas de un compañero. ¿Eso es consentimiento?", "No", "Un sí por miedo no es libre."),
        ex("¿Cuál se puede guardar: «la sorpresa de cumpleaños de mi amigo» o «lo que me hizo un adulto y me pidió callar»?", "La sorpresa de cumpleaños de mi amigo", "Alegra a todos y se cuenta pronto."),
    ],
    Z=[
        ex("Un niño dice: «Si es un familiar, no puedo decirle que no». ¿Es cierto?", "No", "Mi cuerpo es mío incluso con personas conocidas."),
        ex("Un amigo te dice: «No cuentes esto o me meto en problemas». Es algo que te incomodó. ¿Qué es más importante: callar para no acusarlo o cuidarte?", "Cuidarte contándolo a un adulto de confianza", "Avisar no es acusar; es pedir ayuda."),
    ],
    D=[
        arith("En una tarjeta hay 12 situaciones. 7 son un «sí» libre y el resto son un «no» o presión. ¿Cuántas son «no» o presión?", "12-7", "Se resta lo libre al total."),
        ex("Si una persona te pide algo y dice «es nuestro secreto, no le cuentes a nadie», ¿qué señal de alerta es?", "Que me pide esconder algo a los adultos", "Los secretos que se piden esconder a los adultos de confianza no se guardan."),
    ],
    context=[ex("En un cumpleaños, un tío insiste a Vero para que se siente en sus piernas, aunque ella dijo que no. Vero se levanta y se lo cuenta a otro adulto de confianza. ¿Hizo bien?", "Sí", "Dijo no, se alejó y avisó; eso la cuida.")],
    selfcheck=[ex("En Orientación: ¿un amigo o un adulto puede pedirte que le muestres tus partes íntimas?", "No", "Esas partes son privadas y nadie debe pedirlo."), ex("¿Avisar a un adulto de confianza es acusar?", "No", "Es pedir ayuda y cuidarte."), ex("¿Es mi culpa si me presionan?", "No", "Quien presiona es responsable.")],
    task=T("Lee tres tarjetas: (1) un compañero te pide que no cuentes algo que te asustó; (2) tus amigos preparan una sorpresa de cumpleaños; (3) alguien insiste en abrazarte aunque dijiste que no. Para cada una escribe: ¿se guarda o se cuenta?, y a quién le contarías. Si prefieres, usa un personaje.", "(1) se cuenta; a un adulto de confianza. (2) se guarda: es sorpresa. (3) digo no, me alejo y se cuenta.", ["distingue sorpresa y secreto que incomoda", "nombra un adulto de confianza", "no cuenta experiencias personales"], ["respuesta escrita o dibujada"], ["guardar secretos que incomodan", "culparse"], "Reconoce que contar no es acusar y revisa que nombre a alguien de confianza."),
    reinforce="Escribe una frase para decir «no» con respeto y otra para aceptar el «no» de otro.",
    extend="Haz una lista de dos personas adultas de confianza (por ejemplo, de la escuela o del hogar) a quienes podrías contar algo que te incomode, sin escribir nombres.",
)

lesson(
    OA3, 4,
    "Una hoja y un lápiz. Las tarjetas están escritas en los ejercicios. Las preguntas pueden entregarse por escrito en privado.",
    "Aprenderé, con palabras sencillas, cómo comienza la vida de una persona. Sirve para entender de dónde venimos y respetar las historias distintas de cada familia.",
    ["Sé que mi cuerpo es privado.", "Sé que las familias son diversas."],
    [
        "Todas las personas comienzan su vida de la misma forma. Una célula es una parte muy pequeña, que no se ve a simple vista, de la que está hecho el cuerpo. Una célula de una mujer, llamada óvulo, y una célula de un hombre, llamada espermatozoide, se unen. Esa unión forma una nueva célula que comienza a crecer. Así empieza el origen de la vida de una persona.",
        "El bebé crece durante unos nueve meses dentro del útero, un lugar del cuerpo de la mujer que lo cuida. Después nace. Cada familia puede contar su historia de forma distinta. Algunos niños y niñas viven con quienes los vieron nacer y otros llegaron a su familia por adopción. Todos son queridos y merecen cuidado.",
        "Los detalles se conversan con personas adultas de confianza, a la manera de cada familia y cuando estés listo. Si tienes preguntas, puedes hacerlas a un adulto de tu casa o de la escuela. Está bien preguntar, y también está bien no querer saber más por ahora. Cada persona es única y, al crecer, va tomando decisiones sobre su propia vida y aprende a cuidarla.",
    ],
    [("origen de la vida", "cómo comienza la vida de una persona"), ("célula", "parte muy pequeña de la que está hecho el cuerpo"), ("óvulo", "célula de una mujer que participa en el inicio de una vida"), ("espermatozoide", "célula de un hombre que participa en el inicio de una vida"), ("útero", "lugar del cuerpo de la mujer donde crece el bebé"), ("adopción", "cuando una familia recibe a un niño o niña para cuidarlo como hijo o hija")],
    [
        W("Dos células", "¿Qué dos células se unen para empezar la vida de una persona?", ["Una viene de una mujer: el óvulo.", "La otra viene de un hombre: el espermatozoide.", "Al unirse forman una nueva célula."], "El óvulo y el espermatozoide"),
        W("Tiempo de crecimiento", "Un bebé crece unos 9 meses en el útero. Han pasado 4 meses. ¿Cuántos meses faltan?", ["El total es 9 meses.", "Han pasado 4.", "Se calcula 9 menos 4."], "5 meses"),
    ],
    [
        M("Pensar que hay una sola forma de llegar a una familia.", "Se conoce una sola historia.", "Hay nacimientos y adopciones; todos son queridos."),
        M("Hacer bromas o burlas sobre cómo nace un bebé.", "El tema da vergüenza o risa nerviosa.", "Es un tema serio; pregunta con respeto a un adulto de confianza."),
    ],
    R=[
        ex("¿Cómo se llama la célula de una mujer que participa en el inicio de la vida?", "Óvulo", "Es la célula femenina."),
        ex("¿Cómo se llama la célula de un hombre que participa en el inicio de la vida?", "Espermatozoide", "Es la célula masculina."),
        ex("¿Dónde crece el bebé durante unos nueve meses?", "En el útero", "Es el lugar del cuerpo de la mujer que lo cuida."),
    ],
    U=[
        ex("¿Por qué no se hacen burlas sobre el origen de la vida?", "Porque es un tema serio que se trata con respeto", "Las burlas pueden herir a otros."),
        ex("Una compañera fue adoptada. ¿Es menos querida?", "No", "Todas las historias merecen cuidado."),
        ex("Si tienes preguntas, ¿a quién puedes hacerlas?", "A un adulto de confianza", "Esa persona puede explicar con cuidado."),
    ],
    A=[
        arith("Un bebé tarda 9 meses en crecer. Si ya pasaron 6 meses, ¿cuántos faltan?", "9-6", "Se resta lo que pasó al total."),
        ex("Escribe con tus palabras qué se une para empezar una vida.", "Una célula de una mujer y una célula de un hombre", "Son el óvulo y el espermatozoide."),
        ex("Un amigo se ríe de este tema. ¿Qué le dices con respeto?", "Que es un tema serio y se habla con respeto", "Pide cuidado sin burlarse."),
    ],
    Z=[
        ex("Dos niñas cuentan su historia: una nació en una casa con su abuela y otra fue adoptada. ¿Cuál es «la verdadera» forma de comenzar una familia?", "Ninguna es más verdadera; ambas son familias", "Las familias llegan de formas distintas."),
        ex("Un niño dice: «No quiero saber más por ahora». ¿Se puede respetar eso?", "Sí", "Cada persona decide cuándo está lista para saber más."),
    ],
    D=[
        ex("Una niña dice: «Mi vida es única y, al crecer, iré decidiendo cómo cuidarla». ¿Es una idea correcta?", "Sí", "Cada persona es única y, con ayuda de adultos, aprende a decidir sobre su propia vida."),
        ex("¿Es correcto que cada familia cuente su historia a su manera y que en la escuela se enseñe lo general?", "Sí", "La escuela enseña lo común y la familia cuenta su historia."),
    ],
    context=[ex("Un niño pregunta en voz alta algo que le da vergüenza. La profesora dice: «Puedes preguntarlo por escrito o a una persona adulta de confianza». ¿Es una buena respuesta?", "Sí", "Respeta su privacidad y le da una forma de preguntar.")],
    selfcheck=[ex("En Orientación: ¿la vida de toda persona comienza con dos células que se unen?", "Sí", "Un óvulo y un espermatozoide."), ex("¿Hay familias que llegan por adopción?", "Sí", "Todas son familias."), ex("¿Se puede preguntar a un adulto de confianza?", "Sí", "Preguntar está bien.")],
    task=T("Escribe o dibuja, en tres pasos y en privado, cómo comienza la vida de una persona, usando: óvulo, espermatozoide, útero y unos nueve meses. Después escribe una frase que respete a las familias que llegaron por adopción.", "1) un óvulo y un espermatozoide se unen. 2) crece en el útero. 3) tras unos nueve meses nace. Frase: «Las familias que adoptan también se quieren».", ["usa las palabras nuevas con sentido", "los tres pasos están en orden", "la frase respeta todas las historias"], ["escrito o dibujo sin detalles"], ["hacer bromas", "decir que hay una forma «verdadera» de ser familia"], "Reconoce el orden y revisa que el lenguaje sea respetuoso."),
    reinforce="Escribe una pregunta que le harías a un adulto de confianza sobre este tema.",
    extend="Escribe cómo explicarías este tema a un niño más pequeño usando solo palabras simples.",
)

# ================================================================ OA 04
lesson(
    OA4, 1,
    "Una hoja y un lápiz. Los horarios y las tablas están escritos en los ejercicios. Cada casa tiene sus propios recursos; no se pregunta cómo es la tuya.",
    "Aprenderé a armar rutinas de higiene flexibles que puedo hacer con lo que tengo. Sirve para cuidar mi cuerpo y sentirme bien.",
    ["Sé lavarme las manos.", "Sé que cuidar mi cuerpo es importante."],
    [
        "La higiene son las acciones con que cuidamos nuestro cuerpo y nuestra salud: lavarnos las manos con agua y jabón, cepillarnos los dientes, bañarnos o asearnos, usar ropa limpia. Una rutina es una secuencia de acciones que repites a ciertas horas. Así se vuelve un hábito y cuesta menos.",
        "Las manos se lavan antes de comer, después de ir al baño y cuando están sucias, frotando unos 20 segundos con jabón. Los dientes se cepillan al menos dos veces al día. Una rutina puede cambiar según tu casa, tu horario o lo que tengas. Si te falta jabón, cepillo o agua, no es tu culpa: puedes decírselo a un adulto de confianza.",
        "Una rutina flexible tiene un plan y una alternativa. Por ejemplo: «Me cepillo los dientes antes de acostarme. Si olvido, lo hago al levantarme». Así no abandonas el hábito por un tropiezo.",
    ],
    [("higiene", "acciones para cuidar mi cuerpo y mi salud"), ("rutina", "acciones que repito a ciertas horas"), ("hábito", "acción que ya hago casi sin pensar"), ("flexible", "que se puede ajustar"), ("alternativa", "otra opción por si no resulta la primera")],
    [
        W("Armar una rutina", "Nico quiere una rutina para la noche con: cepillarse los dientes, lavarse la cara y acostarse. ¿Qué acción va al final?", ["Los dientes y la cara se pueden hacer en cualquier orden.", "Acostarse es lo último de la noche.", "Va al final: acostarse."], "Acostarse"),
        W("Tiempo de lavado", "Lola se lava las manos frotando 20 segundos. Lo hace 3 veces al día. ¿Cuántos segundos frota en total?", ["Cada vez son 20 segundos.", "Son 3 veces.", "Se multiplica 20 por 3."], "60 segundos"),
    ],
    [
        M("Dejar mi rutina por un día en que no pude hacerla.", "Se cree que, si falló una vez, ya no sirve.", "Usa la alternativa y sigue al día siguiente."),
        M("Sentir culpa porque en mi casa me falta algo para la higiene.", "Se piensa que es mi responsabilidad conseguirlo.", "No es tu culpa; puedes pedir ayuda a un adulto de confianza."),
    ],
    R=[
        ex("¿Las manos se lavan con agua y jabón?", "Sí", "El jabón ayuda a sacar la suciedad."),
        ex("¿Una rutina es algo que repito a ciertas horas?", "Sí", "Así se vuelve un hábito."),
        ex("Si te falta jabón, ¿es tu culpa?", "No", "Los recursos dependen de los adultos y del hogar."),
    ],
    U=[
        ex("¿Qué tiene una rutina flexible además del plan?", "Una alternativa", "Sirve cuando no sale como lo pensaste."),
        ex("¿Cuándo conviene lavarse las manos: antes de comer o solo al terminar?", "Antes de comer", "Evita llevar suciedad a la boca."),
        ex("¿Cuántas veces al día conviene cepillarse los dientes, al menos?", "Dos", "Ayuda a mantener los dientes limpios."),
    ],
    A=[
        arith("Una niña se cepilla los dientes 2 veces al día durante 7 días. ¿Cuántas veces se cepilla?", "2*7", "Se repite dos veces siete días."),
        ex("Escribe una alternativa para «me cepillo los dientes antes de dormir», por si olvidas.", "Me cepillo al levantarme", "Así no pierdes el hábito."),
        ex("Ordena: «lavarse las manos», «sentarse a comer». ¿Cuál va primero?", "Lavarse las manos", "Se lavan antes de comer."),
    ],
    Z=[
        ex("Un niño dice que no se lava las manos porque «le da lata». ¿Qué le ayuda más: culparlo o proponer una rutina con un recordatorio?", "Una rutina con un recordatorio", "Los hábitos se aprenden con apoyo."),
        ex("En una casa no hay ducha caliente. ¿Se puede asear igual con lo que hay y avisar a un adulto?", "Sí", "La higiene puede adaptarse a cada casa."),
    ],
    D=[
        arith("Una rutina de la mañana: lavarse la cara 3 minutos, cepillarse los dientes 3 minutos y vestirse 10 minutos. ¿Cuántos minutos dura?", "3+3+10", "Se suman las tres acciones."),
        ex("Una rutina dice: «hago A, y si no puedo, hago B». ¿Cómo se llama B?", "Alternativa", "Es otra opción para no perder el hábito."),
    ],
    context=[ex("Al volver del recreo, la profesora dice que todos se laven las manos antes de la colación. Tomás se las lava con jabón y las seca. ¿Cuidó su higiene?", "Sí", "Se lavó con agua y jabón antes de comer.")],
    selfcheck=[ex("En Orientación: ¿una rutina puede ajustarse a cada casa?", "Sí", "Una rutina flexible se ajusta."), ex("¿Es mi culpa si me falta algo para la higiene?", "No", "Puedo pedir ayuda."), ex("¿Las manos se lavan con jabón?", "Sí", "Así se quita mejor la suciedad.")],
    task=T("Arma tu rutina para la noche con tres acciones de esta lista: lavarme los dientes, lavarme las manos, lavarme la cara, preparar la ropa de mañana, ordenar mi mochila. Escribe el orden, una alternativa por si no puedes y a quién pedirías ayuda si te falta algo.", "Rutina: ordenar mi mochila, lavarme los dientes, preparar la ropa. Alternativa: si olvido, lo hago por la mañana. Pido ayuda a un adulto de mi casa.", ["tres acciones en orden", "una alternativa", "no hay culpa por recursos"], ["rutina escrita o dibujada"], ["rutina rígida", "sentir culpa por lo que falta"], "Reconoce la rutina y verifica que tenga alternativa."),
    reinforce="Escribe tu rutina de la mañana en tres pasos.",
    extend="Agrega a tu rutina un recordatorio que te ayude a no olvidarla.",
)

lesson(
    OA4, 2,
    "Una hoja y un lápiz. Los horarios y las listas de actividades están escritos en los ejercicios.",
    "Aprenderé a equilibrar descanso, juego y actividad física en mi día. Sirve para tener energía y sentirme bien.",
    ["Sé que dormir es importante.", "Sé jugar y moverme."],
    [
        "El cuerpo necesita descanso, juego y movimiento. Los niños y niñas de tu edad suelen necesitar entre 9 y 11 horas de sueño por noche. Dormir bien ayuda a aprender, a regular las emociones y a crecer. Para dormir mejor, es bueno acostarse a horas parecidas y apagar las pantallas un rato antes.",
        "El movimiento es cualquier actividad que hace trabajar al cuerpo: correr, bailar, saltar, caminar, jugar a la pelota. Se recomienda sumar unos 60 minutos de movimiento al día, en partes pequeñas. Contando recreos, clases de educación física y juegos, se puede lograr.",
        "La recreación es lo que haces para divertirte: jugar, dibujar, leer, escuchar música. Un buen día mezcla estudio, juego, movimiento y descanso. Si tu casa o tu barrio tienen poco espacio, puedes moverte igual con juegos sencillos. No es tu culpa si algunos días no se puede.",
    ],
    [("descanso", "tiempo para dormir o estar tranquilo"), ("recreación", "actividades para divertirme"), ("actividad física", "movimiento que hace trabajar el cuerpo"), ("equilibrar", "dar a cada cosa su lugar en el día"), ("pantalla", "aparato con imagen, como televisor o tablet")],
    [
        W("Horas de sueño", "Beto se acuesta a las 21:00 y se levanta a las 7:00. ¿Cuántas horas durmió?", ["De las 21:00 a las 24:00 hay 3 horas.", "De las 0:00 a las 7:00 hay 7 horas.", "Se suman 3 más 7."], "10 horas"),
        W("Minutos de movimiento", "Ema se movió 20 minutos en el recreo, 25 en educación física y 15 jugando en la tarde. ¿Cuántos minutos se movió?", ["Se suman los tres tiempos.", "20 más 25 es 45.", "45 más 15 es 60."], "60 minutos"),
    ],
    [
        M("Pensar que dormir poco es bueno porque así se aprovecha más el día.", "Parece que se gana tiempo.", "Dormir bien da energía para aprender y jugar."),
        M("Creer que solo cuenta el deporte organizado como actividad física.", "Se olvida que jugar y caminar también cuentan.", "Todo movimiento suma."),
    ],
    R=[
        ex("¿Dormir ayuda a aprender y crecer?", "Sí", "El cuerpo y la mente descansan."),
        ex("Bailar en tu casa, ¿es actividad física?", "Sí", "Hace trabajar el cuerpo."),
        ex("¿Jugar y dibujar son recreación?", "Sí", "Son actividades para divertirse."),
    ],
    U=[
        ex("¿Qué conviene hacer un rato antes de dormir con las pantallas?", "Apagarlas", "Ayuda a dormir mejor."),
        ex("¿Cuántos minutos al día de movimiento se recomienda, en partes?", "Unos 60", "Se pueden sumar varias actividades."),
        ex("Si un día no puedes moverte mucho, ¿es tu culpa?", "No", "No siempre se puede."),
    ],
    A=[
        arith("Si Laura camina 15 minutos a la escuela y 15 minutos de vuelta, ¿cuántos minutos camina?", "15+15", "Se suman ida y vuelta."),
        arith("Pedro necesita 60 minutos de movimiento y ya hizo 35. ¿Cuántos le faltan?", "60-35", "Se resta lo hecho al total."),
        ex("Escribe una actividad de recreación que se pueda hacer en casa con poco espacio.", "Dibujar, leer o armar un rompecabezas", "No necesita mucho espacio."),
    ],
    Z=[
        ex("Dos niños: uno duerme 10 horas y otro 6. ¿Cuál tendrá más energía para aprender?", "El que duerme 10 horas", "Dormir lo necesario ayuda a estar atento."),
        ex("Un niño dice «yo solo juego pantallas, no necesito moverme». ¿Qué le falta a su día?", "Movimiento", "El cuerpo necesita moverse."),
    ],
    D=[
        arith("Una semana tiene 7 noches. Si Rosa duerme 10 horas cada noche, ¿cuántas horas duerme en la semana?", "10*7", "Se repite 10 horas siete noches."),
        ex("En un día: 10 horas de sueño, 6 de clases, 2 de movimiento, 2 de juego y el resto de otras cosas. ¿Se parece a un día equilibrado?", "Sí", "Hay descanso, estudio, movimiento y juego."),
    ],
    context=[ex("En el recreo de 20 minutos, Camila juega a la pelota con sus compañeros. Después, en su casa, camina un rato con una persona adulta. ¿Está sumando minutos de movimiento?", "Sí", "Jugar y caminar son actividad física.")],
    selfcheck=[ex("En Orientación: ¿dormir poco ayuda a estar más atento?", "No", "El sueño ayuda a aprender."), ex("¿Jugar cuenta como movimiento?", "Sí", "Si mueve el cuerpo, cuenta."), ex("¿Hay que equilibrar descanso, juego y actividad?", "Sí", "El cuerpo necesita todo.")],
    task=T("Arma un día equilibrado con estas partes: clases (6 horas), dormir (10 horas), juego, movimiento y comer. Escribe cuántas horas darías a cada parte para que sumen 24 horas, o ordénalas en una línea del día. Puedes cambiar el tiempo del juego y del movimiento.", "Dormir 10, clases 6, comer y asearme 3, movimiento 2, juego 3: suman 24.", ["usa dormir y clases dados", "la suma da 24 horas", "incluye juego y movimiento"], ["plan escrito o dibujado"], ["dejar fuera el descanso", "sumar mal"], "Reconoce el equilibrio y revisa la suma."),
    reinforce="Anota cuántas horas dormiste anoche y qué movimiento hiciste hoy.",
    extend="Propón tres juegos de movimiento para hacer con poco espacio.",
)

lesson(
    OA4, 3,
    "Una hoja y un lápiz. Los platos y menús de ejemplo están escritos en los ejercicios. No se pregunta qué comes en tu casa.",
    "Aprenderé a cuidar mi alimentación con variedad, atendiendo al hambre y sin culpa ni control del cuerpo. Sirve para tener energía y disfrutar la comida.",
    ["Sé que comer me da energía.", "Sé que tengo hambre y saciedad."],
    [
        "Comer nos da energía para jugar, aprender y crecer. Una alimentación variada incluye frutas, verduras, legumbres, cereales como pan, arroz o pasta, lácteos, huevos, pescado o carnes, y agua. No hace falta que todo esté en cada comida. Se mira lo que comes a lo largo de varios días.",
        "El cuerpo avisa cuando tiene hambre y cuando está satisfecho. Escuchar esas señales ayuda a cuidarte. Comer algo rico, como un dulce en una fiesta, no es algo malo ni te hace una mala persona. Las comidas no son buenas o malas moralmente. Algunas se comen más seguido y otras de vez en cuando.",
        "Cada casa tiene recursos distintos y los niños no deciden qué se compra. Si a veces no hay lo que quisieras, no es tu culpa. Tampoco hay que hablar de pesos, dietas ni de cómo se ve el cuerpo de otros. Si tienes dudas o te preocupa tu forma de comer, conversa con un adulto de confianza.",
    ],
    [("alimentación", "lo que comemos y bebemos"), ("variedad", "tener cosas distintas"), ("hambre", "señal del cuerpo de que necesita comer"), ("saciedad", "sensación de estar satisfecho"), ("energía", "fuerza para moverme y pensar")],
    [
        W("Plato variado", "Un plato tiene arroz, ensalada de tomate y lechuga, y lentejas. ¿Tiene variedad?", ["Hay un cereal: arroz.", "Hay verduras: tomate y lechuga.", "Hay legumbres: lentejas."], "Sí, tiene variedad"),
        W("Señales del cuerpo", "Tomás dice que ya no tiene hambre y deja un poco de pan. ¿Qué señal escuchó?", ["Su cuerpo avisó que estaba satisfecho.", "Escuchar esa señal cuida su cuerpo.", "Eso se llama saciedad."], "La saciedad"),
    ],
    [
        M("Decir que un alimento es «malo» y quien lo come, también.", "Se mezcla la comida con juicios sobre las personas.", "Los alimentos se comen más o menos seguido, sin culpa."),
        M("Hablar de pesos o criticar el cuerpo de otros por lo que comen.", "Se cree que es una forma de cuidarse.", "Cuidarse es comer variado y escuchar al cuerpo, sin burlas."),
    ],
    R=[
        ex("¿Beber agua es parte de cuidar la alimentación?", "Sí", "El cuerpo necesita agua."),
        ex("¿La saciedad es la señal de estar satisfecho?", "Sí", "El cuerpo avisa que ya comió suficiente."),
        ex("¿Una persona es mala porque comió un dulce en una fiesta?", "No", "Los alimentos no hacen buenas o malas a las personas."),
    ],
    U=[
        ex("¿Qué es una alimentación con variedad?", "La que incluye alimentos distintos", "Ayuda a tener energía."),
        ex("Si a veces no hay lo que quisieras comer, ¿es tu culpa?", "No", "Los recursos dependen del hogar."),
        ex("¿Se debe criticar el cuerpo de otros por lo que comen?", "No", "Es una falta de respeto."),
    ],
    A=[
        ex("Un plato tiene pan, queso y manzana. ¿En qué grupo está el queso: lácteos o verduras?", "Lácteos", "El queso viene de la leche."),
        arith("Beto tomó 2 vasos de agua en la mañana, 3 en la tarde y 1 en la noche. ¿Cuántos vasos tomó?", "2+3+1", "Se suman los vasos de cada momento."),
        ex("Rita dice «tengo hambre» a media mañana. ¿Escuchar su hambre es cuidarse?", "Sí", "Atender las señales del cuerpo ayuda."),
    ],
    Z=[
        ex("Un compañero se burla porque otro llevó una fruta y no un dulce. ¿Cuál es el problema?", "La burla, porque cada uno come lo que tiene", "No se juzga a las personas por su comida."),
        ex("Una niña dice «hoy no comí verduras, soy mala». ¿Tiene razón?", "No", "Los alimentos se miran en varios días y no hay culpa."),
    ],
    D=[
        arith("En un curso de 28 niños, 19 llevaron fruta a la colación y el resto llevó otra cosa. ¿Cuántos llevaron otra cosa?", "28-19", "Se resta lo de fruta al total."),
        ex("Un niño quiere dejar de comer pan porque otro le habló de peso. ¿A quién conviene contar esto?", "A un adulto de confianza", "Ese adulto puede ayudar a cuidar su forma de comer."),
    ],
    context=[ex("En el almuerzo, Matías come lentejas con arroz y, de postre, un yogur. Dice «ya estoy lleno» y se detiene. ¿Escuchó a su cuerpo?", "Sí", "Dejó de comer al sentirse satisfecho.")],
    selfcheck=[ex("En Orientación: ¿hay alimentos «buenos» que hacen buena a una persona?", "No", "Los alimentos no juzgan a las personas."), ex("¿Se puede escuchar al cuerpo para saber si tengo hambre?", "Sí", "Es una señal útil."), ex("¿Es culpa mía lo que hay en mi casa para comer?", "No", "Los niños no deciden las compras.")],
    task=T("Mira esta lista: pan, lentejas, manzana, queso, arroz, ensalada, agua, huevo. Arma un plato o un día de comida con variedad, usando al menos cuatro de la lista. Escribe cómo sabrás si tienes hambre o estás satisfecho. No hace falta decir qué comes en tu casa.", "Plato: lentejas, arroz, ensalada y agua. Sé que estoy satisfecho cuando ya no quiero seguir comiendo.", ["usa al menos cuatro alimentos distintos", "nombra la señal de hambre o saciedad", "no culpa ni juzga a nadie"], ["plato dibujado o lista escrita"], ["llamar a un alimento «malo»", "hablar de peso o dieta"], "Reconoce la variedad y revisa que no haya juicios sobre personas."),
    reinforce="Escribe tres alimentos de distintos tipos que te gusten.",
    extend="Escribe una frase para responder si alguien se burla de lo que llevas de colación.",
)

lesson(
    OA4, 4,
    "Una hoja y un lápiz. Las situaciones y las listas están escritas en los ejercicios. No uses tus datos reales para completar los ejemplos.",
    "Aprenderé a proteger mi cuerpo, mi intimidad y mi información personal, en la vida real y en internet. Sirve para decidir qué comparto y con quién.",
    ["Sé que mi cuerpo es mío.", "Sé que hay cosas privadas."],
    [
        "Cuidar tu cuerpo y tu intimidad significa que decides quién puede ver o tocar tu cuerpo. Las partes íntimas están bajo la ropa interior o el traje de baño. Puedes pedir privacidad al cambiarte o ir al baño. Si un médico o una médica tiene que revisarte, lo hace con una persona de tu familia o de confianza presente y te explica antes qué hará.",
        "La información personal son datos que dicen quién eres o dónde estás: tu nombre completo, tu dirección, tu teléfono, tu colegio, tus horarios, tus contraseñas y tus fotos. Esos datos solo se comparten con personas de confianza y con permiso de un adulto de tu casa. En internet, no se entregan a personas que no conoces, aunque parezcan amables.",
        "Nunca compartas fotos íntimas ni se las pidas a otros. Si alguien en línea te pide datos, fotos o encontrarte, no contestes, cuéntaselo a un adulto de confianza y guarda la conversación. No es tu culpa, y avisar es cuidar.",
    ],
    [("intimidad", "lo muy personal que cada uno protege"), ("privacidad", "derecho a que otros no vean ni sepan mis cosas privadas"), ("información personal", "datos que dicen quién soy o dónde estoy"), ("contraseña", "clave secreta para entrar a una cuenta"), ("en línea", "en internet")],
    [
        W("Datos que se protegen", "¿Cuál de estos datos es información personal: tu color favorito o tu dirección?", ["La dirección dice dónde vives.", "El color favorito no pone en riesgo a nadie.", "La dirección se protege."], "La dirección"),
        W("Pedido en línea", "Alguien en un juego en línea te pide tu nombre completo y dónde queda tu colegio. ¿Qué haces?", ["No entrego los datos.", "Dejo de hablar con esa persona.", "Se lo cuento a un adulto de confianza."], "No entrego los datos y se lo cuento a un adulto de confianza"),
    ],
    [
        M("Dar mis datos porque la persona en línea parece amable.", "Se piensa que quien es amable es confiable.", "Datos y fotos solo se comparten con personas de confianza y con permiso."),
        M("Pensar que si me equivoqué al compartir algo, no puedo contarlo.", "Se siente vergüenza o miedo al reto.", "Siempre puedes pedir ayuda. No es tu culpa y avisar es cuidarte."),
    ],
    R=[
        ex("¿Tu dirección es información personal?", "Sí", "Dice dónde estás."),
        ex("¿Se comparte una contraseña con alguien que no conoces?", "No", "Es una clave secreta."),
        ex("¿Puedes pedir privacidad para cambiarte de ropa?", "Sí", "Tu cuerpo es tuyo."),
    ],
    U=[
        ex("¿Por qué no se entregan datos a personas desconocidas en línea?", "Porque puede ponerme en riesgo", "No sabemos quién es en realidad."),
        ex("Si alguien en línea te pide una foto íntima, ¿qué haces?", "No contesto y se lo cuento a un adulto de confianza", "Nadie debe pedirla."),
        ex("¿Avisar a un adulto cuando algo te incomoda es cuidar?", "Sí", "Pedir ayuda protege."),
    ],
    A=[
        ex("¿«Nombre completo y colegio» juntos son información personal que se protege?", "Sí", "Dicen quién soy y dónde estoy."),
        ex("Escribe una frase para decir «no» si alguien en línea pide tu teléfono.", "No doy mi teléfono", "Es clara y corta."),
        ex("¿Quién puede ayudarte con una contraseña: un adulto de tu casa o un desconocido?", "Un adulto de mi casa", "Es persona de confianza."),
    ],
    Z=[
        ex("Dos niños: uno comparte su dirección con un desconocido y otro no. ¿Cuál se protege?", "El que no la comparte", "Así evita riesgos y se protege."),
        ex("Un niño dice: «Mi médico me revisó con mi familia presente y me explicó todo». ¿Cumple las reglas de cuidado?", "Sí", "Había una persona de confianza y le explicaron."),
    ],
    D=[
        arith("De 20 datos en una lista, 13 son personales y los demás no. ¿Cuántos no son personales?", "20-13", "Se resta lo personal al total."),
        ex("Un amigo publicó una foto con el nombre del colegio y la hora de salida. ¿Qué información personal compartió?", "El colegio y los horarios", "Dicen dónde y cuándo estará."),
    ],
    context=[ex("En un juego en línea, un desconocido ofrece regalos si le das tu dirección. Camila se sale del juego y se lo cuenta a una persona de su casa. ¿Hizo bien?", "Sí", "No entregó datos y pidió ayuda.")],
    selfcheck=[ex("En Orientación: ¿mi nombre completo y mi dirección son privados?", "Sí", "Dicen quién soy y dónde estoy."), ex("¿Se comparte una contraseña con amigos?", "No", "Es una clave personal."), ex("¿Puedo pedir ayuda si algo en línea me incomoda?", "Sí", "Avisar es cuidarse.")],
    task=T("Lee las situaciones: (1) un juego pide tu dirección, (2) un compañero quiere tu contraseña de un juego, (3) alguien desconocido en línea te escribe «dime dónde estudias». Para cada una escribe qué haces y a quién avisarías. Puedes usar un personaje.", "(1) No la doy; aviso a una persona adulta de mi casa. (2) No la comparto y aviso a un adulto de mi casa. (3) No contesto; se lo cuento a un adulto de confianza.", ["no comparte datos personales", "nombra a quién avisar", "no se culpa"], ["respuesta escrita o dibujada"], ["compartir datos por amabilidad", "no avisar"], "Reconoce las decisiones y revisa que nombre a un adulto de confianza."),
    reinforce="Escribe tres datos que no compartirías con desconocidos.",
    extend="Explica por qué avisar no es acusar cuando algo en línea te incomoda.",
)

lesson(
    OA4, 5,
    "Una hoja y un lápiz. Las situaciones están escritas en los ejercicios. Usa personajes; nadie tiene que contar nada personal.",
    "Aprenderé una forma de actuar ante una situación de peligro: parar, alejarme, contar y seguir contando. Sirve para protegerme y pedir ayuda, también si me ofrecen alcohol, cigarros u otras drogas.",
    ["Sé que mi cuerpo es mío.", "Sé que hay datos que no se comparten."],
    [
        "Hay cuatro pasos para cuidarte cuando algo te incomoda o te da miedo. Parar: decir «no» o «para». Alejarte: irte a un lugar seguro, como donde hay otros adultos. Contar: decirle a un adulto de confianza lo que pasó. Y seguir contando: si el primer adulto no te ayuda o no te cree, cuéntaselo a otro hasta que alguien te ayude.",
        "Si no puedes decir «no», igual puedes alejarte y contar: lo más importante es contar. Estos pasos sirven si alguien te toca o te mira de una forma que te incomoda, si te piden un secreto que te asusta o si te ofrecen alcohol, cigarros u otras drogas, que no son para niños porque dañan un cuerpo que está creciendo. Los medicamentos solo los entrega una persona adulta de confianza que te cuida. No es tu culpa, y avisar no es acusar.",
        "Los adultos de confianza pueden ser de tu casa o de la escuela, como una profesora o una persona de orientación. En Chile, el 133 es el número de emergencias de Carabineros. También hay líneas de ayuda para niños y niñas, como el Fono Niños 147 de Carabineros. Pide a un adulto que confirme los números vigentes y que te diga qué otros apoyos hay en tu escuela.",
    ],
    [("proteger", "cuidar para que no pase algo malo"), ("adulto de confianza", "persona adulta a quien puedo contar algo y que me ayuda"), ("alejarse", "irse a un lugar seguro"), ("droga", "sustancia que altera cómo funciona el cuerpo y que puede dañarlo"), ("emergencia", "situación de peligro que necesita ayuda rápida")],
    [
        W("Los cuatro pasos", "Un compañero mayor le ofrece un cigarro a Pía en la plaza. ¿Qué hace Pía según los cuatro pasos?", ["Para: dice «no».", "Se aleja y busca adultos.", "Cuenta lo que pasó y, si hace falta, sigue contando."], "Dice no, se aleja y se lo cuenta a un adulto de confianza"),
        W("Seguir contando", "Rafa le cuenta algo a un adulto, pero este no lo escucha. ¿Qué hace Rafa?", ["Lo que le pasó es importante.", "El primer adulto no ayudó.", "Se lo cuenta a otro adulto de confianza."], "Se lo cuenta a otro adulto de confianza"),
    ],
    [
        M("Pensar que, si me ofrecen algo peligroso y digo que no, quedaré mal.", "Se teme perder amistades.", "Un «no» te cuida y es valiente. Alejarse y contar protege."),
        M("Contarlo una sola vez y quedarme callado si no me hacen caso.", "Se cree que no hay otro adulto.", "Sigue contando hasta que alguien te ayude."),
    ],
    R=[
        ex("¿Los cuatro pasos son parar, alejarse, contar y seguir contando?", "Sí", "Son la forma de cuidarse."),
        ex("Si el primer adulto no te ayuda, ¿qué haces?", "Se lo cuento a otro adulto de confianza", "Hasta que alguien me ayude."),
        ex("¿Avisar a un adulto es acusar?", "No", "Es pedir ayuda para cuidarte."),
    ],
    U=[
        ex("¿Quién entrega los medicamentos a un niño o niña: un adulto de confianza que lo cuida o un amigo?", "Un adulto de confianza que lo cuida", "Los medicamentos solo los da un adulto responsable."),
        ex("¿Por qué el alcohol y los cigarros no son para niños?", "Porque dañan un cuerpo que está creciendo", "Hacen mal a la salud."),
        ex("¿Qué número de Carabineros se usa en Chile para emergencias?", "133", "Es el número de emergencias de Carabineros."),
    ],
    A=[
        ex("Escribe una frase para parar a alguien que te incomoda.", "Para, no me gusta", "Es clara y directa."),
        ex("Un niño dice «me dio miedo lo que pasó, pero no fue mi culpa». ¿Tiene razón?", "Sí", "Quien daña es responsable, no quien lo vive."),
        ex("Nombra dos adultos de confianza posibles, sin dar nombres.", "Por ejemplo, un adulto de mi casa y una profesora", "Pueden ser de la casa o de la escuela."),
    ],
    Z=[
        ex("Un amigo te dice «si me cuentas a un adulto, me meto en problemas, es un secreto». ¿Qué conviene si te incomodó?", "Contarlo igual a un adulto de confianza", "Cuidarte es más importante que el secreto."),
        ex("Una niña cree que, si cuenta, será castigada. ¿Quién debe hacerse cargo de lo que pasó?", "El adulto o la persona que la puso en peligro", "No es culpa de quien lo vive."),
    ],
    D=[
        arith("En una semana, un curso practicó los cuatro pasos 2 veces por día durante 5 días. ¿Cuántas veces lo practicaron?", "2*5", "Se repite dos veces cinco días."),
        ex("Si te ofrecen algo peligroso, ¿qué orden sigues: contar, parar, alejarte o parar, alejarte, contar?", "Parar, alejarte, contar", "Primero te proteges y luego avisas."),
    ],
    context=[ex("Un adulto desconocido en el parque le ofrece a Dani «una pastilla para sentirse bien». Dani dice «no», se aleja hacia donde está su familia y se lo cuenta a un adulto de su casa. ¿Siguió los pasos?", "Sí", "Paró, se alejó y contó.")],
    selfcheck=[ex("En Orientación: ¿puedo seguir contando si no me ayudan?", "Sí", "Hasta que alguien me ayude."), ex("¿Puedo tomar un medicamento que me ofrece un amigo?", "No", "Solo me lo entrega un adulto de confianza que me cuida."), ex("¿Es mi culpa si me hicieron sentir miedo?", "No", "La responsabilidad es de quien me puso en peligro.")],
    task=T("Lee tres situaciones: (1) un amigo mayor te ofrece un cigarro, (2) alguien te pide que guardes un secreto que te asusta, (3) un desconocido te pide acompañarlo. Para cada una escribe los cuatro pasos (parar, alejarme, contar, seguir contando) y a quién se lo contarías. Usa un personaje si prefieres.", "(1) Digo no, me voy con mis compañeros, se lo cuento a una profesora; si no me ayuda, se lo cuento a otro adulto.", ["usa los cuatro pasos", "nombra adultos de confianza", "dice que no es su culpa"], ["respuesta escrita o dibujada"], ["guardar el secreto", "culparse"], "Reconoce los pasos y recuerda que hay adultos y líneas de ayuda; sugiere confirmar los números vigentes con un adulto."),
    reinforce="Escribe los cuatro pasos con tus palabras.",
    extend="Haz una tarjeta con los cuatro pasos y los números 133 y 147 para tener a mano, después de confirmarlos con un adulto.",
)
