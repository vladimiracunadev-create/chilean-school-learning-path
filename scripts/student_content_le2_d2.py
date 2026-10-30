"""Cuaderno del estudiante, 2.º básico Lenguaje y Comunicación: OA 26 (convenciones sociales) y OA 27 (exposición oral)."""
from __future__ import annotations

from student_lessons import ex, register

OA26, OA27 = "LE02 OA 26", "LE02 OA 27"
E = ex


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, ctx, sc, open_args, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=ctx, selfcheck=sc, open_task=task(*open_args), reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 26
reg(
    OA26, 1,
    "Este cuaderno, lápiz y una hoja. Un adulto o un muñeco como compañero de juego.",
    "Aprenderé a presentarme y a presentar a otra persona dando solo los datos útiles. Sirve para empezar bien un encuentro y cuidar mi privacidad.",
    ["Sé saludar.", "Sé decir mi nombre."],
    [
        "Cuando conocemos a alguien, nos presentamos. Primero saludamos: «Hola» o «Buenos días». Luego decimos nuestro nombre y, si queremos, algo que nos gusta o en qué curso estamos. Por ejemplo: «Hola, me llamo Ema y me gusta dibujar».",
        "También podemos presentar a otra persona. Decimos: «Te presento a mi amigo Pablo». Después agregamos un dato breve: «Juega a la pelota». La persona presentada responde: «Mucho gusto». Presentar bien ayuda a que dos personas se conozcan.",
        "Hay datos que no conviene decir a alguien que recién conocemos, como la dirección de la casa o el número de teléfono. Para presentarse basta el nombre y un gusto. Elegir información pertinente es decir lo que sirve para ese momento y nada más.",
    ],
    [("presentarse", "decir quién soy a alguien nuevo"), ("presentar", "decir quién es otra persona"), ("saludo", "palabras para empezar un encuentro"), ("dato", "información breve"), ("pertinente", "que sirve para ese momento")],
    [
        ("Presentarme", "Llegas a un curso nuevo. Te llamas Ema y te gusta dibujar. ¿Cómo te presentas?", ["Saludo.", "Digo mi nombre.", "Agrego un gusto."], "Hola, me llamo Ema y me gusta dibujar."),
        ("Presentar a otro", "Quieres que tu amiga Luz conozca a tu amigo Pablo, que juega a la pelota. ¿Qué dices?", ["Nombro a los dos.", "Doy un dato de Pablo.", "Espero el «mucho gusto»."], "Luz, te presento a mi amigo Pablo. Le gusta jugar a la pelota."),
    ],
    [("Decir la dirección de la casa al conocer a alguien.", "Se cree que hay que dar muchos datos.", "Basta el nombre y un gusto."), ("Presentar solo a uno.", "Se olvida nombrar a la otra persona.", "Nombra a las dos.")],
    [
        E("Para presentarme, ¿digo mi nombre o mi dirección?", "Mi nombre", "La dirección es un dato privado."),
        E("«Hola, me llamo Tito» ¿es una presentación o una despedida?", "Una presentación", "Dice quién es."),
        E("Cuando me presentan, ¿qué puedo responder: «mucho gusto» o «adiós»?", "Mucho gusto", "Es el saludo para conocer a alguien."),
    ],
    [
        E("¿Qué es presentarse?", "Decir quién soy a alguien nuevo", "Así nos conocemos."),
        E("¿Por qué no digo mi teléfono a alguien que recién conozco?", "Porque es un dato privado", "Cuido mi seguridad."),
        E("¿Qué dos datos bastan en una presentación?", "El nombre y un gusto", "Son útiles y seguros."),
    ],
    [
        E("Te llamas Nico y te gusta jugar fútbol. Escribe tu presentación a una niña nueva.", "Hola, me llamo Nico y me gusta jugar fútbol", "Incluye saludo, nombre y gusto."),
        E("Quieres presentar a tu prima Sofía, que toca guitarra, con tu amigo Leo. Escribe qué dices.", "Leo, te presento a mi prima Sofía. Ella toca guitarra", "Nombra y da un dato."),
        E("Alguien te dice «Hola, soy Ana». Escribe una respuesta cortés.", "Hola, mucho gusto, yo soy…", "Responde con saludo y nombre."),
    ],
    [
        E("Teo se presenta: «Hola, soy Teo, vivo en calle Los Olmos 123». ¿Dio un dato que no convenía?", "Sí, la dirección", "La dirección es privada."),
        E("Lía presenta a Pepe sin decir su nombre: «Este es mi amigo». ¿Se entiende quién es?", "No", "Falta su nombre."),
    ],
    [
        E("Elige la mejor presentación: a) «Hola.» b) «Hola, me llamo Rosa y me gusta pintar.»", "b", "Tiene nombre y un dato."),
        E("Ordena: a) Me llamo Julia, b) Hola, c) y me gusta leer.", "b, a, c", "Primero se saluda, luego el nombre y el gusto."),
    ],
    [E("En el cumpleaños de un primo conoces a un niño nuevo. Tu amigo Beto llega después. Escribe cómo te presentas al niño y cómo presentas a Beto (a Beto le gusta pintar).", "Hola, me llamo… Te presento a mi amigo Beto, le gusta pintar", "Tiene presentación y presentación a otro.")],
    [
        E("¿Saludar es parte de presentarse?", "Sí", "Se parte con un saludo."),
        E("¿Debo decir todos mis datos personales?", "No", "Solo los que sirven."),
        E("¿Puedo presentar a un amigo a otra persona?", "Sí", "Así se conocen."),
    ],
    ("Practica con un adulto. Haz dos presentaciones: 1) Preséntate como si llegaras a una clase nueva. Usa saludo, tu nombre y un gusto. 2) Presenta a un amigo imaginario: Luz, a quien le gusta nadar, a tu compañero Diego. Diego debe responder «mucho gusto». No digas dirección ni teléfono.",
     "1) Hola, me llamo Marta y me gusta dibujar. 2) Diego, te presento a Luz. A ella le gusta nadar. Diego: Mucho gusto.",
     ["saluda y dice el nombre", "da un dato pertinente y seguro", "presenta a otra persona y espera la respuesta"], ["práctica ante un adulto", "frase escrita"], ["dar datos privados", "olvidar nombrar"],
     "Si dice la dirección, explica que es mejor guardarla para personas de confianza."),
    "Preséntate a un muñeco como si fuera nuevo en tu casa.",
    "Presenta a dos personas que no se conocen y cuenta un gusto que tengan en común.",
)

reg(
    OA26, 2,
    "Este cuaderno, lápiz y una hoja. Un adulto para practicar peticiones.",
    "Aprenderé a pedir cosas y permisos, y a preguntar de manera clara y respetuosa. Sirve para conseguir ayuda sin molestar.",
    ["Sé saludar y presentarme.", "Sé decir por favor."],
    [
        "Una petición es cuando pedimos algo, como un lápiz o ayuda. Para pedir con respeto, usamos «por favor» y una voz tranquila. Por ejemplo: «¿Me prestas tu goma, por favor?». También decimos claramente qué necesitamos.",
        "Un permiso es cuando pedimos autorización para hacer algo. Usamos «¿puedo…?» o «con permiso». Por ejemplo: «¿Puedo salir al baño?» o «Con permiso, voy a pasar». Esperamos la respuesta antes de actuar.",
        "También preguntamos para saber algo: «¿A qué hora es el recreo?». Una buena petición es clara, corta y amable. Si nos dicen que no, aceptamos con calma y decimos «está bien». Un «no» no es una falta de respeto hacia nosotros.",
    ],
    [("petición", "cuando pido algo"), ("permiso", "autorización para hacer algo"), ("por favor", "fórmula de cortesía para pedir"), ("claro", "que se entiende bien"), ("aceptar", "recibir una respuesta con calma")],
    [
        ("Pedir con claridad", "Necesitas una goma. Tu compañera tiene dos. ¿Cómo la pides?", ["Digo qué necesito.", "Uso por favor.", "Hablo con tono amable."], "¿Me prestas una goma, por favor?"),
        ("Pedir permiso", "Quieres salir al baño durante la clase. ¿Qué le dices a la profesora?", ["Uso «¿puedo…?».", "Digo para qué.", "Espero su respuesta."], "Profesora, ¿puedo salir al baño, por favor?"),
    ],
    [("Tomar sin preguntar.", "Se cree que no hace falta pedir.", "Pide permiso antes de usar algo ajeno."), ("Enojarse si dicen que no.", "Se confunde el no con una ofensa.", "Di «está bien» y pregunta otra vez más tarde si corresponde.")],
    [
        E("¿Qué es más cortés: «¡Dame ese lápiz!» o «¿Me prestas ese lápiz, por favor?»", "¿Me prestas ese lápiz, por favor?", "Usa por favor y un tono amable."),
        E("Si quiero salir de la sala, ¿pido permiso o salgo sin avisar?", "Pido permiso", "Se debe avisar antes."),
        E("Si me dicen que no, ¿acepto con calma o grito?", "Acepto con calma", "Un no no es una ofensa."),
    ],
    [
        E("¿Qué es una petición?", "Cuando pido algo", "Pido ayuda o un objeto."),
        E("¿Por qué uso «por favor»?", "Porque es una fórmula de cortesía", "Hace la petición amable."),
        E("¿Para qué sirve decir «¿puedo…?» antes de actuar?", "Para pedir permiso antes de actuar", "Espero la autorización."),
    ],
    [
        E("Quieres el agua de tu compañero. Escribe cómo la pides.", "¿Me das un poco de agua, por favor?", "Es clara y cortés."),
        E("Quieres pasar entre dos personas que conversan. Escribe qué dices.", "Con permiso", "Es la fórmula para pasar."),
        E("No sabes a qué hora termina la clase. Escribe una pregunta cortés a tu profesora.", "Profesora, ¿a qué hora termina la clase, por favor?", "Pregunta clara y respetuosa."),
    ],
    [
        E("Nico dice: «Dame la regla». Ana dice: «¿Me prestas la regla, por favor?». ¿Quién pidió mejor?", "Ana", "Usó una fórmula de cortesía."),
        E("Rita pide el columpio y le responden: «Ahora no». Ella dice: «Está bien, espero». ¿Reaccionó con calma?", "Sí", "Aceptó la respuesta."),
    ],
    [
        E("Quieres un lápiz prestado y dices «Lápiz». ¿La petición es clara y amable?", "No", "Falta una frase completa con cortesía, como «¿Me prestas un lápiz, por favor?»."),
        E("Escoge la mejor petición: a) «Necesito ayuda con esto.» b) «¿Puedes ayudarme con esta tarea, por favor?»", "b", "La b es clara, amable y completa."),
    ],
    [E("En una tienda de barrio quieres un pan. El vendedor está ocupado. Escribe cómo pides atención y luego el pan, con cortesía.", "Disculpe, ¿me puede atender, por favor? Quiero un pan, por favor", "Pide atención y pan con cortesía.")],
    [
        E("¿«Con permiso» sirve para pasar?", "Sí", "Es una fórmula de cortesía."),
        E("¿Es mejor pedir con «por favor»?", "Sí", "Se ve amable."),
        E("¿Debo agarrar algo ajeno sin preguntar?", "No", "Se debe pedir."),
    ],
    ("Practica peticiones. Con un adulto, haz estas cuatro: 1) Pide prestado un lápiz. 2) Pide permiso para salir a jugar. 3) Pregunta a qué hora es la cena. 4) Pide pasar por un pasillo angosto. Cada una debe ser clara y cortés. El adulto responderá sí en dos y no en dos; acepta con calma.",
     "1) ¿Me prestas un lápiz, por favor? 2) ¿Puedo salir a jugar, por favor? 3) ¿A qué hora es la cena? 4) Con permiso. Cuando dijo que no, respondí: está bien.",
     ["usa fórmulas de cortesía", "la petición es clara", "acepta con calma un no"], ["práctica ante un adulto"], ["pedir sin cortesía", "enojarse con el no"],
     "Si se molesta con el no, practica decir «está bien» y pregunta si puede intentar otra vez después."),
    "Pide con cortesía algo en tu casa, como el pan, durante la comida.",
    "Escribe tres formas distintas de pedir ayuda a un adulto, con cortesía.",
)

reg(
    OA26, 3,
    "Este cuaderno, lápiz y una hoja. Un adulto para practicar.",
    "Aprenderé a dar las gracias y a responder cuando nos las dan. Sirve para cerrar un encuentro reconociendo la ayuda que recibimos.",
    ["Sé pedir por favor.", "Sé que ayudar es una buena acción."],
    [
        "Agradecer es reconocer que alguien nos ayudó o hizo algo bueno por nosotros. La palabra más usada es «gracias». Podemos agregar qué agradecemos: «Gracias por prestarme tu lápiz». Así la otra persona sabe por qué estamos contentos.",
        "Cuando alguien nos da las gracias, respondemos con «de nada», «con gusto» o «no hay de qué». Esa respuesta cierra el intercambio con cariño. Responder bien muestra que ayudar no fue una molestia.",
        "Agradecer también se hace con una mirada y una sonrisa. Si me ayudan, digo gracias con voz amable y, si me resulta cómodo, miro a la persona. Si la ayuda fue grande, puedo agregar: «Me ayudaste mucho». No agradecemos con burla: sería menos sincero. Cada persona agradece a su manera, con palabras, una sonrisa o un gesto.",
    ],
    [("agradecer", "reconocer una ayuda con palabras"), ("gracias", "palabra para agradecer"), ("de nada", "respuesta cuando nos dan las gracias"), ("ayuda", "apoyo que damos o recibimos"), ("sincero", "que dice lo que de verdad siente")],
    [
        ("Agradecer con motivo", "Marta te prestó su lápiz. ¿Cómo le agradeces?", ["Digo gracias.", "Agrego por qué agradezco.", "La miro."], "Gracias por prestarme tu lápiz."),
        ("Responder a un agradecimiento", "Tu amigo te dice: «Gracias por ayudarme con la tarea». ¿Qué respondes?", ["Escucho el gracias.", "Elijo una respuesta cortés.", "Sonrío."], "De nada, con gusto."),
    ],
    [("Decir gracias de mala gana, entre dientes.", "Se agradece por obligación.", "Di gracias con voz amable y con sinceridad."), ("No responder cuando me agradecen.", "Se cree que no hace falta.", "Responde «de nada» o «con gusto».")],
    [
        E("Si me ayudan, ¿digo gracias o digo adiós?", "Gracias", "Reconozco la ayuda."),
        E("Me dicen «gracias». ¿Qué respondo: «de nada» o «mañana»?", "De nada", "Es la respuesta cortés."),
        E("¿Agradezco con una sonrisa o con mala cara?", "Con una sonrisa", "Se ve sincero."),
    ],
    [
        E("¿Qué significa agradecer?", "Reconocer una ayuda con palabras", "Muestro que lo valoro."),
        E("¿Por qué conviene decir por qué agradezco?", "Para que la otra persona sepa qué valoré", "Así sabe cuál ayuda me sirvió."),
        E("¿Qué muestra responder «con gusto»?", "Que ayudar no fue una molestia", "Responde con cariño."),
    ],
    [
        E("Tu profesora te explicó otra vez un ejercicio. Escribe cómo le agradeces.", "Gracias por explicarme otra vez", "Agradece y dice por qué."),
        E("Una compañera te dijo «gracias por esperarme». Escribe tu respuesta.", "De nada, con gusto", "Responde con cortesía."),
        E("Un vecino te abrió la puerta cuando llevabas bolsas. Escribe qué le dices.", "Gracias por abrirme la puerta", "Dice gracias y el motivo."),
    ],
    [
        E("Pedro dice solo «gracias». Rosa dice «gracias por ayudarme con mi mochila». ¿Quién dijo el motivo de su agradecimiento?", "Rosa", "Nombró la ayuda que recibió."),
        E("Luis le dijo «gracias» a Eva y ella no respondió nada. ¿Cerró bien el intercambio?", "No", "Faltó una respuesta cortés."),
    ],
    [
        E("Elige el mejor agradecimiento: a) «Ya.» b) «Gracias por compartir tu colación, estaba muy rica.»", "b", "La b nombra la ayuda y su valor."),
        E("Ordena: a) Gracias por ayudarme, b) Me ayudaste con mi mochila, c) De nada, con gusto.", "b, a, c", "Ayuda, agradecimiento y respuesta."),
    ],
    [E("Un compañero te pasó el cuaderno que se te cayó, delante de toda la clase. Escribe qué le dices y qué responde él.", "Tú: Gracias por pasarme el cuaderno. Él: De nada", "Hay gracias con motivo y respuesta.")],
    [
        E("¿«De nada» es una respuesta a «gracias»?", "Sí", "Cierra el intercambio."),
        E("¿Puedo agradecer con una sonrisa?", "Sí", "También muestra gratitud."),
        E("¿Debo agradecer solo cuando la ayuda es grande?", "No", "Se puede agradecer siempre."),
    ],
    ("Practica agradecer y responder con un adulto. Cuatro casos: 1) alguien te presta un lápiz, 2) alguien te sirve la comida, 3) alguien te abre una puerta, 4) alguien te enseña a amarrarte los cordones. En cada caso di gracias con el motivo. Luego cambien de rol: el adulto te agradece y tú respondes con una fórmula distinta cada vez.",
     "1) Gracias por prestarme el lápiz. 2) Gracias por servirme la comida. 3) Gracias por abrir la puerta. 4) Gracias por enseñarme a amarrarme los cordones. Cuando me agradecieron respondí: de nada, con gusto y no hay de qué.",
     ["agradece con motivo", "usa un tono amable", "responde de tres maneras distintas"], ["práctica ante un adulto"], ["decir solo «gracias» sin motivo", "no responder"],
     "Si repite siempre lo mismo, enséñale otras respuestas: con gusto, no hay de qué."),
    "Agradece a alguien de tu casa por algo que hizo hoy.",
    "Escribe una nota de agradecimiento breve a alguien que te ayudó esta semana.",
)

reg(
    OA26, 4,
    "Este cuaderno, lápiz y una hoja. Un adulto para practicar.",
    "Aprenderé a pedir perdón de forma sincera y a proponer cómo arreglar lo que pasó. Sirve para cuidar a las personas cuando nos equivocamos.",
    ["Sé que puedo equivocarme.", "Sé decir gracias y por favor."],
    [
        "A veces hacemos algo que molesta o lastima a otra persona, aunque no queramos. Pedir perdón es reconocer que nos equivocamos. Una buena disculpa tiene tres partes: digo qué hice, digo «perdón» y propongo cómo arreglarlo.",
        "Por ejemplo: «Perdón, rompí tu dibujo sin querer. Voy a ayudarte a hacer otro». Decir qué hice muestra que me hago cargo. Proponer cómo reparar muestra que me importa la otra persona. Las excusas como «fue culpa tuya» no sirven para disculparse.",
        "Quien recibe la disculpa puede aceptar o necesitar tiempo. Puede decir «está bien» o «gracias por decírmelo». Si todavía está molesto, esperamos y no insistimos. Una disculpa sincera cuida la relación, pero no borra lo que pasó de inmediato.",
    ],
    [("disculpa", "palabras con las que reconozco un error"), ("perdón", "palabra para pedir disculpas"), ("reparar", "arreglar lo que se dañó"), ("excusa", "razón para no hacerme cargo"), ("sincero", "que dice lo que de verdad siente")],
    [
        ("Armar una disculpa", "Sin querer, pisaste el cuaderno de Ema y lo ensuciaste. ¿Qué le dices?", ["Digo qué hice.", "Pido perdón.", "Propongo repararlo."], "Perdón, ensucié tu cuaderno sin querer. Voy a limpiarlo."),
        ("Detectar una excusa", "Tomás dice: «Perdón, pero fue culpa tuya que me empujaras». ¿Es una buena disculpa?", ["Veo que culpa a otra persona.", "Eso es una excusa.", "No se hace cargo."], "No, culpar a otra persona no es una disculpa."),
    ],
    [("Decir «perdón» sin explicar qué hice.", "Se dice por salir del paso.", "Di qué hiciste y cómo arreglarlo."), ("Exigir que me perdonen enseguida.", "Se olvida que el otro necesita tiempo.", "Espera con paciencia y respeta su decisión.")],
    [
        E("Si rompo algo por accidente, ¿pido perdón o me quedo callado?", "Pido perdón", "Reconozco mi error."),
        E("«Perdón, rompí tu lápiz. Te regalo otro.» ¿Ofrece reparar?", "Sí", "Propone arreglar el daño."),
        E("«Fue culpa tuya» ¿es una disculpa o una excusa?", "Una excusa", "No se hace cargo."),
    ],
    [
        E("¿Cuáles son las tres partes de una buena disculpa?", "Decir qué hice, pedir perdón y proponer reparar", "Muestran responsabilidad y cuidado."),
        E("En Lenguaje: ¿Qué es reparar?", "Arreglar lo que se dañó", "Compenso el error."),
        E("Si la persona sigue molesta, ¿qué hago?", "Espero y no insisto", "Ella necesita tiempo."),
    ],
    [
        E("Sin querer le diste un pelotazo a Lía. Escribe tu disculpa con las tres partes.", "Perdón, te di un pelotazo sin querer. ¿Estás bien? Voy a tener más cuidado", "Dice qué hice, perdón y una forma de arreglar."),
        E("Rompiste el vaso de tu hermana. Escribe cómo repararías.", "Por ejemplo: Le ayudo a recoger los pedazos y le doy uno de los míos", "Repara el daño."),
        E("Llegaste tarde a una cita con tu amiga. Escribe una disculpa sin excusas.", "Perdón por llegar tarde. La próxima vez saldré antes", "Reconoce y propone cambio."),
    ],
    [
        E("Ana: «Perdón, pero tú me distrajiste». Beto: «Perdón, rompí tu hoja. Voy a escribir otra». ¿Quién se disculpó mejor?", "Beto", "Beto se hizo cargo y propuso reparar."),
        E("Rosa pidió perdón, pero Camilo no quiso hablar todavía. ¿Rosa debe pedirle diez veces seguidas que la perdone?", "No", "Debe respetar su tiempo."),
    ],
    [
        E("Elige la mejor disculpa: a) «Perdón, pero tú empezaste.» b) «Perdón por gritarte. Voy a hablar más bajito.»", "b", "La b se hace cargo y propone cambio."),
        E("Ordena una disculpa: a) Voy a ayudarte a limpiarlo, b) Perdón, c) Derramé tu jugo.", "c, b, a", "Qué hice, perdón y reparar."),
    ],
    [E("En el recreo, sin querer, empujaste a un compañero y se le cayó su colación. Escribe qué le dices y cómo reparas.", "Perdón, te empujé sin querer y se cayó tu colación. Voy a ayudarte a recogerla y te doy parte de la mía", "Tiene las tres partes.")],
    [
        E("¿Pedir perdón es reconocer un error?", "Sí", "Así muestro responsabilidad."),
        E("¿Una excusa ayuda a disculparse?", "No", "No se hace cargo del error."),
        E("¿Puedo ofrecer arreglar lo que dañé?", "Sí", "Eso es reparar."),
    ],
    ("Practica disculparte. Lee estas tres situaciones y escribe una disculpa con las tres partes: 1) Sin querer rompiste el dibujo de tu amiga. 2) Hablaste en voz alta mientras alguien leía. 3) Prometiste ayudar y te olvidaste. No uses excusas. Luego di qué harías si una de esas personas no quiere hablar todavía.",
     "1) Perdón, rompí tu dibujo sin querer. Voy a ayudarte a hacer otro. 2) Perdón por hablar fuerte mientras leías. Voy a hablar bajito. 3) Perdón, me olvidé de ayudarte. Ahora puedo hacerlo. Si no quiere hablar, espero y le digo que estoy aquí.",
     ["dice qué hizo", "pide perdón sin excusas", "propone cómo reparar"], ["tres disculpas escritas u orales"], ["usar excusas", "no reparar"],
     "Si usa una excusa, pídele que quite la parte que culpa a otro y la reemplace por qué hizo él."),
    "Cuenta a un adulto una vez en que te equivocaste y cómo lo arreglaste.",
    "Escribe una disculpa para alguien que no quiere hablar todavía, sin insistir.",
)

reg(
    OA26, 5,
    "Este cuaderno, lápiz y una hoja. Un adulto para practicar.",
    "Aprenderé a elegir palabras y tono según con quién hablo y dónde estoy. Sirve para ser cortés en cada situación.",
    ["Sé saludar, pedir y agradecer.", "Sé pedir perdón."],
    [
        "No hablamos igual con todas las personas ni en todos los lugares. El contexto es la situación donde hablamos: quién está, dónde estamos y para qué. Con un amigo en el patio podemos decir «hola». Con la directora decimos «buenos días, señora directora».",
        "El tono es cómo suena la voz: suave, fuerte, amable, serio. En la biblioteca usamos un tono bajito. En una fiesta, uno más alegre. Aunque digamos «por favor» y «gracias», si el tono es enojado o burlón, no suena cortés.",
        "Antes de hablar podemos preguntarnos: ¿con quién hablo?, ¿dónde estoy? y ¿qué quiero decir? Con adultos que no conocemos, usamos «usted». Con amigos, «tú». En algunas familias y escuelas se usa «tú» con adultos cercanos: lo importante es el respeto. También expresamos opiniones y sentimientos con respeto, sin gritar ni burlarnos: «Me sentí mal cuando…, ¿podemos…?». Elegir bien las palabras muestra respeto. Si me equivoco, puedo corregir con calma.",
    ],
    [("contexto", "situación en la que hablo"), ("tono", "forma en que suena mi voz"), ("usted", "forma respetuosa de hablar a adultos"), ("formal", "forma respetuosa de hablar en situaciones serias"), ("informal", "forma relajada de hablar con amigos")],
    [
        ("Cambiar según con quién hablo", "Debes saludar a la directora y a un amigo. ¿Cómo saludas a cada uno?", ["Pienso en quién es.", "Con la directora uso un saludo respetuoso.", "Con el amigo uso uno cercano."], "Directora: Buenos días, señora directora. Amigo: ¡Hola!"),
        ("Cambiar según el lugar", "Estás en la biblioteca y quieres pedir un libro. ¿Cómo hablas?", ["Pienso en el lugar.", "Uso un tono bajo.", "Pido con cortesía."], "Con tono bajito: Disculpe, ¿me presta este libro, por favor?"),
    ],
    [("Hablar igual a todos.", "No se piensa en el contexto.", "Pregúntate con quién y dónde hablas."), ("Decir «gracias» con tono burlón.", "El tono no combina con la palabra.", "Usa un tono amable.")],
    [
        E("A un adulto que no conoces, ¿le hablas de «usted» o de «tú»?", "De usted", "Es más respetuoso."),
        E("En la biblioteca, ¿hablas bajito o gritas?", "Bajito", "Cuidas el silencio."),
        E("Saludar a un amigo con «¡hola!» en el patio, ¿es adecuado o poco adecuado?", "Adecuado", "Es un contexto relajado."),
    ],
    [
        E("En Lenguaje: ¿Qué es el contexto?", "La situación en la que hablo", "Incluye quién, dónde y para qué."),
        E("¿Por qué el tono importa?", "Porque cambia cómo suena lo que digo", "Un tono enojado quita cortesía."),
        E("¿Qué me conviene preguntar antes de hablar?", "Con quién hablo y dónde estoy", "Así elijo mis palabras."),
    ],
    [
        E("Escribe cómo saludas a tu vecina adulta que no conoces bien.", "Buenos días, ¿cómo está usted?", "Usa un saludo respetuoso."),
        E("Escribe cómo saludas a un amigo del curso en el recreo.", "¡Hola! ¿Jugamos?", "Es un saludo cercano."),
        E("Un compañero se metió delante de ti en la fila y te sentiste molesto. Escribe cómo se lo dices con respeto.", "Me sentí molesto porque me pasaste. ¿Puedes ponerte atrás, por favor?", "Dice el sentimiento y la petición con cortesía, sin ofender."),
    ],
    [
        E("Ema dice «gracias» gritando y con cara de enojo. ¿Suena cortés?", "No", "El tono no combina con la palabra."),
        E("Luis habla de «tú» al director en una reunión formal. ¿Qué debe cambiar?", "Hablar de usted", "Es lo respetuoso."),
    ],
    [
        E("Un niño llega a una consulta médica y le dice al doctor «¡Oye, tú!». ¿Eligió bien su forma de hablar?", "No", "Debe hablar con respeto a un adulto."),
        E("Elige la mejor forma de pedir ayuda a una persona mayor en la calle: a) «¡Ayúdame ya!» b) «Disculpe, señor, ¿me puede ayudar, por favor?»", "b", "La b usa usted y cortesía."),
    ],
    [E("Tres situaciones: con un amigo en tu casa, con tu profesora en la sala y con el doctor en la consulta. Escribe cómo pides agua en cada una.", "Amigo: ¿Me das agua? Profesora: ¿Puedo tomar agua, por favor? Doctor: Disculpe, ¿me puede dar un vaso con agua, por favor?", "Cambia según el contexto.")],
    [
        E("¿Hablo igual en una fiesta que en la biblioteca?", "No", "Cambia el contexto."),
        E("¿Es respetuoso hablar de usted a un adulto desconocido?", "Sí", "Es una forma formal."),
        E("¿Puedo ser cortés y tener un tono enojado a la vez?", "No", "El tono resta cortesía."),
    ],
    ("Elige tus palabras según el contexto. Escribe o di cómo pedirías un vaso de agua en estos tres lugares: 1) en tu casa con un hermano, 2) en la sala con tu profesora, 3) en un consultorio con un doctor que no conoces. Practica con un adulto y fíjate en tu tono de voz.",
     "1) ¿Me pasas agua? 2) Profesora, ¿puedo tomar agua, por favor? 3) Disculpe, doctor, ¿me puede dar agua, por favor? Usé un tono tranquilo en las tres.",
     ["cambia las palabras según el contexto", "usa fórmulas de cortesía", "mantiene un tono amable"], ["práctica ante un adulto", "tres frases escritas u orales"], ["usar las mismas palabras en todas", "tono enojado"],
     "Si usa las mismas palabras, pregunta quién escucha y si cambiaría el saludo."),
    "Saluda de formas distintas a tres personas de tu casa o barrio.",
    "Escribe cómo cambiarías una petición para hacerla más formal.",
)

# ================================================================ OA 27
reg(
    OA27, 1,
    "Este cuaderno, lápiz y una hoja. Un adulto como oyente.",
    "Aprenderé a escoger un tema para contar y a delimitarlo para que sea breve. Sirve para preparar una exposición clara.",
    ["Sé contar algo que me pasó.", "Sé hablar con voz audible."],
    [
        "Una exposición oral es cuando presento información (cómo es mi gato) o narro un evento (el día que fui a la playa) a un grupo. Primero elijo un tema que me guste y que conozca. Por ejemplo: mi mascota, un juego o un viaje. Si conozco el tema, hablo con más seguridad.",
        "Un tema muy grande, como «los animales», es difícil de contar en poco tiempo. Por eso lo acoto, es decir, lo hago más pequeño y preciso. En vez de «los animales», elijo «mi gato Pelusa y lo que come». Un tema acotado cabe en un minuto.",
        "También decido qué dejo fuera. Para hablar de mi gato Pelusa, cuento cómo es y qué come. No hablo de todos los gatos del mundo. Al final escribo una frase que resume mi tema: «Hoy les hablaré de lo que come mi gato Pelusa».",
    ],
    [("exposición", "presentar información a un grupo"), ("tema", "de qué voy a hablar"), ("acotar", "hacer un tema más pequeño y preciso"), ("dejar fuera", "no incluir algo para no alargarme"), ("audiencia", "personas que escuchan")],
    [
        ("Acotar un tema grande", "Quieres hablar de «los animales», pero es muy grande. ¿Cómo lo acotas?", ["Elijo un animal que conozco.", "Elijo un aspecto: qué come.", "Escribo el tema nuevo."], "Lo que come mi gato Pelusa."),
        ("Decir qué dejo fuera", "Tema: mi viaje a la playa. ¿Qué dejas fuera para hablar solo un minuto?", ["Cuento lo más importante.", "Dejo fuera los detalles que no ayudan.", "Escribo mi decisión."], "Cuento qué hice en la arena y dejo fuera el viaje en auto."),
    ],
    [("Escoger un tema demasiado grande.", "Se cree que más información es mejor.", "Acótalo: elige una parte."), ("Hablar de algo que no conozco.", "Se escogió por moda.", "Escoge un tema que sepas contar.")],
    [
        E("¿Es mejor el tema «los deportes» o «mi deporte favorito: nadar»?", "Mi deporte favorito: nadar", "Está más acotado."),
        E("Para acotar, ¿hago el tema más grande o más pequeño?", "Más pequeño", "Acotar es precisar."),
        E("«Cómo es mi gato» y «El día que fui a la playa». ¿Cuál narra un evento?", "El día que fui a la playa", "Cuenta algo que pasó, en orden."),
    ],
    [
        E("¿Qué es una exposición oral?", "Presentar información a un grupo hablando", "Es hablar para una audiencia."),
        E("¿Por qué conviene acotar el tema?", "Para que quepa en poco tiempo", "Un tema pequeño se explica mejor."),
        E("¿Qué es «dejar fuera»?", "No incluir algo para no alargarme", "Se elige lo más importante."),
    ],
    [
        E("Acota el tema «las frutas» a algo que cabría en un minuto.", "Por ejemplo: mi fruta favorita, la frutilla", "Es una parte del tema grande."),
        E("Tema: mi cumpleaños. Escribe dos cosas que contarías y una que dejarías fuera.", "Contaría la torta y los juegos; dejaría fuera la lista de invitados", "Distingue lo importante."),
        E("Escribe la frase que resume el tema «mi bicicleta nueva».", "Por ejemplo: Hoy les hablaré de mi bicicleta nueva", "Dice de qué se va a hablar."),
    ],
    [
        E("Eva quiere hablar de «el mundo» en un minuto. Tito de «mi plaza favorita». ¿Quién acotó mejor su tema?", "Tito", "Su tema es más pequeño."),
        E("Rosa quiere contar su vida entera en un minuto. ¿Es posible hacerlo bien?", "No", "Es un tema demasiado grande."),
    ],
    [
        E("De estos temas, ¿cuál es el más acotado? a) «Los deportes» b) «Las reglas del luche» c) «Todos los juegos del mundo»", "b", "Es el más pequeño."),
        E("Para exponer en un minuto sobre tu juguete favorito, ¿incluyes todo lo que haces con él o eliges tres cosas?", "Elijo tres cosas", "Hay que elegir para no pasarse de tiempo."),
    ],
    [E("Tienes un minuto para hablar de «las vacaciones». Escribe un tema acotado y una cosa que dejarás fuera.", "Por ejemplo: El día que fui a la playa; dejaré fuera el viaje en bus", "Tiene tema pequeño y una decisión.")],
    [
        E("¿Un tema acotado es más fácil de contar?", "Sí", "Es más preciso."),
        E("¿Debo contar todo lo que sé?", "No", "Elijo lo importante."),
        E("¿Escojo un tema que conozco?", "Sí", "Así hablo con seguridad."),
    ],
    ("Elige y acota tu tema. Elige una de estas ideas: mi mascota, mi juego favorito, un día especial o mi comida favorita. Escribe: 1) tu tema acotado, 2) tres datos que contarás, 3) un dato que dejarás fuera, 4) la frase que resume tu tema.",
     "Tema: mi juego favorito, el luche. Datos: se dibuja en el suelo, se salta de cuadro en cuadro, se tira una piedra. Dejo fuera: las veces que me caí. Frase: Hoy les hablaré de cómo se juega al luche.",
     ["el tema es pequeño y claro", "escribe tres datos y uno que deja fuera", "tiene una frase que resume el tema"], ["hoja con los cuatro elementos"], ["tema demasiado grande", "no dejar nada fuera"],
     "Si el tema es grande, pregunta qué parte contaría en un minuto."),
    "Dile a alguien de tu casa de qué tema te gustaría hablar y por qué.",
    "Acota el mismo tema dos veces para dos audiencias distintas.",
)

reg(
    OA27, 2,
    "Este cuaderno, lápiz y una hoja.",
    "Aprenderé a ordenar mi exposición en apertura, dos ideas y cierre. Sirve para que mi audiencia me entienda de principio a fin.",
    ["Sé acotar un tema.", "Sé ordenar con primero, luego y al final."],
    [
        "Una exposición ordenada tiene cuatro partes. La apertura es lo primero que digo: saludo, presento el tema y digo qué voy a contar. Luego van dos ideas principales, cada una con un dato. Al final, el cierre resume o termina con una frase.",
        "Por ejemplo, tema: mi gato Pelusa. Apertura: «Hola, hoy les hablaré de mi gato Pelusa». Idea 1: «Pelusa es gris y tiene ojos verdes». Idea 2: «Le gusta dormir en el sillón». Cierre: «Así es Pelusa. Gracias por escucharme».",
        "Para recordar el orden no hace falta memorizar todo palabra por palabra. Escribo una tarjeta con pocas palabras: saludo, idea 1, idea 2 y cierre. Con la tarjeta, hablo con mis propias palabras y no me pierdo. Si narro un evento, ordeno con primero, luego y al final. Hablar más fuerte no reemplaza tener un orden.",
    ],
    [("apertura", "inicio de la exposición"), ("idea principal", "dato importante que quiero contar"), ("cierre", "final de la exposición"), ("tarjeta", "papel con ideas clave"), ("orden", "forma en que se presenta lo que digo")],
    [
        ("Armar la secuencia", "Tema: mi gato Pelusa. ¿Cómo ordenas apertura, dos ideas y cierre?", ["Pienso un saludo.", "Elijo dos datos.", "Escribo un cierre."], "Apertura: hoy les hablaré de mi gato Pelusa. Idea 1: es gris. Idea 2: duerme en el sillón. Cierre: gracias por escucharme."),
        ("Hacer una tarjeta", "Tienes que recordar tu exposición sobre el luche. ¿Qué escribes en la tarjeta?", ["Uso pocas palabras.", "Pongo cada parte.", "No copio todo."], "Hola / se dibuja y se salta / se tira una piedra / gracias."),
    ],
    [("Memorizar palabra por palabra.", "Se cree que así sale perfecto.", "Usa una tarjeta con ideas clave."), ("Hablar más fuerte para tapar el desorden.", "Se confunde volumen con claridad.", "Primero ordena y luego ajusta la voz.")],
    [
        E("¿La apertura va al principio o al final?", "Al principio", "Empieza la exposición."),
        E("¿Cuántas ideas principales tiene el modelo de esta clase?", "Dos", "Apertura, dos ideas y cierre."),
        E("¿«Gracias por escucharme» es parte de la apertura o del cierre?", "Del cierre", "Termina la exposición."),
    ],
    [
        E("¿Qué hace la apertura?", "Saluda y presenta el tema", "Prepara a la audiencia."),
        E("¿Para qué sirve una tarjeta con ideas clave?", "Para recordar el orden sin memorizar todo", "Ayuda a hablar con mis palabras."),
        E("¿Hablar más fuerte arregla el desorden?", "No", "El orden se logra planificando."),
    ],
    [
        E("Tema: mi bicicleta. Escribe una apertura.", "Por ejemplo: Hola, hoy les hablaré de mi bicicleta", "Saluda y dice el tema."),
        E("Tema: mi bicicleta. Escribe dos ideas principales.", "Por ejemplo: Es roja; la uso los sábados", "Son dos datos distintos."),
        E("Tema: mi bicicleta. Escribe un cierre.", "Por ejemplo: Esa es mi bicicleta. Gracias por escuchar", "Termina la exposición."),
    ],
    [
        E("Una niña dice: «Pelusa duerme en el sillón. Hola. Es gris. Gracias». ¿Está ordenada su exposición?", "No", "El saludo debe ir primero y el cierre al final."),
        E("Pablo anota solo 4 palabras en su tarjeta: hola, rápido, grande, gracias. ¿Le sirve para recordar sus ideas?", "No", "Las ideas no quedaron claras."),
    ],
    [
        E("Partes: a) Gracias por escuchar, b) Es alta y ancha, c) Hola, hoy hablaré de la torre. ¿Cuál va primero y cuál al final?", "c primero, a al final", "La apertura va primero y el cierre al final."),
        E("Elige la mejor tarjeta: a) «Todo el texto copiado palabra por palabra» b) «Hola / luche: se salta / piedra / gracias»", "b", "Tiene ideas clave, no todo el texto."),
    ],
    [E("Tema: mi comida favorita, los porotos. Escribe una exposición con una apertura, dos ideas y un cierre.", "Hola, hablaré de los porotos. Son calientitos. Se comen con arroz. Gracias por escucharme", "Tiene cuatro partes ordenadas.")],
    [
        E("¿La exposición tiene principio y final?", "Sí", "Apertura y cierre."),
        E("¿Una tarjeta puede tener solo palabras clave?", "Sí", "Así no memorizo todo."),
        E("¿Debo hablar rápido y fuerte para que me entiendan?", "No", "Debo hablar claro y con orden."),
    ],
    ("Ordena tu exposición. Con el tema que acotaste (o con «mi juego favorito: el luche»), escribe una tarjeta con apertura, idea 1, idea 2 y cierre. Cada parte debe tener entre 3 y 6 palabras. Luego ensaya con un adulto sin leer palabra por palabra: míralo y usa la tarjeta solo para recordar.",
     "Hola, hablaré del luche / se dibuja en el piso / se salta por cuadros / gracias por escucharme.",
     ["tiene apertura, dos ideas y cierre", "las partes son breves", "habla con sus palabras"], ["tarjeta escrita", "ensayo con un adulto"], ["memorizar", "olvidar el cierre"],
     "Si memoriza todo, pídele que cuente solo con la tarjeta."),
    "Cuenta tu tema en tres frases: inicio, idea y final.",
    "Cambia el orden de las ideas y explica cuál versión se entiende mejor.",
)

reg(
    OA27, 3,
    "Este cuaderno, lápiz y una hoja.",
    "Aprenderé a agregar frases descriptivas para que mi audiencia pueda imaginar lo que cuento. Sirve para hacer más claras y entretenidas mis exposiciones.",
    ["Sé armar apertura, ideas y cierre.", "Sé que hay palabras que dicen cómo es algo."],
    [
        "Una frase descriptiva dice cómo es algo. Usa palabras que muestran color, tamaño, forma, sonido o textura. En vez de decir «tengo un gato», puedo decir «tengo un gato gris, de pelo suave y ojos verdes». La audiencia imagina mejor.",
        "Para describir, miro el objeto con mis sentidos. Pregunto: ¿cómo se ve?, ¿cómo suena?, ¿cómo se siente al tocarlo? Después elijo dos o tres palabras que sirven. No hace falta decir diez adjetivos. Más no es mejor: debe ayudar a entender el tema.",
        "Una frase descriptiva se agrega dentro de una idea. Por ejemplo: «Mi bicicleta es roja, con un timbre que suena ring». La descripción debe ser pertinente: si hablo de la bicicleta, no describo la casa del vecino.",
    ],
    [("descripción", "palabras que dicen cómo es algo"), ("frase descriptiva", "frase que muestra cómo es algo"), ("sentidos", "vista, oído, tacto, olfato y gusto"), ("pertinente", "que sirve para el tema"), ("detalle", "dato pequeño que ayuda")],
    [
        ("Mejorar una frase", "«Tengo un perro». ¿Cómo la haces más descriptiva?", ["Pienso cómo es.", "Elijo dos rasgos.", "Los agrego."], "Tengo un perro café, de orejas largas y cola peluda."),
        ("Elegir un detalle pertinente", "Hablas de tu bicicleta. ¿Qué detalle sirve: «es roja» o «mi vecino tiene un loro»?", ["Veo el tema: la bicicleta.", "Reviso cada detalle.", "Elijo el que habla de ella."], "Es roja."),
    ],
    [("Agregar muchas palabras que no sirven.", "Se cree que más es mejor.", "Elige dos o tres detalles que ayuden."), ("Describir algo que no es parte del tema.", "Se pierde el foco.", "Describe solo lo del tema.")],
    [
        E("«Un gato gris de ojos verdes» ¿tiene descripción o no?", "Sí", "Dice color y rasgo."),
        E("«Tengo un gato» ¿es más o menos descriptiva que «Tengo un gato gris y suave»?", "Menos descriptiva", "No dice cómo es."),
        E("Si hablo de mi bicicleta, ¿describo la bicicleta o la casa del vecino?", "La bicicleta", "Debe ser pertinente."),
    ],
    [
        E("¿Qué hace una frase descriptiva?", "Dice cómo es algo", "Ayuda a imaginar."),
        E("¿Por qué no debo agregar diez adjetivos?", "Porque no ayudan si sobran", "Debo elegir lo pertinente."),
        E("¿Qué sentidos puedo usar para describir?", "Vista, oído, tacto, olfato y gusto", "Cada uno entrega rasgos."),
    ],
    [
        E("Describe una naranja usando dos rasgos.", "Por ejemplo: Es redonda y anaranjada", "Dice forma y color."),
        E("Describe la lluvia con un sonido.", "Por ejemplo: Suena como pasitos sobre el techo", "Usa el oído."),
        E("Mejora esta frase: «Tengo una mochila».", "Por ejemplo: Tengo una mochila azul con cierre grande", "Agrega color y un rasgo."),
    ],
    [
        E("Rita describe su torta: «Era grande, de chocolate y con cinco velitas». Beto: «Era linda». ¿Quién dio más información?", "Rita", "Sus descripciones son concretas."),
        E("Mateo habla de su perro y dice: «Mi tía vive lejos». ¿Su descripción es pertinente?", "No", "No habla del perro."),
    ],
    [
        E("Elige la mejor descripción para hablar de un oso de peluche: a) «Es muy bonito.» b) «Es café, suave y con un lazo rojo.»", "b", "La b da rasgos concretos."),
        E("Una exposición dice: «Mi gato es gris. Mi gato es gris. Mi gato es gris». ¿Describe bien?", "No", "Repite el mismo rasgo."),
    ],
    [E("Hablarás de tu comida favorita, el pan. Escribe una frase con tres rasgos usando la vista, el olfato y el tacto.", "Por ejemplo: El pan dorado huele rico y es calentito", "Usa tres rasgos.")],
    [
        E("¿Un detalle sirve si ayuda a entender el tema?", "Sí", "Debe ser pertinente."),
        E("¿Debo describir con palabras variadas?", "Sí", "Así es más claro."),
        E("¿Describir es solo decir el nombre de algo?", "No", "Es decir cómo es."),
    ],
    ("Describe para hacer visible. Elige un objeto de tu casa (un juguete, una fruta o una taza). Míralo bien y escribe o di tres frases descriptivas: una de su color o forma, una de cómo se siente al tocar y otra de lo que hace o suena. Cuéntaselas a un adulto sin decir el nombre y pídele que adivine.",
     "Es redondo y rojo. Tiene la piel lisa y fría. Hace crac cuando lo muerdo. Es una manzana.",
     ["usa al menos tres rasgos", "usa sentidos distintos", "los rasgos son pertinentes"], ["frases dichas o escritas", "el adulto adivina"], ["rasgos repetidos", "palabras que no describen"],
     "Si el adulto no adivina, ayuda a agregar un rasgo más específico."),
    "Describe a alguien de tu casa un objeto del refrigerador sin decir su nombre.",
    "Describe un lugar con tres sentidos distintos.",
)

reg(
    OA27, 4,
    "Este cuaderno, lápiz y espacio libre. Un adulto como público.",
    "Aprenderé a ajustar volumen, pronunciación y postura para que mi audiencia me escuche y entienda. Sirve para ensayar mi exposición.",
    ["Sé ordenar una exposición.", "Sé hablar sin gritar."],
    [
        "Cuando exponemos, no solo importa qué decimos, sino cómo lo decimos. El volumen es qué tan fuerte hablo: debe llegar al fondo de la sala sin gritar. La pronunciación es decir bien las palabras, sin comerse sílabas. Y la postura es cómo me paro: derechito, con los pies firmes.",
        "Para ensayar, practico frente a un adulto o un espejo. Pregunto: ¿me oyen bien?, ¿se entienden mis palabras?, ¿estoy mirando a las personas? Si hablo bajito, subo un poco el volumen. Si me trabo con una palabra larga, la repito despacio.",
        "También respiro antes de empezar y hablo con calma. Mirar a la audiencia y usar gestos suaves ayuda a que me entiendan. No hace falta moverse mucho ni jugar con la ropa. Ensayar varias veces me da seguridad. Cada persona habla a su ritmo: si necesito pausas o tiempo para una palabra, lo hago sin apuro. Si no puedo pararme o mirar a los ojos, elijo una postura cómoda y estable y dirijo mi cara hacia el público.",
    ],
    [("volumen", "qué tan fuerte hablo"), ("pronunciación", "forma en que digo las palabras"), ("postura", "forma en que me paro o me siento"), ("ensayar", "practicar antes de presentar"), ("respirar", "tomar aire con calma")],
    [
        ("Ajustar el volumen", "Tu profesora, sentada al fondo, no te oye. ¿Qué haces?", ["Respiro.", "Subo un poco el volumen.", "No grito."], "Hablo un poco más fuerte, sin gritar."),
        ("Pronunciar bien", "Te trabas con la palabra «bicicleta». ¿Qué haces?", ["La repito despacio.", "Digo cada sílaba.", "Luego la digo normal."], "Digo bi-ci-cle-ta despacio y luego rápido."),
    ],
    [("Gritar para que me oigan.", "Se cree que más fuerte es mejor.", "Habla firme pero sin gritar."), ("Mirar al suelo o al papel todo el tiempo.", "Se tiene nervios.", "Levanta la vista hacia la audiencia.")],
    [
        E("Para que me oigan al fondo, ¿hablo más fuerte sin gritar o susurro?", "Más fuerte sin gritar", "Se debe oír claro."),
        E("¿Cuál es una buena postura: derechito o encorvado?", "Derechito", "Se ve seguro."),
        E("Si me trabo en una palabra larga, ¿la repito despacio o me rindo?", "La repito despacio", "Practicar despacio ayuda."),
    ],
    [
        E("En Lenguaje: ¿Qué es la pronunciación?", "La forma en que digo las palabras", "Debe ser clara."),
        E("¿Por qué ensayar antes de exponer?", "Para sentir más seguridad", "Practicar reduce nervios."),
        E("¿Qué puedo hacer antes de empezar para calmarme?", "Respirar con calma", "Ayuda a hablar tranquilo."),
    ],
    [
        E("Di tres veces «calcetín» despacio y luego escribe cuántas sílabas tiene.", "3", "cal-ce-tín tiene tres sílabas."),
        E("Escribe dos cosas que debes mirar al ensayar: una de tu voz y una de tu cuerpo.", "Voz: volumen; cuerpo: postura", "Son dos aspectos a ensayar."),
        E("Tu amigo habla muy bajito y mira al suelo. Escribe un consejo.", "Por ejemplo: Sube un poco la voz y mira al público", "Mejora volumen y mirada."),
    ],
    [
        E("Luz expone gritando y moviéndose mucho. Nico habla firme, derecho y mirando. ¿Quién ajustó mejor voz y cuerpo?", "Nico", "Controló su volumen y postura."),
        E("Tito dice «bicieta» en vez de «bicicleta». ¿Qué debe practicar?", "La pronunciación", "Debe decir todas las sílabas."),
    ],
    [
        E("Elige la mejor opción para empezar a exponer: a) correr hacia el frente sin mirar, b) respirar, pararse derecho y saludar.", "b", "Así empiezo con calma."),
        E("Una niña expone con voz muy suave, pero la sala está en silencio y todos la oyen. ¿Debe subir el volumen?", "No", "El volumen ya es suficiente."),
    ],
    [E("Vas a exponer en una sala grande. Escribe tres cosas que ensayarás: una de volumen, una de pronunciación y una de postura.", "Hablar firme sin gritar; decir todas las sílabas; pararme derecho", "Cubre las tres cosas.")],
    [
        E("¿Ensayar sirve para exponer mejor?", "Sí", "Practicar da seguridad."),
        E("¿Debo mirar al público?", "Sí", "Así conecto con ellos."),
        E("¿Es necesario gritar para ser oído?", "No", "Basta con hablar firme."),
    ],
    ("Ensaya voz y cuerpo con un adulto. Di esta frase de apertura tres veces: «Hola, hoy les hablaré de mi juego favorito, que se llama el luche». 1) La primera vez, bajito. 2) La segunda, fuerte pero sin gritar. 3) La tercera, claro y mirando a tu público. Pide al adulto que diga cuál se entendió mejor y por qué. Fíjate en tu postura.",
     "La primera vez no me oyeron. La segunda estuvo bien pero un poco rápido. La tercera fue la mejor: hablé firme, derechito y miré a mi mamá.",
     ["prueba tres volúmenes", "mantiene una buena postura", "dice qué versión fue mejor y por qué"], ["ensayo ante un adulto", "comentario del adulto"], ["gritar", "mirar siempre el piso"],
     "Si grita, pídele que baje un poco y mantenga la claridad."),
    "Dile a un adulto tu frase de apertura mirándolo a los ojos.",
    "Ensaya tu exposición completa frente a un espejo y ajusta una cosa.",
)

reg(
    OA27, 5,
    "Este cuaderno, lápiz, una hoja y la tarjeta que preparaste. Un adulto como audiencia.",
    "Aprenderé a presentar mi exposición con apoyo y a contestar una pregunta. Sirve para compartir lo que sé y mostrar que entendí mi tema.",
    ["Sé armar y ensayar mi exposición.", "Sé hacer preguntas."],
    [
        "El día de presentar, uso lo que preparé: una apertura, dos ideas con una frase descriptiva y un cierre. Respiro, me paro derecho y hablo claro. Mi tarjeta me ayuda a recordar el orden, pero no leo palabra por palabra.",
        "Después de presentar, la audiencia puede hacer preguntas. Escucho la pregunta completa y pienso un momento. Respondo con lo que sé: «Pelusa come pescado y croquetas». Si no sé la respuesta, digo con calma «no lo sé, pero lo puedo averiguar». Eso también es honesto.",
        "Al terminar, agradezco: «Gracias por escucharme». Luego puedo pensar qué salió bien y qué mejoraría la próxima vez. Aprender a exponer lleva tiempo. Cada presentación es una nueva oportunidad para hablar con más claridad y seguridad.",
    ],
    [("presentar", "exponer ante una audiencia"), ("pregunta", "frase con la que alguien quiere saber algo"), ("responder", "decir lo que sé a una pregunta"), ("honesto", "que dice la verdad"), ("mejorar", "hacer algo mejor la próxima vez")],
    [
        ("Responder una pregunta", "Expusiste sobre Pelusa. Te preguntan: «¿Qué come?». Tú sabes que come pescado y croquetas. ¿Qué respondes?", ["Escucho la pregunta completa.", "Pienso mi respuesta.", "La digo con claridad."], "Pelusa come pescado y croquetas."),
        ("Responder con honestidad", "Te preguntan: «¿Cuántos años tiene Pelusa?». No lo sabes. ¿Qué dices?", ["No invento.", "Digo que no lo sé.", "Ofrezco averiguarlo."], "No lo sé, pero lo puedo averiguar."),
    ],
    [("Inventar una respuesta si no la sé.", "Se tiene vergüenza.", "Di «no lo sé» y ofrece averiguar."), ("Dejar la presentación sin cierre.", "Se pone nervioso.", "Termina con gracias.")],
    [
        E("Si me hacen una pregunta, ¿la escucho completa o respondo antes de que termine?", "La escucho completa", "Así respondo bien."),
        E("Si no sé la respuesta, ¿invento o digo «no lo sé»?", "Digo no lo sé", "Eso es ser honesto."),
        E("Al terminar, ¿digo gracias o me voy sin decir nada?", "Digo gracias", "Cierro con cortesía."),
    ],
    [
        E("¿Para qué sirve la tarjeta el día de presentar?", "Para recordar el orden", "No es para leer todo."),
        E("¿Por qué es honesto decir «no lo sé»?", "Porque no invento información", "Digo la verdad."),
        E("¿Qué hago después de presentar para mejorar?", "Pienso qué salió bien y qué cambiaría", "Reflexionar ayuda a aprender."),
    ],
    [
        E("Expusiste sobre el luche y dijiste que se tira una piedra. Te preguntan: «¿Qué se tira?». Escribe tu respuesta.", "Se tira una piedra", "Responde con lo que sé."),
        E("Te preguntan algo que no sabes sobre tu tema. Escribe una respuesta honesta.", "No lo sé, pero lo puedo averiguar", "Es una respuesta sincera."),
        E("Escribe una frase de cierre para tu exposición.", "Por ejemplo: Eso es todo. Gracias por escucharme", "Cierra y agradece."),
    ],
    [
        E("Pablo respondió «Porque sí» a una pregunta, sin dar datos. Ema respondió «Pelusa come pescado porque le gusta el sabor». ¿Quién respondió mejor?", "Ema", "Dio una respuesta con razón."),
        E("Lía inventó una respuesta incorrecta para no decir «no sé». ¿Fue honesta?", "No", "Dio información falsa."),
    ],
    [
        E("Ordena: a) Responder la pregunta, b) Presentar, c) Escuchar la pregunta completa, d) Agradecer.", "b, c, a, d", "Orden lógico de la presentación."),
        E("Después de exponer, Tati piensa: «Hablé bajito, pero dije mis ideas en orden». ¿Qué debe mejorar y qué mantener?", "Mejorar el volumen; mantener el orden", "Identifica lo que falló y lo que salió bien."),
    ],
    [E("Expones sobre tu mascota, un conejo llamado Copo, que es blanco y come zanahorias. Un compañero pregunta: «¿De qué color es y qué come?». Escribe tu respuesta completa.", "Copo es blanco y come zanahorias", "Responde con los datos dados.")],
    [
        E("¿Puedo decir «no lo sé» si no sé?", "Sí", "Es una respuesta honesta."),
        E("¿Agradecer al terminar es parte de la presentación?", "Sí", "Es el cierre cortés."),
        E("¿Tengo que leer todo palabra por palabra?", "No", "La tarjeta solo ayuda."),
    ],
    ("Presenta tu exposición a un adulto o a tu familia. Usa tu tarjeta con apertura, dos ideas (una con frase descriptiva) y cierre, en un minuto. Respira antes, mira a tu audiencia y habla claro. Pide que te hagan una pregunta y respóndela con calma. Al final di una cosa que salió bien y una que mejorarías.",
     "Hola, hablaré de mi conejo Copo. Es blanco y suave. Come zanahorias. Gracias por escucharme. Pregunta: ¿cuántos años tiene? Respondí: tiene dos. Salió bien mi orden. Mejoraría mi volumen.",
     ["presenta con orden", "responde una pregunta con calma", "dice qué salió bien y qué mejoraría"], ["presentación ante un adulto", "comentario final"], ["leer todo", "inventar una respuesta"],
     "Si se pone nervioso, pide que respire y use solo su tarjeta."),
    "Haz un resumen oral de tu exposición en dos frases.",
    "Haz tu exposición a dos audiencias distintas y compara qué cambias.",
)
