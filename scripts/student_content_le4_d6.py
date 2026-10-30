"""Cuaderno del estudiante, 4.º básico Lenguaje y Comunicación: OA 29 (caracterización colaborativa de personajes)."""
from __future__ import annotations

from student_content_le4_d import E, reg
from student_lessons import arith

OA29 = "LE04 OA 29"

# ================================================================ OA 29 · clase 1
reg(
    OA29, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer la escena en voz alta.",
    "Aprenderé a descubrir cómo es un personaje y qué quiere lograr, usando lo que hace y dice en el texto. Sirve para poder representarlo después con voz y gestos.",
    ["Sé reconocer personajes y acciones en una escena.", "Sé dar una pista que apoya lo que pienso."],
    [
        "Caracterizar a un personaje es mostrar cómo es y qué quiere, con la voz, el cuerpo y las palabras. Para hacerlo, primero lo conocemos. Un rasgo es una característica del personaje, como ser cuidadoso, curioso o impaciente. La intención es lo que el personaje quiere lograr en la escena. Ni los rasgos ni la intención suelen decirse directamente: los inferimos, es decir, los deducimos a partir de pistas.",
        "Las pistas son sus acciones («coloca las cartulinas con cuidado»), sus palabras («gracias, pero primero quiero practicar sola») y lo que hace con los demás. Para inferir, usamos la fórmula: pista + conclusión. Por ejemplo: «Repite su explicación en voz baja, por eso quiere prepararse bien». Si no hay pista, no podemos asegurar la conclusión.",
        "Varias pistas que apuntan a lo mismo hacen más fuerte la conclusión. Si hay pistas que se contradicen, miramos cuál se repite más o cuál pesa más. Un personaje puede tener más de un rasgo y puede querer algo distinto de lo que dice. Nuestro trabajo es leer con atención.",
    ],
    [("caracterizar", "mostrar cómo es un personaje y qué quiere"), ("rasgo", "característica de un personaje, como ser cuidadoso"), ("intención", "lo que el personaje quiere lograr"), ("inferir", "deducir algo a partir de pistas"), ("pista", "acción o palabra del texto que apoya una idea")],
    [
        ("Inferir el rasgo", "Escena «La feria de ciencias»: Dora llega temprano, coloca sus cartulinas con mucho cuidado y repite su explicación en voz baja. Cuando Gabo le ofrece ayuda, dice: «Gracias, pero primero quiero practicar sola». ¿Qué rasgo muestra el hecho de que coloque las cartulinas con mucho cuidado?", ["Busco qué dice esa acción de Dora.", "Colocar con mucho cuidado muestra que es cuidadosa.", "Es una pista de su rasgo."], "Es cuidadosa."),
        ("Inferir la intención", "En la escena de Dora, ¿qué quiere lograr al practicar sola?", ["Reúno las pistas: llega temprano, repite su explicación.", "Todas apuntan a prepararse.", "Su intención es explicar bien en la feria."], "Quiere explicar bien en la feria."),
    ],
    [("Decir un rasgo sin ninguna pista, como «Dora es mala».", "Se opina sin mirar el texto.", "Cita lo que hace o dice y explica qué muestra."), ("Confundir rasgo con intención.", "Ambas hablan del personaje.", "El rasgo es cómo es; la intención es lo que quiere lograr ahora.")],
    [
        E("En la escena, ¿cuándo llega Dora a la sala: temprano o tarde?", "Temprano", "Lo dice la primera acción."),
        E("¿Qué le ofrece Gabo a Dora?", "Ayuda", "Le pregunta si quiere ayuda."),
        E("¿Qué responde Dora a Gabo: acepta enseguida o dice que primero quiere practicar sola?", "Dice que primero quiere practicar sola", "Esa es su respuesta."),
    ],
    [
        E("¿Qué es una intención?", "Lo que un personaje quiere lograr", "Guía sus acciones."),
        E("¿Un rasgo se dice siempre directamente en el texto?", "No", "Muchas veces se infiere por las pistas."),
        E("«Repite su explicación en voz baja, por eso quiere prepararse bien». ¿Cuál es la pista?", "Repite su explicación en voz baja", "Es una acción que se puede ver."),
    ],
    [
        E("Escena: «Beto entra corriendo, mira el reloj y dice: ¡Rápido, que nos faltan diez minutos! Reparte los materiales y pregunta quién necesita pegamento». ¿Cuál es la intención de Beto: terminar a tiempo o irse a casa?", "Terminar a tiempo", "Mira el reloj y reparte materiales."),
        E("En esa escena de Beto, ¿qué acción muestra que organiza al grupo?", "Reparte los materiales y pregunta quién necesita pegamento", "Ayuda al equipo a trabajar."),
        E("Elige el rasgo que apoya la pista «mira el reloj y apura a los demás»: a) impaciente b) dormilón.", "a", "Apurar a otros muestra impaciencia."),
    ],
    [
        E("Un compañero dice: «Beto es flojo». Otra dice: «Beto es apurado, porque mira el reloj y dice que faltan diez minutos». ¿Quién usó una pista?", "La segunda", "Apoya su idea en lo que dice y hace."),
        E("Dora dice: «Gracias, pero primero quiero practicar sola». ¿Rechaza a Gabo con mala intención?", "No", "Agradece y explica su razón."),
    ],
    [
        E("Escena: «Nina mira el dibujo de su amiga con atención y dice: Me gusta cómo pintaste el cielo. ¿Qué colores usaste? Después le muestra el suyo». ¿Qué rasgo muestra: a) interés por los demás b) enojo?", "a", "Mira con atención y pregunta."),
        E("En esa misma escena, ¿cuántas acciones o palabras muestran su interés: mirar con atención, elogiar el cielo y preguntar por los colores?", "Tres", "Son tres pistas distintas."),
    ],
    [E("Escena: «Mateo guarda sus cosas, se queda de pie junto a la puerta y mira cómo juegan los demás. Cuando lo invitan, dice: Después, tal vez». ¿Cuál es una intención posible apoyada en las pistas: a) sentirse seguro antes de unirse b) irse enojado?", "a", "Observa y responde con cautela.")],
    [
        E("Inferir es deducir a partir de pistas. ¿Verdadero o falso?", "Verdadero", "Eso significa inferir."),
        E("¿Una conclusión necesita al menos una pista?", "Sí", "Sin pista es solo una opinión."),
        E("¿La intención es lo que el personaje quiere lograr?", "Sí", "Es el motivo de sus acciones."),
    ],
    ("Infiere cómo es un personaje. Lee esta escena y escribe el rasgo y la intención de Pía con una pista cada uno. Escena «La mesa de la merienda»: Pía llega con una bolsa de galletas. Mira la mesa, ve que hay poco espacio y mueve su vaso para hacerle sitio a Teo. Dice: «Siéntate aquí, hay lugar para todos». Cuéntaselo a una persona de tu casa.",
     "Rasgo: generosa y atenta, porque mueve su vaso para hacerle sitio a Teo. Intención: que todos puedan sentarse a merendar, porque dice que hay lugar para todos.",
     ["dice un rasgo", "dice una intención", "cada idea tiene su pista", "no inventa datos"], ["respuesta escrita u oral con pistas"], ["dar rasgo sin pista", "confundir rasgo con intención"],
     "Si falta la pista, vuelve a la escena y copia la acción o frase exacta."),
    "Lee en casa una escena corta y di un rasgo con su pista.",
    "Escribe dos pistas distintas para el rasgo «cuidadoso» en una escena que inventes.",
)

# ================================================================ OA 29 · clase 2
reg(
    OA29, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para ver tu ensayo. Muévete en un espacio libre y seguro.",
    "Aprenderé a elegir una voz y un gesto que muestren cómo es mi personaje, sin exagerar hasta la burla. Sirve para representar personajes con respeto y creatividad.",
    ["Sé inferir rasgos e intención con pistas.", "Sé observar voz, cuerpo y espacio en una escena."],
    [
        "Para interpretar un personaje elegimos cómo suena y cómo se mueve. La voz tiene volumen, ritmo y tono. El cuerpo tiene postura, mirada y gestos. Escogemos esas características según el rasgo y la intención que inferimos. Por ejemplo, Dora es cuidadosa y quiere explicar bien: su voz puede ser tranquila, su ritmo pausado, y sus manos pueden acomodar las cartulinas con delicadeza.",
        "Lo importante es mostrar al personaje sin hacer caricatura. Una caricatura exagera tanto un rasgo que el personaje parece una burla. En teatro, caracterizar no significa burlarse de una persona, de su manera de hablar, de su aspecto o de un grupo. Es mejor elegir uno o dos rasgos clave de voz y de gesto, y repetirlos con coherencia.",
        "Para ensayar usamos tres pasos: elegir un rasgo y su intención, probar una voz y un gesto, y revisar si coinciden con las pistas del texto. También cuidamos que lo que hagamos sea seguro en el espacio donde estamos, sin saltos, empujones ni movimientos bruscos.",
    ],
    [("caricatura", "exageración de un rasgo hasta parecer burla"), ("coherencia", "que la voz, el gesto y las acciones concuerden"), ("tono", "manera de decir algo con la voz"), ("postura", "forma de colocar el cuerpo"), ("gesto clave", "movimiento principal que ayuda a mostrar el rasgo")],
    [
        ("Elegir voz y gesto", "Dora es cuidadosa y quiere explicar bien. ¿Qué voz y qué gesto le corresponden: a) voz tranquila y manos que acomodan las cartulinas con cuidado b) gritos y brazos que lanzan las cartulinas?", ["Pienso en el rasgo cuidadosa.", "La a coincide con cuidado y calma.", "La b es lo contrario."], "a."),
        ("Distinguir caricatura", "Para mostrar que un personaje es distraído, un actor se tropieza muchas veces, con exageración, para que todos se rían. Otro solo mira por la ventana y olvida una palabra. ¿Cuál se acerca a una caricatura?", ["Veo qué exagera.", "Tropezar muchas veces es exagerar el rasgo.", "Mirar por la ventana es un gesto breve."], "El primero."),
    ],
    [("Exagerar el rasgo hasta burlarse de una persona.", "Se cree que exagerar es más gracioso.", "Elige uno o dos gestos clave y manténlos con respeto."), ("Usar una voz o un gesto que no corresponde al rasgo.", "No se revisaron las pistas.", "Comprueba que la voz y el gesto coincidan con las pistas.")],
    [
        E("Un personaje impaciente, ¿habla despacio y mira el reloj o habla rápido y mira el reloj?", "Habla rápido y mira el reloj", "La prisa se nota en el ritmo."),
        E("¿La voz tiene volumen, ritmo y tono?", "Sí", "Son sus características principales."),
        E("¿Caracterizar es burlarse de una persona?", "No", "Es representar con respeto."),
    ],
    [
        E("¿Qué es una caricatura?", "Exagerar un rasgo hasta parecer burla", "Va más allá de mostrar al personaje."),
        E("Un personaje seguro de sí mismo, ¿tiene una postura erguida o encogida?", "Erguida", "La postura firme muestra seguridad."),
        E("¿Por qué conviene elegir solo uno o dos gestos clave?", "Para mostrar el rasgo con claridad y sin exagerar", "Muchos gestos distraen."),
    ],
    [
        E("Beto es impaciente y quiere terminar a tiempo. ¿Cuál es un buen gesto clave: a) mirar el reloj con frecuencia b) quedarse dormido en la silla?", "a", "Mirar el reloj muestra prisa."),
        E("Nina es curiosa y atenta. ¿Qué voz le corresponde: a) tono amable con preguntas b) tono apagado sin preguntas?", "a", "Preguntar muestra curiosidad."),
        E("Ordena los pasos para ensayar: a) revisar si coinciden con las pistas, b) elegir un rasgo y una intención, c) probar una voz y un gesto. Escribe las letras.", "b, c, a", "Primero se elige, luego se prueba y después se revisa."),
    ],
    [
        E("Un actor hace de un niño tímido con tartamudeo exagerado para que el público se ría. ¿Es una caracterización respetuosa?", "No", "Se burla de una forma de hablar."),
        E("Un actor hace de un niño tímido con voz suave, mirada al suelo y pasos cortos. ¿Es una caracterización respetuosa?", "Sí", "Muestra el rasgo sin burla."),
    ],
    [
        E("Para actuar a Dora, un grupo propone tres gestos: acomodar las cartulinas, repetir su explicación en voz baja y saltar de alegría con las cartulinas en alto. ¿Cuál no concuerda con su rasgo cuidadoso?", "Saltar con las cartulinas en alto", "Es un movimiento brusco y poco cuidadoso."),
        E("Dos compañeros ensayan en una sala pequeña. ¿Qué es más seguro: a) gestos de las manos y pasos cortos b) correr por la sala?", "a", "Cuidan su seguridad y la de los demás."),
    ],
    [E("Debes caracterizar a un personaje curioso que descubre una caja cerrada. ¿Qué elección es mejor: a) mirar la caja de cerca, inclinar la cabeza y hacer preguntas con voz alegre b) imitar la voz de una persona real del curso?", "a", "Muestra curiosidad sin burlarse de nadie.")],
    [
        E("¿Una caracterización debe coincidir con las pistas del texto?", "Sí", "Así es coherente."),
        E("¿Podemos burlarnos del aspecto de una persona para actuar?", "No", "La caracterización es respetuosa."),
        E("¿Conviene cuidar la seguridad al moverse?", "Sí", "Evita golpes y accidentes."),
    ],
    ("Construye la voz y el gesto de un personaje. Elige uno: a) Dora, cuidadosa y decidida a explicar bien; b) Beto, impaciente y organizado. Escribe: 1) el rasgo y la intención, 2) tres características de la voz (volumen, ritmo y tono), 3) un gesto clave y una postura, y 4) una cosa que evitarías para no hacer caricatura. Ensáyalo en un espacio seguro frente a una persona de tu casa.",
     "Dora. Rasgo: cuidadosa. Intención: explicar bien. Voz: volumen medio, ritmo pausado, tono tranquilo. Gesto clave: acomodar las cartulinas con cuidado. Postura erguida. Evitaría hacerla temblar o tartamudear para que dé risa.",
     ["indica rasgo e intención", "describe voz, gesto y postura coherentes", "evita la caricatura", "ensaya con seguridad"], ["ficha del personaje y ensayo frente a otra persona"], ["exagerar hasta la burla", "gestos que no coinciden con el rasgo"],
     "Si el gesto no coincide con el rasgo, elige otro que muestre lo mismo con más delicadeza."),
    "Elige un personaje de un cuento y escribe cómo sería su voz y su gesto clave.",
    "Compara dos maneras de actuar un mismo rasgo, una con caricatura y otra respetuosa, y explica la diferencia.",
)

# ================================================================ OA 29 · clase 3
reg(
    OA29, 3,
    "Este cuaderno, lápiz y una hoja. Una persona de tu casa que te haga las preguntas en voz alta.",
    "Aprenderé a responder preguntas como si fuera mi personaje, manteniendo su manera de ser y lo que quiere. Sirve para improvisar con seguridad y coherencia.",
    ["Sé inferir rasgos e intención.", "Sé elegir voz y gesto sin hacer caricatura."],
    [
        "Mantener el personaje es hablar y actuar como lo haría él o ella durante toda la escena, aunque no tengamos el guion. Para eso nos hacemos una ficha mental: ¿cómo es?, ¿qué quiere?, ¿cómo suena y se mueve? Cuando alguien nos pregunta algo, respondemos en primera persona, con «yo», y desde lo que el personaje sabe y desea.",
        "Una respuesta en personaje cumple tres condiciones: coincide con el rasgo, ayuda a su intención y no contradice lo que ya se dijo. Si Dora es cuidadosa y quiere explicar bien, no diría «no me importa la feria». Diría: «Prefiero practicar una vez más para no equivocarme».",
        "Si la otra persona propone algo en la escena, aceptamos su idea y la ampliamos con una frase como «Sí, y además…». Así la escena fluye. Si nos equivocamos, podemos seguir y corregir en la siguiente frase, sin salir del personaje. Y cuando queremos terminar, salimos con una señal acordada.",
    ],
    [("improvisar", "actuar o hablar sin guion"), ("en personaje", "hablando y actuando como lo haría el personaje"), ("primera persona", "hablar con «yo»"), ("contradecir", "decir algo que choca con lo anterior"), ("ficha del personaje", "resumen de cómo es, qué quiere y cómo suena y se mueve")],
    [
        ("Responder en personaje", "Una entrevistadora pregunta a Dora, cuidadosa y preparada: «¿Por qué practicas tanto?». ¿Qué respuesta mantiene a Dora: a) «Porque quiero explicar sin equivocarme» b) «No me importa la feria»?", ["Pienso en su rasgo y su intención.", "Dora quiere explicar bien.", "La a lo mantiene."], "a."),
        ("Evitar contradecir", "Antes Dora dijo que le gusta preparar todo con tiempo. Ahora le preguntan por qué llegó tarde. ¿Qué respuesta no contradice a Dora: a) «Tuve un problema en el camino, pero ya estoy preparada» b) «Siempre llego tarde»?", ["Reviso lo que dijo antes.", "Dijo que prepara con tiempo.", "La a no choca con eso."], "a."),
    ],
    [("Salirse del personaje y responder como uno mismo.", "Se pierde la concentración.", "Piensa: ¿cómo respondería él o ella?"), ("Decir que no a todo lo que propone la otra persona.", "Se cree que aceptar es perder la escena.", "Acepta la idea y agrégale algo: «Sí, y además…».")],
    [
        E("Al responder en personaje, ¿hablamos en primera persona con «yo»?", "Sí", "Hablamos como el personaje."),
        E("¿Qué es improvisar?", "Actuar o hablar sin guion", "Se crea en el momento."),
        E("¿Una respuesta en personaje debe contradecir lo que el personaje ya dijo?", "No", "Debe ser coherente."),
    ],
    [
        E("Un personaje impaciente responde con frases cortas y rápidas. Le preguntan «¿Cómo estás?». ¿Qué respuesta calza: a) «Apurado. ¿Podemos empezar?» b) «Con calma, sin apuro, tengo todo el día»?", "a", "Es impaciente y quiere apurarse."),
        E("Una respuesta en personaje coincide con el rasgo, ayuda a su intención y no contradice lo anterior. ¿Cuántas condiciones cumple?", "Tres", "Se cuentan las tres condiciones."),
        E("Si otra persona propone una idea, ¿qué frase sirve para aceptarla y ampliarla: «Sí, y además…» o «No, no, no»?", "Sí, y además…", "Acepta y suma."),
    ],
    [
        E("Nina es curiosa. Le preguntan «¿Qué haces en la sala vacía?». ¿Qué respuesta calza: a) «Quiero ver qué hay en esa caja» b) «No me interesa nada»?", "a", "La curiosidad se nota."),
        E("Beto es organizado. Le preguntan «¿Quién trae el pegamento?». ¿Qué responde: a) «Yo lo traigo; Dora, tú las cartulinas» b) «No sé»?", "a", "Reparte tareas como persona organizada."),
        E("Le preguntan a Dora: «¿Por qué practicas tanto?». Ordena su respuesta: a) Porque quiero explicar sin equivocarme. b) Gracias por preguntar. c) Por eso practico una vez más. Escribe las letras.", "b, a, c", "Agradece, da su razón y cierra con su acción."),
    ],
    [
        E("Una compañera improvisa como Beto y dice: «Tranquilo, no hace falta preparar nada». ¿Es coherente con un personaje organizado?", "No", "Contradice su rasgo."),
        E("Si en la escena otro personaje dice «Aquí hay una puerta secreta», ¿qué respuesta mantiene la escena: a) «Sí, y detrás debe haber algo importante» b) «Eso no existe»?", "a", "Acepta y amplía."),
    ],
    [
        E("Escena: Dora prepara su explicación. Un compañero dice, en el rol de Gabo: «Te puedo ayudar con tu cartulina». Dora, que quiere practicar sola pero es amable, responde: a) «Gracias, Gabo; primero practico sola y luego te muestro» b) «No quiero tu ayuda»?", "a", "Es amable y mantiene su intención."),
        E("Dora no recuerda una frase. ¿Qué es mejor: a) seguir en personaje y decir «Un momento, déjame revisar mis notas» b) salirse y reír diciendo «no me acuerdo»?", "a", "Resuelve sin dejar el personaje."),
    ],
    [E("Haces de Nina, curiosa. Una persona de tu casa te pregunta «¿Qué piensas de esta caja cerrada?». ¿Cuál es la mejor respuesta de Nina: a) «¡Quisiera abrirla para saber qué hay!» b) «No me importa la caja»?", "a", "Concuerda con su rasgo.")],
    [
        E("¿Aceptar ideas ajenas hace que la escena fluya?", "Sí", "Se construye entre todos."),
        E("¿Hay que revisar lo que el personaje dijo antes para no contradecirlo?", "Sí", "La coherencia lo hace creíble."),
        E("¿Se puede seguir en personaje aunque nos equivoquemos?", "Sí", "Se corrige en la frase siguiente."),
    ],
    ("Improvisa en personaje. Elige a Dora, Beto o Nina. Una persona de tu casa te hará tres preguntas como si fuera periodista: ¿Cómo eres?, ¿Qué quieres lograr hoy?, ¿Qué harás si algo sale mal? Responde en primera persona, en personaje, con la voz y el gesto que elegiste. Pide que anote si tus respuestas coinciden con el rasgo y la intención. Escribe después qué respuesta te salió mejor.",
     "Soy Dora. Soy cuidadosa y me gusta tener todo listo. Quiero explicar sin equivocarme. Si algo sale mal, respiro y lo explico otra vez con calma. Nota recibida: coherente con su rasgo.",
     ["responde en primera persona", "es coherente con rasgo e intención", "mantiene la voz y el gesto", "registra una opinión"], ["respuestas en voz alta y nota escrita"], ["salirse del personaje", "contradecirse"],
     "Si te contradijiste, revisa tu ficha y vuelve a responder con calma."),
    "Responde en personaje a una pregunta que te haga alguien de tu casa y anota si fue coherente.",
    "Escribe una ficha de un personaje nuevo y tres preguntas que le harías.",
)

# ================================================================ OA 29 · clase 4
reg(
    OA29, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: dos personas de tu casa para hacer de equipo. Ensayen en un espacio libre y seguro.",
    "Aprenderé a ensayar una escena en equipo y a dar y recibir retroalimentación respetuosa. Sirve para mejorar mi personaje, confiar en mí y trabajar bien con otros.",
    ["Sé caracterizar a un personaje con voz y gesto sin hacer caricatura.", "Sé responder en personaje."],
    [
        "Un ensayo en equipo funciona mejor cuando cada persona tiene un rol. Por ejemplo, en un grupo de tres: una persona actúa, otra observa con una pauta y la tercera cuida el tiempo. Luego se cambian los roles. Un acuerdo previo ayuda: cada ensayo dura dos minutos, todos esperan su turno y nadie se burla.",
        "La retroalimentación es una opinión que ayuda a mejorar. Una buena retroalimentación tiene dos partes: algo que funcionó con una evidencia («Tu voz tranquila mostró que Dora es cuidadosa») y una sugerencia concreta («Podrías mirar a Gabo cuando le respondes»). No sirve decir «estuvo mal» ni comparar a las personas. Se habla de lo que se vio y se oyó, no de cómo es la persona.",
        "Recibir retroalimentación también es una habilidad: escuchamos hasta el final, agradecemos y elegimos qué probar en el siguiente ensayo. Reconocer lo que hacemos bien fortalece la confianza, y aprender de las sugerencias nos ayuda a crecer. Trabajar en equipo es cuidar que todos se sientan valorados.",
    ],
    [("ensayo", "práctica de la escena antes de mostrarla"), ("pauta", "lista de criterios para observar"), ("retroalimentación", "opinión que dice qué funcionó y qué mejorar"), ("sugerencia", "propuesta concreta para mejorar"), ("rol", "tarea que cumple cada persona del equipo")],
    [
        ("Buena retroalimentación", "Un compañero actuó a Dora con voz tranquila y manos cuidadosas. ¿Qué comentario ayuda más: a) «Tu voz tranquila mostró que Dora es cuidadosa; podrías mirar a Gabo cuando le respondes» b) «Estuvo bien»?", ["Busco el que dice qué funcionó y qué mejorar.", "La a tiene evidencia y una sugerencia.", "La b no dice nada concreto."], "a."),
        ("Organizar un ensayo", "Un equipo de tres tiene tres roles: actor, observador y guía del tiempo. ¿Qué hace el observador: a) mira con una pauta y anota lo que ve b) actúa y cuida el tiempo a la vez?", ["Veo qué rol tiene cada persona.", "El observador mira y anota.", "La a es correcta."], "a."),
    ],
    [("Decir «estuvo mal» o «estuvo bien» sin explicar.", "No se sabe qué cambiar o conservar.", "Di qué viste, qué funcionó y qué probar."), ("Comparar a una persona con otra.", "Se piensa que comparar ayuda.", "Habla de la escena y del personaje, no de quién es mejor.")],
    [
        E("¿Cuántas partes tiene una buena retroalimentación: algo que funcionó y una sugerencia?", "Dos", "Son lo logrado y lo que se puede mejorar."),
        E("¿Qué hace el observador en un ensayo?", "Mira con una pauta y anota", "Ayuda a revisar la escena."),
        E("¿Es respetuoso burlarse del compañero que está ensayando?", "No", "El ensayo es un lugar seguro."),
    ],
    [
        E("¿Qué comentario tiene una sugerencia concreta: a) «Podrías hablar más fuerte en la última frase» b) «Mejora todo»?", "a", "La a dice qué cambiar."),
        E("¿Por qué se acuerdan reglas antes de ensayar?", "Para trabajar con respeto y en orden", "Evitan interrupciones y burlas."),
        E("Al recibir una retroalimentación, ¿qué se hace primero: escuchar hasta el final o interrumpir?", "Escuchar hasta el final", "Se entiende mejor lo que dicen."),
    ],
    [
        arith("Un equipo de 3 personas ensaya la escena de modo que cada una actúa una vez durante 2 minutos. ¿Cuántos minutos dura en total?", "3*2", "Cada persona actúa dos minutos y son tres.", " minutos"),
        E("Un compañero actuó a Beto con ritmo rápido y miró el reloj. Escribe la mejor retroalimentación: a) «El ritmo rápido y mirar el reloj mostraron su prisa; podrías repartir los materiales con un gesto» b) «Eres el mejor»", "a", "Tiene evidencia y sugerencia."),
        E("Ordena el ciclo: a) probar la sugerencia en otro ensayo, b) ensayar, c) recibir retroalimentación. Escribe las letras.", "b, c, a", "Se ensaya, se recibe y se prueba."),
    ],
    [
        E("Dos comentarios sobre el personaje de Nina: 1) «Tu tono amable mostró su curiosidad; podrías agregar una pregunta más». 2) «Lo hiciste peor que Marta». ¿Cuál ayuda a mejorar?", "El 1", "El 2 compara y no dice cómo mejorar."),
        E("Un compañero te dice que habla muy bajito. ¿Qué es mejor responder: a) «Gracias, subo el volumen en el próximo ensayo» b) «Tú no sabes»?", "a", "Recibe la sugerencia con respeto."),
    ],
    [
        E("Un equipo se organiza: Luis actúa, Pía observa con la pauta, Teo cuida el tiempo. Después del ensayo, Pía dice qué funcionó y qué mejorar. ¿Qué conviene hacer en el siguiente ensayo para que todos aprendan: cambiar roles o seguir siempre con el mismo?", "Cambiar roles", "Así todos practican."),
        E("Pía anotó: «La voz de Luis fue clara; podría mirar a Teo cuando le habla». ¿Cuál es la sugerencia?", "Mirar a Teo cuando le habla", "Dice qué hacer."),
    ],
    [E("Tu equipo ensaya una escena y una compañera se pone nerviosa y olvida su frase. ¿Qué reacción del equipo ayuda más: a) esperar con calma y decir «Tómate un momento, tú puedes» b) reírse de ella?", "a", "Cuida la confianza y el trabajo en equipo.")],
    [
        E("¿Una retroalimentación debe incluir algo que funcionó?", "Sí", "Reconoce lo logrado."),
        E("¿Los roles se pueden cambiar para que todos practiquen?", "Sí", "Así todos aprenden."),
        E("¿Reconocer lo que hago bien ayuda a confiar en mí?", "Sí", "Fortalece la confianza."),
    ],
    ("Ensaya y retroalimenta con un equipo. Reúne a dos personas de tu casa (si no es posible, hazlo con una sola). Elige el personaje de Dora, Beto o Nina y actúalo durante dos minutos con voz y gesto. Una persona observa con esta pauta: ¿mantuvo el personaje?, ¿voz coherente?, ¿gesto coherente?, ¿escuchó a su pareja de escena? Después te dice una cosa que funcionó y una sugerencia. Escribe ambas y qué probarás en el próximo ensayo.",
     "Funcionó: tu voz tranquila mostró que Dora es cuidadosa. Sugerencia: mira a Gabo cuando le respondes. Próximo ensayo: miraré a Gabo al responder.",
     ["actúa con voz y gesto coherentes", "recibe una retroalimentación con algo que funcionó y una sugerencia", "elige qué probar en el próximo ensayo"], ["notas escritas del ensayo y la retroalimentación"], ["retroalimentación sin evidencia", "burlas"],
     "Si te dijeron solo «estuvo bien», pide un ejemplo de lo que funcionó."),
    "Da una retroalimentación con dos partes a alguien de tu casa que te cuente algo.",
    "Escribe una pauta de cuatro criterios para observar el ensayo de otra escena.",
)

# ================================================================ OA 29 · clase 5
reg(
    OA29, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para ver la escena. Muévete en un espacio libre y seguro.",
    "Aprenderé a mantener el personaje cuando cambia una condición de la escena, como el lugar, la emoción o la persona con quien habla. Sirve para actuar con flexibilidad y seguir siendo coherente.",
    ["Sé caracterizar, responder en personaje y retroalimentar en equipo.", "Sé que el rasgo y la intención guían al personaje."],
    [
        "Un personaje conserva su manera de ser aunque la situación cambie. Lo que cambia es cómo lo muestra. Una condición diferente puede ser el lugar (una biblioteca silenciosa), la emoción (estar nerviosa) o la persona con quien habla (un niño pequeño o una autoridad). El rasgo y la intención siguen igual; se ajustan el volumen, el ritmo, las palabras y los gestos.",
        "Por ejemplo, Dora es cuidadosa y quiere explicar bien. En una biblioteca silenciosa baja el volumen, pero sigue acomodando sus materiales con cuidado. Si está nerviosa, habla algo más rápido y respira hondo, pero sigue preparándose. Si habla con un niño pequeño, usa palabras más simples y gestos más amplios, sin dejar de ser clara.",
        "Para transferir bien nos preguntamos: ¿qué cambió?, ¿qué se mantiene?, ¿cómo lo muestro ahora? Esta idea sirve para actuar y también para la vida: podemos adaptarnos a distintas situaciones sin dejar de ser nosotros.",
    ],
    [("condición", "circunstancia que cambia en la escena, como el lugar o la emoción"), ("transferir", "usar lo aprendido en una situación nueva"), ("adaptar", "ajustar algo a una situación distinta"), ("mantener", "seguir igual"), ("coherente", "que concuerda con lo anterior")],
    [
        ("Ajustar al lugar", "Dora debe explicar su trabajo en una biblioteca donde hay que hablar bajito. ¿Qué cambia y qué se mantiene: a) cambia el volumen, se mantiene su cuidado b) cambia su manera de ser, se mantiene el volumen?", ["Pienso en lo que cambia con el lugar.", "El volumen cambia; su manera de ser no.", "La a lo describe."], "a."),
        ("Ajustar a la persona", "Dora explica la feria a un niño de cinco años. ¿Qué es mejor: a) palabras simples, voz amable y gestos claros b) palabras técnicas y tono serio?", ["Pienso en quién escucha.", "Un niño pequeño necesita palabras simples.", "La a las usa."], "a."),
    ],
    [("Cambiar el rasgo cuando cambia el lugar, como volverse descuidado.", "Se confunde adaptarse con ser otro personaje.", "Mantén el rasgo y cambia solo cómo lo muestras."), ("Actuar igual en todas las situaciones.", "Se olvida la condición nueva.", "Pregúntate qué cambió y ajusta voz, ritmo o palabras.")],
    [
        E("Si cambia el lugar a una biblioteca, ¿qué ajusta Dora primero: el volumen o su nombre?", "El volumen", "Debe hablar bajito."),
        E("¿El rasgo del personaje cambia cuando cambia el lugar?", "No", "El rasgo se mantiene siempre."),
        E("¿Transferir es usar lo aprendido en una situación nueva?", "Sí", "Eso significa transferir."),
    ],
    [
        E("¿Qué se mantiene cuando cambia la condición: el rasgo y la intención o la voz exacta?", "El rasgo y la intención", "Son lo que define al personaje."),
        E("Beto, que es organizado, ahora está en un tren muy ruidoso. ¿Qué ajusta: a) habla más fuerte y con frases cortas b) deja de organizar?", "a", "Se adapta al ruido sin cambiar su rasgo."),
        E("Dora está nerviosa y habla más rápido. ¿Sigue siendo cuidadosa si respira hondo y revisa sus notas?", "Sí", "Mantiene su cuidado."),
    ],
    [
        E("Nina, curiosa, está en un museo con la regla de no tocar. ¿Qué hace: a) mira de cerca y pregunta al guía b) toca todo?", "a", "Mantiene su curiosidad respetando la regla."),
        E("Ordena para adaptar un personaje: a) decidir cómo mostrarlo ahora, b) ver qué cambió, c) reconocer qué se mantiene. Escribe las letras.", "b, c, a", "Se identifica el cambio, lo que sigue igual y luego se decide."),
        E("Beto, impaciente, espera en una fila larga. Para mostrar su rasgo sin molestar, ¿qué gesto es mejor: a) mirar el reloj y suspirar bajito b) empujar a las personas?", "a", "Muestra impaciencia con respeto y seguridad."),
    ],
    [
        E("Dos actrices hacen de Dora nerviosa. La primera tartamudea exageradamente para dar risa. La segunda respira hondo, habla algo más rápido y revisa sus notas. ¿Cuál mantiene mejor el personaje?", "La segunda", "No hace caricatura y mantiene su cuidado."),
        E("¿Por qué conviene preguntarse qué cambió y qué se mantiene?", "Para adaptar sin dejar de ser coherente", "Ayuda a actuar con sentido."),
    ],
    [
        E("Escena nueva: Dora ahora es la presentadora del curso ante el colegio completo. Debe hablar fuerte y claro. ¿Qué ajuste es adecuado: a) proyectar la voz y mantener el cuidado b) hablar bajito como en la biblioteca?", "a", "Se ajusta al escenario sin cambiar su rasgo."),
        E("Un grupo decide que Beto, ahora en un parque, ya no es organizado. ¿Qué error cometió el grupo?", "Cambió el rasgo del personaje", "Solo debían cambiar cómo lo muestra."),
    ],
    [E("Debes actuar a Nina, curiosa, ahora con mucho sueño por la tarde. ¿Qué elección es coherente: a) bosteza pero igual se acerca a mirar la caja, con voz lenta b) corre y grita alegre?", "a", "Cambia la energía, mantiene la curiosidad.")],
    [
        E("¿Un personaje mantiene su rasgo aunque cambie la situación?", "Sí", "Solo cambia cómo lo muestra."),
        E("¿Adaptar es ajustar a una situación distinta?", "Sí", "Se cambian voz, ritmo o palabras."),
        E("¿Reconocer lo que cambió y lo que se mantiene ayuda a actuar mejor?", "Sí", "Orienta las decisiones."),
    ],
    ("Transfiere tu personaje a una condición nueva. Elige a Dora, Beto o Nina y una condición: a) está en una biblioteca silenciosa, b) está nerviosa, o c) habla con un niño de cinco años. Escribe: 1) qué cambia, 2) qué se mantiene, 3) cómo lo muestras con voz y gesto. Actúalo durante un minuto frente a una persona de tu casa y pídele que diga si reconoció al mismo personaje. Anota su respuesta.",
     "Dora en la biblioteca. Cambia: el volumen, que baja. Se mantiene: su cuidado y su intención de explicar bien. Lo muestro con voz suave, ritmo pausado y manos que acomodan las cartulinas sin ruido. La persona dijo: reconocí que era la misma Dora.",
     ["dice qué cambia", "dice qué se mantiene", "muestra el personaje con voz y gesto coherentes", "registra la opinión de quien observó"], ["ficha escrita y actuación frente a otra persona"], ["cambiar el rasgo", "no ajustar la voz a la condición"],
     "Si no reconocieron al personaje, revisa qué rasgo y qué gesto clave mantener."),
    "Actúa un personaje en dos condiciones distintas y compara qué cambió.",
    "Escribe un diálogo de cuatro líneas en que un personaje mantiene su rasgo en una situación nueva.",
)
