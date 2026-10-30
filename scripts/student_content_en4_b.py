"""Cuaderno del estudiante, 4.º básico Inglés: EN04 OA 09 (reaccionar a lo leído) y OA 10 (sonidos del inglés).

Los textos en inglés son originales, muy breves y llevan pista en español. Las imágenes se describen entre corchetes
porque el cuaderno no incluye ilustraciones. Cada estructura se enseña en la propia clase antes de usarla.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA9, OA10 = "EN04 OA 09", "EN04 OA 10"


def E(rows):
    return [r if isinstance(r, dict) else ex(*r) for r in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 09
lesson(
    OA9, 1,
    "Los textos escritos en cada ejercicio, hojas en blanco, lápices de colores y lápiz grafito. Una persona de tu casa puede escuchar tu explicación.",
    "Aprenderé a responder a un texto en inglés con una ilustración que muestre una idea del texto y a señalar la oración que la apoya. Sirve para que mi dibujo demuestre que entendí y no sea solo un adorno.",
    ["Sé leer oraciones cortas en inglés con colores, animales y objetos.", "Sé que un título y una imagen dan pistas."],
    [
        "Una ilustración (illustration) es un dibujo que muestra una idea. Después de leer, puedes responder con un dibujo. Pero un dibujo bonito no basta: tiene que mostrar algo que el texto realmente dice. Esa parte del texto se llama evidencia (evidence).",
        "Para ilustrar bien sigue tres pasos. Primero lee el texto y elige una idea (idea). Luego dibuja esa idea con los detalles del texto: colores, cantidades y lugares. Por último señala la oración que la apoya y di: «I drew a blue boat because the text says blue boat» (dibujé un bote azul porque el texto dice bote azul).",
        "Si un detalle de tu dibujo no está en el texto, no puedes decir que el texto lo dice. Por ejemplo, si el texto no menciona un perro, un perro en tu dibujo es un adorno. Puedes agregar cosas, pero la idea principal de tu dibujo debe venir de una oración del texto.",
    ],
    [("illustration", "ilustración, dibujo que muestra una idea"), ("evidence", "evidencia, parte del texto que prueba algo"), ("idea", "idea"), ("because", "porque"), ("I drew...", "dibujé..."), ("the text says", "el texto dice")],
    [
        ("Elegir una idea y su evidencia", "Texto: «Nico has a small blue boat. He is on the lake with his sister. The sun is hot. Nico is happy.» (small es pequeño; lake es lago; sister es hermana). Elige la idea «Nico is happy». ¿Qué dibujas y cuál es la evidencia?", ["Elijo una idea: Nico está contento.", "Dibujo a Nico sonriendo en su bote.", "Busco la oración que lo dice."], "Dibujo a Nico sonriendo; la evidencia es la oración «Nico is happy.»"),
        ("Corregir un dibujo", "Con el mismo texto, Mia dibujó un bote rojo y dice: «I drew a red boat because the text says red boat». ¿Qué debe cambiar?", ["Busco la oración del bote: small blue boat.", "El texto dice blue, no red.", "Cambio el color del dibujo."], "Debe pintar el bote de azul (blue)."),
    ],
    [
        ("Dibujar algo bonito que no está en el texto y decir que el texto lo dice.", "El dibujo no tiene evidencia en el texto.", "Dibuja la idea con detalles que el texto dice y señala su oración."),
        ("Dibujar sin decir qué oración apoya el dibujo.", "Nadie puede comprobar que entendiste.", "Termina siempre con «I drew... because the text says...»."),
    ],
    [
        ("¿Qué significa «illustration»?", "Ilustración, un dibujo que muestra una idea", "Illustration se parece a la palabra ilustración."),
        ("¿Qué significa «because»?", "Porque", "Because une el dibujo con su razón."),
        ("Texto: «Nico has a small blue boat.» ¿De qué color es el bote? Responde en inglés.", "blue", "El texto dice blue boat."),
    ],
    [
        ("Texto: «Nico has a small blue boat. He is on the lake with his sister.» ¿Qué descripción de dibujo coincide? (a) [un bote azul pequeño en un lago con dos niños] (b) [un bote rojo en la nieve]", "a", "El texto habla de un bote azul, un lago y dos niños."),
        ("Quiero ilustrar la idea «Nico is happy». ¿Qué oración del texto es la evidencia? Escríbela.", "Nico is happy.", "Esa oración dice exactamente la idea que dibujo."),
        ("Un dibujo muestra un perro, pero el texto de Nico no habla de ningún perro. ¿Es evidencia del texto o un adorno?", "Un adorno", "El perro no aparece en ninguna oración del texto."),
    ],
    [
        ("Texto: «Nico has a small blue boat.» Completa con la palabra que dice el color: «I drew a ___ boat.» (small es pequeño)", "blue", "Blue es el color del bote en el texto."),
        ("Texto: «The sun is hot.» Dibujo: [un sol grande y brillante]. ¿Esta oración apoya el dibujo? Responde sí o no.", "Sí", "La oración habla del sol y el dibujo muestra el sol."),
        ("Quiero dibujar el lugar donde está Nico. ¿Qué palabra en inglés del texto debo mirar? (lugar con agua)", "lake", "Lake es el lago donde está Nico."),
    ],
    [
        ("Ana dibujó a Nico solo en el bote. El texto dice «with his sister». ¿Qué falta en su dibujo? Responde en español.", "Su hermana", "El texto dice que Nico está con su hermana (sister)."),
        ("Leo dice: «Mi dibujo es bueno porque tiene muchos colores». ¿Es una buena razón para decir que ilustra el texto? Responde sí o no.", "No", "Los colores no prueban que el dibujo muestre una idea del texto."),
    ],
    [
        ("Dibujo: [un bote azul pequeño, dos niños y un sol]. Elige la mejor frase para decir en voz alta: (a) «I drew Nico and his sister on the lake because the text says so.» (b) «I drew a car because I like cars.»", "a", "La frase (a) usa el texto como razón."),
        ("Ana dibujó un bote grande con un sol. Leo dibujó un bote pequeño azul, dos niños y un sol. ¿Quién siguió mejor el texto de Nico? Escribe el nombre.", "Leo", "El texto dice bote pequeño azul y dos niños."),
    ],
    [("En el club de lectura lees: «Pia has a yellow kite. It is windy. Pia runs in the park.» (kite es cometa; windy es con viento; runs es corre). Para dibujar la cometa, ¿qué oración te dice el color que debes usar? Escríbela.", "Pia has a yellow kite.", "Esa oración dice yellow kite.")],
    [
        ("¿Cómo se dice «hermana» en inglés?", "sister", "Sister es hermana."),
        ("¿Qué es la «evidence» de un dibujo?", "La parte del texto que lo apoya", "La evidencia prueba que el dibujo viene del texto."),
        ("¿Qué frase uso para dar la razón de mi dibujo?", "I drew... because the text says...", "Une el dibujo con la oración del texto."),
    ],
    task("Elige uno de estos dos textos. Texto A: «Nico has a small blue boat. He is on the lake with his sister. The sun is hot. Nico is happy.» Texto B: «Pia has a yellow kite. It is windy. Pia runs in the park.» Lee el texto en voz alta con una persona de tu casa. Dibuja una sola idea del texto con sus colores y cantidades. Subraya en el texto la oración que apoya tu dibujo y di en voz alta: «I drew ___ because the text says ___».", "Texto B: dibujo a Pia corriendo con una cometa amarilla; subrayo «Pia has a yellow kite.» y digo «I drew a yellow kite because the text says yellow kite».", ["el dibujo muestra una idea del texto", "los colores y las cantidades coinciden con el texto", "subraya la oración que apoya el dibujo", "dice «I drew... because the text says...»"], ["el dibujo con la oración subrayada", "nota de la persona que escuchó tu explicación"], ["agregar algo que el texto no dice y presentarlo como evidencia", "no señalar la oración"], "Pregunta qué oración sirve de evidencia y pide corregir un detalle del dibujo que no coincida con el texto."),
    "Relee el texto de Nico y di en español una idea que podrías ilustrar y qué oración la apoya.",
    "Escribe un texto original de dos oraciones en inglés, por ejemplo «The cat is black. It is on a chair», y pide a otra persona que lo ilustre.",
)

lesson(
    OA9, 2,
    "Los textos escritos en cada ejercicio, hojas de papel, lápices y, si quieres, tiras de papel para hacer figuras. Una persona de tu casa puede ayudarte a preparar la escena.",
    "Aprenderé a representar un texto en inglés con una figura o una escena hecha con dibujos de papel. Sirve para mostrar quiénes están, dónde están y qué hacen según el texto.",
    ["Sé que una ilustración debe tener evidencia en el texto.", "Sé decir lugares simples en inglés como kitchen, park y house."],
    [
        "Una escena (scene) muestra personajes (characters), un lugar (setting) y objetos. Una figura (figure) es una forma que representa a una persona, un animal o un objeto: puede ser un muñeco de papel o un dibujo recortado. Con varias figuras puedes armar una escena sobre una mesa.",
        "Para armar una escena, lee el texto y haz una lista. Primero anota quiénes son los personajes. Luego anota el lugar. Por último anota los objetos y cuántos son. Después arma la escena y di: «In my scene there is a cake» (en mi escena hay una torta) o «In my scene there are two cups» (en mi escena hay dos tazas).",
        "Usa «there is» para una cosa y «there are» para varias. Revisa tu escena con el texto: cada figura debe tener una oración que la apoye. Si el texto no dice dónde está un objeto, puedes ubicarlo tú, pero no digas que el texto lo dice.",
    ],
    [("scene", "escena"), ("figure", "figura, muñeco o forma que representa algo"), ("character", "personaje"), ("setting", "lugar donde ocurre la historia"), ("there is", "hay (una cosa)"), ("there are", "hay (varias cosas)")],
    [
        ("Hacer la lista de la escena", "Texto: «Tom and Lia are in the kitchen. Tom has a cake. Lia has two cups. There is a table.» (kitchen es cocina; cups son tazas). ¿Qué figuras necesitas?", ["Personajes: Tom y Lia.", "Lugar: la cocina.", "Objetos: una torta, dos tazas y una mesa."], "Dos personajes, la cocina, una torta, dos tazas y una mesa."),
        ("Describir la escena", "Con la misma escena, ¿cómo dices que hay dos tazas?", ["Son varias cosas, uso there are.", "Digo la cantidad en inglés: two.", "Uso In my scene."], "In my scene there are two cups."),
    ],
    [
        ("Poner en la escena una figura que el texto no menciona y decir que está en el texto.", "No tiene evidencia en ninguna oración.", "Usa solo lo que el texto dice como evidencia; lo demás es adorno."),
        ("Olvidar el lugar de la historia.", "Sin lugar, la escena no muestra dónde ocurre el texto.", "Anota siempre el setting antes de armar la escena."),
    ],
    [
        ("¿Qué significa «scene»?", "Escena", "Scene se parece a escena."),
        ("¿Qué significa «figure» en esta clase?", "Una figura, un muñeco o forma que representa algo", "Sirve para representar personajes y objetos."),
        ("Texto: «Tom and Lia are in the kitchen.» ¿Dónde están? Responde en inglés.", "kitchen", "Kitchen es la cocina del texto."),
    ],
    [
        ("Texto: «Tom and Lia are in the kitchen. Tom has a cake. Lia has two cups.» ¿Cuántas tazas necesitas en tu escena? Escribe el número.", "2", "El texto dice two cups."),
        ("Lista: Tom, Lia, a cake, two cups, a dog. Según el texto de Tom y Lia, ¿qué elemento sobra? Escríbelo.", "a dog", "El texto no menciona ningún perro."),
        ("Elige la frase correcta para describir la escena: (a) «In my scene there are two cups.» (b) «In my scene there are five cups.»", "a", "El texto dice two cups."),
    ],
    [
        ("Completa: «In my scene Lia has ___ cups.» (el número en inglés)", "two", "Two es dos, la cantidad del texto."),
        ("Completa con is o are: «In my scene there ___ a table.»", "is", "Table es una sola cosa, por eso se usa there is."),
        ("Texto: «Ben has a dog. The dog is brown. They are in the park.» ¿Cuántos personajes necesitas? Escribe el número.", "2", "Los personajes son Ben y el perro."),
    ],
    [
        ("Leo armó una escena con Tom, Lia, una torta y tres tazas. ¿Qué debe corregir? Responde en español.", "Debe dejar solo dos tazas", "El texto dice two cups."),
        ("¿Por qué una escena necesita el lugar (setting)? Elige: (a) porque dice dónde ocurre la historia (b) porque es más bonito.", "a", "El lugar es parte de lo que el texto cuenta."),
    ],
    [
        ("Elige la mejor frase para presentar la escena: (a) «My scene shows Tom and Lia in the kitchen with a cake and two cups.» (b) «My scene shows Tom and Lia in the park with two cakes.»", "a", "La frase (a) coincide con el texto."),
        ("Texto: «Ben has a dog. The dog is brown. They are in the park.» Elige la lista correcta: (a) Ben, a brown dog, the park (b) Ben, a black cat, the school", "a", "La lista (a) usa lo que dice el texto."),
    ],
    [("En el taller de arte lees: «The bear is in the forest. It has a basket. There are three apples.» (forest es bosque; basket es cesta). Armarás la cesta con figuras de manzanas. ¿Cuántas manzanas pones? Escribe el número.", "3", "El texto dice three apples.")],
    [
        ("¿Cómo se dice «hay (varias cosas)» en inglés?", "there are", "There are se usa con varias cosas."),
        ("¿Qué escribo primero en mi lista de escena?", "Los personajes", "Primero se anota quién aparece."),
        ("¿Cómo se dice «lugar donde ocurre la historia» en inglés?", "setting", "Setting es el lugar de la historia."),
    ],
    task("Lee con una persona de tu casa: «Tom and Lia are in the kitchen. Tom has a cake. Lia has two cups. There is a table.» Haz tu lista: personajes, lugar y objetos con sus cantidades. Dibuja las figuras en papel y arma la escena sobre una mesa. Presenta tu escena con tres frases que empiecen con «In my scene there is/are...» y señala la oración del texto que apoya cada una.", "«In my scene there are two children. In my scene there is a cake. In my scene there are two cups.»", ["la escena tiene personajes, lugar y objetos del texto", "las cantidades coinciden con el texto", "usa there is y there are correctamente", "señala la oración de apoyo"], ["la escena armada o una foto del dibujo", "nota de la persona que escuchó las tres frases"], ["usar there is con varias cosas", "agregar figuras que el texto no menciona"], "Revisa contigo una oración a la vez y pide corregir there is o there are si es necesario."),
    "Mira una habitación de tu casa y di en español qué personajes, lugar y objetos usarías para armar una escena.",
    "Escribe tres oraciones en inglés sobre una escena inventada, por ejemplo «The cat is in the garden», y arma la escena con figuras de papel.",
)

lesson(
    OA9, 3,
    "Los textos escritos en cada ejercicio y espacio para moverte con seguridad, sin objetos en el suelo. Una persona de tu casa puede hacer de público.",
    "Aprenderé a dramatizar una historia corta en inglés con gestos y una frase, usando solo lo que el texto dice. Sirve para mostrar con el cuerpo que entendí cada acción.",
    ["Sé representar una escena con figuras.", "Sé decir acciones simples en inglés como open y see."],
    [
        "Dramatizar (dramatize) es actuar una historia con el cuerpo, la cara y la voz. Cada acción del texto se convierte en un gesto (gesture). Si el texto dice «Sam opens the door» (Sam abre la puerta), haces el gesto de abrir una puerta con las manos.",
        "También puedes decir una frase del personaje, que se llama línea (line). Si el texto dice: Sam says «Wow! A present!» (¡Guau! ¡Un regalo!), esa es la línea que dices. Para sentimientos, usa la cara y la voz: «surprised» (sorprendido) se muestra con los ojos abiertos y la boca en forma de O.",
        "La regla de oro es la evidencia: cada gesto que haces debe venir de una oración del texto. Si inventas una acción que no está, como saltar, ya no estás mostrando el texto. Antes de actuar, haz una lista de acciones en el orden del texto y actúalas una por una, con movimientos tranquilos y seguros.",
    ],
    [("dramatize", "dramatizar, actuar una historia"), ("gesture", "gesto"), ("line", "frase que dice un personaje"), ("opens the door", "abre la puerta"), ("surprised", "sorprendido"), ("present", "regalo")],
    [
        ("De una oración a un gesto", "Texto: «Sam opens the door. He sees a big box. He is surprised. He says: Wow! A present!» (box es caja). ¿Qué gesto haces para «Sam opens the door»?", ["Leo la acción: opens the door.", "Pienso en cómo se abre una puerta.", "Hago el gesto con las manos."], "Hago como si abriera una puerta con las manos."),
        ("Ordenar la dramatización", "Con el mismo texto, ¿en qué orden actúas: sorpresa, abrir la puerta, decir la línea, ver la caja?", ["Sigo el orden del texto.", "Primero abre la puerta y ve la caja.", "Después se sorprende y dice la línea."], "Abrir la puerta, ver la caja, sorpresa, decir la línea."),
    ],
    [
        ("Actuar acciones que el texto no dice, como saltar o correr.", "No son evidencia del texto.", "Haz solo las acciones del texto, en el mismo orden."),
        ("Actuar rápido sin leer el texto antes.", "Se olvidan acciones o se cambia el orden.", "Haz primero la lista de acciones y luego actúa."),
    ],
    [
        ("¿Qué significa «gesture»?", "Gesto", "Gesture se parece a gesto."),
        ("¿Qué significa «present» en el texto de Sam?", "Regalo", "Present es lo que Sam encuentra en la caja."),
        ("¿Qué significa «opens the door»?", "Abre la puerta", "Opens es abre y door es puerta."),
    ],
    [
        ("Texto: «He is surprised.» ¿Qué cara haces? Elige: (a) ojos abiertos y boca en forma de O (b) ojos cerrados y bostezo", "a", "La sorpresa se muestra con ojos y boca abiertos."),
        ("Texto: «He says: Wow! A present!» ¿Cómo se llama lo que dice el personaje? Escribe la palabra en inglés.", "line", "Line es la frase que dice un personaje."),
        ("Texto de Sam: «Sam opens the door. He sees a big box.» ¿Qué haces después de abrir la puerta? Responde en español.", "Miro una caja grande", "La segunda oración dice que ve una caja grande."),
    ],
    [
        ("Completa la línea de Sam, que dice el texto: «Wow! A ___!»", "present", "El texto dice A present."),
        ("Ordena las acciones del texto escribiendo los números: (1) says the line (2) opens the door (3) sees the box", "2, 3, 1", "El orden es abrir, ver y decir la línea."),
        ("Texto de Sam: «He sees a big box.» ¿Qué gesto sigue esa oración? Elige: (a) miro con curiosidad una caja grande (b) abro una puerta", "a", "Sees es ve: la oración dice que Sam ve una caja grande."),
    ],
    [
        ("Pablo dramatizó a Sam saltando de alegría. El texto no lo dice. ¿Qué parte de la regla rompió? Responde en español.", "Hizo una acción que no está en el texto", "Cada gesto necesita evidencia en una oración del texto."),
        ("Ema actuó todo en orden: abrió la puerta, vio la caja y dijo la línea, pero no mostró sorpresa. ¿Qué oración olvidó actuar?", "He is surprised.", "Esa oración pide una cara de sorpresa."),
    ],
    [
        ("Texto nuevo: «Mia sits on a chair. She reads a book. She is sleepy.» (sleepy es con sueño). Elige la secuencia de gestos correcta: (a) sentarse, hacer como que lees, bostezar (b) correr, saltar, reír", "a", "La secuencia (a) sigue las tres oraciones."),
        ("Texto: «Mia reads a book.» ¿Cuál es la evidencia para hacer el gesto de leer? Escribe la oración.", "She reads a book.", "Esa oración menciona la acción de leer."),
    ],
    [("En el taller de teatro de la escuela te dan este texto: «Dan sees a bird. He smiles. He says: Hello, little bird!» (smiles es sonríe). ¿Qué línea dices? Escríbela.", "Hello, little bird!", "Esa es la línea que dice el texto.")],
    [
        ("¿Cómo se dice «sorprendido» en inglés?", "surprised", "Surprised es sorprendido."),
        ("¿Qué debe tener cada gesto de mi dramatización?", "Evidencia en el texto", "Sin evidencia sería un adorno."),
        ("¿Qué hago antes de actuar?", "Hago la lista de acciones en orden", "Así no olvido ninguna acción."),
    ],
    task("Con una persona de tu casa como público, dramatiza este texto en un espacio libre y seguro: «Sam opens the door. He sees a big box. He is surprised. He says: Wow! A present!» Antes de actuar, escribe la lista de acciones en orden. Actúa con gestos tranquilos y di la línea en inglés. Al final, el público te dice qué oración vio en cada gesto.", "Lista: 1 abrir la puerta, 2 ver la caja, 3 sorpresa, 4 línea «Wow! A present!». Actúo cada una en ese orden.", ["la lista de acciones está en el orden del texto", "cada gesto viene de una oración", "muestra la sorpresa con la cara", "dice la línea en inglés"], ["la lista de acciones", "nota del público con la oración que reconoció en cada gesto"], ["agregar acciones que el texto no tiene", "olvidar la sorpresa"], "El público dice qué gesto entendió y tú señalas en el texto la oración que lo apoya."),
    "Lee en español una escena de un cuento que conozcas y di qué tres gestos usarías para actuarla.",
    "Escribe un texto de tres oraciones en inglés sobre un personaje que abre una caja y dramatízalo.",
)

lesson(
    OA9, 4,
    "Los textos escritos en cada ejercicio, lápiz y una hoja para escribir tus frases. Una persona de tu casa puede leer lo que escribes.",
    "Aprenderé a responder a un texto en inglés con palabras o frases escritas: cómo me siento, qué parte me gusta y con qué experiencia propia la relaciono. Sirve para decir lo que pienso con evidencia.",
    ["Sé representar un texto con un dibujo o una dramatización.", "Sé palabras de sentimientos como happy y sad."],
    [
        "Una respuesta escrita (written response) puede ser una palabra o una frase corta. Para decir cómo te sentiste usa «I feel happy because...» (me siento contento porque...). Para decir qué parte te gustó usa «My favorite part is...» (mi parte favorita es...). Para conectar el texto con tu vida usa «It reminds me of...» (me recuerda a...).",
        "Cada respuesta tiene dos partes: lo que sientes o piensas y una razón del texto. Después de because pones algo que el texto dice. Por ejemplo: «I feel happy because they laugh» (me siento contento porque se ríen). Si la razón no está en el texto, tu respuesta queda sin apoyo.",
        "Al relacionar el texto con una experiencia propia, cuida tu privacidad: habla de actividades generales, como jugar o dibujar, y no entregues datos personales como direcciones o nombres completos. Tu opinión es tuya, pero la razón siempre debe volver al texto.",
    ],
    [("I feel...", "me siento..."), ("My favorite part is...", "mi parte favorita es..."), ("It reminds me of...", "me recuerda a..."), ("funny", "divertido"), ("rainy", "lluvioso"), ("laugh", "reír")],
    [
        ("Escribir un sentimiento con razón", "Texto: «It is a rainy day. Mina and her brother play cards at home. They laugh a lot. Then the sun comes out.» (cards son cartas; laugh es reír; the sun comes out es sale el sol). ¿Cómo escribes qué sientes y por qué?", ["Elijo un sentimiento: happy.", "Busco una razón en el texto: they laugh.", "Escribo I feel happy because they laugh."], "I feel happy because they laugh."),
        ("Relacionar con mi experiencia", "Con el mismo texto, ¿cómo conectas la historia con jugar en casa?", ["Pienso en una actividad mía parecida.", "Uso la frase It reminds me of.", "Digo la actividad sin dar datos personales."], "It reminds me of playing games at home."),
    ],
    [
        ("Escribir «I feel happy» sin decir por qué.", "Falta la razón del texto.", "Agrega because y una razón que el texto diga."),
        ("Dar una razón que no está en el texto.", "La respuesta no tiene evidencia.", "Relee y usa algo que el texto dice."),
    ],
    [
        ("¿Cómo se dice «mi parte favorita es» en inglés?", "My favorite part is", "Se usa para decir qué parte me gustó."),
        ("¿Qué significa «It reminds me of...»?", "Me recuerda a...", "Se usa para relacionar el texto con mi vida."),
        ("¿Qué significa «laugh»?", "Reír", "Laugh es reír."),
    ],
    [
        ("Texto de Mina: «They laugh a lot.» Elige el sentimiento que combina: (a) happy (b) angry", "a", "Reírse mucho se relaciona con estar contento."),
        ("¿Qué parte tiene toda respuesta con razón? Elige: (a) lo que siento y una razón del texto (b) solo un dibujo", "a", "Una respuesta con razón dice lo que pienso y por qué."),
        ("Texto de Mina: «Then the sun comes out.» ¿Qué sale al final? Responde en español.", "El sol", "La oración dice que sale el sol."),
    ],
    [
        ("Completa: «My favorite part is when the ___ comes out.» (el sol en inglés)", "sun", "El texto dice the sun comes out."),
        ("Texto de Mina. Elige la frase con razón del texto: (a) «I feel happy because they laugh.» (b) «I feel happy because I have a new bike.»", "a", "La razón de (a) viene del texto."),
        ("Completa para decir que el texto te recuerda a jugar a las cartas: «It reminds me of playing ___.» (cartas en inglés, palabra del texto)", "cards", "Cards es la palabra del texto para cartas."),
    ],
    [
        ("Rosa escribió: «I feel sad because they laugh.» ¿Es una buena respuesta? Explica en español.", "No, porque reírse no es una razón para estar triste en el texto", "La razón no se relaciona con lo que el texto cuenta."),
        ("Tomás escribió: «It reminds me of my house, 25 Pine Street.» ¿Qué debe quitar? Responde en español.", "La dirección", "La dirección es un dato privado."),
    ],
    [
        ("Ordena las palabras para formar una frase: favorite / My / the / part / is / sun. Escríbela.", "My favorite part is the sun.", "La estructura empieza con My favorite part is."),
        ("Texto de Mina. Escribe una frase con la palabra «because» para decir por qué te gusta el final. Debe terminar con «the sun comes out».", "I like the end because the sun comes out.", "Después de because va la razón del texto."),
    ],
    [("En una reseña de la biblioteca escribes sobre este texto: «A small robot cleans the school at night. It is quiet. It is blue.» (robot, cleans es limpia, quiet es silencioso). Elige la frase con razón del texto: (a) «I like the robot because it is blue.» (b) «I like the robot because it flies.»", "a", "El texto dice que el robot es azul, pero no dice que vuele.")],
    [
        ("¿Cómo se dice «Me siento contento» en inglés?", "I feel happy", "I feel es me siento."),
        ("¿Qué datos no debo escribir al relacionar el texto con mi vida?", "Direcciones y datos personales", "Son datos privados."),
        ("¿Qué va después de because?", "Una razón del texto", "La razón da apoyo a mi respuesta."),
    ],
    task("Lee con una persona de tu casa: «It is a rainy day. Mina and her brother play cards at home. They laugh a lot. Then the sun comes out.» Escribe en una hoja tres respuestas cortas en inglés: (1) cómo te sientes con «I feel... because...», (2) tu parte favorita con «My favorite part is...», (3) una conexión con tu vida con «It reminds me of...». Cada razón debe venir del texto y no debes escribir datos privados.", "«I feel happy because they laugh. My favorite part is the sun. It reminds me of playing games.»", ["escribe tres frases con las estructuras enseñadas", "las razones vienen del texto", "no incluye datos personales", "la ortografía de las palabras del texto es correcta"], ["la hoja con las tres frases", "nota de la persona que las leyó"], ["dar una razón que el texto no dice", "escribir datos privados"], "Pregunta de qué oración sacó la razón y ayuda a corregir la ortografía de una palabra."),
    "Di en español cómo te sentiste con el último cuento que leíste y qué parte te gustó.",
    "Escribe una frase con «I feel... because...» sobre un texto breve que escribas tú.",
)

lesson(
    OA9, 5,
    "Los textos escritos en cada ejercicio, lápiz, hojas para dibujar y una persona de tu casa para escuchar tu opinión.",
    "Aprenderé a dar una opinión sobre un texto en inglés y a apoyarla con una razón del texto, usando dibujo, actuación o escritura. Sirve para decir lo que pienso y demostrar que leí.",
    ["Sé responder con un dibujo, un gesto o una frase.", "Sé usar because para dar una razón."],
    [
        "Una opinión (opinion) dice lo que tú piensas o sientes, y no es un dato del texto. «The tomatoes are red» (los tomates son rojos) es un hecho (fact): el texto lo dice. «The garden is nice» (el huerto es bonito) es una opinión: es lo que alguien piensa.",
        "Para dar una opinión usa «I think...» (yo creo que...) o «I like... because...» (me gusta... porque...). Después de because pones una razón que el texto diga. Palabras útiles para opinar: nice (bonito), funny (divertido), boring (aburrido), interesting (interesante). Una preferencia (preference) es lo que eliges, por ejemplo «I like tomatoes more than flowers».",
        "Puedes comunicar tu opinión de varias formas: diciéndola, escribiéndola, dibujándola o actuándola. En cualquier forma, tu opinión necesita apoyo. Si alguien opina distinto, no es un error: cada persona puede pensar algo distinto, pero debe dar su razón del texto.",
    ],
    [("opinion", "opinión"), ("fact", "hecho, dato que el texto dice"), ("I think...", "yo creo que..."), ("nice", "bonito, agradable"), ("interesting", "interesante"), ("preference", "preferencia, lo que elijo")],
    [
        ("Hecho u opinión", "Texto: «Class 4B has a small garden. The children water the plants every day. They have tomatoes and flowers. The tomatoes are red.» (garden es huerto; water es regar). ¿«The tomatoes are red» es hecho u opinión?", ["Busco la oración en el texto.", "El texto la dice.", "Entonces es un dato del texto."], "Es un hecho (fact), porque el texto lo dice."),
        ("Opinión con razón", "Con el mismo texto, ¿cómo dices que el huerto te parece bonito y por qué?", ["Uso I think para la opinión.", "Elijo una razón del texto: the children water the plants.", "Uno las dos partes con because."], "I think the garden is nice because the children water the plants."),
    ],
    [
        ("Decir una opinión sin razón: «I like it».", "Nadie sabe si leíste el texto.", "Agrega because y una razón que el texto diga."),
        ("Pensar que una opinión distinta es un error.", "Las personas pueden pensar distinto.", "Una opinión es válida si tiene una razón del texto."),
    ],
    [
        ("¿Qué significa «I think...»?", "Yo creo que...", "I think introduce una opinión."),
        ("¿Qué significa «interesting»?", "Interesante", "Se parece a interesante en español."),
        ("¿Cómo se dice «bonito» o «agradable» en inglés?", "nice", "Nice es una palabra para opinar."),
    ],
    [
        ("Texto del huerto: «They have tomatoes and flowers.» ¿Es un hecho o una opinión? Responde en español.", "Un hecho", "El texto lo dice y se puede comprobar."),
        ("¿«The garden is nice» es hecho u opinión? Responde en español.", "Una opinión", "Que algo sea bonito depende de quien lo piensa."),
        ("¿Qué necesita una opinión para tener apoyo? Elige: (a) una razón del texto (b) un dibujo grande", "a", "La razón del texto apoya la opinión."),
    ],
    [
        ("Completa: «I think the garden is nice ___ the tomatoes are red.» (porque)", "because", "Because une la opinión con su razón."),
        ("Texto del huerto. Elige la opinión con razón del texto: (a) «I like the garden because they have tomatoes and flowers.» (b) «I like the garden because it has a pool.»", "a", "El texto dice tomatoes and flowers, no habla de una piscina."),
        ("Escribe en inglés la palabra que significa aburrido. Opciones: boring / nice.", "boring", "Boring es aburrido."),
    ],
    [
        ("Ana dice «I think the garden is boring because the tomatoes are red». ¿Su razón apoya su opinión? Responde sí o no.", "No", "Que los tomates sean rojos no explica por qué sería aburrido."),
        ("Ema prefiere las flores y Luis prefiere los tomates, y ambos dan razones del texto. ¿Alguien se equivocó? Responde sí o no.", "No", "Las preferencias pueden ser distintas si tienen razón."),
    ],
    [
        ("Ordena las palabras para formar una opinión: think / I / the / interesting / is / garden. Escríbela.", "I think the garden is interesting.", "La frase empieza con I think y sigue con la opinión."),
        ("Texto del huerto. Escribe una preferencia: dices que prefieres los tomates a las flores y das la razón «they are red». Usa «I like... because...».", "I like the tomatoes because they are red.", "La razón se saca de la oración «The tomatoes are red»."),
    ],
    [("En la reunión de curso lees este aviso: «Class 4B has a small garden. The children water the plants every day.» Un compañero pregunta qué opinas. Elige la mejor respuesta: (a) «I think the garden is nice because the children water the plants every day.» (b) «I think the garden is nice.»", "a", "La respuesta (a) tiene una razón del texto.")],
    [
        ("¿Cómo se dice «opinión» en inglés?", "opinion", "Opinion se parece a opinión."),
        ("¿Qué es un hecho (fact)?", "Algo que el texto dice y se puede comprobar", "Un hecho no depende de lo que yo piense."),
        ("¿Qué palabra se usa para decir la razón?", "because", "Because significa porque."),
    ],
    task("Lee con una persona de tu casa: «Class 4B has a small garden. The children water the plants every day. They have tomatoes and flowers. The tomatoes are red.» Primero escribe un hecho y una opinión sobre el texto. Luego da tu opinión en una de estas formas a tu elección: decirla con «I think... because...», dibujarla con una oración de apoyo, o actuarla con un gesto y una frase. Termina señalando en el texto la razón que usaste.", "Hecho: The tomatoes are red. Opinión: I think the garden is nice because the children water the plants.", ["escribe un hecho y una opinión distintos", "la opinión tiene una razón del texto", "usa I think o I like con because", "señala la razón en el texto"], ["tu hecho y tu opinión escritos", "nota de la persona que escuchó tu opinión"], ["confundir hecho con opinión", "dar una opinión sin razón"], "Pide explicar la razón y comprueba juntos que esté en el texto; acepta opiniones distintas con buena razón."),
    "Di en español si te gustaría tener un huerto como el del texto y por qué.",
    "Lee un texto breve en inglés de tu casa, escribe un hecho y una opinión sobre él y comparte tu opinión con una razón.",
)

# ================================================================ OA 10
lesson(
    OA10, 1,
    "Las palabras y los chants escritos en cada ejercicio, un espejo pequeño y una persona de tu casa para repetir contigo. Si no hay audio, la persona lee las palabras en voz alta.",
    "Aprenderé a escuchar y producir el sonido /w/ del inglés, redondeando los labios, en palabras y en un chant muy breve. Sirve para que me entiendan mejor al hablar inglés.",
    ["Sé repetir palabras cortas en inglés.", "Sé que un sonido no es lo mismo que una letra."],
    [
        "El inglés tiene sonidos (sounds) que no son iguales a los del español. Uno es /w/. Para decirlo, redondea los labios como para soplar una vela y luego ábrelos rápido hacia la vocal siguiente. Suena como una «u» muy corta y rápida: water suena casi como «uóter».",
        "Cuidado con dos errores típicos. No digas «gu» fuerte: wet no es «guet». Tampoco lo cambies por /v/, que se hace con los dientes sobre el labio: wet y vet son palabras distintas. Mírate en un espejo: en /w/ los labios se redondean y los dientes no tocan el labio.",
        "Palabras con /w/: water (agua), window (ventana), week (semana), wet (mojado), west (oeste), wolf (lobo), worm (gusano), walk (caminar), we (nosotros). Las palabras what y where también empiezan con /w/. Un chant (canto rítmico) ayuda a practicar: repites las palabras con ritmo, aplaudiendo suave en cada palabra.",
    ],
    [("sound", "sonido"), ("/w/", "sonido con labios redondeados, como una u corta"), ("water", "agua"), ("window", "ventana"), ("walk", "caminar"), ("chant", "canto rítmico para practicar")],
    [
        ("Reconocer /w/", "¿Cuál de estas palabras empieza con /w/: sun, water, cat?", ["Digo cada palabra en voz alta.", "En water redondeo los labios al empezar.", "En sun y cat no."], "water"),
        ("Contar /w/ en un chant", "Chant: «We walk to the water. We see a wet worm.» ¿Cuántas palabras empiezan con /w/?", ["Leo palabra por palabra: We, walk, to, the, water.", "Sigo: We, see, a, wet, worm.", "Cuento las que empiezan con /w/: We, walk, water, We, wet, worm."], "6"),
    ],
    [
        ("Decir «guet» en lugar de wet.", "Se agrega una g que no existe.", "Redondea los labios y suelta la vocal rápido, sin g."),
        ("Cambiar /w/ por /v/ y decir vet.", "Vet es otra palabra, veterinario.", "En /w/ los dientes no tocan el labio."),
    ],
    [
        ("Elige la palabra que empieza con /w/: (a) water (b) sun", "a", "Water empieza con labios redondeados."),
        ("¿Qué significa «window»?", "Ventana", "Window es la palabra inglesa para ventana."),
        ("¿Cómo se ponen los labios para decir /w/? Elige: (a) redondeados (b) estirados en sonrisa", "a", "/w/ se hace con los labios redondeados."),
    ],
    [
        ("¿Cuál palabra empieza con /w/: week, tree, dog? Escríbela.", "week", "Week empieza con labios redondeados."),
        ("Palabras: wolf, bag, west, cup. ¿Cuántas empiezan con /w/? Escribe el número.", "2", "Solo wolf y west empiezan con /w/."),
        ("¿Qué significa «worm»?", "Gusano", "Worm es gusano y empieza con /w/."),
    ],
    [
        ("Chant: «We walk to the window.» ¿Cuántas palabras empiezan con /w/? Escribe el número.", "3", "We, walk y window empiezan con /w/."),
        ("Completa con una palabra con /w/ el chant: «We ___ to the park.» Opciones: walk / run.", "walk", "Walk empieza con /w/ y calza con la oración."),
        ("Palabras: wet, vet. Una de ellas empieza con /w/, la otra con /v/. ¿Cuál tiene los labios redondeados? Escríbela.", "wet", "Wet empieza con /w/."),
    ],
    [
        ("Luis dice «guet» para wet. ¿Qué parte debe corregir? Responde en español.", "Debe quitar la g y redondear los labios", "El sonido /w/ no lleva g."),
        ("Ema dice «vater» para water. ¿Qué sonido cambió? Responde en español.", "Cambió /w/ por /v/", "En water los dientes no tocan el labio."),
    ],
    [
        ("Palabras: window, bus, wolf, sit, worm. ¿Cuántas empiezan con /w/? Escribe el número.", "3", "Window, wolf y worm empiezan con /w/."),
        ("Chant: «Wolf, wolf, walk and walk. We want to talk.» (want es querer; talk es hablar). Cuenta las palabras con /w/. Cuéntalas dos veces. Escribe el número.", "6", "Wolf, wolf, walk, walk, We y want empiezan con /w/; and, to y talk no."),
    ],
    [("En la clase de inglés tu profesora escribe en la pizarra: water, window, week, tree, sun. Pide encerrar solo las palabras que empiezan con /w/. ¿Cuántas encierras?", "3", "Water, window y week empiezan con /w/.")],
    [
        ("¿Cómo se dice «agua» en inglés?", "water", "Water empieza con /w/."),
        ("¿Qué significa «chant»?", "Un canto rítmico para practicar", "Un chant se repite con ritmo."),
        ("¿Cuál palabra NO empieza con /w/: wet, walk, sun?", "sun", "Sun empieza con /s/."),
    ],
    task("Con una persona de tu casa y un espejo, practica este chant en voz baja y con ritmo suave: «We walk to the water. We see a wet worm. Walk, walk, walk. Water, water, water.» Primero lee cada palabra con /w/ mirando tus labios. Luego di el chant completo tres veces y subraya cuántas palabras con /w/ dijiste en la primera línea. Si una palabra no sale bien, repite solo esa palabra.", "En «We walk to the water» hay tres palabras con /w/: We, walk, water.", ["redondea los labios al decir /w/", "no agrega una g ni cambia por /v/", "dice el chant completo con ritmo", "cuenta bien las palabras con /w/ de la primera línea"], ["nota de la persona que escuchó el chant", "la línea subrayada en el papel"], ["decir guet", "cambiar /w/ por /v/"], "Elogia las palabras bien dichas y practica solo la que costó con el espejo."),
    "Di en voz alta water, window, week y worm frente a un espejo y mira tus labios.",
    "Inventa una frase corta con tres palabras que empiecen con /w/ y dila a una persona de tu casa.",
)

lesson(
    OA10, 2,
    "Las palabras escritas en cada ejercicio, un espejo y una persona de tu casa para escuchar. No muerdas la lengua ni uses los dedos: solo apóyala suavemente.",
    "Aprenderé a escuchar y producir el sonido /th/ del inglés, con la lengua entre los dientes, de forma segura. Sirve para decir palabras como think y this de manera comprensible.",
    ["Conozco el sonido /w/.", "Sé repetir palabras cortas en inglés."],
    [
        "El sonido /th/ no existe en el español de Chile. Para hacerlo, pon la punta de la lengua suavemente entre los dientes de adelante, sin morder, y deja salir el aire. No aprietes: la lengua solo toca los dientes. Mírate en un espejo para ver la punta de la lengua.",
        "Hay dos tipos. Uno es suave, sin vibración, como en think (pensar), three (tres), thank (agradecer), thin (delgado), thumb (pulgar), bath (baño de tina) y mouth (boca). El otro vibra en la garganta, como en this (esto), that (eso), the, they (ellos), mother (madre) y brother (hermano). Toca tu garganta con la mano: en este segundo tipo la sientes vibrar.",
        "Los errores típicos son decir /t/ (tree en vez de three), /s/ (sink en vez de think) o /d/ (dis en vez de this). Estas palabras cambian de significado: three es tres, pero tree es árbol; think es pensar, pero sink es lavaplatos. Por eso practicar /th/ ayuda a que te entiendan.",
    ],
    [("/th/", "sonido con la lengua entre los dientes"), ("think", "pensar"), ("three", "tres"), ("this", "esto"), ("mother", "madre"), ("bath", "baño de tina")],
    [
        ("Contar /th/ en una frase", "Frase: «I think this is the third bath.» (third es tercero). ¿Cuántas palabras tienen /th/?", ["Leo: I, think, this, is, the, third, bath.", "I e is no tienen /th/.", "Sí tienen: think, this, the, third, bath."], "5"),
        ("Palabras que cambian de significado", "¿Qué diferencia hay entre three y tree?", ["Three empieza con /th/.", "Tree empieza con /t/.", "Cada palabra tiene un significado."], "Three es tres y tree es árbol."),
    ],
    [
        ("Decir tree en lugar de three.", "Se cambia /th/ por /t/ y es otra palabra.", "Pon la lengua entre los dientes y deja salir el aire."),
        ("Morder la lengua con fuerza para hacer /th/.", "No es necesario y duele.", "Solo toca los dientes suavemente."),
    ],
    [
        ("¿Dónde pongo la punta de la lengua para decir /th/? Elige: (a) suavemente entre los dientes (b) detrás de los labios cerrados", "a", "/th/ se hace con la lengua entre los dientes."),
        ("¿Qué significa «three»?", "Tres", "Three es el número 3 en inglés."),
        ("¿Qué significa «mother»?", "Madre", "Mother tiene /th/ en el medio."),
    ],
    [
        ("¿Cuál palabra empieza con /th/: think, sink, tin? Escríbela.", "think", "Think empieza con /th/."),
        ("¿Cuál palabra empieza con /th/: tree, three? Escríbela.", "three", "Three tiene la lengua entre los dientes."),
        ("¿Qué palabra tiene /th/ al final: bath, bat? Escríbela.", "bath", "Bath termina con /th/."),
    ],
    [
        ("Frase: «Thank you, mother.» (thank you es gracias). ¿Cuántas palabras tienen /th/? Escribe el número.", "2", "Thank y mother tienen /th/."),
        ("Palabras: this, that, dog, they, cup. ¿Cuántas tienen /th/? Escribe el número.", "3", "This, that y they tienen /th/."),
        ("Completa con una palabra con /th/: «I ___ it is a good idea.» Opciones: think / sink.", "think", "Think significa pensar y tiene /th/."),
    ],
    [
        ("Pía dice «sink» cuando quiere decir think. ¿Qué cambió? Responde en español.", "Cambió /th/ por /s/", "Sink es otra palabra: lavaplatos."),
        ("Un niño dice «tree» y quería decir tres. ¿Qué debe hacer con la lengua? Responde en español.", "Ponerla entre los dientes", "Así produce /th/ en three."),
    ],
    [
        ("Frase: «The three brothers are thin.» (brothers son hermanos; thin es delgado). Cuenta las palabras con /th/. Cuéntalas dos veces.", "4", "The, three, brothers y thin tienen /th/."),
        ("Palabras: thumb, tub, bath, bag. ¿Cuántas tienen /th/? Escribe el número.", "2", "Thumb y bath tienen /th/."),
    ],
    [("Una profesora lee una lista de palabras: three, tree, think, sink, thank, tank. Quiere que levantes la mano solo en las palabras con /th/. ¿En cuántas palabras levantas la mano?", "3", "Three, think y thank tienen /th/.")],
    [
        ("¿Cómo se dice «gracias» en inglés con /th/? (palabra de la lista de la clase)", "thank you", "Thank empieza con /th/."),
        ("¿Qué significa «thin»?", "Delgado", "Thin empieza con /th/."),
        ("Si digo «tree» cuando quiero decir three, ¿qué sonido cambié? Responde: /th/ por /t/ o /t/ por /th/.", "/th/ por /t/", "Cambié /th/ por /t/ porque la lengua no está entre los dientes."),
    ],
    task("Con un espejo y una persona de tu casa, di cada palabra con la lengua suavemente entre los dientes: think, three, thank, thin, this, that, mother, brother. Luego di la frase «Thank you, mother. I think this bath is good.» y cuenta cuántas palabras tienen /th/. La persona escucha si dijiste tree o sink por error. Si es así, repite solo esa palabra.", "En la frase hay cinco palabras con /th/: Thank, mother, think, this, bath.", ["pone la lengua suavemente entre los dientes", "no cambia /th/ por /t/, /s/ o /d/", "dice la frase completa", "cuenta bien las palabras con /th/"], ["nota de la persona que escuchó las palabras", "tu conteo escrito"], ["decir tree por three", "morder la lengua"], "Muestra con el espejo dónde va la lengua y practica una palabra a la vez."),
    "Di three y tree cinco veces frente al espejo y nota la diferencia.",
    "Inventa una frase con cuatro palabras que tengan /th/ y practícala sin morder la lengua.",
)

lesson(
    OA10, 3,
    "Las palabras escritas en cada ejercicio y tu mano para sentir la vibración en la garganta. Una persona de tu casa puede escuchar.",
    "Aprenderé a diferenciar los sonidos /s/ y /z/ del inglés: uno sin vibración y otro con vibración en la garganta. Sirve para hablar y entender palabras como bus y buzz.",
    ["Conozco los sonidos /w/ y /th/.", "Sé repetir palabras cortas en inglés."],
    [
        "En español la letra s casi siempre suena /s/. En inglés existe además el sonido /z/, que suena como una abeja: zzz. Los dos se hacen casi igual, con la lengua cerca de los dientes. La diferencia es la voz: en /s/ solo sale aire, en /z/ la garganta vibra.",
        "Para comprobar, pon la mano suavemente en tu garganta. Di sss: no sientes vibración. Di zzz: sientes vibrar. Palabras con /s/: sun (sol), sit (sentarse), bus (bus), ice (hielo), face (cara). Palabras con /z/: zoo (zoológico), zip (cierre), zebra (cebra), buzz (zumbido), nose (nariz), rose (rosa).",
        "Atención: la letra s a veces suena /z/. En is, his y sees suena /z/. En los plurales también: cats (gatos) termina en /s/, pero dogs (perros) termina en /z/. Por eso no hay que fiarse solo de la letra: hay que escuchar. Hay pares de palabras que cambian de significado: sip y zip, bus y buzz, ice y eyes (ojos).",
    ],
    [("/s/", "sonido sin vibración, como una serpiente"), ("/z/", "sonido con vibración, como una abeja"), ("zoo", "zoológico"), ("bus", "bus"), ("buzz", "zumbido"), ("vibration", "vibración")],
    [
        ("Sentir la vibración", "Pones la mano en la garganta y dices zoo. ¿Sientes vibración? ¿Qué sonido es?", ["Digo zoo con la mano en la garganta.", "Siento vibración al empezar.", "La vibración es de /z/."], "Sí, hay vibración: es /z/."),
        ("Clasificar plurales", "¿Cats termina en /s/ o en /z/, y dogs?", ["Digo cats: sale aire sin voz.", "Digo dogs: la garganta vibra.", "Comparo los dos finales."], "Cats termina en /s/ y dogs en /z/."),
    ],
    [
        ("Decir /s/ cuando la palabra lleva /z/, como sebra en vez de zebra.", "Se pierde la vibración.", "Siente la garganta vibrar en /z/."),
        ("Pensar que la letra s siempre suena /s/.", "En is, his y dogs suena /z/.", "Escucha el sonido final y no solo la letra."),
    ],
    [
        ("¿Qué sonido vibra en la garganta: /s/ o /z/? Responde.", "/z/", "En /z/ la garganta vibra."),
        ("¿Qué significa «zoo»?", "Zoológico", "Zoo empieza con /z/."),
        ("¿Qué significa «buzz»?", "Zumbido", "Buzz termina con /z/."),
    ],
    [
        ("¿Cuál palabra empieza con /z/: sun, zip? Escríbela.", "zip", "Zip empieza con /z/."),
        ("¿Cuál palabra termina con /s/: bus, buzz? Escríbela.", "bus", "Bus termina con /s/ y buzz con /z/."),
        ("Sentir la garganta: ¿cats termina con vibración? Responde sí o no.", "No", "Cats termina con /s/, sin vibración."),
    ],
    [
        ("Palabras: sun, zoo, sit, zebra, bus. ¿Cuántas tienen /z/? Escribe el número.", "2", "Zoo y zebra tienen /z/."),
        ("Completa con una palabra con /z/: «Sam sees a ___ at the zoo.» Opciones: zebra / sock.", "zebra", "Zebra empieza con /z/."),
        ("Pares: sip / zip. ¿Cuál tiene vibración al empezar? Escríbela.", "zip", "Zip empieza con /z/."),
    ],
    [
        ("Pablo dice «sebra» para zebra. ¿Qué le falta? Responde en español.", "La vibración de /z/", "En /z/ la garganta vibra."),
        ("Ema dice que dogs termina igual que cats. ¿Tiene razón? Responde sí o no.", "No", "Dogs termina en /z/ y cats en /s/."),
    ],
    [
        ("Pares: ice / eyes. ¿Cuál termina en /z/? Escríbela.", "eyes", "Eyes termina en /z/ e ice en /s/."),
        ("Palabras: his, is, sun, rose. ¿Cuántas tienen /z/? Escribe el número.", "3", "His, is y rose tienen /z/; sun tiene /s/."),
    ],
    [("En el zoo de un libro ves los carteles: «zebra», «bus» y «zip». Debes subrayar los que empiezan con /z/. ¿Cuántos subrayas?", "2", "Zebra y zip empiezan con /z/; bus empieza con /b/.")],
    [
        ("¿Cómo se dice «cebra» en inglés?", "zebra", "Zebra empieza con /z/."),
        ("¿En qué se diferencian /s/ y /z/?", "En la vibración de la garganta", "/z/ vibra y /s/ no."),
        ("¿Qué sonido final tiene dogs?", "/z/", "Dogs termina con vibración."),
    ],
    task("Con la mano en la garganta y una persona de tu casa, practica estos pares: sip - zip, bus - buzz, ice - eyes. Di cada palabra y anota si sentiste vibración (V) o no (N). Luego completa este mini chant: «Sam sees a zebra at the zoo. Zip, zip, zip! Buzz, buzz, buzz!» y subraya con lápiz las palabras con /z/.", "sip N, zip V; bus N, buzz V; ice N, eyes V.", ["siente la vibración en /z/ y no en /s/", "anota bien V o N en cada palabra", "dice el chant completo", "subraya sees, zebra, zoo, zip y buzz (sees termina en /z/)"], ["la tabla de V y N", "nota de la persona que escuchó los pares"], ["decir /s/ en vez de /z/", "fiarse solo de la letra"], "Practica los pares con la mano en la garganta y elogia la vibración clara."),
    "Di sss y zzz con la mano en la garganta y nota la diferencia.",
    "Busca en casa tres palabras que conozcas en inglés con /z/ o /s/ y di cuál sonido tienen.",
)

lesson(
    OA10, 4,
    "Los chants escritos en cada ejercicio y una persona de tu casa para repetirlos contigo, aplaudiendo suave.",
    "Aprenderé a usar los sonidos /w/, /th/, /s/ y /z/ dentro de un chant con ritmo. Sirve para practicar los sonidos juntos y recordar palabras nuevas.",
    ["Conozco los sonidos /w/, /th/, /s/ y /z/."],
    [
        "Un chant es un texto corto con ritmo que se repite. Sirve para practicar sonidos. Un chant tiene versos (lines) y a veces rimas (rhymes): palabras que terminan con el mismo sonido, como day y way, o zoo y blue.",
        "Para practicar, lee el chant en voz baja y marca con color las palabras con el sonido que quieres entrenar. Luego dilo despacio, y después con ritmo, aplaudiendo suave en cada palabra importante. Repite las palabras con /th/ con la lengua entre los dientes, las palabras con /w/ con los labios redondeados y las de /z/ con vibración.",
        "Cuando un verso está incompleto, puedes completarlo con una palabra que rime y tenga sentido. Por ejemplo, «We see a zebra at the ___» se completa con zoo. Al terminar, di el chant completo, claro y sin apuro: lo importante es que se entienda.",
    ],
    [("chant", "canto rítmico"), ("line", "verso"), ("rhyme", "rima"), ("zoo - blue", "zoo y blue riman"), ("day - way", "day y way riman"), ("clap", "aplaudir")],
    [
        ("Completar un verso con rima", "Completa el verso del chant: «We see a zebra at the ___». La palabra debe rimar con blue y tener sentido con zebra.", ["Leo el verso.", "Busco una palabra que rime con blue.", "Compruebo que tenga sentido con zebra."], "zoo"),
        ("Marcar los sonidos", "Chant: «This is the way we walk.» ¿Qué palabras tienen /th/ y cuáles /w/?", ["Con /th/: This, the.", "Con /w/: way, we, walk.", "Marco cada grupo con un color."], "/th/: This, the. /w/: way, we, walk."),
    ],
    [
        ("Decir el chant muy rápido sin pronunciar los sonidos.", "No se entiende y no se practica.", "Dilo despacio primero, con sonidos claros."),
        ("Completar un verso con una palabra que rima pero no tiene sentido.", "La rima sola no basta.", "La palabra debe rimar y encajar con el verso."),
    ],
    [
        ("¿Qué significa «rhyme»?", "Rima", "Rhyme es palabras que terminan igual."),
        ("¿Qué palabra rima con zoo? Elige: (a) blue (b) sun", "a", "Zoo y blue terminan con el mismo sonido."),
        ("¿Qué significa «line» en un chant?", "Verso", "Line es una línea del chant."),
    ],
    [
        ("Chant: «Walk, walk, walk, we walk by the sea.» ¿Cuántas palabras empiezan con /w/? Escribe el número.", "5", "Walk tres veces, we y walk otra vez suman 5; by, the y sea no."),
        ("Chant: «Zip, zip, zip, buzz, buzz, buzz.» ¿Cuántas palabras tienen /z/? Escribe el número.", "6", "Las seis palabras tienen /z/."),
        ("Chant: «Think, think, think.» ¿Qué sonido practicas? Responde: /th/ o /w/.", "/th/", "Think empieza con /th/."),
    ],
    [
        ("Completa con una palabra con /w/: «We ___ to the park.» Opciones: walk / ride.", "walk", "Walk tiene /w/ y encaja en la frase."),
        ("Elige la palabra que rima con day: (a) way (b) bus", "a", "Day y way terminan con el mismo sonido."),
        ("Chant: «This is the thing.» ¿Cuántas palabras tienen /th/? Escribe el número.", "3", "This, the y thing tienen /th/."),
    ],
    [
        ("Luis completa «Sam sees a zebra at the sun». ¿Tiene sentido? Responde sí o no.", "No", "La frase correcta es at the zoo."),
        ("Ema dice que un chant debe decirse siempre muy rápido. ¿Tiene razón? Responde sí o no.", "No", "Primero se dice despacio para que se entienda."),
    ],
    [
        ("Chant: «Three wet worms walk with me.» ¿Cuántas palabras tienen /w/ o /th/? Cuéntalas dos veces.", "5", "Three, wet, worms, walk y with tienen /th/ o /w/; me no."),
        ("Chant: «Zoo, zoo, zebra, zip. Sit, sit, sun, sip.» ¿Cuántas palabras tienen /z/ y cuántas /s/? Responde con el formato 4 y 4.", "4 y 4", "Zoo, zoo, zebra y zip tienen /z/; sit, sit, sun y sip tienen /s/."),
    ],
    [("En el taller de música, para imitar el sonido de una abeja escribes la palabra «buzz» en tu chant. ¿La palabra buzz termina con el sonido /z/? Responde sí o no.", "Sí", "Buzz termina con /z/, el sonido de abeja.")],
    [
        ("¿Cómo se dice «rima» en inglés?", "rhyme", "Rhyme es rima."),
        ("¿Qué hago primero cuando practico un chant?", "Lo digo despacio", "Así los sonidos salen claros."),
        ("¿Qué palabra rima con blue? Elige: zoo / sun.", "zoo", "Blue y zoo terminan igual."),
    ],
    task("Practica este chant con una persona de tu casa: «Three wet worms walk with me. This is the way we walk. Zip, zip, zebra at the zoo. We say: Buzz, buzz, boo!» Primero subraya con colores las palabras con /w/, /th/ y /z/. Luego di el chant despacio y después con ritmo, aplaudiendo suave. La persona anota si se entendió cada línea.", "Con /w/: wet, worms, walk, with, we, way. Con /th/: Three, This, the, with. Con /z/: zip, zebra, zoo, Buzz.", ["marca las palabras con los tres sonidos", "dice el chant despacio y luego con ritmo", "repite /th/ con la lengua entre los dientes", "se entiende cada línea"], ["el chant subrayado", "nota de la persona que lo escuchó"], ["decir el chant muy rápido", "olvidar la vibración de /z/"], "Elogia las líneas claras y repite solo la línea que costó."),
    "Aplaude el ritmo de una línea del chant y di las palabras con /w/ en voz alta.",
    "Inventa un chant de dos versos con tres palabras que rimen y practica los sonidos.",
)

lesson(
    OA10, 5,
    "El diálogo escrito en esta clase, lápiz y una persona de tu casa que lea el papel B.",
    "Aprenderé a decir un diálogo muy breve en inglés con claridad, usando los sonidos /w/, /th/, /s/ y /z/. Sirve para que me entiendan cuando hablo con otras personas.",
    ["Conozco los sonidos /w/, /th/, /s/ y /z/.", "Sé decir un chant breve con ritmo."],
    [
        "Un diálogo (dialogue) es una conversación entre dos personas. Para que se entienda (intelligible), hay tres claves: hablar despacio, hacer pausas entre frases y decir claros los sonidos. No necesitas tener una pronunciación perfecta, pero sí que la otra persona te entienda.",
        "Este es el diálogo de la clase. A: «Hello! What is this?» B: «This is a zebra.» A: «Where is the zebra?» B: «The zebra is at the zoo. We can walk there.» Las palabras what, where, we y walk tienen /w/; this, the y there tienen /th/; zebra y zoo tienen /z/.",
        "Practica en tres pasos. Primero lee tu papel en voz baja. Luego léelo en voz alta con ritmo suave. Por último di el diálogo con otra persona, mirándola, con pausas. Si la otra persona no entiende una palabra, repítela más despacio y con el sonido claro.",
    ],
    [("dialogue", "diálogo"), ("intelligible", "que se entiende"), ("role", "papel, personaje que hago"), ("pause", "pausa"), ("slowly", "despacio"), ("repeat", "repetir")],
    [
        ("Reconocer sonidos en el diálogo", "En «The zebra is at the zoo», ¿qué palabras empiezan con /z/ y cuáles con /th/?", ["Con /z/: zebra, zoo.", "Con /th/: The, the.", "Las demás no tienen esos sonidos."], "Con /z/: zebra, zoo. Con /th/: The, the."),
        ("Repetir con claridad", "La otra persona no entendió zoo. ¿Qué haces?", ["Repito la palabra despacio.", "Hago la vibración de /z/.", "Miro a la persona y hago una pausa."], "Repito zoo despacio, con /z/ claro."),
    ],
    [
        ("Leer el diálogo sin pausas y muy rápido.", "La otra persona no alcanza a entender.", "Haz pausas entre frases y habla despacio."),
        ("Pensar que debo hablar perfecto para que me entiendan.", "No es necesario.", "Lo importante es que los sonidos sean claros y se entienda el mensaje."),
    ],
    [
        ("¿Qué significa «dialogue»?", "Diálogo, una conversación entre dos personas", "Dialogue se parece a diálogo."),
        ("¿Qué significa «intelligible»?", "Que se entiende", "Un diálogo intelligible se entiende."),
        ("¿Qué significa «slowly»?", "Despacio", "Hablar slowly ayuda a que te entiendan."),
    ],
    [
        ("Diálogo: A: «Where is the zebra?» ¿Quién pregunta dónde está la cebra? Escribe la letra.", "A", "A hace la pregunta con Where."),
        ("Diálogo: B: «This is a zebra.» ¿Qué sonido tiene la palabra zebra al empezar? Responde: /s/ o /z/.", "/z/", "Zebra empieza con /z/."),
        ("¿Qué haces si la otra persona no entiende una palabra? Elige: (a) la repito despacio (b) la digo más rápido", "a", "Repetir despacio ayuda a entender."),
    ],
    [
        ("Completa B: «The zebra is at the ___.»", "zoo", "El diálogo dice at the zoo."),
        ("Palabras del diálogo: what, where, we, walk, this, the. ¿Cuántas tienen /w/? Escribe el número.", "4", "What, where, we y walk empiezan con /w/."),
        ("Palabras del diálogo: this, the, there, zoo. ¿Cuántas tienen /th/? Escribe el número.", "3", "This, the y there tienen /th/."),
    ],
    [
        ("Ana dice el diálogo sin pausas y la otra persona no entiende. ¿Qué debe mejorar? Responde en español.", "Hacer pausas y hablar despacio", "Así la otra persona entiende cada frase."),
        ("Leo dice «sebra» para zebra. ¿Qué sonido debe mejorar? Responde: /z/ o /w/.", "/z/", "Zebra empieza con /z/ con vibración."),
    ],
    [
        ("Ordena las palabras para formar la pregunta de A: is / Where / zebra / the. Escríbela.", "Where is the zebra?", "La pregunta empieza con Where."),
        ("Elige la mejor respuesta de B: (a) «The zebra is at the zoo.» (b) «The zebra is a bus.»", "a", "Tiene sentido con la pregunta Where."),
    ],
    [("En un teatro de títeres tu amigo dice la parte de A y tú la de B. A pregunta: «What is this?» Elige tu respuesta: (a) «This is a zebra.» (b) «We can walk there.»", "a", "La pregunta What is this? se responde diciendo qué es.")],
    [
        ("¿Cómo se dice «papel o personaje» en inglés?", "role", "Role es el papel que hago."),
        ("¿Qué tres cosas ayudan a que se entienda un diálogo?", "Hablar despacio, hacer pausas y decir claros los sonidos", "Son las tres claves de la clase."),
        ("¿Qué palabra de «We can walk there» tiene /th/?", "there", "There empieza con /th/."),
    ],
    task("Con una persona de tu casa, digan este diálogo dos veces, cambiando de papel. A: «Hello! What is this?» B: «This is a zebra.» A: «Where is the zebra?» B: «The zebra is at the zoo. We can walk there.» Antes, subrayen las palabras con /w/ y /th/ y marquen con otro color las de /z/. Hablen despacio, con pausas, mirándose. Después de cada vuelta, la otra persona dice qué palabra costó entender y la repiten.", "Primera vuelta: yo hago A y la otra persona B. Segunda vuelta: cambiamos. En ambas repito despacio zoo y zebra con /z/.", ["dice el diálogo completo en ambos papeles", "hace pausas entre frases", "pronuncia con claridad /w/, /th/ y /z/", "repite una palabra difícil más despacio"], ["nota de la persona con la palabra que costó entender", "el diálogo subrayado"], ["hablar muy rápido", "no repetir una palabra que no se entendió"], "Pregunta qué palabra costó, practícala tres veces y vuelve a decir la línea completa."),
    "Lee en voz alta solo tu papel del diálogo, despacio.",
    "Escribe una pregunta y una respuesta de tu invención con una palabra con /w/ y una con /th/ y dilas con claridad.",
)
