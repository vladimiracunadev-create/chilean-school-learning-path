"""Cuaderno del estudiante, 1.º básico Lenguaje y Comunicación: OA 10 (textos no literarios) y OA 11 (libros e ilustraciones).

Todos los textos son originales y breves; cada ejercicio trae el texto que necesita.
"""
from __future__ import annotations

from student_lessons import ex, register

OA10, OA11 = "LE01 OA 10", "LE01 OA 11"
E = ex


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=ctx, selfcheck=sc, open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ======================================================================== OA 10
CARTA = "«Querida abuela Rosa: Gracias por el gorro de lana. Me queda muy calentito. Te quiero mucho. Tu nieta, Luisa.»"
NOTA = "«Mamá: fui a la plaza con Tomás. Vuelvo a las cinco. Pedro.»"

lesson(
    OA10, 1,
    "Este cuaderno, lápiz y una hoja. Los textos de la carta y de la nota están escritos en cada ejercicio.",
    "Aprenderé a ver quién escribe, a quién escribe y qué quiere decir una carta o una nota. Sirve para entender los mensajes que recibo en casa y en el colegio.",
    ["Sé leer oraciones cortas.", "Sé que las personas se escriben mensajes."],
    [
        "Una carta y una nota son textos para comunicar algo a alguien. Siempre hay alguien que escribe, que se llama emisor, y alguien que lee, que se llama destinatario. El mensaje es lo que el emisor quiere decir.",
        "La carta empieza con un saludo, como «Querida abuela Rosa:», sigue con el mensaje y termina con una despedida y la firma, que es el nombre de quien escribe. La nota es más corta: avisa o pide algo rápido y a veces sólo lleva el nombre de quien la deja.",
        "Para entender un mensaje hazte tres preguntas: ¿quién lo escribe?, ¿para quién es?, ¿qué dice o qué pide? La firma te dice quién escribe y el saludo te dice quién lo recibe.",
    ],
    [("emisor", "la persona que escribe el mensaje"), ("destinatario", "la persona que recibe el mensaje"), ("saludo", "las primeras palabras, como «Querida abuela:»"), ("firma", "el nombre de quien escribe, al final"), ("mensaje", "lo que se quiere decir")],
    [
        ("Leer una carta", f"Lee: {CARTA} ¿Quién escribe y para quién?", ["Busco la firma al final: dice Luisa.", "Busco el saludo al comienzo: dice abuela Rosa.", "Luisa escribe y la abuela Rosa recibe."], "Escribe Luisa y el destinatario es la abuela Rosa"),
        ("Leer una nota", f"Lee: {NOTA} ¿Qué avisa Pedro?", ["Busco qué hizo: fue a la plaza con Tomás.", "Busco cuándo vuelve: a las cinco."], "Avisa que fue a la plaza con Tomás y que vuelve a las cinco"),
    ],
    [
        ("Pensar que quien lee la carta es quien la escribe.", "Se confunde el saludo con la firma.", "El saludo nombra al destinatario; la firma nombra al emisor."),
        ("Leer sólo el saludo y no el mensaje.", "Se cree que lo importante es el comienzo.", "Lee hasta el final y busca qué dice o qué pide."),
    ],
    [
        E(f"Lee: {CARTA} ¿Quién escribe la carta?", "Luisa", "La firma al final dice Luisa."),
        E(f"Lee: {CARTA} ¿Para quién es la carta?", "Para la abuela Rosa", "El saludo nombra a la abuela Rosa."),
        E(f"Lee: {NOTA} ¿Quién firma la nota?", "Pedro", "Su nombre aparece al final."),
    ],
    [
        E(f"Lee: {CARTA} ¿Qué agradece Luisa?", "El gorro de lana", "Dice «Gracias por el gorro de lana»."),
        E(f"Lee: {NOTA} ¿A qué hora vuelve Pedro?", "A las cinco", "El texto dice «Vuelvo a las cinco»."),
        E("¿Qué es el destinatario de una carta?", "La persona que recibe el mensaje", "Es quien lee lo que otro escribió."),
    ],
    [
        E("Lee: «Papá: se acabó la leche. ¿Puedes comprar una bolsa? Gracias. Ema.» ¿Quién escribe?", "Ema", "La firma al final es Ema."),
        E("Lee: «Papá: se acabó la leche. ¿Puedes comprar una bolsa? Gracias. Ema.» ¿Qué pide Ema?", "Que compre una bolsa de leche", "Lo pide con la pregunta del medio."),
        E("Lee: «Para Sofía: te dejé tu bufanda en la silla. Camila.» ¿Quién es el destinatario?", "Sofía", "El saludo «Para Sofía» nombra a quien recibe."),
    ],
    [
        E("Pedro necesita avisar algo muy corto y rápido. ¿Qué le sirve más? A) una nota B) una carta de tres hojas", "A) una nota", "La nota es breve y sirve para avisos rápidos."),
        E(f"Lee: {CARTA} ¿Qué palabra muestra cariño al comienzo?", "Querida", "Es la palabra del saludo que expresa afecto."),
    ],
    [
        E("Ordena las partes de una carta: 1) «Tu nieta, Luisa» 2) «Gracias por el gorro.» 3) «Querida abuela Rosa:». Escribe los números en el orden correcto.", "3, 2, 1", "Primero va el saludo, luego el mensaje y al final la firma."),
        E("Lee: «Tomás: hoy no hay clases de música. Avísale a Iván. Profesora Ana.» ¿Quién es el emisor y quién el destinatario?", "El emisor es la profesora Ana y el destinatario es Tomás", "Firma quien escribe y el saludo nombra a quien recibe."),
    ],
    [E("Mamá deja esta nota en la mesa: «Tomás: la comida está en el horno. Cuidado, está caliente. Mamá.» ¿Qué le pide cuidar a Tomás?", "Que tenga cuidado porque la comida está caliente", "La nota advierte del peligro de quemarse.")],
    [
        E("¿Qué parte de una carta nombra a quien escribe?", "La firma", "La firma lleva el nombre del emisor."),
        E("En «Querida tía Ana:», ¿quién es el destinatario?", "La tía Ana", "El saludo nombra a quien recibe el mensaje."),
        E("¿Qué es más corta, una nota o una carta?", "La nota", "La nota sólo avisa o pide algo rápido."),
    ],
    task(
        "Escribe una nota de dos oraciones para alguien de tu casa. Elige una de estas ideas: A) avisas que juegas en la casa de un amigo hasta las cuatro; B) pides que compren pan. Incluye saludo, mensaje y tu firma.",
        "Papá: pedí permiso para jugar en la casa de un amigo. Vuelvo a las cuatro. Ema.",
        ["tiene saludo con el nombre del destinatario", "dice un mensaje claro de una o dos oraciones", "termina con la firma del que escribe"],
        ["nota escrita en el cuaderno o en una hoja", "lectura en voz alta a un adulto"],
        ["no poner firma", "escribir el mensaje sin saludo", "no decir qué se avisa o se pide"],
        "Marca con un color el saludo, el mensaje y la firma; si falta una parte, agrégala.",
    ),
    "Lee de nuevo la nota de Pedro y di en voz alta quién escribe, para quién es y qué avisa.",
    "Escribe una carta de tres oraciones a un familiar con saludo, mensaje, despedida y firma.",
)

PASOS_DIENTES = "«1) Pon un poco de pasta en el cepillo. 2) Cepilla arriba y abajo. 3) Escupe la pasta. 4) Enjuágate con agua.»"

lesson(
    OA10, 2,
    "Lápiz, cuaderno, un pan, una palta y un tenedor si quieres hacer la receta de verdad (si no, basta con leer los pasos).",
    "Aprenderé a leer instrucciones y a seguir sus pasos en orden. Sirve para hacer cosas solo, como una receta o una manualidad.",
    ["Sé leer oraciones cortas.", "Sé contar hasta 10."],
    [
        "Las instrucciones son textos que enseñan a hacer algo paso a paso. Dicen primero qué se necesita y luego los pasos, que suelen ir numerados: 1, 2, 3. Cada paso dice una acción y empieza con un verbo como «pon», «corta» o «mezcla».",
        "El orden es muy importante. Si cambias el orden, el resultado sale mal: no puedes ponerte los zapatos antes que los calcetines. Palabras como «primero», «después», «luego» y «al final» te ayudan a saber cuál va antes.",
        "Antes de empezar, lee todos los pasos. Después hazlos uno por uno y marca el que ya terminaste. Si algo no se entiende, vuelve a leer ese paso.",
    ],
    [("instrucciones", "texto que dice cómo hacer algo"), ("paso", "cada acción de las instrucciones"), ("orden", "qué va primero, qué va después y qué va al final"), ("materiales", "las cosas que necesito"), ("verbo", "palabra que dice una acción, como «pon»")],
    [
        ("Contar los pasos", f"Lee: {PASOS_DIENTES} ¿Cuántos pasos tiene?", ["Cuento los números: 1, 2, 3, 4.", "Hay un número por cada paso."], "Tiene 4 pasos"),
        ("Qué va primero", f"Lee: {PASOS_DIENTES} ¿Qué se hace después de cepillar?", ["Cepillar es el paso 2.", "El paso que sigue es el 3: escupir la pasta."], "Se escupe la pasta"),
    ],
    [
        ("Hacer los pasos en cualquier orden.", "Se salta la numeración.", "Sigue los números de menor a mayor."),
        ("Empezar a hacer sin leer todo.", "Hay apuro por terminar.", "Lee todos los pasos antes de empezar."),
    ],
    [
        E(f"Lee: {PASOS_DIENTES} ¿Qué se hace primero?", "Poner un poco de pasta en el cepillo", "El paso 1 es el primero."),
        E(f"Lee: {PASOS_DIENTES} ¿Qué se hace al final?", "Enjuagarse con agua", "El paso 4 es el último."),
        E("Lee: «1) Saca dos tajadas de pan. 2) Aplasta la palta con un tenedor.» ¿Qué se necesita aplastar?", "La palta", "El paso 2 lo dice."),
    ],
    [
        E("Lee: «1) Saca dos tajadas de pan. 2) Aplasta la palta con un tenedor. 3) Unta la palta en una tajada. 4) Tapa con la otra tajada.» ¿Cuántos pasos hay?", "4", "Hay cuatro pasos numerados."),
        E("Lee: «1) Saca dos tajadas de pan. 2) Aplasta la palta con un tenedor. 3) Unta la palta en una tajada. 4) Tapa con la otra tajada.» ¿Con qué se aplasta la palta?", "Con un tenedor", "El paso 2 nombra el utensilio."),
        E("¿Para qué sirven los números en las instrucciones?", "Para mostrar el orden de los pasos", "Indican qué va primero, después y al final."),
    ],
    [
        E("Ordena para hacer un barquito de papel: a) Dobla las puntas hacia el centro. b) Toma una hoja rectangular. c) Dobla la hoja por la mitad. Escribe las letras en orden.", "b, c, a", "Primero se toma la hoja, luego se dobla por la mitad y después las puntas."),
        E("Lee: «Mójate las manos, frota con jabón, enjuaga y seca.» ¿Cuál es el tercer paso?", "Enjuagar", "Se cuenta: mojar, frotar, enjuagar."),
        E("¿Qué palabra de estas indica una acción que haces? A) pan B) corta C) mesa", "B) corta", "«Corta» es un verbo: dice lo que hay que hacer."),
    ],
    [
        E("María hizo el paso 3 antes del paso 2 de la receta de pan con palta: untó la palta sin aplastarla. ¿Por qué salió mal?", "Porque no respetó el orden de los pasos", "Primero había que aplastar la palta y después untarla."),
        E("Un niño dice: «No leo los pasos, empiezo y listo». ¿Es buena idea? Responde sí o no.", "No", "Hay que leer todo antes para saber el orden y los materiales."),
    ],
    [
        E("Ordena estos pasos de «ponerse los zapatos»: a) Amarra los cordones. b) Mete el pie en el zapato. c) Siéntate en una silla. Escribe las letras en orden.", "c, b, a", "Primero te sientas, luego metes el pie y al final amarras."),
        E("Este paso está mal escrito: «Zapato el pie mete». ¿Cómo queda bien?", "Mete el pie en el zapato", "Las palabras deben ir en orden para que se entienda."),
    ],
    [E("Mateo quiere preparar pan con palta con estos pasos desordenados: «Tapa con la otra tajada. Saca dos tajadas de pan. Unta la palta. Aplasta la palta con un tenedor.» ¿Qué paso debe hacer primero?", "Sacar dos tajadas de pan", "Primero se necesitan las tajadas para poder untar.")],
    [
        E("¿Cómo se llama el texto que dice cómo hacer algo paso a paso?", "Instrucciones", "Enseña a hacer algo en orden."),
        E("Si las instrucciones dicen «primero» y «después», ¿qué muestran esas palabras?", "El orden de los pasos", "Dicen qué va antes y qué va después."),
        E("Lee: «Pon agua en un vaso y agrega una cucharada de azúcar.» ¿Qué hay que poner en el vaso?", "Agua y una cucharada de azúcar", "Se piden dos cosas dentro del vaso."),
    ],
    task(
        "Escribe en tu cuaderno los pasos de «lavarse las manos», numerados del 1 al 4, usando estas frases en el orden correcto: «seca con una toalla», «mójate las manos», «frota con jabón», «enjuaga con agua».",
        "1) Mójate las manos. 2) Frota con jabón. 3) Enjuaga con agua. 4) Seca con una toalla.",
        ["los cuatro pasos están numerados", "el orden es lógico", "cada paso empieza con una acción"],
        ["lista numerada en el cuaderno", "demostración en voz alta con gestos"],
        ["poner el secado antes del jabón", "olvidar un paso", "no numerar"],
        "Lee tu lista en voz alta mientras haces los gestos; si algún paso no funciona, cámbialo de lugar.",
    ),
    "Lee de nuevo los pasos de lavarse los dientes y señala con el dedo cada número.",
    "Escribe tres pasos numerados para hacer pan con palta, con tus propias palabras.",
)

PINGUINO = "«El pingüino de Humboldt vive en las costas de Chile y de Perú. Nada muy bien y come peces pequeños, como las sardinas. Hace su nido en cuevas o en hoyos de la tierra. Tiene una franja negra en el pecho.»"

lesson(
    OA10, 3,
    "Cuaderno y lápiz. El artículo sobre el pingüino de Humboldt y el de las abejas están escritos en los ejercicios.",
    "Aprenderé a leer un artículo informativo y a encontrar los datos que dice. Sirve para aprender cosas nuevas del mundo.",
    ["Sé leer textos de cuatro oraciones.", "Sé qué es un animal."],
    [
        "Un artículo informativo es un texto que cuenta datos verdaderos sobre un tema. Se escribe para que el lector aprenda, no para contar una aventura. Tiene un título que dice de qué trata y oraciones con información.",
        "Para encontrar información explícita, busca las palabras que están escritas en el texto. Si te preguntan dónde vive el pingüino de Humboldt, vuelves a leer y subrayas la oración que lo dice. La respuesta está dicha, sólo hay que encontrarla.",
        "Un buen lector se hace preguntas: ¿qué aprendí?, ¿qué dato es nuevo para mí? Después vuelve al texto para comprobar su respuesta. Así no confunde lo que leyó con lo que ya sabía.",
    ],
    [("artículo", "texto que informa sobre un tema"), ("dato", "una información verdadera"), ("explícito", "que está dicho en el texto"), ("tema", "de qué trata el texto"), ("costa", "borde de tierra junto al mar")],
    [
        ("Buscar un dato", f"Lee: {PINGUINO} ¿Dónde hace su nido?", ["Busco la palabra nido.", "La oración dice: en cuevas o en hoyos de la tierra."], "En cuevas o en hoyos de la tierra"),
        ("Tema del texto", f"Lee: {PINGUINO} ¿De qué trata el texto?", ["Todas las oraciones hablan del pingüino de Humboldt.", "Cuentan dónde vive, qué come y cómo es."], "Trata del pingüino de Humboldt"),
    ],
    [
        ("Responder con algo que yo sé pero que el texto no dice.", "Se mezcla lo conocido con lo leído.", "Vuelve al texto y busca la oración que responde."),
        ("Leer sólo el título.", "Se cree que basta para saberlo todo.", "Lee todas las oraciones antes de contestar."),
    ],
    [
        E(f"Lee: {PINGUINO} ¿Dónde vive el pingüino de Humboldt?", "En las costas de Chile y de Perú", "La primera oración lo dice."),
        E(f"Lee: {PINGUINO} ¿Qué come?", "Peces pequeños, como las sardinas", "La segunda oración nombra su comida."),
        E(f"Lee: {PINGUINO} ¿Qué tiene en el pecho?", "Una franja negra", "La última oración lo describe."),
    ],
    [
        E(f"Lee: {PINGUINO} ¿Cuántas oraciones tiene el texto?", "4", "Se cuentan cuatro puntos finales."),
        E(f"Lee: {PINGUINO} ¿Nada bien o nada mal el pingüino de Humboldt?", "Nada bien", "El texto dice «Nada muy bien»."),
        E("¿Para qué se escribe un artículo informativo?", "Para que el lector aprenda datos", "Entrega información verdadera sobre un tema."),
    ],
    [
        E("Lee: «Las abejas viven en una colmena. Juntan néctar de las flores y hacen miel.» ¿Dónde viven las abejas?", "En una colmena", "La primera oración lo dice."),
        E("Lee: «Las abejas viven en una colmena. Juntan néctar de las flores y hacen miel.» ¿Qué hacen con el néctar?", "Hacen miel", "La segunda oración lo explica."),
        E("Lee: «Las abejas viven en una colmena. Juntan néctar de las flores y hacen miel.» ¿De dónde juntan el néctar?", "De las flores", "El texto lo nombra directamente."),
    ],
    [
        E(f"Lee: {PINGUINO} Marta dice que el pingüino de Humboldt vive en la selva. ¿Tiene razón?", "No; el texto dice que vive en las costas", "La respuesta se comprueba en la primera oración."),
        E("Lee: «Las abejas viven en una colmena. Juntan néctar de las flores y hacen miel.» ¿Qué título sirve mejor? A) Mi paseo B) La vida de las abejas", "B) La vida de las abejas", "El título debe decir de qué trata el texto."),
    ],
    [
        E("Lee: «Sin las abejas, muchas plantas no tendrían frutos.» ¿Qué pasaría sin abejas, según el texto?", "Muchas plantas no tendrían frutos", "La oración dice esa consecuencia."),
        E("Ordena para armar un dato: «nido / pingüino / hace / el / su / en una cueva». Escribe la oración.", "El pingüino hace su nido en una cueva", "Las palabras se ordenan para que tenga sentido."),
    ],
    [E("Una niña quiere saber qué come el pingüino de Humboldt para contárselo a su hermano. Lee el artículo: " + PINGUINO + " ¿Qué le puede decir?", "Que come peces pequeños, como las sardinas", "Es el dato que dice el texto.")],
    [
        E("¿Un artículo informativo cuenta datos verdaderos o inventados?", "Verdaderos", "Su propósito es informar."),
        E("¿Cómo se llama lo que está dicho con palabras en el texto?", "Información explícita", "Está escrita y se puede encontrar."),
        E("Lee: «La colmena es el hogar de las abejas.» ¿Cuál es el hogar de las abejas?", "La colmena", "La oración lo afirma."),
    ],
    task(
        "Lee este artículo: «El zorro culpeo vive en los cerros y en el campo de Chile. Come ratones y frutos. Tiene la cola larga y peluda.» Escribe tres datos que aprendiste, empezando cada uno con «Aprendí que».",
        "Aprendí que el zorro culpeo vive en los cerros y en el campo de Chile. Aprendí que come ratones y frutos. Aprendí que tiene la cola larga y peluda.",
        ["tres datos escritos", "cada dato está en el texto", "empiezan con «Aprendí que»"],
        ["tres oraciones en el cuaderno", "explicación oral a un adulto"],
        ["inventar datos que no están", "copiar el texto completo", "escribir menos de tres datos"],
        "Subraya en el texto la oración de donde sacaste cada dato para comprobar que está dicho.",
    ),
    "Vuelve a leer el texto del pingüino y subraya con lápiz el lugar donde vive.",
    "Escribe una pregunta sobre las abejas que se responda con el texto y respóndela.",
)

lesson(
    OA10, 4,
    "Cuaderno, lápiz y los textos cortos escritos en cada ejercicio.",
    "Aprenderé a descubrir lo que un texto no dice con palabras pero deja entender, usando pistas. Sirve para entender mejor lo que leo.",
    ["Sé leer oraciones.", "Sé buscar información explícita."],
    [
        "A veces un texto no dice todo con palabras, pero deja pistas para descubrirlo. A eso se le llama información implícita. Por ejemplo, si lees «Tomás sale con paraguas y botas», el texto no dice que llueve, pero tú lo puedes descubrir.",
        "Para inferir, junta dos cosas: las pistas del texto y lo que ya sabes. Las pistas son las palabras escritas; lo que sabes es tu experiencia. Con eso armas la respuesta y puedes decir «lo sé porque el texto dice...».",
        "Cuidado: una inferencia debe apoyarse en pistas. Si no hay ninguna pista, es sólo una idea inventada. Siempre explica con una pista del texto.",
    ],
    [("inferir", "descubrir algo que no está dicho usando pistas"), ("pista", "palabra o dato que ayuda a descubrir"), ("implícito", "que no está dicho, pero se puede descubrir"), ("explícito", "que sí está escrito"), ("conclusión", "lo que decides después de pensar en las pistas")],
    [
        ("Descubrir el tiempo", "Lee: «Tomás sale con paraguas y botas. Las calles están mojadas.» ¿Qué tiempo hace?", ["Pistas: paraguas, botas y calles mojadas.", "Sé que eso pasa cuando llueve."], "Está lloviendo"),
        ("Descubrir un lugar", "Lee: «Hay mesas, platos y un olor a pan. Un señor trae la cuenta.» ¿Dónde están?", ["Pistas: mesas, platos, comida y cuenta.", "Eso hay en un restaurante."], "En un restaurante"),
    ],
    [
        ("Decir una idea sin pista del texto.", "Se confunde adivinar con inferir.", "Busca una palabra del texto que apoye tu idea."),
        ("Creer que lo que no está escrito no se puede saber.", "Sólo se mira lo explícito.", "Piensa en las pistas y en lo que sabes."),
    ],
    [
        E("Lee: «Tomás sale con paraguas y botas. Las calles están mojadas.» ¿Qué usa Tomás para protegerse de la lluvia?", "Un paraguas", "El texto lo dice directamente."),
        E("Lee: «Ema se puso la bufanda y el gorro de lana.» ¿Hace frío o calor?", "Frío", "La bufanda y el gorro de lana se usan para abrigarse."),
        E("Lee: «El perro mueve la cola y salta cuando ve a Nico.» ¿Está contento o triste el perro?", "Contento", "Mover la cola y saltar muestran alegría."),
    ],
    [
        E("Lee: «Sonó el timbre. Los niños guardaron sus cuadernos y salieron corriendo al patio.» ¿Qué momento es?", "El recreo", "Salir al patio al sonar el timbre indica recreo."),
        E("Lee: «Luz bostezó, se frotó los ojos y apagó la lámpara.» ¿Qué va a hacer Luz?", "Dormir", "Bostezar y apagar la luz son pistas de sueño."),
        E("¿Cómo se llama lo que está en el texto pero no dicho con todas las letras?", "Información implícita", "Se descubre con pistas."),
    ],
    [
        E("Lee: «Hay una torta con velas. Todos cantan y Ana sopla.» ¿Qué se celebra?", "Un cumpleaños", "La torta, las velas y el canto son pistas de cumpleaños."),
        E("Lee: «Pedro abrió la ventana: había nubes oscuras y se oyó un trueno.» ¿Qué va a pasar probablemente?", "Va a llover", "Las nubes oscuras y el trueno anuncian lluvia."),
        E("Lee: «La profesora tomó la tiza y escribió en la pizarra.» ¿Dónde están?", "En la sala de clases", "La tiza y la pizarra se usan en una sala."),
    ],
    [
        E("Lee: «Ema tiene los ojos rojos y un pañuelo en la mano.» Tomás dice que Ema está llorando. ¿Qué pista usó?", "Los ojos rojos y el pañuelo", "Son las palabras del texto que apoyan la idea."),
        E("Lee: «Hoy Rosa llegó tarde y sin mochila.» Juan dice que Rosa viajó a la luna. ¿Tiene alguna pista del texto? Responde sí o no.", "No", "No hay ninguna pista que apoye esa idea."),
    ],
    [
        E("Lee: «Nico sacó la pala, la regadera y las semillas. Cavó un hoyo en la tierra.» ¿Qué va a hacer Nico?", "Plantar una semilla", "Pala, regadera, semillas y hoyo son pistas de plantar."),
        E("Lee: «Al abrir la puerta, el olor a pan caliente llenó la casa.» ¿Quién estuvo haciendo pan? Elige: A) alguien en la casa B) nadie", "A) alguien en la casa", "El pan caliente indica que alguien lo preparó hace poco."),
    ],
    [E("Lee esta nota: «Mamá: no olvides tu chaleco y tus guantes. Hoy hace mucho viento y está nublado.» ¿Qué le pide la nota a quien la lee? Responde con tus palabras.", "Que se abrigue con chaleco y guantes", "El viento y las nubes sugieren que hace frío.")],
    [
        E("Lee: «La niña corre a la puerta cuando suena el timbre y grita: ¡Llegó papá!» ¿Está alegre o enojada?", "Alegre", "Corre y grita para recibirlo."),
        E("¿Qué se necesita para inferir bien? A) una pista del texto B) nada", "A) una pista del texto", "La inferencia se apoya en pistas."),
        E("Lee: «Las hojas caen de los árboles y los días se acortan.» ¿Qué estación puede ser?", "Otoño", "Caer las hojas es una pista del otoño."),
    ],
    task(
        "Lee esta escena: «Sofía llega a casa con las botas llenas de barro. Deja el paraguas goteando en la entrada y se saca la bufanda.» Escribe dos cosas que descubres aunque el texto no las dice (por ejemplo, el tiempo que hizo) y la pista que usaste para cada una.",
        "Descubro que llovió porque el paraguas gotea. Descubro que caminó por la tierra mojada porque tiene las botas con barro.",
        ["dos cosas descubiertas", "cada una tiene una pista del texto", "no repite lo que ya está dicho"],
        ["dos oraciones en el cuaderno", "respuesta oral con «lo sé porque»"],
        ["decir algo sin pista", "repetir lo que el texto ya dice", "dar una sola idea"],
        "Pregúntate: ¿qué palabra del texto me lo hizo pensar? Anótala junto a tu idea.",
    ),
    "Lee de nuevo la escena de Tomás y su paraguas y di qué pistas usaste.",
    "Escribe dos oraciones con una pista y pide a alguien que descubra qué pasó.",
)

lesson(
    OA10, 5,
    "Cuaderno y lápiz. Los cuatro textos de ejemplo están escritos en los ejercicios.",
    "Aprenderé a distinguir una carta, una nota, unas instrucciones y un artículo según para qué se escriben. Sirve para saber qué esperar al leer cada texto.",
    ["Sé leer cartas y notas.", "Sé leer instrucciones y artículos breves."],
    [
        "Cada tipo de texto tiene un propósito, es decir, una razón para ser escrito. La carta sirve para comunicarse con alguien lejano; la nota, para avisar algo rápido; las instrucciones, para enseñar a hacer algo; el artículo, para informar sobre un tema.",
        "Cada uno se reconoce por sus pistas. La carta tiene saludo y firma. La nota es corta y nombra a quien la recibe. Las instrucciones tienen pasos numerados y verbos. El artículo tiene un título y datos.",
        "Saber el propósito ayuda a leer mejor: si es una instrucción, sigo los pasos; si es un artículo, busco datos; si es una carta, pienso en quién la escribe.",
    ],
    [("propósito", "la razón por la que se escribe un texto"), ("género", "tipo de texto, como carta o artículo"), ("avisar", "decir algo rápido que otro necesita saber"), ("informar", "dar datos sobre un tema"), ("comparar", "ver en qué se parecen y se diferencian")],
    [
        ("Reconocer el género", "Lee: «1) Corta el papel. 2) Dobla la punta. 3) Pega.» ¿Es carta, nota, instrucciones o artículo?", ["Hay números.", "Cada paso dice una acción."], "Son instrucciones"),
        ("Reconocer el propósito", "Lee: «Querido Pablo: ¿cómo estás? Te extraño. Tu primo, Leo.» ¿Para qué se escribió?", ["Tiene saludo y firma.", "Quiere saludar a alguien lejano."], "Para comunicarse con Pablo (es una carta)"),
    ],
    [
        ("Pensar que todos los textos sirven para lo mismo.", "Se lee sin fijarse en el propósito.", "Pregunta siempre: ¿para qué se escribió?"),
        ("Confundir una nota con instrucciones.", "Ambas son cortas.", "Las instrucciones tienen pasos; la nota avisa."),
    ],
    [
        E("¿Qué texto sirve para enseñar a hacer algo? A) instrucciones B) carta", "A) instrucciones", "Dicen los pasos en orden."),
        E("¿Qué texto sirve para avisar algo rápido? A) nota B) artículo", "A) nota", "Es breve y directa."),
        E("¿Qué texto sirve para informar sobre un tema? A) artículo informativo B) nota", "A) artículo informativo", "Entrega datos verdaderos."),
    ],
    [
        E("Lee: «Papá: salí con la abuela. Vuelvo luego. Ema.» ¿Qué tipo de texto es?", "Una nota", "Es corta, avisa y nombra a quien la recibe."),
        E("Lee: «El pulpo tiene ocho brazos y vive en el mar.» ¿Qué tipo de texto es?", "Un artículo informativo", "Entrega un dato sobre un animal."),
        E("Lee: «Querida tía Lola: Gracias por tu regalo. Tu sobrino, Beto.» ¿Qué tipo de texto es?", "Una carta", "Tiene saludo, mensaje y firma."),
    ],
    [
        E("Lee: «1) Toma un vaso. 2) Llénalo con agua. 3) Bebe despacio.» ¿Cuántos pasos tiene y qué texto es?", "Tres pasos; son instrucciones", "Hay tres números y verbos de acción."),
        E("Lee: «Tomás: hoy hay reunión a las cuatro. Profesora Ana.» ¿Cuál es el propósito?", "Avisar algo", "La nota informa a Tomás de una reunión."),
        E("Lee: «Los caracoles llevan su casa en la espalda.» ¿Qué se aprende?", "Que los caracoles llevan su casa en la espalda", "Es un dato dicho en el texto."),
    ],
    [
        E("Una niña quiere aprender a armar un barco de papel. ¿Qué texto le sirve más? A) instrucciones B) carta", "A) instrucciones", "Tienen los pasos para hacerlo."),
        E("Quieres contarle a tu abuela que la extrañas y vive en otra ciudad. ¿Qué texto escribes? A) una carta B) un artículo", "A) una carta", "Se usa para comunicarse con alguien lejano."),
    ],
    [
        E("Un texto dice: «Dobla la hoja. Pega las puntas. Pinta.» Otro dice: «Los gatos duermen mucho.» ¿Cuál es artículo informativo?", "El segundo, «Los gatos duermen mucho»", "Da un dato, no pasos a seguir."),
        E("¿En qué se parecen una carta y una nota? A) Las dos comunican un mensaje a alguien B) Las dos tienen pasos numerados", "A) Las dos comunican un mensaje a alguien", "Tienen emisor y destinatario."),
    ],
    [E("Julián encuentra este papel en la cocina: «Julián: la sopa está en la olla. Caliéntala 5 minutos. Mamá.» ¿Qué texto es y quién lo escribió?", "Una nota escrita por mamá", "Avisa y pide algo; la firma es Mamá.")],
    [
        E("¿Qué tipo de texto lleva saludo y firma? A) carta B) instrucciones", "A) carta", "El saludo y la firma son típicos de la carta."),
        E("¿Qué tipo de texto lleva pasos numerados?", "Instrucciones", "Cada número es un paso."),
        E("¿Qué texto sirve para aprender datos? A) artículo B) nota", "A) artículo", "Su propósito es informar."),
    ],
    task(
        "Elige uno de estos tres textos y di de qué tipo es y para qué sirve, usando la frase «Es ... porque ...»: A) «Mezcla la harina con agua. Amasa. Hornea.» B) «Querido Pablo: ¿cómo estás? Tu primo, Leo.» C) «Los delfines viven en el mar y respiran aire.»",
        "Elijo A. Es un texto de instrucciones porque tiene pasos con acciones: mezcla, amasa y hornea. Sirve para enseñar a hacer pan.",
        ["dice el tipo de texto", "usa una pista como razón", "dice para qué sirve"],
        ["respuesta oral", "oración escrita en el cuaderno"],
        ["decir el tipo sin razón", "confundir el propósito", "no usar «porque»"],
        "Busca una pista en el texto (saludo, pasos, dato) y úsala en tu explicación.",
    ),
    "Mira una nota, una receta o una carta de tu casa y di para qué sirve.",
    "Inventa una frase de cada tipo de texto: carta, nota, instrucción y dato.",
)

ABEJAS = "«Las abejas viven en una colmena. Juntan néctar de las flores y hacen miel. Sin las abejas, muchas plantas no tendrían frutos.»"

lesson(
    OA10, 6,
    "Cuaderno y lápiz. El texto sobre las abejas está escrito en los ejercicios.",
    "Aprenderé a dar mi opinión sobre lo que leí y a apoyarla con una razón del texto. Sirve para decir lo que pienso sin dejar de entender.",
    ["Sé leer un artículo breve.", "Sé buscar información explícita."],
    [
        "Una opinión es lo que tú piensas o sientes sobre algo que leíste. No es un dato, porque otra persona puede pensar distinto. «Las abejas hacen miel» es un dato. «Me parece importante cuidar a las abejas» es una opinión.",
        "Una opinión se dice mejor con una razón. Para eso se usa la palabra «porque». Por ejemplo: «Creo que las abejas son importantes porque ayudan a que haya frutos». La razón debe estar apoyada en lo que dice el texto.",
        "Primero entiende el texto, después opina. Si no comprendiste, puedes dar una opinión que no tiene que ver con lo leído. Cuando opines, usa frases como «me parece que», «creo que» o «me gustó porque».",
    ],
    [("opinión", "lo que pienso sobre algo"), ("dato", "algo que se puede comprobar en el texto"), ("razón", "la explicación de lo que pienso"), ("porque", "palabra que une mi opinión con mi razón"), ("importante", "que vale mucho o ayuda mucho")],
    [
        ("Dato u opinión", f"Lee: {ABEJAS} ¿«Las abejas viven en una colmena» es dato u opinión?", ["Puedo comprobarlo en el texto.", "Otra persona no puede decir lo contrario si leyó el texto."], "Es un dato"),
        ("Opinión con razón", f"Lee: {ABEJAS} Completa: «Creo que hay que cuidar a las abejas porque ...»", ["Busco en el texto por qué son importantes.", "El texto dice que sin ellas muchas plantas no tendrían frutos."], "Creo que hay que cuidar a las abejas porque sin ellas muchas plantas no tendrían frutos"),
    ],
    [
        ("Dar una opinión sin razón.", "Se cree que basta con decir «me gusta».", "Agrega «porque» y una razón."),
        ("Dar como razón algo que no tiene que ver con el texto.", "Se opina sin releer.", "Busca en el texto una razón que apoye tu opinión."),
    ],
    [
        E(f"Lee: {ABEJAS} «Las abejas hacen miel» ¿es dato u opinión?", "Dato", "Está dicho en el texto."),
        E("«Las abejas son lo más lindo del mundo» ¿es dato u opinión?", "Opinión", "Es lo que piensa una persona."),
        E("¿Qué palabra usamos para dar una razón de lo que pensamos?", "Porque", "Une la opinión con su explicación."),
    ],
    [
        E(f"Lee: {ABEJAS} ¿Qué pasaría sin las abejas, según el texto?", "Muchas plantas no tendrían frutos", "La última oración lo dice."),
        E("Lee: «Me gustó el texto porque aprendí cómo se hace la miel». ¿Qué razón da?", "Aprendió cómo se hace la miel", "Viene después de «porque»."),
        E("¿Cuál tiene una razón? A) «Me gustó» B) «Me gustó porque aprendí algo nuevo»", "B) «Me gustó porque aprendí algo nuevo»", "Sólo la segunda explica por qué."),
    ],
    [
        E(f"Lee: {ABEJAS} Completa: «Me parece importante cuidar las abejas porque ...» usando el texto.", "porque ayudan a que muchas plantas tengan frutos", "La razón sale de la última oración."),
        E("Escribe una opinión sobre el texto de las abejas empezando con «Me gustó que...».", "Por ejemplo: Me gustó que las abejas hagan miel", "Debe empezar con la frase y tratar del texto."),
        E("Escribe una pregunta que tengas sobre las abejas después de leer el texto.", "Por ejemplo: ¿Cuántas flores visita una abeja en un día?", "Es una pregunta que surge del tema leído."),
    ],
    [
        E(f"Lee: {ABEJAS} Pedro dice: «Las abejas no sirven para nada». ¿Qué parte del texto muestra que se equivoca?", "Que hacen miel y que sin ellas muchas plantas no tendrían frutos", "Muestra que son útiles."),
        E("Ana dice: «Es malo el texto porque sí». ¿Su opinión tiene razón?", "No", "«Porque sí» no explica nada."),
    ],
    [
        E("Dos niños opinan: Luis: «Me gustó porque las abejas ayudan a las plantas». Mia: «Me gustó». ¿Quién apoyó mejor su opinión?", "Luis", "Dio una razón del texto."),
        E("Tomás dice: «Las abejas son importantes porque hacen miel y ayudan a las plantas». Cuenta cuántas razones da.", "2", "Menciona hacer miel y ayudar a las plantas."),
    ],
    [E("En el curso preguntan: ¿Hay que cuidar a las abejas? Lee el texto: " + ABEJAS + " Elige la mejor respuesta. A) Sí, porque sí B) Sí, porque sin ellas muchas plantas no tendrían frutos", "B) Sí, porque sin ellas muchas plantas no tendrían frutos", "Usa una razón del texto.")],
    [
        E("Al leer un artículo, ¿qué es una opinión mía?", "Lo que yo pienso sobre algo", "Otra persona puede pensar distinto."),
        E("Escribe la palabra que va después de tu opinión para dar la razón.", "Porque", "Anuncia la explicación."),
        E("«Las abejas viven en una colmena» ¿es opinión o dato?", "Dato", "Se comprueba en el texto."),
    ],
    task(
        "Lee este artículo: «El colibrí es un ave muy pequeña. Mueve las alas muy rápido y se alimenta del néctar de las flores.» Escribe una opinión que empiece con «Me gustó...» o «Me parece...» y agrégale una razón con «porque».",
        "Me parece que el colibrí es especial porque mueve las alas muy rápido.",
        ["la opinión empieza con la frase pedida", "usa «porque»", "la razón sale del texto"],
        ["oración escrita", "opinión dicha en voz alta"],
        ["no usar «porque»", "dar una razón que no está en el texto", "copiar una oración del texto como opinión"],
        "Subraya en el texto la razón que usaste para comprobar que está ahí.",
    ),
    "Di en voz alta una opinión sobre las abejas usando la palabra «porque».",
    "Pregunta a alguien de tu casa si está de acuerdo contigo y por qué.",
)

# ======================================================================== OA 11
LIBRO = "Portada: título «El gato que quería volar», autora Marta Ríos, dibujo de un gato mirando pájaros. Contraportada: «Un gato curioso quiere subir al cielo. ¿Lo logrará?»"

lesson(
    OA11, 1,
    "Un libro de tu casa si tienes uno (si no, basta con la descripción escrita en el ejercicio), cuaderno y lápiz.",
    "Aprenderé a mirar la portada y la contraportada de un libro para adivinar de qué trata. Sirve para elegir libros que me gusten.",
    ["Sé leer palabras y títulos cortos.", "Sé qué es un libro."],
    [
        "Un libro entrega pistas antes de leerlo. La portada es la parte de adelante: tiene el título, que es el nombre del libro, el autor, que es quien lo escribió, y un dibujo. La contraportada es la parte de atrás y suele contar un poco de qué trata.",
        "Con esas pistas puedes hacer una predicción, es decir, pensar de qué puede tratar el libro. Si el título dice «El gato que quería volar» y el dibujo muestra un gato mirando pájaros, puedes pensar que el gato quiere ser como los pájaros.",
        "Después de leer puedes comprobar si tu predicción era correcta. No pasa nada si te equivocaste: lo bueno es pensar y mirar las pistas.",
    ],
    [("portada", "la parte de adelante del libro"), ("contraportada", "la parte de atrás del libro"), ("título", "el nombre del libro"), ("autor", "la persona que escribió el libro"), ("predicción", "lo que pienso que pasará o tratará")],
    [
        ("Leer la portada", f"Lee: {LIBRO} ¿Cuál es el título?", ["El título es el nombre del libro.", "Está entre comillas: «El gato que quería volar»."], "El gato que quería volar"),
        ("Predecir", f"Lee: {LIBRO} ¿De qué puede tratar el libro?", ["El dibujo muestra un gato mirando pájaros.", "La contraportada dice que quiere subir al cielo."], "De un gato que quiere volar como los pájaros"),
    ],
    [
        ("Confundir autor con título.", "Ambos están en la portada.", "El título es el nombre del libro; el autor, quien lo escribió."),
        ("Decidir sin mirar ninguna pista.", "Se elige por azar.", "Mira portada, título y contraportada."),
    ],
    [
        E(f"Lee: {LIBRO} ¿Quién es la autora?", "Marta Ríos", "Su nombre aparece como autora en la portada."),
        E(f"Lee: {LIBRO} ¿Qué animal aparece dibujado en la portada?", "Un gato", "El dibujo muestra un gato mirando pájaros."),
        E("¿Dónde está el título de un libro? A) en la portada B) en la contraportada del reverso", "A) en la portada", "El título se escribe en la parte de adelante."),
    ],
    [
        E(f"Lee: {LIBRO} ¿Qué parte del libro dice «Un gato curioso quiere subir al cielo»?", "La contraportada", "Es el texto de la parte de atrás."),
        E("Antes de abrir un libro, ¿qué es una predicción?", "Pensar de qué tratará el libro antes de leerlo", "Se hace con pistas de portada y título."),
        E("¿Quién es el autor de un libro?", "La persona que lo escribió", "Su nombre está en la portada."),
    ],
    [
        E("Un libro tiene el título «La tortuga y el mar». En la portada hay una tortuga nadando. ¿De qué crees que trata?", "De una tortuga en el mar", "El título y el dibujo coinciden."),
        E("Un libro tiene el título «Mi primer día de clases» y un niño con mochila. ¿Quién crees que es el personaje principal?", "Un niño en su primer día de clases", "El dibujo y el título lo muestran."),
        E("Un libro tiene el título «Recetas de pan». ¿Servirá para aprender a cocinar o para ver planetas? Escribe cuál.", "Para aprender a cocinar", "El título habla de recetas."),
    ],
    [
        E("Dos libros: «El zorro y las uvas» con un zorro y un racimo, y «Los planetas» con dibujos del espacio. ¿Cuál servirá para saber cómo es Marte?", "«Los planetas»", "Trata del espacio."),
        E("Luis dijo que «El gato que quería volar» trata de una tortuga. ¿Qué pista de la portada muestra que se equivoca?", "El dibujo de un gato", "El título y la imagen hablan de un gato."),
    ],
    [
        E("Dos portadas: «El gato que quería volar» con un gato y pájaros, y «Dinosaurios gigantes» con huesos grandes. ¿Cuál elegirías para leer sobre animales de hace mucho?", "«Dinosaurios gigantes»", "Los dinosaurios vivieron hace mucho."),
        E("Escribe el título de un libro inventado que trate de un perro explorador.", "Por ejemplo: El perro explorador", "El título debe mostrar el tema."),
    ],
    [E("Caro está en la biblioteca y quiere un libro para saber cómo viven los pingüinos. Ve «Pingüinos del sur» y «El castillo encantado». ¿Cuál elige?", "«Pingüinos del sur»", "El título muestra que trata del tema.")],
    [
        E("¿Cómo se llama la parte de adelante del libro?", "Portada", "Lleva título y dibujo."),
        E("¿Para qué sirve mirar la contraportada?", "Para saber un poco de qué trata", "Cuenta un resumen breve."),
        E("¿Qué es el título?", "El nombre del libro", "Dice cómo se llama el libro."),
    ],
    task(
        "Mira esta portada descrita: título «El oso y la luna», dibujo de un oso mirando una luna llena. Escribe tu predicción: ¿de qué crees que trata? Usa «Creo que... porque...».",
        "Creo que el libro trata de un oso que quiere alcanzar la luna porque en el dibujo la mira y el título nombra la luna.",
        ["usa «Creo que... porque...»", "nombra una pista de la portada", "la predicción es posible"],
        ["oración escrita", "respuesta oral"],
        ["no dar razón", "predecir algo sin relación con las pistas"],
        "Relee el título y mira el dibujo; si tu idea no se apoya en ellos, cámbiala.",
    ),
    "Mira la portada de un libro de tu casa y di su título y su autor.",
    "Dibuja la portada de un libro inventado con título y autor.",
)

lesson(
    OA11, 2,
    "Cuaderno y lápiz. Las ilustraciones están descritas con palabras en cada ejercicio.",
    "Aprenderé a leer las ilustraciones: lo que muestran y lo que hacen sentir. Sirve para entender mejor un libro, aun sin leer todas las palabras.",
    ["Sé mirar dibujos con atención.", "Sé nombrar colores y objetos."],
    [
        "Las ilustraciones también cuentan. Un dibujo puede mostrar quiénes son los personajes, dónde están y qué pasa. Para leer una ilustración, mira primero qué hay: personas, animales, lugares y objetos. Luego piensa qué hacen.",
        "Los colores y los gestos dan pistas de lo que sienten los personajes. Si un niño tiene la boca hacia arriba y los ojos abiertos, parece contento. Si el cielo es gris y los árboles se doblan, puede haber viento o tormenta.",
        "Las ilustraciones se completan con las palabras. A veces el dibujo muestra algo que el texto no dice. Por eso conviene mirar y leer juntos, y no sólo una de las dos cosas.",
    ],
    [("ilustración", "dibujo que acompaña el texto"), ("personaje", "quien aparece en la historia"), ("lugar", "dónde ocurre la historia"), ("gesto", "movimiento de la cara o del cuerpo que muestra lo que siente"), ("detalle", "una parte pequeña pero importante")],
    [
        ("Mirar el dibujo", "Una ilustración muestra: de noche, un niño con linterna, un bosque y dos luces amarillas entre los árboles. ¿Cuándo ocurre?", ["Hay linterna y se ve oscuro.", "Eso es de noche."], "De noche"),
        ("Gestos", "En otra ilustración, una niña tiene los ojos muy abiertos y las manos en la boca. ¿Qué siente?", ["Ojos abiertos y manos en la boca muestran sorpresa o susto.", "Es una emoción fuerte."], "Sorpresa o susto"),
    ],
    [
        ("Mirar sólo una parte del dibujo.", "Se apura la lectura.", "Revisa todo: personajes, lugar y objetos."),
        ("Decir lo que siente el personaje sin mirar su cara.", "Se adivina.", "Observa los gestos para decidir."),
    ],
    [
        E("Ilustración: un perro grande corre tras una pelota roja en un parque con árboles. ¿Qué hace el perro?", "Corre tras una pelota", "El dibujo muestra al perro en movimiento."),
        E("Ilustración: una niña sonríe con los brazos abiertos frente a su abuela. ¿Está contenta o triste?", "Contenta", "La sonrisa y los brazos abiertos muestran alegría."),
        E("Ilustración: un barco pequeño en un mar con grandes olas y cielo gris. ¿Hace buen tiempo?", "No", "Las olas grandes y el cielo gris indican mal tiempo."),
    ],
    [
        E("Ilustración: una niña con paraguas y botas, gotas cayendo, charcos en el suelo. ¿Qué tiempo muestra?", "Lluvia", "Las gotas, el paraguas y los charcos lo indican."),
        E("¿Dónde pueden ocurrir las ilustraciones de un pez y burbujas?", "En el agua", "Los peces y burbujas viven bajo el agua."),
        E("¿Qué puede mostrar una ilustración además de personajes?", "El lugar y los objetos", "También cuenta dónde ocurre y qué hay."),
    ],
    [
        E("Texto: «Nico llegó a la plaza». Ilustración: Nico con un globo azul y muchas personas alrededor. ¿Qué dato extra da la ilustración?", "Que Nico tiene un globo azul", "El dibujo agrega información que el texto no dice."),
        E("Ilustración: un niño dormido, luna en la ventana y un osito en la cama. ¿Qué hora del día es?", "La noche", "La luna y el sueño muestran la noche."),
        E("Ilustración: un conejo tiene las orejas caídas y ojos llorosos. ¿Cómo se siente?", "Triste", "Las orejas caídas y las lágrimas muestran pena."),
    ],
    [
        E("Ilustración: un niño con la boca abierta y las manos en la cabeza, y una torre de bloques en el suelo. ¿Qué puede haber pasado?", "Que se cayó la torre de bloques", "Los bloques en el suelo y su gesto lo sugieren."),
        E("Un niño dice que en una ilustración hay sol, pero el dibujo está lleno de nubes oscuras y rayos. ¿Qué pista muestra que se equivoca?", "Las nubes oscuras y los rayos", "Esos detalles indican tormenta."),
    ],
    [
        E("Dos ilustraciones: A) una niña ríe con globos y torta. B) una niña llora sola bajo la lluvia. ¿En cuál es probable que sea un cumpleaños?", "En la A", "La torta y los globos son de fiesta."),
        E("Ilustración: un zorro mira un racimo de uvas muy alto. ¿Qué quiere hacer?", "Alcanzar las uvas", "Mira las uvas hacia arriba y parece querer tomarlas."),
    ],
    [E("En una biblioteca hay un libro sin texto, sólo con dibujos. Ilustración 1: una semilla en la tierra. 2: un brote pequeño. 3: una planta con flores. ¿Qué cuenta la historia?", "Cómo crece una planta", "Las tres ilustraciones muestran el crecimiento.")],
    [
        E("¿Qué muestran las ilustraciones?", "Personajes, lugares y lo que pasa", "Cuentan parte de la historia."),
        E("Los gestos de la cara muestran...", "Lo que siente el personaje", "Son pistas de emociones."),
        E("¿Las ilustraciones sirven para entender un libro?", "Sí", "Aportan pistas y detalles."),
    ],
    task(
        "Lee esta ilustración descrita: un niño sentado en una banca, con una mochila, mirando la lluvia por la ventana, con la boca hacia abajo. Escribe dos cosas que descubres mirando la ilustración (por ejemplo, cómo se siente) y qué detalle usaste.",
        "Descubro que el niño está triste porque tiene la boca hacia abajo. Descubro que llueve porque se ve la lluvia por la ventana.",
        ["dos cosas descubiertas", "cada una tiene un detalle de la ilustración", "se entienden"],
        ["dos oraciones escritas", "explicación oral"],
        ["inventar algo sin detalle", "una sola idea", "copiar la descripción"],
        "Pregúntate qué detalle te hizo pensar eso y anótalo.",
    ),
    "Mira un dibujo de un libro y di tres cosas que ves.",
    "Dibuja una escena de lluvia y marca tres detalles que cuenten qué pasa.",
)

PRIMERAS = "Libro A, primera línea: «Había una vez un dragón que tenía miedo del fuego». Libro B, primera línea: «Las ballenas son los animales más grandes del mar». Libro C, primera línea: «Primero, corta el papel en cuadrados»."

lesson(
    OA11, 3,
    "Cuaderno y lápiz. Las primeras líneas de tres libros están escritas en los ejercicios.",
    "Aprenderé a probar un libro antes de decidir: miro la portada, leo una página y observo las ilustraciones. Sirve para elegir un libro que quiero leer.",
    ["Sé mirar portada y título.", "Sé leer una oración corta."],
    [
        "Antes de elegir un libro conviene probarlo. Primero mira la portada y el título. Luego abre el libro y hojéalo: pasa las páginas mirando las ilustraciones. Después lee una página o unas líneas para saber si se entiende y si te gusta.",
        "La primera línea cuenta mucho. «Había una vez un dragón...» anuncia un cuento. «Las ballenas son los animales más grandes del mar» anuncia un libro informativo. «Primero, corta el papel» anuncia instrucciones. Así puedes saber qué tipo de libro es.",
        "Elige según lo que te interesa: si te gustan los animales, busca libros de animales. Si puedes leer la mayor parte de una página sin atascarte, el libro es adecuado para ti. Si no, puedes pedir que un adulto te lo lea.",
    ],
    [("hojear", "pasar las páginas mirando rápido"), ("probar", "mirar y leer un poco antes de decidir"), ("interés", "lo que me gusta saber o leer"), ("cuento", "historia inventada"), ("libro informativo", "libro que da datos sobre un tema")],
    [
        ("Reconocer el tipo", f"Lee: {PRIMERAS} ¿Qué libro es un cuento?", ["«Había una vez» anuncia un cuento.", "Es el libro A."], "El libro A"),
        ("Elegir por interés", f"Lee: {PRIMERAS} A Tomás le gustan los animales marinos. ¿Qué libro prueba?", ["Marinos significa del mar.", "El libro B habla de ballenas en el mar."], "El libro B"),
    ],
    [
        ("Elegir sólo por la portada bonita.", "Se mira sólo lo de afuera.", "Hojea y lee una página antes de decidir."),
        ("Elegir un libro muy difícil.", "Se quiere leer algo largo.", "Lee una página: si se entiende, es adecuado."),
    ],
    [
        E(f"Lee: {PRIMERAS} ¿Qué libro habla de ballenas?", "El libro B", "Su primera línea nombra a las ballenas."),
        E(f"Lee: {PRIMERAS} ¿Qué libro tiene instrucciones para hacer algo?", "El libro C", "Dice «Primero, corta el papel en cuadrados»."),
        E("¿Qué se hace con un libro para probarlo? A) hojearlo y leer una página B) botarlo", "A) hojearlo y leer una página", "Así sabes si te gusta."),
    ],
    [
        E(f"Lee: {PRIMERAS} ¿Qué libro es informativo?", "El libro B", "Da un dato verdadero sobre las ballenas."),
        E(f"Lee: {PRIMERAS} ¿Cuál es el personaje del libro A?", "Un dragón", "La primera línea nombra un dragón."),
        E("¿Para qué sirve leer la primera línea de un libro?", "Para saber qué tipo de libro es", "Anuncia si es cuento, dato o instrucción."),
    ],
    [
        E(f"Lee: {PRIMERAS} A Ema le gusta hacer manualidades. ¿Qué libro prueba?", "El libro C", "Trae instrucciones para trabajar con papel."),
        E(f"Lee: {PRIMERAS} A Beto le encantan las historias con dragones. ¿Qué libro prueba?", "El libro A", "Habla de un dragón."),
        E("Lee esta primera línea: «Dobla el papel por la mitad.» ¿Qué tipo de libro es probablemente?", "Un libro de instrucciones", "Dice una acción para hacer."),
    ],
    [
        E("Camila lee una página del libro y se detiene en seis palabras que no entiende. ¿Es adecuado para ella sola? Responde sí o no.", "No", "Hay muchas palabras difíciles; necesita ayuda."),
        E("Pedro quiere un libro para aprender sobre planetas. Se fija sólo en que la portada es roja. ¿Es buena forma de elegir? Responde sí o no.", "No", "Debe mirar el tema, no sólo el color."),
    ],
    [
        E(f"Lee: {PRIMERAS} Un niño dice: «Quiero un libro que me haga reír con un personaje que sea fantástico». ¿Qué libro puede ser?", "El libro A", "Un dragón con miedo del fuego es un personaje fantástico."),
        E("Ordena los pasos para elegir un libro: a) Leer una página. b) Mirar la portada. c) Hojear las ilustraciones. Escribe las letras.", "b, c, a", "Se mira afuera, luego se hojea y al final se lee."),
    ],
    [E("En la biblioteca Rosa quiere un libro de insectos. Encuentra uno cuya primera línea dice: «Las hormigas viven en colonias muy grandes». ¿Le sirve?", "Sí", "Habla de hormigas, que son insectos.")],
    [
        E("¿Qué significa hojear?", "Pasar las páginas mirando", "Se mira rápido el contenido."),
        E("¿Qué palabras anuncian un cuento? A) Había una vez B) Mezcla y hornea", "A) Había una vez", "Es el inicio típico de un cuento."),
        E("¿Qué se mira para elegir un libro además de la portada?", "Una página y las ilustraciones", "Sirven para probarlo."),
    ],
    task(
        "Elige uno de estos tres libros: A) «Había una vez un dragón que tenía miedo del fuego». B) «Las ballenas son los animales más grandes del mar». C) «Primero, corta el papel en cuadrados». Escribe cuál elegirías para leer ahora y por qué usando «Elijo... porque...».",
        "Elijo el libro B porque me gustan los animales del mar.",
        ["dice qué libro elige", "usa «porque» con una razón", "la razón se relaciona con la primera línea o con el interés"],
        ["oración escrita", "respuesta oral"],
        ["no dar razón", "elegir sin relación con el texto"],
        "Lee la primera línea de tu libro en voz alta para confirmar que te gusta.",
    ),
    "Hojea un libro de tu casa y lee una línea en voz alta.",
    "Prueba dos libros distintos y cuenta cuál te gustó más.",
)

lesson(
    OA11, 4,
    "Cuaderno y lápiz. Los comentarios de lectores están escritos en los ejercicios.",
    "Aprenderé a conversar sobre un libro con otros lectores: contar qué me gustó, escuchar y recomendar. Sirve para disfrutar más la lectura.",
    ["Sé contar lo que me gustó.", "Sé esperar mi turno para hablar."],
    [
        "Los lectores conversan sobre los libros. Pueden contar de qué trata, qué parte les gustó y si lo recomiendan. Para conversar bien, cada uno habla en su turno, mira a quien habla y escucha hasta el final.",
        "Una buena recomendación dice el nombre del libro, de qué trata y por qué lo recomiendas. Por ejemplo: «Te recomiendo El gato que quería volar porque es divertido y tiene lindas ilustraciones».",
        "Cuando otro lector habla, puedes preguntar o comentar con respeto: «¿Qué parte te gustó más?» o «Yo pensé distinto porque...». Así aprendes a ver el libro de otra forma.",
    ],
    [("recomendar", "decir a otro que lea un libro y por qué"), ("turno", "el momento en que me toca hablar"), ("escuchar", "poner atención a lo que dice otro"), ("comentar", "decir lo que pienso de algo"), ("respeto", "tratar bien a los demás")],
    [
        ("Recomendar", "Ana leyó «El gato que quería volar». Dice: «Te lo recomiendo porque es divertido y tiene lindas ilustraciones». ¿Qué razones da?", ["Busco después de «porque».", "Dice dos: divertido y lindas ilustraciones."], "Que es divertido y tiene lindas ilustraciones"),
        ("Respetar el turno", "Tres niños quieren hablar a la vez. ¿Qué deben hacer?", ["Levantar la mano.", "Esperar que termine el que habla."], "Levantar la mano y esperar su turno"),
    ],
    [
        ("Hablar todos a la vez.", "Hay entusiasmo por contar.", "Levanta la mano y espera tu turno."),
        ("Decir «es malo» sin razón.", "No se piensa por qué.", "Usa «porque» y di una parte concreta del libro."),
    ],
    [
        E("Beto dice: «El libro trata de un oso que busca miel». ¿De qué trata el libro?", "De un oso que busca miel", "Beto lo cuenta."),
        E("¿Qué hace un buen oyente cuando alguien habla? A) lo escucha hasta el final B) lo interrumpe", "A) lo escucha hasta el final", "Escuchar es parte de conversar."),
        E("¿Qué se hace para pedir la palabra?", "Levantar la mano", "Así se respeta el turno."),
    ],
    [
        E("Lucía dice: «Me gustó la parte en que el gato por fin sube al árbol». ¿Qué parte le gustó?", "Cuando el gato sube al árbol", "Lo dice directamente."),
        E("Una recomendación dice: «Lee Los planetas porque tiene dibujos grandes». ¿Qué razón da?", "Tiene dibujos grandes", "Viene después de «porque»."),
        E("Para comentar con respeto, ¿cuál frase sirve? A) «Qué libro más tonto» B) «Yo pensé distinto porque...»", "B) «Yo pensé distinto porque...»", "Es respetuosa y da una razón."),
    ],
    [
        E("Escribe una recomendación para el libro «El oso y la luna» que diga el título y una razón.", "Por ejemplo: Te recomiendo El oso y la luna porque es una historia tierna", "Debe incluir el título y «porque»."),
        E("Escribe una pregunta que le harías a un amigo sobre el libro que leyó.", "Por ejemplo: ¿Qué parte te gustó más?", "Es una pregunta sobre el libro."),
        E("Completa: «Mi parte favorita fue cuando ...»", "Por ejemplo: el gato aprendió a trepar", "Debe nombrar una parte del libro."),
    ],
    [
        E("Dos niños comentan: Iván: «Me gustó porque el dragón es gracioso». Mía: «Está bien». ¿Quién dio mejor su comentario?", "Iván", "Dio una razón concreta."),
        E("Pablo interrumpe a Daniela cuando cuenta el libro. ¿Qué debería hacer en vez de eso?", "Esperar a que termine y pedir su turno", "Así respeta su turno."),
    ],
    [
        E("Tres niños hablan del mismo libro y uno dice algo distinto. ¿Es malo pensar distinto? Responde sí o no.", "No", "Cada lector puede ver el libro a su manera."),
        E("¿Cuántas partes tiene una buena recomendación: título, de qué trata y razón? Cuenta.", "3", "Son el título, el tema y la razón."),
    ],
    [E("En el círculo de lectura Ema dice: «Leí El gato que quería volar. Trata de un gato curioso. Lo recomiendo porque es divertido». ¿Qué tres cosas dijo?", "El título, de qué trata y por qué lo recomienda", "Cumple las tres partes de una recomendación.")],
    [
        E("¿Qué se debe hacer cuando otro habla?", "Escucharlo", "Es parte de respetar su turno."),
        E("En una recomendación de un libro, ¿qué palabra introduce la razón?", "Porque", "Une la opinión con su explicación."),
        E("¿Para qué sirve conversar sobre libros?", "Para compartir lo que pensamos y aprender de otros", "Ayuda a disfrutar más la lectura."),
    ],
    task(
        "Practica una conversación de lectores con alguien de tu casa. Cuéntale de este libro: «El gato que quería volar», de un gato curioso que mira a los pájaros. Di el título, de qué trata y si lo recomendarías con «porque». Pauta de oralidad: hablo fuerte y claro; espero mi turno; miro a quien habla.",
        "El libro se llama El gato que quería volar. Trata de un gato curioso que mira a los pájaros. Lo recomiendo porque es divertido.",
        ["dice el título", "cuenta de qué trata", "da una razón con «porque»", "habla claro y espera su turno"],
        ["conversación con un adulto", "la recomendación escrita"],
        ["hablar sin decir el título", "no dar razón", "interrumpir"],
        "Pide a tu compañero que te diga qué parte de tu recomendación entendió mejor.",
    ),
    "Cuenta a alguien de tu casa el libro que más te ha gustado.",
    "Pregunta a un familiar qué libro le gustaba de niño y por qué.",
)

lesson(
    OA11, 5,
    "Cuaderno, lápiz y una hoja para hacer tu ficha. El modelo de ficha está escrito en los ejercicios.",
    "Aprenderé a llevar un registro de los libros que leo para ver mi recorrido como lector. Sirve para recordar y para elegir mejor.",
    ["Sé el título de un libro que he leído o escuchado.", "Sé escribir palabras cortas."],
    [
        "Un recorrido lector es la lista de los libros que has leído o escuchado. Se puede anotar en una ficha con el título, de qué trata, una nota de 1 a 3 estrellas y lo que más te gustó. Así recuerdas lo que ya leíste.",
        "La ficha te sirve para mirar lo que más te gusta. Si muchos de tus libros son de animales, ya sabes qué buscar en la biblioteca. También puedes ver cómo cambió tu gusto con el tiempo.",
        "Al terminar un libro, pregúntate: ¿qué aprendí?, ¿qué me gustó?, ¿lo recomendaría? Anota las respuestas. Es tu historia de lector.",
    ],
    [("ficha", "hoja con los datos de un libro que leí"), ("recorrido", "el camino de libros que he leído"), ("estrellas", "marcas para indicar cuánto me gustó (1, 2 o 3)"), ("favorito", "el que más me gusta"), ("registro", "lista que anoto para recordar")],
    [
        ("Leer una ficha", "Ficha: Título: «El gato que quería volar». Estrellas: 3. Lo que más me gustó: el final. ¿Cuántas estrellas le puso?", ["Busco la palabra estrellas.", "Dice 3."], "3 estrellas"),
        ("Contar libros", "Lista: «El oso y la luna», «Los planetas», «El gato que quería volar». ¿Cuántos libros ha leído?", ["Cuento los títulos.", "Hay tres."], "3 libros"),
    ],
    [
        ("Anotar el libro sin decir qué me gustó.", "Se cree que basta con el título.", "Agrega por qué te gustó."),
        ("Poner estrellas sin pensar.", "Se marca por apuro.", "Piensa cuánto te gustó y recuerda una parte."),
    ],
    [
        E("Ficha: «Los planetas». Estrellas: 2. ¿Cuántas estrellas tiene?", "2", "La ficha lo indica."),
        E("Ficha: Título: «El oso y la luna». Lo que más me gustó: las ilustraciones. ¿Qué le gustó?", "Las ilustraciones", "Lo dice la ficha."),
        E("Lista: «Pingüinos del sur», «El zorro y las uvas». ¿Cuántos libros hay?", "2", "Hay dos títulos."),
    ],
    [
        E("Una ficha tiene: título, de qué trata, estrellas, lo que más me gustó. ¿Cuántos datos lleva?", "4", "Son cuatro datos."),
        E("¿Para qué sirve la ficha de un libro?", "Para recordar lo que leí", "Guarda título, tema y opinión."),
        E("Si una niña lee tres libros de animales y uno de planetas, ¿qué tema le gusta más?", "Animales", "Leyó más libros de animales."),
    ],
    [
        E("Completa la ficha: Título: «El gato que quería volar». De qué trata: ...", "De un gato curioso que quería volar", "Resume la historia en una oración."),
        E("Una niña puso 3 estrellas a «El oso y la luna». ¿Le gustó mucho o poco?", "Mucho", "Tres estrellas es la nota más alta."),
        E("Escribe en una oración qué te gusta de leer.", "Por ejemplo: Me gusta leer porque aprendo cosas nuevas", "Debe expresar una razón personal."),
    ],
    [
        E("Lista de Tomás: Animales: 3 libros. Cuentos de aventura: 1 libro. Recetas: 0. ¿Qué tema debería buscar en la biblioteca si quiere repetir lo que más le gusta?", "Animales", "Es el tema con más libros."),
        E("Ana tiene la ficha de «Los planetas» sin estrellas ni opinión. ¿Qué falta para que sirva para recordar?", "Las estrellas y lo que más le gustó", "Son los datos de opinión."),
    ],
    [
        E("Recorrido: enero, 2 libros; febrero, 3 libros; marzo, 4 libros. ¿Cuántos libros leyó en total?", "9", "2 más 3 más 4 son 9."),
        E("Elige: ¿qué ficha es más útil? A) «Lo leí» B) «El oso y la luna, 3 estrellas, me gustaron los dibujos»", "B) «El oso y la luna, 3 estrellas, me gustaron los dibujos»", "Tiene título, nota y razón."),
    ],
    [E("En el curso hacen un mural con los libros leídos. Rosa leyó «El zorro y las uvas» y «Los planetas». Pega una ficha por libro. ¿Cuántas fichas pega?", "2", "Una ficha por cada libro.")],
    [
        E("¿Cómo se llama la hoja donde anoto un libro que leí?", "Ficha", "Guarda los datos del libro."),
        E("¿Qué número de estrellas es el máximo en nuestra ficha?", "3", "La escala es de 1 a 3."),
        E("¿Qué debo anotar además del título?", "De qué trata y qué me gustó", "Así recuerdo el libro."),
    ],
    task(
        "Completa esta ficha con un libro real que hayas leído o escuchado, o con «El gato que quería volar» si no tienes otro: Título; De qué trata (una oración); Estrellas (1 a 3); Lo que más me gustó (una oración).",
        "Título: El gato que quería volar. De qué trata: de un gato curioso que quiere ser como los pájaros. Estrellas: 3. Lo que más me gustó: el final.",
        ["completa los cuatro datos", "las oraciones se entienden", "la nota está entre 1 y 3"],
        ["ficha escrita", "lectura en voz alta"],
        ["dejar un dato vacío", "poner una nota fuera de 1 a 3", "no decir de qué trata"],
        "Lee tu ficha a otro y pregúntale si entiende de qué trata el libro.",
    ),
    "Anota los títulos de tres libros que conozcas y pon estrellas a cada uno.",
    "Dibuja tu libro favorito y escribe por qué lo es.",
)
