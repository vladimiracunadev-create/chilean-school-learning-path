"""Cuaderno del estudiante, 3.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 06 (territorio, espiritualidad y vida comunitaria) y OA 07 (historia indígena, presente y futuro).

Criterio de autoría: las comunidades, los lugares, las personas y los relatos de práctica son INVENTADOS
(no pertenecen a ningún pueblo real) y se rotulan así. No se afirma nada de lengua, ritos, fechas de
celebraciones, arte, cosmovisión ni roles de un pueblo concreto. Lo tradicional lo enseñan el educador
o la educadora tradicional y la comunidad; ningún ejercicio exige saber una lengua indígena.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA6, OA7 = "LC03 OA 06", "LC03 OA 07"

CONSULT = " Recuerda: lo tradicional lo enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales a ellos antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad."


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement + CONSULT, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback + FEEDBACK_ADD}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def L(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


FICHA_VA = ("Ficha de práctica (inventada): Comunidad: Valle Alto. Territorio: un valle con un río, una vertiente y el cerro Pelado. "
            "Fuente: doña Rosa, vecina de la comunidad. Permiso: doña Rosa autorizó usar esta ficha en la escuela. "
            "Límite: no se cuenta dónde está el sitio de respeto del cerro.")
FICHA_CC = ("Ficha de práctica (inventada): Comunidad: Costa Clara. Territorio: una playa con rocas y mar. "
            "Fuente: don Luis, pescador de la comunidad. Permiso: don Luis autorizó usar esta ficha en la escuela. "
            "Límite: no se cuentan las historias que la comunidad reserva.")

# ============================================================ OA 06 · Territorio, espiritualidad y vida comunitaria
L(
    OA6, 1,
    materials="Lápiz y hojas. Las fichas con los datos están escritas en este cuaderno. Las comunidades, los lugares y las personas son inventados.",
    use="Aprenderé a situar un territorio: decir de qué comunidad es, quién cuenta y qué se puede compartir. Sirve para hablar de un lugar sin inventar ni generalizar.",
    prior=["Sé qué es un espacio importante para una comunidad.", "Sé que una fuente es quien entrega un dato."],
    explain=[
        "El territorio no es solo un dibujo en un mapa. Es el lugar donde una comunidad vive, trabaja, celebra y recuerda. Incluye ríos, cerros, playas, caminos y también las historias y los trabajos que ocurren allí.",
        "Para hablar de un territorio hay que situarlo. Situar es decir de qué pueblo o comunidad es, qué lugar es y quién lo cuenta. Esa persona es la fuente. También hay que saber si autorizó compartir su relato y qué parte no se cuenta.",
        "Una ficha situada tiene cinco partes: comunidad, territorio, fuente, permiso y límite. Lo que dice una ficha vale para esa comunidad, no para todos los pueblos. Si falta el permiso o la fuente, nos detenemos y preguntamos al educador o a la comunidad.",
    ],
    vocab=[("territorio", "lugar donde una comunidad vive, trabaja, celebra y recuerda"), ("situar", "decir de quién es, dónde queda y quién lo cuenta"), ("fuente", "persona o texto que entrega el dato"), ("permiso", "autorización para compartir algo"), ("límite", "lo que no se cuenta o no se muestra")],
    worked=[
        W("Leer una ficha situada", "Lee: «" + FICHA_VA + "» ¿Quién cuenta y qué no se puede decir?", ["Busco Fuente: doña Rosa.", "Busco Límite: no se cuenta dónde está el sitio de respeto.", "Junto las dos ideas."], "Cuenta doña Rosa; no se puede decir dónde está el sitio de respeto del cerro."),
        W("Separar fuente e interpretación", "Con la ficha de Costa Clara: «" + FICHA_CC + "» Un niño dice: «Seguro la playa tiene un tesoro». ¿Qué parte viene de la ficha?", ["La ficha habla de una playa con rocas y mar.", "El tesoro no está escrito.", "Lo del tesoro es idea del niño."], "Viene de la ficha: playa con rocas y mar. El tesoro es idea del niño."),
    ],
    mistakes=[
        M("Pensar que la ficha de una comunidad vale para todos los pueblos.", "Cada comunidad vive su territorio a su manera.", "Escribe siempre de qué comunidad habla la ficha."),
        M("Usar una ficha que no dice quién dio el permiso.", "Sin permiso no sabemos si se puede compartir.", "Detente y pregunta al educador o a la comunidad."),
    ],
    R=[
        ex("Ficha de Valle Alto (inventada): fuente, doña Rosa. ¿Quién es la fuente?", "Doña Rosa", "La ficha escribe su nombre en la parte «Fuente»."),
        ex("La ficha de Valle Alto dice «un valle con un río, una vertiente y el cerro Pelado». ¿Qué parte de la ficha es esa: territorio o permiso?", "Territorio", "Describe el lugar donde vive la comunidad."),
        ex("En la ficha de Valle Alto, ¿qué NO se cuenta? A) dónde está el sitio de respeto del cerro B) que hay un río", "A", "Eso lo dice la parte «Límite»."),
    ],
    C=[
        ex("Verdadero o falso: territorio es solamente el dibujo de un mapa.", "Falso", "El territorio incluye lo que la comunidad vive, trabaja y recuerda."),
        ex("¿Qué es situar un territorio? A) decir de qué comunidad es y quién lo cuenta B) pintarlo de colores", "A", "Situar es dar comunidad, lugar y fuente."),
        ex("Verdadero o falso: si una ficha no dice quién autorizó compartirla, igual se puede usar.", "Falso", "Sin permiso hay que detenerse y preguntar."),
    ],
    A=[
        ex("¿Cuántas partes tiene una ficha situada de este cuaderno? Escribe el número.", "5", "Son comunidad, territorio, fuente, permiso y límite."),
        ex("Una ficha dice: «Comunidad: Costa Clara. Territorio: una playa con rocas y mar. Fuente: don Luis. Permiso: sí.» ¿Qué parte falta?", "El límite", "Faltan las cosas que no se cuentan."),
        ex("Una frase sale de la ficha de Costa Clara y otra es idea tuya. 1) «Hay una playa con rocas.» 2) «Creo que allí hay un barco hundido.» ¿Cuál sale de la ficha?", "1", "La playa con rocas está escrita; el barco no."),
    ],
    Z=[
        ex("Tomás copió la ficha de Valle Alto, pero borró la parte «Permiso». ¿Por qué es un problema?", "No se sabe si la fuente autorizó compartirla", "El permiso dice si se puede usar el relato."),
        ex("Ema dice: «La ficha de Valle Alto tiene un río, entonces todos los pueblos tienen un río en su territorio». ¿Qué error comete?", "Generaliza una ficha a todos los pueblos", "Una ficha habla de una sola comunidad."),
    ],
    D=[
        ex("Hay dos fichas inventadas. Valle Alto: valle, río y cerro. Costa Clara: playa, rocas y mar. Alguien dice: «Aquí hay rocas junto al mar». ¿De cuál ficha viene esa frase?", "Costa Clara", "Solo la ficha de Costa Clara habla de rocas y mar."),
        ex("Una ficha dice «Límite: no se sacan fotos del lugar». ¿Puedes subir una foto de ese lugar a internet? Responde Sí o No.", "No", "El límite lo prohíbe."),
    ],
    context=[ex("En el curso leen la ficha de Valle Alto. Mía quiere decir en voz alta dónde está el sitio de respeto del cerro. ¿Puede hacerlo? Responde Sí o No.", "No", "La ficha dice que eso no se cuenta.")],
    selfcheck=[
        ex("Escribe dos partes de una ficha situada.", "Dos de estas: comunidad, territorio, fuente, permiso, límite", "Las cinco partes se explican en la lección."),
        ex("¿Qué haces si a una ficha le falta el permiso?", "Me detengo y pregunto al educador o a la comunidad", "Sin permiso no se comparte."),
        ex("Verdadero o falso: lo que dice la ficha de una comunidad vale para todos los pueblos.", "Falso", "Solo habla de esa comunidad."),
    ],
    task=T("Lee la ficha de Costa Clara (inventada): «" + FICHA_CC + "» Copia en tu hoja una tabla con cinco filas: comunidad, territorio, fuente, permiso y límite, con lo que dice la ficha. Debajo escribe una frase que empiece con «La fuente dice…» y otra que empiece con «Yo pienso…». Termina con una pregunta que le harías al educador tradicional sobre el territorio de tu zona.",
           "Comunidad: Costa Clara. Territorio: playa con rocas y mar. Fuente: don Luis. Permiso: sí. Límite: no se cuentan historias reservadas. La fuente dice que hay rocas y mar. Yo pienso que debe ser lindo en verano. Pregunta: ¿qué lugares de nuestra zona cuida la comunidad?",
           ["copia las cinco partes sin cambiar datos", "separa lo que dice la fuente de lo que piensa", "formula una pregunta respetuosa"], ["tabla de cinco filas", "dos frases", "pregunta escrita"], ["mezclar la opinión con lo que dice la ficha", "inventar un dato que la ficha no tiene"],
           "Pedir que muestre en qué fila está cada dato; valorar que separe la fuente de su opinión."),
    reinforce="Subraya en la ficha de Valle Alto la fuente con un color y el límite con otro.",
    extend="Escribe dos diferencias entre el territorio de Valle Alto y el de Costa Clara, usando solo las fichas.",
)

L(
    OA6, 2,
    materials="Lápiz y hojas. El testimonio está escrito aquí y es inventado.",
    use="Aprenderé a relacionar un territorio con la vida espiritual de una comunidad escuchando lo que la comunidad cuenta. Sirve para respetar lo que es de ella y no adivinar.",
    prior=["Sé situar un territorio con una ficha.", "Sé que hay cosas que no se cuentan."],
    explain=[
        "Para muchas comunidades, algunos lugares del territorio son importantes también por su vida espiritual. La espiritualidad es la forma en que una comunidad entiende y cuida lo que considera sagrado o muy respetable.",
        "Solo la comunidad puede decir qué lugar es importante y por qué. Nosotros no lo adivinamos mirando un cerro o una foto. Un lugar puede parecer común y ser muy importante, o parecer misterioso y no serlo.",
        "Lo que la comunidad cuenta se escucha con respeto. Algunas partes se comparten con todos y otras se resguardan. Lo que no se cuenta no se inventa ni se busca por otro lado. Si queremos saber más, preguntamos al educador tradicional.",
    ],
    vocab=[("espiritualidad", "forma de entender y cuidar lo que una comunidad considera sagrado"), ("sagrado", "muy importante y digno de respeto"), ("resguardar", "cuidar algo y no mostrarlo a todos"), ("testimonio", "relato de una persona sobre lo que vive o sabe"), ("respeto", "tratar con cuidado lo que es importante para otros")],
    worked=[
        W("Qué dice el testimonio", "Testimonio inventado de doña Rosa, de Valle Alto: «El cerro Pelado es un lugar de respeto. Se sube en silencio y se pide permiso. Lo demás lo contamos solo en la comunidad.» ¿Qué sabemos y qué no?", ["Sabemos que es un lugar de respeto.", "Sabemos que se sube en silencio y con permiso.", "Lo demás no se cuenta, así que no lo sabemos."], "Sabemos que es lugar de respeto, silencio y permiso; el resto no se sabe."),
        W("No adivinar", "Un niño dice: «Si el cerro es de respeto, seguro hay allí una ceremonia con fuego». ¿Se puede afirmar eso?", ["Reviso el testimonio: no habla de fuego.", "La ceremonia no está escrita.", "No se puede afirmar."], "No, porque el testimonio no lo dice."),
    ],
    mistakes=[
        M("Decir cómo es una ceremonia sin que la comunidad lo haya contado.", "Es adivinar, y puede ser falso o irrespetuoso.", "Escribe solo lo que dice la fuente."),
        M("Buscar en internet lo que la comunidad decidió no contar.", "Lo reservado no se publica ni se busca.", "Pregunta al educador tradicional qué se puede conocer."),
    ],
    R=[
        ex("Según el testimonio de doña Rosa, ¿cómo se sube al cerro Pelado: en silencio o gritando?", "En silencio", "El testimonio dice que se sube en silencio."),
        ex("¿Quién puede decir por qué un lugar es importante para la vida espiritual de la comunidad: la comunidad o un desconocido que mira una foto?", "La comunidad", "Solo quienes viven allí conocen su significado."),
        ex("Si la comunidad dice «lo demás lo contamos solo entre nosotros», ¿se puede inventar lo que falta? Responde Sí o No.", "No", "Lo reservado no se inventa."),
    ],
    C=[
        ex("¿Qué es la espiritualidad? A) La forma en que una comunidad entiende y cuida lo sagrado B) Un tipo de comida", "A", "Es su manera de entender y cuidar lo importante y sagrado."),
        ex("Verdadero o falso: un lugar es sagrado cuando se ve misterioso en una foto.", "Falso", "Lo dice la comunidad, no la apariencia."),
        ex("Verdadero o falso: en el testimonio de doña Rosa se pide permiso para subir al cerro.", "Verdadero", "El testimonio lo dice."),
    ],
    A=[
        ex("Testimonio inventado: «La quebrada de Piedra Blanca es lugar de reunión. A la orilla se conversa en voz baja.» Escribe un dato que SÍ dice el testimonio.", "Es lugar de reunión o se conversa en voz baja", "Son las dos cosas escritas en el testimonio."),
        ex("Une la frase con su origen. 1) «Se sube en silencio» 2) «Debe haber un tesoro» a) lo dice el testimonio b) lo imagino yo", "1-a, 2-b", "La primera está escrita; la segunda no."),
        ex("Una niña escribe: «Para la comunidad de Valle Alto el cerro Pelado es lugar de respeto». ¿Atribuyó la fuente? Responde Sí o No.", "No", "No escribió que lo cuenta doña Rosa."),
    ],
    Z=[
        ex("Pedro dice: «El cerro de mi ciudad parece misterioso, así que es sagrado para algún pueblo». ¿Qué error comete?", "Adivina sin que una fuente lo diga", "Para afirmarlo, la comunidad debe contarlo."),
        ex("Ana quiere agregar a su trabajo cómo es la ceremonia del cerro Pelado, que doña Rosa no contó. ¿Qué debe hacer? A) Inventarla B) Dejar escrito que esa parte no se cuenta", "B", "Lo reservado se respeta y no se inventa."),
    ],
    D=[
        ex("Dos niños leen el mismo testimonio. Uno escribe «es lugar de respeto y se sube en silencio». Otro escribe «allí viven espíritus». ¿Cuál se queda en lo que dice la fuente?", "El primero", "El segundo agrega algo que el testimonio no dice."),
        ex("Un lugar no parece especial y la comunidad dice que es muy importante. ¿Quién tiene razón sobre su importancia: la comunidad o quien lo mira de lejos?", "La comunidad", "Ella conoce su significado."),
    ],
    context=[ex("Un visitante llega a Valle Alto y quiere subir al cerro Pelado sin avisar. Según el testimonio, ¿qué debe hacer antes?", "Pedir permiso", "El testimonio dice que se pide permiso para subir.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es la espiritualidad.", "La forma en que una comunidad entiende y cuida lo sagrado", "Es la idea central de la explicación."),
        ex("¿Qué haces con lo que la comunidad no cuenta?", "Lo respeto y no lo invento", "Lo reservado no se comparte."),
        ex("Verdadero o falso: puedo saber por mi cuenta si un lugar es sagrado para una comunidad.", "Falso", "Lo dice la comunidad."),
    ],
    task=T("Lee este testimonio inventado de doña Rosa: «La vertiente de Valle Alto da agua a todas las familias. Allí se agradece el agua en silencio. Hay cosas que solo conversamos entre nosotros.» Escribe en una hoja dos columnas: «Lo que sí sé» y «Lo que no sé». Después escribe una frase que atribuya la fuente, por ejemplo con «Doña Rosa cuenta que…». No dibujes ni inventes ninguna ceremonia.",
           "Lo que sí sé: la vertiente da agua a las familias y allí se agradece en silencio. Lo que no sé: lo que la comunidad conversa solo entre ella. Doña Rosa cuenta que la vertiente da agua a todas las familias.",
           ["separa lo que dice el testimonio de lo que no se sabe", "atribuye la fuente", "no inventa ritos"], ["dos columnas", "frase con la fuente"], ["inventar una ceremonia", "llenar la columna «no sé» con suposiciones"],
           "Preguntar qué parte del testimonio respalda cada dato; valorar que deje en blanco lo reservado."),
    reinforce="Marca en el testimonio del cerro Pelado las tres cosas que sí se dicen.",
    extend="Escribe dos preguntas respetuosas para el educador tradicional sobre un lugar de tu zona, sin pedirle lo que la comunidad reserva.",
)

L(
    OA6, 3,
    materials="Lápiz y hojas. Los datos del año de Valle Alto están escritos aquí y son inventados.",
    use="Aprenderé a relacionar las festividades con las actividades productivas de una comunidad, usando un calendario inventado. Sirve para ver que el trabajo, la naturaleza y la fiesta se conectan.",
    prior=["Sé que cada comunidad vive su territorio a su manera.", "Sé que hay cosas que solo cuenta la comunidad."],
    explain=[
        "Una actividad productiva es un trabajo que da algo a la comunidad, como alimento o materiales. Sembrar, cosechar, pescar, recoger algas o tejer son actividades productivas. Dependen de lo que hay en el territorio y de la época del año.",
        "Una festividad es un día o un tiempo en que la comunidad se junta a celebrar o agradecer. Muchas veces la festividad se conecta con una actividad productiva, por ejemplo cuando termina una cosecha. Pero cada comunidad decide cuándo y cómo celebra.",
        "Por eso no podemos decir fechas ni modos de celebrar de un pueblo sin que lo cuente la comunidad. En esta clase usamos el calendario inventado de Valle Alto solo para practicar cómo se relacionan trabajo, territorio y fiesta.",
    ],
    vocab=[("actividad productiva", "trabajo que entrega alimentos o materiales a la comunidad"), ("festividad", "tiempo en que la comunidad se junta a celebrar o agradecer"), ("cosecha", "recoger lo que se sembró"), ("época", "parte del año"), ("ciclo", "serie de pasos que se repite")],
    worked=[
        W("Ordenar el ciclo de Valle Alto (inventado)", "Calendario inventado: primero se prepara la tierra, después se siembra, luego se cuida la huerta, después se cosecha y al terminar se hace la fiesta de agradecimiento. ¿Qué viene justo antes de la fiesta?", ["Leo el orden: preparar, sembrar, cuidar, cosechar, fiesta.", "Busco la palabra antes de «fiesta».", "Es cosechar."], "Cosechar"),
        W("Relacionar territorio y fiesta", "La huerta de Valle Alto recibe agua de la vertiente. Si la vertiente se seca, ¿qué actividad se ve afectada y cómo puede afectar la fiesta?", ["El agua se usa para regar la huerta.", "Sin agua hay menos cosecha.", "Con menos cosecha hay menos que agradecer o compartir en la fiesta."], "Se afecta el riego y la cosecha, y con ella la fiesta."),
    ],
    mistakes=[
        M("Decir que un pueblo real celebra en cierta fecha sin tener una fuente.", "Cada comunidad decide cuándo y cómo celebra.", "Usa solo fechas que cuente la comunidad."),
        M("Creer que la fiesta no tiene relación con el trabajo y el territorio.", "Muchas veces celebran lo que el territorio y el trabajo entregan.", "Pregunta qué actividad se conecta con la fiesta."),
    ],
    R=[
        ex("En el calendario inventado de Valle Alto, ¿qué se hace primero: sembrar o cosechar?", "Sembrar", "Primero se siembra y después se cosecha."),
        ex("Sembrar y cosechar son actividades productivas. ¿Dan alimento o dan juguetes?", "Alimento", "La huerta entrega alimentos."),
        ex("¿Qué es una festividad? A) tiempo en que la comunidad se junta a celebrar B) un tipo de semilla", "A", "Es un tiempo de celebración o agradecimiento."),
    ],
    C=[
        ex("Verdadero o falso: todas las comunidades celebran en la misma fecha.", "Falso", "Cada comunidad decide cuándo celebra."),
        ex("En Valle Alto (inventado), ¿qué actividad se conecta con la fiesta de agradecimiento? A) la cosecha B) el viaje en bus", "A", "La fiesta ocurre al terminar la cosecha."),
        ex("¿Qué depende de la vertiente en Valle Alto: el riego de la huerta o la escuela?", "El riego de la huerta", "La huerta recibe agua de la vertiente."),
    ],
    A=[
        ex("Ordena los pasos de Valle Alto (inventado): a) cosechar b) preparar la tierra c) sembrar d) fiesta e) cuidar la huerta. Escribe las letras en orden.", "b, c, e, a, d", "Primero se prepara, luego se siembra, se cuida, se cosecha y se celebra."),
        ex("Una comunidad inventada recoge algas en verano y hace una fiesta de agradecimiento después. ¿Qué actividad productiva se conecta con su fiesta?", "Recoger algas", "Es el trabajo que la fiesta agradece."),
        ex("Cuenta: en Valle Alto hay 5 pasos en el ciclo (preparar, sembrar, cuidar, cosechar, fiesta). ¿Cuántos son actividades de trabajo, sin contar la fiesta?", "4", "Preparar, sembrar, cuidar y cosechar son trabajo; la fiesta no."),
    ],
    Z=[
        ex("Lía dice: «Los pueblos originarios celebran siempre el mismo día». ¿Qué error comete?", "Generaliza sin una fuente", "Cada comunidad define sus fechas."),
        ex("Pedro cuenta que en Valle Alto (inventado) la fiesta es antes de sembrar. El calendario dice que es al terminar la cosecha. ¿Quién se equivoca?", "Pedro", "El calendario pone la fiesta después de cosechar."),
    ],
    D=[
        ex("En Costa Clara (inventada) la fiesta se hace al terminar la temporada de recoger algas. Si ese año la playa tuvo pocas algas, ¿qué puede pasar con lo que la comunidad comparte en la fiesta?", "Habrá menos algas para compartir", "La producción afecta lo que se tiene para celebrar."),
        ex("Dos niños preguntan: «¿Cuándo celebra un pueblo originario su fiesta?» y «¿Quién nos puede contar cuándo celebra nuestra comunidad?». ¿Cuál pregunta se puede responder con seguridad en esta clase?", "La segunda", "La fecha real la cuenta el educador o la comunidad."),
    ],
    context=[ex("Una familia de Valle Alto (inventada) cosechó papas y ahora prepara la fiesta de agradecimiento. ¿Qué actividad productiva ocurrió antes de la fiesta?", "La cosecha", "La fiesta viene después de cosechar.")],
    selfcheck=[
        ex("Escribe qué es una actividad productiva.", "Un trabajo que entrega alimentos o materiales a la comunidad", "Es la definición de la lección."),
        ex("Verdadero o falso: puedo decir la fecha de una fiesta de un pueblo si la vi en un video.", "Falso", "La fecha la cuenta la comunidad."),
        ex("¿Qué dos cosas relaciona esta clase? A) trabajo y fiesta B) dinero y juegos", "A", "Se relacionan las actividades productivas con las festividades."),
    ],
    task=T("Con el calendario inventado de Valle Alto (preparar la tierra, sembrar, cuidar la huerta, cosechar, fiesta de agradecimiento), dibuja cinco recuadros en orden y escribe una frase bajo cada uno. Después responde: ¿qué cosa del territorio hace posible la cosecha? Añade una pregunta para el educador tradicional sobre cómo celebra tu comunidad, sin pedirle nada que sea reservado.",
           "1 Preparar la tierra. 2 Sembrar. 3 Cuidar la huerta con agua de la vertiente. 4 Cosechar. 5 Fiesta de agradecimiento. Lo que hace posible la cosecha: el agua de la vertiente y la tierra. Pregunta: ¿cómo celebra nuestra comunidad cuando termina un trabajo importante?",
           ["ordena los cinco pasos", "nombra un elemento del territorio", "plantea una pregunta respetuosa"], ["cinco recuadros", "frases", "pregunta"], ["poner la fiesta antes de la cosecha", "inventar una fecha real"],
           "Revisar el orden de los pasos; preguntar qué parte del territorio entrega lo necesario."),
    reinforce="Escribe los pasos del ciclo de Valle Alto en una cinta de papel y ordénala.",
    extend="Imagina qué cambiaría en el ciclo si la vertiente se secara. Escríbelo en dos frases.",
)

L(
    OA6, 4,
    materials="Lápiz y hojas. Las notas de práctica están escritas en este cuaderno y son inventadas.",
    use="Aprenderé a comunicar las conexiones entre territorio, espiritualidad, fiesta y trabajo, diciendo también hasta dónde llega lo que sé. Sirve para presentar sin inventar.",
    prior=["Sé situar un territorio con una ficha.", "Sé relacionar actividades productivas con festividades."],
    explain=[
        "Comunicar es contar lo aprendido a otras personas. Para hacerlo bien con un tema cultural, decimos de qué comunidad habla, quién es la fuente y cuáles conexiones encontramos entre territorio, vida espiritual, festividades y trabajo.",
        "Una conexión es una relación que se puede explicar con datos. Por ejemplo: «La vertiente da agua, el agua riega la huerta, la huerta da cosecha y con la cosecha se hace la fiesta de agradecimiento». Cada paso está en los datos de Valle Alto que ya conocemos.",
        "También decimos los límites: qué no sé, qué no se cuenta y qué no corresponde a otros pueblos. Terminamos agradeciendo a la fuente y diciendo que lo tradicional lo enseña el educador o la comunidad. Así evitamos inventar y generalizar.",
    ],
    vocab=[("comunicar", "contar lo aprendido a otras personas"), ("conexión", "relación entre dos cosas que se explica con datos"), ("límite", "lo que no se sabe, no se cuenta o no corresponde decir"), ("agradecer", "reconocer lo que otra persona nos dio"), ("atribuir", "decir de quién viene un dato")],
    worked=[
        W("Armar una cadena de conexiones", "Con la ficha y el calendario inventado de Valle Alto (clases anteriores): la vertiente da agua, la huerta se riega, hay cosecha y se hace una fiesta de agradecimiento. Escribe una frase que conecte los cuatro datos.", ["Pongo los datos en orden.", "Uso la palabra «porque» o «luego».", "Cuido que cada dato esté en la ficha o el calendario."], "La vertiente da agua, con el agua se riega la huerta, luego hay cosecha y después se hace la fiesta de agradecimiento."),
        W("Escribir el límite", "Después de contar la cadena, ¿cómo dices que no sabes cómo se celebra la fiesta?", ["Reconozco que la ficha no lo cuenta.", "Lo escribo como límite.", "Agrego que lo enseña el educador o la comunidad."], "La ficha no cuenta cómo se celebra; eso lo enseña el educador tradicional o la comunidad."),
    ],
    mistakes=[
        M("Terminar la presentación sin decir qué no sabes.", "Parece que lo sabemos todo y podemos generalizar.", "Agrega una frase con los límites."),
        M("Contar la cadena sin decir de qué comunidad habla.", "El oyente cree que vale para todos los pueblos.", "Empieza diciendo la comunidad y la fuente."),
    ],
    R=[
        ex("¿Qué debes decir primero al presentar: de qué comunidad habla el dato o el color de tu lápiz?", "De qué comunidad habla el dato", "Primero se sitúa la información."),
        ex("En la cadena de Valle Alto, ¿qué viene justo después de «la huerta se riega»? A) hay cosecha B) llega el invierno", "A", "Con el riego la huerta da cosecha."),
        ex("Si no sabes algo, ¿lo escribes como límite o lo inventas?", "Lo escribo como límite", "No se inventa lo que no se sabe."),
    ],
    C=[
        ex("¿Qué es una conexión? A) una relación explicada con datos B) una suposición sin fuente", "A", "Se explica con datos de la ficha."),
        ex("Verdadero o falso: al comunicar un tema cultural conviene decir qué no sabemos.", "Verdadero", "Los límites evitan inventar."),
        ex("¿Para qué agradecemos a la fuente? A) para reconocer lo que nos entregó B) para ganar puntos", "A", "Agradecer reconoce la ayuda recibida."),
    ],
    A=[
        ex("Ordena las frases de la cadena de Valle Alto: a) hay cosecha b) la vertiente da agua c) se hace la fiesta de agradecimiento d) se riega la huerta. Escribe las letras en orden.", "b, d, a, c", "Primero el agua, luego el riego, la cosecha y la fiesta."),
        ex("Completa con la fuente. En el testimonio de la clase 2, doña Rosa cuenta: «La vertiente da ___ a todas las familias». Escribe la palabra.", "agua", "El testimonio dice que la vertiente da agua."),
        ex("Completa con un límite: «La ficha no cuenta ___ ». Elige. A) cómo se celebra la fiesta B) que hay un río", "A", "Eso no está en la ficha; que hay un río sí está."),
    ],
    Z=[
        ex("Julia presenta la cadena de Valle Alto y dice al final «así lo hacen todos los pueblos». ¿Qué error comete?", "Generaliza una comunidad a todos los pueblos", "La ficha solo habla de Valle Alto."),
        ex("Tomás presentó sin decir quién contó la ficha. ¿Qué dato le falta?", "La fuente", "Falta decir quién la cuenta."),
    ],
    D=[
        ex("Dos presentaciones: 1) «Valle Alto cosecha y celebra. Lo cuenta doña Rosa. No sé cómo celebran.» 2) «Todos los pueblos cosechan y celebran igual.» ¿Cuál es más respetuosa y precisa?", "La 1", "Atribuye la fuente y reconoce el límite."),
        ex("Una niña quiere agregar un baile que vio en televisión a la presentación de Valle Alto. ¿Puede hacerlo, si la ficha no lo cuenta? Responde Sí o No.", "No", "Sería un dato sin fuente."),
    ],
    context=[ex("Tu curso presentará la ficha de Valle Alto a otros cursos. ¿Qué frase debe ir al final? A) «Lo tradicional lo enseña el educador o la comunidad» B) «Así es siempre en todos los pueblos»", "A", "Reconoce quién enseña lo tradicional.")],
    selfcheck=[
        ex("Escribe dos cosas que debes decir al presentar una ficha de comunidad.", "La comunidad y la fuente, o los límites", "Son las partes de una buena presentación."),
        ex("Verdadero o falso: un buen trabajo inventa lo que falta para que quede completo.", "Falso", "Lo que falta se escribe como límite."),
        ex("¿Qué palabra usas para decir de quién viene un dato? A) atribuir B) copiar", "A", "Atribuir es decir quién lo contó."),
    ],
    task=T("Con la ficha de Valle Alto (inventada): «" + FICHA_VA + "» y el calendario de la cosecha de la clase anterior, prepara un cartel con cuatro partes: 1) comunidad y fuente, 2) una cadena de cuatro conexiones, 3) un límite («no sé…») y 4) un agradecimiento a la fuente. Usa letra clara. No dibujes el sitio de respeto del cerro.",
           "1 Comunidad de Valle Alto (inventada). Fuente: doña Rosa. 2 La vertiente da agua, con el agua se riega la huerta, hay cosecha y se hace la fiesta de agradecimiento. 3 No sé cómo se celebra la fiesta. 4 Gracias, doña Rosa. Lo tradicional lo enseña el educador o la comunidad.",
           ["incluye las cuatro partes", "las conexiones salen de la ficha", "declara un límite"], ["cartel con cuatro partes"], ["no decir la fuente", "dibujar el sitio de respeto", "dar un dato inventado"],
           "Preguntar de dónde sale cada conexión; reconocer que escribió su límite con claridad."),
    reinforce="Une con flechas los cuatro pasos de la cadena de Valle Alto.",
    extend="Escribe dos límites distintos que pondrías al presentar la ficha de Costa Clara.",
)

# ============================================================ OA 07 · Historia indígena, presente y futuro
L(
    OA7, 1,
    materials="Lápiz y hojas. Los textos están escritos aquí. La comunidad y las personas son inventadas.",
    use="Aprenderé a formular una pregunta histórica: una pregunta sobre el pasado que se pueda responder con una fuente. Sirve para investigar sin adivinar.",
    prior=["Sé que una fuente es quien entrega un dato.", "Sé distinguir pasado y presente."],
    explain=[
        "La historia cuenta qué pasó antes y cómo ese pasado se conecta con el presente. Para estudiarla hacemos preguntas. Una buena pregunta histórica se puede responder con una fuente: una persona que recuerda, un objeto o un texto.",
        "Algunas preguntas piden un dato: ¿quién?, ¿cuándo?, ¿dónde?, ¿cómo cambió? Otras piden una opinión, como «¿qué fue lo más lindo?». Las preguntas de opinión no sirven para investigar un hecho.",
        "En la historia de un pueblo originario, la fuente más importante es la propia comunidad. Por eso nuestras preguntas se dirigen a personas mayores, al educador tradicional o a materiales que la comunidad autorice. Hoy el pueblo sigue vivo y su historia continúa.",
    ],
    vocab=[("historia", "lo que pasó antes y sus efectos en el presente"), ("pregunta histórica", "pregunta sobre el pasado que se puede responder con una fuente"), ("testimonio", "relato de una persona sobre lo que vivió o sabe"), ("pasado", "lo que ya ocurrió"), ("presente", "lo que ocurre ahora")],
    worked=[
        W("Elegir una buena pregunta", "Una abuela de la comunidad inventada de Valle Alto puede contar cómo era el camino al río cuando ella era niña. ¿Cuál pregunta es histórica? A) ¿Cómo era el camino al río cuando usted era niña? B) ¿Cuál es el mejor color del río?", ["Busco una pregunta sobre el pasado.", "La pregunta A habla de cuando era niña.", "La B pide una opinión."], "A"),
        W("Convertir una opinión en pregunta histórica", "Cambia «¿Fue bonito el pueblo antes?» por una pregunta que pida un dato.", ["Pienso qué dato puedo pedir.", "Pido que cuente cómo era algo.", "Escribo la pregunta."], "¿Cómo era el pueblo cuando usted era niña?"),
    ],
    mistakes=[
        M("Hacer una pregunta que se responde con sí o no y no cuenta nada.", "No entrega información sobre el pasado.", "Usa «cómo», «quién», «cuándo» o «dónde»."),
        M("Preguntar por algo reservado de la comunidad.", "Hay conocimientos que la comunidad no comparte.", "Pregunta al educador qué se puede preguntar."),
    ],
    R=[
        ex("¿Qué pregunta habla del pasado? A) ¿Cómo era el camino al río hace muchos años? B) ¿Qué comerás hoy?", "A", "La A pregunta por lo que pasó antes."),
        ex("Una pregunta empieza con «¿Quién…?». ¿Pide un dato o una opinión?", "Un dato", "Pide el nombre de una persona."),
        ex("¿Quién es una fuente para la historia de una comunidad: una abuela que recuerda o un dibujo inventado por un desconocido?", "Una abuela que recuerda", "Es quien vivió esa historia."),
    ],
    C=[
        ex("Verdadero o falso: «¿Qué fue lo más lindo?» es una buena pregunta histórica.", "Falso", "Pide una opinión, no un dato del pasado."),
        ex("¿Cuál palabra sirve para empezar una pregunta histórica? A) ¿Cuándo…? B) ¿Te gusta…?", "A", "Cuándo pide una época o un momento."),
        ex("Verdadero o falso: la historia de un pueblo originario termina en el pasado.", "Falso", "Hoy el pueblo sigue vivo y su historia continúa."),
    ],
    A=[
        ex("Clasifica en DATO u OPINIÓN: a) ¿Dónde se juntaba la gente? b) ¿Fue mejor antes? c) ¿Cómo se hacía el trabajo?", "a dato, b opinión, c dato", "Dónde y cómo piden información; «mejor» pide opinión."),
        ex("Escribe una pregunta histórica para una abuela de Valle Alto sobre cómo se trabajaba la huerta cuando era niña. Empieza con «¿Cómo…?».", "¿Cómo se trabajaba la huerta cuando usted era niña?", "Pide un dato del pasado."),
        ex("Una pregunta histórica dice: «¿Cómo era el camino cuando usted era niña?». ¿Cuál es la palabra que pide el dato: cómo o niña?", "Cómo", "La palabra interrogativa pide el dato que se busca."),
    ],
    Z=[
        ex("Mateo pregunta: «¿Los pueblos originarios ya no existen?». ¿Qué error tiene la pregunta?", "Supone que ya no existen, pero existen hoy", "Los pueblos viven hoy."),
        ex("Ema dice que su pregunta «¿Cómo era el pueblo antes?» sirve solo si la responde una fuente. ¿Tiene razón? Responde Sí o No.", "Sí", "Sin fuente la respuesta sería una suposición."),
    ],
    D=[
        ex("Hay tres preguntas: 1) ¿Cómo celebraba la comunidad de Valle Alto (inventada) cuando doña Rosa era niña? 2) ¿Fue lindo? 3) ¿Qué se puede preguntar al educador? ¿Cuál es la mejor pregunta histórica?", "La 1", "Pide un dato del pasado a una fuente."),
        ex("Una niña quiere preguntar algo que la comunidad guarda en reserva. ¿A quién debe consultar antes de preguntar? A) al educador tradicional B) a un desconocido en internet", "A", "El educador sabe qué se puede preguntar."),
    ],
    context=[ex("Tu curso visitará a doña Rosa (inventada). ¿Qué pregunta histórica llevas? A) ¿Cómo era la vertiente cuando usted era niña? B) ¿Le gusta el agua?", "A", "La A pide un dato del pasado.")],
    selfcheck=[
        ex("Escribe qué es una pregunta histórica.", "Una pregunta sobre el pasado que se puede responder con una fuente", "Es la idea central de la clase."),
        ex("Verdadero o falso: una pregunta de opinión sirve para investigar un hecho.", "Falso", "Una opinión no entrega un dato."),
        ex("Nombra una palabra con la que puede empezar una pregunta histórica.", "Cómo, quién, cuándo o dónde", "Son palabras que piden datos."),
    ],
    task=T("Imagina que visitarás a una persona mayor de la comunidad inventada de Valle Alto, doña Rosa. Escribe tres preguntas históricas: una con «cómo», una con «quién» y una con «cuándo». Subraya en cada una la palabra que pide el dato. Escribe al final de la hoja la respuesta que imaginas para una sola, rotulada como «Respuesta imaginada».",
           "¿Cómo era el camino al río cuando usted era niña? ¿Quién les enseñaba a cuidar la huerta? ¿Cuándo se juntaba la gente en la vertiente? Respuesta imaginada: «El camino era de tierra».",
           ["escribe tres preguntas con cómo, quién y cuándo", "las preguntas piden datos del pasado", "rotula la respuesta como imaginada"], ["tres preguntas", "respuesta imaginada"], ["escribir preguntas de opinión", "presentar la respuesta imaginada como real"],
           "Revisar que cada pregunta pida un dato; destacar que rotuló la respuesta como imaginada."),
    reinforce="Cambia dos preguntas de opinión a preguntas que pidan un dato.",
    extend="Inventa dos preguntas históricas para un objeto de práctica: una olla vieja de la comunidad de Valle Alto (inventada).",
)

L(
    OA7, 2,
    materials="Lápiz y hojas. Los testimonios, objetos y fichas son inventados y están escritos aquí.",
    use="Aprenderé a leer memorias y fuentes de una comunidad y a distinguir lo que la fuente dice de lo que yo pienso. Sirve para conocer la historia con respeto y sin inventar.",
    prior=["Sé hacer preguntas históricas.", "Sé que una fuente tiene quién cuenta, qué cuenta y permiso."],
    explain=[
        "Una memoria es lo que una persona o una comunidad recuerda y cuenta del pasado. Puede ser un relato oral, una fotografía familiar, un objeto o un texto. Estos materiales se llaman fuentes.",
        "Al leer una fuente nos preguntamos: ¿quién la entrega?, ¿de qué comunidad es?, ¿tiene permiso para compartirla? y ¿qué dice exactamente? También separamos lo que la fuente dice de lo que yo pienso o imagino.",
        "Una sola fuente no cuenta toda la historia. Cada persona recuerda una parte. Por eso decimos «según doña Rosa…», para dejar claro de quién viene el dato. Si dos fuentes dicen cosas distintas, no se corrige a ninguna: se pregunta a la comunidad.",
    ],
    vocab=[("memoria", "lo que una persona o comunidad recuerda y cuenta"), ("fuente oral", "relato que una persona cuenta con su voz"), ("objeto", "cosa que guarda recuerdos del pasado"), ("según", "palabra para decir quién entrega el dato"), ("interpretación", "lo que yo pienso de la fuente")],
    worked=[
        W("Leer un testimonio", "Testimonio inventado de don Luis, de Costa Clara: «Cuando yo era niño, las lanchas eran de madera y todas salían juntas al amanecer.» Anota fuente, dato y lo que yo pienso si digo «eran más lindas».", ["Fuente: don Luis.", "Dato: las lanchas eran de madera y salían juntas al amanecer.", "«Eran más lindas» es lo que yo pienso."], "Fuente: don Luis. Dato: lanchas de madera que salían juntas al amanecer. «Más lindas» es mi opinión."),
        W("Dos fuentes", "Doña Rosa dice: «El camino era de tierra». Don Pedro, también de Valle Alto, dice: «El camino tenía piedras a los lados». ¿Se contradicen?", ["Una habla del suelo.", "La otra habla de los lados.", "Pueden ser ciertas las dos."], "No se contradicen: cuentan partes distintas."),
    ],
    mistakes=[
        M("Escribir «el pueblo siempre hizo esto» a partir de un solo testimonio.", "Una persona recuerda una parte de la historia.", "Escribe «según don Luis…» o «según doña Rosa…»."),
        M("Mezclar lo que dice la fuente con lo que yo pienso.", "Parece que la fuente dijo algo que no dijo.", "Usa dos colores: uno para la fuente y otro para mi opinión."),
    ],
    R=[
        ex("Testimonio de don Luis: «Las lanchas eran de madera». ¿De qué material eran las lanchas?", "De madera", "Lo dice el testimonio."),
        ex("¿Qué palabra sirve para decir quién entrega el dato: «según» o «siempre»?", "Según", "Según indica la fuente."),
        ex("Un objeto viejo que guarda recuerdos, ¿es una fuente? Responde Sí o No.", "Sí", "Los objetos también cuentan parte del pasado."),
    ],
    C=[
        ex("Verdadero o falso: una sola persona cuenta toda la historia de una comunidad.", "Falso", "Cada persona recuerda una parte."),
        ex("¿Qué es una fuente oral? A) un relato contado con la voz B) un mapa sin nombre", "A", "Se cuenta hablando."),
        ex("Verdadero o falso: «eran más lindas» lo dice la fuente en el testimonio de don Luis.", "Falso", "Es la interpretación de quien lee."),
    ],
    A=[
        ex("Clasifica en FUENTE o MI OPINIÓN: a) «las lanchas eran de madera» b) «creo que se ven felices» c) «salían al amanecer».", "a fuente, b mi opinión, c fuente", "El testimonio dice madera y amanecer; «felices» lo agrega quien lee."),
        ex("Escribe la frase con «según»: dato, las lanchas salían juntas; fuente, don Luis.", "Según don Luis, las lanchas salían juntas", "Se atribuye el dato a la fuente."),
        ex("Doña Rosa dice que el camino era de tierra. Don Pedro dice que tenía piedras a los lados. Cuenta cuántos datos distintos del camino hay en total.", "2", "Tierra y piedras a los lados son dos datos."),
    ],
    Z=[
        ex("Ana lee solo el testimonio de don Luis y escribe: «Siempre todas las comunidades salían al amanecer». ¿Qué error comete?", "Generaliza desde una sola fuente", "Don Luis habla de su comunidad."),
        ex("Tomás encuentra que dos fuentes dicen cosas distintas y borra una. ¿Qué debería hacer? A) Preguntar a la comunidad B) Borrar la que no le gusta", "A", "No se corrige a ninguna sin consultar."),
    ],
    D=[
        ex("Una foto de Valle Alto (inventada) muestra a varias personas junto a la vertiente. Alguien dice «es el día de la fiesta». ¿Puede afirmarlo sin una fuente? Responde Sí o No.", "No", "La foto no dice qué día es."),
        ex("Una niña escribe «según doña Rosa, el cerro era alto». Otro escribe «el cerro era altísimo y bellísimo». ¿Quién separó la fuente de su opinión?", "La niña", "Usó «según» y se quedó en el dato."),
    ],
    context=[ex("En la biblioteca de la escuela (inventada) hay una cinta con la voz de don Luis y un permiso firmado para usarla. ¿Puedes usarla en tu trabajo si citas «según don Luis»? Responde Sí o No.", "Sí", "Tiene permiso y atribuyes la fuente.")],
    selfcheck=[
        ex("¿Qué es una memoria?", "Lo que una persona o comunidad recuerda y cuenta", "Es la definición de la lección."),
        ex("Verdadero o falso: dos fuentes que cuentan cosas distintas siempre se contradicen.", "Falso", "Pueden contar partes distintas."),
        ex("Escribe qué palabra pones antes del dato para decir quién lo contó.", "Según", "Atribuye el dato."),
    ],
    task=T("Lee dos testimonios inventados de Valle Alto. Doña Rosa: «El camino al río era de tierra y los niños lo recorrían descalzos en verano.» Don Pedro: «Yo recuerdo que junto al camino había un álamo muy grande.» Haz una tabla con tres columnas: fuente, lo que dice y lo que yo pienso. Rellena una fila por cada persona. Al final escribe una pregunta para el educador tradicional sobre la historia de tu zona.",
           "Doña Rosa: el camino era de tierra y los niños iban descalzos en verano; yo pienso que sería divertido. Don Pedro: había un álamo grande junto al camino; yo pienso que daría sombra. Pregunta: ¿qué cuenta la comunidad sobre cómo era nuestro lugar antes?",
           ["rellena las tres columnas", "no mezcla fuente y opinión", "plantea una pregunta respetuosa"], ["tabla de tres columnas", "pregunta escrita"], ["escribir su opinión en la columna de la fuente", "olvidar la fuente"],
           "Revisar que cada dato esté en la columna correcta; valorar que use «según»."),
    reinforce="Subraya con un color los datos de los testimonios y con otro tus opiniones.",
    extend="Escribe una frase que junte los dos testimonios usando «según doña Rosa» y «según don Pedro».",
)

L(
    OA7, 3,
    materials="Lápiz y hojas. Los relatos son inventados y están escritos aquí.",
    use="Aprenderé a reconocer cambios y continuidades en la historia de una comunidad. Sirve para entender que el pasado y el presente se conectan.",
    prior=["Sé leer una fuente y separar lo que dice de lo que pienso.", "Sé que los pueblos originarios viven hoy."],
    explain=[
        "Un cambio es algo que antes era de una manera y hoy es distinto. Una continuidad es algo que sigue igual a través del tiempo. En la historia de una comunidad hay cambios y continuidades al mismo tiempo.",
        "Para encontrarlos comparamos dos momentos: antes y hoy. Nos preguntamos qué es distinto, qué sigue igual y por qué. Los cambios no significan que la cultura se perdió. Una comunidad puede usar cosas nuevas y mantener lo que valora.",
        "Los pueblos originarios viven hoy. Sus integrantes van a la escuela, usan teléfono, trabajan y también mantienen saberes de su pueblo. Para saber qué cambió y qué continúa en una comunidad real, hay que preguntar a la propia comunidad.",
    ],
    vocab=[("cambio", "algo que antes era de una manera y hoy es distinto"), ("continuidad", "algo que sigue igual a través del tiempo"), ("antes", "tiempo pasado"), ("hoy", "tiempo presente"), ("comparar", "mirar dos cosas para ver qué se parece y qué es distinto")],
    worked=[
        W("Cambio y continuidad", "Testimonio inventado de doña Rosa: «Antes llevábamos el agua en baldes desde la vertiente. Hoy llega por una manguera, pero seguimos juntándonos en la vertiente a conversar.» ¿Qué cambió y qué continúa?", ["Cambió cómo se lleva el agua.", "Continúa juntarse en la vertiente.", "Escribo las dos cosas."], "Cambió: del balde a la manguera. Continúa: juntarse en la vertiente a conversar."),
        W("Cultura viva", "Un niño dice: «Si usan manguera, ya perdieron su cultura». ¿Tiene razón?", ["Miro el testimonio.", "La comunidad sigue juntándose y cuidando la vertiente.", "Cambiar una herramienta no es perder la cultura."], "No: cambió una herramienta, pero la comunidad sigue con su costumbre."),
    ],
    mistakes=[
        M("Pensar que todo cambio significa que se perdió la cultura.", "Las comunidades pueden cambiar y mantener lo que valoran.", "Pregunta qué sigue igual."),
        M("Hablar de una comunidad en pasado como si ya no existiera.", "Los pueblos originarios viven hoy.", "Usa el presente: «vive», «cuida», «se junta»."),
    ],
    R=[
        ex("Antes el agua se llevaba en baldes y hoy llega por manguera. ¿Eso es un cambio o una continuidad?", "Un cambio", "La manera de llevar el agua es distinta."),
        ex("La gente de Valle Alto (inventada) seguía juntándose en la vertiente a conversar antes y hoy. ¿Eso es un cambio o una continuidad?", "Una continuidad", "Sigue igual a través del tiempo."),
        ex("¿Qué palabra marca el tiempo pasado en «antes llevábamos agua en baldes»? A) antes B) hoy", "A", "Antes señala el pasado."),
    ],
    C=[
        ex("Verdadero o falso: si una comunidad cambia una herramienta, pierde su cultura.", "Falso", "Puede cambiar herramientas y mantener su cultura."),
        ex("¿Qué es una continuidad? A) algo que sigue igual B) algo que se perdió para siempre", "A", "Continuidad es lo que sigue igual."),
        ex("Verdadero o falso: las comunidades indígenas también usan cosas nuevas, como teléfonos.", "Verdadero", "Viven hoy y usan lo que hay hoy."),
    ],
    A=[
        ex("Clasifica en CAMBIO o CONTINUIDAD, según el testimonio de doña Rosa: a) antes el agua se llevaba en baldes b) la gente se junta en la vertiente a conversar, antes y hoy c) hoy el agua llega por una manguera.", "a cambio, b continuidad, c cambio", "Juntarse en la vertiente sigue igual; la manera de llevar el agua es distinta."),
        ex("Completa la tabla de Costa Clara (inventada): Antes salían al amanecer en lanchas de madera. Hoy salen al amanecer en lanchas con motor. ¿Qué continúa?", "Salir al amanecer", "El horario sigue igual."),
        ex("En la tabla anterior, ¿qué cambió? A) las lanchas, que hoy tienen motor B) la hora de salida", "A", "Las lanchas ahora tienen motor; la hora sigue igual."),
    ],
    Z=[
        ex("Ema dice: «Antes la comunidad se juntaba en la vertiente y hoy ya no». Pero doña Rosa dice que hoy se siguen juntando. ¿Quién tiene razón según la fuente?", "Doña Rosa", "Ella cuenta lo que ocurre hoy."),
        ex("Pedro escribe: «Los pueblos originarios vivían en el campo». ¿Qué problema tiene el verbo?", "Habla en pasado como si ya no existieran", "Hoy los pueblos viven en distintos lugares."),
    ],
    D=[
        ex("Una niña de una comunidad inventada hace tareas con el computador y también aprende a cuidar el agua con su abuela. ¿Qué muestra esto: cambio, continuidad o ambas?", "Ambas", "Hay algo nuevo y algo que se mantiene."),
        ex("Para saber qué cambió de verdad en tu zona, ¿a quién consultas primero? A) a la comunidad o al educador tradicional B) a un video al azar", "A", "Ellos son la fuente confiable."),
    ],
    context=[ex("Doña Rosa cuenta que antes se trabajaba solo a mano y hoy usan también un carretón. La huerta sigue siendo de toda la comunidad. ¿Cuál es la continuidad?", "La huerta es de toda la comunidad", "Eso sigue igual, aunque cambie la herramienta.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es un cambio.", "Algo que antes era de una manera y hoy es distinto", "Es la definición de la clase."),
        ex("Verdadero o falso: los pueblos originarios solo existieron en el pasado.", "Falso", "Los pueblos viven hoy."),
        ex("¿Qué haces para saber qué cambió en una comunidad real? A) Pregunto a la comunidad B) Lo adivino", "A", "La comunidad es la fuente."),
    ],
    task=T("Lee este relato inventado de la comunidad de Costa Clara: «Antes salíamos a pescar en lanchas de madera y volvíamos a repartir el pescado entre las familias. Hoy las lanchas tienen motor, pero seguimos repartiendo el pescado entre las familias.» Haz un cuadro con dos columnas: «Cambió» y «Continúa». Escribe dos frases en presente sobre la comunidad. Añade una pregunta para el educador tradicional sobre algo que continúa en tu comunidad.",
           "Cambió: las lanchas ahora tienen motor. Continúa: repartir el pescado entre las familias. Frases: «La comunidad de Costa Clara pesca hoy con motor. La comunidad reparte el pescado entre las familias.» Pregunta: ¿qué costumbre de nuestra comunidad sigue igual hace muchos años?",
           ["separa un cambio y una continuidad", "usa el presente", "formula una pregunta respetuosa"], ["cuadro de dos columnas", "dos frases", "pregunta"], ["escribir todo en pasado", "decir que la cultura se perdió"],
           "Valorar el uso del presente; preguntar por qué la continuidad es importante."),
    reinforce="Pinta de verde lo que continúa y de rojo lo que cambió en el relato de Costa Clara.",
    extend="Escribe un cambio y una continuidad que veas en tu propia familia o curso.",
)

L(
    OA7, 4,
    materials="Lápiz y hojas. El relato está escrito aquí y es inventado.",
    use="Aprenderé a vincular la historia de una comunidad con su presente y con el futuro que desea. Sirve para valorar por qué la historia importa hoy.",
    prior=["Sé hacer preguntas históricas y leer fuentes.", "Sé reconocer cambios y continuidades."],
    explain=[
        "La historia de una comunidad ayuda a entender su presente. Si sabemos cómo se cuidó un lugar antes, entendemos por qué hoy se cuida de cierta manera. El pasado explica una parte de lo que ocurre hoy.",
        "El futuro es lo que la comunidad desea para después. Una comunidad puede querer, por ejemplo, cuidar sus lugares o enseñar a las nuevas generaciones, pero eso lo dice cada comunidad. El futuro lo construyen las personas con lo que hacen hoy.",
        "Para vincular pasado, presente y futuro, usamos una línea de tiempo con tres partes: antes, hoy y mañana. Para la comunidad real, quien dice qué desea para su futuro es la propia comunidad. Nosotros escuchamos y no decidimos por ellos.",
    ],
    vocab=[("futuro", "lo que ocurrirá después"), ("línea de tiempo", "dibujo que ordena sucesos desde antes hasta después"), ("generación", "grupo de personas de edades parecidas"), ("deseo", "lo que alguien quiere lograr"), ("vincular", "unir dos cosas explicando su relación")],
    worked=[
        W("Armar una línea de tiempo", "Relato inventado de Valle Alto: «Mis abuelos cuidaban la vertiente. Hoy los niños ayudan a limpiarla. Mañana queremos que sigan cuidándola.» Ordena en antes, hoy y mañana.", ["Antes: los abuelos cuidaban la vertiente.", "Hoy: los niños ayudan a limpiarla.", "Mañana: se desea que sigan cuidándola."], "Antes: abuelos cuidan. Hoy: niños limpian. Mañana: seguir cuidándola."),
        W("Explicar el vínculo", "¿Cómo se conecta el cuidado de los abuelos con lo que hacen los niños hoy?", ["Los abuelos mostraron cómo cuidar.", "Los niños hoy lo hacen con ellos.", "Así se transmite el cuidado."], "Los niños aprenden de los abuelos y continúan el cuidado."),
    ],
    mistakes=[
        M("Decidir cuál es el futuro que debe tener una comunidad real.", "Eso lo decide la propia comunidad.", "Escucha lo que la comunidad desea y no decidas por ella."),
        M("Poner solo el pasado en la línea de tiempo.", "Falta lo que ocurre hoy y lo que se desea.", "Incluye antes, hoy y mañana."),
    ],
    R=[
        ex("En el relato de Valle Alto, ¿quién cuidaba la vertiente antes: los abuelos o los niños de hoy?", "Los abuelos", "El relato dice que los abuelos la cuidaban."),
        ex("¿Qué ayudan a hacer los niños hoy según el relato? A) limpiar la vertiente B) construir un puente", "A", "El relato dice que ayudan a limpiarla."),
        ex("¿Qué desea la comunidad para mañana en el relato?", "Que sigan cuidando la vertiente", "Lo dice la última frase."),
    ],
    C=[
        ex("Verdadero o falso: el pasado no tiene relación con el presente.", "Falso", "El pasado explica una parte del presente."),
        ex("¿Quién dice qué desea para su futuro una comunidad real? A) la propia comunidad B) cualquier visitante", "A", "Ella decide su futuro."),
        ex("¿Cuántas partes tiene la línea de tiempo de esta clase? Escribe el número.", "3", "Son antes, hoy y mañana."),
    ],
    A=[
        ex("Ordena en una línea de tiempo: a) los niños limpian la vertiente b) los abuelos la cuidaban c) se desea que siga cuidándose. Escribe las letras de antes a mañana.", "b, a, c", "Primero los abuelos, hoy los niños y mañana el deseo."),
        ex("Relato inventado de Costa Clara: «Antes los abuelos contaban historias en la playa. Hoy las cuentan también en la escuela.» Completa: hoy los abuelos cuentan historias también en la ___. Escribe la palabra.", "escuela", "El relato dice que hoy las cuentan en la escuela."),
        ex("Escribe una frase que una el pasado con el presente: los abuelos cuidaban la vertiente y hoy los niños la limpian.", "Los niños limpian la vertiente como la cuidaban los abuelos", "Une los dos tiempos con la misma acción."),
    ],
    Z=[
        ex("Mateo dice: «Como el pueblo es del pasado, no necesita futuro». ¿Qué error comete?", "Piensa que el pueblo es del pasado", "Los pueblos viven hoy y construyen su futuro."),
        ex("Ana propone qué debería querer una comunidad real para su futuro. ¿Qué debe hacer primero? A) Preguntar a la comunidad B) Decidir ella", "A", "La comunidad decide lo que desea."),
    ],
    D=[
        ex("Dos niños: uno dice «mañana queremos que sigan cuidando la vertiente». Otro dice «mañana nadie la cuidará». ¿Cuál frase sale del relato?", "La primera", "El relato expresa el deseo de continuar."),
        ex("En el relato, ¿qué acción se mantiene entre antes, hoy y mañana? A) cuidar la vertiente B) trabajar en la ciudad", "A", "Es la acción que aparece en los tres momentos."),
    ],
    context=[ex("Tu curso hará una línea de tiempo con el relato de Valle Alto. ¿Qué tres títulos pones? A) antes, hoy y mañana B) rojo, azul y verde", "A", "Esos títulos ordenan los tiempos.")],
    selfcheck=[
        ex("Escribe las tres partes de la línea de tiempo.", "Antes, hoy y mañana", "Ordenan pasado, presente y futuro."),
        ex("Verdadero o falso: yo puedo decidir qué futuro debe tener una comunidad real.", "Falso", "Lo decide la comunidad."),
        ex("¿Para qué sirve conocer la historia de una comunidad? A) Para entender mejor su presente B) Para olvidarla", "A", "La historia explica una parte del presente."),
    ],
    task=T("Lee este relato inventado de Costa Clara: «Mi abuelo pescaba y repartía el pescado entre las familias. Hoy yo pesco con mi tío y también repartimos. Mañana queremos que los niños aprendan a cuidar el mar.» Dibuja una línea de tiempo con tres recuadros: antes, hoy y mañana. En cada uno escribe una frase del relato. Debajo escribe una frase que explique cómo se conectan los tres tiempos. Añade una pregunta para el educador tradicional sobre lo que desea tu comunidad para el futuro.",
           "Antes: mi abuelo pescaba y repartía el pescado. Hoy: yo pesco con mi tío y repartimos. Mañana: queremos que los niños aprendan a cuidar el mar. Se conectan porque antes y hoy se reparte el pescado, y mañana se quiere cuidar el mar. Pregunta: ¿qué desea nuestra comunidad para el futuro?",
           ["completa los tres recuadros con datos del relato", "explica la conexión", "formula una pregunta respetuosa"], ["línea de tiempo", "frase de conexión", "pregunta"], ["dejar vacío «mañana»", "decidir por la comunidad"],
           "Preguntar cómo une el relato los tres tiempos; valorar la pregunta final."),
    reinforce="Completa una línea de tiempo con un cambio de tu escuela: antes, hoy y mañana.",
    extend="Escribe dos deseos de futuro que una comunidad podría tener, rotulándolos como ejemplos inventados.",
)
