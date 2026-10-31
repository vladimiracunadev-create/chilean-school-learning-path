"""Cuaderno del estudiante, 6.º básico Lenguaje y Comunicación: OA 24 (comprensión de textos orales).

Todos los guiones son originales y breves (una persona de tu casa puede leerlos en voz alta); cada ejercicio trae el guion que necesita.
Nota: los títulos de las clases del currículo son genéricos; este cuaderno sigue el OA oficial y organiza las clases por contenido.
"""
from __future__ import annotations

from student_lessons import ex, register

OA24 = "LE06 OA 24"
E = ex


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, tiers, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers=dict(zip(("recovery", "understand", "apply", "reason", "challenge"), tiers)),
        context=ctx, selfcheck=sc, open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )


AGUA = "«Explicación oral: el ciclo del agua. El agua de los mares, los ríos y los lagos se calienta con el sol y se evapora, es decir, pasa a vapor. El vapor sube, se enfría y forma nubes. Cuando las gotas de las nubes son muy pesadas, caen como lluvia o nieve. Luego el agua vuelve a los ríos y al mar, y el ciclo comienza otra vez.»"
POROTO = "«Instrucciones orales: cómo hacer germinar un poroto. Primero, humedece un algodón con un poco de agua. Segundo, coloca el poroto sobre el algodón dentro de un vaso plástico. Tercero, deja el vaso cerca de una ventana con luz. Cuarto, humedece el algodón cada día.»"
NOTICIA = "«Noticia escolar: esta mañana, el 6.º básico inauguró la biblioteca de aula con 120 libros donados por las familias. La actividad comenzó a las 10:00 y participaron 28 estudiantes.»"
ENTREVISTA = "«Entrevista. Periodista: ¿Desde cuándo existe la huerta del colegio? Profesora: Desde hace dos años. Periodista: ¿Qué cultivan? Profesora: Lechugas, zanahorias y cilantro.»"
TESTIMONIO = "«Testimonio: Soy Rosa y vivo en este barrio hace cuarenta años. Recuerdo que la plaza no tenía árboles. Hoy, gracias al trabajo de los vecinos, da sombra a todos.»"

# ================================================================ OA 24 · clase 1
L(OA24, 1,
  "Este cuaderno, lápiz y una hoja. Una persona de tu casa puede leerte cada guion en voz alta, despacio. Si estás solo, léelos como si los escucharas.",
  "Aprenderé a reconocer qué tipo de texto oral escucho (explicación, instrucciones, noticia, entrevista, testimonio) y para qué sirve. Sirve para escuchar con un objetivo y relacionar lo que oigo con lo que ya sé.",
  ["Sé escuchar sin interrumpir.", "Sé qué significa informar y explicar."],
  ["Los textos orales se escuchan y no se leen. Hay explicaciones, que ayudan a comprender cómo ocurre algo; instrucciones, que dan pasos para hacer algo; noticias, que cuentan un hecho reciente; entrevistas, donde un periodista pregunta y otra persona responde; y testimonios, donde alguien cuenta lo que vivió. Cada uno tiene un propósito distinto.",
   "Antes de escuchar, pregúntate qué sabes del tema. Eso se llama conocimientos previos y te ayuda a entender mejor. Si escuchas sobre el ciclo del agua, recordar cómo se seca un charco al sol te ayuda a entender qué es evaporarse. Mientras escuchas, busca el propósito: ¿me explican, me dan pasos, me cuentan un hecho?",
   "Para disfrutar y aprender de un texto oral, escúchalo hasta el final, atiende las palabras que marcan el orden («primero», «luego») y los datos importantes (números, nombres, lugares). Al terminar, comprueba si entendiste el propósito y qué relación tiene con tu experiencia."],
  [("texto oral", "texto que se comunica hablando"), ("explicación", "texto que ayuda a comprender cómo o por qué ocurre algo"), ("instrucciones", "texto con pasos para hacer algo"), ("noticia", "texto que informa un hecho reciente"), ("testimonio", "relato de lo que una persona vivió"), ("conocimientos previos", "lo que ya sé sobre un tema")],
  [("Tipo y propósito", f"Escucha: {AGUA} ¿Qué tipo de texto es y para qué sirve?", ["Veo que explica cómo ocurre algo.", "No da pasos para hacer algo.", "Es una explicación que ayuda a comprender un proceso."], "Es una explicación; ayuda a comprender el ciclo del agua."),
   ("Conocimientos previos", "En la explicación del agua se dice que el agua «se evapora». ¿Qué experiencia tuya te ayuda a entender esa palabra?", ["Pienso en un charco que desaparece al sol.", "El agua no se fue al suelo, pasó al aire.", "Con eso entiendo evaporar."], "Ver cómo se seca un charco al sol.")],
  [("Escuchar sin pensar en el propósito.", "Se pierde qué quiere lograr el texto.", "Pregúntate si explican, instruyen, informan o cuentan."),
   ("No usar lo que ya sé.", "Entender es más difícil.", "Relaciona lo que oyes con tu experiencia.")],
  ([E(f"Escucha: {AGUA} ¿Qué tipo de texto oral es: explicación, noticia o instrucciones?", "Explicación", "Explica cómo ocurre un proceso."),
    E(f"Escucha: {POROTO} ¿Qué tipo de texto oral es: instrucciones, noticia o testimonio?", "Instrucciones", "Da pasos ordenados para hacer algo."),
    E(f"Escucha: {NOTICIA} ¿Qué hecho se informa?", "La inauguración de la biblioteca de aula", "Lo dice el texto.")],
   [E(f"Escucha: {AGUA} ¿Para qué se escucha este texto: para comprender cómo ocurre un proceso o para reírse?", "Para comprender cómo ocurre un proceso", "Es el propósito de una explicación."),
    E(f"Escucha: {POROTO} ¿Qué palabras marcan el orden de los pasos?", "Primero, segundo, tercero y cuarto", "Indican la secuencia."),
    E(f"Escucha: {TESTIMONIO} ¿Cómo sabes que es un testimonio: porque Rosa cuenta lo que vivió o porque da pasos?", "Porque Rosa cuenta lo que vivió", "Un testimonio relata una experiencia personal.")],
   [E(f"Escucha: {NOTICIA} ¿Cuántos libros se donaron?", "120", "Es el dato numérico de la donación."),
    E(f"Escucha: {ENTREVISTA} ¿Quién responde las preguntas: la profesora o el periodista?", "La profesora", "El periodista pregunta."),
    E(f"Escucha: {ENTREVISTA} ¿Qué cultivan en la huerta?", "Lechugas, zanahorias y cilantro", "Lo dice la profesora.")],
   [E(f"Escucha: {POROTO} Ana dice que el propósito es entretener. ¿Tiene razón?", "No", "El propósito es dar instrucciones."),
    E(f"Escucha: {NOTICIA} ¿Qué datos de tiempo entrega: «esta mañana» y «las 10:00» o «ayer» y «las 5:00»?", "«Esta mañana» y «las 10:00»", "Son los que dice el texto.")],
   [E("Escuchas: «Cuando llegué a este barrio no había luz en las calles». ¿Qué tipo de texto es: un testimonio o unas instrucciones?", "Un testimonio", "Alguien cuenta lo que vivió."),
    E("Escuchas: «Mañana la temperatura bajará a 4 grados; se recomienda abrigarse». ¿Cuál es el propósito: informar para tomar precauciones o contar un cuento?", "Informar para tomar precauciones", "Anuncia un hecho y recomienda actuar.")]),
  [E("Vas a escuchar una explicación sobre el ciclo del agua y sabes que los charcos desaparecen cuando sale el sol. ¿Qué conocimiento previo te sirve: ese hecho o el nombre de tu profesor?", "Ese hecho", "Se relaciona con evaporar.")],
  [E("En Lenguaje: ¿Qué tipo de texto da pasos para hacer algo?", "Instrucciones", "Su propósito es guiar una acción."),
   E("En Lenguaje: ¿Qué son los conocimientos previos?", "Lo que ya sé sobre un tema", "Ayudan a comprender."),
   E("¿Qué tipo de texto cuenta un hecho reciente?", "Una noticia", "Informa lo que ocurrió.")],
  ("Pide a una persona que te lea este guion y escribe tipo de texto, propósito, un conocimiento previo tuyo y dos datos importantes: «Noticia radial: el domingo, 40 vecinos limpiaron la ribera del río durante dos horas. Recogieron 15 bolsas de basura. La alcaldía agradeció su ayuda».",
   "Tipo: noticia. Propósito: informar un hecho reciente. Conocimiento previo: sé que la basura contamina el agua. Datos: 40 vecinos y 15 bolsas.",
   ["identifica tipo y propósito", "relaciona con lo que sabe", "extrae dos datos"], ["cuatro respuestas"], ["confundir noticia con testimonio", "no incluir datos"],
   "Pide que muestre dónde escuchó cada dato."),
  "Escucha una noticia de la radio o la tele y anota qué tipo de texto es.",
  "Inventa un guion de cuatro oraciones de explicación sobre algo que sabes.")

# ================================================================ OA 24 · clase 2
PING = "«Documental: el pingüino de Humboldt. El pingüino de Humboldt vive en las costas de Chile y Perú. Mide unos 65 centímetros y pesa cerca de 4 kilogramos. Se alimenta de peces pequeños, como la sardina y la anchoveta. Anida en cuevas o en huecos entre las rocas. Para protegerlo, es importante no acercarse a sus nidos.»"
L(OA24, 2,
  "Este cuaderno, lápiz y una hoja. Una persona de tu casa puede leerte el guion en voz alta. Anota mientras escuchas.",
  "Aprenderé a extraer y registrar la información relevante de un texto oral con apuntes breves. Sirve para recordar lo importante después de escuchar.",
  ["Sé reconocer el tipo de texto oral.", "Sé que hay palabras clave."],
  ["Tomar apuntes es escribir lo importante mientras escuchas. No se anota todo: se anotan las palabras clave (sustantivos y verbos importantes), los números, los nombres y los lugares. Para anotar rápido, usa abreviaturas («cm» por centímetros, «aprox.» por aproximadamente) y flechas o guiones.",
   "Un buen apunte se organiza en categorías. En el documental del pingüino puedes tener cuatro: dónde vive, cómo es, qué come y dónde anida. Escribir cada categoría con un dato la hace más clara que copiar frases completas. Si no alcanzas, deja un espacio y pregunta después.",
   "Después de escuchar, relee tus apuntes y completa lo que falta. Comprueba que los números y los nombres están bien escritos. Con tus apuntes deberías poder responder preguntas sobre el texto sin volver a escucharlo."],
  [("apuntes", "notas breves que escribo al escuchar"), ("palabra clave", "palabra que contiene la idea importante"), ("abreviatura", "forma corta de escribir una palabra"), ("categoría", "grupo de datos del mismo tipo"), ("información relevante", "información importante para el objetivo"), ("dato", "información precisa, como un número")],
  [("Armar apuntes", f"Escucha: {PING} Escribe apuntes breves.", ["Elijo categorías: dónde vive, tamaño, alimentación, nido.", "Anoto solo palabras clave y números.", "Uso abreviaturas."], "Humboldt: Chile y Perú; 65 cm aprox.; 4 kg aprox.; peces pequeños (sardina, anchoveta); nido en cuevas o huecos entre rocas."),
   ("Descartar lo que no sirve", "Quieres saber qué come el pingüino. De «Mide unos 65 centímetros y se alimenta de peces pequeños», ¿qué parte anotas?", ["Mi pregunta es sobre alimentación.", "El tamaño no responde esa pregunta.", "Anoto «peces pequeños»."], "«Peces pequeños».")],
  [("Copiar frases completas.", "Se pierde el hilo del texto.", "Anota palabras clave y datos."),
   ("No registrar números ni nombres.", "Después no se pueden recuperar.", "Anota siempre cifras, lugares y nombres.")],
  ([E(f"Escucha: {PING} ¿Dónde vive el pingüino de Humboldt?", "En las costas de Chile y Perú", "Lo dice la primera oración."),
    E(f"Escucha: {PING} ¿Cuánto pesa aproximadamente?", "Cerca de 4 kilogramos", "Es el dato que entrega el documental."),
    E(f"Escucha: {PING} ¿De qué se alimenta?", "De peces pequeños", "Se mencionan la sardina y la anchoveta.")],
   [E(f"Escucha: {PING} ¿Qué palabras clave anotas para saber dónde anida: «cuevas» y «huecos entre rocas» o «sardina» y «anchoveta»?", "«Cuevas» y «huecos entre rocas»", "Responden a dónde anida."),
    E(f"Escucha: {PING} ¿Cuál apunte es mejor? A: «Humboldt: Chile y Perú; 65 cm; 4 kg; peces pequeños; nido en cuevas». B: copiar todo el texto.", "A", "Registra solo lo importante y es breve."),
    E(f"Escucha: {PING} Si tu pregunta es «¿Qué come?», ¿qué dato NO te sirve: 65 centímetros o sardina y anchoveta?", "65 centímetros", "No tiene relación con la alimentación.")],
   [E(f"Escucha: {PING} ¿Qué recomendación final se da?", "No acercarse a sus nidos", "Lo dice la última oración."),
    E(f"Escucha: {PING} ¿En qué categoría anotas «cuevas o huecos entre las rocas»: tamaño o nido?", "Nido", "Indica dónde anida."),
    E(f"Escucha: {PING} Al oír «unos 65 centímetros», ¿cómo lo anotas rápido? A: «65 cm aprox.». B: «el pingüino mide unos sesenta y cinco centímetros de largo».", "A", "Usa una abreviatura corta.")],
   [E("¿Por qué conviene anotar mientras se escucha en vez de confiar solo en la memoria: porque se olvidan los datos o porque es más lento?", "Porque se olvidan los datos", "Los apuntes conservan la información."),
    E(f"Escucha: {PING} Un compañero anotó «pesa 40 kg». ¿Está bien?", "No", "Se dijo cerca de 4 kilogramos.")],
   [E(f"Escucha: {PING} Con tus apuntes, ¿en qué país, además de Chile, vive este pingüino?", "En Perú", "Lo dice la primera oración."),
    E(f"Escucha: {PING} ¿Qué dos peces se mencionan?", "La sardina y la anchoveta", "Son los ejemplos de su alimento.")]),
  [E(f"Escucha: {PING} Tu amiga dice: «Quiero un apunte para exponer». ¿Qué le recomiendas: organizar por categorías (hábitat, tamaño, alimentación, nido) o escribir todo seguido?", "Organizar por categorías", "Hace el apunte claro.")],
  [E("¿Qué debes anotar siempre al escuchar: números, nombres y lugares?", "Sí", "Son los datos más difíciles de recordar."),
   E("¿Qué es una abreviatura?", "Una forma corta de escribir una palabra", "Ahorra tiempo al anotar."),
   E("¿Se anota todo lo que se dice o solo lo importante?", "Solo lo importante", "Se eligen palabras clave y datos.")],
  ("Pide a una persona que te lea este guion y haz apuntes con tres categorías (quién, qué hace, cuánto): «Reportaje: la ciclovía del barrio. Desde marzo, 300 personas usan cada día la ciclovía de la avenida Los Aromos. Tiene 4 kilómetros y conecta la plaza con el colegio. El municipio planea ampliarla en un año».",
   "Quién: 300 personas por día. Qué hace: usan la ciclovía Los Aromos. Cuánto: 4 km; conecta plaza y colegio; ampliación en 1 año.",
   ["apuntes breves", "incluye números y lugares", "usa categorías"], ["apuntes en tres categorías"], ["copiar frases completas", "omitir cifras"],
   "Comprueba que los números coincidan con el guion."),
  "Escucha un noticiario durante un minuto y anota tres datos.",
  "Resume en tres líneas tus apuntes de un programa que veas.")

# ================================================================ OA 24 · clase 3
PAPEL = "«Explicación: cómo se recicla el papel. Primero, se recogen hojas y cajas usadas. Luego se mezclan con agua hasta formar una pulpa, que es una masa blanda. Después se limpia la pulpa para quitar la tinta. Finalmente, se extiende, se prensa y se seca para formar hojas nuevas. Así se usan menos árboles.»"
L(OA24, 3,
  "Este cuaderno, lápiz y una hoja. Una persona de tu casa puede leerte el guion en voz alta.",
  "Aprenderé a formular preguntas para comprender mejor, elaborar una idea o aclarar el significado de una palabra. Sirve para participar al escuchar y no quedarme con dudas.",
  ["Sé escuchar y tomar apuntes.", "Sé usar palabras interrogativas."],
  ["Hacer preguntas es parte de escuchar bien. Hay tres tipos útiles. Las preguntas para comprender buscan datos del texto: «¿Qué se hace después de formar la pulpa?». Las preguntas para elaborar una idea buscan ir más allá: «¿Por qué reciclar el papel ahorra árboles?» o «¿Qué pasaría si todo el papel se botara?». Las preguntas para aclarar una palabra piden el significado: «¿Qué significa prensar?».",
   "Una buena pregunta se relaciona con el tema, es clara y se puede responder. «¿Qué?» a secas es poco clara. «¿Cuántos árboles hay en Chile?» se aleja del tema del reciclaje. Las palabras interrogativas ayudan: «por qué» pregunta la causa, «cómo» pregunta el modo, «cuándo» pregunta el tiempo y «cuánto» pregunta la cantidad.",
   "Si no entendiste algo, es mejor preguntar con respeto: «¿Puede explicar de nuevo el paso tres?». Tu duda probablemente es la de otros. Y después de escuchar la respuesta, comprueba si ya entendiste."],
  [("pregunta de comprensión", "pregunta que busca datos del texto"), ("pregunta de elaboración", "pregunta que busca ir más allá del texto"), ("pregunta de aclaración", "pregunta sobre el significado de una palabra"), ("interrogativo", "palabra que sirve para preguntar"), ("pulpa", "masa blanda de papel y agua"), ("prensar", "apretar para quitar el agua")],
  [("Clasificar una pregunta", "¿Qué tipo de pregunta es «¿Qué significa prensar?»: de comprensión, de elaboración o de aclaración?", ["Pregunta por el significado de una palabra.", "No pide datos ni ideas nuevas.", "Es de aclaración."], "De aclaración."),
   ("Formular una pregunta", f"Escucha: {PAPEL} No entendiste por qué reciclar ahorra árboles. ¿Qué preguntas?", ["La duda es sobre la causa.", "Uso «por qué».", "Pregunto: «¿Por qué reciclar papel ahorra árboles?»."], "«¿Por qué reciclar papel ahorra árboles?».")],
  [("Preguntar «¿qué?» sin más.", "No se entiende qué se quiere saber.", "Formula la pregunta completa."),
   ("Preguntar algo que se aleja del tema.", "No ayuda a comprender.", "Relaciona la pregunta con lo escuchado.")],
  ([E(f"Escucha: {PAPEL} ¿Qué pregunta aclara una palabra? A: «¿Qué significa pulpa?». B: «¿Cuántas hojas se hacen?».", "A", "Pide el significado de «pulpa»."),
    E(f"Escucha: {PAPEL} ¿Qué pregunta se responde con el texto? A: «¿Para qué se limpia la pulpa?». B: «¿Quién inventó el papel?».", "A", "El texto dice que se limpia para quitar la tinta."),
    E(f"Escucha: {PAPEL} ¿Qué tipo de pregunta es «¿Qué se hace después de formar la pulpa?»: de comprensión o de aclaración?", "De comprensión", "Busca un dato del texto.")],
   [E("¿Qué tipo de pregunta es «¿Qué pasaría si todo el papel se botara?»: de elaboración o de comprensión?", "De elaboración", "Va más allá del texto."),
    E(f"Escucha: {PAPEL} ¿Cuántos pasos tiene el proceso que se explica?", "4", "Primero, luego, después y finalmente."),
    E("¿Qué palabra interrogativa sirve para preguntar una causa: por qué o cuándo?", "Por qué", "Pregunta la razón.")],
   [E(f"Escucha: {PAPEL} ¿Qué pregunta es mejor para entender por qué se usan menos árboles? A: «¿Por qué reciclar el papel permite usar menos árboles?». B: «¿Por qué?».", "A", "Es clara y se relaciona con el tema."),
    E(f"Escucha: {PAPEL} ¿Qué pregunta de comprensión puedes hacer sobre el segundo paso? A: «¿Con qué se mezclan las hojas usadas?». B: «¿Te gusta el papel?».", "A", "Se responde con el texto."),
    E(f"Escucha: {PAPEL} ¿Qué pregunta de aclaración hace falta si no sabes qué es la tinta? A: «¿Qué es la tinta?». B: «¿Dónde vives?».", "A", "Aclara un término del texto.")],
   [E("Durante una exposición no escuchaste un paso. ¿Conviene preguntar o quedarte con la duda?", "Preguntar", "Es la forma de comprender."),
    E(f"Escucha: {PAPEL} La pregunta «¿Cuántos árboles hay en Chile?», ¿se relaciona con el tema del reciclaje?", "No", "Se aleja de lo que se explicó.")],
   [E(f"Escucha: {PAPEL} ¿Qué tipo de pregunta es «¿Es posible reciclar el papel más de una vez?»: de comprensión o de elaboración?", "De elaboración", "Pide ir más allá de lo dicho."),
    E(f"Escucha: {PAPEL} Si quieres saber la cantidad de pasos, ¿qué interrogativo usas: cuántos o dónde?", "Cuántos", "Pregunta una cantidad.")]),
  [E("Escuchas una explicación sobre cómo se hace un helado casero, y no entiendes la palabra «batir». ¿Qué preguntas: «¿Qué significa batir?» o «¿Quién inventó el helado?»?", "«¿Qué significa batir?»", "Aclara una palabra del texto.")],
  [E("¿Cuáles son los tres tipos de preguntas de esta clase?", "De comprensión, de elaboración y de aclaración", "Cada una tiene un propósito."),
   E("¿Una buena pregunta debe relacionarse con el tema?", "Sí", "Así ayuda a comprender."),
   E("¿Qué interrogativo pregunta el modo: cómo o dónde?", "Cómo", "Pide la manera de hacer algo.")],
  ("Pide a una persona que te lea este guion y escribe tres preguntas: una de comprensión, una de elaboración y una de aclaración. Guion: «Explicación: por qué flotan los barcos. Un barco flota porque hace a un lado mucha agua y esa agua lo empuja hacia arriba. Un barco es hueco y está lleno de aire; por eso, aunque sea muy grande, flota».",
   "Comprensión: ¿Qué empuja al barco hacia arriba? Elaboración: ¿Qué pasaría si el barco no estuviera hueco? Aclaración: ¿Qué significa hueco?",
   ["una pregunta de cada tipo", "relacionadas con el tema", "claras y completas"], ["tres preguntas"], ["hacer preguntas vagas", "alejarse del tema"],
   "Pide clasificar cada pregunta que escribió."),
  "Escucha una conversación y anota una pregunta de comprensión.",
  "Escribe cinco preguntas de elaboración sobre un tema que estudies.")

# ================================================================ OA 24 · clase 4
FERIA_A = "«Texto A, noticia radial: esta mañana se realizó la feria del libro en la plaza. Asistieron unas 150 personas, según la organización. Se vendieron 80 libros y hubo cuentacuentos para niños.»"
FERIA_B = "«Texto B, testimonio de un vendedor: yo estuve en la feria del libro. Éramos como 100 personas, nada más. Vendí 30 libros, pero los niños disfrutaron mucho el cuentacuentos.»"
CONSEJOS = "«Consejos para estudiar. Primero, estudia en un lugar tranquilo. Segundo, haz pausas de cinco minutos cada 25 minutos. Tercero, duerme bien la noche anterior. Cuarto, explica en voz alta lo que aprendiste.»"
L(OA24, 4,
  "Este cuaderno, lápiz y una hoja. Una persona de tu casa puede leerte los guiones en voz alta.",
  "Aprenderé a comparar información dentro de un texto oral y entre dos textos orales sobre un mismo tema. Sirve para notar semejanzas, diferencias y fuentes distintas.",
  ["Sé extraer información relevante.", "Sé identificar el tipo de texto oral."],
  ["Comparar es buscar qué coincide y qué difiere. Dentro de un mismo texto puedes comparar dos consejos o dos pasos («¿cuáles se relacionan con el descanso?»). Entre dos textos puedes comparar datos, ejemplos y la forma de contar. Para eso necesitas tus apuntes de ambos.",
   "Cuando dos textos tratan el mismo hecho, mira quién habla y desde dónde. Una noticia suele informar de manera neutral y citar fuentes («según la organización»). Un testimonio cuenta lo vivido y puede incluir opiniones («los niños disfrutaron mucho»). Dos cifras distintas pueden deberse a que cada fuente contó de otra forma o se refiere a cosas distintas.",
   "Observa también las palabras que indican precisión. «Unas 150» o «como 100» son cifras aproximadas. «Vendí 30 libros» se refiere a lo que vendió una persona, mientras que «se vendieron 80» habla del total. Comparar bien evita sacar conclusiones apuradas."],
  [("comparar", "buscar semejanzas y diferencias"), ("fuente", "persona o entidad de donde viene la información"), ("aproximado", "cercano al valor exacto"), ("neutral", "sin tomar partido"), ("opinión", "lo que alguien piensa o siente"), ("coincidencia", "dato que aparece en ambos textos")],
  [("Comparar cifras", f"{FERIA_A} {FERIA_B} ¿En qué dato difieren sobre la asistencia?", ["El texto A dice unas 150 personas, según la organización.", "El texto B dice como 100.", "Difieren en la cantidad de asistentes."], "Texto A: unas 150; texto B: como 100."),
   ("No contradice", "¿Los 80 libros vendidos (texto A) contradicen los 30 libros que vendió el vendedor (texto B)?", ["El texto A habla del total.", "El texto B habla de lo que vendió una persona.", "Pueden ser compatibles."], "No se contradicen; los 30 son parte de los 80.")],
  [("Pensar que dos cifras distintas siempre significan que alguien miente.", "Pueden contarse cosas distintas o de forma distinta.", "Revisa a quién se refiere cada dato."),
   ("Comparar sin anotar.", "Se olvidan los datos.", "Registra los datos de cada texto.")],
  ([E(f"{FERIA_A} ¿Cuántas personas asistieron, según la organización?", "Unas 150", "Es la cifra del texto A."),
    E(f"{FERIA_B} ¿Cuántos libros vendió el vendedor?", "30", "Es el dato del texto B."),
    E(f"{FERIA_A} {FERIA_B} ¿Qué actividad mencionan ambos textos?", "El cuentacuentos", "Aparece en los dos.")],
   [E(f"{FERIA_A} {FERIA_B} ¿Qué cifra de asistentes es distinta entre ambos?", "Unas 150 y como 100", "Los dos textos dan números diferentes."),
    E("¿Por qué pueden coexistir dos cifras distintas de asistentes: porque cada fuente puede haber contado de forma diferente o porque una persona miente siempre?", "Porque cada fuente puede haber contado de forma diferente", "No siempre hay mentira."),
    E(f"{FERIA_A} {FERIA_B} ¿Los 80 libros vendidos del texto A contradicen los 30 del vendedor?", "No", "Los 30 pueden ser parte de los 80.")],
   [E(f"{FERIA_A} {FERIA_B} Supón que los 30 libros del vendedor están incluidos en los 80 del total. ¿Cuántos libros vendieron las demás personas?", "50", "Se restan los 30 del vendedor a los 80 totales. Cálculo: 80 − 30 = 50.", calc="80-30"),
    E(f"{FERIA_A} {FERIA_B} ¿Cuántas personas de diferencia hay entre la cifra de la organización y la del vendedor?", "50", "Se restan 100 a 150. Cálculo: 150 − 100 = 50.", calc="150-100"),
    E(f"Escucha: {CONSEJOS} ¿Cuántos consejos se dan?", "4", "Primero, segundo, tercero y cuarto.")],
   [E(f"{FERIA_B} La expresión «como 100 personas», ¿indica una cifra exacta o aproximada?", "Aproximada", "«Como» suaviza la precisión."),
    E("Al notar que dos textos tienen cifras distintas, ¿qué hace un buen oyente: compara las fuentes o cree sin pensar en el primero?", "Compara las fuentes", "Así evalúa mejor la información.")],
   [E(f"{FERIA_A} {FERIA_B} ¿Qué texto incluye una opinión?", "El texto B", "Dice que los niños «disfrutaron mucho»."),
    E(f"Escucha: {CONSEJOS} ¿Qué dos consejos se relacionan con el descanso?", "El segundo y el tercero", "Hablan de hacer pausas y de dormir bien.")]),
  [E(f"{FERIA_A} {FERIA_B} Para saber la cifra exacta de asistentes, ¿qué conviene hacer: pedir la lista de asistentes a la organización o elegir la cifra que más te guste?", "Pedir la lista de asistentes a la organización", "Es la fuente más precisa.")],
  [E("¿Qué es comparar dos textos?", "Buscar semejanzas y diferencias", "Permite entender mejor la información."),
   E("«Según la organización» indica una fuente. ¿Sí o no?", "Sí", "Dice de dónde viene el dato."),
   E("¿Un testimonio puede incluir opiniones?", "Sí", "Cuenta lo que la persona vivió y siente.")],
  ("Pide a una persona que te lea estos dos guiones. Texto 1: «El club de ajedrez tiene 12 integrantes y se reúne los lunes». Texto 2: «Soy parte del club de ajedrez; somos como 15 y nos juntamos los lunes y los jueves». Escribe una semejanza, una diferencia y por qué puede haber diferencias.",
   "Semejanza: el club se reúne los lunes. Diferencia: 12 integrantes y como 15; lunes solamente y lunes y jueves. Puede haber diferencias porque el texto 2 es aproximado o lo cuenta un integrante.",
   ["escribe una semejanza", "escribe una diferencia", "explica una razón"], ["tres respuestas"], ["no justificar la diferencia", "olvidar el origen de cada texto"],
   "Pide señalar cada dato en el guion."),
  "Compara el pronóstico del tiempo de dos programas y anota diferencias.",
  "Elige un hecho del colegio y pide a dos personas que lo cuenten; compara.")

# ================================================================ OA 24 · clase 5
PROP = "«Propuesta del Centro de Estudiantes: ampliar el recreo de 20 a 30 minutos. Según la propuesta, así habría más tiempo para jugar y almorzar sin apuro. Para compensar, cada día la salida sería 10 minutos más tarde.»"
L(OA24, 5,
  "Este cuaderno, lápiz y una hoja. Una persona de tu casa puede leerte el guion en voz alta.",
  "Aprenderé a formular y fundamentar una opinión sobre lo que escucho, diferenciando hechos y opiniones. Sirve para participar en conversaciones y debates con razones.",
  ["Sé extraer información de un texto oral.", "Sé diferenciar un hecho de una opinión."],
  ["Opinar sobre lo que escuchas es tomar una postura y justificarla. Una opinión fundamentada tiene tres partes: lo que piensas («estoy de acuerdo»), la razón («porque habría más tiempo para almorzar») y la evidencia del texto («la propuesta dice que sería con más tiempo para almorzar sin apuro»). Sin razón, una opinión es solo una preferencia.",
   "Distingue lo que el texto dice de lo que tú piensas. «El recreo pasaría de 20 a 30 minutos» es un dato de la propuesta. «Es la mejor idea» es una opinión. Para fundamentar, usa datos del texto, no suposiciones. Si dices algo que el texto no dice, aclara que es tu idea. Por ejemplo, el guion no dice a qué hora sería la salida; no inventes una hora.",
   "Una opinión puede considerar ventajas y desventajas. «Estoy de acuerdo porque tendría más tiempo para almorzar, aunque salir más tarde me cansaría». Escuchar otras opiniones y respetarlas es parte de opinar. Dos personas pueden pensar distinto y ambas tener razones válidas."],
  [("opinión", "lo que pienso sobre algo"), ("fundamento", "razón que respalda una opinión"), ("postura", "posición a favor o en contra"), ("evidencia", "parte del texto que respalda lo que digo"), ("ventaja", "aspecto positivo"), ("desventaja", "aspecto negativo")],
  [("Opinión fundamentada", f"Escucha: {PROP} Opina a favor y fundamenta.", ["Tomo la postura: estoy a favor.", "Busco una razón en el texto.", "Cito: tendría más tiempo para almorzar sin apuro."], "«Estoy a favor, porque con más recreo se puede almorzar sin apuro»."),
   ("Hecho u opinión", "«El recreo pasaría de 20 a 30 minutos», ¿es un hecho de la propuesta o una opinión?", ["Está en la propuesta.", "No dice si es bueno o malo.", "Es un hecho de la propuesta."], "Un hecho de la propuesta.")],
  [("Opinar sin dar razones.", "La opinión queda sin respaldo.", "Agrega «porque» y una razón."),
   ("Atribuir al texto lo que no dice.", "Se informa mal.", "Cita solo lo que el texto afirma.")],
  ([E(f"Escucha: {PROP} ¿Cuántos minutos más de recreo se proponen?", "10", "Se pasa de 20 a 30 minutos. Cálculo: 30 − 20 = 10.", calc="30-20"),
    E(f"Escucha: {PROP} ¿Cómo se compensa el recreo más largo?", "Con una salida 10 minutos más tarde", "Lo dice el texto."),
    E(f"Escucha: {PROP} ¿Quién hace la propuesta?", "El Centro de Estudiantes", "Lo dice la primera oración.")],
   [E(f"Escucha: {PROP} ¿«Es la mejor idea» es un hecho o una opinión?", "Una opinión", "Expresa una valoración personal."),
    E(f"Escucha: {PROP} ¿Cuál opinión está mejor fundamentada? A: «Estoy de acuerdo, porque con más tiempo se puede almorzar sin apuro». B: «Estoy de acuerdo porque sí».", "A", "Da una razón tomada del texto."),
    E(f"Escucha: {PROP} ¿Qué parte del texto respalda la opinión A de la pregunta anterior: «almorzar sin apuro» o «Centro de Estudiantes»?", "«almorzar sin apuro»", "Es la razón que se menciona.")],
   [E(f"Escucha: {PROP} ¿Qué argumento en contra se basa en el texto? A: «Salir más tarde puede afectar a quienes viajan lejos». B: «Los recreos son malos».", "A", "Se apoya en la salida 10 minutos más tarde."),
    E(f"Escucha: {PROP} ¿Cuál es un dato del texto que respalda un argumento a favor: «más tiempo para jugar» o «la mayoría quiere jugar»?", "«más tiempo para jugar»", "Lo dice la propuesta."),
    E(f"Escucha: {PROP} ¿Qué opinión considera ventajas y desventajas? A: «Me parece buena porque tendría más tiempo para almorzar, aunque salir más tarde me cansaría». B: «Me parece mala».", "A", "Equilibra ambos aspectos.")],
   [E(f"Escucha: {PROP} Pedro dice: «Todos quieren el recreo largo». ¿Está respaldado por el texto?", "No", "El texto no dice qué quieren todos."),
    E("Dos oyentes opinan distinto (uno a favor y otro en contra) y ambos dan razones del texto. ¿Es posible que ambas opiniones sean válidas?", "Sí", "Cada una se apoya en evidencia.")],
   [E(f"Escucha: {PROP} Alguien dice: «Según la propuesta, la salida sería a las 15:00». ¿Es correcto?", "No", "El texto no menciona la hora de salida."),
    E(f"Escucha: {PROP} ¿Qué falta en «Estoy en contra porque no me gusta»?", "Una razón basada en el texto", "No fundamenta su postura.")]),
  [E(f"Escucha: {PROP} Después de escuchar, tu curso debate. ¿Qué haces para opinar bien: decir tu postura, dar una razón y citar el texto, o gritar más fuerte?", "Decir tu postura, dar una razón y citar el texto", "Eso la hace fundamentada.")],
  [E("¿Qué partes tiene una opinión fundamentada?", "Postura, razón y evidencia", "Así se respalda."),
   E("¿«El recreo es de 20 minutos» es un hecho u opinión?", "Un hecho", "Se puede comprobar."),
   E("¿Se puede respetar una opinión distinta a la mía?", "Sí", "Es parte de escuchar.")],
  ("Pide a una persona que te lea este guion: «Propuesta del curso: los viernes habrá 15 minutos de lectura en voz alta antes de salir. Se leerá un cuento corto cada semana, y cada estudiante podrá recomendar uno». Escribe tu opinión en tres oraciones: postura, razón y una parte del guion que la respalde.",
   "Estoy de acuerdo con la propuesta. Creo que ayuda a disfrutar los cuentos. El guion dice que cada estudiante podrá recomendar uno, lo que da participación a todos.",
   ["toma una postura", "da una razón", "cita el guion"], ["opinión de tres oraciones"], ["no fundamentar", "inventar datos"],
   "Pide mostrar la frase que usó como evidencia."),
  "Da tu opinión sobre un programa de radio y justifica con un dato.",
  "Escribe dos opiniones opuestas sobre la propuesta, ambas con razones.")

# ================================================================ OA 24 · clase 6
SKATE = "«Entrevista. Periodista: hoy conversamos sobre el proyecto de un skatepark en la plaza del barrio. Marta, ¿qué opina? Marta: Estoy a favor, porque los jóvenes necesitan un lugar seguro para practicar. Periodista: Don Luis, ¿y usted? Don Luis: Yo estoy en contra. Esa plaza es el único espacio con árboles y el ruido molestaría a los vecinos. Periodista: Gracias a ambos.»"
L(OA24, 6,
  "Este cuaderno, lápiz y una hoja. Una persona de tu casa puede leerte el guion en voz alta, con voces distintas.",
  "Aprenderé a identificar diferentes puntos de vista en un texto oral y a resumirlos para una audiencia sin deformarlos. Sirve para entender cómo piensan personas distintas sobre un mismo tema.",
  ["Sé formular una opinión fundamentada.", "Sé comparar información."],
  ["Un punto de vista es la forma en que una persona ve un tema desde su posición, sus experiencias y sus intereses. En una entrevista o un debate pueden aparecer varios. Para identificarlos, pregúntate quién habla, qué postura toma (a favor, en contra o neutral) y qué razones da. El periodista que entrevista suele mantenerse neutral: pregunta, pero no toma partido.",
   "Cuando dos personas están en desacuerdo, no necesariamente una tiene toda la razón. Cada una puede tener una razón válida desde su perspectiva. Marta piensa en la necesidad de los jóvenes; don Luis piensa en los árboles y el ruido. Entender ambos permite buscar soluciones.",
   "Para contar a otra persona lo que escuchaste, resume con justicia: nombra cada postura y su razón, sin burlarte ni favorecer a nadie. Un buen resumen usa expresiones como «Marta sostiene que...» y «Don Luis considera que...». Si alguien te pregunta tu opinión, sepárala del resumen."],
  [("punto de vista", "forma de ver un tema desde la posición de alguien"), ("a favor", "que apoya una idea"), ("en contra", "que se opone a una idea"), ("neutral", "que no toma partido"), ("debate", "conversación en que se defienden posturas"), ("resumen justo", "resumen que no favorece a una persona")],
  [("Identificar posturas", f"Escucha: {SKATE} ¿Qué postura tiene cada persona?", ["Marta dice «Estoy a favor».", "Don Luis dice «Yo estoy en contra».", "El periodista solo pregunta."], "Marta, a favor; don Luis, en contra; el periodista, neutral."),
   ("Resumen justo", "Escribe un resumen justo de lo que dicen Marta y don Luis.", ["Nombro la postura de cada uno.", "Incluyo la razón de cada uno.", "No opino."], "Marta sostiene que los jóvenes necesitan un lugar seguro; don Luis considera que hay que cuidar los árboles y evitar el ruido.")],
  [("Resumir favoreciendo a quien pienso igual.", "Se deforma lo que dijo el otro.", "Incluye ambas posturas con justicia."),
   ("Decir que una persona «no tiene razón» sin escucharla.", "Cada una tiene razones desde su punto de vista.", "Pregunta por sus razones.")],
  ([E(f"Escucha: {SKATE} ¿Quién está a favor del skatepark?", "Marta", "Lo dice: «Estoy a favor»."),
    E(f"Escucha: {SKATE} ¿Quién está en contra?", "Don Luis", "Lo dice: «Yo estoy en contra»."),
    E(f"Escucha: {SKATE} ¿Qué razón da Marta?", "Los jóvenes necesitan un lugar seguro para practicar", "Es su argumento a favor.")],
   [E(f"Escucha: {SKATE} ¿Qué rol cumple el periodista: pregunta sin tomar partido o apoya a Marta?", "Pregunta sin tomar partido", "Solo conduce la entrevista."),
    E(f"Escucha: {SKATE} ¿Qué razones da don Luis?", "El único espacio con árboles y el ruido", "Son sus argumentos."),
    E("¿Qué es un punto de vista?", "La forma de ver un tema desde la posición de alguien", "Depende de sus intereses y experiencias.")],
   [E(f"Escucha: {SKATE} ¿Quién estaría de acuerdo con «Hay que cuidar los árboles de la plaza»?", "Don Luis", "Defiende el espacio con árboles."),
    E(f"Escucha: {SKATE} Una niña que patina diría que el proyecto es positivo. ¿Con qué punto de vista coincide: el de Marta o el de don Luis?", "El de Marta", "Ambas ven un lugar para practicar."),
    E(f"Escucha: {SKATE} ¿Qué pregunta aclara el punto de vista de don Luis? A: «¿Qué alternativa propone para evitar el ruido?». B: «¿De qué color es la plaza?».", "A", "Pide una propuesta.")],
   [E("¿Pueden dos personas con opiniones opuestas tener razones válidas?", "Sí", "Cada una piensa desde su perspectiva."),
    E(f"Escucha: {SKATE} Cuando el periodista dice «Gracias a ambos», ¿qué posición muestra?", "Neutral", "No favorece a ninguno.")],
   [E(f"Escucha: {SKATE} ¿Qué resumen es justo? A: «Marta quiere el skatepark para dar un lugar seguro a los jóvenes; don Luis se opone por el ruido y para cuidar los árboles». B: «Don Luis es gruñón y Marta tiene la razón».", "A", "Incluye ambas posturas sin favorecer."),
    E(f"Escucha: {SKATE} Si el skatepark se construyera lejos de las casas y los árboles se mantuvieran, ¿se atenderían las razones de ambos?", "Sí", "Se cuidarían el lugar seguro, el ruido y los árboles.")]),
  [E("Debes contarle a tu curso el debate de Marta y don Luis. ¿Cómo empiezas: «Marta sostiene que... y don Luis considera que...» o «Yo creo que don Luis tiene razón porque...»?", "«Marta sostiene que... y don Luis considera que...»", "El resumen presenta ambas posturas.")],
  [E("¿Qué postura tiene quien dice «Estoy a favor»?", "Apoya la idea", "Está de acuerdo."),
   E("¿Un periodista que entrevista debe tomar partido?", "No", "Su rol es preguntar."),
   E("¿Se debe incluir la razón de cada persona en un resumen justo?", "Sí", "Así se entienden sus posturas.")],
  ("Pide a una persona que te lea este guion: «Debate. Sofía: Creo que el curso debe tener una mascota, porque nos enseñaría a ser responsables. Nicolás: No estoy de acuerdo; las mascotas necesitan cuidados diarios y a veces habría gente alérgica en la sala». Escribe un resumen justo de las dos posturas en dos oraciones.",
   "Sofía sostiene que el curso debe tener una mascota porque enseñaría responsabilidad. Nicolás considera que no, porque requiere cuidados diarios y podría haber alergias.",
   ["incluye ambas posturas", "incluye las razones", "no toma partido"], ["resumen de dos oraciones"], ["favorecer a una postura", "omitir razones"],
   "Pide leer el resumen en voz alta y comprobar si es justo."),
  "Escucha a dos personas opinar de un tema y anota sus posturas.",
  "Escribe una posible solución que atienda las razones de Sofía y Nicolás.")
