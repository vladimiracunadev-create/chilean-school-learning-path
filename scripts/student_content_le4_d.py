"""Cuaderno del estudiante, 4.º básico Lenguaje y Comunicación: OA 24 (experiencia y lenguaje teatral)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA24 = "LE04 OA 24"
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


# ================================================================ OA 24 · clase 1
reg(
    OA24, 1,
    "Este cuaderno, lápiz y una hoja. Si puedes, una obra en vivo o grabada para ver con una persona de tu casa; si no, usa el afiche y las escenas escritas aquí.",
    "Aprenderé a prepararme para ver una obra de teatro: leer un afiche, predecir de qué trata, acordar cómo cuidar la función y llevar una pregunta para observar. Sirve para disfrutar más y para opinar con razones.",
    ["Sé que en el teatro los actores cuentan una historia con voz y cuerpo.", "Sé leer horas, días y precios."],
    [
        "El teatro es un género: una forma de contar historias en que personas las representan ante un público, en vivo. Antes de ir a ver una obra conviene leer el afiche, que informa el título, el lugar, el día, la hora y la duración. Muchos afiches traen una sinopsis, que es un resumen muy breve de la historia, sin contar el final. Con el título y la sinopsis podemos hacer una predicción: pensar qué puede pasar.",
        "Para cuidar la función, el público acuerda reglas simples: llegar con tiempo, apagar el celular, no hablar mientras actúan, reír cuando algo es gracioso y aplaudir al final. Estas reglas no piden quedarse sin sentir nada. Sirven para que todos puedan oír y ver, y para que los actores trabajen tranquilos.",
        "También ayuda llevar una pregunta para observar, por ejemplo: ¿cómo muestra el personaje que tiene miedo? Con una pregunta así miramos la escena completa. Después, al opinar, damos una razón: no decimos solo «me gustó el decorado», sino qué vimos y por qué nos hizo sentir algo. El decorado es lo que hay armado o pintado en el escenario; ayuda, pero la obra son las acciones, las voces y los gestos.",
    ],
    [("género", "tipo de texto o espectáculo, como el teatro"), ("función", "cada vez que se presenta una obra"), ("sinopsis", "resumen breve de la historia que no cuenta el final"), ("predicción", "idea de lo que podría pasar, apoyada en pistas"), ("decorado", "objetos y telones que forman el lugar de la escena")],
    [
        ("Leer un afiche", "Afiche: «La sombra de Tomás. Teatro de la Plaza. Viernes, 18:30. Duración: 55 minutos. Sinopsis: Tomás despierta y su sombra ya no está». ¿Cuál es el problema que anuncia la sinopsis?", ["Busco en la sinopsis lo que le pasa al personaje.", "Dice que despierta y su sombra ya no está.", "Eso es lo que debe resolver."], "Tomás perdió su sombra."),
        ("Opinar con razones", "Un amigo dice: «Me gustó la obra». Otra amiga dice: «Me gustó porque Tomás hablaba bajito cuando tenía miedo y se notaba». ¿Quién dio una razón?", ["Busco quién explica por qué.", "El amigo solo dice que le gustó.", "La amiga nombra lo que vio y lo que le hizo sentir."], "La amiga."),
    ],
    [("Creer que una obra es buena solo si el decorado es bonito.", "El decorado es solo una parte; la historia se cuenta con acciones, voz y gestos.", "Opina sobre personajes, conflicto, voz y cuerpo, además del decorado."), ("Pensar que cuidar la función es no sentir nada.", "Se confunde respetar con quedarse inmóvil.", "Reír, emocionarse y aplaudir sin molestar también cuidan la función.")],
    [
        E("Afiche: «La sombra de Tomás. Teatro de la Plaza. Viernes, 18:30». ¿En qué día es la función?", "El viernes", "El día está escrito en el afiche."),
        E("¿Cómo se llama el resumen breve de la historia que trae un afiche?", "Sinopsis", "Resume la historia sin contar el final."),
        E("Durante una función, ¿qué hace el público: mira y escucha la obra o actúa en el escenario?", "Mira y escucha la obra", "El público observa la función."),
    ],
    [
        E("Una sinopsis dice: «Una niña encuentra un mapa en el patio». ¿Qué predicción se apoya en esa pista: a) la niña saldrá a buscar algo b) la niña dormirá toda la obra?", "a", "Un mapa invita a buscar algo."),
        E("¿Por qué apagar el celular durante la función ayuda al público y a los actores?", "Porque evita luces y ruidos que distraen", "Así todos pueden concentrarse."),
        E("Elige la mejor pregunta para observar: a) ¿Qué hora es? b) ¿Cómo muestra el personaje que se siente solo?", "b", "La b te hace mirar voz, gestos y espacio."),
    ],
    [
        arith("Una entrada cuesta $2.000. Van cuatro personas. ¿Cuánto pagan en total?", "2000+2000+2000+2000", "Se suma el precio de cada entrada.", " pesos"),
        E("La función empieza a las 18:30 y dura 55 minutos. ¿A qué hora termina?", "A las 19:25", "De 18:30 a 19:00 pasan 30 minutos y faltan 25 más."),
        E("Ordena los pasos: a) aplaudir al final, b) leer el afiche, c) mirar la función en silencio. Escribe las letras.", "b, c, a", "Primero te informas, luego miras y al final aplaudes."),
    ],
    [
        E("Ana dice: «La obra fue mala porque el decorado era simple». Luis dice: «La historia me costó entenderla porque los actores hablaban muy bajito». ¿Cuál razón se refiere a cómo se contó la historia?", "La de Luis", "Habla de la voz de los actores, que cuenta la historia."),
        E("Una niña dice: «Me gustó». ¿Qué le falta a su opinión: a) una razón b) un precio?", "a", "Opinar bien incluye explicar por qué."),
    ],
    [
        E("Las puertas abren 45 minutos antes de las 18:30, y tú llegas 15 minutos después de que abren. ¿A qué hora llegas?", "A las 18:00", "Abren a las 17:45 y 15 minutos después son las 18:00."),
        E("Un afiche dice «Para niñas y niños desde 6 años». Tú tienes 9. ¿Puedes ir?", "Sí", "Nueve es mayor que seis."),
    ],
    [E("Lees el afiche «El tesoro del abuelo. Sala Norte. Domingo, 11:00. Duración: 40 minutos». Un compañero dice que irá a las 12:00 porque «igual es en la mañana». ¿Qué dato del afiche muestra que se perdería la función?", "La hora: 11:00", "A las 12:00 la función ya habría comenzado.")],
    [
        E("¿Qué datos informa un afiche de teatro?", "Título, lugar, día, hora y duración", "Son los datos para asistir a la función."),
        E("¿Una predicción necesita pistas?", "Sí", "Se apoya en título y sinopsis."),
        E("Opinar bien sobre una obra, ¿incluye una razón?", "Sí", "La razón sustenta lo que pensamos."),
    ],
    ("Prepárate para ver «El tesoro del abuelo». Afiche: «El tesoro del abuelo. Sala Norte. Domingo, 11:00. Duración: 40 minutos. Sinopsis: Una niña encuentra una llave sin puerta». Escribe o cuenta: 1) a qué hora termina la función, 2) tu predicción de lo que pasará, apoyada en la sinopsis, 3) tres acuerdos de público, 4) una pregunta para observar, que puedes elegir de esta lista: «¿Cómo muestra su curiosidad?», «¿Qué problema tiene la niña?», «¿Cómo cambia la voz cuando se asusta?». Si no puedes ver una obra, usa esta información y cuéntaselo a una persona de tu casa.",
     "1) Termina a las 11:40. 2) Creo que la niña buscará la puerta de la llave, porque la sinopsis habla de una llave sin puerta. 3) Llegar con tiempo, apagar el celular, no hablar mientras actúan. 4) ¿Cómo cambia la voz cuando se asusta?",
     ["calcula bien la hora de término", "la predicción usa una pista de la sinopsis", "escribe tres acuerdos que cuidan la función", "elige una pregunta que mira voz, cuerpo o conflicto"], ["hoja con las cuatro respuestas o explicación oral a una persona de tu casa"], ["predecir sin apoyarse en una pista", "proponer acuerdos que impiden reír o sentir"],
     "Si tu predicción no usa una pista, pregúntate: ¿qué palabra de la sinopsis me hizo pensar eso?"),
    "Lee otro afiche que te escriba una persona de tu casa y di título, lugar, día, hora y duración.",
    "Escribe un afiche para una obra imaginaria con título, lugar, día, hora, duración y una sinopsis de dos líneas.",
)

# ================================================================ OA 24 · clase 2
reg(
    OA24, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa que lea las escenas con distintas voces.",
    "Aprenderé a observar cómo la voz, el cuerpo y el espacio muestran lo que siente y quiere un personaje, y a explicarlo con pistas. Sirve para entender mejor una obra y para actuar con más claridad.",
    ["Sé que un personaje tiene emociones y deseos.", "Sé que en una obra se cuenta con voz y cuerpo, no solo con palabras."],
    [
        "En el teatro, además de las palabras, cuentan la voz, el cuerpo y el espacio. La voz cambia en volumen (fuerte o bajito), en ritmo (rápido o lento), en tono (alegre, serio, asustado) y en silencios. La proyección es hablar de modo que se oiga hasta la última fila. El cuerpo habla con la postura, la mirada y los gestos. El espacio es el lugar del escenario donde se mueve cada personaje, cerca o lejos de otros.",
        "Una pista sola no siempre alcanza. Si un personaje habla bajito, puede estar triste, pero también puede estar contando un secreto. Por eso juntamos varias pistas y miramos si coinciden. Cuando la voz, el cuerpo y el espacio dicen lo mismo, podemos explicar con más seguridad lo que siente. Cuando no coinciden, como alguien que dice «no tengo miedo» con voz temblorosa, esa diferencia también es una pista.",
        "Para explicar una escena usamos una frase en dos partes: nombramos la pista y decimos qué muestra. Por ejemplo: «Retrocedió dos pasos y habló con voz temblorosa, por eso parecía asustado». Así mostramos cómo se cuenta la historia, no solo qué ocurre.",
    ],
    [("volumen", "qué tan fuerte o bajito suena la voz"), ("ritmo", "qué tan rápido o lento se habla o se mueve"), ("proyección", "hablar de modo que se oiga hasta el fondo de la sala"), ("postura", "forma de colocar el cuerpo"), ("espacio escénico", "lugar del escenario por donde se mueven los personajes")],
    [
        ("Juntar pistas", "Escena: Mateo entra a pasos rápidos, habla fuerte y agita los brazos: «¡Se nos acaba el tiempo!». ¿Qué quiere o siente Mateo?", ["Voz: fuerte.", "Cuerpo: pasos rápidos y brazos agitados.", "Las tres pistas coinciden: prisa."], "Tiene prisa y quiere apurar a los demás."),
        ("Cuando las pistas no coinciden", "Escena: Clara dice «no me da miedo» con voz temblorosa y retrocede dos pasos. ¿Qué pista contradice sus palabras?", ["Comparo lo que dice con cómo lo dice.", "Dice que no tiene miedo.", "Pero tiembla la voz y retrocede."], "La voz temblorosa y el retroceso contradicen sus palabras: parece tener miedo."),
    ],
    [("Decir «estaba triste» sin nombrar ninguna pista.", "No se ve de dónde sale la idea.", "Agrega la pista: «Habló bajito y miró al suelo, por eso parecía triste»."), ("Fijarse solo en lo que dice el personaje.", "La voz, el cuerpo y el espacio también cuentan la historia.", "Observa cómo lo dice y qué hace mientras lo dice.")],
    [
        E("Un personaje habla bajito y mira al suelo. ¿«Mira al suelo» es una pista de voz o de cuerpo?", "De cuerpo", "La mirada es parte del cuerpo."),
        E("Dos personajes que estaban cerca ahora están en esquinas opuestas del escenario. ¿Qué cambió: el espacio o el tono?", "El espacio", "Cambió dónde están en el escenario."),
        E("¿Qué es el volumen de la voz?", "Qué tan fuerte o bajito suena", "Es la intensidad con que se habla."),
    ],
    [
        E("Una actriz habla fuerte y claro para que la escuchen desde la última fila. ¿Qué hace: proyectar la voz o hablar en secreto?", "Proyectar la voz", "Proyectar es hacerse oír hasta el fondo."),
        E("En una persecución, los actores corren por el escenario y hablan rápido. ¿Para qué sirve ese ritmo: a) mostrar urgencia b) mostrar sueño?", "a", "El ritmo rápido transmite apuro."),
        E("Un personaje se queda callado cinco segundos antes de responder, mirando a su amigo. ¿Qué puede mostrar ese silencio: a) que duda o piensa b) que la obra terminó?", "a", "Un silencio breve en medio de la escena puede mostrar duda."),
    ],
    [
        E("Escena: «Ema abre los brazos, sonríe y grita: ¡Lo logramos!». ¿Qué emoción muestran sus pistas: alegría o pena?", "Alegría", "Sonrisa, brazos abiertos y voz fuerte se parecen a la alegría."),
        E("Escena: «Tomás se sienta en el suelo, lejos de los demás, y habla con voz muy baja». Nombra una pista de espacio.", "Se sienta lejos de los demás", "El lugar donde está es el espacio."),
        E("Elige la frase que explica con pistas: a) «Estaba asustado.» b) «Retrocedió y habló con voz temblorosa, por eso parecía asustado.»", "b", "La b nombra pistas y dice qué muestran."),
    ],
    [
        E("Escena: «Laura habla muy bajito y se tapa la boca con la mano mirando a Pedro». Un espectador dice que tiene vergüenza y otro que cuenta un secreto. Con solo estas pistas, ¿se puede decidir cuál tiene razón?", "No", "Las dos ideas encajan; faltan pistas, como lo que dice."),
        E("Para mostrar que dos amigos se pelearon, ¿qué uso del espacio es mejor: a) se sientan juntos riendo b) cada uno se va a un extremo del escenario y no se miran?", "b", "La distancia y la mirada esquiva muestran el enojo."),
    ],
    [
        E("Don Raúl entra con pasos pesados, la cabeza baja, habla despacio y con tono apagado. ¿Cuántas de esas pistas son del cuerpo y no de la voz?", "Dos", "Los pasos pesados y la cabeza baja son del cuerpo; hablar despacio y el tono son de la voz."),
        E("Para mostrar sorpresa sin decir esa palabra, ¿qué combinación sirve más: a) voz aguda, ojos muy abiertos y un paso atrás b) voz grave, ojos cerrados y un bostezo?", "a", "La combinación a coincide en voz, cara y movimiento."),
    ],
    [E("Observa: «Sofía entra caminando lento, abraza su mochila y dice bajito: Hoy no quiero jugar. Diego se acerca, se agacha a su lado y dice con voz suave: Si quieres, nos sentamos juntos». ¿Qué pista de Diego muestra que quiere acompañar a Sofía?", "Se acerca, se agacha a su lado y habla con voz suave", "Su cuerpo y su voz van hacia ella con cuidado.")],
    [
        E("¿Una pista sola puede tener más de un significado?", "Sí", "Por eso se juntan varias pistas."),
        E("Para explicar una escena, ¿conviene decir qué pista vi y qué muestra?", "Sí", "Así se apoya la idea en lo observado."),
        E("¿El espacio escénico es el lugar donde se mueven los personajes?", "Sí", "Incluye cerca, lejos, arriba o abajo."),
    ],
    ("Observa y explica una escena. Lee esta escena en voz alta o pide que te la lean: «Ignacio entra al escenario saltando y dice fuerte: ¡Mañana es el campeonato! Se detiene al ver a Rosa, que está sentada en una esquina con un yeso en el brazo. Ignacio baja la voz, camina lento hasta ella y se sienta a su lado sin hablar». Escribe qué crees que siente Ignacio al principio y al final, y da una pista de voz, de cuerpo o de espacio para cada momento.",
     "Al principio Ignacio parece feliz y entusiasmado: entra saltando y habla fuerte. Al final parece preocupado y solidario: baja la voz, camina lento y se sienta junto a Rosa sin hablar.",
     ["dice qué siente en cada momento", "da una pista para cada momento", "explica con «porque» o «por eso»"], ["respuesta escrita u oral con pistas"], ["resumir sin dar pistas", "inventar datos que la escena no dice"],
     "Si solo resumiste, pregúntate: ¿cómo hablaba Ignacio antes y después? ¿Qué hizo con el cuerpo?"),
    "Pide a alguien de tu casa que diga «ya llegué» de tres maneras y explica qué sientes en cada una.",
    "Cambia la voz y el espacio de la escena de Ignacio para que termine alegre y explica qué cambiaste.",
)

# ================================================================ OA 24 · clase 3
reg(
    OA24, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: seis papelitos para ordenar acciones.",
    "Aprenderé a reconstruir una escena: decir quiénes son los personajes, cuál es el conflicto, qué acciones ocurren en orden y cómo termina. Sirve para recordar una obra y contarla sin perder lo importante.",
    ["Sé reconocer personajes y sus acciones.", "Sé ordenar hechos con primero, luego y al final."],
    [
        "Una escena es una parte de una obra donde los personajes hacen y dicen cosas. Lo que hacen son las acciones; lo que dicen es el diálogo. El conflicto es el problema que los personajes quieren resolver y que mueve la historia. Una escena suele tener tres momentos: el inicio, donde conocemos a los personajes y lo que quieren; el nudo, donde aparece la dificultad; y el desenlace, donde el conflicto se resuelve o queda abierto.",
        "Para reconstruir una escena, primero ubicamos a los personajes y lo que desea cada uno. Luego buscamos el conflicto con la pregunta: ¿qué se lo impide? Después ordenamos las acciones importantes con palabras como primero, luego, entonces y al final. Muchas acciones son causa de otras: «como no alcanzaba el agua, repartieron el balde».",
        "Al contar una escena no repetimos cada palabra del diálogo. Resumimos quiénes eran, qué problema tenían, qué hicieron y cómo terminó. Un buen resumen deja ver la causa de cada cambio.",
    ],
    [("escena", "parte de una obra donde pasa algo"), ("conflicto", "problema que los personajes deben resolver"), ("nudo", "momento en que la dificultad crece"), ("desenlace", "cómo termina el conflicto"), ("causa", "lo que hace que otra cosa ocurra")],
    [
        ("Encontrar el conflicto", "Escena «El huerto»: Rita y Beto quieren regar el huerto, pero solo queda un balde con poca agua. Rita quiere regar los tomates y Beto, las lechugas. Discuten. Beto propone repartir el agua a la mitad. Riegan las dos hileras. ¿Cuál es el conflicto?", ["Busco qué quiere cada personaje.", "Ambos quieren usar la poca agua en plantas distintas.", "Ese problema es el conflicto."], "Hay poca agua y cada uno quiere usarla en sus plantas."),
        ("Explicar la causa", "En «El huerto», ¿por qué Beto propone repartir el agua?", ["Veo qué ocurría antes: solo quedaba un balde y ambos discutían.", "Repartir permite que las dos hileras reciban agua.", "Eso es la causa de la propuesta."], "Porque había poca agua y los dos la necesitaban; repartirla resolvía la discusión."),
    ],
    [("Contar la escena repitiendo cada palabra del diálogo.", "Se pierde lo importante.", "Resume: personajes, conflicto, acciones en orden y final."), ("Decir que el conflicto es un lugar o un objeto.", "El conflicto es un problema, no una cosa.", "Pregunta: ¿qué problema deben resolver y qué se los impide?")],
    [
        E("En «El huerto», ¿quiénes son los personajes?", "Rita y Beto", "Son quienes actúan y hablan."),
        E("¿Cuál es el desenlace de «El huerto»: riegan las dos hileras o dejan el huerto sin agua?", "Riegan las dos hileras", "Así termina la escena."),
        E("La discusión de Rita y Beto, ¿pertenece al inicio o al nudo?", "Al nudo", "Es cuando la dificultad crece."),
    ],
    [
        E("¿Qué es el conflicto de una escena?", "El problema que los personajes deben resolver", "Mueve la historia."),
        E("¿Qué parte de la escena presenta a los personajes y lo que quieren: el inicio o el desenlace?", "El inicio", "Allí conocemos la situación de partida."),
        E("«Como no alcanzaba el agua, repartieron el balde». ¿Qué parte de la oración es la causa: «no alcanzaba el agua» o «repartieron el balde»?", "No alcanzaba el agua", "Es lo que provoca la acción."),
    ],
    [
        E("Ordena las acciones de «El huerto»: a) riegan las hileras, b) discuten, c) Beto propone repartir. Escribe las letras.", "b, c, a", "Primero discuten, luego proponen un acuerdo y al final riegan."),
        E("Escena «El paraguas»: Inés y Oli esperan el bus bajo la lluvia con un solo paraguas. Cada una quiere ir tapada. Inés lo sostiene en el centro para las dos y se acercan. ¿Cuál es el desenlace?", "Comparten el paraguas en el centro", "Así se resuelve su problema."),
        E("En «El paraguas», ¿qué es la causa de que se acerquen: a) llueve y hay un solo paraguas b) llega el bus?", "a", "La lluvia y un solo paraguas las obligan a acercarse."),
    ],
    [
        E("Resumen 1: «Rita y Beto hablaron mucho.» Resumen 2: «Rita y Beto discutieron porque había poca agua, pero acordaron repartirla y regaron todo.» ¿Cuál reconstruye mejor la escena?", "El resumen 2", "Incluye conflicto, acción y final."),
        E("En una escena, dos amigos quieren leer el mismo libro. Uno lo toma y el otro se enoja. Al final deciden leerlo juntos. ¿El conflicto se resolvió o quedó abierto?", "Se resolvió", "Hallaron una solución que sirve a ambos."),
    ],
    [
        E("Escena: «Camilo no encuentra su gorro y se lo pregunta a su hermana. Ella dice que no lo ha visto. Camilo mira bajo la cama y no está. La hermana ve el gorro sobre la repisa. Camilo ríe y se lo pone». Ordena: a) mira bajo la cama, b) la hermana lo ve en la repisa, c) pregunta a su hermana. Escribe las letras.", "c, a, b", "Primero pregunta, luego busca y al final aparece."),
        E("En esa escena de Camilo, ¿qué personaje resuelve el conflicto: Camilo o su hermana?", "Su hermana", "Ella ve el gorro en la repisa."),
    ],
    [E("Escena «La bicicleta»: Dani quiere usar la bicicleta de su hermano mayor, pero este la necesita para ir a un entrenamiento. Dani se enoja. Su hermano le promete que, cuando vuelva, saldrán a pasear juntos. Dani acepta. ¿Cuál es el conflicto?", "Ambos quieren usar la bicicleta al mismo tiempo", "La necesidad de los dos choca.")],
    [
        E("¿Qué pregunta ayuda a encontrar el conflicto: «¿Qué se lo impide al personaje?» o «¿Cuántas sillas hay?»?", "¿Qué se lo impide al personaje?", "Apunta al problema."),
        E("Al contar una escena, ¿conviene repetir cada palabra o resumir?", "Resumir", "Así queda lo importante."),
        E("¿El desenlace puede dejar el problema abierto?", "Sí", "A veces la escena termina sin resolverlo."),
    ],
    ("Reconstruye esta escena: «La pelota en el techo: Valentina y Joaquín juegan en el patio. La pelota cae sobre el techo bajo. Valentina quiere subir a buscarla, pero Joaquín dice que es peligroso. Deciden pedir ayuda a una persona adulta de la casa, que la baja con cuidado. Los dos se ríen». Escribe o cuenta: quiénes son los personajes, el conflicto, las acciones en orden y el desenlace.",
     "Personajes: Valentina y Joaquín. Conflicto: la pelota cayó al techo y no están de acuerdo en cómo sacarla. Acciones: la pelota cae; Valentina quiere subir; Joaquín dice que es peligroso; piden ayuda a una persona adulta. Desenlace: la persona adulta la baja y se ríen.",
     ["nombra a los personajes", "explica el conflicto", "ordena las acciones", "dice el desenlace"], ["resumen escrito u oral"], ["repetir todo el diálogo", "olvidar el desenlace"],
     "Si falta algo, revisa: ¿quién?, ¿qué problema?, ¿qué pasó primero, luego y al final?"),
    "Cuenta a una persona de tu casa una escena de una historia que conozcas, diciendo conflicto y desenlace.",
    "Cambia el desenlace de «La pelota en el techo» para que el conflicto quede abierto y explica cómo cambia la escena.",
)

# ================================================================ OA 24 · clase 4
reg(
    OA24, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer los diálogos en dos voces.",
    "Aprenderé a mirar una escena desde otro rol: el de cada personaje, el del público y el de quien dirige. Sirve para entender por qué actúan distinto y para crear escenas más ricas.",
    ["Sé reconocer personajes, conflicto y acciones.", "Sé usar pistas de voz, cuerpo y espacio."],
    [
        "Una misma escena puede mirarse desde distintos roles. Cada personaje tiene su punto de vista: lo que ve, lo que desea y lo que siente. El público ve a todos y sabe más que cada personaje. Quien dirige una obra, la directora o el director, decide cómo se dicen las frases, dónde se paran los actores y qué se muestra primero.",
        "Cambiar de rol sirve para entender el conflicto. Un personaje puede sentirse molesto por algo que el otro hizo sin mala intención. Para ponernos en su lugar preguntamos: ¿qué quería?, ¿qué sabía en ese momento?, ¿qué sintió? La respuesta debe apoyarse en lo que dice la escena, no en inventos.",
        "También podemos contar la escena otra vez desde otro personaje. Cambia el relato, pero no los hechos. Por ejemplo, el que se rió dirá que era una broma y el que se fue dirá que se sintió mal. Los hechos son los mismos; las razones y las emociones cambian según quién cuenta.",
    ],
    [("punto de vista", "manera de ver una situación según quién la mira"), ("rol", "papel que cumple alguien, como personaje, público o directora"), ("directora o director", "persona que decide cómo se presenta la obra"), ("hecho", "lo que de verdad ocurre en la escena"), ("empatía", "ponerse en el lugar de otra persona")],
    [
        ("Mirar desde un personaje", "Escena «El gorro»: Camila estrena un gorro rojo. Nico se ríe y dice: «Pareces un tomate». Camila baja la cabeza y se va callada. Más tarde Nico le dice: «Perdón, fue una broma, pero no me di cuenta de que te dolió». ¿Qué sintió Camila cuando Nico se rió?", ["Veo qué hizo Camila: bajó la cabeza y se fue callada.", "Esas pistas muestran que no le dio risa.", "Se sintió herida o avergonzada."], "Se sintió herida o avergonzada."),
        ("Contar desde otro rol", "En «El gorro», ¿qué diría Nico sobre sus intenciones al reírse?", ["Busco lo que Nico dice después.", "Dice que fue una broma.", "Su intención era bromear, aunque no se dio cuenta de que dolía."], "Que quería hacer una broma, sin querer lastimar."),
    ],
    [("Cambiar los hechos al contar desde otro personaje.", "Se cree que cambiar de punto de vista permite inventar lo que pasó.", "Los hechos son los mismos; cambian las razones y las emociones."), ("Decir que un personaje «es malo» sin mirar qué sabía o quería.", "Se juzga sin pensar en su punto de vista.", "Pregunta qué quería y qué sabía en ese momento, con base en la escena.")],
    [
        E("En «El gorro», ¿quién estrena el gorro rojo?", "Camila", "Lo dice la primera línea de la escena."),
        E("¿Quién se disculpa al final de «El gorro»?", "Nico", "Dice «Perdón» a Camila."),
        E("¿Qué rol decide cómo se dicen las frases y dónde se paran los actores: la directora o el público?", "La directora", "Dirigir es decidir cómo se presenta la obra."),
    ],
    [
        E("¿Qué es el punto de vista de un personaje?", "La manera en que ve y siente la situación", "Cada personaje la mira desde lo que sabe y desea."),
        E("En una escena, ¿cambian los hechos si la cuenta otro personaje?", "No", "Cambian las razones y las emociones, no lo ocurrido."),
        E("¿Quién sabe más de lo que pasa en la escena: cada personaje o el público que los ve a todos?", "El público", "Ve las acciones de todos los personajes."),
    ],
    [
        E("Escena: Lola cree que su amigo Bruno no vino a su cumpleaños porque no quiso, pero Bruno estaba enfermo y no pudo avisarle. ¿Qué sabe el público que Lola no sabe?", "Que Bruno estaba enfermo", "Es un dato que Lola no tiene."),
        E("En «El gorro», ¿cuál es un hecho: a) «Camila se fue callada» b) «Nico es un mal amigo»?", "a", "La a es lo que ocurre; la b es una opinión."),
        E("Si fueras la directora de «El gorro», ¿cómo pedirías que Nico diga «Perdón»: a) riéndose b) con voz baja y mirando a Camila?", "b", "La disculpa pide un tono serio y sincero."),
    ],
    [
        E("Un compañero dice: «Nico es malo porque se rió». Otra compañera dice: «Nico se rió sin darse cuenta de que dolía, y después pidió perdón». ¿Quién tiene en cuenta el punto de vista de Nico?", "La compañera", "Considera qué sabía y qué hizo después."),
        E("En «El gorro», ¿qué pista muestra que Nico se arrepintió: a) pidió perdón b) se rió?", "a", "Pedir perdón muestra que reconoce el daño."),
    ],
    [
        E("Escena «El turno»: Ema y Pía esperan para usar el único columpio. Pía lo toma antes y Ema se queda parada, con los brazos cruzados. Pía dice: «No te vi». Ema responde: «Yo estaba primero». ¿Qué quería cada una? Elige: a) las dos querían usar el columpio b) Ema quería irse y Pía quería jugar con ella.", "a", "Ambas querían el único columpio."),
        E("En «El turno», ¿qué pista de cuerpo muestra el enojo de Ema?", "Los brazos cruzados", "Es una pista de postura."),
    ],
    [E("Eres la actriz que hace de Camila. Debes mostrar cómo se siente al escuchar «Pareces un tomate». ¿Qué opción sirve más: a) sonreír y saltar b) bajar la cabeza y quedarse en silencio un momento?", "b", "Esas acciones muestran que le dolió.")],
    [
        E("¿Pueden dos personajes ver una misma escena de manera distinta?", "Sí", "Cada uno tiene su punto de vista."),
        E("Para ponerme en el lugar de otro personaje, ¿debo preguntar qué quería y qué sabía?", "Sí", "Esas dos preguntas ayudan a entender sus razones."),
        E("¿La directora decide cómo se presenta la obra?", "Sí", "Guía las voces, los movimientos y el orden."),
    ],
    ("Cuenta «El turno» desde el punto de vista de Pía: «Pía corre al columpio, se sienta y empieza a balancearse. Ema llega, se queda parada y cruza los brazos. Pía dice: No te vi. Ema responde: Yo estaba primero». Escribe tres o cuatro líneas diciendo qué vio, qué quería y qué sintió Pía, sin cambiar los hechos. Luego agrega una acción con la que Pía podría arreglar el problema.",
     "Pía iba hacia el columpio porque quería jugar y no vio a Ema esperando. Cuando Ema le dijo que estaba primero, se sintió sorprendida y un poco apenada. Podría bajarse y proponer turnos de cinco balanceos.",
     ["los hechos son los mismos de la escena", "explica qué quería y qué sintió Pía", "propone una acción para resolver"], ["texto de tres o cuatro líneas, escrito u oral"], ["cambiar los hechos", "juzgar a un personaje sin explicar su punto de vista"],
     "Si cambiaste hechos, vuelve a leer la escena y deja solo lo que ocurre; cambia las razones y las emociones."),
    "Cuenta una escena de un cuento conocido desde el punto de vista de otro personaje, sin cambiar los hechos.",
    "Escribe qué indicaciones daría la directora de «El gorro» para que Nico diga «Perdón» con sinceridad.",
)

# ================================================================ OA 24 · clase 5
reg(
    OA24, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer la otra voz y dar su opinión.",
    "Aprenderé a crear una respuesta teatral breve: una escena escrita con personajes, conflicto, diálogo y acotaciones, para ensayarla y mejorarla con ayuda de otra persona. Sirve para expresarme con creatividad y disfrutar del teatro desde adentro.",
    ["Sé reconocer conflicto y desenlace en una escena.", "Sé usar pistas de voz, cuerpo y espacio para mostrar emociones."],
    [
        "Un guion es el texto de una obra. Cada línea indica quién habla, escribiendo el nombre del personaje antes de lo que dice. Las acotaciones son indicaciones entre paréntesis que dicen cómo hablar o qué hacer, por ejemplo: (se cruza de brazos). No se leen en voz alta: se actúan. Con diálogo y acotaciones podemos mostrar emociones sin nombrarlas.",
        "Para crear una escena breve sigue tres pasos. Primero elige dos personajes y un conflicto sencillo. Luego escribe cuatro a seis líneas: en las primeras aparece el problema, en las siguientes se complica o se busca una solución, y en la última llega el desenlace. Por último, agrega acotaciones de voz, cuerpo o espacio que se puedan hacer con seguridad en una sala.",
        "Una escena no está terminada al escribirla. Se ensaya en voz alta, se pide una opinión y se mejora. Una buena retroalimentación dice qué funcionó y qué puede cambiar, por ejemplo: «Se entendió el conflicto; prueba hablar más fuerte al final». Un comentario como «estuvo mal» no ayuda a mejorar.",
    ],
    [("guion", "texto que indica qué dicen y hacen los personajes"), ("acotación", "indicación entre paréntesis sobre cómo hablar o moverse"), ("ensayo", "práctica de la escena antes de mostrarla"), ("retroalimentación", "opinión que dice qué resultó bien y qué mejorar"), ("desenlace", "cómo termina el conflicto")],
    [
        ("Leer un guion", "Guion «El último pan». LUZ: (mira la bolsa vacía) ¿Dónde está el pan? TOMÁS: (se toca la barriga, avergonzado) Yo... me lo comí. LUZ: (cruza los brazos) Era para los dos. TOMÁS: (saca una manzana) Te cambio mi manzana por tu perdón. LUZ: (sonríe) Aceptado. La partimos. ¿Cuál es el conflicto?", ["Busco el problema entre los personajes.", "Tomás se comió el pan que era para los dos.", "Luz se enoja por eso."], "Tomás se comió el pan que era para los dos."),
        ("Distinguir acotación y diálogo", "En «El último pan», ¿«(sonríe)» se dice en voz alta o se actúa?", ["Está entre paréntesis.", "Lo entre paréntesis es una acotación.", "Las acotaciones se actúan, no se leen."], "Se actúa: es una acotación."),
    ],
    [("Escribir la acotación como si fuera una frase que el personaje dice.", "Se olvida que va entre paréntesis y que se actúa.", "Escribe entre paréntesis lo que el personaje hace o cómo habla, y después su frase."), ("Dar una opinión como «estuvo mal» o «estuvo bien» sin razones.", "No dice qué cambiar ni qué conservar.", "Di qué funcionó y qué mejorar, con un ejemplo de la escena.")],
    [
        E("En el guion de «El último pan», ¿cómo se llaman las indicaciones entre paréntesis?", "Acotaciones", "Dicen cómo hablar o qué hacer."),
        E("¿Cuántos personajes hablan en «El último pan»?", "Dos", "Son Luz y Tomás."),
        E("¿Quién dice «Era para los dos.»?", "Luz", "El nombre antes de los dos puntos indica quién habla."),
    ],
    [
        E("¿Qué muestra la acotación «(se toca la barriga, avergonzado)» de Tomás?", "Que siente vergüenza por haberse comido el pan", "Combina gesto y emoción."),
        E("¿Cuál es el desenlace de «El último pan»?", "Luz acepta la manzana y la parten", "El conflicto se resuelve con un acuerdo."),
        E("¿Para qué sirve ensayar una escena antes de mostrarla?", "Para probar y mejorar cómo se dice y se mueve", "Ensayar permite corregir antes de presentar."),
    ],
    [
        E("Elige la acotación: a) «(cruza los brazos)» b) «Era para los dos.»", "a", "La a está entre paréntesis y dice qué hace el personaje."),
        E("En «El último pan», ¿cuántas líneas dice Luz?", "Tres", "Habla en la primera, la tercera y la quinta línea."),
        E("Elige la línea escrita como guion: a) «Tomás pidió perdón con voz baja.» b) «TOMÁS: (voz baja) Perdón.»", "b", "La b pone el nombre, la acotación y la frase."),
    ],
    [
        E("Una acotación debe poder hacerse con seguridad en una sala. ¿Cuál sirve: a) «(se sube a la mesa y salta)» b) «(da un paso atrás y levanta las manos)»?", "b", "La b muestra sorpresa sin riesgo."),
        E("Comentario 1: «Estuvo mal.» Comentario 2: «Se entendió el conflicto, pero la voz de Luz era muy baja al final; prueba proyectar.» ¿Cuál ayuda a mejorar?", "El comentario 2", "Dice qué funcionó y qué cambiar."),
    ],
    [
        E("Ordena las líneas para formar una escena con sentido: a) LEO: (baja la voz) Podemos usarlo por turnos. b) ANA: (toma el único lápiz) Voy a dibujar con este lápiz. c) LEO: (alza la voz) ¡Yo también lo necesito! d) ANA: (le pasa el lápiz) Tú primero. Escribe las letras.", "b, c, a, d", "Primero aparece el problema, luego sube la tensión, después la propuesta y el acuerdo."),
        E("Escena: «Vero quiere el asiento junto a la ventana y Pablo también. Vero propone cambiar cada día». ¿Qué final cierra el conflicto: a) Pablo acepta y empiezan hoy con Vero b) Vero se va y nadie vuelve a hablar?", "a", "El acuerdo de turnos resuelve el problema de ambos."),
    ],
    [E("Quieres mostrar que un personaje tiene frío sin decir la palabra «frío». ¿Qué acotación sirve: a) «(se frota los brazos y encoge los hombros)» b) «(se pone a bailar)»?", "a", "Esos gestos se asocian con sentir frío.")],
    [
        E("¿Una acotación va entre paréntesis?", "Sí", "Así se distingue de lo que se dice."),
        E("Una escena breve ¿necesita conflicto?", "Sí", "El conflicto mueve la historia."),
        E("Una buena retroalimentación, ¿dice qué funcionó y qué mejorar?", "Sí", "Así ayuda a corregir."),
    ],
    ("Crea tu respuesta teatral. Escribe una escena de cuatro a seis líneas con dos personajes. Elige uno de estos conflictos: a) dos amigos quieren el mismo sitio junto a la ventana; b) uno de ellos perdió el cuaderno del otro y debe contarlo. Usa el formato «NOMBRE: (acotación) frase», con al menos dos acotaciones de voz, cuerpo o espacio que se puedan hacer con seguridad, y un desenlace. Luego léela en voz alta a una persona de tu casa y pídele una opinión que diga una cosa que funcionó y una que puedes mejorar.",
     "ANA: (se sienta junto a la ventana) Hoy es mi turno. BETO: (se cruza de brazos) Yo llegué primero. ANA: (baja la voz) Podemos cambiar cada día. BETO: (sonríe) Hoy tú, mañana yo. Retroalimentación: se entendió el conflicto; falta más volumen en la última frase.",
     ["tiene dos personajes y un conflicto", "usa el formato de guion", "incluye al menos dos acotaciones seguras", "tiene desenlace", "registra una opinión con algo que funcionó y algo por mejorar"], ["guion escrito y nota con la opinión recibida"], ["escribir acotaciones como si se dijeran", "dejar el conflicto sin desenlace", "pedir una opinión sin razones"],
     "Si no hay conflicto claro, pregúntate: ¿qué quiere cada personaje y qué se lo impide?"),
    "Vuelve a escribir en forma de guion con acotaciones la escena «El paraguas» de la clase 3.",
    "Escribe una segunda versión de tu escena con otro desenlace y compara cuál muestra mejor el conflicto.",
)
