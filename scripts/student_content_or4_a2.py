"""Cuaderno del estudiante, 4.º básico Orientación: OA 03 (sexualidad, vínculo, intimidad y origen de la vida) y OA 04 (pubertad)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA3, OA4 = "OR04 OA 03", "OR04 OA 04"


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
    "Una hoja y un lápiz. Las situaciones de personajes están escritas en los ejercicios. Nadie tiene que contar nada de su cuerpo ni de su familia.",
    "Aprenderé que la sexualidad es parte de ser persona y que tiene varias dimensiones, no solo el cuerpo. Sirve para entender cómo cuidarnos y respetarnos.",
    ["Sé que mi cuerpo y mis emociones son míos.", "Sé que hay cosas privadas que no tengo que contar."],
    [
        "La sexualidad es una parte de ser persona que existe durante toda la vida. No es solo el cuerpo. Tiene cuatro dimensiones. La dimensión del cuerpo: cómo somos y cómo lo cuidamos. La dimensión afectiva: lo que sentimos por otros, como cariño o amistad. La dimensión social: cómo nos relacionamos y qué reglas de respeto usamos. La dimensión ética: las decisiones que tomamos con cuidado y respeto.",
        "Una misma situación puede tener varias dimensiones a la vez. Abrazar a una abuela con su permiso muestra cariño (afectiva) y respeto (social). En la vida adulta, la sexualidad también es una forma en que dos personas expresan amor, vínculo e intimidad. Esa intimidad es privada y se vive con respeto y con acuerdo de ambas personas.",
        "En esta clase no se cuentan cosas personales: usamos personajes inventados. Si algo te inquieta o tienes preguntas, puedes hablar con una persona adulta de confianza, de tu casa o de la escuela. Preguntar está bien.",
    ],
    [("sexualidad", "parte de ser persona que incluye cuerpo, afectos, relaciones y valores"), ("dimensión", "una parte o aspecto de algo"), ("afectivo", "que tiene que ver con lo que sentimos por otros"), ("ético", "que tiene que ver con decidir con cuidado y respeto"), ("íntimo", "muy personal; cada uno decide si lo cuenta")],
    [
        W("Dimensión del cuerpo", "Eli se lava las manos antes de comer y se cepilla los dientes. ¿De qué dimensión se trata?", ["Eli cuida cómo es su cuerpo.", "No habla de sentimientos ni de reglas con otros.", "Es la dimensión del cuerpo."], "La dimensión del cuerpo"),
        W("Dos dimensiones a la vez", "Rita abraza a su abuela porque la quiere y antes le pregunta «¿puedo abrazarte?». ¿Qué dimensiones aparecen?", ["Querer a su abuela es afectivo.", "Pedir permiso es una regla de respeto: social.", "Hay dos dimensiones juntas."], "Afectiva y social"),
    ],
    [
        M("Pensar que la sexualidad es solo cómo es el cuerpo.", "Se habla del tema solo con partes del cuerpo.", "También incluye afectos, relaciones respetuosas y valores."),
        M("Creer que tengo que contar cosas mías para participar.", "Pensamos que hay que responder todo.", "Puedes usar personajes y decir «prefiero no contar»."),
    ],
    R=[
        ex("La sexualidad ¿es solo el cuerpo o tiene varias dimensiones?", "Tiene varias dimensiones", "Incluye cuerpo, afectos, relaciones y valores."),
        ex("«Sentir cariño por un amigo» ¿es de la dimensión afectiva o de la del cuerpo?", "De la dimensión afectiva", "Es un sentimiento hacia otra persona."),
        ex("Si algo te inquieta, ¿con quién puedes hablar?", "Con una persona adulta de confianza", "Preguntar está bien y alguien puede ayudarte."),
    ],
    U=[
        ex("¿Qué dimensión es «pedir permiso antes de abrazar»: social o del cuerpo?", "Social", "Es una regla de respeto entre personas."),
        ex("Si un compañero te pide que cuentes algo íntimo, ¿estás obligado?", "No", "Lo íntimo se cuenta solo si uno quiere."),
        ex("¿La sexualidad existe solo cuando se es adulto?", "No, existe durante toda la vida", "Es parte de ser persona desde siempre."),
    ],
    A=[
        ex("Tomás decide no entrar a un juego que lo incomoda y lo dice con calma. ¿Qué dimensión muestra: ética o del cuerpo?", "Ética", "Decide con cuidado y respeto por sí mismo."),
        ex("Escribe la dimensión de cada acción, en orden: «lavarme los dientes», «alegrarme por un amigo», «saludar con respeto».", "Cuerpo, afectiva, social", "Cuidar el cuerpo, sentir cariño y relacionarse con respeto."),
        ex("Según la clase, la intimidad entre dos personas adultas que se aman, ¿es algo público o privado?", "Privado", "Es íntimo y se vive con respeto y acuerdo."),
    ],
    Z=[
        ex("Un compañero dice «la sexualidad es solo cómo es el cuerpo por fuera». ¿Qué dimensiones le faltan?", "Afectiva, social y ética", "Incluye lo que sentimos, cómo nos relacionamos y qué decidimos."),
        ex("Un niño dice: «Para participar tengo que contar cómo es mi cuerpo». ¿Es cierto?", "No", "Nadie debe contar cosas íntimas; se trabaja con personajes."),
    ],
    D=[
        arith("En una lista de 12 situaciones, 5 son del cuerpo y 4 son afectivas. Las demás son sociales o éticas. ¿Cuántas son sociales o éticas?", "12-5-4", "Se quitan las del cuerpo y las afectivas."),
        ex("Frases: (a) «Me lavo bien las manos». (b) «Extraño a mi amiga». (c) «Respeto el turno de los demás». (d) «Decido no entrar a un juego que me incomoda». ¿Cuántas son de la dimensión social o ética?", "2", "La (c) es social y la (d) es ética; (a) es del cuerpo y (b) es afectiva."),
    ],
    context=[ex("Un niño decide saludar a un familiar con la mano y no con un abrazo, y lo dice con respeto. ¿Qué dimensión muestra mejor su decisión: la ética o la afectiva?", "La ética", "Decide con cuidado de sí mismo y respeto hacia el otro.")],
    selfcheck=[ex("En Orientación: ¿la sexualidad tiene varias dimensiones?", "Sí", "Incluye cuerpo, afectos, relaciones y valores."), ex("¿Estás obligado a contar algo íntimo?", "No", "Cada uno decide."), ex("¿Preguntar a una persona adulta de confianza está bien?", "Sí", "Preguntar ayuda a entender.")],
    task=T("Lee: Lola cuida su cuerpo, quiere mucho a su amiga Eli y le pide permiso antes de abrazarla. Eli prefiere hoy solo darle la mano y Lola lo respeta. Escribe una frase para cada dimensión (cuerpo, afectiva, social, ética) usando este caso. Puedes trabajar solo con los personajes.", "Cuerpo: Lola cuida su cuerpo. Afectiva: quiere mucho a Eli. Social: pide permiso antes de abrazar. Ética: respeta que hoy Eli prefiera la mano.", ["escribe una frase por cada dimensión", "usa solo los personajes", "no cuenta nada íntimo propio"], ["texto escrito o dicho"], ["reducir todo al cuerpo", "contar algo íntimo"], "Reconoce cada dimensión y pregunta qué otras situaciones tendrían dos dimensiones a la vez."),
    reinforce="Inventa un personaje y escribe una acción para cada dimensión de la sexualidad.",
    extend="Piensa en una situación de la escuela que tenga dos dimensiones a la vez y explica cuáles son.",
)

lesson(
    OA3, 2,
    "Una hoja y un lápiz. Las situaciones están escritas en los ejercicios. Nadie tiene que contar cómo es su familia.",
    "Aprenderé a reconocer vínculos respetuosos, que pueden ser de muchas formas. Sirve para valorar a las personas que nos cuidan y para saber cuándo un vínculo no es respetuoso.",
    ["Conozco las dimensiones de la sexualidad.", "Sé que las personas somos distintas."],
    [
        "Un vínculo es la unión afectiva entre personas: familia, amistad o compañerismo. En la vida adulta, también puede ser el amor entre dos personas. Un vínculo respetuoso tiene cuidado, confianza, escucha y libertad. En él cada persona puede decir que no, opinar distinto y ser tratada con cariño.",
        "Las familias son diversas. Hay niños que viven con su mamá y su papá, con una sola persona adulta, con sus abuelos, con tíos o con otras personas que los cuidan. Ninguna forma es mejor que otra. Lo importante en una familia es que las personas se cuiden y se respeten. En esta clase no se pregunta ni se juzga cómo es la familia de nadie.",
        "El amor no justifica el control ni la violencia. Quien te quiere no te asusta, no te obliga a hacer lo que no quieres ni te prohíbe tener otros amigos. Frases como «si me quieres, haz lo que digo» no son cuidado. Si un vínculo te hace sentir miedo o mucha tristeza, puedes contárselo a una persona adulta de confianza.",
    ],
    [("vínculo", "unión afectiva entre personas"), ("respeto", "tratar bien al otro y aceptar que es distinto"), ("confianza", "sentir que alguien me cuida y no me hará daño"), ("diversidad", "que las personas y las familias somos distintas"), ("control", "querer mandar sobre lo que otro hace o decide")],
    [
        W("Vínculo respetuoso", "«Mi amiga me escucha, me deja decir que no y no se enoja si juego con otros.» ¿Es un vínculo respetuoso?", ["Escuchar es un signo de cuidado.", "Dejar decir que no da libertad.", "No se enoja si juego con otros: no hay control."], "Sí, es respetuoso"),
        W("Diversidad de familias", "Lola vive con su abuela, Teo con su mamá y su papá, Ema con su papá y Dino con su tía y su tío. ¿Cuál de estas familias no merece respeto?", ["Se mira si se cuidan y se respetan.", "En las cuatro hay personas que cuidan.", "Todas merecen respeto."], "Ninguna: todas merecen respeto"),
    ],
    [
        M("Pensar que hay una sola forma correcta de ser familia.", "Se mira cómo se ve la familia y no cómo se cuidan.", "Lo importante es el cuidado y el respeto."),
        M("Creer que quien me quiere puede mandarme siempre.", "Se confunde cariño con control.", "El cariño respeta mi libertad y mis límites."),
    ],
    R=[
        ex("Un vínculo ¿es una unión afectiva entre personas o un objeto?", "Una unión afectiva entre personas", "Es la relación de cariño que tenemos con otros."),
        ex("«Me cuida, me escucha y me deja decir que no». ¿Es un vínculo respetuoso?", "Sí", "Tiene cuidado, escucha y libertad."),
        ex("«Si me quieres, me obedeces siempre». ¿Es respetuoso?", "No", "Obliga y quita libertad."),
    ],
    U=[
        ex("¿Qué importa más en una familia: cuántas personas la forman o que se cuiden y se respeten?", "Que se cuiden y se respeten", "El cuidado es lo que hace a una familia."),
        ex("¿Se puede decir que una forma de familia vale más que otra?", "No", "Todas las familias merecen respeto."),
        ex("¿Por qué «si me quieres, haz lo que te digo» no es respeto?", "Porque obliga y quita libertad", "El cariño no manda sobre lo que el otro decide."),
    ],
    A=[
        ex("Nombra una conducta respetuosa en una amistad: «devolver lo prestado y dar las gracias» o «esconder el cuaderno para que no pueda jugar».", "Devolver lo prestado y dar las gracias", "Cuida al otro; esconder el cuaderno lo daña."),
        ex("Cinco conductas: cuidar, gritar, escuchar, esperar el turno y amenazar. ¿Cuántas muestran respeto?", "3", "Cuidar, escuchar y esperar el turno son respetuosas; gritar y amenazar no."),
        ex("Un compañero dice «la familia de Pía no es de verdad porque vive con su abuela». ¿Qué le responderías?", "Una familia es donde se cuidan y se respetan", "Se valora el cuidado y no la forma."),
    ],
    Z=[
        ex("Un niño dice: «Mi familia es la correcta porque somos cuatro». ¿Es una buena razón?", "No", "El número de personas no determina el cuidado."),
        ex("Una amiga te pide siempre que no hables con otros compañeros. ¿Es cuidado o control? ¿A quién puedes contárselo?", "Es control; a una persona adulta de confianza", "Quitar libertad no es cariño."),
    ],
    D=[
        arith("En un juego de roles hay 24 tarjetas con conductas. 15 son respetuosas. ¿Cuántas no lo son?", "24-15", "Se resta a las 24 las que sí son respetuosas."),
        ex("Tres conductas: A) «te escucho aunque pensemos distinto», B) «no te dejo hablar con otros amigos», C) «te ayudo y dejo que decidas». ¿Cuáles son respetuosas?", "A y C", "La B quita libertad: es control."),
    ],
    context=[ex("En una actividad, la profesora dice: «Una familia es donde las personas se cuidan y se respetan, sin importar cuántas sean». ¿Respeta la diversidad de las familias?", "Sí", "No juzga la forma y valora el cuidado.")],
    selfcheck=[ex("En Orientación: ¿hay una sola forma correcta de ser familia?", "No", "Hay muchas, y todas merecen respeto."), ex("¿El cariño justifica el control?", "No", "El cariño respeta la libertad."), ex("¿Puedes contar a un adulto de confianza si un vínculo te da miedo?", "Sí", "Pedir ayuda es importante.")],
    task=T("Lee las frases de un personaje: A) «Mi amigo me escucha y me deja elegir». B) «Mi compañera me dice que si juego con otros ya no será mi amiga». C) «En mi casa nos cuidamos y nos ayudamos». Marca cuáles muestran un vínculo respetuoso y cuál no. Escribe por qué y qué podría hacer el personaje en el caso B.", "A y C son respetuosos porque hay escucha y cuidado. B no lo es porque controla. El personaje puede contarle a una persona adulta de confianza.", ["clasifica las tres frases", "explica con cuidado, escucha o libertad", "propone pedir ayuda en B"], ["texto escrito o dicho"], ["juzgar una forma de familia", "confundir cariño con control"], "Reconoce el criterio de respeto y revisa que no se juzgue a ninguna familia."),
    reinforce="Escribe dos conductas respetuosas y dos que no lo sean dentro de una amistad.",
    extend="Escribe un mensaje que un personaje diría a un compañero que se burla de la familia de otro.",
)

lesson(
    OA3, 3,
    "Una hoja y un lápiz. Los casos de personajes están escritos en los ejercicios.",
    "Aprenderé qué es la intimidad, qué es el consentimiento y cómo poner y respetar límites. Sirve para cuidar mi cuerpo y mis emociones, y respetar a los demás.",
    ["Conozco vínculos respetuosos.", "Sé que mi cuerpo es mío."],
    [
        "La intimidad es lo privado de cada persona: su cuerpo, sobre todo las partes que cubre la ropa interior o el traje de baño, y lo que piensa y siente. Cada uno decide con quién la comparte. Un límite es lo que acepto y lo que no acepto, como un abrazo, una broma o que me tomen una foto. Tengo derecho a ponerlo y debo respetar el de los demás.",
        "El consentimiento es decir «sí» de manera libre, es decir, sin presión, engaño ni miedo. Tiene tres ideas. Se pregunta antes: «¿puedo?». Un «no» basta, sin dar explicaciones. Y puede cambiar: puedo decir sí hoy y no mañana. El silencio o la cara de incomodidad no son un sí. Si el otro duda, se detiene la acción.",
        "Nadie puede pedirte que muestres o toques tu cuerpo, ni tocarte de una forma que te incomode. Si pasa, avisa a una persona adulta de confianza y sigue contando hasta que te escuchen. No es tu culpa. Una sorpresa de cumpleaños es distinta a un secreto que da miedo: las sorpresas alegran y los secretos que asustan se cuentan.",
    ],
    [("intimidad", "lo privado de una persona: su cuerpo y lo que siente"), ("límite", "lo que acepto y lo que no acepto"), ("consentimiento", "decir sí libre, sin presión, y que puede cambiar"), ("presión", "insistir para que alguien haga algo que no quiere"), ("privado", "algo que cada persona decide si comparte")],
    [
        W("Respetar un no", "Tomás pregunta «¿te puedo dar un abrazo?». Lola dice «hoy no». ¿Qué debe hacer Tomás?", ["Lola puso un límite.", "El no basta, sin explicación.", "Tomás debe respetarlo."], "Respetarlo y no insistir"),
        W("Sorpresa o secreto", "Ema escondió el regalo de su amiga hasta el cumpleaños. Un niño mayor le dice a Pía: «Esto es un secreto entre los dos. Si se lo cuentas a alguien, te irá mal». ¿Cuál es una sorpresa y cuál un secreto que se cuenta?", ["La sorpresa se revela pronto y alegra.", "Esconder algo que da miedo no es una sorpresa.", "El secreto que asusta se cuenta a un adulto de confianza."], "El regalo es una sorpresa; lo del niño mayor es un secreto que asusta y se cuenta"),
    ],
    [
        M("Pensar que si alguien no dice nada, dijo que sí.", "Se confunde el silencio con un permiso.", "Pregunta y espera un sí claro."),
        M("Creer que debo guardar un secreto que me asusta.", "Se piensa que contar es traicionar.", "Los secretos que asustan se cuentan a una persona adulta de confianza."),
    ],
    R=[
        ex("El consentimiento ¿es decir sí libre o decir sí por miedo?", "Decir sí libre", "Debe ser sin presión ni miedo."),
        ex("Si alguien dice «no quiero», ¿hay que respetarlo?", "Sí", "Un no basta."),
        ex("¿Puede alguien cambiar de opinión y decir no después de haber dicho sí?", "Sí", "El consentimiento puede cambiar."),
    ],
    U=[
        ex("¿El silencio es un sí?", "No", "Quien calla puede sentir miedo o incomodidad."),
        ex("¿Qué debes hacer si alguien te toca de una forma que te incomoda?", "Decir que no y contárselo a una persona adulta de confianza", "Nadie puede tocarte si no quieres."),
        ex("¿Una sorpresa de cumpleaños es lo mismo que un secreto que da miedo?", "No", "La sorpresa alegra; el secreto que asusta se cuenta."),
    ],
    A=[
        ex("Dino quiere abrazar a Rita. ¿Cuál es la forma respetuosa: «¿puedo darte un abrazo?» o abrazarla de sorpresa?", "«¿Puedo darte un abrazo?»", "Se pregunta antes y se espera la respuesta."),
        ex("Ana dice «no quiero que me saquen una foto». ¿Qué debe hacer el compañero que iba a sacarla?", "No sacarla", "Respeta su límite sobre su imagen."),
        ex("Pedro le pide a su amiga mostrarle algo íntimo de su cuerpo. ¿Ella debe hacerlo?", "No", "Nadie puede pedir que se muestre el cuerpo; debe contarlo a una persona adulta de confianza."),
    ],
    Z=[
        ex("Un niño dice: «Ella no dijo que no, así que está bien». ¿Es correcto?", "No", "Falta un sí claro y libre."),
        ex("Un niño ofrece un regalo a cambio de que guardes un secreto que te da miedo. ¿Qué haces?", "No lo guardo; se lo cuento a una persona adulta de confianza", "Los secretos que asustan se cuentan."),
    ],
    D=[
        arith("En un juego de casos hay 10 situaciones. En 7 se respetó el no. ¿En cuántas no se respetó?", "10-7", "Se restan las situaciones respetadas del total."),
        ex("Tres frases de consentimiento: A) «Sí, me parece bien». B) «Sí, me gusta». C) «Sí, pero no se lo cuentes a nadie o me enojo». ¿Cuál tiene presión o secreto?", "C", "Pide guardar un secreto y amenaza con enojarse: eso es presión."),
    ],
    context=[ex("Luis pregunta «¿te puedo dar un abrazo?». Eli dice «hoy no». Luis responde «está bien, otro día». ¿Respetó el límite?", "Sí", "Aceptó el no sin insistir.")],
    selfcheck=[ex("En Orientación: ¿un no basta para poner un límite?", "Sí", "No necesitas explicarlo."), ex("¿El consentimiento puede cambiar?", "Sí", "Puedo decir sí hoy y no mañana."), ex("¿Los secretos que asustan se deben guardar?", "No", "Se cuentan a una persona adulta de confianza.")],
    task=T("Lee: Marta quiere sacar una foto de Joaquín jugando. Joaquín dice «no quiero». Marta insiste y se la saca igual. Escribe qué límite puso Joaquín, qué hizo mal Marta y qué debió hacer. Después escribe una frase que Joaquín puede decir y a quién puede contárselo.", "Límite: no quería la foto. Marta insistió y la sacó. Debió respetar el no. Joaquín puede decir: «No quiero, por favor borra la foto». Puede contárselo a su profesora.", ["identifica el límite", "explica por qué no se respetó", "propone una frase y a quién contar"], ["texto escrito o dicho"], ["decir que el no necesita razón", "no avisar a un adulto"], "Reconoce el límite y revisa que la frase sea clara y firme."),
    reinforce="Escribe tres frases para decir «no» con firmeza y respeto.",
    extend="Escribe cómo un personaje pregunta antes de abrazar o de sacar una foto, y qué hace si le dicen que no.",
)

lesson(
    OA3, 4,
    "Una hoja y un lápiz. Los datos están en los ejercicios. Usa solo lo que se explica aquí; el resto puede conversarlo con una persona adulta de confianza.",
    "Aprenderé, con lenguaje adecuado, cómo comienza una vida y por qué la sexualidad está relacionada con el origen de cada persona. Sirve para entender de dónde venimos con respeto.",
    ["Conozco la intimidad y el consentimiento.", "Sé que todas las familias merecen respeto."],
    [
        "Cada persona tuvo un origen. Una nueva vida comienza cuando una célula de una mujer, llamada óvulo, y una célula de un hombre, llamada espermatozoide, se unen. Con esa unión se forma una primera célula que se divide muchas veces. Así se forma el embrión, que más adelante se llama bebé. La sexualidad de las personas adultas puede ser una forma de expresar amor y vínculo, y también puede dar origen a una nueva vida.",
        "El embrión crece dentro del cuerpo de la mujer, en un órgano llamado útero. Ese tiempo se llama embarazo y dura cerca de nueve meses. Después el bebé nace. Cómo se unen las células es un tema de la intimidad de las personas adultas, y cada familia lo conversa a su manera. Si tienes preguntas, puedes hacerlas a una persona adulta de confianza.",
        "Tener un hijo es una decisión muy grande, porque un bebé necesita cuidado por muchos años. Por eso es una decisión de personas adultas. Hay familias que se forman por adopción: allí también hay vínculo y cuidado. Todas las personas valen igual, sin importar cómo comenzó su vida o cómo está formada su familia.",
    ],
    [("óvulo", "célula de la mujer que participa en el origen de una vida"), ("espermatozoide", "célula del hombre que participa en el origen de una vida"), ("útero", "órgano de la mujer donde crece el bebé"), ("embarazo", "tiempo en que el bebé crece dentro del útero"), ("adopción", "cuando una familia cuida como hijo o hija a un niño que no nació en ella")],
    [
        W("Ordenar el origen", "Ordena: A) el bebé nace, B) se unen las células, C) el embrión crece en el útero.", ["Primero se unen las células: B.", "Luego el embrión crece: C.", "Al final nace el bebé: A."], "B, C, A"),
        W("Duración del embarazo", "El embarazo dura cerca de nueve meses. Si han pasado cuatro meses, ¿cuántos faltan aproximadamente?", ["El total es nueve meses.", "Ya pasaron cuatro.", "Se resta: 9 menos 4."], "Cerca de 5 meses"),
    ],
    [
        M("Pensar que solo importan las personas que nacieron en una familia por sangre.", "Se ignora el vínculo que crea el cuidado.", "Una familia por adopción también es una familia."),
        M("Creer que debo contar cómo nací o cómo es mi familia.", "Se piensa que hay que responder todo.", "Cada persona decide qué compartir."),
    ],
    R=[
        ex("El óvulo ¿es una célula de la mujer o del hombre?", "De la mujer", "La mujer aporta el óvulo."),
        ex("El espermatozoide ¿es una célula del hombre o de la mujer?", "Del hombre", "El hombre aporta el espermatozoide."),
        ex("¿Dónde crece el bebé antes de nacer?", "En el útero", "Es el órgano de la mujer donde crece."),
    ],
    U=[
        ex("¿Cómo comienza una nueva vida?", "Se unen un óvulo y un espermatozoide", "Esa unión forma la primera célula."),
        ex("Tener un hijo, ¿es una decisión pequeña o grande de personas adultas?", "Grande, de personas adultas", "Un bebé necesita cuidado por muchos años."),
        ex("¿Una persona adoptada tiene menos valor que otra?", "No", "Todas las personas valen igual."),
    ],
    A=[
        ex("Pasaron dos meses de un embarazo de nueve meses. ¿Qué viene después: el embrión sigue creciendo o el bebé nace ya?", "El embrión sigue creciendo", "Aún faltan varios meses para nacer."),
        ex("Un niño pregunta «¿cómo se unen las células?». ¿Con quién puede conversar ese tema?", "Con una persona adulta de confianza", "Es un tema de intimidad que cada familia explica a su manera."),
        ex("Escribe una frase que muestre respeto por una familia adoptiva.", "Una familia es donde las personas se cuidan y se quieren", "Valora el cuidado más que la forma."),
    ],
    Z=[
        ex("Un niño dice que su compañero adoptado «no es de verdad» de su familia. ¿Qué le respondes?", "Que la familia se forma por cuidado y vínculo", "El cuidado hace a una familia."),
        ex("¿Por qué tener un bebé es una decisión de personas adultas?", "Porque un bebé necesita cuidado por muchos años", "Los adultos pueden asumir esa responsabilidad."),
    ],
    D=[
        arith("El embarazo dura cerca de 9 meses. Una mujer cumplió 6 meses. ¿Cuántos meses faltan aproximadamente?", "9-6", "Se resta lo que pasó al total."),
        ex("Tres frases: A) «Cada persona tuvo un origen». B) «Solo algunas personas valen». C) «Una familia se forma de muchas maneras». ¿Cuáles son correctas?", "A y C", "La B dice que algunas valen más, lo cual es falso."),
    ],
    context=[ex("Mateo pregunta cómo nacen los bebés. La profesora usa los términos correctos, explica el embarazo y dice que lo demás lo conversa cada familia. ¿Usó un lenguaje adecuado y respetuoso?", "Sí", "Respondió con claridad y cuidó la intimidad de las familias.")],
    selfcheck=[ex("En Orientación: ¿una vida comienza con la unión de dos células?", "Sí", "El óvulo y el espermatozoide se unen."), ex("¿Todas las familias valen igual?", "Sí", "Todas merecen respeto."), ex("¿Puedes preguntar a una persona adulta de confianza?", "Sí", "Preguntar ayuda a entender.")],
    task=T("Escribe con tus palabras, en tres o cuatro frases, cómo comienza una vida y cuánto dura el embarazo. Usa al menos tres de estas palabras: óvulo, espermatozoide, útero, embarazo, bebé. Agrega una frase que diga por qué todas las familias merecen respeto.", "Una vida comienza cuando se unen un óvulo y un espermatozoide. El embrión crece en el útero durante el embarazo, cerca de nueve meses. Luego nace el bebé. Todas las familias merecen respeto porque se cuidan.", ["usa al menos tres palabras correctamente", "explica el orden del origen", "incluye una frase de respeto a las familias"], ["texto escrito o dicho"], ["mezclar el orden", "juzgar una forma de familia"], "Reconoce el vocabulario y pregunta si falta algún paso del orden."),
    reinforce="Dibuja tres cuadros con el orden: se unen las células, crece en el útero, nace el bebé.",
    extend="Anota dos preguntas que quieras hacer a una persona adulta de confianza sobre este tema.",
)

# ================================================================ OA 04
lesson(
    OA4, 1,
    "Una hoja y un lápiz. Los casos de personajes y las listas de cambios están escritos en los ejercicios. Nadie debe describir ni comparar su cuerpo.",
    "Aprenderé qué cambios físicos ocurren en la pubertad y que no hay un calendario único para todos. Sirve para entender mi cuerpo y respetar el de los demás.",
    ["Sé que mi cuerpo es mío y es privado.", "Sé que las personas crecen a ritmos distintos."],
    [
        "La pubertad es la etapa en que el cuerpo cambia de niño a adulto. Los cambios los producen las hormonas, que son mensajeros químicos del cuerpo. Entre los cambios que pueden ocurrir están: crecer más rápido, sudar más y tener olor más fuerte, que aparezca vello nuevo, que salgan granitos en la piel y que cambie la voz. En las niñas crecen los pechos y llega la menstruación, un sangrado mensual normal. En los niños cambian los órganos sexuales y la voz se hace más grave.",
        "No hay un calendario único. La pubertad puede empezar antes en algunas personas y después en otras. También cambia el orden y la velocidad de los cambios. Nadie está «atrasado» ni «adelantado»: cada cuerpo sigue su propio ritmo, y todos llegan a esta etapa.",
        "Comparar los cuerpos puede hacer sentir mal. Por eso en esta clase no se compara a nadie ni se cuentan cosas personales. Usamos personajes inventados. Si algo te preocupa, puedes preguntar a una persona adulta de confianza o a un profesional de la salud.",
    ],
    [("pubertad", "etapa en que el cuerpo cambia de niño a adulto"), ("hormona", "mensajero químico que el cuerpo produce y que causa cambios"), ("menstruación", "sangrado mensual normal que llega en las niñas durante la pubertad"), ("cambio físico", "cambio que se ve o se siente en el cuerpo"), ("ritmo", "velocidad con que cada persona cambia")],
    [
        W("Cambio de la pubertad", "¿Cuál es un cambio de la pubertad: «aprender a andar en bicicleta» o «aparece vello nuevo»?", ["La pubertad cambia el cuerpo.", "Andar en bicicleta es una destreza que se aprende.", "El vello nuevo es un cambio del cuerpo."], "«Aparece vello nuevo»"),
        W("Sin calendario único", "Rita ya tuvo cambios y su amigo Pablo aún no. ¿Alguno está mal?", ["Cada cuerpo empieza en su tiempo.", "El orden y la velocidad varían.", "Ninguno está mal."], "Ninguno: cada cuerpo sigue su ritmo"),
    ],
    [
        M("Pensar que todos deben cambiar a la misma edad.", "Se mira solo a quienes cambiaron primero.", "Cada cuerpo tiene su ritmo y todos llegan."),
        M("Comparar mi cuerpo con el de otros.", "Se cree que hay un cuerpo ideal.", "No hay cuerpos mejores ni peores; consulta tus dudas a un adulto de confianza."),
    ],
    R=[
        ex("La pubertad, ¿es una etapa o una enfermedad?", "Una etapa", "Es parte normal del crecimiento."),
        ex("Sudar más y que aparezca vello nuevo, ¿son cambios de la pubertad?", "Sí", "Son cambios físicos esperables."),
        ex("¿Todas las personas empiezan la pubertad el mismo día?", "No", "Cada cuerpo empieza en su tiempo."),
    ],
    U=[
        ex("¿Qué son las hormonas?", "Mensajeros químicos que causan los cambios", "El cuerpo las produce y provocan los cambios."),
        ex("Si un amigo cambió antes que tú, ¿significa que algo anda mal en ti?", "No", "No hay un calendario único."),
        ex("¿La voz que se hace más grave es un cambio de la pubertad?", "Sí", "Es un cambio físico esperable, sobre todo en los varones."),
    ],
    A=[
        ex("De estas tres cosas, ¿cuántas son cambios físicos de la pubertad? 1) crecer más rápido, 2) aprender a andar en bicicleta, 3) aparece vello nuevo.", "2", "Crecer más rápido y el vello nuevo son cambios del cuerpo."),
        ex("Tomás aún no ha tenido cambios y sus amigos sí. ¿Cuál frase es correcta: «estás atrasado» o «cada cuerpo empieza en su tiempo»?", "«Cada cuerpo empieza en su tiempo»", "No hay un calendario único."),
        ex("Ana nota que suda más y que su ropa huele más. ¿Es un cambio esperable de la pubertad o algo que hizo mal?", "Un cambio esperable de la pubertad", "Sudar más y tener olor más fuerte son cambios del cuerpo; no son una falta."),
    ],
    Z=[
        ex("Un niño afirma que a los 11 años todos tienen que haber cambiado. ¿Es verdad?", "No", "No hay una edad única para todos."),
        ex("¿Por qué no sirve comparar cuerpos?", "Porque cada cuerpo tiene su ritmo y comparar puede doler", "Comparar crea burlas y preocupación sin necesidad."),
    ],
    D=[
        arith("Una lista tiene 8 cambios. 3 se notan sobre todo en niñas, 3 sobre todo en niños y el resto en todos. ¿Cuántos son de todos?", "8-3-3", "Se quitan los que se notan más en niñas y en niños."),
        ex("Elige el dato verdadero: A) la pubertad empieza igual para todos. B) puede empezar en momentos distintos y el orden de los cambios varía.", "B", "No hay calendario único."),
    ],
    context=[ex("En un cuento, Lola se preocupa porque no ha tenido cambios aún y sus amigas sí. Su profesora le explica que cada cuerpo sigue su ritmo. ¿La explicación es correcta?", "Sí", "No hay calendario único en la pubertad.")],
    selfcheck=[ex("En Orientación: ¿la pubertad empieza igual para todos?", "No", "Cada cuerpo tiene su ritmo."), ex("¿Comparar cuerpos es una buena idea?", "No", "Puede hacer sentir mal."), ex("¿Puedes preguntar tus dudas a una persona adulta de confianza?", "Sí", "Preguntar siempre ayuda.")],
    task=T("Lee: Dino, Eli y Marta son amigos. Eli tuvo cambios antes. Dino aún no. Marta está en medio. Escribe tres cosas: dos cambios físicos que se pueden dar en la pubertad, una frase que explique que no hay un calendario único y una frase amable que diga Marta a Dino. No compares cuerpos.", "Cambios: crecer más rápido y sudar más. Frase: cada cuerpo sigue su ritmo. Marta: Tú vas a tu ritmo y está bien.", ["nombra dos cambios físicos", "explica que no hay calendario único", "la frase es amable y no compara"], ["texto escrito o dicho"], ["comparar cuerpos", "decir que hay una edad correcta"], "Reconoce los cambios y revisa que la frase no compare ni juzgue."),
    reinforce="Escribe cuatro cambios que pueden ocurrir en la pubertad y una frase para tranquilizar a alguien que se preocupa.",
    extend="Explica con tus palabras por qué decir «estás atrasado» es una idea equivocada.",
)

lesson(
    OA4, 2,
    "Una hoja y un lápiz. Los casos de personajes están escritos en los ejercicios.",
    "Aprenderé qué cambios afectivos pueden aparecer en la pubertad y qué necesidades tienen las personas. Sirve para cuidarme, pedir lo que necesito y respetar a otros.",
    ["Conozco los cambios físicos de la pubertad.", "Sé identificar emociones y sus intensidades."],
    [
        "En la pubertad cambian también las emociones y las relaciones. Puede haber emociones más intensas o cambios de ánimo en el mismo día: estar contento y luego molesto. Puede darte más ganas de estar con tus amigos, de tener privacidad o de decidir más cosas por ti mismo. Esto es normal y pasa en distintos momentos.",
        "También puede aparecer atracción o enamoramiento por otra persona. A algunas personas les pasa antes, a otras después, y a otras todavía no. Todas esas experiencias son normales. No hay un momento correcto para sentirlo, y nadie está obligado a contar lo que siente.",
        "Estas nuevas necesidades se pueden cuidar. Necesitas dormir bien, moverte, hablar con alguien de confianza y tener un espacio de privacidad que los demás respeten, por ejemplo no leer tu diario ni abrir tu mochila. La privacidad no es lo mismo que un secreto que te asusta: ese siempre se cuenta a una persona adulta de confianza. Si las emociones son muy fuertes por mucho tiempo, o no te dejan dormir o comer, cuéntaselo a una persona adulta de confianza.",
    ],
    [("cambio afectivo", "cambio en lo que siento y en cómo me relaciono"), ("ánimo", "estado de ánimo; cómo me siento durante el día"), ("privacidad", "espacio y cosas que solo yo decido compartir"), ("atracción", "cuando una persona nos gusta de una manera especial"), ("necesidad", "algo que necesito para estar bien")],
    [
        W("Cambio de ánimo", "Pía estaba contenta en la mañana y en la tarde se enojó sin saber por qué. ¿Es normal en la pubertad?", ["Los cambios de ánimo pueden pasar.", "Dura poco y se puede cuidar.", "Es normal."], "Sí, es normal"),
        W("Privacidad", "Ana pide cerrar la puerta para cambiarse de ropa. ¿Es una necesidad válida?", ["La privacidad es una necesidad.", "Es sobre su cuerpo, que es privado.", "Debe respetarse."], "Sí, es una necesidad válida que debe respetarse"),
    ],
    [
        M("Pensar que los cambios de ánimo significan que algo anda mal.", "Se cree que las emociones deben ser siempre iguales.", "Son parte de crecer; si agobian, se pide ayuda."),
        M("Burlarse de alguien porque le gusta otra persona.", "Se cree que es un chiste inocente.", "Es privado de cada uno; se respeta."),
    ],
    R=[
        ex("¿Los cambios de ánimo pueden ocurrir en la pubertad?", "Sí", "Son cambios normales."),
        ex("¿Pedir privacidad es una necesidad válida?", "Sí", "Cada persona tiene derecho a un espacio privado."),
        ex("¿Todas las personas sienten atracción al mismo tiempo?", "No", "Pasa a ritmos distintos."),
    ],
    U=[
        ex("¿Qué cosas ayudan cuando una emoción es muy intensa: dormir bien y hablar con alguien de confianza, o esconderse siempre?", "Dormir bien y hablar con alguien de confianza", "Cuidarse y hablar ayuda."),
        ex("¿Está bien leer el diario de otra persona sin permiso?", "No", "Es su privacidad."),
        ex("¿Estás obligado a contar si te gusta alguien?", "No", "Es algo que cada uno decide compartir o no."),
    ],
    A=[
        ex("Pía llora y no sabe por qué. ¿Qué es lo primero que puede hacer: nombrar lo que siente o romper algo?", "Nombrar lo que siente", "Así se entiende la emoción sin dañar."),
        ex("Dino cuenta que a su amigo le gusta alguien y los demás se ríen. ¿Se debe respetar la privacidad de ese amigo?", "Sí", "Lo que siente es privado y no es motivo de burla."),
        ex("Si a Lola le cuesta dormir y está muy triste hace semanas, ¿qué debería hacer?", "Contárselo a una persona adulta de confianza", "Cuando la emoción dura mucho, se pide ayuda."),
    ],
    Z=[
        ex("Un niño dice: «Si mi ánimo cambia tanto, algo anda mal conmigo». ¿Qué le dirías?", "Que es parte de crecer, y que puede hablar con un adulto si lo agobia", "Los cambios de ánimo son esperables en la pubertad."),
        ex("Una niña cuenta que ahora le gusta más pasar tiempo con sus amigos, y que igual quiere mucho a su familia. ¿Es un cambio normal o un problema?", "Es un cambio normal", "En esta etapa los amigos suelen ser más importantes y eso no quita el cariño por la familia."),
    ],
    D=[
        arith("A esta edad se recomienda dormir al menos 9 horas. Hoy un estudiante durmió 7. ¿Cuántas horas le faltaron para llegar a 9?", "9-7", "La diferencia es lo que le faltó dormir."),
        ex("Tres frases: A) «Cada persona siente atracción en un momento distinto». B) «Si no te gusta nadie, estás mal». C) «Lo que sientes es privado». ¿Cuáles son correctas?", "A y C", "La B es falsa: no hay un momento correcto."),
    ],
    context=[ex("En el curso, un niño le dice a otro: «Me contaron que te gusta alguien». El segundo responde: «Prefiero no hablar de eso». ¿Usó su derecho a la privacidad?", "Sí", "Decidió no compartir algo personal.")],
    selfcheck=[ex("En Orientación: ¿los cambios de ánimo son parte de la pubertad?", "Sí", "Son cambios esperables."), ex("¿Puedes pedir privacidad?", "Sí", "Es una necesidad válida."), ex("¿Hay que burlarse de quien siente atracción?", "No", "Es privado de cada uno.")],
    task=T("Lee: Eli siente que su ánimo cambia mucho y quiere más tiempo a solas. Además, un compañero le preguntó si le gusta alguien. Escribe dos cosas que Eli necesita, una frase que Eli puede decirle al compañero y a quién puede contarle si se siente mal por mucho tiempo.", "Necesita dormir bien y privacidad. Frase: Prefiero no hablar de eso. Puede contarle a una persona adulta de confianza.", ["nombra dos necesidades", "escribe una frase que protege su privacidad", "dice a quién pedir ayuda"], ["texto escrito o dicho"], ["decir que lo normal es no tener cambios", "burlarse de lo que siente otro"], "Reconoce las necesidades y revisa que la frase sea firme y respetuosa."),
    reinforce="Escribe tres necesidades que podría tener un personaje en la pubertad y cómo cuidarlas.",
    extend="Escribe cómo reaccionarías si un compañero se burla de alguien porque le gusta otra persona.",
)

lesson(
    OA4, 3,
    "Una hoja y un lápiz. Los comentarios y los casos están escritos en los ejercicios. No se comparan cuerpos reales.",
    "Aprenderé a respetar los distintos ritmos de desarrollo de mis compañeros y a actuar si alguien se burla. Sirve para que todos nos sintamos seguros en el curso.",
    ["Sé que no hay calendario único.", "Sé que los cambios son privados."],
    [
        "El ritmo es la velocidad con que cada persona cambia en la pubertad. No hay ritmos mejores ni peores: unos cambian antes y otros después. Respetar los ritmos diversos significa tratar a todos con la misma dignidad, sin importar cómo vayan sus cambios.",
        "Hay conductas que no respetan los ritmos: burlarse, poner apodos por el cuerpo, comparar cuerpos, preguntar por partes privadas, tocar o mirar sin permiso, difundir rumores o comentar los cambios de otros. Aunque parezca una broma, puede dañar. Lo respetuoso es no comentar el cuerpo de los demás.",
        "Si alguien se burla, puedes decir «para, eso no está bien», acompañar a la persona afectada y avisar a un adulto. Si te burlan a ti, no es tu culpa y no estás solo: cuéntaselo a una persona adulta de confianza. Todos tenemos derecho a un curso donde nadie sea molestado por su cuerpo.",
    ],
    [("ritmo", "velocidad con que cada persona cambia"), ("respeto", "tratar bien al otro y aceptar que es distinto"), ("burla", "reírse de alguien para molestarlo"), ("apodo", "nombre que se pone a alguien, a veces para molestar"), ("rumor", "cosa que se dice de alguien sin saber si es cierta")],
    [
        W("Comentario respetuoso o no", "«Te veo más alto que antes» ¿es siempre respetuoso? ¿Y «mírenlo, qué cambiado está, jaja»?", ["Comentar el cuerpo de otro puede incomodar.", "Burlarse daña.", "Lo respetuoso es no comentar el cuerpo ajeno."], "Lo mejor es no comentar el cuerpo; la burla no es respetuosa"),
        W("Actuar frente a una burla", "Tres niños se ríen de Dino por su voz. ¿Qué puedes hacer: reírte con ellos o decir «para, eso no está bien» y avisar a un adulto?", ["Reírse apoya la burla.", "Decir para y avisar ayuda a Dino.", "Elige la segunda."], "Decir «para, eso no está bien» y avisar a un adulto"),
    ],
    [
        M("Creer que una burla sobre el cuerpo es solo un chiste.", "Se mira la intención y no el efecto.", "El impacto en la otra persona es lo que importa."),
        M("Pensar que si me burlan es mi culpa.", "Se cree que algo anda mal en mí.", "Nunca es tu culpa; cuéntalo a un adulto de confianza."),
    ],
    R=[
        ex("¿Burlarse del cuerpo de otro es respetuoso?", "No", "Puede dañar mucho."),
        ex("¿Poner un apodo por el cuerpo de alguien es respetuoso?", "No", "Puede hacerlo sentir mal."),
        ex("¿Todos tienen derecho a que nadie los moleste por su cuerpo?", "Sí", "Es parte del respeto."),
    ],
    U=[
        ex("¿Por qué aunque sea «una broma» puede dañar?", "Porque el efecto en la otra persona puede doler", "El impacto importa más que la intención."),
        ex("Si te burlan por tu cuerpo, ¿es tu culpa?", "No", "Nadie merece burlas."),
        ex("¿Qué puedes hacer si alguien se burla de otro?", "Decir para, apoyar y avisar a un adulto", "Así proteges a la persona."),
    ],
    A=[
        ex("Pedro dice «mira cómo suda Tomás, jaja». ¿Qué puedes decir tú?", "Para, eso no está bien", "Se detiene la burla con firmeza."),
        ex("Ana llora porque se burlaron de ella. Escribe una frase de apoyo que puedes decirle.", "No es tu culpa, estoy contigo", "Acompaña y no culpa."),
        ex("Un compañero pregunta a otro por una parte privada de su cuerpo. ¿Es una pregunta respetuosa?", "No", "Las partes privadas no se preguntan ni se comentan."),
    ],
    Z=[
        ex("Un niño dice: «Si solo lo miro y me río, no hago nada malo». ¿Es cierto?", "No", "Reírse apoya la burla."),
        ex("¿Qué es mejor: contar a un adulto una burla o esperar que se pase sola?", "Contarlo a un adulto", "Así se frena el daño."),
    ],
    D=[
        arith("En un juego de casos, 9 comentarios son respetuosos y 6 no lo son. ¿Cuántos comentarios hay en total?", "9+6", "Se suman ambos tipos."),
        ex("Tres frases: A) «No comento el cuerpo de nadie». B) «Le pongo un apodo a ver si se enoja». C) «Si me burlan, se lo cuento a un adulto». ¿Cuáles son respetuosas?", "A y C", "La B busca molestar."),
    ],
    context=[ex("En el recreo, unos niños se ríen de la voz de Dino. Eli dice: «Basta, eso duele» y luego avisa a la profesora. ¿Actuó con respeto?", "Sí", "Detuvo la burla y pidió ayuda.")],
    selfcheck=[ex("En Orientación: ¿hay ritmos de desarrollo mejores que otros?", "No", "Cada ritmo es válido."), ex("¿Se debe comentar el cuerpo de otros?", "No", "Puede incomodar o dañar."), ex("¿Puedes contar a un adulto si te burlan?", "Sí", "Siempre puedes pedir ayuda.")],
    task=T("Lee: unos niños llaman «pelusa» a Eli por el vello nuevo de sus piernas y se ríen. Escribe qué podría decir una compañera para detener la burla, qué podría decir Eli y a qué adulto podrían avisar. Escribe también una norma de curso que proteja a todos.", "Compañera: Para, eso no está bien. Eli: No me gusta que me digan eso. Pueden avisar a su profesora. Norma: No comentamos el cuerpo de nadie.", ["escribe frases claras y firmes", "nombra a un adulto de apoyo", "propone una norma respetuosa"], ["texto escrito o dicho"], ["justificar la burla", "culpar a Eli"], "Reconoce la intención de proteger y revisa que no se juzgue a ninguna persona."),
    reinforce="Escribe tres frases para detener una burla sobre el cuerpo.",
    extend="Propón dos normas de curso para que todos respeten los ritmos de desarrollo.",
)

lesson(
    OA4, 4,
    "Una hoja y un lápiz. Las fuentes de información y los casos están escritos en los ejercicios.",
    "Aprenderé a elegir fuentes confiables para mis dudas sobre la pubertad, a cuidarme y a pedir apoyo adulto. Sirve para decidir con información correcta y sentirme seguro.",
    ["Conozco los cambios físicos y afectivos.", "Sé que puedo preguntar a un adulto de confianza."],
    [
        "Cuando tienes una duda sobre la pubertad, la fuente importa. Una fuente confiable es una persona o un lugar que sabe del tema y cuida de ti: una persona adulta de confianza de tu casa, tu profesora, la orientadora o el personal de salud. También sirven los libros o materiales hechos por profesionales de la salud o por el Ministerio de Salud.",
        "Una fuente poco confiable es un rumor, un video sin autor conocido, un comentario de otro niño que dice saberlo todo o alguien que te pide guardar el secreto. Antes de creer algo, pregúntate: ¿quién lo dice?, ¿sabe del tema?, ¿me cuida? Si no estás seguro, pregunta a un adulto de confianza.",
        "El autocuidado en la pubertad incluye higiene: ducharte con regularidad, lavarte la cara y las manos, usar ropa limpia y, si un adulto te lo recomienda, desodorante. También incluye dormir bien, comer variado y moverte. Si algo te duele, te preocupa mucho o alguien te presiona, avisa a un adulto de confianza y sigue contando hasta que te ayuden.",
    ],
    [("fuente confiable", "persona o material que sabe del tema y me cuida"), ("rumor", "cosa que se dice sin saber si es cierta"), ("higiene", "limpieza que cuida mi cuerpo y mi salud"), ("autocuidado", "cuidar mi cuerpo y mis emociones"), ("apoyo adulto", "ayuda de una persona adulta de confianza")],
    [
        W("Elegir una fuente", "Lola tiene una duda sobre la pubertad. ¿A quién le conviene preguntar: a un rumor del patio o a la orientadora?", ["La orientadora sabe del tema y cuida a los estudiantes.", "Un rumor no se puede comprobar.", "Elige la orientadora."], "A la orientadora"),
        W("Probar la fuente con preguntas", "Un compañero dice: «Yo sé todo, pero no se lo cuentes a nadie». ¿Es una fuente confiable?", ["Pide guardar secreto.", "No se sabe si sabe del tema.", "No es confiable."], "No es confiable"),
    ],
    [
        M("Creer lo que dice un video porque tiene muchas visitas.", "Se piensa que lo popular es lo cierto.", "Pregunta quién lo hizo y consulta a un adulto de confianza."),
        M("Esperar a estar mal antes de pedir ayuda.", "Se piensa que hay que aguantar solo.", "Puedes pedir apoyo apenas tengas una duda o te sientas incómodo."),
    ],
    R=[
        ex("Una persona adulta de confianza, ¿es una fuente confiable para tus dudas?", "Sí", "Sabe del tema y te cuida."),
        ex("Un rumor del patio, ¿es una fuente confiable?", "No", "Nadie puede comprobar si es cierto."),
        ex("¿Ducharte con regularidad es parte de la higiene?", "Sí", "La higiene cuida el cuerpo."),
    ],
    U=[
        ex("Un video sobre la pubertad no muestra quién lo hizo. ¿Qué no puedes comprobar: si quien lo hizo sabe del tema o si el video es largo?", "Si quien lo hizo sabe del tema", "Sin autor conocido no se sabe si sabe del tema."),
        ex("Si alguien te dice «no se lo cuentes a nadie», ¿es buena señal?", "No", "Pedir secreto es una señal de alerta."),
        ex("¿Puedes pedir ayuda apenas tengas una duda?", "Sí", "No tienes que esperar a sentirte mal."),
    ],
    A=[
        ex("Clasifica estas fuentes: «la orientadora», «un video sin autor», «un material del Ministerio de Salud». ¿Cuántas son confiables?", "2", "La orientadora y el material del Ministerio son confiables."),
        ex("Pía nota que suda más. ¿Qué acción de higiene puede hacer: ducharse y usar ropa limpia o taparse con más ropa?", "Ducharse y usar ropa limpia", "Es una conducta de higiene."),
        ex("Dino tiene una duda y un compañero mayor le dice «te lo cuento, pero es secreto». ¿Qué debe hacer Dino?", "Preguntar a un adulto de confianza", "Un secreto no es una fuente confiable."),
    ],
    Z=[
        ex("Una niña dice: «Si algo me preocupa, mejor lo aguanto sola». ¿Es buena idea?", "No", "Contarlo a un adulto de confianza ayuda."),
        ex("Un video dice que todos deben cambiar a la misma edad. ¿Cómo comprobarías si es cierto?", "Preguntando a un adulto de confianza o a un profesional de la salud", "Hay que contrastar con una fuente confiable."),
    ],
    D=[
        arith("En una lista hay 10 fuentes de información. 6 son confiables. ¿Cuántas no lo son?", "10-6", "Se resta lo confiable del total."),
        ex("Tres frases: A) «Pregunto a mi profesora». B) «Creo lo que dice el patio». C) «Pido ayuda a un adulto de confianza». ¿Cuáles son buenas decisiones?", "A y C", "La B depende de rumores."),
    ],
    context=[ex("Joaquín leyó en un chat que «a todos les cambia la voz a los 10 años». Se lo cuenta a su orientadora, que le explica que no hay una edad única. ¿Hizo bien en consultar?", "Sí", "Verificó con una fuente confiable.")],
    selfcheck=[ex("En Orientación: ¿un rumor es una fuente confiable?", "No", "No se puede comprobar."), ex("¿La higiene es parte del autocuidado en la pubertad?", "Sí", "Cuida el cuerpo."), ex("¿Puedes pedir ayuda a un adulto de confianza?", "Sí", "Siempre puedes pedirla.")],
    task=T("Lee: Marta quiere saber qué pasa en el cuerpo durante la pubertad. Tiene estas opciones: un comentario del patio, su profesora, un video sin autor y un libro de salud de la biblioteca. Escribe cuáles elegirías y por qué, con las tres preguntas (¿quién lo dice?, ¿sabe del tema?, ¿me cuida?). Después escribe dos hábitos de higiene para la pubertad.", "Elijo a mi profesora y el libro de salud, porque saben del tema y me cuidan. Higiene: ducharme y lavarme la cara.", ["elige fuentes confiables", "explica con las tres preguntas", "escribe dos hábitos de higiene"], ["texto escrito o dicho"], ["creer rumores", "no pedir ayuda"], "Reconoce las fuentes y revisa que explique con las preguntas."),
    reinforce="Haz una lista de tres adultos o lugares donde podrías consultar tus dudas.",
    extend="Elabora un cartel con tres preguntas para decidir si una fuente es confiable.",
)
