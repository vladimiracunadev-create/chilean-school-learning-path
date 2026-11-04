"""Cuaderno del estudiante, 1.º medio Orientación: OA 03 (riesgos, protección y búsqueda de ayuda) y OA 04 (acciones autónomas para una vida saludable)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA3, OA4 = "OR1M OA 03", "OR1M OA 04"


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
    "Una hoja y un lápiz. El caso de la fiesta de Antonella, una joven inventada, está escrito en los ejercicios. No cuentes nada tuyo.",
    "Aprenderé a examinar un caso y a evaluar riesgos relacionados con sustancias, conductas sexuales riesgosas y violencia. Sirve para reconocer cuándo una situación es peligrosa y qué la hace más o menos riesgosa.",
    ["Sé que las presiones se pueden responder con un «no» claro (8.º básico).", "Sé que debo avisar a una persona adulta de confianza ante un peligro."],
    [
        "Un riesgo es la posibilidad de que ocurra un daño. Evaluarlo es preguntarse dos cosas: qué tan probable es que pase y qué tan grave sería. Algunas situaciones aumentan el riesgo y se llaman factores de riesgo: presión de grupo, consumo de alcohol o de otras sustancias, estar sin adultos que se enteren, irse con alguien que no conoces o relaciones donde hay control y gritos. Otras lo disminuyen y se llaman factores de protección: tener personas de confianza, avisar dónde estás, tener información, saber decir que no.",
        "Las sustancias que se consumen, como el alcohol, el tabaco, los vapeadores y las drogas ilegales, pueden alterar el juicio, la coordinación y la salud. Las conductas sexuales riesgosas son aquellas que se hacen sin consentimiento, bajo presión, con alcohol u otras sustancias, sin protección o con alguien mucho mayor que se aprovecha de la diferencia de edad; pueden causar daño emocional, infecciones de transmisión sexual o embarazo no planificado. La violencia es todo daño intencional, físico, psicológico, sexual o digital.",
        "Examinar un caso es leerlo en tercera persona y separar hechos, emociones, factores de riesgo y factores de protección. No se juzga ni se diagnostica a nadie. Después se piensa qué opciones tiene el personaje y a quién podría pedir ayuda. Así aprendes a evaluar sin exponer tu vida personal.",
    ],
    [("riesgo", "posibilidad de que ocurra un daño"), ("factor de riesgo", "situación que aumenta la posibilidad de un daño"), ("factor de protección", "situación que disminuye la posibilidad de un daño"), ("violencia", "daño intencional físico, psicológico, sexual o digital"), ("sustancia", "alcohol, tabaco, vapeadores u otras drogas que alteran el cuerpo")],
    [
        W("Separar factores", "Caso: Antonella va a una fiesta sin avisar en su casa y un amigo le ofrece alcohol. Su prima la acompaña y sabe a qué hora volver. Clasifica.", ["Ir sin avisar y recibir una oferta de alcohol suben el riesgo.", "La prima y la hora de vuelta protegen."], "Riesgo: no avisar y la oferta; protección: la prima y la hora de vuelta"),
        W("Probabilidad y gravedad", "Un joven cruza corriendo una avenida sin mirar. ¿Qué tan probable y qué tan grave puede ser el daño?", ["Puede ser atropellado: es posible.", "El daño podría ser grave."], "Probable y grave: riesgo alto"),
    ],
    [
        M("Pensar que el riesgo es lo mismo que la mala suerte.", "Se cree que no se puede prever.", "Se evalúa con factores de riesgo y de protección."),
        M("Juzgar a la persona del caso en vez de analizar la situación.", "Se mira a la persona y no los factores.", "Describe hechos y factores sin etiquetar a nadie."),
    ],
    R=[
        ex("Tener personas de confianza a quienes avisar, ¿es un factor de riesgo o de protección?", "De protección", "Disminuye la posibilidad de un daño."),
        ex("La presión de grupo para consumir, ¿es un factor de riesgo o de protección?", "De riesgo", "Aumenta la posibilidad de un daño."),
        ex("Compara dos situaciones: 1) cruzar por el paso de cebra con luz verde; 2) cruzar corriendo entre autos con luz roja. ¿Qué situación tiene más probabilidad de daño grave? A) La 1 B) La 2", "B", "Cruzar con luz roja entre autos es más probable y más grave."),
    ],
    U=[
        ex("En un caso, un joven sube a un auto cuyo conductor consumió alcohol. ¿Qué tipo de factor es? A) De riesgo B) De protección.", "A", "El alcohol altera la coordinación del conductor."),
        ex("¿Cuál de estas es una conducta sexual riesgosa? A) Tenerla bajo presión o con alcohol B) Conversar con respeto y con consentimiento.", "A", "La presión y el alcohol quitan la libertad de decidir."),
        ex("Un golpe, un insulto repetido y la difusión de una foto sin permiso. ¿Qué tienen en común? A) Son daños intencionales, físicos, psicológicos o digitales B) Son bromas sin consecuencias", "A", "Son formas de violencia: daño intencional."),
    ],
    A=[
        ex("Antonella avisó dónde estaba, llevó su celular cargado y tomó agua en lugar de alcohol. Cuenta cuántos son factores de protección.", "3", "Avisar, llevar el celular y no consumir protegen."),
        ex("Clasifica con R (riesgo) o P (protección): 1) ir sola de noche por una calle desconocida; 2) quedarse con amigas de confianza; 3) aceptar una bebida abierta de un desconocido. Escribe las letras en orden.", "R, P, R", "La 1 y la 3 aumentan el riesgo; la 2 protege."),
        ex("Dos situaciones: X) conducir una bicicleta con casco por la ciclovía; Y) conducir sin casco entre autos. ¿Cuál tiene mayor probabilidad de daño grave? A) X B) Y", "B", "Sin casco y entre autos, el daño sería más grave."),
    ],
    Z=[
        ex("¿Por qué el alcohol aumenta el riesgo de conductas sexuales sin consentimiento?", "Porque altera el juicio y la capacidad de decidir con libertad", "Bajo sus efectos, es difícil decir que no o entender lo que ocurre."),
        ex("¿Qué es mejor para evaluar un caso? A) Separar hechos y factores sin juzgar a nadie B) Culpar al personaje de lo que le pasó.", "A", "Analizar permite proponer acciones; culpar no ayuda."),
    ],
    D=[
        arith("En una fiesta inventada hay 7 factores de riesgo y 4 de protección. ¿Cuántos factores de riesgo hay de más?", "7-4", "Se resta el número de factores de protección."),
        arith("Una lista del curso anota 3 factores de riesgo por cada uno de 8 casos. ¿Cuántos factores de riesgo hay en total?", "3*8", "Se multiplican factores por casos."),
    ],
    context=[ex("Tu curso analiza un caso: Paula se queda sola en una plaza de noche con un grupo que consume vapeadores y se burla de ella. ¿Qué sería un factor de protección? A) Llamar a una persona de confianza para que la vaya a buscar B) Quedarse un poco más para no quedar mal.", "A", "Avisar a una persona de confianza reduce el riesgo.")],
    selfcheck=[ex("En Orientación: ¿un factor de protección disminuye el riesgo?", "Sí", "Ayuda a evitar el daño."), ex("¿La violencia puede ser psicológica?", "Sí", "Los insultos y amenazas dañan emocionalmente."), ex("¿Analizar un caso es juzgar al personaje?", "No", "Se analizan hechos y factores.")],
    task=T("Lee este caso inventado: Esteban, de 15 años, va a una casa donde no hay adultos. Le ofrecen alcohol y vapeadores, y un compañero le dice que si no prueba «no es parte del grupo». Esteban avisó a su tía dónde estaba y tiene su celular cargado. Escribe una tabla con cuatro factores de riesgo y dos factores de protección, y una frase que explique el riesgo mayor.", "Riesgo: no hay adultos, oferta de alcohol, oferta de vapeador, presión de grupo. Protección: avisó a su tía, tiene el celular cargado. Mayor riesgo: la presión de grupo con consumo y sin adultos.", ["identifica factores de riesgo del caso", "identifica factores de protección", "explica el riesgo mayor", "no juzga a Esteban"], ["tabla escrita", "texto oral"], ["culpar al personaje", "inventar factores que el caso no nombra"], "Reconoce los factores bien separados y pregunta cuál protegería más."),
    reinforce="Anota dos factores de riesgo y dos de protección de ir en bicicleta por una calle.",
    extend="Explica por qué evaluar un riesgo no es lo mismo que tener miedo.",
)

lesson(
    OA3, 2,
    "Una hoja y un lápiz. Las afirmaciones sobre sustancias y violencia están escritas en los ejercicios; son datos generales, sin experiencias personales.",
    "Aprenderé a distinguir hechos, derechos y límites sobre sustancias, conductas sexuales riesgosas y violencia. Sirve para separar mitos de datos y saber qué derechos me protegen.",
    ["Sé evaluar factores de riesgo y de protección.", "Sé que una opinión no es un hecho."],
    [
        "Un hecho se puede comprobar con una fuente confiable; un mito, no. Es un hecho que el alcohol altera la coordinación y el juicio, que el tabaco y la nicotina crean dependencia y que en Chile está prohibido vender alcohol y cigarrillos a menores de 18 años. Es un mito que «el vapeador no hace daño porque solo es vapor» o que «a esta edad no pasa nada». Un dato sin fuente ni fecha debe verificarse.",
        "Los derechos te protegen: derecho a la salud, a vivir libre de violencia, a la intimidad, a decir no y a ser protegido por los adultos y por las instituciones. Los límites son lo que no se debe hacer o permitir: ninguna persona puede obligarte a consumir, a tener contacto sexual o a soportar golpes, insultos o amenazas.",
        "Con una pareja o con amigos, hay conductas que son violencia aunque no haya golpes: controlar el celular, humillar, amenazar, aislar o difundir imágenes. Reconocerlas es el primer paso para pedir ayuda. Y cuando alguien decide consumir una sustancia, el riesgo es de esa persona y también de quienes la rodean, por ejemplo si conduce.",
    ],
    [("mito", "idea muy repetida que no se puede comprobar"), ("dependencia", "necesidad de seguir consumiendo una sustancia"), ("fuente confiable", "origen de información que puede comprobarse"), ("derecho a la salud", "derecho a cuidar y proteger el bienestar físico y emocional"), ("límite", "aquello que no se debe hacer ni permitir")],
    [
        W("Mito o hecho", "Un chat dice: «El vapeador solo tiene vapor de agua». ¿Es hecho o mito?", ["Muchos vapeadores contienen nicotina y otras sustancias.", "La frase no tiene fuente."], "Mito"),
        W("Reconocer violencia", "Caso: una pareja inventada se insulta y uno controla el celular del otro. ¿Es violencia?", ["Los insultos dañan emocionalmente.", "Controlar el celular invade la intimidad."], "Sí: violencia psicológica"),
    ],
    [
        M("Creer que si algo lo hacen muchos, no tiene riesgo.", "Se confunde frecuencia con seguridad.", "Revisa la fuente y los efectos en la salud."),
        M("Pensar que sin golpes no hay violencia.", "Se olvida la violencia psicológica y digital.", "Los insultos, amenazas, aislamiento y difusión de imágenes también son violencia."),
    ],
    R=[
        ex("Clasifica con H (hecho) o M (mito): 1) «En Chile está prohibido vender cigarrillos a menores de 18 años.» 2) «Si solo es vapor, no hace daño.» Escribe las letras en orden.", "H, M", "La 1 es una regla comprobable; la 2 no tiene respaldo."),
        ex("«A los 15 años el tabaco no hace nada». ¿Es un hecho o un mito?", "Un mito", "La nicotina crea dependencia a cualquier edad."),
        ex("Un compañero dice: «Nadie puede obligarme a probar algo ni a soportar golpes». ¿Qué expresa? A) Un derecho y un límite B) Un mito", "A", "Se refiere a su derecho a vivir sin violencia y a decir no."),
    ],
    U=[
        ex("¿Cuál de estas es un hecho? A) En Chile está prohibido vender alcohol a menores de 18 años B) Solo los adultos tienen riesgos.", "A", "La primera es una regla comprobable; la segunda es un mito."),
        ex("¿Qué es un límite en este contexto? A) Lo que no se debe permitir, como una agresión B) Un castigo que ponen los adultos.", "A", "Un límite protege a las personas."),
        ex("Un mensaje dice «Sé quién eres, o haces lo que digo o publico tu foto». ¿Qué tipo de violencia es? A) Digital y psicológica B) Una broma sin consecuencias.", "A", "Amenaza con difundir una imagen."),
    ],
    A=[
        ex("Clasifica con H (hecho) o M (mito): 1) La nicotina puede generar dependencia. 2) Si lo hacen todos, no hay riesgo. 3) Conducir bajo los efectos del alcohol aumenta los accidentes. Escribe las letras en orden.", "H, M, H", "La 1 y la 3 son hechos; la 2 es un mito."),
        ex("Un artículo afirma sin fuente ni fecha que «un solo vapeo no daña nada». ¿Qué haces primero? A) Buscarlo en una fuente confiable B) Compartirlo.", "A", "Un dato sin fuente debe verificarse."),
        ex("Carla cuenta que su pololo la insulta, le controla el celular y amenaza con publicar una foto suya. ¿Cuántas de esas tres conductas son violencia?", "3", "Las tres dañan su dignidad, su intimidad o su seguridad."),
    ],
    Z=[
        ex("¿Por qué «lo hacen todos» no es un dato confiable?", "Porque exagera y no se apoya en una fuente", "Se repite sin comprobar y presiona a ceder."),
        ex("Un joven dice: «Mi pareja me controla el celular porque me quiere». Con lo aprendido, ¿qué idea falta? A) Que controlar invade la intimidad y es violencia B) Que el control demuestra amor.", "A", "El cariño respeta la privacidad."),
    ],
    D=[
        arith("En una encuesta inventada a 120 estudiantes, 45 dicen que han oído mitos sobre vapeadores. ¿Cuántos no los han oído?", "120-45", "Al total se le restan los que sí los han oído."),
        arith("Un curso de 36 estudiantes forma equipos de 4 para revisar mitos, uno por equipo. ¿Cuántos mitos se revisan?", "36//4", "Se divide el total de estudiantes entre los integrantes de cada equipo."),
    ],
    context=[ex("En el recreo, un compañero dice: «Probar marihuana una vez no tiene riesgo». ¿Cuál es una respuesta basada en hechos? A) «Las sustancias pueden afectar la atención y la memoria; mejor revisarlo con una fuente de salud.» B) «Si lo dice él, será cierto.»", "A", "Se apoya en una fuente de salud y no en una opinión.")],
    selfcheck=[ex("En Orientación: ¿un mito se puede comprobar con una fuente?", "No", "No tiene respaldo."), ex("¿Tienes derecho a decir no a consumir una sustancia?", "Sí", "Es un derecho y un límite."), ex("¿Insultar y amenazar es violencia?", "Sí", "Daña emocionalmente a la persona.")],
    task=T("Lee las cuatro afirmaciones inventadas de un chat: (a) «El alcohol altera la forma de reaccionar»; (b) «Todos mis amigos lo han probado y no pasó nada»; (c) «Mi pololo me controla el celular porque me cuida»; (d) «Tengo derecho a decir no a una oferta». Marca cada una como hecho, mito o derecho y explica por qué con una frase.", "(a) Hecho: afecta el juicio y la coordinación. (b) Mito: es una generalización sin fuente. (c) Mito: controlar invade la intimidad y es violencia. (d) Derecho: puede decir no.", ["clasifica las cuatro afirmaciones", "justifica con un argumento", "distingue hecho de derecho", "no pide datos personales"], ["tabla escrita", "texto oral"], ["aceptar un dato sin fuente", "confundir control con cuidado"], "Reconoce las clasificaciones correctas y pregunta qué fuente usaría para comprobar una."),
    reinforce="Escribe un hecho y un mito sobre el alcohol para un cartel del curso.",
    extend="Explica por qué la violencia no siempre deja marcas visibles.",
)

lesson(
    OA3, 3,
    "Una hoja y un lápiz. Los dos casos de Matías y de Josefa, personas inventadas, están escritos en los ejercicios.",
    "Aprenderé a comparar opciones y consecuencias ante una oferta de sustancias, una presión sexual o una situación de violencia. Sirve para elegir la opción que cuida mi salud y mi seguridad.",
    ["Sé separar hechos y mitos.", "Sé usar el semáforo de riesgo."],
    [
        "Cuando enfrentas una situación riesgosa tienes varias opciones. Puedes aceptar, quedarte callado, enfrentar con agresión, decir que no con claridad, irte o pedir ayuda. Para compararlas, mira las consecuencias para tu salud, tu seguridad, tus relaciones y tu proyecto de vida. Con un semáforo: verde, si la opción te protege; amarillo, si tiene riesgos que podrías reducir; rojo, si te daña o daña a otros.",
        "Por ejemplo, ante una oferta de alcohol, aceptar puede alterar tu juicio y exponerte a accidentes o a presiones. Decir «no, gracias» y quedarte con personas de confianza protege tu salud. Ante la violencia en una pareja, quedarte callado mantiene el daño; avisar a un adulto abre la ayuda. Ante un conductor que consumió, la opción segura es no subir al auto y avisar a un adulto para que te busque.",
        "Las consecuencias pueden ser inmediatas, como una pelea o un accidente, o a largo plazo, como una dependencia o la pérdida de oportunidades. También hay consecuencias para otras personas: quien consume y conduce pone en riesgo a todos. Compararlas te ayuda a decidir con calma, aun bajo presión.",
    ],
    [("opción", "una de las respuestas posibles ante una situación"), ("consecuencia", "lo que ocurre después de una decisión"), ("semáforo", "forma de clasificar opciones en verde, amarillo y rojo"), ("accidente", "hecho inesperado que causa daño"), ("dependencia", "necesidad de seguir consumiendo una sustancia")],
    [
        W("Clasificar con semáforo", "Matías debe volver de una fiesta. Opción 1: subir al auto de un amigo que tomó alcohol. Opción 2: llamar a una persona adulta para que lo busque. ¿Cómo clasificas cada una?", ["Subir al auto con conductor que consumió arriesga a todos: rojo.", "Llamar a un adulto es seguro: verde."], "Opción 1: rojo; opción 2: verde"),
        W("Consecuencias a largo plazo", "Josefa se calla ante los insultos de su pareja durante meses. ¿Qué consecuencia puede tener?", ["El daño emocional puede aumentar.", "Los insultos pueden volverse más graves."], "El daño continúa y puede crecer"),
    ],
    [
        M("Creer que elegir la opción más rápida es elegir la más segura.", "La rapidez no mide el daño posible.", "Compara consecuencias con el semáforo."),
        M("Pensar que no decidir es no elegir.", "Quedarse callado también es una opción con consecuencias.", "No decidir también tiene efectos; compáralos."),
    ],
    R=[
        ex("Con el semáforo, clasifica: «decir no, gracias a una oferta de alcohol y quedarse con amigos de confianza». ¿Verde, amarillo o rojo?", "Verde", "Protege su salud y su decisión."),
        ex("Una compañera recibe insultos repetidos por chat. ¿Qué opción abre la ayuda? A) Mostrar el chat a la profesora jefe B) Borrar el chat y callarse", "A", "Un adulto puede actuar; borrar y callar mantiene el daño."),
        ex("Si alguien se calla ante la violencia, ¿qué suele pasar? A) El daño puede continuar B) El problema desaparece solo", "A", "No pide ayuda y el daño sigue."),
    ],
    U=[
        ex("¿Qué opción cuida más la salud de Matías ante una oferta de alcohol? A) Decir «no, gracias» y quedarse con personas de confianza B) Aceptar para no quedar mal.", "A", "Protege su juicio y su seguridad."),
        ex("¿Qué consecuencia de largo plazo puede tener consumir habitualmente tabaco o vapeadores con nicotina? A) Dependencia B) Mayor rendimiento deportivo.", "A", "La nicotina genera dependencia."),
        ex("Ante una pelea entre compañeros, ¿qué opción cuida más? A) Avisar a un adulto B) Meterse a pegar.", "A", "Evita más daño sin arriesgarse."),
    ],
    A=[
        ex("Josefa tiene cuatro opciones: 1) callarse; 2) insultar de vuelta; 3) avisar a la orientadora; 4) cortar el chat sin avisar a nadie. ¿Cuál abre la ayuda?", "La 3", "Es la única que involucra a una persona adulta."),
        ex("Un grupo invita a Matías a un lugar sin adultos donde habrá alcohol. ¿Qué opción es verde en el semáforo? A) Quedarse en casa y proponer otro plan B) Ir y ver qué pasa.", "A", "Evita la exposición al riesgo."),
        ex("Una persona adulta le pide a un joven un secreto sobre un contacto íntimo. Opciones: guardar el secreto o avisar a un adulto de confianza. ¿Cuál es verde?", "Avisar a un adulto de confianza", "El secreto mantiene el daño."),
    ],
    Z=[
        ex("¿Por qué aceptar una sustancia «solo esta vez» puede tener consecuencias aunque no pase nada de inmediato?", "Porque puede generar dependencia o riesgos que no se ven enseguida", "Los efectos pueden aparecer más tarde."),
        ex("Un joven dice: «Mejor no hago nada, así no me meto en problemas». ¿Qué le falta considerar? A) Que no hacer nada también tiene consecuencias B) Que siempre hay que enfrentar con gritos.", "A", "Quedarse callado puede mantener el daño."),
    ],
    D=[
        arith("En un caso inventado, Josefa escribe 3 consecuencias de ceder, 4 de enfrentar con gritos y 2 de pedir ayuda. ¿Cuántas consecuencias anotó en total?", "3+4+2", "Se suman las de cada opción."),
        arith("Un curso de 30 estudiantes vota la opción más segura de un caso: 21 eligen pedir ayuda. ¿Cuántos eligen otra opción?", "30-21", "Al total se le restan los que eligen pedir ayuda."),
    ],
    context=[ex("Camilo sale de una fiesta a las 23:00 y el conductor de su grupo dice «solo tomé uno». Camilo no está seguro. ¿Qué es lo más seguro? A) Llamar a una persona adulta para que lo busque B) Confiar para no complicar al grupo.", "A", "Si hay duda sobre alcohol, no se sube al auto.")],
    selfcheck=[ex("En Orientación: ¿quedarse callado ante la violencia es una opción con consecuencias?", "Sí", "Mantiene el daño."), ex("¿Subir a un auto con un conductor que consumió alcohol es rojo?", "Sí", "Es muy riesgoso."), ex("¿El semáforo sirve para comparar opciones?", "Sí", "Clasifica en verde, amarillo o rojo.")],
    task=T("Lee este caso inventado: Valeria está en una fiesta donde un compañero le ofrece una bebida con alcohol. Ella no quiere. Otro joven consume vapeadores y se burla de quienes no lo hacen. Escribe tres opciones para Valeria, clasifícalas con el semáforo y escribe una consecuencia de cada una.", "Aceptar: rojo, puede alterar su juicio. Decir «no, gracias» y quedarse con amigas de confianza: verde, protege su decisión. Irse y llamar a un adulto: verde, evita la presión.", ["escribe tres opciones", "usa el semáforo", "anota una consecuencia por opción", "no culpa a Valeria"], ["tabla escrita", "texto oral"], ["no anotar consecuencias", "culpar a la víctima"], "Reconoce las opciones bien clasificadas y pregunta cuál consecuencia es la más grave."),
    reinforce="Compara dos formas de volver a casa de noche con el semáforo.",
    extend="Explica por qué las consecuencias de una decisión pueden afectar también a otras personas.",
)

lesson(
    OA3, 4,
    "Una hoja y un lápiz. Los cuatro casos están escritos en los ejercicios; todo ocurre con personas inventadas.",
    "Aprenderé a elegir una acción segura ante consumo de sustancias, presión sexual y violencia, incluidas las emergencias. Sirve para saber qué hacer y qué no hacer.",
    ["Sé comparar opciones con el semáforo.", "Conozco la regla de avisar a un adulto de confianza."],
    [
        "Una acción segura protege primero a la persona en riesgo y a ti, sin ponerte en peligro. Tiene tres partes: alejarte del riesgo, avisar a una persona adulta o a un servicio de ayuda y, si puedes, quedarte con alguien de confianza. No se trata de resolver todo solo ni de enfrentar a quien daña.",
        "Si alguien parece intoxicado, está dormido y no responde, o se siente muy mal después de consumir, un adulto debe pedir ayuda a los servicios de emergencia de inmediato: no lo dejes solo, no le des remedios ni lo obligues a vomitar. Si presencias una pelea, no grabes para difundirlo ni te metas físicamente: avisa a un adulto del colegio. Si te piden una imagen íntima o te amenazan, no la envíes, guarda la captura del mensaje, bloquea y avisa a un adulto.",
        "También forma parte de cuidar a otros respetar su privacidad: no cuentes a todo el curso lo que un compañero te confió; llévalo con un adulto que pueda ayudar. Y recuerda que decir «no» es una acción segura en sí misma.",
    ],
    [("acción segura", "paso que protege a la persona en riesgo sin ponerte en peligro"), ("intoxicado", "afectado por el consumo de alcohol u otra sustancia"), ("servicios de emergencia", "ayuda urgente que se activa cuando hay peligro"), ("captura", "imagen de lo que se ve en la pantalla del celular"), ("privacidad", "ámbito personal que no se difunde")],
    [
        W("Persona que no responde", "Caso: tras una fiesta, un joven duerme y no responde cuando lo llaman. ¿Qué acción es segura?", ["No dejarlo solo.", "Pedir a un adulto que llame a emergencia.", "No darle remedios ni obligarlo a vomitar."], "Avisar de inmediato a un adulto para pedir emergencia y acompañarlo"),
        W("Pelea en el patio", "Dos compañeros se pelean. ¿Qué haces?", ["No grabar para difundir.", "No meterse físicamente.", "Avisar a un adulto del colegio."], "Avisar a un adulto del colegio"),
    ],
    [
        M("Grabar una pelea para subirla a redes.", "Se cree que sirve como prueba o como broma.", "Avisa a un adulto; difundir expone y daña a las personas."),
        M("Intentar resolver solo una intoxicación.", "Se cree que dormir lo soluciona.", "Un adulto debe pedir ayuda de emergencia sin dejarlo solo."),
    ],
    R=[
        ex("Si una persona no responde tras consumir alcohol, ¿se pide ayuda de emergencia o se deja dormir?", "Se pide ayuda de emergencia", "Podría estar en peligro grave."),
        ex("Dos compañeros se pelean en el patio. Marca la acción segura: A) Avisar a un adulto del colegio B) Grabar el video para mostrar quién empezó", "A", "Protege sin arriesgarse ni difundir."),
        ex("Un chat te exige una imagen íntima y te amenaza si no la envías. ¿Cuál es un primer paso seguro? A) No enviarla y guardar la captura del mensaje B) Enviarla para que se calme", "A", "Enviarla expone la intimidad; la captura sirve de evidencia."),
    ],
    U=[
        ex("Si alguien está intoxicado y no responde, ¿qué debes evitar? A) Darle remedios o forzar el vómito B) Acompañarlo y pedir ayuda a un adulto.", "A", "Pueden empeorar su estado."),
        ex("¿Por qué no se debe grabar una pelea para difundirla? A) Porque expone y daña a las personas B) Porque sirve de prueba para castigar al que pega.", "A", "Difundir violencia agrava el daño."),
        ex("¿Qué se hace con una captura de una amenaza por chat? A) Guardarla y mostrarla a un adulto B) Borrarla para que no se vea.", "A", "Sirve de evidencia."),
    ],
    A=[
        ex("Clasifica con S (segura) o N (no segura): 1) Quedarse con una persona que se siente mal y pedir ayuda a un adulto. 2) Dejarla durmiendo sola. 3) Grabar la pelea para subirla. Escribe las letras en orden.", "S, N, N", "Solo la 1 protege a la persona."),
        ex("Un adulto desconocido ofrece dinero a Tomás por una foto íntima. ¿Qué hace Tomás? A) No responde, guarda la captura, bloquea y avisa a un adulto B) Pide más dinero.", "A", "Protege su intimidad y detiene el riesgo."),
        ex("En un patio, un grupo golpea a un compañero. ¿Qué corresponde? A) Avisar de inmediato a un adulto del colegio B) Gritar para que se separen y meterse.", "A", "No te expone y consigue ayuda."),
    ],
    Z=[
        ex("¿Por qué no se debe dejar solo a alguien que consumió mucho alcohol y duerme?", "Porque su estado puede empeorar sin que nadie lo note", "Podría necesitar ayuda urgente."),
        ex("¿Por qué una acción segura no incluye enfrentar a quien daña? A) Porque puede ponerte en peligro; mejor avisar a un adulto B) Porque nadie hace daño.", "A", "La seguridad propia también cuenta."),
    ],
    D=[
        arith("En un taller inventado, 4 grupos de 5 estudiantes practican los pasos de una acción segura. ¿Cuántos estudiantes hay?", "4*5", "Se multiplican grupos por integrantes."),
        arith("De 28 estudiantes, 19 recuerdan los tres pasos de una acción segura. ¿Cuántos no los recuerdan?", "28-19", "Al total se le restan quienes sí los recuerdan."),
    ],
    context=[ex("En una excursión inventada, una compañera dice que se siente mareada después de recibir un vaso en una reunión. ¿Qué es lo más seguro? A) Acompañarla y avisar a un adulto B) Decirle que descanse sola.", "A", "No se deja sola a una persona que podría estar mal.")],
    selfcheck=[ex("En Orientación: ¿una acción segura incluye avisar a un adulto?", "Sí", "Consigue ayuda competente."), ex("¿Debes grabar una pelea para difundirla?", "No", "Difundirla agrava el daño."), ex("¿Una persona intoxicada que no responde necesita ayuda urgente?", "Sí", "Podría estar en peligro grave.")],
    task=T("Lee los tres casos inventados: (a) una compañera duerme y no responde después de una fiesta; (b) una pelea en el patio; (c) un chat que te exige una imagen íntima. Para cada caso escribe: una acción segura, algo que no debes hacer y a quién avisar.", "(a) Segura: no dejarla sola y pedir a un adulto que llame a emergencia; no dar remedios; avisar a un adulto. (b) Segura: avisar al inspector o profesor; no grabar ni meterse. (c) Segura: no enviar, guardar captura, bloquear; no responder con amenazas; avisar a un adulto.", ["escribe una acción segura por caso", "escribe algo que no se debe hacer", "indica a quién avisar", "no incluye datos personales"], ["tabla escrita", "texto oral"], ["no decir a quién avisar", "dar remedios"], "Reconoce las acciones seguras y pregunta cuál sería la primera en cada caso."),
    reinforce="Escribe tres pasos de una acción segura ante una pelea.",
    extend="Explica por qué avisar a un adulto no es traicionar.",
)

lesson(
    OA3, 5,
    "Una hoja y un lápiz. El mapa de redes de apoyo y la lista de señales de una página web confiable están en los ejercicios. Todo con personas inventadas.",
    "Aprenderé a identificar redes de apoyo (familia, profesores, salud, centros comunitarios, fonos y páginas web) y a pedir ayuda con claridad. Sirve para saber a quién recurrir y cómo decir lo que pasa.",
    ["Sé elegir una acción segura.", "Sé que pedir ayuda cuida."],
    [
        "Una red de apoyo es el conjunto de personas e instituciones a las que puedes pedir ayuda. Incluye a tu familia o a una persona de tu casa, a tu profesor o profesora jefe y al equipo de orientación y convivencia escolar, a los centros de salud, a los centros comunitarios del barrio, a las líneas telefónicas como el Fono Niños 147 y a las páginas web de instituciones especializadas. Cada una ayuda en algo distinto: salud, seguridad, orientación, escucha.",
        "Para pedir ayuda, di quién eres, qué pasa, desde cuándo y qué necesitas. Ejemplo: «Soy Camila, de 1.º medio. Un compañero me presiona para consumir desde hace dos semanas. Necesito orientación». Si la primera persona no te ayuda, sigue con otra. Pedir ayuda no te quita el control: te da compañía para decidir.",
        "Antes de confiar en una página web, revisa cuatro señales: quién la publica (una institución pública, una universidad o una organización reconocida), la fecha, si cita fuentes y si no te pide dinero ni datos privados. Si no cumple, no la uses como única fuente.",
    ],
    [("red de apoyo", "personas e instituciones a las que se puede pedir ayuda"), ("centro comunitario", "lugar del barrio que ofrece actividades y apoyo a la comunidad"), ("fono especializado", "línea telefónica de ayuda para un tema determinado"), ("fuente confiable", "origen de información comprobable"), ("convivencia escolar", "equipo del colegio que cuida el buen trato")],
    [
        W("Elegir la red", "Fabián se siente muy angustiado y quiere hablar con un profesional por teléfono. ¿Qué parte de la red usa?", ["Necesita escucha profesional por teléfono.", "Existe el Fono Niños 147."], "El Fono Niños 147"),
        W("Evaluar una página web", "Una página web sobre drogas es de una universidad, tiene fecha reciente y cita estudios. ¿Es confiable?", ["La publica una universidad.", "Tiene fecha y fuentes.", "No pide dinero."], "Sí, cumple las señales"),
    ],
    [
        M("Pensar que pedir ayuda es debilidad.", "Se cree que hay que resolver todo solo.", "Pedir ayuda es una acción de cuidado y compañía."),
        M("Confiar en cualquier página web que aparezca primero.", "La posición no mide la calidad.", "Revisa quién publica, la fecha, las fuentes y que no pida dinero ni datos."),
    ],
    R=[
        ex("¿Cuál de estos apoyos es una línea telefónica de ayuda? A) El Fono Niños 147 B) El centro comunitario del barrio", "A", "El centro comunitario es un lugar físico; el Fono Niños 147 es una línea telefónica."),
        ex("En el colegio, alguien te presiona para consumir. ¿Qué apoyo tienes más cerca? A) La persona orientadora o tu profesora jefe B) El centro de salud de otra comuna", "A", "Están en el colegio y pueden actuar de inmediato."),
        ex("¿Cuál es una señal de página web confiable? A) La publica una universidad o institución pública, con fecha y fuentes B) Aparece primero en el buscador", "A", "El lugar en el buscador no mide la calidad."),
    ],
    U=[
        ex("¿Cuál es una buena frase para pedir ayuda? A) «Soy Ema, de 1.º medio. Un compañero me presiona desde hace una semana. Necesito orientación.» B) «No sé, olvídalo.»", "A", "Dice quién es, qué pasa, desde cuándo y qué necesita."),
        ex("Una página web te pide dinero y tus datos para ayudarte. ¿Es confiable? A) No B) Sí.", "A", "Una fuente confiable no pide datos privados ni dinero."),
        ex("Si el primer adulto no te ayuda, ¿qué haces? A) Sigues con otra persona de la red B) Dejas de pedir ayuda.", "A", "Hay varias personas e instituciones."),
    ],
    A=[
        ex("Une cada necesidad con su apoyo más directo: 1) atención de salud; 2) escucha telefónica profesional; 3) orientación escolar. Opciones: (a) Fono Niños 147; (b) centro de salud; (c) persona orientadora. Escribe 1-letra, 2-letra, 3-letra.", "1-b, 2-a, 3-c", "Cada necesidad coincide con su apoyo."),
        ex("Una página web sobre alcohol es de un blog anónimo, sin fecha, no cita fuentes y vende productos. ¿Cuántas señales de confianza cumple de las cuatro revisadas (quién, fecha, fuentes, sin pedir dinero)?", "0", "No cumple ninguna de las cuatro."),
        ex("Rodrigo quiere ayuda para un amigo que sufre violencia en su pareja. ¿A quién avisa primero? A) A la persona orientadora o convivencia escolar B) A todo el curso.", "A", "Un adulto puede activar la ayuda."),
    ],
    Z=[
        ex("¿Por qué conviene tener más de una persona en tu red de apoyo?", "Porque si una no puede ayudar, otra sí puede", "Varias personas dan más posibilidades de ayuda."),
        ex("¿Por qué conviene revisar la fecha de una página de salud? A) Porque la información puede cambiar B) Porque la fecha la hace más bonita.", "A", "Los datos de salud se actualizan."),
    ],
    D=[
        arith("La red de apoyo de un estudiante inventado tiene 2 personas de su casa, 3 adultos del colegio, 1 centro de salud y 1 línea de ayuda. ¿Cuántos apoyos tiene en total?", "2+3+1+1", "Se suman los apoyos de cada tipo."),
        arith("Un centro comunitario inventado realiza 3 talleres por semana durante 6 semanas. ¿Cuántos talleres hace en total?", "3*6", "Se multiplican talleres por semanas."),
    ],
    context=[ex("Darío siente que un compañero lo golpea a escondidas desde hace tres semanas. ¿Cuál es la mejor manera de pedir ayuda? A) Contar quién es, qué pasa y desde cuándo a la persona orientadora B) Esperar a que se pase.", "A", "Dar hechos concretos permite que el adulto actúe.")],
    selfcheck=[ex("En Orientación: ¿una red de apoyo incluye a la familia y al colegio?", "Sí", "Son parte de la red."), ex("¿Una página que pide tus datos privados es confiable?", "No", "Puede ser peligrosa."), ex("¿Pedir ayuda es una forma de cuidarte?", "Sí", "Te da compañía y protección.")],
    task=T("Lee el caso inventado: Pía observa que su amiga Tania llora a diario porque su pololo la insulta y le controla el celular. Escribe: un mensaje breve de pedido de ayuda para la persona orientadora (quién, qué pasa, desde cuándo y qué necesita), y tres apoyos de la red que podrías mencionar.", "Hola, soy Pía de 1.º medio. Mi amiga Tania llora a diario desde hace dos semanas porque su pololo la insulta y le controla el celular. Necesito orientación para ayudarla. Apoyos: orientadora, centro de salud, Fono Niños 147.", ["el mensaje dice quién, qué, desde cuándo y qué necesita", "nombra tres apoyos de la red", "no culpa a Tania", "no incluye datos personales reales"], ["mensaje escrito", "texto oral"], ["mensaje vago", "olvidar el pedido concreto"], "Reconoce las partes del mensaje y pregunta cuál apoyo contactaría primero."),
    reinforce="Dibuja un mapa de red de apoyo con cinco recuadros para un personaje inventado.",
    extend="Explica por qué una página web confiable no te pide dinero ni datos privados.",
)

lesson(
    OA3, 6,
    "Una hoja y un lápiz. Los casos de Dante y de Francisca, personas inventadas, están escritos en los ejercicios; no se pide contar experiencias propias.",
    "Aprenderé a aplicar lo aprendido a casos nuevos y a diseñar un protocolo de ayuda del curso. Sirve para evaluar riesgos y recurrir a la red de apoyo sin exponerme.",
    ["Sé evaluar riesgos, elegir acciones seguras y reconocer redes de apoyo.", "Sé no guardar secretos dañinos."],
    [
        "Transferir es aplicar lo aprendido a un caso nuevo. Usa una secuencia de cinco pasos: 1) leer el caso y separar hechos y emociones, 2) identificar factores de riesgo y de protección, 3) comparar opciones con el semáforo, 4) elegir una acción segura, 5) decidir a quién de la red de apoyo se avisa. Con esta secuencia puedes analizar casos de consumo de sustancias, de conductas sexuales de riesgo o de violencia sin hablar de ti.",
        "Un curso también puede tener un protocolo de ayuda: pasos acordados que todos conocen. Por ejemplo: «si alguien está en riesgo, no lo dejamos solo; avisamos a un adulto; no grabamos ni difundimos; respetamos lo que se cuenta». Un buen protocolo es corto, fácil de recordar y deja claro quién avisa a quién.",
        "Recuerda que en los casos de riesgo la persona afectada nunca es culpable, que los secretos que ocultan un daño no se guardan y que no es necesario resolver todo solo. Pedir ayuda es parte de evaluar bien la situación.",
    ],
    [("transferir", "aplicar lo aprendido a un caso distinto"), ("protocolo", "conjunto de pasos acordados para actuar en una situación"), ("hecho", "dato que se puede comprobar"), ("factor de riesgo", "situación que aumenta la posibilidad de un daño"), ("red de apoyo", "personas e instituciones que ayudan")],
    [
        W("Aplicar la secuencia", "Caso: Dante recibe mensajes de un adulto que le pide secreto y fotos. Aplica los pasos 2 y 4.", ["Riesgo: un adulto pide secreto y fotos.", "Acción segura: no responder, guardar capturas, bloquear y avisar a un adulto."], "Riesgo alto; acción: guardar capturas, bloquear y avisar"),
        W("Redactar un protocolo", "Convierte «ayudemos a quien lo necesita» en un paso observable.", ["Debe decir qué se hace.", "«Si alguien está en riesgo, avisamos a un adulto del colegio.»"], "«Si alguien está en riesgo, avisamos a un adulto del colegio.»"),
    ],
    [
        M("Aplicar solo una parte de la secuencia.", "Se salta de los hechos a la acción.", "Sigue los cinco pasos en orden."),
        M("Hacer un protocolo muy largo y confuso.", "No se recuerda en una emergencia.", "Hazlo corto, con verbos y con responsables."),
    ],
    R=[
        ex("En la secuencia de cinco pasos, ¿cuál es el paso 3? A) Comparar opciones con el semáforo B) Identificar factores de riesgo", "A", "El paso 2 identifica factores y el 3 compara opciones."),
        ex("Un curso acuerda: «no grabamos, no difundimos, avisamos a un adulto». ¿Para qué sirve? A) Para que todos sepan cómo actuar ante un riesgo B) Para decidir quién tiene la razón", "A", "Un protocolo da pasos conocidos para actuar rápido."),
        ex("Tras una agresión, un compañero comenta: «ella se lo buscó». ¿Qué falta en esa idea? A) Que la responsabilidad es de quien daña B) Que hay que grabar la agresión", "A", "La persona afectada nunca es culpable."),
    ],
    U=[
        ex("¿Cuál es el primer paso de la secuencia? A) Leer el caso y separar hechos y emociones B) Elegir a quién culpar.", "A", "Se parte por entender el caso."),
        ex("¿Cuál es un buen paso de protocolo? A) «No dejamos solo a quien está en riesgo y avisamos a un adulto.» B) «Cada uno hace lo que quiera.»", "A", "Describe una acción clara."),
        ex("¿Qué se hace después de comparar opciones con el semáforo? A) Elegir una acción segura B) Cerrar el caso.", "A", "Es el paso 4."),
    ],
    A=[
        ex("Francisca, personaje inventado, cuenta que su pareja le prohíbe ver a su familia y la insulta. Según los cinco pasos, ¿cuál es el paso 5? A) Decidir a quién de la red se avisa B) Leer el caso otra vez.", "A", "El último paso es elegir la ayuda."),
        ex("Clasifica con F (factor de riesgo) o P (protección): 1) un adulto que pide secreto; 2) un curso con protocolo claro; 3) un grupo que difunde fotos. Escribe las letras en orden.", "F, P, F", "La 1 y la 3 aumentan el riesgo; la 2 protege."),
        ex("Un protocolo de curso dice «avisamos a un adulto, no grabamos, no difundimos». ¿Cuántas acciones concretas nombra?", "3", "Avisar, no grabar y no difundir."),
    ],
    Z=[
        ex("¿Por qué un protocolo corto es mejor que uno largo?", "Porque se recuerda y se usa cuando hay urgencia", "En una emergencia hay poco tiempo para leer."),
        ex("Un compañero dice: «No avisemos, que se resuelva solo». ¿Qué falta en su idea? A) Que el riesgo puede crecer sin ayuda adulta B) Que siempre hay que grabar.", "A", "Dejar pasar el tiempo puede aumentar el daño."),
    ],
    D=[
        arith("Un protocolo inventado tiene 5 pasos y 12 equipos del colegio lo revisan. Si cada equipo anota 2 mejoras por paso, ¿cuántas mejoras anotan en total?", "12*5*2", "Se multiplican equipos, pasos y mejoras."),
        arith("De 150 estudiantes inventados, 90 conocen el protocolo del colegio. ¿Cuántos no lo conocen?", "150-90", "Al total se le restan los que sí lo conocen."),
    ],
    context=[ex("En el Consejo de Curso se propone un protocolo de ayuda. ¿Qué parte es mejor incluir? A) Una lista de adultos a quienes avisar B) Una lista de los estudiantes con problemas.", "A", "Protege la privacidad y facilita la ayuda.")],
    selfcheck=[ex("En Orientación: ¿un protocolo debe ser corto y claro?", "Sí", "Así se recuerda."), ex("¿Se guarda un secreto que oculta un daño?", "No", "Hay que avisar a un adulto."), ex("¿Se puede analizar un caso sin hablar de ti?", "Sí", "Los casos ficticios protegen la privacidad.")],
    task=T("Un curso inventado debe redactar su protocolo de ayuda con tres pasos observables para tres situaciones: consumo en una fiesta, violencia en una pareja y una imagen íntima que circula. Redacta el protocolo de tres pasos: qué se hace primero, a quién se avisa y qué no se hace.", "Primero: no dejamos solo a quien está en riesgo. Segundo: avisamos a un adulto del colegio (orientación o convivencia). No hacemos: grabar, difundir ni reenviar imágenes.", ["escribe los tres pasos", "usa verbos observables", "incluye a quién avisar y qué no hacer", "no pide experiencias personales"], ["protocolo escrito", "afiche"], ["pasos vagos", "olvidar lo que no se hace"], "Reconoce los pasos claros y pregunta cuál es el más fácil de recordar."),
    reinforce="Escribe los cinco pasos de la secuencia con tus palabras.",
    extend="Explica por qué un protocolo ayuda a decidir bajo presión.",
)

# ================================================================ OA 04
lesson(
    OA4, 1,
    "Una hoja y un lápiz. La semana de Renata, una estudiante inventada, está escrita en los ejercicios. No necesitas contar tu propia rutina.",
    "Aprenderé a examinar un caso de vida saludable y a reconocer hábitos de alimentación, descanso, manejo del estrés y uso del tiempo de ocio. Sirve para detectar qué cuida el bienestar y qué lo desgasta.",
    ["Sé que dormir, comer bien y moverme cuidan mi salud (8.º básico).", "Sé que el estrés es una reacción normal."],
    [
        "Una vida saludable no se logra con una sola acción, sino con hábitos: la alimentación variada, el descanso suficiente, la actividad física, el manejo del estrés, el uso positivo del tiempo de ocio y la seguridad en lo cotidiano. Cada hábito se puede observar en una rutina semanal. Examinar un caso es leer esa rutina y detectar qué cuida y qué desgasta.",
        "El estrés es la reacción del cuerpo ante una exigencia, como una prueba. Es normal y puede ayudar a esforzarte; pero cuando es muy intenso y dura mucho, causa cansancio, dolor de cabeza, irritabilidad o dificultad para dormir. El tiempo de ocio es el tiempo libre: puede usarse en actividades que descansan y enriquecen, como caminar, leer, tocar música o jugar con amigos, o en otras que dejan más cansado.",
        "Cuidar la salud también es social: tus hábitos influyen en tu familia y en tu curso, y el entorno influye en ti. Por eso, al examinar un caso se separan los hechos de la rutina, las emociones del personaje y las acciones que podría mejorar con apoyo.",
    ],
    [("hábito", "conducta que se repite y forma parte de la rutina"), ("estrés", "reacción del cuerpo ante una exigencia"), ("tiempo de ocio", "tiempo libre que se usa para descansar o disfrutar"), ("bienestar", "sensación de estar bien física y emocionalmente"), ("rutina", "conjunto de actividades que se repiten cada día o semana")],
    [
        W("Clasificar hábitos", "Renata duerme 6 horas, toma agua durante el día y camina 30 minutos al regresar. ¿Cuáles cuidan su salud?", ["Beber agua y caminar cuidan su salud.", "Dormir solo 6 horas puede ser poco para su edad."], "Agua y caminata cuidan; el sueño corto desgasta"),
        W("Detectar estrés", "Renata dice: «Tengo prueba mañana, me duele la cabeza y no puedo dormir». ¿Qué señales de estrés aparecen?", ["Dolor de cabeza.", "Dificultad para dormir.", "Son reacciones a una exigencia."], "Dolor de cabeza y dificultad para dormir"),
    ],
    [
        M("Creer que el estrés es siempre malo.", "Se confunde cualquier tensión con daño.", "Un nivel moderado ayuda; el problema es cuando es intenso y se prolonga."),
        M("Pensar que descansar es perder el tiempo.", "Se valora solo lo productivo.", "El descanso y el ocio positivo cuidan la salud."),
    ],
    R=[
        ex("Clasifica cada hábito con C (cuida) o D (desgasta): 1) beber agua durante el día; 2) dormir 5 horas por varias semanas. Escribe las letras en orden.", "C, D", "La hidratación cuida; dormir muy poco por semanas desgasta."),
        ex("Un estudiante tiene prueba mañana y siente dolor de cabeza y dificultad para dormir. ¿Qué describe eso? A) Una reacción de estrés B) Una forma de ocio", "A", "Son reacciones del cuerpo ante una exigencia."),
        ex("¿Cuál es un uso positivo del tiempo de ocio? A) Jugar a la pelota con amigos B) Mirar el celular hasta la madrugada", "A", "Descansa y enriquece; lo otro quita sueño."),
    ],
    U=[
        ex("¿Cuál es una señal posible de estrés muy alto? A) Dolor de cabeza y dificultad para dormir B) Tener buen apetito y energía.", "A", "Son reacciones frecuentes ante estrés intenso."),
        ex("¿Qué hábito pertenece al descanso? A) Dormir lo suficiente B) Estudiar toda la noche.", "A", "Dormir restaura el cuerpo."),
        ex("Renata revisa su rutina de la semana. ¿Qué hace ese examen? A) Detecta qué cuida y qué desgasta B) Elimina el estrés.", "A", "Observar la rutina permite mejorarla."),
    ],
    A=[
        ex("Clasifica cada hábito como C (cuida) o D (desgasta): 1) cenar a tiempo y sin pantallas; 2) quedarse sin dormir antes de una prueba; 3) hacer una pausa activa de 10 minutos. Escribe las letras en orden.", "C, D, C", "La 1 y la 3 cuidan; la 2 desgasta."),
        ex("Renata anotó en su semana: lunes 7 horas de sueño, martes 6, miércoles 8. ¿Cuántas horas durmió en los tres días?", "21", "7 + 6 + 8 suman 21 horas."),
        ex("En una semana de ejemplo, Renata dedicó a pantallas 3 horas diarias y a deporte media hora diaria. ¿Qué actividad ocupó más tiempo? A) Pantallas B) Deporte.", "A", "3 horas es más que media hora."),
    ],
    Z=[
        ex("¿Por qué dormir poco antes de una prueba puede perjudicar el rendimiento?", "Porque el cansancio reduce la atención y la memoria", "El descanso ayuda a concentrarse y recordar."),
        ex("Un amigo dice: «Siempre estoy estresado, es normal». ¿Qué conviene decirle? A) Que si el estrés es intenso y dura mucho, conviene conversarlo con un adulto de confianza B) Que lo ignore.", "A", "Un estrés persistente afecta la salud."),
    ],
    D=[
        arith("Renata duerme 7 horas por noche de lunes a viernes. ¿Cuántas horas duerme en esos cinco días?", "7*5", "Se multiplican horas por noches."),
        arith("En un día, Renata reparte 24 horas así: 8 de sueño, 7 de colegio y 3 de tareas. Si el resto es libre, ¿cuántas horas libres tiene?", "24-8-7-3", "Al total del día se le restan las horas ocupadas."),
    ],
    context=[ex("En la semana de exámenes, tu curso conversa sobre cómo estudiar sin dejar de dormir. ¿Qué propuesta cuida la salud? A) Estudiar un poco cada día y dormir lo necesario B) Dejar todo para la noche anterior.", "A", "Distribuye el esfuerzo y protege el descanso.")],
    selfcheck=[ex("En Orientación: ¿los hábitos se ven en la rutina?", "Sí", "Se repiten cada día o semana."), ex("¿El estrés puede causar dificultad para dormir?", "Sí", "Es una reacción frecuente."), ex("¿El ocio positivo cuida el bienestar?", "Sí", "Descansa y enriquece.")],
    task=T("Lee la semana inventada de Joaquín: duerme 6 horas; toma bebidas azucaradas en los recreos; camina 20 minutos al ir al colegio; tiene una prueba el viernes y dice sentirse tenso; los fines de semana juega fútbol con amigos. Escribe una tabla con dos hábitos que cuidan, dos que desgastan, una señal de estrés y una acción posible para mejorar.", "Cuidan: caminar y jugar fútbol. Desgastan: dormir 6 horas y bebidas azucaradas. Señal: está tenso por la prueba. Acción: dormir una hora más y estudiar un poco cada día.", ["identifica hábitos que cuidan", "identifica hábitos que desgastan", "nombra una señal de estrés", "propone una acción"], ["tabla escrita", "texto oral"], ["culpar al personaje", "proponer cambios imposibles"], "Reconoce los hábitos bien clasificados y pregunta cuál cambio sería más fácil de iniciar."),
    reinforce="Anota tres hábitos que cuidan la salud de un personaje inventado.",
    extend="Explica por qué el estrés moderado puede ayudar y el muy intenso puede dañar.",
)

lesson(
    OA4, 2,
    "Una hoja y un lápiz. La tabla de etiquetas de alimentos y los datos de sueño están escritos en los ejercicios; son datos de ejemplo.",
    "Aprenderé a distinguir hechos, derechos y límites sobre alimentación, descanso, estrés y seguridad cotidiana. Sirve para decidir con información y para saber qué puedo cambiar yo y en qué necesito apoyo.",
    ["Sé reconocer hábitos que cuidan y que desgastan.", "Sé que las cifras de un cuadro deben leerse con cuidado."],
    [
        "En Chile, los alimentos envasados que tienen mucho azúcar, sodio, grasas saturadas o calorías llevan un sello negro de «ALTO EN». Es un hecho que ayuda a elegir. Una alimentación saludable incluye verduras, frutas, legumbres, agua y comidas regulares. En sueño, en general se recomienda que adolescentes duerman entre 8 y 10 horas; es una recomendación general y cada persona puede necesitar un poco más o menos.",
        "Tienes derecho a la salud, al descanso, al juego y a ser cuidado, y los adultos y las instituciones deben proteger esos derechos. Pero también hay límites: no todo depende de ti, por ejemplo qué hay en el almacén o en el kiosco del barrio. Por eso, distingue qué puedes decidir tú, como beber agua o pedir una pausa, y qué requiere apoyo, como pedir a la familia cambios en las compras.",
        "En seguridad cotidiana, hay hechos básicos: usar casco en bicicleta, cruzar por el paso de cebra, avisar a una persona adulta dónde estarás y no manipular cosas peligrosas. Estas medidas reducen el riesgo y se pueden decidir de forma autónoma.",
    ],
    [("sello «ALTO EN»", "etiqueta negra que avisa de exceso de azúcar, sodio, grasas saturadas o calorías"), ("hidratación", "tomar suficiente agua"), ("recomendación general", "consejo para la mayoría de las personas, no una regla exacta"), ("autonomía", "capacidad de decidir y actuar por uno mismo"), ("paso de cebra", "lugar marcado para cruzar la calle a pie")],
    [
        W("Leer una etiqueta", "Una galleta de ejemplo lleva el sello «ALTO EN azúcares». ¿Qué te informa?", ["El sello avisa de un exceso.", "Contiene mucha azúcar."], "Que tiene exceso de azúcares"),
        W("Qué depende de mí", "Pía quiere comer más verduras, pero en su casa no se compran. ¿Qué puede decidir ella y qué necesita apoyo?", ["Ella puede pedir verduras en el almuerzo del colegio y tomar agua.", "Las compras de la casa requieren hablar con una persona adulta."], "Decide pedir y tomar agua; el apoyo es para las compras"),
    ],
    [
        M("Creer que un alimento sin sello es siempre saludable.", "Se confunde ausencia de sello con calidad.", "Mira la variedad de la dieta y los ingredientes."),
        M("Pensar que descansar menos es solo cuestión de voluntad.", "Se ignoran las condiciones, como horarios y ruido.", "Distingue qué cambiar tú y qué conversar con otros."),
    ],
    R=[
        ex("Clasifica cada frase como H (hecho) u O (opinión): 1) «Esta bebida de ejemplo tiene sello ALTO EN azúcares.» 2) «Esa bebida es la más rica.» Escribe las letras en orden.", "H, O", "La 1 se comprueba en la etiqueta; la 2 es un gusto."),
        ex("Clasifica con D (depende de mí) o A (requiere apoyo): 1) tomar un vaso de agua; 2) que en casa se compren más frutas. Escribe las letras en orden.", "D, A", "La 1 la decides tú; la 2 se conversa con quien compra."),
        ex("¿Cuál es una medida de seguridad para andar en bicicleta? A) Usar casco y luces B) Pedalear con audífonos puestos", "A", "El casco protege la cabeza y las luces te hacen visible."),
    ],
    U=[
        ex("¿Qué dice el sello «ALTO EN grasas saturadas»? A) Que tiene exceso de ese nutriente B) Que no tiene grasas.", "A", "Es un aviso de exceso."),
        ex("La recomendación general de sueño para adolescentes es de 8 a 10 horas. ¿Qué significa «general»? A) Que sirve para la mayoría, no es una regla exacta B) Que es obligatoria.", "A", "Cada persona puede variar."),
        ex("¿Qué requiere apoyo de otras personas? A) Cambiar qué se compra en la casa B) Tomar un vaso de agua.", "A", "Depende de una decisión familiar."),
    ],
    A=[
        ex("Cuenta cuántas medidas de seguridad hay: usar casco, cruzar por el paso de cebra, avisar dónde estás, subir al auto sin cinturón.", "3", "Las tres primeras son medidas de seguridad; subir sin cinturón es un riesgo."),
        ex("Una etiqueta de ejemplo trae dos sellos negros: «ALTO EN azúcares» y «ALTO EN calorías». ¿Cuántos excesos avisa?", "2", "Cada sello avisa un exceso."),
        ex("Matías duerme 6 horas por noche y la recomendación general para adolescentes es de 8 a 10 horas. ¿Cuántas horas le faltan como mínimo para llegar a 8?", "2", "8 menos 6 son 2 horas."),
    ],
    Z=[
        ex("¿Por qué es útil distinguir lo que depende de ti de lo que requiere apoyo?", "Porque permite actuar donde puedes y pedir ayuda donde no", "Evita frustrarse o culparse por lo que no controla."),
        ex("Un joven dice: «Si no duermo 8 horas exactas, fallo». ¿Qué le falta entender? A) Que 8 a 10 es una recomendación general B) Que no hay que dormir.", "A", "Hay variación entre personas."),
    ],
    D=[
        arith("Una persona de ejemplo duerme 7 horas de lunes a viernes y 9 horas sábado y domingo. ¿Cuántas horas duerme en la semana?", "7*5+9*2", "Se suman las horas de días de semana y las del fin de semana."),
        arith("Un kiosco de ejemplo vende 40 productos y 25 tienen sello «ALTO EN». ¿Cuántos no tienen sello?", "40-25", "Al total se le restan los que sí tienen sello."),
    ],
    context=[ex("En el kiosco del barrio, casi todo tiene sellos «ALTO EN» (dato de ejemplo). Un curso quiere hacer una campaña para informar a sus compañeros. ¿Qué conviene hacer? A) Presentar una propuesta con datos al Consejo de Curso B) Dejar de comer.", "A", "Es una acción colectiva pacífica y con datos.")],
    selfcheck=[ex("En Orientación: ¿el sello «ALTO EN» avisa de un exceso?", "Sí", "Es una etiqueta para decidir mejor."), ex("¿Todo depende solo de la voluntad?", "No", "Hay condiciones que requieren apoyo."), ex("¿Usar casco es una medida de seguridad?", "Sí", "Protege la cabeza.")],
    task=T("Lee los datos de ejemplo de una semana: Camila duerme 6 horas por noche; en el kiosco del barrio hay galletas con sello «ALTO EN azúcares», fruta y yogur; en su barrio hay una ciclovía y ella tiene bicicleta sin casco. Separa: dos hechos, una cosa que depende de ella, una que requiere apoyo y una medida de seguridad que debería tomar.", "Hechos: duerme 6 horas; hay galletas con sello. Depende de ella: elegir fruta o yogur. Requiere apoyo: conseguir un casco. Seguridad: usar casco al andar en bicicleta.", ["separa hechos", "nombra lo que depende de ella", "nombra lo que requiere apoyo", "propone una medida de seguridad"], ["lista escrita", "texto oral"], ["culpar a Camila", "confundir hecho con opinión"], "Reconoce los hechos bien identificados y pregunta qué apoyo pediría y a quién."),
    reinforce="Anota dos sellos «ALTO EN» y qué exceso avisa cada uno.",
    extend="Explica por qué una recomendación general no es una regla exacta.",
)

lesson(
    OA4, 3,
    "Una hoja y un lápiz. Los planes de estudio de Tomás y de Valentina, personas inventadas, están escritos en los ejercicios.",
    "Aprenderé a comparar opciones para manejar el estrés y usar el tiempo de ocio, y a prever sus consecuencias. Sirve para decidir cómo organizarme sin descuidar mi salud.",
    ["Sé distinguir hechos, derechos y límites.", "Sé reconocer señales de estrés."],
    [
        "Para manejar el estrés hay estrategias sanas y otras que no ayudan. Entre las sanas están organizarse en pasos pequeños, respirar profundo, hacer una pausa activa, moverse, hablar con alguien de confianza y dormir. Entre las que no ayudan están dejar todo para última hora, evitar el problema, aislarse o usar sustancias para calmarse, porque pueden empeorar la situación.",
        "El tiempo de ocio también se decide. Puedes usarlo en pantallas, deporte, música, lectura, voluntariado, tiempo con amigos o descanso. No hay una sola correcta, pero cada una tiene consecuencias. Mucho tiempo seguido en pantallas puede quitar horas de sueño y movimiento; combinar actividades suele equilibrar mejor. Elegir bien es considerar cómo te sentirás después y qué te falta cuidar.",
        "Para comparar opciones, mira el costo de hoy y el efecto de mañana. Una opción puede ser cómoda hoy y cansar mañana; otra puede costar un poco y aliviar después. Un plan realista suma dos o tres estrategias, no veinte, y se prueba una semana antes de cambiar.",
    ],
    [("estrategia", "forma planificada de enfrentar un problema"), ("pausa activa", "descanso corto con movimiento"), ("organizarse", "dividir las tareas en pasos y repartirlas en el tiempo"), ("equilibrio", "reparto parejo entre distintas actividades"), ("consecuencia", "lo que ocurre después de una decisión")],
    [
        W("Comparar planes", "Tomás tiene prueba el viernes. Plan A: estudiar 30 minutos cada día lunes a jueves. Plan B: estudiar 4 horas el jueves en la noche. ¿Cuál cuida mejor su salud?", ["El plan A reparte el esfuerzo.", "El plan B puede quitar sueño."], "El plan A"),
        W("Elegir ocio", "Valentina tiene 2 horas libres. Opción 1: dos horas de videojuegos seguidas. Opción 2: 1 hora de caminata con una amiga y 1 hora de música. ¿Cuál equilibra más?", ["La opción 2 combina movimiento y descanso.", "La opción 1 usa una sola actividad."], "La opción 2"),
    ],
    [
        M("Dejar todo para la última noche para «rendir más con la presión».", "Se confunde estrés con motivación.", "Distribuir el estudio reduce el cansancio y mejora la memoria."),
        M("Usar sustancias para calmar el estrés.", "Alivian un momento y pueden crear nuevos problemas.", "Usa estrategias como pausa, movimiento y hablar con alguien."),
    ],
    R=[
        ex("Antes de una prueba, Tomás se siente tenso. ¿Qué estrategia sana puede usar? A) Respirar profundo y hacer una pausa activa de 10 minutos B) Quedarse despierto toda la noche", "A", "Descansa con movimiento y baja la tensión."),
        ex("Una persona deja todo para la última hora y siente más tensión cada día. ¿Por qué ocurre? A) Porque el trabajo se junta y el tiempo no alcanza B) Porque el estrés desaparece al apurarse", "A", "Acumular tareas aumenta la tensión."),
        ex("Valentina se siente abrumada por las tareas. ¿Qué estrategia sana puede usar? A) Conversar con una persona de confianza y armar un plan B) Aislarse para pensar sola", "A", "Compartir reduce la carga."),
    ],
    U=[
        ex("¿Qué estrategia no ayuda? A) Aislarse y no hablar con nadie B) Respirar profundo.", "A", "Aislarse suele aumentar el malestar."),
        ex("¿Qué plan reparte mejor el esfuerzo? A) Estudiar un poco cada día B) Estudiar todo la noche anterior.", "A", "Distribuir evita el agotamiento."),
        ex("¿Qué consecuencia puede tener usar pantallas seguidas por muchas horas? A) Quitar tiempo al sueño y al movimiento B) Mejorar siempre el ánimo.", "A", "Desplaza otras actividades de cuidado."),
    ],
    A=[
        ex("Tomás tiene 5 días (lunes a viernes) y 150 minutos para estudiar. Si estudia lo mismo cada día, ¿cuántos minutos por día?", "30", "150 dividido en 5 días da 30 minutos."),
        ex("Clasifica con S (sana) o N (no sana): 1) respirar profundo antes de una prueba; 2) usar alcohol para calmarse; 3) dormir lo suficiente. Escribe las letras en orden.", "S, N, S", "La 1 y la 3 cuidan; la 2 es riesgosa."),
        ex("Valentina tiene tres planes para el sábado: A) 5 horas de pantalla; B) 1 hora de pantalla, 2 de deporte y 1 de lectura; C) 3 horas de sueño extra. ¿Cuál combina más actividades?", "B", "Incluye tres tipos de actividad."),
    ],
    Z=[
        ex("¿Por qué dividir una tarea grande en pasos pequeños reduce el estrés?", "Porque cada paso parece alcanzable y se avanza con orden", "Una meta dividida es menos abrumadora."),
        ex("Un amigo dice: «El estrés se me pasa con vapeador». ¿Qué le responderías? A) Que alivia un momento y crea riesgos para la salud; hay estrategias más sanas B) Que está bien.", "A", "Los vapeadores no resuelven el problema y dañan la salud."),
    ],
    D=[
        arith("Tomás estudia 25 minutos y descansa 5, y repite 4 veces. ¿Cuántos minutos dura todo el ciclo?", "(25+5)*4", "Se suma estudio y descanso y se multiplica por las repeticiones.", " minutos"),
        arith("Valentina duerme 8 horas, está 7 en el colegio, 3 en tareas y 2 en traslados. ¿Cuántas horas libres le quedan de 24?", "24-8-7-3-2", "Al total se le restan las horas ocupadas."),
    ],
    context=[ex("La semana anterior a las pruebas, un curso decide organizarse en grupos de estudio de 45 minutos con pausas. ¿Qué ventaja tiene? A) Distribuye el esfuerzo y acompaña B) Estudian más rápido sin necesidad de dormir.", "A", "Reparte la carga y da apoyo.")],
    selfcheck=[ex("En Orientación: ¿una pausa activa es una estrategia sana?", "Sí", "Descansa con movimiento."), ex("¿Aislarse ayuda a manejar el estrés?", "No", "Suele empeorar el malestar."), ex("¿Combinar actividades en el ocio equilibra mejor?", "Sí", "Reparte el tiempo entre varias cosas.")],
    task=T("Lee el caso inventado: Ignacio tiene dos pruebas el jueves y una tarea el miércoles. Duerme poco y siente dolor de cabeza. Escribe un plan de tres días (lunes a miércoles) con dos estrategias de manejo del estrés y una actividad de ocio positiva, y explica una consecuencia de cumplir el plan.", "Lunes: estudiar 30 minutos y caminar 15. Martes: estudiar 30 minutos y hacer una pausa de respiración. Miércoles: terminar la tarea y tocar música 30 minutos. Consecuencia: llega con más descanso y menos tensión.", ["escribe un plan de tres días", "incluye dos estrategias sanas", "incluye una actividad de ocio positiva", "explica una consecuencia"], ["plan escrito", "tabla"], ["plan irreal", "usar sustancias"], "Reconoce el plan realista y pregunta qué ajustaría si no alcanza el tiempo."),
    reinforce="Escribe dos estrategias para un personaje inventado que tiene una exposición mañana.",
    extend="Explica por qué un plan realista suma pocas estrategias.",
)

lesson(
    OA4, 4,
    "Una hoja y un lápiz. Los casos de Elena y de Bastián, personas inventadas, están escritos en los ejercicios.",
    "Aprenderé a elegir y llevar a cabo acciones autónomas para mi vida saludable y mi seguridad en situaciones cotidianas. Sirve para pasar de saber a actuar con cuidado y de forma sostenida.",
    ["Sé comparar estrategias de manejo del estrés.", "Sé que las acciones seguras son concretas y pequeñas."],
    [
        "Una acción autónoma es aquella que decides tú, con información, y que puedes realizar sin que alguien te la imponga. Para que dure, conviene que sea pequeña, concreta y con un momento fijo: «tomar agua en cada recreo», «caminar 15 minutos después de las tareas», «apagar las pantallas 30 minutos antes de dormir». Se mide con una evidencia sencilla, como marcar un calendario.",
        "La prevención de riesgos cotidianos es parte de la vida saludable. Algunas acciones: usar casco y luces en bicicleta; cruzar por el paso de cebra y esperar la luz verde; avisar a una persona adulta adónde vas y a qué hora vuelves; no usar el celular mientras cruzas; saber cómo salir de tu colegio en un simulacro. Estas decisiones evitan accidentes.",
        "También hay una dimensión social: tus acciones pueden ayudar a otros. Por ejemplo, proponer pausas activas en el curso o recordar a un compañero el casco. Cuando una acción depende de otros, pides apoyo. Y si un hábito no resulta, ajústalo una semana: autonomía es aprender y corregir.",
    ],
    [("acción autónoma", "acción que decides tú con información y puedes realizar por ti mismo"), ("prevención", "acción para evitar un daño antes de que ocurra"), ("simulacro", "ensayo de cómo actuar ante una emergencia"), ("evidencia", "prueba sencilla de que cumpliste, como un calendario marcado"), ("hábito", "conducta que se repite")],
    [
        W("Convertir una idea en acción", "Elena quiere «comer mejor». Conviértelo en una acción concreta.", ["Debe ser pequeña y con momento fijo.", "«Llevar una fruta al recreo cada día»."], "«Llevar una fruta al recreo cada día»"),
        W("Prevención cotidiana", "Bastián sale en bicicleta a las 18:00. ¿Qué dos acciones previenen riesgos?", ["Usar casco.", "Avisar a una persona adulta adónde va y a qué hora vuelve."], "Casco y avisar adónde va"),
    ],
    [
        M("Proponerse cambios enormes de una vez.", "Se cree que el esfuerzo inmenso garantiza el resultado.", "Parte con una acción pequeña y sostenida."),
        M("Creer que prevenir es perder libertad.", "Se ve la prevención como prohibición.", "Prevenir permite disfrutar con menos riesgo."),
    ],
    R=[
        ex("Clasifica con C (concreta) o V (vaga): 1) «Tomar agua en cada recreo.» 2) «Cuidarme más.» Escribe las letras en orden.", "C, V", "La 1 dice qué hacer y cuándo; la 2 no."),
        ex("¿Cuál de estas acciones es de prevención? A) Avisar adónde vas y a qué hora vuelves B) Comprar una bicicleta nueva", "A", "Reduce el riesgo antes de que ocurra un daño."),
        ex("Un estudiante quiere comprobar que cumple su hábito de caminar. ¿Qué evidencia sencilla puede usar? A) Marcar un calendario cada día B) Recordarlo de memoria sin anotar", "A", "Lo anotado se puede revisar; la memoria falla."),
    ],
    U=[
        ex("¿Cuál es una acción autónoma bien formulada? A) «Caminar 15 minutos después de las tareas.» B) «Hacer deporte alguna vez.»", "A", "Es concreta y tiene momento fijo."),
        ex("¿Qué se hace cuando un hábito no resulta? A) Ajustarlo una semana y reintentar B) Abandonar todo.", "A", "Corregir es parte de la autonomía."),
        ex("Avisar adónde vas y a qué hora vuelves, ¿qué tipo de acción es? A) Preventiva B) Solo una costumbre sin efecto.", "A", "Reduce los riesgos."),
    ],
    A=[
        ex("Elena marcó en su calendario que tomó agua en recreos: lunes sí, martes sí, miércoles no, jueves sí, viernes sí. ¿Cuántos días cumplió?", "4", "Cumplió lunes, martes, jueves y viernes."),
        ex("Bastián llega a un cruce con semáforo y la luz para peatones está roja. ¿Qué debe hacer? A) Esperar a que cambie a verde B) Cruzar rápido si no vienen autos.", "A", "Respetar la luz peatonal previene atropellos."),
        arith("Elena se propuso tomar agua en los recreos 5 de los 7 días de la semana y lleva 3 días cumplidos. ¿Cuántos días le faltan para su propósito?", "5-3", "A los días propuestos se les restan los ya cumplidos."),
    ],
    Z=[
        ex("¿Por qué una acción pequeña y constante suele durar más que un gran cambio?", "Porque es más fácil de cumplir cada día", "Se vuelve hábito sin agotar."),
        ex("Un curso quiere proponer pausas activas. ¿Qué debe hacer? A) Pedir apoyo a su profesor jefe y probar una semana B) Imponerlas a otros sin hablar.", "A", "La acción social requiere apoyo y acuerdo."),
    ],
    D=[
        arith("Elena camina 15 minutos al día durante 6 días. ¿Cuántos minutos camina en total?", "15*6", "Se multiplican minutos por días.", " minutos"),
        arith("Un curso de 36 estudiantes forma 4 grupos iguales para proponer una acción saludable. ¿Cuántos integrantes tiene cada grupo?", "36//4", "Se divide el total entre los grupos."),
    ],
    context=[ex("En el simulacro del colegio, un compañero bromea y no sigue la ruta de salida. ¿Qué acción es segura? A) Seguir la ruta indicada y pedirle que lo haga B) Quedarse atrás.", "A", "El simulacro enseña cómo actuar ante una emergencia.")],
    selfcheck=[ex("En Orientación: ¿una acción autónoma se decide con información?", "Sí", "Es una decisión propia e informada."), ex("¿Es mejor empezar con una acción pequeña?", "Sí", "Se puede sostener."), ex("¿Usar casco es una acción preventiva?", "Sí", "Evita un daño grave.")],
    task=T("Lee el caso inventado de Mateo: duerme poco, toma muchas bebidas azucaradas y camina solo 5 minutos al día. Diseña un plan de dos semanas con tres acciones autónomas (una de alimentación o hidratación, una de descanso o estrés y una de seguridad), cada una concreta, con momento fijo y evidencia. Escribe también un apoyo que podría pedir.", "1) Beber agua en cada recreo; evidencia: marcar calendario. 2) Apagar pantallas 30 minutos antes de dormir; evidencia: anotar la hora. 3) Usar casco y avisar adónde va cuando sale en bicicleta; evidencia: calendario. Apoyo: pedir a la familia que compre agua o frutas.", ["escribe tres acciones", "cada una es concreta, con momento fijo y evidencia", "una es de seguridad", "nombra un apoyo"], ["plan escrito", "tabla"], ["acciones vagas", "plan demasiado largo"], "Reconoce las acciones concretas y pregunta cuál sería la primera en iniciar."),
    reinforce="Convierte «dormir mejor» en una acción concreta con hora y evidencia.",
    extend="Explica por qué la autonomía incluye ajustar los planes.",
)

lesson(
    OA4, 5,
    "Una hoja y un lápiz. Las frases de ejemplo y los casos de Laura y Gonzalo, personas inventadas, están escritos en los ejercicios.",
    "Aprenderé a comunicar cómo me siento cuando estoy muy estresado o decaído y a pedir ayuda a una persona adulta de confianza. Sirve para cuidar mi salud mental y apoyar a otros.",
    ["Sé manejar el estrés con estrategias sanas.", "Sé que pedir ayuda es una acción de cuidado."],
    [
        "Es normal sentirse triste, nervioso o enojado a veces. Pero si por varias semanas aparece mucho cansancio, tristeza, desánimo, pérdida de interés, problemas para dormir o comer, o ganas de aislarse, es una señal para pedir ayuda. Estas señales no son debilidad ni culpa de nadie: se cuidan igual que la salud del cuerpo.",
        "Para comunicarlo, usa frases en primera persona con tres partes: lo que sientes, desde cuándo y qué necesitas. Ejemplo: «Hace tres semanas me siento muy decaído y me cuesta levantarme. Necesito hablar con alguien». Elige a una persona adulta de confianza: de tu casa, el profesor jefe, la persona orientadora, o el centro de salud. También puedes llamar al Fono Niños 147. Si hay peligro inmediato, una persona adulta debe pedir ayuda a los servicios de emergencia.",
        "Si alguna vez un pensamiento de hacerse daño aparece en alguien, en ti o en un amigo, hay que avisar de inmediato a una persona adulta y no dejar sola a esa persona. Nunca se guarda ese secreto. Y si un amigo te cuenta que se siente mal, escucha sin juzgar, di que te importa y acompáñalo a hablar con un adulto.",
    ],
    [("salud mental", "bienestar de las emociones, los pensamientos y las relaciones"), ("decaído", "con poco ánimo y pocas ganas de hacer cosas"), ("señal de alerta", "cambio que indica que se necesita ayuda"), ("persona adulta de confianza", "adulto que escucha, cree y ayuda"), ("acompañar", "estar al lado de alguien sin juzgarlo")],
    [
        W("Armar una frase", "Laura se siente decaída hace un mes y no quiere ir a clases. ¿Qué frase usa para pedir ayuda?", ["Dice lo que siente: decaída.", "Dice desde cuándo: hace un mes.", "Dice qué necesita: hablar con alguien."], "«Hace un mes me siento muy decaída y me cuesta ir a clases. Necesito hablar con alguien.»"),
        W("Apoyar a un amigo", "Gonzalo le cuenta a un compañero que se siente muy mal y piensa que no vale nada. ¿Cuál es la mejor respuesta?", ["Escucharlo sin juzgar.", "Decirle que le importa.", "Acompañarlo a hablar con un adulto."], "Escucharlo, decirle que importa y acompañarlo con un adulto"),
    ],
    [
        M("Pensar que la tristeza que dura semanas se pasa sola sin hablar con nadie.", "Se cree que decir algo es exagerar.", "Si dura varias semanas, conviene hablar con un adulto."),
        M("Prometer a un amigo guardar el secreto si dice que quiere hacerse daño.", "Se confunde lealtad con protección.", "Avisa de inmediato a un adulto y no lo dejes solo."),
    ],
    R=[
        ex("Clasifica cada situación como N (normal) o S (señal para pedir ayuda): 1) estar nervioso el día de una exposición; 2) sentir tres semanas seguidas mucho desánimo y no querer ver a nadie. Escribe las letras en orden.", "N, S", "La 1 es pasajera; la 2 dura semanas y afecta la vida."),
        ex("Alguien dice: «Me siento muy decaído». ¿Qué partes de una frase para pedir ayuda le faltan? A) Desde cuándo y qué necesita B) Solo su nombre", "A", "Una buena frase dice qué siente, desde cuándo y qué necesita."),
        ex("Un compañero cuenta que hace semanas se siente muy decaído. ¿Cuál respuesta escucha sin juzgar? A) «Gracias por contarme, estoy contigo.» B) «Anímate, no es para tanto.»", "A", "Valida lo que siente y abre la posibilidad de buscar ayuda."),
    ],
    U=[
        ex("¿Qué partes tiene una frase para pedir ayuda emocional? A) Lo que sientes, desde cuándo y qué necesitas B) Solo un chiste.", "A", "Esas tres partes hacen clara la petición."),
        ex("¿Qué hace un buen amigo ante alguien que se siente muy mal? A) Escuchar sin juzgar y acompañarlo a pedir ayuda B) Contarlo al curso.", "A", "Cuida la privacidad y ayuda."),
        ex("Alguien siente tristeza intensa por semanas. ¿Cómo se entiende mejor esa situación? A) Es una señal de salud que se cuida, no una culpa B) Es una debilidad que conviene ocultar", "A", "Se cuida igual que la salud del cuerpo."),
    ],
    A=[
        ex("Cuatro frases: 1) «Me siento mal, olvídalo»; 2) «Hace dos semanas duermo muy poco y estoy muy ansioso; necesito hablar con alguien»; 3) «Nada importa»; 4) silencio. ¿Cuál tiene las tres partes?", "La 2", "Dice qué siente, desde cuándo y qué necesita."),
        arith("Gonzalo lleva 5 semanas con desgano. Si espera 3 semanas más sin pedir ayuda, ¿cuántas semanas habrá estado así en total?", "5+3", "Se suman las semanas transcurridas y las que espera."),
        ex("Un amigo te dice que quiere hacerse daño. ¿Qué haces? A) Avisar de inmediato a un adulto y quedarte con él B) Esperar a ver si se le pasa.", "A", "Hay riesgo y se necesita ayuda adulta."),
    ],
    Z=[
        ex("¿Por qué conviene pedir ayuda cuando el malestar dura varias semanas?", "Porque puede afectar la salud y se mejora con apoyo", "Un malestar prolongado se alivia con ayuda profesional y de confianza."),
        ex("Un compañero se burla de quien dice sentirse mal. ¿Qué respuesta cuida? A) «Es normal pedir ayuda; no es debilidad.» B) «Tiene razón, exageras.»", "A", "Respeta la dignidad y la salud mental."),
    ],
    D=[
        arith("Un colegio inventado ofrece orientación 4 horas al día durante 5 días. ¿Cuántas horas de orientación hay en la semana?", "4*5", "Se multiplican horas por días.", " horas"),
        arith("En una encuesta inventada de 60 estudiantes, 24 dicen que no saben a quién pedir ayuda. ¿Cuántos sí lo saben?", "60-24", "Al total se le restan los que no lo saben."),
    ],
    context=[ex("Valentina nota que su amiga lleva un mes sin hablar con nadie y llora mucho. ¿Qué es lo más responsable? A) Acompañarla a hablar con la persona orientadora B) Contarlo al curso.", "A", "Un adulto puede ayudar y se respeta la privacidad.")],
    selfcheck=[ex("En Orientación: ¿pedir ayuda por tristeza intensa es válido?", "Sí", "Es cuidar la salud mental."), ex("¿Se escucha sin juzgar a quien se siente mal?", "Sí", "Da confianza para hablar."), ex("¿Está bien guardar el secreto si alguien piensa hacerse daño?", "No", "Hay que avisar a un adulto.")],
    task=T("Lee el caso inventado: Leo lleva un mes sin ganas de salir, duerme mal y dice que nada le importa. Escribe: (1) una frase en primera persona con las tres partes para que Leo pida ayuda, (2) una respuesta de apoyo de un amigo que no juzga y (3) a quién podría acudir Leo en el colegio y fuera de él.", "(1) «Hace un mes duermo mal y no tengo ganas de nada; necesito hablar con alguien.» (2) «Gracias por contarme, me importas; vamos juntos a hablar con la orientadora.» (3) Orientadora, profesor jefe, una persona de su casa, centro de salud, Fono Niños 147.", ["la frase tiene sentir, desde cuándo y necesidad", "la respuesta del amigo no juzga", "nombra al menos tres apoyos", "no incluye datos personales"], ["texto escrito", "juego de roles"], ["frase sin necesidad concreta", "respuesta que juzga"], "Reconoce las frases claras y pregunta qué apoyo sería el primero."),
    reinforce="Escribe dos frases de apoyo para un amigo que se siente mal.",
    extend="Explica por qué cuidar la salud mental es tan importante como cuidar la salud del cuerpo.",
)
