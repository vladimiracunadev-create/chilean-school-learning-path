"""Cuaderno del estudiante, 6.º básico Lenguaje y Comunicación: OA 27 (dialogar para compartir ideas y buscar acuerdos)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA27 = "LE06 OA 27"
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
D_CONV = ("Tema: elegir una actividad de convivencia para el curso. Ana: «Propongo una convivencia con juegos en el patio.» "
          "Bruno: «Buena idea. Ayer vi un partido buenísimo.» Ana: «Volvamos al tema: ¿qué juegos podríamos hacer?» Carla: «Carreras de sacos y búsqueda del tesoro.»")
D_HUERTO = ("Tema: qué plantar en el huerto del colegio. Sofía: «Necesitamos decidir qué plantar.» Mateo: «Podríamos plantar lechugas, porque crecen rápido.» "
            "Lía: «Mi gato se escapó ayer.» Sofía: «Lía, ¿qué verduras te gustaría plantar a ti?»")

reg(
    OA27, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer los diálogos a dos voces.",
    "Aprenderé a mantener el foco en un tema cuando dialogo con otras personas. Sirve para que una conversación en grupo avance y lleguemos a ideas claras en lugar de dar vueltas.",
    ["Sé conversar por turnos.", "Sé identificar de qué trata una conversación."],
    [
        "Dialogar es conversar entre dos o más personas para compartir ideas y, muchas veces, llegar a acuerdos. Para que un diálogo funcione, todos necesitan hablar del mismo tema. Mantener el foco significa que cada intervención se relaciona con el tema que se está tratando. Si el tema es elegir una actividad de convivencia, un comentario sobre un partido de ayer se sale del foco, aunque sea interesante.",
        "Cuando alguien se aleja del tema, podemos ayudar a volver con frases amables como «volvamos al tema», «eso lo vemos después, ahora estamos con…» o con una pregunta que lleve de regreso: «¿qué juegos podríamos hacer?». No se trata de callar a la persona, sino de cuidar el tiempo y lo que el grupo necesita decidir.",
        "También hay comentarios que parecen salirse, pero sí ayudan: un ejemplo, una experiencia o un dato relacionado con el tema mantienen el foco. Para decidir, pregúntate: ¿mi comentario ayuda a responder lo que estamos tratando? Si la respuesta es sí, sigues en el foco.",
    ],
    [("dialogar", "conversar entre dos o más personas para compartir ideas"), ("foco", "el tema del que se está hablando"), ("intervención", "cada vez que alguien habla en una conversación"), ("tema", "asunto del que trata una conversación"), ("acuerdo", "decisión que aceptan las personas que dialogan")],
    [
        ("Detectar quién se aleja", "Tema: cómo cuidar el patio. Pedro: «Pongamos más basureros.» Rosa: «Y carteles para recordar botar la basura.» Tito: «Me dieron entradas para un concierto.» ¿Quién se sale del foco?", ["Busco el tema: cuidar el patio.", "Pedro y Rosa proponen formas de cuidar el patio.", "Tito habla de un concierto."], "Tito."),
        ("Volver al tema", "En ese diálogo, ¿qué frase amable puede decir Rosa para volver al tema?", ["Debe reconocer lo dicho y retomar el tema.", "Una frase posible: «Qué bueno, pero ahora volvamos a cómo cuidar el patio».", "No es un reto: es una invitación."], "«Volvamos a cómo cuidar el patio».")
    ],
    [("Responder al compañero con un tema distinto, pensando que lo propio es más importante.", "Se confunde ser escuchado con cambiar el tema.", "Si es importante, anótalo para después: «Eso lo vemos luego»."), ("Retar con enojo a quien se aleja del tema.", "Se piensa que corregir es lo mismo que molestar.", "Usa una frase amable: «Volvamos al tema, por favor».")],
    [
        E(f"{D_CONV} ¿Cuál es el tema del diálogo: a) elegir una actividad de convivencia para el curso b) un partido de ayer?", "a", "Ana lo plantea al inicio y los demás proponen juegos."),
        E(f"{D_CONV} ¿Quién se aleja del tema?", "Bruno", "Habla de un partido de ayer en lugar de la convivencia."),
        E(f"{D_CONV} ¿Qué frase usa Ana para volver al tema?", "Volvamos al tema", "Es la frase con que retoma lo que se trataba."),
    ],
    [
        E(f"{D_HUERTO} ¿Qué intervención no mantiene el foco?", "La de Lía sobre su gato", "No tiene relación con qué plantar."),
        E(f"{D_HUERTO} ¿Qué hace Sofía con su última pregunta: a) lleva a Lía de vuelta al tema b) cambia el tema?", "a", "Le pregunta qué verduras plantar, que es el tema."),
        E("Tema: elegir el color de un mural. Pedro dice: «Yo propongo azul, como el mar.» ¿Qué respuesta mantiene el foco: a) «Yo prefiero verde, como el bosque.» b) «Mañana hay prueba.»", "a", "Responde sobre el color del mural."),
    ],
    [
        E("Tema: cómo cuidar el patio. Alguien empieza a hablar de fútbol. ¿Qué frase ayuda a volver: a) «Volvamos a cómo cuidar el patio.» b) «Yo también quería hablar de fútbol.»", "a", "Retoma el tema sin ofender."),
        arith("Un diálogo sobre un mural tiene 8 intervenciones en total. Seis hablan del mural y las demás de otros temas. ¿Cuántas intervenciones se salen del foco?", "8-6", "Se restan las que sí hablan del mural."),
        E("Tema: reglas para la biblioteca del curso. Luis: «Podemos prestar los libros por una semana.» Ema: «El año pasado, con una semana alcanzábamos a leerlos.» ¿Ema mantiene el foco? Responde sí o no.", "Sí", "Aporta una experiencia relacionada con el plazo de préstamo."),
    ],
    [
        E("Un compañero dice: «Mantener el foco significa no dar una opinión distinta». ¿Es correcto? Responde sí o no.", "No", "Se puede opinar distinto; lo importante es hablar del mismo tema."),
        E("Tema: salida a terreno. Alguien interrumpe: «Hablando de comida, ¿y la fiesta?». ¿Qué respuesta es mejor: a) «Anotémoslo para después; ahora terminemos la salida a terreno.» b) «Sí, hablemos de la fiesta.»", "a", "Reconoce la idea y protege el tema actual."),
    ],
    [
        E("Tema: elegir un juego para el recreo. Intervenciones: 1) «Podemos jugar a la pinta.» 2) «Mi tío tiene un perro.» 3) «También podemos jugar a las escondidas.» 4) «Ayer llovió mucho.» 5) «Mejor un juego que todos conozcan.» ¿Cuántas intervenciones mantienen el foco?", "3", "Son la 1, la 3 y la 5."),
        E("Si dos amigos dialogan sobre qué libro leer y uno cuenta cómo le fue de vacaciones, ¿qué conviene hacer: a) retomar el tema con una pregunta sobre los libros b) callar todo el resto del diálogo?", "a", "Una pregunta amable lleva de vuelta al foco."),
    ],
    [E("Tu curso conversa para elegir el lugar de la salida de fin de año. Una compañera comenta que le encantan los helados y otro dice que el museo tiene una exhibición de dinosaurios. ¿Quién mantiene el foco?", "El que habla del museo", "Sugiere un posible lugar para la salida.")],
    [
        E("¿Cómo se llama el tema del que se habla en un diálogo?", "Foco", "Es lo que todos deben tener presente."),
        E("¿Sirve decir «volvamos al tema» para retomarlo? Responde sí o no.", "Sí", "Es una frase respetuosa para regresar."),
        E("¿Un ejemplo relacionado con el tema mantiene el foco? Responde sí o no.", "Sí", "Aporta a lo que se está tratando."),
    ],
    ("Lee este diálogo: «Tema: cómo ahorrar agua en la escuela. Valeria: Podemos cerrar bien las llaves. Hugo: Anoche vi una película de piratas. Valeria: Cierto, pero volvamos al ahorro de agua. Hugo: Entonces podemos avisar a los de cuarto básico con un cartel». Responde por escrito: 1) ¿quién se sale del tema?, 2) ¿qué frase usa Valeria para volver?, 3) escribe una intervención nueva que mantenga el foco.",
     "1) Hugo. 2) «Cierto, pero volvamos al ahorro de agua». 3) «Podemos regar las plantas con el agua que sobra del lavado».",
     ["identifica a quien se sale del tema", "reconoce la frase para retomar", "su intervención nueva habla del ahorro de agua"], ["tres respuestas escritas"], ["decir que nadie se sale del tema", "escribir una intervención sobre otro tema"],
     "Si dudas, pregúntate: ¿esta frase ayuda a responder el tema del diálogo?"),
    "Escribe una frase amable para volver al tema si en una reunión sobre el cumpleaños del curso alguien habla de tareas.",
    "En una conversación familiar, fíjate cuántas veces cambia el tema y cómo vuelven a él.",
)

# ================================================================ OA 27 · clase 2
D_FERIA = ("Tema: qué presentar en la feria de ciencias. Marco: «Podemos hacer una maqueta del sistema solar.» Elisa: «Y además podríamos agregar una tarjeta con un dato de cada planeta.» "
           "Marco: «Buena idea.» Elisa: «¿Qué te parece si usamos pelotas de distintos tamaños?»")
reg(
    OA27, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para dialogar a dos voces.",
    "Aprenderé a complementar las ideas de otra persona y a ofrecer sugerencias en un diálogo. Sirve para que entre todos mejoremos las ideas y decidamos mejor.",
    ["Sé mantener el foco en un diálogo.", "Sé dar una opinión con una razón."],
    [
        "Complementar la idea de otra persona es agregar algo que la mejora o la hace más completa, sin cambiarla por otra. Se hace con expresiones como «además», «y también», «a eso se puede sumar» o «lo que dices me hace pensar en…». Complementar no es repetir lo que ya se dijo ni contradecir; es construir sobre la idea del otro.",
        "Una sugerencia es una propuesta para mejorar algo o decidir un camino. Se presenta con frases amables como «podríamos», «¿qué te parece si…?» o «una sugerencia sería…». Una sugerencia no es una orden: da la opción de aceptarla, modificarla o rechazarla. Compara «Hagan carteles» con «¿Qué te parece si hacemos carteles?»: la segunda invita al diálogo.",
        "Para complementar bien, escucha primero y piensa qué falta o qué podría mejorar la idea. Para sugerir bien, explica brevemente para qué sirve tu sugerencia. Así tu aporte sirve al tema y la otra persona entiende por qué lo propones.",
    ],
    [("complementar", "agregar algo que mejora o completa la idea de otro"), ("sugerencia", "propuesta amable para mejorar o decidir"), ("además", "palabra para sumar una idea a otra"), ("aporte", "idea o dato que ayuda al grupo"), ("orden", "mandato que no da opción de elegir")],
    [
        ("Complementar", "Mara dice: «Hagamos carteles para cuidar el patio». Nico responde: «Y además podemos pegarlos cerca de los basureros». ¿Qué hace Nico con la idea de Mara?", ["Reviso si cambia la idea o la mejora.", "Nico suma un lugar para los carteles.", "La completa."], "La complementa: agrega dónde ubicar los carteles."),
        ("Convertir una orden en sugerencia", "Cambia «Cierren las llaves» por una sugerencia amable.", ["Quito el mandato.", "Uso «podríamos» o «¿qué te parece si…?».", "Agrego la razón si puedo."], "«¿Qué te parece si cerramos bien las llaves para ahorrar agua?»"),
    ],
    [("Repetir lo que dijo el otro y creer que complementas.", "Se confunde acompañar con aportar.", "Agrega algo nuevo: un lugar, una razón, un ejemplo."), ("Dar una sugerencia como orden.", "Se piensa que sugerir es mandar.", "Usa «podríamos» o «¿qué te parece si…?».")],
    [
        E(f"{D_FERIA} ¿Qué palabra usa Elisa para sumar su idea a la de Marco?", "Además", "Aparece al comienzo de su primera intervención."),
        E(f"{D_FERIA} ¿Qué frase de Elisa es una sugerencia en forma de pregunta?", "¿Qué te parece si usamos pelotas de distintos tamaños?", "Propone algo sin imponerlo."),
        E("Mara dice: «Hagamos carteles». Nico responde: «Hagamos carteles». ¿Nico complementa o solo repite?", "Solo repite", "No agrega nada nuevo."),
    ],
    [
        E("Camila dice: «Podemos reciclar papel en la sala». ¿Qué respuesta complementa: a) «Y además podemos poner una caja azul para guardarlo» b) «No, mejor no hagamos nada»?", "a", "La a) suma una forma de hacerlo."),
        E("¿Cuál es una sugerencia amable: a) «Hazlo así.» b) «Podríamos hacerlo así, ¿te parece?»", "b", "Da la posibilidad de aceptar o cambiar."),
        E("Tema: festival del curso. Juan propone un baile. Luz dice: «Una sugerencia sería sumar música en vivo con un instrumento». ¿Esa frase es complemento o rechazo?", "Complemento", "Mejora la idea del baile sin eliminarla."),
    ],
    [
        E("Ordena un diálogo: a) «Podemos organizar un campeonato de ajedrez.» b) «Además, podríamos hacer una tabla para anotar los resultados.» c) «¡Buena idea, la tabla ayudará!» Escribe las letras.", "a, b, c", "Primero la idea, luego el complemento y luego la reacción."),
        E("Elige la sugerencia que sirve al tema «cómo cuidar los libros»: a) «Podríamos forrar los libros con plástico transparente» b) «Podríamos jugar a la pinta»", "a", "La a) se relaciona con el tema."),
        arith("Tu curso propone comprar 3 cajas azules para reciclar papel a $2.500 cada una. ¿Cuánto cuestan en total?", "3*2500", "Se multiplica el precio por la cantidad."),
    ],
    [
        E("Rosa dice: «Hagamos una feria de libros». Eli dice: «Mejor no, es muy aburrido». ¿Eli complementa la idea o la rechaza sin aportar?", "La rechaza sin aportar", "No agrega nada ni propone una alternativa."),
        E("Para sugerir bien, ¿qué conviene agregar: la razón o un volumen más fuerte?", "La razón", "Explica para qué sirve tu sugerencia."),
    ],
    [
        E("Leo dice: «Podríamos hacer un afiche». Completa con un complemento que aporte algo nuevo: a) «Sí, un afiche.» b) «Y además podemos poner un código QR» c) «Y además podemos dibujar un animal que represente el mensaje». Elige el que no usa tecnología especial.", "c", "Cualquier curso puede hacerlo con lápices y papel."),
        E("Si Tomás dice «Podríamos grabar un video» y Ana responde «Y también escribir antes un guion corto para que no nos perdamos», ¿Ana mejora la idea? Responde sí o no.", "Sí", "El guion ayuda a que el video salga ordenado."),
    ],
    [E("Tu curso quiere decorar la sala para el aniversario del colegio. Una compañera propone guirnaldas de papel. ¿Qué respuesta complementa: a) «Y podríamos usar colores del uniforme» b) «Mejor hablemos de la tarea»", "a", "Suma una idea sobre los colores de las guirnaldas.")],
    [
        E("¿Qué palabra sirve para sumar una idea: además o nunca?", "Además", "Suma algo a lo dicho."),
        E("¿Una sugerencia es lo mismo que una orden? Responde sí o no.", "No", "La sugerencia permite aceptar o cambiar."),
        E("Al complementar, ¿repites exactamente lo que dijo la otra persona? Responde sí o no.", "No", "Debes agregar algo nuevo."),
    ],
    ("Lee esta idea: «Mi propuesta es hacer una colecta de útiles escolares para el jardín infantil del barrio». Escribe 1) un complemento con «además» o «y también», 2) una sugerencia con «¿qué te parece si…?» y 3) la razón por la que tu sugerencia ayudaría. Si puedes, léelo en voz alta a una persona de tu casa y pregúntale si sonó amable.",
     "Complemento: Y además podemos colocar una caja en la entrada. Sugerencia: ¿Qué te parece si ponemos un cartel? Razón: así todos sabrán qué traer.",
     ["el complemento agrega algo nuevo", "la sugerencia está formulada como propuesta amable", "incluye una razón"], ["tres frases escritas o dichas"], ["repetir la idea", "dar la sugerencia como orden"],
     "Si tu complemento se parece al original, agrega un dato nuevo: un lugar, un material o una razón."),
    "Escribe una sugerencia amable para mejorar una idea como «hacer un mural en el pasillo».",
    "Pide a una persona de tu casa su idea para una salida y complétala con un aporte tuyo.",
)

# ================================================================ OA 27 · clase 3
D_TURNOS = ("Tema: organizar un campeonato de ajedrez. Pía explica: «Propongo jugar en parejas y…» Gonzalo la interrumpe: «No, mejor solos.» Pía lo mira y se queda callada.")
reg(
    OA27, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para practicar los turnos.",
    "Aprenderé a aceptar sugerencias y a hacer comentarios en el momento adecuado. Sirve para que todos puedan hablar y sentirse escuchados.",
    ["Sé complementar ideas y ofrecer sugerencias.", "Sé esperar mi turno para hablar."],
    [
        "Aceptar una sugerencia es reconocer que sirve y usarla, completa o con algunos cambios. Se puede decir: «me parece bien, la voy a incorporar», «buena idea, pero la cambiaría un poco» o «gracias, no lo había pensado». Aceptar no significa estar de acuerdo con todo: si algo no sirve, se puede explicar por qué con respeto, sin desprestigiar a quien sugirió.",
        "Hacer comentarios en los momentos adecuados es otra norma del diálogo. El momento adecuado es cuando la otra persona terminó de hablar o hace una pausa. Interrumpir corta la idea de quien habla y hace que se sienta poco valorado. Si necesitas agregar algo urgente, puedes levantar la mano o decir «¿puedo agregar algo?» y esperar la señal.",
        "También son momentos adecuados las pausas naturales, el cierre de una idea y cuando quien modera da la palabra. Los comentarios sirven mejor si son breves y se relacionan con lo recién dicho. Así el grupo mantiene el hilo y todos pueden participar.",
    ],
    [("aceptar", "reconocer que algo sirve y usarlo"), ("interrumpir", "cortar lo que otra persona está diciendo"), ("turno", "momento en que a cada uno le toca hablar"), ("moderador", "persona que da la palabra"), ("incorporar", "agregar algo a lo que ya se tiene")],
    [
        ("Elegir el momento", "Pía todavía está explicando su plan. Gonzalo tiene una idea. ¿Cuándo debe decirla?", ["Veo que Pía aún habla.", "Esperar a que termine o pedir la palabra.", "Así no corta su idea."], "Cuando Pía termine o cuando él pida la palabra con «¿puedo agregar algo?»."),
        ("Aceptar con cambios", "Luis sugiere hacer un cartel con letras grandes. Tú piensas que debe ser más pequeño por el espacio. ¿Cómo aceptas parte de su sugerencia?", ["Reconozco lo bueno: el cartel.", "Propongo un cambio: más pequeño por el espacio.", "Lo digo con respeto."], "«Me parece bien el cartel; lo haría un poco más pequeño por el espacio».")
    ],
    [("Interrumpir porque la idea propia es importante.", "Se cree que es peor olvidar que esperar.", "Anota tu idea y espera la pausa o pide la palabra."), ("Rechazar una sugerencia diciendo «eso no sirve».", "Se piensa que ser directo es ser claro.", "Explica con respeto: «Gracias, pero creo que no calza porque…».")],
    [
        E(f"{D_TURNOS} ¿Quién interrumpe a quién?", "Gonzalo interrumpe a Pía", "Habla mientras ella aún explica."),
        E("¿Cuál es una buena forma de pedir la palabra: a) «¿Puedo agregar algo?» b) hablar más fuerte que los demás?", "a", "Pide el turno sin cortar a nadie."),
        E("Ana sugiere un afiche. Tomás responde: «Gracias, buena idea, la incorporo». ¿Tomás acepta o rechaza la sugerencia?", "Acepta", "Reconoce que sirve y la usa."),
    ],
    [
        E("¿Cuál es un momento adecuado para comentar: a) cuando otra persona termina su idea b) en medio de una explicación?", "a", "Así no se corta lo que dice."),
        E("Mara sugiere dividir el trabajo en tres grupos. Sofi responde: «Me parece bien, pero lo haría en cuatro grupos porque somos veinte». ¿Qué hace Sofi: acepta con cambios o rechaza sin explicar?", "Acepta con cambios", "Reconoce la idea y propone una modificación con razón."),
        E("¿Qué frase rechaza con respeto una sugerencia: a) «No sirve para nada.» b) «Gracias, pero creo que no calza porque nos falta tiempo.»", "b", "Da la razón y agradece."),
    ],
    [
        E("Ordena: a) Gonzalo levanta la mano. b) Pía termina su explicación. c) Pía le da la palabra y Gonzalo comenta. Escribe las letras.", "b, a, c", "Primero termina quien habla; luego se pide la palabra y se comenta."),
        arith("Seis estudiantes hablan en una reunión del curso y dos de ellos interrumpen a otros. ¿Cuántos de los seis no interrumpen y esperan su turno?", "6-2", "Seis menos los dos que interrumpen."),
        E("Camilo sugiere: «Hagamos una lista de materiales». ¿Qué comentario es adecuado inmediatamente después: a) «Sí, y agreguemos las cantidades.» b) «Mi perro se llama Rocky.»", "a", "Se relaciona con la sugerencia recién dicha."),
    ],
    [
        E("Un estudiante piensa: «Si interrumpo es porque mi idea es más urgente». ¿Está bien? Responde sí o no.", "No", "Incluso una idea urgente se pide con respeto, esperando una pausa o el permiso."),
        E("Tomás acepta una sugerencia de Eva, pero la cambia un poco. ¿Sigue siendo aceptar? Responde sí o no.", "Sí", "Aceptar con ajustes también reconoce el aporte."),
    ],
    [
        E("Si alguien explica cómo hacer un cartel y tú notas un error de ortografía en su ejemplo, ¿qué haces: a) esperas su pausa y lo comentas con amabilidad b) lo corriges en voz alta cortándolo?", "a", "Comentas en el momento adecuado y con respeto."),
        E("Elige la mejor intervención de cierre al aceptar: a) «Gracias, Tito, tu sugerencia mejora el plan.» b) «Ya.»", "a", "Reconoce y agradece el aporte."),
    ],
    [E("En una reunión del curso, la profesora pide que cada uno diga una idea para el diario mural. Mientras Eli habla, Joaquín cree tener una mejor idea. ¿Qué debería hacer: a) esperar su turno b) interrumpir con voz alta?", "a", "Respeta el turno de Eli.")],
    [
        E("¿Cómo se llama el momento en que a cada persona le toca hablar?", "Turno", "Evita que se hable todos a la vez."),
        E("¿Se puede aceptar una sugerencia y cambiarla un poco? Responde sí o no.", "Sí", "Es una forma de incorporarla."),
        E("¿Qué frase pide la palabra: «¿puedo agregar algo?» o «cállate»?", "¿Puedo agregar algo?", "Es respetuosa y clara."),
    ],
    ("Lee este diálogo y reescribe las intervenciones que no respetan el turno o rechazan mal: «Rosa: Podemos hacer un mural con cajas recicladas. Felipe (interrumpiendo): Eso no sirve, mejor un video. Rosa: Pero… Felipe: Ya hablé». Escribe cómo debería decirlo Felipe para 1) esperar su turno y 2) rechazar o modificar la idea con respeto.",
     "«Rosa, ¿puedo agregar algo? Me parece buena idea el mural, pero creo que un video llegaría a más gente. ¿Qué te parece si hacemos ambos?»",
     ["Felipe espera o pide la palabra", "reconoce algo de la idea de Rosa", "explica con razón su cambio"], ["dos frases reescritas"], ["mantener la interrupción", "rechazar sin razón"],
     "Revisa: ¿pidió la palabra?, ¿reconoció la idea?, ¿dio una razón?"),
    "Escribe tres frases para pedir la palabra y tres para aceptar una sugerencia con respeto.",
    "Cuenta en una conversación familiar cuántas veces se interrumpe y cómo se pide la palabra.",
)

# ================================================================ OA 27 · clase 4
D_ACUERDO = ("Tema: ¿mural o campeonato para el aniversario del curso? Ema: «Prefiero el mural, porque queda para siempre.» "
             "Raúl: «Entiendo tu idea, pero yo pienso que el campeonato nos reúne a todos.» Ema: «Eso es una tontería.»")
reg(
    OA27, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para practicar frases de acuerdo y desacuerdo.",
    "Aprenderé a mostrar acuerdo o desacuerdo con respeto en un diálogo. Sirve para opinar distinto sin ofender a nadie y seguir buscando soluciones juntos.",
    ["Sé aceptar sugerencias y esperar mi turno.", "Sé dar razones para mis opiniones."],
    [
        "En un diálogo es normal estar de acuerdo con algunas ideas y en desacuerdo con otras. Mostrar acuerdo es decir que compartes la idea y por qué: «Estoy de acuerdo con Raúl porque el campeonato reúne a todos». Mostrar desacuerdo es decir que piensas distinto, explicando tu razón: «Entiendo tu idea, pero yo pienso que el mural dura más».",
        "El respeto consiste en criticar la idea y no a la persona. Decir «tu idea no resuelve el problema del tiempo» critica la idea. Decir «eres tonto» ataca a la persona y termina el diálogo. Para un desacuerdo respetuoso sirve una estructura de tres partes: reconocer algo de la idea del otro, decir tu postura distinta y dar una razón.",
        "Los marcadores de acuerdo (estoy de acuerdo, coincido, tienes razón en…) y de desacuerdo (no coincido, entiendo, pero…, veo otra posibilidad) ayudan a que el otro entienda en qué punto estás. Un buen dialogante puede estar en desacuerdo y, aun así, escuchar, agradecer y seguir buscando una solución.",
    ],
    [("acuerdo", "estar de acuerdo con una idea"), ("desacuerdo", "pensar distinto sobre una idea"), ("respeto", "trato amable que reconoce al otro"), ("postura", "opinión que alguien defiende"), ("coincidir", "pensar lo mismo en algún punto")],
    [
        ("Desacuerdo respetuoso", "Raúl no está de acuerdo con Ema. ¿Cuál frase muestra desacuerdo con respeto: a) «Entiendo tu idea, pero yo pienso que el campeonato nos reúne a todos.» b) «Eso es una tontería.»", ["Reviso si critica la idea o a la persona.", "La a) reconoce la idea de Ema y da una razón.", "La b) ofende."], "a)"),
        ("Acuerdo con razón", "Lía está de acuerdo con el mural. ¿Cómo lo dice con razón?", ["Digo que estoy de acuerdo.", "Agrego el porqué.", "Uso «porque»."], "«Estoy de acuerdo con el mural porque queda como recuerdo para todo el año»."),
    ],
    [("Decir «no» sin explicar el desacuerdo.", "Se cree que basta rechazar la idea.", "Agrega «porque» y una razón."), ("Atacar a la persona en lugar de la idea.", "Se confunde desacuerdo con pelea.", "Habla de la idea: «esta propuesta no resuelve…».")],
    [
        E(f"{D_ACUERDO} ¿Qué frase de Raúl muestra desacuerdo con respeto?", "Entiendo tu idea, pero yo pienso que el campeonato nos reúne a todos", "Reconoce la idea de Ema y da su razón."),
        E(f"{D_ACUERDO} ¿Qué intervención no es respetuosa: la de Ema final o la de Raúl?", "La de Ema final", "Llama «tontería» a la idea de Raúl, ofendiendo."),
        E("«Estoy de acuerdo» muestra... ¿acuerdo o desacuerdo?", "Acuerdo", "Expresa que compartes la idea."),
    ],
    [
        E("¿Cuál critica la idea y no a la persona: a) «Tu propuesta no resuelve el problema del tiempo.» b) «Eres tonto por proponerlo.»", "a", "Critica la propuesta, no a quien la dijo."),
        E("Elige el marcador de desacuerdo: a) «Coincido contigo.» b) «No coincido, porque falta presupuesto.»", "b", "Marca una postura distinta y da razón."),
        E("Tema: salida a terreno. Mara: «Prefiero el museo». Tomás: «Tienes razón en que aprenderíamos, pero el parque es gratis». ¿Tomás muestra acuerdo parcial con desacuerdo? Responde sí o no.", "Sí", "Reconoce algo y propone otra opción por una razón."),
    ],
    [
        E("Ordena un desacuerdo respetuoso: a) «...porque nos falta tiempo.» b) «Entiendo tu idea,...» c) «...pero yo pienso que no alcanzamos a hacerlo.» Escribe las letras.", "b, c, a", "Primero se reconoce, luego se dice la postura y al final la razón."),
        arith("En un diálogo hay seis intervenciones y cuatro muestran desacuerdo con respeto. Las demás ofenden. ¿Cuántas ofenden?", "6-4", "Del total se restan las respetuosas."),
        E("Lía: «Prefiero el mural». Raúl: «Coincido en que queda para siempre, aunque el campeonato une más». ¿Raúl está en desacuerdo total? Responde sí o no.", "No", "Coincide en un punto y propone otra opción."),
    ],
    [
        E("Un estudiante dice: «Si no coincido, debo callarme». ¿Está bien? Responde sí o no.", "No", "Se puede opinar distinto con respeto."),
        E("Ana comenta: «Tu idea es mala». Beto comenta: «No coincido con tu idea porque necesitaría más materiales». ¿Cuál es más constructivo?", "El de Beto", "Da una razón sobre la idea."),
    ],
    [
        E("Frase: «No, eso no». ¿Qué le falta para ser un buen desacuerdo: a) una razón y un tono respetuoso b) más volumen?", "a", "Debe explicar por qué."),
        E("Si sientes que una idea tiene algo bueno, pero no todo, ¿qué conviene decir: a) «Coincido en… pero veo otra posibilidad» b) «Nada de eso sirve»?", "a", "Reconoce lo bueno y propone otra opción."),
    ],
    [E("En una reunión de curso, Pía propone cancelar el recreo para hacer un ensayo y tú no estás de acuerdo. ¿Qué frase dices: a) «Entiendo que quieras ensayar, pero necesitamos descansar; ¿ensayamos después del almuerzo?» b) «¡Qué mala idea!»", "a", "Reconoce la intención, da razón y propone una alternativa.")],
    [
        E("Al discrepar con respeto, ¿sobre qué centras tu crítica: sobre la propuesta o sobre quien la dijo?", "Sobre la propuesta", "Se mantiene el respeto hacia la persona."),
        E("¿Hay que dar una razón al mostrar desacuerdo? Responde sí o no.", "Sí", "Así el otro entiende tu postura."),
        E("¿Sirve «entiendo, pero…» para mostrar desacuerdo con respeto? Responde sí o no.", "Sí", "Reconoce al otro antes de dar tu postura."),
    ],
    ("Lee estas dos posturas: «Postura A: Para el recreo largo conviene jugar fútbol porque todos conocemos las reglas. Postura B: Conviene hacer juegos variados porque no todos quieren jugar fútbol». Escribe 1) una frase de acuerdo con una de ellas con razón y 2) una de desacuerdo respetuoso con la otra, usando «entiendo… pero…».",
     "1) Estoy de acuerdo con B porque a algunos no les gusta el fútbol. 2) Entiendo la postura A, pero muchos prefieren otros juegos.",
     ["muestra acuerdo con una razón", "muestra desacuerdo sin atacar a la persona", "usa «entiendo… pero…»"], ["dos frases escritas o dichas"], ["ofender", "no dar razón"],
     "Si no usaste «porque», agrega la razón al final."),
    "Escribe dos frases de desacuerdo respetuoso sobre la idea de «hacer la tarea en grupo todas las semanas».",
    "Observa una conversación y anota una frase de acuerdo y una de desacuerdo, y si fueron respetuosas.",
)

# ================================================================ OA 27 · clase 5
reg(
    OA27, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para practicar con un tema de conversación.",
    "Aprenderé a fundamentar mi postura con razones, ejemplos y datos al dialogar. Sirve para convencer con argumentos y no solo con insistencia.",
    ["Sé mostrar acuerdo y desacuerdo con respeto.", "Sé mantener el foco."],
    [
        "Fundamentar una postura es explicar por qué piensas lo que piensas. Una postura bien fundamentada tiene tres partes: la afirmación (lo que defiendes), la razón (por qué) y, si es posible, un ejemplo o dato que la apoye. Por ejemplo: «El curso debería ir al parque (afirmación), porque es gratis (razón); la entrada al museo cuesta $1.500 por persona (dato)».",
        "No todas las razones sirven igual. Una razón buena se relaciona con el tema, es verdadera y se puede comprobar. «Es mejor el parque porque me gusta» es una razón débil porque habla solo de gustos. «Es mejor el parque porque el curso no gastaría dinero» es más fuerte, porque se puede comprobar con un precio.",
        "Al fundamentar usa conectores como «porque», «ya que», «por ejemplo», «además» y «por lo tanto». Y escucha los argumentos de los demás: una persona que fundamenta bien también reconoce cuando otro tiene una razón mejor, y puede cambiar o ajustar su postura.",
    ],
    [("fundamentar", "dar razones, ejemplos o datos que apoyan una postura"), ("afirmación", "lo que defiendes"), ("razón", "el porqué de lo que defiendes"), ("dato", "información que se puede comprobar"), ("conector", "palabra que une ideas, como «porque»")],
    [
        ("Armar una postura", "Quieres que el curso vaya al parque. Hay un dato: el museo cuesta $1.500 por persona y el parque es gratis. ¿Cómo fundamentas?", ["Afirmación: ir al parque.", "Razón: es gratis.", "Dato: el museo cuesta $1.500."], "«Deberíamos ir al parque porque es gratis; el museo cuesta $1.500 por persona»."),
        ("Elegir la razón más fuerte", "¿Cuál razón es más fuerte para ir al parque: a) «Me gusta» b) «Es gratis y todos pueden ir»?", ["Veo cuál puede comprobarse.", "«Es gratis» se comprueba.", "«Me gusta» es solo un gusto."], "b)"),
    ],
    [("Dar solo un gusto personal como razón.", "Se piensa que la opinión basta.", "Agrega una razón comprobable: un precio, un horario, un ejemplo."), ("Repetir la afirmación varias veces.", "Se confunde insistir con argumentar.", "Cambia la repetición por una razón nueva.")],
    [
        E("En «El curso debería ir al parque porque es gratis», ¿cuál es la razón?", "Es gratis", "Va después de «porque»."),
        E("¿Qué conector introduce una razón: porque o también?", "Porque", "Indica el motivo."),
        E("«Me gusta más» ¿es una razón fuerte o débil para elegir el lugar de la salida?", "Débil", "Solo habla de gustos, no se puede comprobar."),
    ],
    [
        E("Elige la razón mejor fundamentada para llevar un sombrero en la salida: a) «Se ve bien» b) «El sol del mediodía puede quemar la piel»", "b", "La b) se relaciona con la salud y puede comprobarse."),
        arith("La visita al planetario cuesta $2.000 por persona y el curso tiene 28 estudiantes. ¿Cuánto costaría la entrada de todo el curso?", "28*2000", "Se multiplica el precio por la cantidad de estudiantes."),
        E("«Por ejemplo» sirve para introducir... ¿un ejemplo o un desacuerdo?", "Un ejemplo", "Presenta un caso que apoya la idea."),
    ],
    [
        E("Ordena una postura bien fundamentada: a) «...ya que es gratis.» b) «Deberíamos ir al parque...» c) «Por ejemplo, el planetario cobra entrada y el parque no.» Escribe las letras.", "b, a, c", "Primero la afirmación, luego la razón y por último el ejemplo."),
        arith("Ir al planetario cuesta $2.000 de entrada y $900 de transporte por estudiante. ¿Cuánto cuesta en total por estudiante?", "2000+900", "Se suman entrada y transporte."),
        E("Postura: «No conviene salir en invierno sin abrigo». ¿Qué dato la apoya mejor: a) «El pronóstico indica 6 grados en la mañana.» b) «A mí me gusta el verano.»", "a", "Un dato de temperatura se puede comprobar y se relaciona con el tema."),
    ],
    [
        E("Un compañero dice: «Mi idea es la mejor porque lo digo yo». ¿Está fundamentando? Responde sí o no.", "No", "No da razones ni datos."),
        E("Ema defiende ir al parque y Raúl el planetario. Ema dice «es gratis». Raúl dice «aprenderemos sobre las estrellas». ¿Cuál razón se puede comprobar con un precio?", "La de Ema", "Gratis se puede verificar con el costo de entrada."),
    ],
    [
        E("Quieres convencer al curso de usar menos plástico. ¿Qué argumento es mejor: a) «El plástico tarda mucho en descomponerse, por ejemplo, una botella puede quedar en el ambiente por muchos años.» b) «No me gusta el plástico.»", "a", "Da una razón con ejemplo y es comprobable."),
        E("Si otra persona te da una razón mejor que la tuya, ¿qué haces: a) la reconoces y ajustas tu postura b) la ignoras?", "a", "Fundamentar bien incluye escuchar buenos argumentos."),
    ],
    [E("En una reunión de curso se discute si hacer una rifa o una venta de pasteles para juntar $60.000. Tu postura es la venta de pasteles. ¿Qué frase está mejor fundamentada: a) «Prefiero los pasteles porque me gusta el dulce.» b) «Propongo la venta de pasteles ya que se puede hacer sin gastar mucho: harinas y huevos se aportan entre todos.»", "b", "Da una razón práctica y comprobable.")],
    [
        E("En una postura fundamentada, ¿cómo se llama lo que defiendes: afirmación o razón?", "Afirmación", "La razón es el porqué; lo que defiendes es la afirmación."),
        E("¿Una razón buena se relaciona con el tema? Responde sí o no.", "Sí", "Las razones fuera de tema no ayudan."),
        E("¿Se puede fundamentar con un dato? Responde sí o no.", "Sí", "Los datos comprobables fortalecen una postura."),
    ],
    ("Lee este tema: «¿El curso debe hacer la clase de ciencias en el patio o en la sala?». Datos: el curso tiene 28 estudiantes; en el patio hay luz natural y espacio para 30 estudiantes; en la sala hay 20 sillas. Elige una postura y escribe una afirmación, una razón y un dato tomado de lo anterior. Luego di si estarías dispuesto a cambiar tu postura con una razón mejor.",
     "Afirmación: la clase debe ser en el patio. Razón: allí caben todos. Dato: el curso tiene 28 estudiantes y la sala solo 20 sillas.",
     ["tiene afirmación, razón y dato", "el dato está tomado del enunciado", "indica si cambiaría su postura"], ["tres frases escritas"], ["razón basada solo en gusto", "dato inventado"],
     "Si tu razón dice «me gusta», cámbiala por algo comprobable en los datos."),
    "Escribe una postura fundamentada sobre la idea de que el curso recicle el papel.",
    "En una conversación en casa, escucha a quien dé una razón con un dato y anótala.",
)

# ================================================================ OA 27 · clase 6
reg(
    OA27, 6,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para ensayar el diálogo completo.",
    "Aprenderé a buscar acuerdos al dialogar: juntar posturas, hallar puntos comunes, proponer una solución y dejar el acuerdo claro. Sirve para resolver desacuerdos reales y revisar si mi conversación cumplió el objetivo.",
    ["Sé mostrar acuerdo y desacuerdo con respeto.", "Sé fundamentar mi postura."],
    [
        "Buscar un acuerdo es encontrar una decisión que el grupo pueda aceptar. Para lograrlo, primero se escucha cada postura y se identifica qué quiere cada persona y por qué. Luego se buscan puntos en común: lo que todos valoran. Después se proponen soluciones que combinen ideas o se ceda un poco, por ejemplo hacer el campeonato por la mañana y el mural por la tarde.",
        "Cuando hay dos opciones, el grupo puede combinar, turnarse, votar o elegir según un criterio acordado (costo, tiempo, número de participantes). No siempre todos consiguen lo que querían, pero un buen acuerdo es justo y claro. Cuando se llega a una solución, se resume en voz alta: «Entonces acordamos que… y quien se encarga de… es…».",
        "Revisar el acuerdo para su audiencia significa dejarlo escrito de forma que lo entienda quien no estuvo: qué se decidió, quién hace qué y para cuándo. Un acuerdo vago, como «lo vemos después», no resuelve nada. Un acuerdo claro dice qué, quién y cuándo.",
    ],
    [("buscar un acuerdo", "encontrar una decisión que el grupo acepte"), ("punto en común", "algo que todos valoran o quieren"), ("ceder", "dejar un poco lo que uno quería para llegar a un acuerdo"), ("criterio", "regla para decidir, como el costo"), ("resumir", "decir en pocas palabras lo acordado")],
    [
        ("Combinar posturas", "Ema quiere un mural; Raúl, un campeonato. Ambos quieren que el aniversario sea recordado y que participe todo el curso. ¿Qué acuerdo combina ambas ideas?", ["Busco el punto en común: recordar y que participe todo el curso.", "Combino: mural colectivo durante el recreo y mini campeonato de cierre.", "Todos aportan algo."], "Hacer un mural colectivo y cerrar con un mini campeonato."),
        ("Resumir el acuerdo", "Después de acordar, ¿cómo resumes? Faltan tres cosas: qué, quién y cuándo.", ["Digo qué se decidió.", "Digo quién lo hará.", "Digo para cuándo."], "«Acordamos hacer el mural. Ema y Lía traen la cartulina; lo pintamos el viernes»."),
    ],
    [("Seguir defendiendo cada uno su idea sin buscar algo en común.", "Se cree que ceder es perder.", "Pregunta: ¿qué quiere cada uno y qué podemos combinar?"), ("Cerrar con «lo vemos después».", "Se evita decidir.", "Cierra con qué, quién y cuándo.")],
    [
        E("Dos amigos quieren: uno, jugar fútbol; el otro, jugar ajedrez. Ambos quieren estar juntos en el recreo. ¿Cuál es el punto en común: estar juntos en el recreo o el fútbol?", "Estar juntos en el recreo", "Es lo que ambos quieren."),
        E("¿Qué significa ceder un poco: dejar un poco lo que uno quería o discutir más fuerte?", "Dejar un poco lo que uno quería", "Así se facilita el acuerdo."),
        E("«Entonces acordamos que…» sirve para... ¿resumir el acuerdo o cambiar de tema?", "Resumir el acuerdo", "Deja claro qué se decidió."),
    ],
    [
        E("Dos propuestas para juntar dinero: rifa o venta de pasteles. El curso necesita $60.000 y tiene 15 días. ¿Qué acuerdo combina ambas ideas: a) hacer una venta de pasteles la primera semana y una rifa la segunda b) hacer solo lo que quiere el más fuerte?", "a", "Reúne ambas propuestas y reparte el tiempo."),
        E("Para decidir entre dos opciones sin pelear, ¿qué sirve: un criterio acordado, como el costo, o un grito más fuerte?", "Un criterio acordado, como el costo", "Permite decidir con una regla justa."),
        E("¿Qué le falta a este acuerdo: «Lo vemos después»? a) qué, quién y cuándo b) un nombre bonito", "a", "Un acuerdo claro dice qué, quién y cuándo."),
    ],
    [
        E("Ordena el proceso para llegar a un acuerdo: a) proponer una solución que combine ideas b) escuchar cada postura c) resumir lo acordado d) buscar puntos en común. Escribe las letras.", "b, d, a, c", "Se escucha, se buscan coincidencias, se propone y se resume."),
        arith("El curso acordó pintar un mural de 6 metros. Cada uno de los 3 grupos pintará la misma cantidad de metros. ¿Cuántos metros pintará cada grupo?", "6//3", "Se reparte el total en partes iguales."),
        E("Camila quiere salir al patio a las 10:00 y Dani a las 10:30. Acuerdan salir a las 10:15. ¿Qué hicieron: a) ceder ambos un poco b) uno ganó y el otro perdió?", "a", "Ambos movieron su hora para encontrarse."),
    ],
    [
        E("Un estudiante dice: «Un buen acuerdo es cuando yo gano». ¿Es correcto? Responde sí o no.", "No", "Un buen acuerdo es justo para el grupo."),
        E("Acuerdo: «Pintaremos el mural». ¿Qué falta para que quien no asistió lo entienda: quién lo hará y cuándo, o el color del lápiz?", "Quién lo hará y cuándo", "Un acuerdo claro dice qué, quién y cuándo."),
    ],
    [
        E("Dos opciones para el cartel: dibujo grande de Marta o texto grande de Pablo. Ambos quieren que se lea desde lejos. ¿Qué acuerdo sirve: a) texto grande con un dibujo pequeño al lado b) hacer dos carteles iguales?", "a", "Combina lo que valora cada uno y se lee desde lejos."),
        E("Para que un acuerdo sea claro para la audiencia, ¿debe incluir quién se encarga? Responde sí o no.", "Sí", "Sin responsable, nadie sabe quién actúa."),
    ],
    [E("En el taller de teatro, nueve estudiantes votan por tres obras distintas. Acuerdan elegir la que tenga más votos. Salieron 2 votos por la obra A, 4 por la B y 3 por la C. ¿Cuál obra eligen?", "B", "Es la que obtuvo más votos (4).")],
    [
        E("¿Cómo se llama algo que todos quieren en un desacuerdo?", "Punto en común", "Permite construir el acuerdo."),
        E("¿Un buen acuerdo dice qué, quién y cuándo? Responde sí o no.", "Sí", "Así todos saben qué hacer."),
        E("¿Hay que escuchar cada postura antes de proponer un acuerdo? Responde sí o no.", "Sí", "Así se identifican intereses y puntos comunes."),
    ],
    ("Lee este desacuerdo: «Tomás propone que el recreo largo sea de fútbol. Sara prefiere que sea de juegos de mesa. Ambos quieren que todos se diviertan y que nadie quede fuera». Escribe 1) el punto en común, 2) un acuerdo que combine ambas ideas, 3) un resumen con qué, quién y cuándo. Si puedes, léelo en voz alta a una persona de tu casa.",
     "1) Que todos se diviertan. 2) Alternar: lunes y miércoles fútbol; martes y jueves juegos de mesa. 3) Acordamos alternar; Tomás avisa del fútbol y Sara de los juegos de mesa; empieza el lunes.",
     ["identifica el punto en común", "el acuerdo combina las ideas", "el resumen dice qué, quién y cuándo"], ["tres respuestas escritas"], ["ganar uno solo", "resumen sin responsables ni fecha"],
     "Si falta un dato en tu resumen, revisa: ¿qué?, ¿quién?, ¿cuándo?"),
    "Escribe un acuerdo claro para repartir el trabajo de limpiar la sala entre cuatro estudiantes, con qué, quién y cuándo.",
    "Observa un desacuerdo en casa y piensa un acuerdo que combine lo que quería cada persona.",
)
