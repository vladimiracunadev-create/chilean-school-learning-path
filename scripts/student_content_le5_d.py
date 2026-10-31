"""Cuaderno del estudiante, 5.º básico Lenguaje y Comunicación: OA 27 (convenciones sociales y registro)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA27 = "LE05 OA 27"
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


# ================================================================ OA 27 · clase 1
reg(
    OA27, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para practicar en voz alta las situaciones.",
    "Aprenderé a reconocer para qué sirve cada fórmula de cortesía (por favor, gracias, perdón, permiso) y a elegir la que corresponde a cada situación. Sirve para que los demás se sientan respetados cuando hablo con ellos.",
    ["Sé saludar y despedirme.", "Sé que hablar con otras personas tiene reglas de respeto."],
    [
        "Las convenciones sociales son acuerdos no escritos sobre cómo nos tratamos en cada situación. Las usamos todos los días: saludar al llegar, esperar el turno, agradecer. Dentro de ellas están las fórmulas de cortesía, que son palabras breves que muestran respeto. Las cuatro más comunes son «por favor», «gracias», «perdón» y «permiso».",
        "Cada fórmula tiene un propósito. «Por favor» suaviza un pedido. «Gracias» reconoce lo que otra persona hizo por nosotros. «Perdón» sirve para reconocer un error o una molestia. «Permiso» se usa antes de pasar, entrar o usar algo que no es nuestro. El desafío es elegir la fórmula según lo que está pasando y no repetirlas sin pensar.",
        "También importa cómo se dicen. Una fórmula de cortesía dicha con voz de burla o sin mirar a la persona no cumple su propósito. Para que funcione, la palabra, el tono y la actitud deben ir de acuerdo: quien dice «gracias» debe mostrar que de verdad agradece.",
    ],
    [("convención social", "acuerdo sobre cómo tratarnos en cada situación"), ("fórmula de cortesía", "palabra breve que muestra respeto, como «gracias»"), ("propósito", "para qué se dice algo"), ("tono", "manera de la voz al decir algo"), ("situación", "lo que ocurre en un momento y lugar")],
    [
        ("Elegir la fórmula", "Camila quiere pasar entre dos compañeros que conversan en el pasillo. ¿Qué fórmula usa?", ["Veo qué quiere hacer: pasar por un lugar ocupado.", "Para pasar se avisa antes.", "La fórmula que avisa es «permiso»."], "Permiso."),
        ("Reconocer el propósito", "Tomás pisa sin querer el cuaderno de Rosa. Dice: «Perdón, no me di cuenta». ¿Para qué usó «perdón»?", ["Busco qué pasó: pisó el cuaderno sin querer.", "Hubo una molestia.", "Con «perdón» reconoce el error."], "Para reconocer que se equivocó y molestó sin querer."),
    ],
    [("Pedir algo sin ninguna fórmula, solo con una orden.", "Se cree que lo importante es conseguir lo que se necesita.", "Agrega «por favor» y usa una pregunta: «¿Me prestas el lápiz, por favor?»."), ("Decir «gracias» con burla o sin mirar.", "Se piensa que basta pronunciar la palabra.", "Dilo mirando a la persona y con un tono sincero.")],
    [
        E("Matías le pasa un cuaderno a Ema y ella dice «gracias». ¿Para qué usa esa palabra: para pedir algo o para agradecer?", "Para agradecer", "«Gracias» reconoce lo que la otra persona hizo."),
        E("Necesitas que te presten una regla. ¿Qué fórmula agregas al pedirla?", "Por favor", "«Por favor» suaviza un pedido."),
        E("Empujas sin querer a un compañero en la fila. ¿Qué dices: a) «Perdón» b) «Por favor»?", "a", "«Perdón» reconoce una molestia que no fue a propósito."),
    ],
    [
        E("¿Qué fórmula conviene usar antes de pasar entre dos personas que conversan: a) gracias b) permiso c) por favor?", "b", "«Permiso» avisa que quieres pasar por un lugar ocupado."),
        E("De estos dos pedidos, ¿cuál es más cortés: a) «Ayúdame con la mochila.» b) «¿Me ayudas con la mochila, por favor?»", "b", "Usa pregunta y «por favor», lo que suaviza el pedido."),
        E("Una profesora te devuelve tu prueba corregida. ¿Qué fórmula corresponde decir al recibirla?", "Gracias", "Se reconoce lo que ella hizo por ti."),
    ],
    [
        E("Completa con una fórmula de cortesía: «______, ¿puedo entrar a la sala?». Opciones: permiso / gracias.", "Permiso", "Antes de entrar a un lugar se pide permiso."),
        E("Ordena una petición cortés. a) Gracias. b) ¿Me prestas tu borrador, por favor? c) Toma, aquí lo tienes. Escribe las letras.", "b, c, a", "Primero se pide, luego se entrega y al final se agradece."),
        E("¿Cuál frase usa dos fórmulas de cortesía? a) «Perdón, ¿me das permiso para pasar?» b) «Pásame eso.» c) «Ya, listo.»", "a", "Tiene «perdón» y «permiso»."),
    ],
    [
        E("Sofía dice «gracias» mirando hacia otro lado, con voz seca. Su compañero queda incómodo. ¿Qué falló: a) la palabra b) el tono y la actitud?", "b", "La palabra era correcta; faltó que el tono mostrara agradecimiento."),
        E("Nico dice «por favor» siempre, pero si le dicen que no, grita y se enoja. ¿Basta con decir las fórmulas para ser cortés? Responde sí o no.", "No", "La cortesía también necesita respeto en la actitud."),
    ],
    [
        E("Llegas atrasado y la profesora ya explica. ¿Qué es más adecuado: a) entrar en silencio sin decir nada b) esperar en la puerta, decir «permiso, perdón por llegar tarde» y sentarte sin hacer ruido c) entrar corriendo y preguntar la hora?", "b", "Pide permiso, reconoce el atraso y cuida la clase."),
        E("Ordena lo que dices en un pasillo angosto. a) «Gracias.» b) «Permiso.» c) Pasas con cuidado cuando se mueven. Escribe las letras.", "b, c, a", "Primero avisas, luego pasas y al final agradeces."),
    ],
    [E("En el comedor de la escuela quieres que una compañera te pase la sal. Ella te la pasa. ¿Qué dos fórmulas usas y en qué orden?", "Por favor al pedirla y gracias al recibirla", "Se pide con cortesía y luego se agradece.")],
    [
        E("¿Qué fórmula se dice al recibir algo?", "Gracias", "Reconoce lo que otra persona hizo por ti."),
        E("¿Qué fórmula se usa antes de pasar por un lugar estrecho o de entrar a una sala?", "Permiso", "Avisa y pide autorización."),
        E("¿Sirve «perdón» para reconocer un error sin mala intención? Responde sí o no.", "Sí", "Así reconoces la molestia que causaste."),
    ],
    ("Practica en voz alta estas tres escenas y anota qué dirías en cada una: 1) quieres usar el sacapuntas de un compañero; 2) alguien te sostiene la puerta; 3) mojaste sin querer el cuaderno de una amiga con tu botella. Usa una fórmula distinta en cada escena y dilo con el tono que corresponde. Si puedes, practica con una persona de tu casa y pregúntale si sonó sincero.",
     "1) «¿Me prestas el sacapuntas, por favor?». 2) «Gracias por sostener la puerta». 3) «Perdón, no fue mi intención; te ayudo a secarlo».",
     ["usa una fórmula distinta en cada escena", "la fórmula corresponde al propósito", "el tono es sincero y respetuoso"], ["tres frases escritas o dichas"], ["usar «perdón» para pedir algo", "decir solo una orden sin fórmula"],
     "Si una fórmula no calza, pregúntate: ¿qué quiero lograr con esta frase: pedir, agradecer, disculparme o pasar?"),
    "Escribe otras dos situaciones de tu día en que usarías «gracias» y «permiso», y la frase exacta que dirías.",
    "Observa durante un día cuántas veces oyes fórmulas de cortesía en tu casa o escuela y anota en qué situaciones aparecen.",
)

# ================================================================ OA 27 · clase 2
reg(
    OA27, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: dos personas de tu casa para practicar presentaciones.",
    "Aprenderé a presentarme y a presentar a otras personas con un saludo adecuado, sin entregar datos privados. Sirve para comenzar bien una conversación en un curso, un taller o una visita.",
    ["Sé usar fórmulas de cortesía.", "Sé que hay datos personales que no se comparten con desconocidos."],
    [
        "Presentarse es decir quién eres para que otros te conozcan. Una buena presentación lleva un saludo, tu nombre y uno o dos datos que ayuden a conversar, como tu curso o algo que te gusta. Por ejemplo: «Hola, me llamo Ana, estoy en quinto básico y me gusta dibujar». Después se responde con «mucho gusto» o «encantado».",
        "Presentar a otros es decir a dos personas quiénes son para que se conozcan. Se dice el saludo, el nombre de cada una y cómo la conoces: «Sara, te presento a Rubén, mi compañero de curso». Con una persona mayor o de cargo, como una directora, se usa un trato más formal: «Directora, le presento a mi compañero Rubén».",
        "El saludo cambia con la hora: «buenos días» en la mañana, «buenas tardes» después del mediodía y «buenas noches» al anochecer. Además, al presentarte no debes decir datos privados, como tu dirección o tus claves. Eso solo se comparte con personas de confianza.",
    ],
    [("presentarse", "decir quién eres para que otros te conozcan"), ("presentar a otros", "decir a dos personas quiénes son para que se conozcan"), ("trato formal", "manera respetuosa de hablar, por ejemplo con «usted»"), ("dato privado", "información que no se comparte con desconocidos"), ("mucho gusto", "frase de bienvenida al conocer a alguien")],
    [
        ("Presentarse bien", "Daniela llega a un taller de teatro y dice: «Hola, me llamo Daniela, estoy en quinto básico y me gusta cantar». ¿Qué partes tiene su presentación?", ["Busco el saludo: «Hola».", "Luego su nombre y su curso.", "Al final dice algo que le gusta."], "Saludo, nombre, curso y un gusto."),
        ("Presentar a otro", "Quieres presentar a tu compañero Luis con la directora del colegio. ¿Qué frase usas?", ["Con una directora uso trato formal.", "Digo su cargo y le hablo de «usted».", "«Directora, le presento a mi compañero Luis.»"], "«Directora, le presento a mi compañero Luis.»"),
    ],
    [("Decir la dirección o las claves al presentarse.", "Se piensa que presentarse es contar todo sobre uno.", "Di nombre, curso y un gusto; guarda los datos privados."), ("Presentar a alguien solo con «él» o «ella».", "Se cree que la otra persona ya sabe quién es.", "Di su nombre y cómo la conoces.")],
    [
        E("Son las 9 de la mañana. ¿Qué saludo corresponde: «buenos días» o «buenas noches»?", "Buenos días", "Es de mañana."),
        E("En «Hola, me llamo Ana y estoy en quinto básico», ¿cuál es el nombre de quien habla?", "Ana", "Lo dice después de «me llamo»."),
        E("Después de conocer a alguien se dice «mucho gusto». ¿Para qué sirve: a) para mostrar que nos alegra conocerla b) para pedir permiso?", "a", "Es una frase de bienvenida."),
    ],
    [
        E("En un primer día de taller, ¿qué conviene decir de ti: a) tu nombre y tu curso b) la dirección de tu casa y la clave del computador?", "a", "La dirección y las claves son datos privados."),
        E("¿Qué frase presenta bien a tu compañero Luis con una vecina, la señora Rosa: a) «Señora Rosa, le presento a mi compañero Luis.» b) «Señora Rosa, él.»", "a", "Dice el nombre y cómo lo conoces."),
        E("A las 5 de la tarde saludas a la bibliotecaria. ¿Qué saludo usas: buenos días, buenas tardes o buenas noches?", "Buenas tardes", "Después del mediodía y antes del anochecer se dice «buenas tardes»."),
    ],
    [
        E("Ordena la presentación. a) «Hola, Sara.» b) «Sara, te presento a Rubén, mi compañero de curso.» c) «Mucho gusto, Rubén.» Escribe las letras.", "a, b, c", "Primero se saluda, luego se presenta y al final se responde."),
        E("Visitas un colegio y te presentas a la directora. ¿Cuál es más adecuada: a) «Buenos días, directora. Me llamo Joaquín y soy alumno de quinto.» b) «Hola, ¿qué onda? Soy el Joaco.»", "a", "Con una directora se usa un saludo y un trato formal."),
        E("En «Me llamo Dani, tengo diez años y me gusta dibujar», ¿cuántas cosas dice Dani sobre sí mismo, contando su nombre?", "Tres", "Dice su nombre, su edad y un gusto."),
    ],
    [
        E("Mario se presenta: «Soy Mario, vivo en el pasaje Los Aromos número 345 y mi clave del computador es 1234». ¿Qué debería callar y por qué?", "La dirección y la clave, porque son datos privados", "No se comparten con quienes recién conoces."),
        E("Una niña nueva solo dice «Hola» y se queda callada. Otra dice «Hola, me llamo Eli, ¿cómo te llamas?». ¿Cuál facilita iniciar una conversación y por qué?", "La segunda, porque pregunta el nombre", "La pregunta invita a responder."),
    ],
    [
        E("En una reunión formal de apoderados presentas a una vecina con tu profesora. ¿Qué frase es más adecuada: a) «Profe, mi vecina, ella.» b) «Profesora, le presento a mi vecina, la señora Carmen.»", "b", "Nombra a ambas y usa trato formal."),
        E("Un compañero dice: «Presentarse es decir todo sobre uno». ¿Estás de acuerdo? Responde sí o no.", "No", "Se dice lo que ayuda a conocerse y se guardan los datos privados."),
    ],
    [E("Llegas a un campamento escolar y te piden presentarte en 20 segundos. ¿Cuál presentación cumple: a) «Hola, me llamo Pía, estoy en quinto y me gusta la natación.» b) «Soy Pía.» c) «Hola, vivo en la calle Los Pinos y mi mamá trabaja de noche.»", "a", "Tiene saludo, nombre, curso y un gusto, sin datos privados.")],
    [
        E("¿Qué saludo se usa a las 8 de la mañana?", "Buenos días", "Es el saludo de la mañana."),
        E("¿Se debe decir la dirección de la casa al presentarse ante desconocidos? Responde sí o no.", "No", "Es un dato privado."),
        E("En «Sara, te presento a Rubén, mi compañero de curso», ¿qué parte dice cómo conoces a Rubén?", "Mi compañero de curso", "Dice qué relación tienes con él."),
    ],
    ("Escribe y practica en voz alta dos presentaciones. A) Presentarte ante un curso nuevo de un taller: saludo, nombre, curso y un gusto. B) Presentar a tu amigo Felipe con una persona adulta que visita tu casa: saludo, nombres y cómo lo conoces. No incluyas datos privados. Pide a una persona de tu casa que te diga si se entendió quién eres y quién es Felipe.",
     "A) «Buenos días. Me llamo Lía, estoy en quinto básico y me gusta jugar básquetbol». B) «Señor Gómez, le presento a mi amigo Felipe, mi compañero de curso».",
     ["tiene saludo y nombre", "incluye un dato útil sin ser privado", "presenta a ambas personas por su nombre"], ["dos presentaciones escritas o dichas"], ["entregar datos privados", "presentar sin decir los nombres"],
     "Si faltan datos, revisa tu lista: ¿dije saludo, nombre y cómo conozco a la otra persona?"),
    "Escribe cómo te presentarías ante un grupo de niños de otro curso y cómo presentarías a un compañero ante tu profesor o profesora.",
    "Anota los saludos que usan en tu casa según la hora del día y compáralos con los de este cuaderno.",
)

# ================================================================ OA 27 · clase 3
reg(
    OA27, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer los diálogos con voces distintas.",
    "Aprenderé a preguntar con cortesía y a encontrar en un diálogo las pistas que muestran cómo se tratan las personas: saludo, fórmulas, trato y tono. Sirve para elegir bien mis palabras en cada situación.",
    ["Sé usar fórmulas de cortesía.", "Sé presentarme y saludar."],
    [
        "Preguntar es una forma de interactuar: pedimos información o ayuda. Una pregunta cortés lleva un saludo o una fórmula y dice con claridad lo que se necesita. Por ejemplo: «Disculpe, ¿me puede decir dónde está la biblioteca?». Compárala con «¿Dónde está la biblioteca?»: ambas preguntan lo mismo, pero la primera muestra más respeto.",
        "En un diálogo hay pistas que muestran cómo se relacionan las personas. Una pista es una palabra o expresión que ayuda a deducir algo. El saludo, las fórmulas de cortesía, el uso de «tú» o «usted» y títulos como «señora» o «profesor» muestran el vínculo y el nivel de respeto. Para encontrar la pista, buscamos la frase exacta del diálogo que respalda lo que decimos.",
        "Por eso, cuando nos preguntan «¿cómo sabes que…?», respondemos con evidencia: citamos las palabras del diálogo. Así no solo opinamos que alguien fue cortés, sino que mostramos en qué frase se ve.",
    ],
    [("pregunta cortés", "pregunta que lleva saludo o fórmula y es clara"), ("pista", "palabra o frase que ayuda a deducir algo"), ("vínculo", "relación entre dos personas"), ("usted", "forma de hablar con respeto a una persona mayor o de cargo"), ("evidencia", "frase del texto que respalda lo que decimos")],
    [
        ("Encontrar la fórmula", "Diálogo: Niño: «Buenas tardes, señora Elena. Disculpe, ¿me puede ayudar a encontrar un libro de insectos?». Bibliotecaria: «Claro, está en el estante azul». Niño: «Muchas gracias». ¿Qué fórmula usa el niño para agradecer?", ["Busco la frase de cierre del niño.", "Dice «Muchas gracias».", "Esa es la fórmula de agradecimiento."], "«Muchas gracias»."),
        ("Deducir el vínculo", "En el diálogo anterior, el niño llama a la bibliotecaria «señora Elena» y le habla de «usted» (¿me puede ayudar?). ¿Qué pista muestra que usa un trato respetuoso?", ["Miro cómo la llama: «señora Elena».", "También mira el verbo: «puede», no «puedes».", "Ambas son pistas de trato formal."], "El título «señora» y el uso de «usted»."),
    ],
    [("Decir que alguien fue cortés sin mostrar en qué frase.", "Se responde por impresión y no por evidencia.", "Cita la palabra exacta: por ejemplo «disculpe» o «gracias»."), ("Creer que toda pregunta cortés debe ser larga.", "Se confunde cortesía con exceso de palabras.", "Basta una fórmula y una pregunta clara.")],
    [
        E("Diálogo: Ana: «Hola, Sebastián. ¿Me prestas tu regla, por favor?». Sebastián: «Toma». Ana: «Gracias». ¿Qué fórmula usa Ana para pedir?", "Por favor", "Aparece en su pregunta."),
        E("En el mismo diálogo, ¿qué palabra de Ana agradece?", "Gracias", "Es la última palabra que dice."),
        E("¿Cuál pregunta es más cortés: a) «Disculpe, ¿me puede decir la hora?» b) «¿La hora?»", "a", "Lleva una fórmula y una pregunta completa."),
    ],
    [
        E("Diálogo: Mateo: «Buenos días, profesor Iván. Permiso, ¿puedo guardar mi trabajo en su escritorio?». Profesor: «Sí, déjalo ahí». ¿Qué saludo y qué fórmula de cortesía usa Mateo?", "Buenos días y permiso", "Saluda y pide permiso."),
        E("En el diálogo anterior, ¿qué palabra muestra que Mateo respeta al profesor al llamarlo: a) profesor b) Iván a secas?", "a", "El título «profesor» muestra respeto."),
        E("¿Cuál pregunta es cortés y clara: a) «Buenas tardes, ¿me indica dónde está el baño, por favor?» b) «¿Baño?» c) «Dime dónde está el baño.»", "a", "Tiene saludo, fórmula y un pedido completo."),
    ],
    [
        E("Diálogo: Vicky: «Tío Raúl, ¿me ayudas a subir la bolsa, por favor?». Tío: «Claro, mi niña». ¿Qué pista muestra que Vicky habla de «tú» con su tío: a) «ayudas» b) «bolsa»?", "a", "El verbo «ayudas» es de «tú»; con «usted» sería «ayuda»."),
        E("Camilo dice: «Disculpe, señora, ¿puede pasarme mi mochila?». ¿Qué palabra marca el trato respetuoso hacia la señora: a) «Disculpe» b) «mochila»?", "a", "«Disculpe» es una fórmula de respeto."),
        E("Ordena la conversación en un mostrador. a) «Con gusto, aquí tiene.» b) «Buenas tardes, ¿me puede dar un cuaderno de cuadros, por favor?» c) «Gracias.» Escribe las letras.", "b, a, c", "Primero pide, después le entregan y al final agradece."),
    ],
    [
        E("Dos niños responden a «¿Quién fue cortés?». Uno dice «Lía, porque fue amable». El otro dice «Lía, porque dijo ‘disculpe’ y ‘gracias’». ¿Quién usó evidencia del diálogo?", "El segundo", "Cita palabras exactas del diálogo."),
        E("Rosa le dice a su vecina de ochenta años: «Oye, ¿me pasai el pan?». ¿Cuál es la mejor corrección: a) «Señora, ¿me puede pasar el pan, por favor?» b) «Oye, pásame el pan.»", "a", "Con una persona mayor se usa «usted» y una fórmula de cortesía."),
    ],
    [
        E("Diálogo: Pedro: «Perdón, joven, ¿esta fila es para el bus?». Joven: «Sí, señor». ¿Qué palabra del joven muestra respeto hacia Pedro?", "Señor", "Lo trata con un título de respeto."),
        E("En una fila, un niño le dice a otro: «Disculpa, ¿me dejas pasar?». ¿Cuál es el pedido concreto que hace?", "Que lo deje pasar", "Después de la fórmula dice qué necesita."),
    ],
    [E("Lees este diálogo: Julia: «Buenas tardes, señor Marcos. ¿Podría decirme si llegó el paquete?». Marcos: «Sí, ya lo dejaron en la entrada». Julia: «Muchas gracias». ¿Qué palabra de Julia muestra que lo trata de «usted»: a) «podría» b) «paquete»?", "a", "«Podría» es la forma de «usted»; con «tú» diría «podrías».")],
    [
        E("¿Qué fórmula usa quien pide un favor y quiere ser cortés?", "Por favor", "Suaviza el pedido."),
        E("¿Cómo respaldas que alguien fue cortés: citando una frase o diciendo ‘me parece’? Responde con una de las dos opciones.", "Citando una frase", "La evidencia es la palabra exacta del diálogo."),
        E("«Señora» y «usted» son pistas de trato formal. Responde sí o no.", "Sí", "Muestran respeto hacia la otra persona."),
    ],
    ("Lee este diálogo: Tomás: «Hola, don Lalo. Disculpe, ¿me podría vender dos huevos, por favor?». Don Lalo: «Claro, aquí tienes». Tomás: «Muchas gracias». Subraya o copia dos frases que muestren cortesía y una que muestre el vínculo (cómo trata Tomás a don Lalo). Luego escribe una pregunta cortés que Tomás haría para saber cuánto cuesta una bolsa de pan.",
     "Cortesía: «Disculpe» y «Muchas gracias». Vínculo: lo trata de «don» y de «usted» (¿me podría vender?). Pregunta: «Disculpe, don Lalo, ¿me podría decir cuánto cuesta la bolsa de pan?».",
     ["cita dos frases del diálogo", "explica el vínculo con una pista", "escribe una pregunta cortés y clara"], ["tres frases copiadas y una pregunta escrita"], ["resumir sin citar", "escribir una pregunta sin fórmula"],
     "Para mejorar, comprueba que cada afirmación tenga una frase del diálogo que la respalde."),
    "Escribe una pregunta cortés para cada una de estas personas: tu profesora, un niño más pequeño y una vecina mayor.",
    "Fíjate en cómo se tratan dos personas en una conversación que oigas y anota dos pistas de su trato.",
)

# ================================================================ OA 27 · clase 4
reg(
    OA27, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para decir en voz alta las dos versiones de cada mensaje.",
    "Aprenderé a comparar el registro formal y el informal y a decidir cuál usar según con quién hablo y en qué situación. Sirve para hablar con respeto a una persona adulta y con confianza a un amigo.",
    ["Sé que hay trato de «tú» y de «usted».", "Sé usar fórmulas de cortesía."],
    [
        "El registro es la manera de hablar que elegimos según la situación. El registro formal se usa con personas que no conocemos, con adultos o en ocasiones oficiales, como una reunión o una carta a la directora. Usa «usted» o frases completas, evita bromas y trae saludos y despedidas. El registro informal se usa con amigos o familiares de confianza: es más relajado y usa «tú».",
        "Elegir el registro depende de cuatro cosas: con quién hablo (vínculo), dónde estoy, por qué medio hablo (en persona, por mensaje o carta) y qué quiero lograr. Un mismo mensaje puede decirse de dos formas. Informal: «Oye, ¿me prestas tu cuaderno?». Formal: «Profesora, ¿podría prestarme su cuaderno, por favor?».",
        "Equivocar el registro puede sonar descortés, aunque no queramos. Si le hablo a mi directora como a mi amigo, puede parecer falta de respeto; si le hablo a mi amigo con frases muy formales, puede parecer distante. Comparar versiones nos ayuda a decidir cuál conviene.",
    ],
    [("registro", "manera de hablar según la situación"), ("registro formal", "el que se usa con adultos o en ocasiones oficiales"), ("registro informal", "el que se usa con amigos y personas de confianza"), ("medio", "canal por el que se comunica, como mensaje o carta"), ("vínculo", "relación entre quienes hablan")],
    [
        ("Comparar dos versiones", "Versión A: «Oye, ¿me prestas tu cuaderno?». Versión B: «Profesora, ¿podría prestarme su cuaderno, por favor?». ¿Cuál es formal y qué pista lo muestra?", ["Miro cómo se dirige a la otra persona.", "En B usa «profesora» y «usted» (su cuaderno).", "En A usa «oye» y «tu»."], "La B; llama «profesora» y habla de «usted»."),
        ("Elegir para la situación", "Escribes una carta a la directora para pedir permiso para una visita. ¿Qué registro usas?", ["La directora es una autoridad escolar.", "Es una carta oficial.", "Corresponde el registro formal."], "Formal."),
    ],
    [("Usar siempre el mismo registro en todas las situaciones.", "Se cree que hablar así es más natural.", "Pregúntate con quién hablas y en qué situación, y ajusta."), ("Creer que lo formal es lo mismo que hablar difícil.", "Se piensa que hay que usar palabras rebuscadas.", "Lo formal es claro, respetuoso y cuidado, sin palabras innecesarias.")],
    [
        E("¿Qué registro usas con un amigo de tu edad en el recreo: formal o informal?", "Informal", "Entre amigos hay confianza."),
        E("¿Qué registro usas para hablar con la directora en una reunión: formal o informal?", "Formal", "Es una autoridad y una situación oficial."),
        E("¿Cuál de estas frases es informal: a) «Buenos días, señor, ¿podría ayudarme?» b) «Oye, ¿me ayudas?»", "b", "Usa «oye» y «tú»."),
    ],
    [
        E("¿Cuál frase usa «usted»: a) «¿Me puede pasar el libro, por favor?» b) «¿Me puedes pasar el libro?»", "a", "El verbo «puede» corresponde a «usted»."),
        E("Mandas un mensaje a tu mejor amiga para invitarla a jugar. ¿Qué registro conviene: a) formal b) informal?", "b", "Hay confianza con tu amiga."),
        E("¿De qué depende elegir el registro: a) del vínculo, el lugar, el medio y el propósito b) solo del color de la ropa?", "a", "Son los cuatro aspectos de la situación."),
    ],
    [
        E("Cambia a registro formal: «Oye, ¿tienes hora?». ¿Qué versión es correcta: a) «Disculpe, ¿tiene hora?» b) «Oye, ¿qué hora es?»", "a", "Usa una fórmula y «usted»."),
        E("Ordena de más informal a más formal. a) «Disculpe, ¿podría indicarme la hora?» b) «Oye, ¿qué hora es?» c) «Perdón, ¿tienes hora?» Escribe las letras.", "b, c, a", "«Oye» es lo más informal; «podría indicarme» es lo más formal."),
        E("¿Qué frase de despedida es formal: a) «Chao, nos vemos» b) «Que tenga un buen día»?", "b", "Usa «tenga», que es forma de «usted»."),
    ],
    [
        E("Un niño le escribe a su profesora: «Hola, profe, wena, mañana no voy xq estoy enfermo». ¿Qué registro usa y por qué no calza: a) informal, porque es una profesora y un aviso importante b) formal, porque saluda?", "a", "El registro informal no es el adecuado para avisar a la profesora."),
        E("Elena habla con su abuelo con «tú» y con la directora con «usted». ¿Por qué cambia: a) porque ajusta el registro al vínculo b) porque se equivoca?", "a", "Elige según con quién habla."),
    ],
    [
        E("Mensaje al director para pedir una sala. Elige el más adecuado: a) «Director, necesito la sala el jueves.» b) «Estimado director: junto con saludarlo, le solicito la sala el jueves, si fuera posible. Muchas gracias.»", "b", "Tiene saludo, trato formal, un pedido cortés y agradecimiento."),
        E("Hablando con un amigo de tu edad, usas «Estimado amigo: junto con saludarlo, le solicito…». ¿Qué problema hay: a) el registro es demasiado formal para el vínculo b) el registro es muy informal?", "a", "El vínculo de confianza no pide ese nivel de formalidad."),
    ],
    [E("Tu curso recibe la visita de un bombero. Un compañero dice: «Oye, tío, cuéntanos algo». Tú quieres decirle mejor. ¿Qué eliges: a) «Señor, ¿podría contarnos cómo se prepara para su trabajo?» b) «Cuenta algo, po».", "a", "Es una visita de un adulto desconocido y requiere registro formal.")],
    [
        E("El registro formal usa «usted». Responde sí o no.", "Sí", "Es una forma de trato respetuoso."),
        E("¿Se debe usar el mismo registro con un amigo y con la directora? Responde sí o no.", "No", "El registro depende del vínculo y de la situación."),
        E("Menciona un factor que influye en el registro: el vínculo o el color del papel.", "El vínculo", "La relación entre las personas guía el registro."),
    ],
    ("Observa este mensaje: «Oye Marta, ¿me prestai tu bicicleta pa mañana?». Reescríbelo para dos destinatarios: A) una amiga de tu curso, B) un vecino mayor que llamas «don Julio». Cada versión debe mantener el mismo pedido. Subraya qué palabras cambiaste y por qué.",
     "A) «Marta, ¿me prestas tu bicicleta para mañana?». B) «Don Julio, ¿podría prestarme su bicicleta para mañana, por favor?». Cambié «oye» por el nombre o título, «prestai» por «prestas» o «podría prestarme», y agregué «por favor».",
     ["mantiene el mismo pedido", "ajusta el trato (tú/usted)", "agrega una fórmula en la versión formal"], ["dos versiones escritas", "palabras cambiadas subrayadas"], ["usar el mismo registro en ambas", "cambiar el pedido"],
     "Si las dos versiones suenan igual, revisa tratamiento, saludo y fórmula de cortesía."),
    "Escribe dos oraciones informales y pásalas a registro formal.",
    "Escribe un mensaje breve para tu profesor o profesora en el que expliques que no puedes asistir un día, con saludo y despedida formales.",
)

# ================================================================ OA 27 · clase 5
reg(
    OA27, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para ensayar una conversación.",
    "Aprenderé a expresar opiniones, sentimientos e ideas con respeto, incluso cuando pienso distinto. Sirve para conversar sin ofender y para que me escuchen mejor.",
    ["Sé usar fórmulas de cortesía.", "Sé elegir el registro según la situación."],
    [
        "Expresar una opinión es decir lo que pensamos sobre algo. Para hacerlo con respeto usamos frases como «yo pienso que…» o «a mí me parece que…», y damos una razón con «porque». Así dejamos claro que es nuestro punto de vista, no una verdad que se impone a los demás. Por ejemplo: «Yo pienso que el recreo debería ser más largo, porque así podemos jugar más».",
        "También podemos expresar sentimientos. Una forma clara es el mensaje en primera persona: «Me sentí triste cuando no me invitaron, porque quería jugar». Este mensaje cuenta lo que sentimos sin acusar a nadie con frases como «tú siempre…» o «eres malo». Acusar suele provocar peleas; contar lo que sentimos ayuda a resolver.",
        "Cuando no estamos de acuerdo, mostramos que escuchamos antes de responder: «Entiendo tu idea, pero yo pienso distinto, porque…». Se critican las ideas y no a las personas. Y si alguien nos dice cómo se sintió, le respondemos con interés: «Gracias por contármelo».",
    ],
    [("opinión", "lo que alguien piensa sobre algo"), ("sentimiento", "emoción que se siente, como alegría o tristeza"), ("mensaje en primera persona", "frase que cuenta lo que yo siento con «me sentí…»"), ("desacuerdo", "cuando pensamos distinto"), ("acusar", "culpar a alguien con frases como «tú siempre…»")],
    [
        ("Opinar con respeto", "Lucas quiere decir que no le gusta el juego que eligió el grupo. ¿Cuál frase lo hace con respeto: a) «Ese juego es malo.» b) «Yo pienso que otro juego sería mejor, porque ayer ya jugamos este.»?", ["Busco la frase que dice que es un punto de vista.", "La b usa «yo pienso» y da una razón.", "La a acusa y no explica."], "La b."),
        ("Decir un sentimiento", "A Emilia la dejaron fuera de un juego. ¿Cómo lo cuenta con un mensaje en primera persona?", ["Empiezo con «me sentí».", "Digo cuándo y por qué.", "No acuso a nadie."], "«Me sentí triste cuando no me dejaron jugar, porque quería participar.»"),
    ],
    [("Decir «tú siempre haces todo mal».", "Se acusa a la persona en lugar de contar lo que pasó.", "Di qué ocurrió y cómo te sentiste: «Me molestó que… porque…»."), ("Estar en desacuerdo gritando o riéndose de la idea del otro.", "Se piensa que así se gana la discusión.", "Reconoce la idea y explica tu razón con calma.")],
    [
        E("¿Qué frase inicia una opinión: a) «Yo pienso que…» b) «Tú nunca…»", "a", "«Yo pienso que» muestra tu punto de vista."),
        E("¿Qué palabra introduce la razón en «Me gusta la lectura porque aprendo cosas»?", "Porque", "Después de «porque» viene la razón."),
        E("«Me sentí contento cuando me felicitaron» expresa: a) un sentimiento b) una orden.", "a", "Cuenta una emoción: estar contento."),
    ],
    [
        E("¿Cuál frase es un mensaje en primera persona: a) «Me sentí nervioso cuando me tocó exponer.» b) «Eres un nervioso.»", "a", "Cuenta lo que sentí sin acusar."),
        E("Fabián no está de acuerdo con Sara. ¿Qué respuesta muestra respeto: a) «Entiendo tu idea, pero yo pienso distinto, porque…» b) «Qué idea tonta.»", "a", "Reconoce la idea y explica su postura."),
        E("Sofía le cuenta a Pablo que se sintió triste. ¿Qué respuesta muestra interés: a) «Gracias por contármelo.» b) «No importa.»", "a", "Agradece y valora lo que dijo."),
    ],
    [
        E("Convierte en opinión respetuosa: «Esa regla es injusta». ¿Qué versión es mejor: a) «Yo pienso que esa regla podría cambiar, porque no todos pueden participar.» b) «Qué regla más injusta, a nadie le importa.»", "a", "Da su punto de vista con una razón y sin acusar."),
        E("Ordena una respuesta en un desacuerdo. a) pero yo pienso distinto b) Entiendo tu idea c) porque necesitamos más tiempo. Escribe las letras.", "b, a, c", "Primero muestra que escuchó, luego dice su postura y la razón."),
        E("En «Me molestó que me interrumpieran, porque estaba explicando mi idea», ¿cuál es la razón del sentimiento?", "Estaba explicando su idea", "Sigue a «porque»."),
    ],
    [
        E("Dos niños discuten. Uno dice: «Tú siempre arruinas todo». El otro dice: «Me pongo triste cuando se ríen de mi trabajo». ¿Quién usa un mensaje que ayuda a resolver y por qué?", "El segundo, porque cuenta lo que siente sin acusar", "El primero acusa y el segundo informa."),
        E("«Tengo derecho a decir lo que pienso, pero también debo escuchar al otro». ¿Es una buena regla para conversar? Responde sí o no.", "Sí", "Opinar y escuchar van juntos."),
    ],
    [
        E("Un amigo dijo en clase que tu dibujo estaba feo. Tú escribes: «Me sentí mal cuando dijiste que mi dibujo estaba feo, porque me esforcé mucho». ¿Qué parte cuenta el sentimiento y qué parte da la razón?", "«Me sentí mal» cuenta el sentimiento; «porque me esforcé mucho» da la razón", "Una parte dice la emoción y la otra explica por qué."),
        E("Un grupo debe elegir entre ir al parque o al museo. Julieta dice: «Yo pienso que es mejor el parque, porque hoy hay sol». Matías dice: «Entiendo tu idea, pero yo pienso que el museo sería mejor, porque ahí aprendemos de dinosaurios». ¿Quién está de acuerdo con ir al parque?", "Julieta", "Ella propone el parque; Matías propone el museo."),
    ],
    [E("En tu curso votarán si el juego de los recreos será fútbol o saltar la cuerda. Dos compañeros opinan: «Mejor fútbol porque somos muchos» y «Mejor saltar la cuerda porque pueden jugar todos». ¿Qué fórmula ayuda a Camilo a decir que prefiere saltar la cuerda sin ofender a quien propone fútbol: a) «Entiendo tu idea, pero yo prefiero saltar la cuerda, porque pueden jugar todos.» b) «Fútbol es aburrido.»", "a", "Reconoce la idea del otro y explica su razón.")],
    [
        E("¿Qué se critica en un desacuerdo respetuoso: la idea o la persona?", "La idea", "Se discute el tema y no se ataca al otro."),
        E("¿Un mensaje en primera persona dice ‘me sentí…’ o ‘tú eres…’? Responde con una de las dos opciones.", "Me sentí", "Cuenta lo que yo siento."),
        E("¿Es respetuoso gritar para ganar una discusión? Responde sí o no.", "No", "Gritar no muestra respeto."),
    ],
    ("Lee esta situación: tu curso debe elegir qué lectura harán en la biblioteca, un cuento de aventuras o un libro de animales. Escribe tres frases: 1) tu opinión con «yo pienso que… porque…», 2) un sentimiento con «me sentí / me siento… porque…» sobre cómo te sientes al elegir, 3) una respuesta respetuosa a un compañero que prefiere la otra opción, comenzando con «Entiendo tu idea, pero…». Ensáyalas en voz alta.",
     "1) «Yo pienso que es mejor el cuento de aventuras, porque me emociona la acción». 2) «Me siento un poco nervioso, porque quiero que escojan algo que nos guste a todos». 3) «Entiendo tu idea, pero yo pienso que el cuento sería más entretenido para el grupo, porque tiene personajes».",
     ["la opinión lleva una razón", "el sentimiento no acusa", "la respuesta reconoce la idea contraria"], ["tres frases escritas y ensayadas"], ["opinión sin razón", "acusar a alguien al contar un sentimiento"],
     "Si tu frase suena a ataque, cámbiala por «yo pienso» o «me sentí» y agrega tu razón."),
    "Escribe un mensaje en primera persona sobre algo que te alegró esta semana.",
    "Con una persona de tu casa, conversen sobre un tema donde piensan distinto y practiquen la frase «Entiendo tu idea, pero…».",
)

# ================================================================ OA 27 · clase 6
reg(
    OA27, 6,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para comentar tu versión corregida.",
    "Aprenderé a revisar una conversación con una lista de criterios, a dar y recibir retroalimentación y a reparar un error con una disculpa completa. Sirve para mejorar cómo me comunico.",
    ["Sé usar fórmulas de cortesía.", "Sé elegir el registro según la situación.", "Sé expresar opiniones y sentimientos con respeto."],
    [
        "Revisar una conversación es mirarla de nuevo con criterios claros. Podemos usar esta lista: ¿hubo saludo?, ¿se usó la fórmula de cortesía que corresponde?, ¿el registro calza con el vínculo?, ¿el tono fue respetuoso? y ¿hubo un cierre amable? Cada criterio se comprueba con una frase del diálogo.",
        "La retroalimentación es un comentario para ayudar a mejorar. Para que sirva debe ser específica, amable y proponer un cambio. Por ejemplo: «Tu saludo fue cálido; podrías agregar ‘por favor’ al pedir el cuaderno». Decir solo «está mal» no ayuda, porque no dice qué cambiar.",
        "Una disculpa completa repara un error. Tiene tres partes: reconocer lo que pasó («rompí tu lápiz»), pedir perdón («perdón») y ofrecer reparar o cambiar («te presto el mío»). Una disculpa que echa la culpa al otro («perdón, pero tú me empujaste») no repara. Al recibir retroalimentación, escuchamos, agradecemos y probamos una segunda versión.",
    ],
    [("revisar", "mirar de nuevo con criterios claros"), ("retroalimentación", "comentario que ayuda a mejorar"), ("disculpa completa", "reconoce lo ocurrido, pide perdón y ofrece reparar"), ("reparar", "arreglar o compensar el daño causado"), ("criterio", "aspecto que se mira para evaluar algo")],
    [
        ("Revisar con la lista", "Diálogo: Pablo: «Dame el pegamento». Rita: «Toma». ¿Qué criterio de la lista no cumple Pablo?", ["Reviso saludo, fórmula, registro, tono y cierre.", "Pablo no saluda ni usa «por favor».", "Tampoco agradece."], "No usa saludo ni fórmula de cortesía."),
        ("Armar una disculpa completa", "Rompiste sin querer el lápiz de Gael. ¿Qué disculpa tiene las tres partes: reconocer, pedir perdón y reparar?", ["Primero digo lo que pasó.", "Luego pido perdón.", "Al final ofrezco algo para reparar."], "«Rompí tu lápiz sin querer. Perdón. Te presto el mío mientras compro otro.»"),
    ],
    [("Decir solo «perdón» sin reconocer lo ocurrido ni reparar.", "Se piensa que la palabra arregla todo.", "Reconoce qué pasó y ofrece una reparación."), ("Dar retroalimentación diciendo «está mal».", "No se piensa en cómo ayudar al otro.", "Señala qué estuvo bien y qué cambiaría, con un ejemplo.")],
    [
        E("¿Cuál criterio de la lista pregunta si dijiste ‘hola’ o ‘buenos días’?", "El saludo", "Es el primer criterio de la lista."),
        E("En una disculpa completa, ¿qué se hace además de reconocer lo ocurrido y pedir perdón: reparar o cambiar de tema?", "Reparar", "Ofrecer reparar es parte de la disculpa."),
        E("¿Qué comentario ayuda más: a) «Está mal.» b) «Tu pedido fue claro; agrega ‘por favor’.»", "b", "Dice qué estuvo bien y qué cambiar."),
    ],
    [
        E("Diálogo: Ana: «Buenos días, profesor. ¿Podría explicarme de nuevo el ejercicio, por favor?». Profesor: «Claro». Ana: «Muchas gracias». ¿Cumple Ana el criterio del cierre amable: sí o no?", "Sí", "Termina con «Muchas gracias»."),
        E("¿Cuál disculpa echa la culpa al otro: a) «Perdón, pero tú me empujaste.» b) «Perdón, choqué contigo sin querer.»", "a", "Culpa a la otra persona y no reconoce su parte."),
        E("Al recibir una retroalimentación amable, ¿qué conviene hacer primero: a) escuchar y agradecer b) discutir de inmediato?", "a", "Escuchar permite aprovechar el comentario."),
    ],
    [
        E("Revisa: Luis: «Hola. Oye, ¿me prestas tu lápiz?». Vera: «Sí». Luis: «Ya». ¿Qué fórmula de cortesía debería decir ahí?", "Gracias", "Es la fórmula para agradecer."),
        E("Ordena una disculpa completa. a) Te traigo otro. b) Se me cayó tu botella. c) Perdón. Escribe las letras.", "b, c, a", "Reconoce, pide perdón y repara."),
        E("Escribe la mejor segunda versión de «Pásame ese libro»: a) «Disculpa, ¿me pasas ese libro, por favor?» b) «Pásame ese libro, ya.»", "a", "Agrega fórmula, pregunta y trato amable."),
    ],
    [
        E("Dos compañeros comentan tu exposición. Uno dice: «Habló fuerte y se entendió, pero faltó saludar al curso». El otro dice: «Nada me gustó». ¿Cuál comentario es retroalimentación útil y por qué?", "El primero, porque dice qué estuvo bien y qué mejorar", "El segundo no entrega información para mejorar."),
        E("Camila dice: «Perdón» y se va sin reparar la torre que botó. ¿Qué parte de la disculpa completa le faltó: a) reparar b) saludar?", "a", "Debía ofrecer arreglar el daño."),
    ],
    [
        E("Mira el diálogo: Raúl: «Buenas tardes, señora Inés. Disculpe, ¿puede prestarme su tijera? Se me olvidó la mía». Señora Inés: «Tome». Raúl: «Gracias, se la devuelvo enseguida». ¿Cuántos criterios de la lista cumple con seguridad: saludo, fórmula de cortesía, registro formal y cierre amable?", "Cuatro", "Saluda, usa «disculpe», habla de «usted» y agradece."),
        E("Matías revisa su diálogo y escribe: «Cumplí el saludo, pero me faltó el cierre». Si agrega «Muchas gracias por su ayuda», ¿qué criterio mejora: el cierre o el saludo?", "El cierre", "La frase añadida es una despedida amable."),
    ],
    [E("Rompiste sin querer el dibujo de un compañero. Revisa estas tres disculpas: a) «Perdón.» b) «Perdón, pero estaba en mi camino.» c) «Rompí tu dibujo sin querer. Perdón. Te ayudo a pegarlo.» ¿Cuál es completa?", "c", "Reconoce, pide perdón y repara.")],
    [
        E("¿La retroalimentación debe decir qué cambiar? Responde sí o no.", "Sí", "Así sirve para mejorar."),
        E("¿Cuáles son las tres partes de una disculpa completa: reconocer, pedir perdón y reparar, o gritar, huir y olvidar?", "Reconocer, pedir perdón y reparar", "Son los pasos que reparan el error."),
        E("Después de recibir retroalimentación, ¿qué se hace: probar una segunda versión o ignorarla?", "Probar una segunda versión", "Mejoramos aplicando el comentario."),
    ],
    ("Lee este diálogo: Hugo: «Dame la hoja». Marta: «Aquí». Hugo: «Ya». Luego Hugo rompe sin querer la hoja de Marta y dice: «Perdón, pero estaba muy cerca». Haz tres cosas: 1) usa la lista (saludo, fórmula, registro, tono, cierre) y escribe dos criterios que Hugo no cumplió, 2) escribe una retroalimentación amable para Hugo, 3) escribe una disculpa completa que Hugo podría decir.",
     "1) No saludó y no usó fórmula de cortesía para pedir ni para agradecer. 2) «Hugo, pediste la hoja rápido; la próxima vez agrega ‘por favor’ y ‘gracias’, así Marta se siente respetada». 3) «Rompí tu hoja sin querer. Perdón. Te doy una de las mías».",
     ["identifica dos criterios con evidencia", "la retroalimentación es amable y propone un cambio", "la disculpa tiene tres partes"], ["lista de criterios completada", "retroalimentación escrita", "disculpa escrita"], ["decir solo «está mal»", "disculpa que culpa a otro"],
     "Si algo no sirve, pregúntate: ¿mi comentario dice qué cambiar? ¿mi disculpa repara el daño?"),
    "Revisa una conversación breve tuya con la lista de cinco criterios y anota qué mejorarías.",
    "Pide a una persona de tu casa que te dé retroalimentación sobre cómo pides algo y escribe qué cambiarías.",
)
