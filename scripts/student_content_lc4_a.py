"""Cuaderno del estudiante, 4.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 07 (organización del territorio) y OA 08 (historia, cambio y continuidad en la organización).

Criterio de autoría: las comunidades, los lugares, las personas y los relatos de práctica son INVENTADOS
(no pertenecen a ningún pueblo real) y se rotulan así. No se afirma nada de lengua, ritos, fechas de
celebraciones, arte, cosmovisión, organización política ni roles de un pueblo concreto. Lo tradicional lo
enseñan el educador o la educadora tradicional y la comunidad; ningún ejercicio exige saber una lengua
indígena. El contenido que enseña cada pueblo (su territorio, su historia) queda para la fuente comunitaria.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA7, OA8 = "LC04 OA 07", "LC04 OA 08"

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


FV4 = ("Ficha situada (inventada). Comunidad: Valle Alto (no es un pueblo real). Territorio: un valle con río, vertiente, huerta comunitaria y cerro Pelado. "
       "Fuente y responsable: doña Rosa, vecina de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: doña Rosa autorizó usar esta ficha en la escuela. "
       "Límite: no se cuenta dónde está el sitio de respeto del cerro.")
FC4 = ("Ficha situada (inventada). Comunidad: Costa Clara (no es un pueblo real). Territorio: una caleta con playa, rocas y mar. "
       "Fuente y responsable: don Luis, pescador de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: don Luis autorizó usar esta ficha en la escuela. "
       "Límite: no se cuentan las historias que la comunidad reserva.")

# ============================================================ OA 07 · Territorio, espiritualidad y vida comunitaria
L(
    OA7, 1,
    materials="Lápiz y hojas. Las fichas y los testimonios están escritos en este cuaderno. Las comunidades, los lugares y las personas son inventados.",
    use="Aprenderé a describir cómo se organiza un territorio y a situar quién lo cuenta. Sirve para hablar de un lugar sin reducirlo a un mapa y sin decir que todos los pueblos lo viven igual.",
    prior=["Sé que una ficha situada dice comunidad, territorio, fuente, permiso y límite.", "Sé que lo que cuenta una comunidad vale para esa comunidad."],
    explain=[
        "Un territorio no es solo un dibujo en un mapa. Es el espacio donde una comunidad vive, trabaja, se junta y recuerda. Está organizado: hay lugares para vivir, para cultivar o pescar, para reunirse y lugares de respeto. Esa organización une el espacio natural, como el río o el cerro, con el espacio social, como las familias y sus reuniones.",
        "Cada comunidad organiza su territorio a su manera y lo explica con sus propias palabras. Por eso lo primero es situar: decir de qué comunidad habla la ficha, quién cuenta (la fuente), si autorizó compartirlo (el permiso) y qué no se cuenta (el límite). Con esos datos sabemos hasta dónde llega lo que afirmamos.",
        "Para describir la organización de un territorio, lee la fuente y anota qué hay en cada lugar y para qué sirve. Lo que no está escrito no se agrega. Lo que dice una ficha vale para su comunidad, no para todos los pueblos. Si hay dudas, se pregunta al educador o educadora tradicional.",
    ],
    vocab=[("territorio", "espacio que una comunidad habita, trabaja y recuerda"), ("organización del territorio", "cómo se reparten y usan sus lugares"), ("espacio natural", "lo que existe en la naturaleza, como un río o un cerro"), ("espacio social", "lugares y momentos donde las personas se relacionan"), ("fuente", "persona o texto que entrega el dato")],
    worked=[
        W("Describir la organización", "Testimonio de doña Rosa (inventado): «Las casas están junto al río. La huerta comunitaria está bajo la vertiente. Las reuniones se hacen en la explanada. El cerro Pelado es lugar de respeto.» ¿Para qué sirve cada lugar?", ["Junto al río: viven las familias.", "Bajo la vertiente: huerta que cuida toda la comunidad.", "En la explanada: reuniones. Cerro Pelado: lugar de respeto."], "Casas para vivir, huerta para cultivar, explanada para reunirse y cerro como lugar de respeto."),
        W("Separar la ficha de mi idea", "Un niño dice: «En Valle Alto cada familia tiene su propia huerta». ¿Lo dice el testimonio?", ["El testimonio habla de una huerta comunitaria.", "No habla de huertas por familia.", "Esa frase es idea del niño."], "No lo dice: el testimonio menciona una huerta comunitaria."),
    ],
    mistakes=[
        M("Pensar que el territorio es solo el mapa o el límite dibujado.", "El territorio incluye lo que la comunidad hace y recuerda allí.", "Describe los lugares y para qué sirven."),
        M("Decir que todos los pueblos organizan su territorio como Valle Alto.", "La ficha habla de una sola comunidad.", "Escribe siempre el nombre de la comunidad de la ficha."),
    ],
    R=[
        ex("Según el testimonio de doña Rosa, ¿dónde se hacen las reuniones de Valle Alto?", "En la explanada", "El testimonio lo dice así."),
        ex("En el testimonio, ¿qué está bajo la vertiente: la huerta comunitaria o las casas?", "La huerta comunitaria", "Las casas están junto al río."),
        ex("Ficha inventada: «Comunidad: Valle Alto. Fuente y responsable: doña Rosa, vecina de la comunidad. Permiso: sí. Límite: no se cuenta dónde está el sitio de respeto del cerro.» ¿Quién es la fuente?", "Doña Rosa", "La ficha escribe su nombre como fuente y responsable."),
    ],
    C=[
        ex("Verdadero o falso: el territorio es solamente el dibujo de un mapa.", "Falso", "Incluye lo que la comunidad vive, trabaja y recuerda."),
        ex("¿Qué une la organización de un territorio? A) el espacio natural y el espacio social B) solo los colores del mapa", "A", "Junta el río o el cerro con las familias y sus reuniones."),
        ex("Verdadero o falso: lo que dice la ficha de Valle Alto vale para todos los pueblos de Chile.", "Falso", "Una ficha habla de una sola comunidad."),
    ],
    A=[
        ex("Testimonio inventado de don Luis, de Costa Clara: «Los botes se guardan en la playa. Las redes se arreglan en las rocas planas. La comunidad se junta en la sede.» ¿Dónde se arreglan las redes?", "En las rocas planas", "El testimonio lo dice."),
        ex("Clasifica los lugares de Valle Alto en ESPACIO NATURAL o ESPACIO SOCIAL: a) el río b) la explanada de reuniones.", "a natural, b social", "El río existe en la naturaleza; la explanada es donde las personas se reúnen."),
        ex("Una ficha trae comunidad, territorio, fuente y límite, pero no el permiso. ¿Puedes usarla para tu trabajo? Responde Sí o No.", "No", "Sin permiso no se sabe si se puede compartir."),
    ],
    Z=[
        ex("Tomás escribe: «En Valle Alto hay un lago» porque ve un lago en su cuaderno de dibujo. ¿Por qué esa frase no es válida?", "La ficha no habla de un lago", "Solo se afirma lo que dice la fuente."),
        ex("Sofía dice: «Si en Costa Clara hay caleta, todos los pueblos viven junto al mar». ¿Qué error comete?", "Generaliza una ficha a todos los pueblos", "Una comunidad no representa a todas."),
    ],
    D=[
        ex("Dos fichas inventadas: Valle Alto (valle, río, huerta) y Costa Clara (caleta, rocas, mar). Alguien escribe «la comunidad arregla redes en las rocas planas». ¿De cuál viene la frase?", "De Costa Clara", "Las rocas planas aparecen solo en el testimonio de don Luis."),
        ex("La ficha de Valle Alto dice: «no se cuenta dónde está el sitio de respeto del cerro». ¿Escribes su ubicación en tu trabajo? Responde Sí o No.", "No", "El límite de la ficha lo prohíbe."),
    ],
    context=[ex("En tu curso leen el testimonio de doña Rosa. Una niña quiere dibujar un mapa que marque dónde está el sitio de respeto del cerro Pelado. Según la ficha, ¿qué debe hacer? A) dibujarlo igual B) dejar ese lugar sin marcar", "B", "El límite dice que esa ubicación no se cuenta.")],
    selfcheck=[
        ex("Nombra dos datos que se necesitan para situar un territorio.", "Dos entre: comunidad, fuente, permiso, límite", "Son datos de la ficha situada."),
        ex("Verdadero o falso: el territorio incluye lo que la comunidad hace en él, no solo el mapa.", "Verdadero", "Es la idea central de la clase."),
        ex("¿Qué haces si tienes una duda sobre el territorio de una comunidad real? A) Pregunto al educador tradicional o a la comunidad B) Lo imagino", "A", "Ellos son la fuente."),
    ],
    task=T("Lee la ficha de Costa Clara (inventada): «" + FC4 + "» y el testimonio: «Los botes se guardan en la playa. Las redes se arreglan en las rocas planas. La comunidad se junta en la sede.» Haz una tabla de tres columnas: lugar, para qué sirve y espacio (natural o social). Escribe debajo una frase con «La fuente dice…» y otra con «Yo pienso…». Cierra con una pregunta que le harías al educador tradicional sobre el territorio de tu zona.",
           "Playa: guardar botes (natural). Rocas planas: arreglar redes (natural). Sede: reunirse (social). La fuente dice que las redes se arreglan en las rocas planas. Yo pienso que debe ser entretenido verlo. Pregunta: ¿qué lugares de nuestra zona cuida la comunidad?",
           ["completa la tabla con datos del testimonio", "separa lo que dice la fuente de lo que piensa", "formula una pregunta respetuosa"], ["tabla de tres columnas", "dos frases rotuladas", "pregunta escrita"], ["agregar lugares que el testimonio no menciona", "generalizar a todos los pueblos"],
           "Pedir que señale en qué línea del testimonio está cada dato; valorar que separe la fuente de su opinión."),
    reinforce="Dibuja un esquema de Valle Alto con solo los lugares del testimonio, sin agregar otros ni marcar el sitio de respeto.",
    extend="Escribe dos diferencias entre la organización del territorio de Valle Alto y la de Costa Clara, usando solo las fichas.",
)

L(
    OA7, 2,
    materials="Lápiz y hojas. El testimonio está escrito aquí y es inventado.",
    use="Aprenderé a relacionar el territorio con la vida espiritual de una comunidad leyendo lo que ella cuenta. Sirve para respetar lo que es de la comunidad y no adivinar.",
    prior=["Sé describir cómo se organiza un territorio con una ficha.", "Sé que hay cosas que una comunidad no cuenta."],
    explain=[
        "Para muchas comunidades, algunos lugares del territorio también son importantes por su vida espiritual. La espiritualidad es la manera en que una comunidad entiende y cuida lo que considera sagrado o muy respetable. Esa manera se nota en cómo las personas se comportan en esos lugares.",
        "Solo la comunidad puede decir qué lugar es importante y por qué. Nosotros no lo adivinamos mirando un cerro o una foto. Un lugar puede parecer común y ser muy importante, o parecer misterioso y no serlo. Lo que sí podemos leer en un testimonio son las normas de respeto, como ir en silencio o pedir permiso.",
        "Relacionar territorio y espiritualidad es unir dos datos de la fuente: el lugar y cómo la comunidad lo cuida. Lo que la comunidad guarda para sí no se pregunta con insistencia, no se inventa ni se busca por otro lado. Si queremos saber más, preguntamos al educador o educadora tradicional.",
    ],
    vocab=[("espiritualidad", "manera de entender y cuidar lo que una comunidad considera sagrado"), ("sagrado", "muy importante y digno de respeto"), ("norma de respeto", "regla para comportarse en un lugar importante"), ("resguardar", "cuidar algo y no mostrarlo a todos"), ("testimonio", "relato de una persona sobre lo que vive o sabe")],
    worked=[
        W("Qué sabemos y qué no", "Testimonio inventado de doña Rosa: «El cerro Pelado es lugar de respeto. Se sube en silencio y con una persona mayor de la comunidad. Lo que se hace arriba no se cuenta.» ¿Qué sabemos y qué no?", ["Sabemos que es lugar de respeto.", "Sabemos que se sube en silencio y con una persona mayor.", "Lo que se hace arriba no se cuenta, así que no lo sabemos."], "Sabemos las normas de respeto; no sabemos qué se hace arriba."),
        W("No adivinar", "Un niño dice: «Seguro que arriba hay una ceremonia con música». ¿Se puede afirmar?", ["Reviso el testimonio: no menciona música.", "Tampoco dice qué se hace arriba.", "No se puede afirmar."], "No, porque el testimonio no lo dice."),
    ],
    mistakes=[
        M("Describir una ceremonia que la comunidad no contó.", "Es adivinar y puede ser falso o irrespetuoso.", "Escribe solo lo que dice la fuente."),
        M("Buscar en internet lo que la comunidad decidió no contar.", "Lo reservado no se publica ni se busca por otro lado.", "Pregunta al educador tradicional qué se puede conocer."),
    ],
    R=[
        ex("Según doña Rosa, ¿cómo se sube al cerro Pelado: en silencio o en voz alta?", "En silencio", "El testimonio dice que se sube en silencio."),
        ex("¿Con quién se sube al cerro según el testimonio? A) con una persona mayor de la comunidad B) con cualquier visitante", "A", "El testimonio lo dice así."),
        ex("Si la comunidad dice «lo que se hace arriba no se cuenta», ¿se puede inventar lo que falta? Responde Sí o No.", "No", "Lo que no se cuenta no se inventa."),
    ],
    C=[
        ex("En Lengua y Cultura, ¿qué es la espiritualidad? A) la manera en que una comunidad entiende y cuida lo sagrado B) un tipo de comida", "A", "Es su manera de entender y cuidar lo importante."),
        ex("Verdadero o falso: un lugar es sagrado cuando se ve misterioso en una foto.", "Falso", "Lo dice la comunidad, no la apariencia."),
        ex("Verdadero o falso: ir en silencio es una norma de respeto en el testimonio de doña Rosa.", "Verdadero", "El testimonio lo señala."),
    ],
    A=[
        ex("Testimonio inventado de don Luis: «Las rocas del extremo de la caleta son lugar de respeto. Allí no se grita ni se juega.» Escribe una norma de respeto de ese testimonio.", "No gritar o no jugar", "Son las dos normas escritas."),
        ex("Testimonio de doña Rosa: «Se sube en silencio y con una persona mayor.» Une cada frase con su origen. 1) «Se sube en silencio» 2) «Arriba hay una cueva con dibujos» a) lo dice el testimonio b) lo imagino yo", "1-a, 2-b", "La primera está escrita; la segunda no."),
        ex("Una niña escribe: «El cerro Pelado es lugar de respeto». No dice quién lo cuenta. ¿Atribuyó la fuente? Responde Sí o No.", "No", "Faltó escribir que lo cuenta doña Rosa."),
    ],
    Z=[
        ex("Pedro dice: «El cerro de mi ciudad parece misterioso, entonces es sagrado para algún pueblo». ¿Qué error comete?", "Adivina sin que una fuente lo diga", "Solo la comunidad dice qué es sagrado."),
        ex("Ana quiere agregar a su trabajo lo que se hace arriba del cerro, que doña Rosa no contó. ¿Qué debe hacer? A) inventarlo B) dejar escrito que esa parte no se cuenta", "B", "Lo reservado se respeta y no se inventa."),
    ],
    D=[
        ex("Dos niños leen el mismo testimonio. Uno escribe «se sube en silencio con una persona mayor». Otro escribe «allí hay una cueva con dibujos». ¿Cuál se queda en lo que dice la fuente?", "El primero", "El segundo agrega algo que el testimonio no dice."),
        ex("Un lugar no parece especial, pero la comunidad dice que es muy importante. ¿Quién sabe por qué lo es: la comunidad o quien lo mira de lejos?", "La comunidad", "Ella conoce su significado."),
    ],
    context=[ex("Un visitante llega a Valle Alto y quiere subir al cerro Pelado sin avisar. Según el testimonio, ¿qué debe hacer antes? A) pedir ir con una persona mayor de la comunidad B) subir rápido para no molestar", "A", "El testimonio dice que se sube con una persona mayor de la comunidad.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es la espiritualidad.", "La manera en que una comunidad entiende y cuida lo sagrado", "Es la idea central de la explicación."),
        ex("¿Qué haces con lo que la comunidad no cuenta?", "Lo respeto y no lo invento", "Lo reservado no se comparte."),
        ex("Verdadero o falso: puedo saber por mi cuenta si un lugar es sagrado para una comunidad.", "Falso", "Lo dice la comunidad."),
    ],
    task=T("Lee este testimonio inventado de doña Rosa: «La vertiente de Valle Alto da agua a todas las familias. Se agradece el agua en silencio. Hay cosas que solo conversamos entre nosotros.» Haz dos columnas: «Lo que sí sé» y «Lo que no sé». Después escribe una frase que una el lugar con la forma de cuidarlo, empezando con «Doña Rosa cuenta que…». No dibujes ni describas ninguna ceremonia.",
           "Lo que sí sé: la vertiente da agua a todas las familias; se agradece el agua en silencio. Lo que no sé: lo que la comunidad conversa solo entre ellos. Doña Rosa cuenta que la vertiente se cuida agradeciendo el agua en silencio.",
           ["distingue lo que sabe de lo que no sabe", "atribuye la fuente", "une lugar y forma de cuidarlo sin inventar"], ["dos columnas", "frase con la fuente"], ["describir una ceremonia no contada", "completar con datos propios como si fueran de la fuente"],
           "Preguntar de qué línea del testimonio sale cada dato; valorar que deje en blanco lo no contado."),
    reinforce="Subraya en el testimonio de doña Rosa las normas de respeto con un color.",
    extend="Explica con tus palabras por qué es importante no inventar lo que una comunidad decidió no contar.",
)

L(
    OA7, 3,
    materials="Lápiz y hojas. El testimonio está escrito aquí y es inventado. Para los cálculos solo se usan multiplicaciones y divisiones de las tablas.",
    use="Aprenderé a relacionar una festividad con la producción de una comunidad, es decir, con lo que cultiva, pesca o elabora. Sirve para entender que las celebraciones y el trabajo se conectan con el territorio.",
    prior=["Sé que el territorio tiene lugares con distintos usos.", "Sé multiplicar y dividir con las tablas."],
    explain=[
        "La producción es lo que una comunidad cultiva, pesca, cría o elabora con lo que le da su territorio. Una festividad es un momento especial en que la comunidad se junta a celebrar o a compartir. En muchos casos, ambas están relacionadas: se celebra lo que se logró o se comparte lo producido.",
        "En esta clase usamos un encuentro inventado de Valle Alto para practicar. Lo que cada comunidad real celebra, cuándo lo hace y cómo lo hace lo cuenta ella; nosotros no lo adivinamos ni usamos fechas inventadas como si fueran reales. Un buen análisis relaciona tres datos: qué se produce, dónde y cuándo se produce y cómo se comparte.",
        "También se pueden hacer cuentas con la producción, por ejemplo cuántos canastos se juntan o cuántos toca por mesa. Las cuentas ayudan a ver que compartir exige organización. Lo que no esté escrito en la fuente no se agrega, y las fechas y los modos de celebrar de una comunidad real se consultan al educador tradicional.",
    ],
    vocab=[("producción", "lo que una comunidad cultiva, pesca, cría o elabora"), ("festividad", "momento especial en que una comunidad se junta a celebrar"), ("cosecha", "recoger lo que se sembró"), ("compartir", "repartir algo entre varios"), ("semilla", "parte de la planta con la que se vuelve a sembrar")],
    worked=[
        W("Relacionar producción y encuentro", "Testimonio inventado de doña Rosa: «Cuando termina la cosecha de la huerta comunitaria, nos juntamos en la explanada. Cada familia trae lo que cosechó y lo compartimos. Guardamos semillas para volver a sembrar.» ¿Qué relación hay?", ["La producción es la cosecha de la huerta.", "El encuentro ocurre al terminar la cosecha.", "Se comparte lo cosechado y se guardan semillas."], "El encuentro celebra y comparte lo que produce la huerta."),
        W("Cuenta del encuentro", "Hay 8 familias y cada una trae 6 canastos. ¿Cuántos canastos hay en total?", ["Cada familia trae 6.", "Hay 8 familias.", "Multiplico 8 × 6."], "48 canastos."),
    ],
    mistakes=[
        M("Escribir la fecha de una fiesta de un pueblo real porque «seguro es en esa época».", "Es adivinar y puede ser falso.", "Pregunta la fecha y su significado al educador o a la comunidad."),
        M("Pensar que una festividad solo es diversión y no tiene relación con el trabajo.", "Muchas celebraciones se conectan con lo que la comunidad produce.", "Busca qué producción aparece en el testimonio."),
    ],
    R=[
        ex("En el testimonio de doña Rosa, ¿qué ocurre al terminar la cosecha: la comunidad se junta o cada familia se va sin compartir?", "La comunidad se junta", "El testimonio dice que se juntan en la explanada."),
        ex("¿Qué se guarda para volver a sembrar? A) semillas B) ropa", "A", "El testimonio dice que guardan semillas."),
        ex("¿Qué produce la huerta comunitaria de Valle Alto: cosecha o redes de pesca?", "Cosecha", "La huerta da lo que se cosecha."),
    ],
    C=[
        ex("¿Qué es la producción de una comunidad? A) lo que cultiva, pesca, cría o elabora B) la fecha de una fiesta", "A", "Es lo que obtiene o elabora con su territorio."),
        ex("Verdadero o falso: una festividad puede relacionarse con lo que la comunidad produce.", "Verdadero", "En el ejemplo, el encuentro sigue a la cosecha."),
        ex("Verdadero o falso: puedo escribir la fecha de una fiesta de un pueblo real sin consultar a nadie.", "Falso", "La fecha la informa la comunidad o el educador tradicional."),
    ],
    A=[
        arith("En el encuentro de Valle Alto hay 8 familias y cada una trae 6 canastos. ¿Cuántos canastos hay en total?", "8*6", "Se repite 6 canastos ocho veces."),
        arith("Los 48 canastos se reparten en partes iguales en 4 mesas. ¿Cuántos canastos hay en cada mesa?", "48//4", "Se reparte en partes iguales."),
        ex("Testimonio inventado de don Luis: «Después de la pesca grande, la caleta se junta a compartir el pescado». ¿Qué producción se comparte?", "El pescado", "El testimonio lo dice."),
    ],
    Z=[
        ex("Clara afirma: «El encuentro de Valle Alto ocurre todos los años en la misma fecha, como en todos los pueblos». ¿Qué datos agrega que el testimonio no dice?", "La fecha y que sea igual en todos los pueblos", "Ninguno de los dos aparece en la fuente."),
        ex("Si no se guardaran semillas, ¿qué dificultad habría para la próxima cosecha? A) no habría con qué volver a sembrar B) habría más canastos", "A", "Las semillas permiten sembrar de nuevo."),
    ],
    D=[
        arith("En Costa Clara (inventada), 5 familias aportan 9 cajas de pescado cada una. Todo el pescado se reparte en partes iguales en 3 mesas. ¿Cuántas cajas hay en cada mesa?", "(5*9)//3", "Primero se halla el total (5 × 9 = 45) y luego se reparte en 3 mesas."),
        ex("Dos frases: 1) «Se comparte lo cosechado» 2) «Se baila una danza especial». ¿Cuál puede escribirse como dato del testimonio de doña Rosa?", "La primera", "La segunda no está en el testimonio."),
    ],
    context=[ex("Tu curso quiere imitar el encuentro de Valle Alto con una cuenta: 6 familias, 4 canastos cada una. ¿Cuántos canastos hay? Responde con un número.", "24", "6 × 4 = 24 canastos.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es la producción.", "Lo que una comunidad cultiva, pesca, cría o elabora", "Es la definición de la clase."),
        ex("¿A quién preguntas la fecha de una festividad de un pueblo real? A) al educador tradicional o a la comunidad B) a nadie, la invento", "A", "Ellos son la fuente."),
        ex("Verdadero o falso: las celebraciones y el trabajo de una comunidad pueden estar conectados.", "Verdadero", "Es la relación que se estudia."),
    ],
    task=T("Lee este testimonio inventado de don Luis, de Costa Clara: «Cuando vuelven los botes con buena pesca, la caleta se junta en la playa. Cada familia aporta pescado y lo compartimos. Las redes se arreglan juntos para la próxima salida.» Escribe tres frases: qué se produce, cómo se comparte y qué hace la comunidad para la próxima vez. Agrega una cuenta con números propios (por ejemplo, cuántas familias y cuántas cajas) y su resultado. No escribas fechas ni inventes una celebración.",
           "Se produce pescado. Se comparte entre todas las familias de la caleta. Arreglan las redes juntos para la próxima salida. Cuenta: 4 familias × 3 cajas = 12 cajas.",
           ["usa solo datos del testimonio", "relaciona producción y encuentro", "hace una cuenta correcta"], ["tres frases", "cuenta con resultado"], ["inventar fechas o ritos", "agregar datos que el testimonio no dice"],
           "Pedir que muestre la línea del testimonio de cada frase; revisar la cuenta."),
    reinforce="Dibuja una flecha desde la producción de la huerta hasta el encuentro en la explanada.",
    extend="Escribe una pregunta que le harías a una persona de tu comunidad sobre lo que se produce en tu zona.",
)

L(
    OA7, 4,
    materials="Lápiz y hojas. Los testimonios están escritos aquí y son inventados.",
    use="Aprenderé a comunicar las conexiones entre territorio, vida espiritual y producción, y a decir también hasta dónde llega lo que sé. Sirve para presentar un trabajo respetuoso.",
    prior=["Sé describir la organización de un territorio.", "Sé relacionar territorio con espiritualidad y con producción."],
    explain=[
        "Comunicar es contar a otros lo que aprendimos de manera clara y respetuosa. Un buen informe sobre un territorio tiene tres partes: lo que cuenta la fuente, la conexión que descubrimos entre territorio, vida espiritual y producción, y los límites de lo que afirmamos.",
        "Una conexión une dos datos de la fuente, por ejemplo: «La huerta está bajo la vertiente y la comunidad agradece el agua». Cada conexión debe poder verificarse en el testimonio. Si la conexión es solo idea nuestra, se escribe como idea nuestra, con una frase como «yo pienso que».",
        "Los límites dicen qué no sabemos, qué la comunidad no cuenta y qué debemos preguntar al educador o educadora tradicional. Declarar límites no es debilidad: es honestidad y respeto. Además, el informe se devuelve a la comunidad o al educador para que revise si quedó bien.",
    ],
    vocab=[("conexión", "relación entre dos datos de la fuente"), ("límite", "lo que no se cuenta o no se sabe"), ("informe", "texto breve que cuenta lo aprendido"), ("devolución", "mostrar a la comunidad lo que se escribió para que lo revise"), ("verificar", "comprobar que algo está en la fuente")],
    worked=[
        W("Armar una conexión", "Testimonio inventado de doña Rosa: «La huerta está bajo la vertiente. El agua se agradece en silencio. Después de cosechar nos juntamos en la explanada.» Escribe una conexión.", ["Busco dos datos relacionados.", "La huerta está bajo la vertiente y el agua se agradece.", "Los junto en una frase."], "La huerta está bajo la vertiente y la comunidad agradece el agua en silencio. (Que la huerta necesite esa agua es idea mía: lo rotulo «yo pienso que».)"),
        W("Escribir un límite", "En el mismo informe, ¿qué límite puedes escribir sobre la parte espiritual?", ["El testimonio dice que se agradece el agua en silencio.", "No dice cómo ni con qué palabras.", "Eso es lo que no sé."], "No sé cómo se agradece el agua; eso lo explica la comunidad o el educador tradicional."),
    ],
    mistakes=[
        M("Escribir conexiones que no están en el testimonio.", "Una conexión sin fuente es una idea nuestra.", "Rotúlala con «yo pienso que»."),
        M("Cerrar el informe sin decir qué falta saber.", "Parece que lo sabemos todo.", "Agrega un límite y una pregunta para el educador."),
    ],
    R=[
        ex("¿Cuántas partes tiene un buen informe en esta clase? Escribe el número.", "3", "Son fuente, conexión y límites."),
        ex("¿Qué es una conexión: una relación entre dos datos de la fuente o un dato aislado?", "Una relación entre dos datos de la fuente", "Une dos datos del testimonio."),
        ex("En el testimonio de doña Rosa, ¿dónde se juntan después de cosechar?", "En la explanada", "El testimonio lo dice."),
    ],
    C=[
        ex("¿Para qué sirve escribir los límites de un informe? A) para decir lo que no sé o no se cuenta B) para llenar espacio", "A", "Los límites muestran hasta dónde llega lo afirmado."),
        ex("Verdadero o falso: una idea mía puede ir en el informe si la rotulo como «yo pienso que».", "Verdadero", "Así queda claro que no viene de la fuente."),
        ex("Verdadero o falso: una vez terminado el informe, no hace falta mostrarlo a nadie.", "Falso", "Se devuelve a la comunidad o al educador para que lo revise."),
    ],
    A=[
        ex("Dado el testimonio «El cerro es lugar de respeto. Se sube en silencio.», ¿cuál es una conexión válida? A) el cerro es lugar de respeto y se sube en silencio B) el cerro es el más alto del país", "A", "La primera une dos datos escritos."),
        ex("Clasifica en DATO DE LA FUENTE o MI IDEA: a) las redes se arreglan en las rocas planas b) creo que es un trabajo difícil.", "a dato de la fuente, b mi idea", "La primera está escrita en el testimonio; la segunda es opinión."),
        ex("Escribe un límite posible sobre el testimonio «Se agradece el agua en silencio».", "No sé cómo se agradece", "El testimonio no explica cómo se hace."),
    ],
    Z=[
        ex("Lucas escribe: «Como las casas están junto al río, el río es sagrado para ese pueblo». ¿Qué problema tiene la conexión?", "El testimonio no dice que el río sea sagrado", "Afirma algo que la fuente no dice."),
        ex("¿Por qué conviene mostrar el informe a la comunidad antes de darlo por terminado? A) para que corrijan lo que quedó mal B) para ganar tiempo", "A", "Ellos conocen su territorio y pueden corregir errores."),
    ],
    D=[
        ex("Dos informes: uno dice «el pescado se comparte y no sé cómo se reparte»; el otro dice «el pescado se reparte con una ceremonia». Testimonio de don Luis (inventado): «Después de la pesca grande, la caleta se junta a compartir el pescado.» ¿Cuál informe es más respetuoso?", "El primero", "Reconoce lo que no sabe y no inventa."),
        ex("Tu informe tiene una conexión y ningún límite. ¿Qué le falta? A) un límite o pregunta B) más adornos", "A", "Debe decir qué no se sabe o no se cuenta."),
    ],
    context=[ex("En la feria de la escuela presentarás tu informe sobre Valle Alto. Una compañera te pide agregar cómo es el sitio de respeto del cerro. Según la ficha, ¿qué respondes? A) esa parte no se cuenta B) te lo describo", "A", "El límite de la ficha lo prohíbe.")],
    selfcheck=[
        ex("Nombra las tres partes de un informe respetuoso.", "Fuente, conexión y límites", "Están en la explicación."),
        ex("¿Cómo rotulas una idea que es tuya? A) con «yo pienso que» B) como si fuera de la fuente", "A", "Así no se confunde con la fuente."),
        ex("Verdadero o falso: declarar los límites es una muestra de respeto.", "Verdadero", "Reconoce lo que no corresponde a nosotros."),
    ],
    task=T("Usa la ficha de Valle Alto: «" + FV4 + "» y el testimonio: «Las casas están junto al río. La huerta comunitaria está bajo la vertiente. Se agradece el agua en silencio. Después de cosechar nos juntamos en la explanada.» Escribe un informe corto con tres partes: 1) qué cuenta la fuente, 2) una conexión entre territorio, vida espiritual o producción y 3) dos límites. Termina con la pregunta que llevarías al educador tradicional.",
           "1) Doña Rosa cuenta que las casas están junto al río y la huerta bajo la vertiente. 2) La huerta está bajo la vertiente y la comunidad agradece el agua en silencio. 3) No sé cómo se agradece el agua; el sitio de respeto no se cuenta. Pregunta: ¿qué cuidados tiene nuestra comunidad con el agua?",
           ["incluye fuente, conexión y límites", "la conexión sale del testimonio", "declara lo que no sabe"], ["informe de tres partes", "pregunta final"], ["conexiones sin fuente", "no incluir límites"],
           "Pedir que señale la línea de donde sale la conexión; valorar que reconozca lo que falta saber."),
    reinforce="Marca con un color la conexión de tu informe y con otro los límites.",
    extend="Reescribe tu informe pensando en cómo le explicarías la devolución a doña Rosa para que lo revise.",
)

# ============================================================ OA 08 · Historia indígena, presente y futuro
L(
    OA8, 1,
    materials="Lápiz y hojas. Los testimonios están escritos aquí y son inventados.",
    use="Aprenderé a formular una pregunta histórica sobre cómo se organizaba una comunidad. Sirve para investigar con orden y respeto.",
    prior=["Sé distinguir pasado y presente.", "Sé que una fuente es quien o lo que entrega un dato."],
    explain=[
        "La historia de un pueblo incluye cómo se organizaba para tomar decisiones y vivir juntos. Eso se llama organización política y sociocomunitaria: quién decidía, cómo se juntaban y cómo se repartían las tareas. Para conocerla se parte con una buena pregunta.",
        "Una pregunta histórica se puede responder con fuentes y se refiere a un pasado concreto. Por ejemplo: «¿Cómo tomaban decisiones las familias de Valle Alto sobre el agua?». No es histórica una pregunta de opinión, como «¿qué era más bonito?», ni una que se responde con sí o no sin explicación.",
        "Una buena pregunta tiene un tema, un tiempo y una comunidad. También dice a quién se le va a preguntar o qué fuente se va a leer. Cuando es una comunidad real, la pregunta se lleva al educador o educadora tradicional o a quien la comunidad indique, con respeto.",
    ],
    vocab=[("organización sociocomunitaria", "manera en que una comunidad se junta, se reparte tareas y convive"), ("organización política", "manera en que una comunidad toma decisiones"), ("pregunta histórica", "pregunta sobre el pasado que se puede responder con fuentes"), ("fuente", "persona o texto que entrega datos"), ("memoria", "lo que una comunidad recuerda y transmite")],
    worked=[
        W("Elegir la mejor pregunta", "Para investigar Valle Alto (inventada), ¿cuál es mejor? A) «¿Era más lindo antes?» B) «¿Cómo decidían las familias de Valle Alto el uso del agua?»", ["A es de opinión.", "B tiene tema (uso del agua), comunidad y se puede responder con fuentes.", "Elijo B."], "B"),
        W("Mejorar una pregunta", "Mejora «¿Qué hacían?».", ["Falta el tema.", "Falta la comunidad.", "Agrego ambos."], "«¿Cómo se repartían las tareas de la huerta en Valle Alto?»"),
    ],
    mistakes=[
        M("Hacer una pregunta de opinión como pregunta histórica.", "Las opiniones no se comprueban con fuentes.", "Pregunta por hechos del pasado: cómo, quién, cuándo."),
        M("Preguntar por «los indígenas» en general.", "Cada pueblo y comunidad tiene su historia.", "Nombra la comunidad concreta."),
    ],
    R=[
        ex("¿Una pregunta histórica se refiere al pasado o al futuro?", "Al pasado", "Pregunta por hechos que ya ocurrieron."),
        ex("¿Cuál es una pregunta histórica? A) «¿Cómo decidían las familias de Valle Alto sobre el agua?» B) «¿Qué es más lindo?»", "A", "Se puede responder con fuentes."),
        ex("En la pregunta «¿Cómo se repartían las tareas de la huerta en Valle Alto?», ¿cuál es la comunidad?", "Valle Alto", "Es el lugar nombrado."),
    ],
    C=[
        ex("Verdadero o falso: «¿Qué comida era la más rica?» es una pregunta de opinión.", "Verdadero", "Depende de gustos y no de datos del pasado."),
        ex("¿Qué dos datos debe tener una buena pregunta histórica? A) tema y comunidad B) color y tamaño", "A", "Dice sobre qué y sobre quién se investiga."),
        ex("Verdadero o falso: para una comunidad real, la pregunta se lleva al educador o a quien la comunidad indique.", "Verdadero", "Así se respeta la fuente."),
    ],
    A=[
        ex("Valle Alto tiene huerta comunitaria y vertiente. Costa Clara tiene caleta y botes. ¿Para qué comunidad sirve la pregunta histórica «¿Cómo se turnaban los botes para salir a pescar?»", "Costa Clara", "Los botes y la pesca son de la caleta de Costa Clara."),
        ex("Clasifica en HISTÓRICA o DE OPINIÓN: a) ¿Cómo se turnaban para usar la caleta? b) ¿Cuál era el mejor bote?", "a histórica, b de opinión", "La primera busca un hecho del pasado; la segunda, una preferencia."),
        ex("Mejora la pregunta «¿Qué pasaba?» agregando comunidad y tema. Escribe una versión posible con Valle Alto.", "Por ejemplo: ¿Cómo se organizaban las familias de Valle Alto para cuidar la vertiente?", "Incluye tema y comunidad."),
    ],
    Z=[
        ex("Tomás pregunta: «¿Cómo se organizaban los pueblos indígenas?». ¿Qué problema tiene?", "Es demasiado general: mezcla todos los pueblos", "Cada pueblo tiene su propia historia."),
        ex("¿Por qué «¿Fue bonito el pasado de Costa Clara?» no sirve como pregunta histórica? A) es de opinión B) menciona el pasado", "A", "No se responde con datos de una fuente."),
    ],
    D=[
        ex("Tienes el testimonio de don Luis sobre cómo se turnaban los botes. ¿Qué pregunta se responde con ese testimonio? A) ¿Cómo se turnaban los botes en Costa Clara? B) ¿Cuántos años tiene don Luis?", "A", "El testimonio trata de los turnos."),
        ex("Una pregunta tiene tema y comunidad, pero no dice a quién preguntar. ¿Qué agregarías?", "La fuente o la persona a quien se pregunta", "Una buena pregunta indica de dónde saldrá la respuesta."),
    ],
    context=[ex("Tu curso visitará virtualmente a doña Rosa (inventada) para saber de Valle Alto. ¿Cuál pregunta llevas? A) ¿Cómo se juntaban las familias para decidir sobre el agua? B) ¿Te gusta tu casa?", "A", "Es histórica y se puede responder con su testimonio.")],
    selfcheck=[
        ex("Nombra dos datos que lleva una buena pregunta histórica.", "Tema y comunidad", "Son lo que la hace precisa."),
        ex("Verdadero o falso: una pregunta de opinión es una pregunta histórica.", "Falso", "No se responde con fuentes."),
        ex("¿A quién llevas una pregunta sobre una comunidad real? A) al educador tradicional o a quien la comunidad indique B) a un desconocido", "A", "Ellos son la fuente."),
    ],
    task=T("Lee este resumen inventado de la comunidad de Valle Alto: «Las familias comparten el agua de la vertiente y la huerta comunitaria. Se juntan en la explanada para ponerse de acuerdo.» Escribe tres preguntas históricas sobre cómo se organizaba la comunidad en el pasado: una sobre decisiones, una sobre tareas y una sobre reuniones. Subraya el tema y la comunidad en cada una.",
           "Decisiones: ¿Cómo decidían las familias de Valle Alto el uso del agua? Tareas: ¿Cómo se repartían las tareas de la huerta comunitaria? Reuniones: ¿Cómo se juntaban las familias en la explanada para ponerse de acuerdo?",
           ["escribe tres preguntas históricas", "cada una tiene tema y comunidad", "ninguna es de opinión"], ["tres preguntas escritas", "temas y comunidad subrayados"], ["preguntas de sí o no", "preguntas de opinión"],
           "Pedir que explique por qué cada pregunta se puede responder con fuentes."),
    reinforce="Convierte esta pregunta de opinión en histórica: «¿Era mejor la vida antes en Costa Clara?».",
    extend="Escribe una pregunta que llevarías al educador tradicional sobre la historia de tu zona.",
)

L(
    OA8, 2,
    materials="Lápiz y hojas. Los testimonios y el documento están escritos aquí y son inventados.",
    use="Aprenderé a leer memorias y fuentes sobre la historia de una comunidad. Sirve para saber qué dice cada fuente y qué no dice.",
    prior=["Sé formular una pregunta histórica.", "Sé que lo que dice una fuente vale para su comunidad."],
    explain=[
        "Una memoria es lo que una comunidad recuerda y se transmite de generación en generación, muchas veces hablando. Un testimonio es el relato de una persona sobre lo que vivió o aprendió. También hay documentos escritos, como actas o cartas. Todas son fuentes y sirven para responder preguntas históricas.",
        "Al leer una fuente conviene preguntar: ¿quién cuenta?, ¿de qué comunidad?, ¿qué dice?, ¿qué no dice? y ¿tiene permiso para compartirse? Dos fuentes pueden contar cosas distintas del mismo tema, y eso no significa que una esté mal: cada una tiene su punto de vista.",
        "Cuando una fuente responde solo una parte de la pregunta, anotamos lo que falta. No rellenamos los vacíos con imaginación. Si queremos completar la información de una comunidad real, volvemos al educador o educadora tradicional o a la comunidad.",
    ],
    vocab=[("memoria", "lo que una comunidad recuerda y transmite"), ("testimonio", "relato de una persona sobre lo que vivió o supo"), ("documento", "texto escrito que guarda información"), ("punto de vista", "manera en que una persona ve y cuenta algo"), ("vacío de información", "lo que la fuente no dice")],
    worked=[
        W("Interrogar una fuente", "Testimonio inventado de doña Rosa: «Cuando yo era niña, las familias se juntaban en la explanada para decidir cómo repartir el agua. Hablaba cada familia y se buscaba un acuerdo.» ¿Quién cuenta, qué dice y qué no dice?", ["Cuenta doña Rosa, de Valle Alto.", "Dice que se juntaban en la explanada y buscaban un acuerdo.", "No dice quién lideraba ni cuántas familias eran."], "Cuenta doña Rosa; dice cómo decidían el agua; no dice quién lideraba ni cuántas familias."),
        W("Comparar dos fuentes", "Un acta inventada de Valle Alto dice: «Se acordó turnar el agua entre 12 familias». ¿Qué agrega al testimonio?", ["El testimonio dice cómo decidían.", "El acta dice cuántas familias y que turnaban.", "Se complementan."], "El acta agrega el número de familias y el turno."),
    ],
    mistakes=[
        M("Pensar que si dos fuentes dicen cosas distintas, una miente.", "Cada una cuenta desde su punto de vista o sobre otra parte del tema.", "Anota las diferencias y pregunta al educador tradicional."),
        M("Rellenar con imaginación lo que la fuente no dice.", "Se mezcla lo escrito con lo inventado.", "Escribe «la fuente no dice» y deja el vacío."),
    ],
    R=[
        ex("Según el testimonio de doña Rosa, ¿dónde se juntaban las familias para decidir?", "En la explanada", "El testimonio lo dice."),
        ex("¿Cómo se decidía según ese testimonio: hablaba cada familia o decidía una sola persona?", "Hablaba cada familia", "Y se buscaba un acuerdo."),
        ex("En el acta inventada, ¿entre cuántas familias se turnaba el agua?", "12", "El acta dice 12 familias."),
    ],
    C=[
        ex("Verdadero o falso: un testimonio es el relato de una persona sobre lo que vivió o aprendió.", "Verdadero", "Es la definición de la clase."),
        ex("¿Qué haces con lo que una fuente no dice? A) escribo «la fuente no dice» B) lo invento", "A", "Los vacíos se reconocen y no se inventan."),
        ex("Verdadero o falso: si dos fuentes cuentan distinto, una de ellas necesariamente miente.", "Falso", "Pueden tener otro punto de vista o hablar de otra parte."),
    ],
    A=[
        ex("Testimonio inventado de don Luis: «Antes los pescadores se turnaban para salir. Cada familia tenía su día.» ¿Qué dice y qué no dice? Escribe un dato que no dice.", "Por ejemplo: cuántas familias eran o cuántos días había", "El testimonio no da esos datos."),
        arith("El acta dice que 12 familias se turnan el agua y cada una tiene 2 turnos al mes. ¿Cuántos turnos hay en el mes entre todas?", "12*2", "Se multiplica el número de familias por los turnos de cada una."),
        ex("Une cada pregunta con la fuente que la responde mejor. 1) ¿Cuántas familias eran? 2) ¿Cómo hablaban en la explanada? a) acta b) testimonio de doña Rosa", "1-a, 2-b", "El acta da el número; doña Rosa cuenta cómo se hablaba."),
    ],
    Z=[
        ex("Julia dice: «Doña Rosa dijo que decidía una sola persona». Según su testimonio, ¿es correcto? Responde Sí o No.", "No", "El testimonio dice que cada familia hablaba y se buscaba un acuerdo."),
        ex("Dos testimonios sobre la misma comunidad cuentan distinto el mismo hecho. ¿Qué haces? A) anotar ambos y preguntar al educador tradicional B) elegir el que más me gusta", "A", "Se respetan ambas voces y se consulta."),
    ],
    D=[
        ex("Un cuaderno de la escuela, escrito por un adulto que no es de la comunidad, dice que en Valle Alto decidía una sola persona. El testimonio de doña Rosa dice otra cosa. ¿Qué fuente es más cercana a la comunidad?", "El testimonio de doña Rosa", "Ella es de la comunidad y habla de su experiencia."),
        ex("¿Por qué conviene saber quién cuenta una fuente antes de usarla? A) porque define desde qué experiencia habla B) porque así se ve más largo el trabajo", "A", "Quien cuenta influye en lo que dice."),
    ],
    context=[ex("Quieres saber cuántos turnos de agua hay en Valle Alto. El testimonio de doña Rosa y el acta aportan datos distintos. ¿Qué fuente miras primero para el número? A) el acta B) el testimonio", "A", "El acta tiene el número de familias y turnos.")],
    selfcheck=[
        ex("Escribe dos preguntas que haces al leer una fuente.", "Por ejemplo: ¿quién cuenta? y ¿qué no dice?", "Son parte de la lectura crítica."),
        ex("Verdadero o falso: se pueden completar los vacíos de una fuente con imaginación.", "Falso", "Se anotan como vacíos."),
        ex("Si dos fuentes cuentan distinto, ¿qué es lo más respetuoso? A) anotar las dos y consultar B) borrar una", "A", "Respeta ambos puntos de vista."),
    ],
    task=T("Lee dos fuentes inventadas de Costa Clara. Testimonio de don Luis: «Antes los botes salían por turnos. Cada familia tenía su día y se respetaba.» Acta: «Se acordó que cada familia sale un día a la semana.» Haz un cuadro con cuatro filas: quién cuenta, qué dice, qué no dice y qué se complementa. Escribe una pregunta que llevarías al educador tradicional.",
           "Quién cuenta: don Luis y un acta. Dice: los botes salían por turnos y cada familia un día a la semana. No dice: cuántas familias eran. Se complementa: don Luis cuenta cómo era y el acta cuántos días. Pregunta: ¿cómo se acordaban los turnos en nuestra zona?",
           ["completa las cuatro filas con datos de las fuentes", "reconoce vacíos de información", "formula una pregunta respetuosa"], ["cuadro de cuatro filas", "pregunta escrita"], ["rellenar los vacíos con imaginación", "decir que una fuente miente"],
           "Pedir que señale en qué fuente está cada dato; valorar que reconozca el vacío."),
    reinforce="Subraya en el testimonio de doña Rosa quién cuenta y qué cuenta, cada uno con un color.",
    extend="Escribe una razón por la cual dos personas de la misma comunidad pueden recordar algo de distinta manera.",
)

L(
    OA8, 3,
    materials="Lápiz y hojas. Los testimonios están escritos aquí y son inventados.",
    use="Aprenderé a reconocer qué cambió y qué continúa en la organización de una comunidad entre el pasado y hoy. Sirve para comprender que la cultura es dinámica y no se pierde cuando algo cambia.",
    prior=["Sé leer una fuente y reconocer sus vacíos.", "Sé que los pueblos originarios viven hoy."],
    explain=[
        "Un cambio es algo que antes era de una manera y hoy es distinto. Una continuidad es algo que se mantiene igual o casi igual a través del tiempo. En la organización de una comunidad hay cambios y continuidades al mismo tiempo, y ambos son parte de su historia.",
        "Que algo cambie no significa que la cultura se haya perdido. Una comunidad puede usar herramientas nuevas, como un cuaderno de actas o un teléfono, y mantener lo que valora, como decidir entre todos. Por eso se pregunta siempre: ¿qué cambió?, ¿qué continúa? y ¿qué dice la comunidad sobre eso?",
        "Para reconocerlos, compara el antes y el hoy en una tabla de dos columnas. Escribe los verbos en presente cuando hables de la comunidad actual: viven, cuidan, se juntan. Así recordamos que los pueblos originarios existen hoy y no solo en el pasado.",
    ],
    vocab=[("cambio", "algo que antes era de una manera y hoy es distinto"), ("continuidad", "algo que se mantiene a través del tiempo"), ("acuerdo", "decisión a la que llegan varias personas"), ("acta", "documento que anota lo acordado en una reunión"), ("cultura dinámica", "cultura que cambia y se renueva sin perderse")],
    worked=[
        W("Comparar antes y hoy", "Relato inventado de Valle Alto: «Antes las familias se juntaban en la explanada y decidían hablando. Hoy se juntan en la sede, siguen decidiendo entre todos y anotan los acuerdos en un cuaderno.» ¿Qué cambió y qué continúa?", ["Cambió el lugar (de explanada a sede) y se anota en un cuaderno.", "Continúa que las familias deciden entre todos.", "Separo en dos columnas."], "Cambió el lugar y el registro; continúa decidir entre todos."),
        W("Cuidar el verbo", "¿Qué problema hay en «Los habitantes de Valle Alto se juntaban en la explanada»?", ["El verbo está en pasado.", "Parece que hoy ya no ocurre.", "Hay que decir qué se mantiene hoy."], "Habla solo en pasado; debe decir también lo que ocurre hoy."),
    ],
    mistakes=[
        M("Pensar que si algo cambió, la cultura se perdió.", "Las comunidades cambian herramientas y mantienen lo que valoran.", "Pregunta qué continúa."),
        M("Hablar de una comunidad solo en pasado.", "Parece que dejó de existir.", "Usa el presente: «viven», «cuidan», «se juntan»."),
    ],
    R=[
        ex("Antes decidían hablando en la explanada. Hoy anotan los acuerdos en un cuaderno. ¿Anotar en un cuaderno es un cambio o una continuidad?", "Un cambio", "Antes no se anotaba en un cuaderno."),
        ex("La comunidad de Valle Alto sigue decidiendo entre todos. ¿Eso es un cambio o una continuidad?", "Una continuidad", "Se mantiene a través del tiempo."),
        ex("¿Dónde se juntan hoy las familias de Valle Alto según el relato: en la sede o en la explanada?", "En la sede", "Antes era la explanada."),
    ],
    C=[
        ex("Verdadero o falso: si una comunidad usa un cuaderno de actas, ya perdió su cultura.", "Falso", "Puede cambiar herramientas y mantener lo que valora."),
        ex("¿Qué es una continuidad? A) algo que se mantiene B) algo que desapareció para siempre", "A", "Es lo que sigue a través del tiempo."),
        ex("Verdadero o falso: una comunidad indígena de hoy puede usar cosas nuevas, como un teléfono, y seguir cuidando lo que valora.", "Verdadero", "Viven hoy y pueden usar lo que hay hoy."),
    ],
    A=[
        ex("Clasifica en CAMBIO o CONTINUIDAD: a) antes se juntaban en la explanada y hoy en la sede b) siguen decidiendo entre todos c) hoy se anota lo acordado en un cuaderno.", "a cambio, b continuidad, c cambio", "Lugar y registro cambian; decidir entre todos continúa."),
        ex("Relato inventado de Costa Clara: «Antes los botes eran de madera y hoy tienen motor. Seguimos saliendo por turnos.» ¿Qué continúa?", "Salir por turnos", "Es lo que se mantiene."),
        ex("En el relato anterior, ¿qué cambió? A) los botes, que hoy tienen motor B) el sistema de turnos", "A", "Los turnos siguen; los botes cambiaron."),
    ],
    Z=[
        ex("Ema dice: «Antes se juntaban en la explanada y hoy ya no se juntan». El relato dice que hoy se juntan en la sede. ¿Quién tiene razón?", "El relato", "Hoy se juntan en otro lugar."),
        ex("Pedro quiere contar cómo es la comunidad de Valle Alto hoy y escribe: «Las familias de Valle Alto decidían entre todos». ¿Qué problema tiene el verbo?", "Habla en pasado como si ya no ocurriera", "Debe reflejar lo que ocurre hoy."),
    ],
    D=[
        ex("Una niña de Valle Alto usa el computador para anotar actas y también escucha a su abuela contar cómo decidían antes. ¿Qué muestra esto: cambio, continuidad o ambas?", "Ambas", "Hay herramientas nuevas y una memoria que se mantiene."),
        ex("Para saber qué cambió de verdad en una comunidad real, ¿a quién consultas? A) a la comunidad o al educador tradicional B) a un video cualquiera", "A", "Ellos son la fuente confiable."),
    ],
    context=[ex("Un compañero dice: «La cultura de Valle Alto se perdió porque ahora anotan en cuaderno». Según el relato, ¿qué le respondes? A) que siguen decidiendo entre todos B) que tiene razón", "A", "Eso continúa aunque cambie el registro.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es un cambio.", "Algo que antes era de una manera y hoy es distinto", "Es la definición de la clase."),
        ex("Verdadero o falso: los pueblos originarios solo existieron en el pasado.", "Falso", "Los pueblos viven hoy."),
        ex("¿Qué haces para saber qué cambió en una comunidad real? A) pregunto a la comunidad B) lo adivino", "A", "La comunidad es la fuente."),
    ],
    task=T("Lee este relato inventado de Costa Clara: «Antes, el reparto del pescado se anunciaba en la playa. Hoy se avisa también por mensaje de teléfono. Seguimos repartiendo entre todas las familias.» Haz un cuadro de dos columnas: «Cambió» y «Continúa». Escribe dos frases en presente sobre la comunidad y una pregunta para el educador tradicional.",
           "Cambió: ahora se avisa también por mensaje de teléfono. Continúa: se reparte el pescado entre todas las familias. Frases: La comunidad de Costa Clara usa el teléfono para avisar. Las familias reparten el pescado entre todas. Pregunta: ¿qué costumbres de nuestra comunidad continúan hoy?",
           ["separa un cambio y una continuidad", "usa el presente", "formula una pregunta respetuosa"], ["cuadro de dos columnas", "dos frases", "pregunta"], ["escribir todo en pasado", "decir que la cultura se perdió"],
           "Valorar el uso del presente; preguntar por qué la continuidad es importante."),
    reinforce="Pinta de verde lo que continúa y de rojo lo que cambió en el relato de Costa Clara.",
    extend="Escribe un cambio y una continuidad que veas en la organización de tu curso o de tu familia.",
)

L(
    OA8, 4,
    materials="Lápiz y hojas. El relato está escrito aquí y es inventado.",
    use="Aprenderé a vincular la historia de una comunidad con su presente y con el futuro que ella desea. Sirve para valorar por qué la historia importa hoy.",
    prior=["Sé reconocer cambios y continuidades.", "Sé que cada comunidad decide su futuro."],
    explain=[
        "La historia de una comunidad ayuda a entender su presente. Si sabemos cómo se decidía antes, entendemos por qué hoy se decide de cierta manera. El pasado explica una parte de lo que ocurre hoy, aunque no lo explica todo.",
        "El futuro es lo que una comunidad desea para después. Puede querer, por ejemplo, seguir decidiendo entre todos o enseñar a las nuevas generaciones, pero eso lo dice cada comunidad. El futuro lo construyen las personas con lo que hacen hoy, y nosotros escuchamos sin decidir por ellos.",
        "Para vincular pasado, presente y futuro usamos una línea de tiempo con tres partes: antes, hoy y mañana. Cada parte debe salir de la fuente. Luego escribimos una frase que explica cómo se conectan. Así vemos que la historia no queda atrás: se continúa en lo que hacemos.",
    ],
    vocab=[("futuro", "lo que ocurrirá después"), ("línea de tiempo", "dibujo que ordena sucesos desde antes hasta después"), ("generación", "grupo de personas de edades parecidas"), ("deseo", "lo que alguien quiere lograr"), ("vincular", "unir dos cosas mostrando su relación")],
    worked=[
        W("Armar una línea de tiempo", "Relato inventado de Valle Alto: «Mis abuelos decidían sobre el agua reunidos en la explanada. Hoy mis papás y vecinos lo hacen en la sede. Mañana queremos que los jóvenes participen en las reuniones.» Ordena en antes, hoy y mañana.", ["Antes: los abuelos decidían en la explanada.", "Hoy: se decide en la sede.", "Mañana: se desea que participen los jóvenes."], "Antes explanada, hoy sede, mañana participación de jóvenes."),
        W("Explicar el vínculo", "¿Cómo se conecta lo que hacían los abuelos con lo que se desea para mañana?", ["Los abuelos decidían reunidos.", "Hoy se mantiene la reunión.", "Mañana se quiere que más personas participen."], "Se mantiene la costumbre de decidir reunidos y se desea que participen los jóvenes."),
    ],
    mistakes=[
        M("Decidir qué futuro debe tener una comunidad real.", "Eso lo decide la propia comunidad.", "Escucha lo que desea y no decidas por ella."),
        M("Poner solo el pasado en la línea de tiempo.", "Falta lo que ocurre hoy y lo que se desea.", "Incluye antes, hoy y mañana."),
    ],
    R=[
        ex("En el relato de Valle Alto, ¿dónde decidían los abuelos sobre el agua?", "En la explanada", "El relato lo dice."),
        ex("¿Dónde se decide hoy según el relato? A) en la sede B) en la plaza de otra ciudad", "A", "Hoy lo hacen en la sede."),
        ex("¿Quiénes desean participar mañana en las reuniones según el relato?", "Los jóvenes", "El relato dice que los jóvenes participen."),
    ],
    C=[
        ex("Verdadero o falso: el pasado no tiene ninguna relación con el presente.", "Falso", "El pasado explica una parte del presente."),
        ex("¿Quién dice qué desea para su futuro una comunidad real? A) la propia comunidad B) cualquier visitante", "A", "Ella decide su futuro."),
        ex("¿Cuántas partes tiene la línea de tiempo de esta clase? Escribe el número.", "3", "Son antes, hoy y mañana."),
    ],
    A=[
        ex("Ordena de antes a mañana: a) los jóvenes participarán b) los abuelos decidían en la explanada c) hoy se decide en la sede. Escribe las letras.", "b, c, a", "Primero los abuelos, luego hoy, después el deseo de mañana."),
        ex("Relato inventado de Costa Clara: «Antes los abuelos contaban cómo repartir el pescado. Hoy lo anotamos en un cuaderno.» Completa: hoy el reparto se anota en un ___. Escribe la palabra.", "cuaderno", "El relato lo dice."),
        ex("Escribe una frase que una el pasado con el presente: los abuelos decidían reunidos y hoy se decide en la sede.", "Antes y hoy se decide reunidos", "Une los dos tiempos con la misma idea."),
    ],
    Z=[
        ex("Mateo dice: «Como el pueblo es del pasado, no necesita futuro». ¿Qué error comete?", "Cree que el pueblo es del pasado", "Los pueblos viven hoy y construyen su futuro."),
        ex("Ana propone qué debería querer una comunidad real para su futuro. ¿Qué debe hacer primero? A) preguntar a la comunidad B) decidir ella", "A", "La comunidad decide lo que desea."),
    ],
    D=[
        ex("Dos frases: 1) «Mañana queremos que los jóvenes participen» 2) «Mañana nadie decidirá nada». ¿Cuál sale del relato de Valle Alto?", "La primera", "La segunda no aparece en el relato."),
        ex("En el relato, ¿qué idea aparece en los tres tiempos? A) reunirse para decidir B) cambiar la sede", "A", "Se mantiene en antes, hoy y mañana."),
    ],
    context=[ex("Tu curso hará una línea de tiempo con el relato de Valle Alto. ¿Qué tres títulos pones? A) antes, hoy y mañana B) rojo, azul y verde", "A", "Esos títulos ordenan los tiempos.")],
    selfcheck=[
        ex("Escribe las tres partes de la línea de tiempo.", "Antes, hoy y mañana", "Ordenan pasado, presente y futuro."),
        ex("Verdadero o falso: yo puedo decidir qué futuro debe tener una comunidad real.", "Falso", "Lo decide la comunidad."),
        ex("¿Para qué sirve conocer la historia de una comunidad? A) para entender mejor su presente B) para olvidarla", "A", "La historia explica una parte del presente."),
    ],
    task=T("Lee este relato inventado de Costa Clara: «Mi abuelo se reunía con los pescadores en la playa para decidir los turnos. Hoy decidimos en la sede y anotamos. Mañana queremos que los niños aprendan a cuidar el mar.» Dibuja una línea de tiempo con tres recuadros: antes, hoy y mañana. Debajo escribe una frase que explique cómo se conectan y una pregunta para el educador tradicional. No decidas tú qué futuro debe tener la comunidad.",
           "Antes: mi abuelo decidía los turnos en la playa. Hoy: decidimos en la sede y anotamos. Mañana: queremos que los niños cuiden el mar. Conexión: siempre se decide reunidos y se desea que los niños participen. Pregunta: ¿qué desea nuestra comunidad para mañana?",
           ["completa los tres recuadros con datos del relato", "explica la conexión", "formula una pregunta respetuosa"], ["línea de tiempo", "frase de conexión", "pregunta"], ["dejar vacío «mañana»", "decidir por la comunidad"],
           "Preguntar cómo une el relato los tres tiempos; valorar la pregunta final."),
    reinforce="Completa una línea de tiempo con un cambio de tu escuela: antes, hoy y mañana.",
    extend="Escribe dos deseos de futuro que una comunidad podría tener, rotulándolos como ejemplos inventados.",
)

L(
    OA8, 5,
    materials="Lápiz y hojas. Los testimonios están escritos aquí y son inventados.",
    use="Aprenderé a aplicar lo aprendido sobre historia en una comunidad distinta, sin copiar ni generalizar. Sirve para comprobar que mi método funciona con otra fuente.",
    prior=["Sé formular preguntas históricas, leer fuentes y reconocer cambios y continuidades.", "Sé armar una línea de tiempo."],
    explain=[
        "Transferir es usar lo aprendido en una situación nueva. Hasta aquí estudiamos cómo se organizaba Valle Alto. Ahora aplicamos los mismos pasos a otra comunidad, Costa Clara. Los pasos son los mismos, pero las respuestas serán distintas porque cada comunidad tiene su propia historia.",
        "Los pasos son cuatro: hacer una pregunta histórica, leer la fuente y sus vacíos, comparar antes y hoy para ver qué cambió y qué continúa, y escribir qué desea la comunidad para mañana. Si una respuesta de Valle Alto aparece también en Costa Clara, no es porque sea igual: hay que comprobar que la fuente lo diga.",
        "También cuidamos que no se mezclen las fuentes ni se jerarquice: ninguna comunidad es mejor o más tradicional que otra. Comparar sirve para ver diferencias y semejanzas con respeto. Y cuando se trata de una comunidad real, el educador o educadora tradicional es quien guía.",
    ],
    vocab=[("transferir", "usar lo aprendido en una situación nueva"), ("comparar", "mirar semejanzas y diferencias"), ("generalizar", "decir que algo vale para todos"), ("jerarquizar", "ordenar de mejor a peor"), ("guía", "persona que orienta y enseña")],
    worked=[
        W("Aplicar los pasos", "Testimonio inventado de don Luis: «Antes los botes salían por turnos y cada familia tenía su día. Hoy usamos una pizarra en la sede donde anotamos el turno. Mañana queremos que los niños aprendan a organizar los turnos.» Aplica los cuatro pasos.", ["Pregunta: ¿cómo se organizaban los turnos en Costa Clara?", "Cambió: ahora se anota en una pizarra. Continúa: hay turnos por familia.", "Mañana: se desea que los niños aprendan a organizarlos."], "Pregunta histórica, cambio y continuidad, y deseo de futuro salen del testimonio."),
        W("No generalizar", "Una niña dice: «Como en Valle Alto se decide en reunión, en Costa Clara también». ¿Es válido?", ["Reviso el testimonio de Costa Clara.", "Habla de turnos por familia y una pizarra.", "No menciona reuniones."], "No es válido hasta que la fuente lo diga."),
    ],
    mistakes=[
        M("Copiar las respuestas de Valle Alto en el trabajo de Costa Clara.", "Cada comunidad tiene su propia historia.", "Lee la fuente nueva y escribe solo lo que dice."),
        M("Decir que una comunidad es más tradicional que otra.", "Es jerarquizar y no hay base para hacerlo.", "Compara sin ordenar de mejor a peor."),
    ],
    R=[
        ex("Según don Luis, ¿qué tenía cada familia antes en Costa Clara?", "Su día de salida", "El testimonio dice que cada familia tenía su día."),
        ex("¿Qué usan hoy en la sede para anotar el turno: una pizarra o un computador?", "Una pizarra", "El testimonio lo dice."),
        ex("¿Qué desean mañana los pescadores del testimonio? A) que los niños aprendan a organizar los turnos B) que se acaben los turnos", "A", "Eso dice el testimonio."),
    ],
    C=[
        ex("¿Qué significa transferir? A) usar lo aprendido en una situación nueva B) copiar sin leer", "A", "Es aplicar los pasos en otro caso."),
        ex("Verdadero o falso: lo que sirve para Valle Alto es necesariamente cierto en Costa Clara.", "Falso", "Cada comunidad tiene su historia."),
        ex("Verdadero o falso: comparar dos comunidades es decir cuál es mejor.", "Falso", "Comparar es ver semejanzas y diferencias, sin ordenar de mejor a peor."),
    ],
    A=[
        ex("Escribe una pregunta histórica con el tema «turnos» y la comunidad Costa Clara.", "¿Cómo se organizaban los turnos de salida en Costa Clara?", "Lleva tema y comunidad."),
        ex("Clasifica según el testimonio de don Luis, en CAMBIO o CONTINUIDAD: a) hoy se anota en una pizarra b) cada familia tiene su turno.", "a cambio, b continuidad", "El registro cambió; el turno por familia continúa."),
        ex("Completa la línea de tiempo con el testimonio: Antes, ___; hoy, se anota en una pizarra; mañana, los niños aprenderán a organizar turnos. Escribe qué va en «antes».", "los botes salían por turnos", "Es el dato de antes del testimonio."),
    ],
    Z=[
        ex("Ignacio escribe: «En Costa Clara se decide en reuniones en la explanada». ¿De qué comunidad toma el dato?", "De Valle Alto", "La explanada aparece en la ficha de Valle Alto."),
        ex("¿Qué haces si una respuesta de Valle Alto parece servir en Costa Clara? A) compruebo que la fuente de Costa Clara lo diga B) la copio igual", "A", "Cada fuente vale para su comunidad."),
    ],
    D=[
        ex("Dos frases: 1) «Ambas comunidades hablan de turnos o acuerdos, y cada una los organiza a su manera» 2) «Costa Clara es más tradicional que Valle Alto». ¿Cuál compara sin jerarquizar?", "La primera", "La segunda ordena de mejor a peor."),
        ex("¿A quién consultas para saber la historia de una comunidad real de tu zona? A) al educador tradicional o a la comunidad B) a una página al azar", "A", "Son las fuentes que corresponden."),
    ],
    context=[ex("Te piden presentar la historia de Costa Clara sin mezclarla con Valle Alto. ¿Qué compruebas en cada frase? A) que salga del testimonio de Costa Clara B) que suene bonita", "A", "Cada dato debe tener fuente.")],
    selfcheck=[
        ex("Nombra los cuatro pasos para estudiar la historia de una comunidad.", "Pregunta histórica, leer la fuente, cambio y continuidad, deseo de futuro", "Son los pasos de la clase."),
        ex("Verdadero o falso: puedo copiar las respuestas de una comunidad en otra.", "Falso", "Cada comunidad tiene su historia."),
        ex("¿Por qué no se debe jerarquizar a las comunidades? A) porque ninguna es mejor que otra B) porque es difícil", "A", "Cada una es valiosa a su manera."),
    ],
    task=T("Lee este testimonio inventado de don Luis, de Costa Clara: «Antes, la caleta se organizaba para limpiar la playa después de cada marea grande. Hoy usamos carretillas para sacar los desechos. Seguimos limpiando juntos. Mañana queremos que todos los niños participen.» Aplica los cuatro pasos: una pregunta histórica, un dato que cambió, un dato que continúa y un deseo de futuro. Agrega una frase que compare con Valle Alto sin decir cuál es mejor.",
           "Pregunta: ¿cómo se organizaban para limpiar la playa en Costa Clara? Cambió: hoy usan carretillas. Continúa: limpian juntos. Mañana: que todos los niños participen. Comparación: en Valle Alto se organizan para el agua y en Costa Clara para la playa, y en ambas actúan juntos.",
           ["aplica los cuatro pasos con datos de la fuente", "compara sin jerarquizar", "no copia datos de Valle Alto"], ["cuatro respuestas", "frase comparativa"], ["copiar datos de otra comunidad", "decir cuál comunidad es mejor"],
           "Pedir que muestre la línea del testimonio de cada dato; valorar que compare sin jerarquizar."),
    reinforce="Escribe qué dato de Valle Alto no puedes usar para Costa Clara y por qué.",
    extend="Elige una situación de tu escuela y aplica los cuatro pasos: pregunta, fuente, cambio y continuidad, y deseo de futuro.",
)
