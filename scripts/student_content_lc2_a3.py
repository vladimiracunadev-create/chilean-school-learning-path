"""Cuaderno del estudiante, 2.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 10 (elementos espirituales, naturales y cósmicos en el contexto familiar y comunitario) y
OA 11 (relación con la naturaleza y actividades productivas).

Criterio de autoría: OA 10 es delicado. Las creencias, los seres y las prácticas espirituales de cada pueblo
las explican sus propias autoridades y su educador/a tradicional; aquí solo se enseña a reconocerlas con
respeto, a distinguir fuente de suposición y a no imitar ritos. Los ejemplos de comunidad son inventados.
No se nombra ningún ser espiritual, rol ritual ni práctica real: todo ejemplo espiritual es inventado y de práctica.
Ningún ejercicio exige creer, practicar ni probar plantas.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA10, OA11 = "LC02 OA 10", "LC02 OA 11"

CONSULT = " Recuerda: lo que es tradicional lo enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales a ellos antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. No evaluar creencias."


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


H_AYM = "Pueblo aymara: vive en el altiplano del norte de Chile. Cría llamas y alpacas y cultiva papas y quinua."
H_LICK = "Pueblo lickanantay: vive en el desierto de Atacama, en oasis cerca de un gran salar. Los canales llevan el agua a los cultivos."
H_RN = "Pueblo rapa nui: vive en una isla del océano Pacífico, rodeada por el mar. La pesca es una actividad importante."
H_DIA = "Pueblo diaguita: vive en valles del Norte Chico, junto a ríos. Cultiva en los valles y hace cerámica."
H_MAP = "Pueblo mapuche: vive en el centro y sur de Chile. Cultiva la tierra y teje."

# ============================================================ OA 10 · Elementos espirituales, naturales y cósmicos
L(
    OA10, 1,
    materials="Lápiz y hojas. Los ejemplos de comunidad son inventados y están escritos aquí.",
    use="Aprenderé a distinguir elementos naturales, cósmicos y espirituales y a saber quién puede explicarlos. Sirve para hablar de ellos con respeto, sin inventar ni burlarse.",
    prior=["Sé que cada pueblo tiene su cultura.", "Sé que una ficha dice quién cuenta."],
    explain=[
        "Para muchos pueblos originarios, la naturaleza y el cielo son parte de su manera de ver el mundo. Los elementos naturales son el mar, el río, el cerro, las plantas y los animales. Los elementos cósmicos son el sol, la luna, las estrellas y el cielo.",
        "También existen los elementos espirituales. Son seres o fuerzas en las que un pueblo cree. Se nombran divinidades o deidades, y entes tutelares, que según la creencia cuidan un lugar o a las personas. Cada pueblo tiene los suyos y los explica a su manera.",
        "Estas creencias son delicadas. No las inventamos ni las juzgamos. Las explican las personas de cada pueblo, en especial el educador o la educadora tradicional. En este cuaderno usamos ejemplos de práctica inventados para aprender a escuchar con respeto.",
    ],
    vocab=[("elemento natural", "parte de la naturaleza, como un río o un cerro"), ("elemento cósmico", "parte del cielo, como el sol o la luna"), ("divinidad", "ser superior al que un pueblo honra, según su creencia"), ("ente tutelar", "ser que, según la creencia, cuida un lugar o a las personas"), ("creencia", "lo que una persona o un pueblo considera verdadero y sagrado")],
    worked=[
        W("Clasificar elementos", "Clasifica en NATURAL o CÓSMICO: río, luna, cerro, sol.", ["El río y el cerro son parte de la tierra.", "La luna y el sol están en el cielo.", "Los separo en dos grupos."], "Natural: río, cerro. Cósmico: luna, sol."),
        W("Ejemplo inventado de ente tutelar", "Ficha inventada: «Según don Luis, en Valle Alto se cuenta que el cerro cuida a la comunidad.» ¿Quién es la fuente y qué dice?", ["La fuente es don Luis.", "Dice que, según la creencia de su comunidad, el cerro cuida a la gente.", "Es un ejemplo para practicar."], "Don Luis; dice que el cerro cuida a la comunidad según su creencia."),
    ],
    mistakes=[
        M("Decir que una creencia de otro pueblo es falsa o tonta.", "Las creencias son importantes para quienes las tienen.", "Escucha con respeto y pregunta sin juzgar."),
        M("Inventar el nombre de un ser espiritual para completar una tarea.", "Podrías decir algo falso sobre un pueblo.", "Escribe solo lo que dice la fuente."),
    ],
    R=[
        ex("El mar, el río y el cerro son elementos... A) naturales B) cósmicos", "A", "Son parte de la naturaleza de la tierra."),
        ex("El sol y la luna son elementos... A) naturales de la tierra B) cósmicos", "B", "Están en el cielo."),
        ex("¿Quién explica las creencias de un pueblo: las personas de ese pueblo o cualquier persona que no las conoce?", "Las personas de ese pueblo", "Ellas conocen sus creencias."),
    ],
    C=[
        ex("Verdadero o falso: se puede inventar el nombre de un ser espiritual para una tarea.", "Falso", "Se puede decir algo falso sobre un pueblo."),
        ex("¿Qué es un ente tutelar según esta clase? A) Un ser que según la creencia cuida un lugar B) Un tipo de herramienta", "A", "Es la definición dada."),
        ex("¿Qué haces si no entiendes una creencia? A) Me burlo B) Pregunto con respeto", "B", "Preguntar evita ofender."),
    ],
    A=[
        ex("Clasifica en NATURAL o CÓSMICO: estrella, planta, mar, cielo.", "Natural: planta, mar. Cósmico: estrella, cielo", "Planta y mar están en la tierra; estrella y cielo, en el espacio."),
        ex("Ficha inventada: «Según doña Rosa, en su comunidad se honra al agua». ¿Quién es la fuente?", "Doña Rosa", "La ficha dice «según doña Rosa»."),
        ex("Une palabra y significado. 1) divinidad 2) ente tutelar 3) creencia. a) ser que según la creencia cuida un lugar b) lo que se considera verdadero y sagrado c) ser superior que se honra", "1-c, 2-a, 3-b", "Cada palabra tiene la definición de la clase."),
    ],
    Z=[
        ex("Pedro dice: «Eso que cuentan es mentira». Ema dice: «Es lo que cree su comunidad y merece respeto». ¿Quién actúa mejor?", "Ema", "Respeta a quienes tienen esa creencia."),
        ex("Una niña dice que conoce todas las creencias de todos los pueblos. ¿Es posible? Responde Sí o No.", "No", "Cada pueblo tiene las suyas y las explican sus integrantes."),
    ],
    D=[
        ex("Ficha inventada: «Según don Luis, el río es parte de la vida de su comunidad. Lo cuenta él». ¿Podemos decir que todos los pueblos creen lo mismo del río? Responde Sí o No.", "No", "La ficha habla de una comunidad inventada y de una sola fuente."),
        ex("Un video muestra una ceremonia sin explicar de quién es. ¿Puedes decir qué significa? Responde Sí o No.", "No", "Sin fuente no se puede afirmar."),
    ],
    context=[ex("En clase, Tomás dice que el cerro de Valle Alto cuida a la gente. Su profesora le pregunta de dónde lo sabe. ¿Cuál es una buena respuesta? A) «Lo leí en la ficha de don Luis» B) «Me lo imaginé»", "A", "Una buena respuesta cita la fuente.")],
    selfcheck=[ex("Escribe un ejemplo de elemento natural y uno de elemento cósmico.", "Río y sol, por ejemplo", "Un río es natural y el sol es cósmico."), ex("¿Quién explica las creencias de un pueblo?", "Las personas de ese pueblo", "Ellas son la fuente."), ex("¿Qué haces si una creencia te parece distinta a la tuya?", "Escucho con respeto", "No se juzga.")],
    task=T("Mira esta ficha inventada de Valle Alto: «Según don Luis, la comunidad respeta al río porque les da agua. Cuenta que sus abuelos agradecen al agua cuando la usan.» Haz una tabla: fuente, elemento natural, qué hace la comunidad. Después escribe una pregunta respetuosa para el educador tradicional sobre un elemento natural importante en su pueblo. No dibujes seres espirituales ni ceremonias.",
           "Fuente: don Luis. Elemento: el río. La comunidad lo respeta y agradece al usarlo. Pregunta: ¿qué elemento de la naturaleza es importante para su pueblo?",
           ["usa datos de la ficha", "nombra a la fuente", "no inventa seres espirituales"], ["tabla de tres filas", "pregunta"], ["inventar seres espirituales", "juzgar la creencia"],
           "Valorar la tabla; si inventó un ser espiritual, pedir que lo reemplace por una pregunta."),
    reinforce="Haz una lista de cinco elementos naturales y cinco cósmicos que conozcas.",
    extend="Escribe una pregunta para el educador tradicional sobre el cielo o el mar en su pueblo.",
)

L(
    OA10, 2,
    materials="Lápiz y hojas. Los ejemplos son inventados.",
    use="Aprenderé cómo la naturaleza y el cielo se relacionan con la vida diaria de una comunidad. Sirve para entender por qué se valoran sin tener que creer ni practicar nada.",
    prior=["Sé qué son los elementos naturales y cósmicos.", "Sé que las creencias se explican con una fuente."],
    explain=[
        "Los elementos de la naturaleza y del cielo están presentes en la vida diaria. Una comunidad puede mirar el sol, la luna o las estrellas para decidir cuándo sembrar o cuándo salir a pescar. El mar da alimento y el río da agua. Por eso se les valora y se les cuida. En esta clase los ejemplos son inventados.",
        "Algunos pueblos tienen formas propias de agradecer a la tierra, al agua y a otros elementos. Cuáles son, cómo se hacen y qué significan lo explica cada comunidad y su educador tradicional. Nosotros no las adivinamos ni las inventamos.",
        "Hay elementos espirituales que algunos pueblos honran en ocasiones especiales. Nosotros no hacemos esas ceremonias en el aula ni las copiamos. Aprendemos a reconocerlas con respeto y a hacer preguntas. Cada pueblo tiene su propia relación con el mundo.",
    ],
    vocab=[("observar", "mirar con atención para aprender"), ("agradecer", "reconocer lo que se recibe"), ("ocasión especial", "momento importante para una comunidad"), ("cuidar", "mantener algo en buen estado")],
    worked=[
        W("Elemento y vida diaria", "Ficha inventada: «En Bahía Clara, los pescadores observan la luna para elegir cuándo salir al mar». ¿Qué elemento cósmico aparece y para qué sirve?", ["El elemento cósmico es la luna.", "Sirve para elegir cuándo pescar.", "Lo escribo en una frase."], "La luna; sirve para elegir cuándo salir a pescar."),
        W("Un elemento natural en una ficha", "Ficha inventada: «Según don Luis, en Valle Alto la comunidad agradece al agua cada vez que la usa». ¿Qué elemento natural aparece y qué hace la comunidad?", ["El elemento natural es el agua.", "La comunidad agradece al usarla.", "Lo escribo y nombro la fuente."], "El agua; según don Luis, la comunidad la agradece."),
    ],
    mistakes=[
        M("Pensar que todos los pueblos se relacionan igual con el cielo.", "Cada pueblo tiene su propia visión.", "Lee cada ficha y no mezcles."),
        M("Hacer una ceremonia en el aula para «probar cómo es».", "Las ceremonias tienen un sentido y no son juegos.", "Mejor escucha a una persona de la comunidad si te invita."),
    ],
    R=[
        ex("Un pescador observa la luna para elegir cuándo pescar. ¿La luna es un elemento natural de la tierra o cósmico?", "Cósmico", "La luna está en el cielo."),
        ex("El río da agua. ¿Qué da el río: agua o dinero?", "Agua", "El río da agua para la comunidad."),
        ex("Ficha inventada: «Según doña Rosa, la comunidad cuida la vertiente». ¿Qué elemento de la naturaleza cuida: la vertiente o el cielo?", "La vertiente", "La ficha lo dice."),
    ],
    C=[
        ex("Verdadero o falso: todas las comunidades se relacionan igual con el cielo.", "Falso", "Cada pueblo tiene su propia visión."),
        ex("¿Por qué una comunidad agradece al agua? A) Porque le da vida y alimento B) Porque es bonita", "A", "El agua es necesaria para vivir."),
        ex("Si una ceremonia es importante para un pueblo, ¿la hacemos en clase como juego? Responde Sí o No.", "No", "Las ceremonias no son un juego."),
    ],
    A=[
        ex("Ficha inventada de Bahía Clara: «Miramos el sol para saber la hora del trabajo, la luna para elegir cuándo pescar y bebemos el agua del río». Une elemento y uso. 1) sol 2) luna 3) río. a) elegir cuándo pescar b) saber la hora del trabajo c) tener agua para beber", "1-b, 2-a, 3-c", "Cada elemento tiene el uso que dice la ficha."),
        ex("Marca solo lo respetuoso: a) escuchar una explicación b) imitar una ceremonia en el patio c) preguntar con respeto d) burlarse.", "a y c", "Escuchar y preguntar respetan; imitar y burlarse no."),
        ex("Ficha inventada: «Los vecinos agradecen al agua cada vez que la usan». ¿Qué hacen los vecinos con el agua: agradecer o contaminar?", "Agradecer", "La ficha dice que agradecen."),
    ],
    Z=[
        ex("Lía dice: «Todos los pueblos hacen lo mismo con el cielo». ¿Qué le dirías?", "Que cada pueblo tiene su propia relación", "Las fichas muestran formas distintas."),
        ex("Mateo quiere hacer en el patio una ceremonia que vio en un video. ¿Qué error comete?", "Imitar una ceremonia como juego", "Las ceremonias tienen sentido para sus comunidades."),
    ],
    D=[
        ex("En una ficha inventada, una comunidad observa las estrellas para saber cuándo sembrar. ¿Qué dato le falta a la ficha para ser buena? A) La fuente B) El color de las estrellas", "A", "Siempre debe decir quién cuenta."),
        ex("Dos fichas: una dice que el río es importante por el agua, otra por las historias. ¿Se contradicen? Responde Sí o No.", "No", "Un mismo elemento puede importar por varias razones."),
    ],
    context=[ex("Julia quiere escribir en un cartel el nombre de un ser espiritual que oyó en un video. Su profesor le pregunta cómo lo sabe. ¿Qué debe hacer? A) Preguntar al educador tradicional y decir la fuente B) Escribirlo porque suena bien", "A", "No se escriben nombres sin fuente y sin consultar.")],
    selfcheck=[ex("¿Para qué observan algunos pueblos el cielo?", "Para saber cuándo sembrar o pescar", "Es la idea de la explicación."), ex("¿Qué haces si no entiendes un ejemplo de otra cultura?", "Pregunto con respeto", "Así evitas inventar datos."), ex("Verdadero o falso: las ceremonias se pueden copiar en clase.", "Falso", "Tienen un sentido y no son un juego.")],
    task=T("Lee esta ficha inventada: «En Bahía Clara, la comunidad observa la luna para elegir cuándo pescar y agradece al mar por los peces. Lo cuenta doña Rosa.» Dibuja una escena con el mar, la luna y un bote, sin personas en ceremonia. Debajo, escribe dos frases: una sobre el elemento cósmico y otra sobre el elemento natural, con la fuente.",
           "Dibujo: mar de noche con luna y bote. Frases: según doña Rosa, la comunidad observa la luna para elegir cuándo pescar. Según doña Rosa, agradecen al mar por los peces.",
           ["identifica un elemento cósmico y uno natural", "cita la fuente", "no dibuja ceremonias"], ["dibujo", "dos frases"], ["dibujar ceremonias", "olvidar la fuente"],
           "Revisar que no haya ceremonias dibujadas y que se cite a doña Rosa."),
    reinforce="Copia la ficha de Bahía Clara y subraya el elemento cósmico y el natural.",
    extend="Escribe una pregunta sobre cómo observa el cielo un pueblo originario para un educador tradicional.",
)

L(
    OA10, 3,
    materials="Lápiz y hojas. Los casos son inventados. No necesitas plantas ni sustancias.",
    use="Aprenderé que la medicina ancestral existe hoy, que la conocen personas de cada pueblo y que no se prueba ni se prepara por cuenta propia. Sirve para respetar ese saber y cuidar tu salud.",
    prior=["Sé que hay elementos naturales en la vida diaria.", "Sé que un portador del conocimiento es una persona que sabe y enseña."],
    explain=[
        "La medicina ancestral es el conocimiento de un pueblo sobre cómo cuidar la salud con plantas, alimentos, cuidados y prácticas. Lo conocen y lo aplican personas a quienes su comunidad reconoce por ese saber. Cada pueblo las nombra a su manera, y eso lo explican el educador tradicional y la comunidad.",
        "Estos saberes están vivos hoy. Hay personas que visitan al médico de un consultorio y también consultan a una autoridad de su comunidad. Las dos formas de cuidar la salud pueden convivir. Nunca debemos pensar que una es mejor sin saber.",
        "Por seguridad, jamás probamos plantas, hojas o frutos que no sean nuestros alimentos conocidos. Nunca preparamos remedios por cuenta propia. Si queremos aprender, escuchamos a un educador tradicional y a nuestras familias con la ayuda de un adulto. La salud es lo primero.",
    ],
    vocab=[("medicina ancestral", "saber de un pueblo para cuidar la salud"), ("autoridad de la comunidad", "persona a quien su comunidad reconoce y respeta por su saber"), ("remedio", "algo que se usa para curar"), ("seguridad", "estar protegido de un daño"), ("consultorio", "lugar donde un médico atiende a las personas")],
    worked=[
        W("Qué hacer con una planta", "Un niño ve una planta en el cerro y piensa que sirve como remedio. ¿Qué debe hacer? a) probarla b) preguntar a un adulto y a un educador tradicional c) dársela a un amigo.", ["Probar plantas es peligroso.", "Un adulto y un educador saben cómo hacerlo con seguridad.", "Elijo preguntar."], "b"),
        W("Dos formas de cuidar la salud", "Caso inventado: una abuela va al consultorio y también conversa con una autoridad de su comunidad. ¿Cuántas formas de cuidar la salud usa?", ["Va al consultorio: una.", "Conversa con la autoridad de su comunidad: dos.", "Cuento las dos."], "2"),
    ],
    mistakes=[
        M("Probar una planta porque «seguro es medicina».", "Muchas plantas son peligrosas.", "No pruebes plantas: pregunta a un adulto."),
        M("Decir que la medicina de un pueblo es peor que la del hospital.", "Cada saber tiene su valor y su lugar.", "Respeta ambos y pregunta a una fuente."),
    ],
    R=[
        ex("¿Se deben probar plantas desconocidas? Responde Sí o No.", "No", "Pueden ser peligrosas."),
        ex("La medicina ancestral es un saber de un pueblo para cuidar la salud. ¿Verdadero o falso?", "Verdadero", "Es su definición."),
        ex("Si ves una planta desconocida, ¿le preguntas a un adulto o la pruebas?", "Le pregunto a un adulto", "Es la forma segura de actuar."),
    ],
    C=[
        ex("Verdadero o falso: se pueden preparar remedios sin ayuda de un adulto.", "Falso", "Es peligroso y no corresponde."),
        ex("¿Quién aplica la medicina ancestral? A) Personas que su comunidad reconoce por ese saber B) Cualquier persona que probó una planta", "A", "Es un saber que se aprende y se reconoce en la comunidad."),
        ex("¿Se pueden usar la medicina del consultorio y los saberes de una comunidad? Responde Sí o No.", "Sí", "Pueden convivir con respeto."),
    ],
    A=[
        ex("Marca las acciones seguras: a) preguntar a un adulto b) probar hojas del cerro c) escuchar al educador d) preparar un remedio solo.", "a y c", "Preguntar y escuchar son acciones seguras."),
        ex("Ordena para cuidar tu salud si te sientes mal: 1) sigo las indicaciones del médico 2) aviso a un adulto 3) voy con un adulto al consultorio. Escribe el orden.", "2, 3, 1", "Primero aviso, luego voy al consultorio y al final sigo las indicaciones."),
        ex("Un niño tiene dolor de estómago. ¿Qué hace primero? A) Avisa a un adulto B) Toma hojas del patio", "A", "Los adultos deciden cómo cuidar su salud."),
    ],
    Z=[
        ex("Tomás dice: «Esa planta es medicina, la voy a probar». ¿Qué le dirías por seguridad?", "Que no pruebe plantas y pregunte a un adulto", "Podría enfermarse si la prueba."),
        ex("Rosa dice que la medicina ancestral ya no existe. ¿Qué dato de esta clase la contradice?", "Hay personas que hoy la conocen y la aplican", "Es un saber vivo."),
    ],
    D=[
        ex("Una niña ve a su abuela recoger una planta que ella conoce bien. ¿Debe copiar sola esa acción cuando no está la abuela? Responde Sí o No.", "No", "Solo la abuela sabe cómo y cuándo."),
        ex("Un libro dice que una planta cura. Otro no lo dice. ¿Qué haces antes de usarla?", "Preguntar a un adulto o al educador", "Hay que verificar con quien sabe."),
    ],
    context=[ex("En el aula leen sobre medicina ancestral. Julia trae un frasco con hojas de su casa para mostrar. La profesora le pide que no lo abra. ¿Por qué?", "Por seguridad", "Las plantas no se manipulan sin un adulto que sepa.")],
    selfcheck=[ex("¿Quién sabe aplicar la medicina ancestral?", "Personas reconocidas por su comunidad", "Son las portadoras de ese saber."), ex("Escribe una regla de seguridad con plantas.", "No probar plantas desconocidas", "Pueden dañar la salud."), ex("Verdadero o falso: el saber de un pueblo y el consultorio pueden convivir.", "Verdadero", "Se complementan con respeto.")],
    task=T("Lee este caso inventado: «Una niña se siente mal. Su mamá la lleva al consultorio y después conversa con la autoridad de su comunidad.» Dibuja dos cuadros: uno con el consultorio y otro con una conversación. Escribe tres reglas de seguridad para tu salud, por ejemplo no probar plantas. No dibujes plantas ni preparaciones reales.",
           "Cuadros: consultorio y conversación. Reglas: no probar plantas; avisar a un adulto; preguntar a un educador.",
           ["dibuja las dos formas de cuidado", "escribe tres reglas de seguridad", "no incluye preparaciones"], ["dos cuadros", "tres reglas"], ["incluir recetas", "probar plantas"],
           "Revisar que no haya recetas ni instrucciones de preparación."),
    reinforce="Copia las tres reglas de seguridad y compártelas con un adulto de tu casa.",
    extend="Escribe una pregunta para el educador tradicional: ¿cómo saben las comunidades quién puede cuidar la salud?",
)

L(
    OA10, 4,
    materials="Lápiz y hojas. Los casos son inventados.",
    use="Aprenderé acciones respetuosas ante los elementos espirituales y naturales: no tocar lo sagrado, no imitar ritos y devolver cuidado a la naturaleza. Sirve para actuar con respeto en cualquier lugar.",
    prior=["Sé que hay creencias que merecen respeto.", "Sé que no se prueban plantas desconocidas."],
    explain=[
        "Los elementos sagrados de un pueblo merecen cuidado. Un objeto sagrado no se toca ni se fotografía sin permiso. Un lugar sagrado no se visita sin que la comunidad lo autorice. Una ceremonia no se imita ni se transforma en juego.",
        "También cuidamos con la naturaleza. El agua, el cielo y la tierra nos dan vida. Una forma de devolver es cuidarlos: no botar basura, no malgastar el agua, tomar solo lo necesario y agradecer. Esa es la reciprocidad con la naturaleza.",
        "Si no estamos seguros de qué hacer, preguntamos antes. Podemos decir: «¿Me puede explicar con respeto?» o «¿Puedo estar aquí?». Y si la persona dice que no, lo aceptamos. Respetar es lo mismo que cuidar a todos, aunque no comprendamos del todo.",
    ],
    vocab=[("sagrado", "muy importante y respetado por una comunidad"), ("reciprocidad", "devolver algo a cambio de lo que se recibe"), ("permiso", "aprobación de quien puede darla"), ("malgastar", "usar más de lo que se necesita"), ("agradecer", "reconocer lo que se recibe")],
    worked=[
        W("Qué hacer ante un objeto", "Un niño ve un objeto especial en el hogar de un vecino. ¿Qué debe hacer? a) tocarlo b) pedir permiso y preguntar con respeto c) fotografiarlo.", ["Los objetos especiales pueden ser sagrados.", "No se tocan ni se fotografían sin permiso.", "Elijo la opción respetuosa."], "b"),
        W("Devolver a la naturaleza", "El agua de la comunidad viene de un río de práctica. ¿Qué acción devuelve cuidado: cerrar la llave cuando no se usa, o dejarla abierta?", ["Cuidar el agua es devolver.", "Cerrar la llave cuando no se usa cuida.", "Dejarla abierta malgasta."], "Cerrar la llave cuando no se usa"),
    ],
    mistakes=[
        M("Imitar una ceremonia en un juego.", "Tiene un sentido especial y puede ofender.", "Escucha una explicación de una persona de la comunidad."),
        M("Sacar fotos de un lugar sagrado sin permiso.", "Puede violar su privacidad y su sentido.", "Pregunta antes y acepta la respuesta."),
    ],
    R=[
        ex("Antes de tocar un objeto especial, ¿qué haces? A) Pedir permiso B) Tocarlo rápido", "A", "El objeto puede ser sagrado."),
        ex("¿Se puede imitar una ceremonia en el patio como juego? Responde Sí o No.", "No", "No es un juego."),
        ex("Cerrar la llave del agua es una forma de cuidar. ¿Verdadero o falso?", "Verdadero", "Así se evita malgastar."),
    ],
    C=[
        ex("Verdadero o falso: se puede fotografiar un lugar sagrado sin permiso.", "Falso", "Hay que pedir autorización."),
        ex("¿Qué significa reciprocidad con la naturaleza? A) Devolver cuidado por lo que recibimos B) Tomar todo lo que se pueda", "A", "Es cuidar lo que nos da vida."),
        ex("Si la persona dice que no puedes estar en un lugar, ¿qué haces? A) Me quedo igual B) Lo acepto", "B", "Se respeta su decisión."),
    ],
    A=[
        ex("Marca las acciones de cuidado: a) apagar la llave del agua b) botar basura al río c) agradecer el agua d) disfrazarse para una ceremonia.", "a y c", "Cuidan el agua y reconocen lo que se recibe."),
        ex("Ordena: 1) acepto la respuesta 2) pregunto con respeto 3) llego al lugar. Escribe el orden.", "3, 2, 1", "Primero llego, luego pregunto y al final acepto lo que dicen."),
        ex("Una niña ve un lugar con una piedra especial. ¿Qué hace para respetarlo? A) La levanta B) La deja donde está", "B", "Las piedras especiales no se mueven."),
    ],
    Z=[
        ex("Ema dice: «Si saco una foto no pasa nada». ¿Qué le dirías sobre un lugar sagrado?", "Que debe pedir permiso", "El lugar puede tener reglas."),
        ex("Pedro dice que cuidar el agua no sirve de nada porque ya la recibimos. ¿Qué le responderías con esta clase?", "Que cuidar el agua es devolver lo que recibimos", "Cuidar la naturaleza es reciprocidad."),
    ],
    D=[
        ex("Un grupo visita un río de práctica. Cuatro ideas: a) llevar basura de vuelta b) cantar fuerte c) pedir permiso d) agradecer al terminar. ¿Cuáles son de respeto?", "a, c y d", "Cantar fuerte puede molestar."),
        ex("Una comunidad pide que no se publique el lugar de una ceremonia. Un visitante lo publica de todas formas. ¿Qué falló?", "No respetó su decisión", "La comunidad decide qué compartir."),
    ],
    context=[ex("El curso visita un parque con una laguna. Lía propone dejar sus restos de comida en el agua porque «los peces comen». ¿Está bien? Responde Sí o No.", "No", "Puede dañar la laguna.")],
    selfcheck=[ex("¿Qué haces antes de tocar un objeto especial?", "Pedir permiso", "Puede ser sagrado."), ex("Escribe dos formas de cuidar el agua.", "Cerrar la llave y no botar basura", "Son acciones de cuidado."), ex("Verdadero o falso: imitar una ceremonia es respetuoso.", "Falso", "Tiene un sentido que no se juega.")],
    task=T("Crea una tarjeta de cuidado para ir de excursión a un río de práctica. Escribe cinco reglas, incluyendo una sobre pedir permiso, una sobre la basura y una sobre no tocar objetos especiales. Dibuja el río con el cielo. No dibujes ceremonias ni lugares sagrados reales.",
           "1. Pedir permiso. 2. Llevar la basura de vuelta. 3. No tocar objetos especiales. 4. No gritar. 5. Agradecer. Dibujo: río con sol.",
           ["escribe cinco reglas", "incluye permiso, basura y objetos", "no dibuja ceremonias"], ["tarjeta", "dibujo"], ["reglas peligrosas", "dibujar ceremonias"],
           "Revisar que las reglas sean claras y seguras."),
    reinforce="Elige tres reglas de la tarjeta y explica cada una a un adulto.",
    extend="Escribe una regla más para cuidar la naturaleza en tu barrio.",
)

L(
    OA10, 5,
    materials="Lápiz y hojas. La ficha y los datos están escritos aquí.",
    use="Aprenderé a presentar lo que entendí sobre elementos espirituales, naturales y cósmicos diciendo mis fuentes y lo que no puedo afirmar. Sirve para comunicar con honestidad.",
    prior=["Sé que cada creencia tiene sus portadores.", "Sé que no se inventan significados."],
    explain=[
        "Presentar lo que aprendiste es contar tres cosas: qué entendí, de qué fuente lo sé y qué no puedo afirmar. Por ejemplo: «Entendí que la comunidad de Bahía Clara observa la luna para pescar. Lo leí en la ficha de doña Rosa. No sé si otras comunidades hacen lo mismo».",
        "Es muy importante decir lo que no sabes. Eso se llama ser honesto. Si no sabes el significado de una palabra o una práctica, lo dices y preguntas. Nadie espera que sepas todo. Lo importante es no inventar y no hablar por otros.",
        "Al presentar sobre creencias de otros pueblos, usamos frases como «según la ficha» o «según el educador tradicional». También evitamos decir «todos creen». Y si hay algo muy delicado, mejor lo dejamos fuera y lo conversamos con un adulto.",
    ],
    vocab=[("presentar", "contar a otros lo que aprendiste"), ("honestidad", "decir la verdad, también sobre lo que no sabes"), ("según", "palabra que dice quién cuenta algo"), ("delicado", "que debe tratarse con mucho cuidado"), ("afirmar", "decir que algo es verdad")],
    worked=[
        W("Qué puedo afirmar", "Ficha inventada: «Según doña Rosa, la comunidad observa la luna para pescar». Frases: a) «Todos los pueblos observan la luna» b) «Según doña Rosa, su comunidad observa la luna para pescar». ¿Cuál puedo afirmar?", ["La ficha habla de una comunidad y una fuente.", "La frase b respeta eso.", "La frase a habla de todos los pueblos."], "b"),
        W("Decir lo que no sé", "Leíste sobre una práctica, pero no sabes su significado. ¿Qué dices al presentar?", ["No invento un significado.", "Digo que no lo sé.", "Pregunto al educador."], "Digo «no lo sé» y pregunto"),
    ],
    mistakes=[
        M("Decir «todos creen» en una presentación.", "No puedes hablar por todo un pueblo.", "Usa «según la ficha» o «según el educador»."),
        M("Inventar un significado para no quedar mal.", "Puede ser falso y faltar al respeto.", "Di «no lo sé» y pregunta."),
    ],
    R=[
        ex("Una presentación incluye qué entendí, mi fuente y lo que no puedo afirmar. ¿Cuántas partes son?", "3", "Se cuentan las tres partes."),
        ex("Si no sabes un significado, ¿dices «no lo sé» o lo inventas?", "Digo «no lo sé»", "Ser honesto es no inventar."),
        ex("«Según la ficha» sirve para decir la fuente. ¿Verdadero o falso?", "Verdadero", "Esa frase nombra la fuente."),
    ],
    C=[
        ex("Verdadero o falso: al presentar, hay que decir lo que no sabes.", "Verdadero", "Es parte de ser honesto."),
        ex("¿Qué frase es mejor? A) «Todos los pueblos creen lo mismo» B) «Según la ficha de doña Rosa, su comunidad…»", "B", "Cita la fuente y no habla por todos."),
        ex("¿Qué haces si un tema es muy delicado? A) Lo dejo fuera y lo converso con un adulto B) Lo invento", "A", "Cuidas el tema y a las personas."),
    ],
    A=[
        ex("Ficha inventada: «Según don Luis, el río da agua a Valle Alto». Clasifica en PUEDO AFIRMAR o NO PUEDO AFIRMAR: a) El río da agua a Valle Alto, según don Luis. b) Todos los ríos de Chile dan agua según don Luis.", "a puedo afirmar; b no puedo afirmar", "La ficha solo habla de Valle Alto."),
        ex("Ordena una presentación: 1) lo que no puedo afirmar 2) lo que entendí 3) mi fuente. Escribe el orden: 2, 3, 1 o 1, 2, 3.", "2, 3, 1", "Primero lo que entendí, luego la fuente y al final lo que no puedo afirmar."),
        ex("Completa con una palabra: «_____ la ficha de doña Rosa, su comunidad observa la luna».", "Según", "Esa palabra nombra la fuente."),
    ],
    Z=[
        ex("Tomás presenta: «Todos creen que la luna manda en los peces». ¿Qué error comete?", "Habla por todos sin fuente", "No puede afirmar que todos lo creen."),
        ex("Ana dice: «No sé qué significa esta práctica, voy a preguntar». ¿Qué cualidad muestra?", "Honestidad", "Reconoce lo que no sabe."),
    ],
    D=[
        ex("En una presentación se muestra una foto de una ceremonia sin explicar de quién es. ¿Qué falta antes de mostrarla?", "La fuente y el permiso", "Hay que saber de quién es y si se puede mostrar."),
        ex("Un compañero dice algo delicado sobre la creencia de una comunidad. ¿Qué hace un oyente respetuoso?", "Pregunta si es correcto a un adulto o al educador", "Evita difundir algo falso."),
    ],
    context=[ex("El curso presenta lo aprendido. Julia dice: «Aprendí que según doña Rosa se observa la luna; no sé si todos lo hacen». ¿Es una buena presentación? Responde Sí o No.", "Sí", "Cita la fuente y dice lo que no sabe.")],
    selfcheck=[ex("¿Cuáles son las tres partes de una presentación honesta?", "Lo que entendí, mi fuente y lo que no puedo afirmar", "Son las tres ideas de la clase."), ex("¿Qué palabra uso para decir quién cuenta?", "Según", "Nombra la fuente."), ex("Verdadero o falso: puedo inventar si no sé.", "Falso", "Debo decir que no lo sé.")],
    task=T("Prepara una presentación de un minuto sobre lo que aprendiste del OA. Usa la ficha inventada: «Según doña Rosa, en Bahía Clara la comunidad observa la luna para pescar y agradece al mar». Escribe tres frases: una de lo que entendí, una de la fuente y una de lo que no puedo afirmar. Dibuja una lámina sin personas en ceremonia.",
           "Entendí que la comunidad observa la luna para pescar. Mi fuente es doña Rosa. No puedo afirmar que otras comunidades hagan lo mismo.",
           ["escribe las tres frases", "usa según", "no inventa"], ["tres frases", "lámina"], ["decir todos creen", "inventar"],
           "Revisar las tres partes y el uso de «según»."),
    reinforce="Practica en voz alta tus tres frases con un adulto.",
    extend="Escribe una frase que explique por qué es bueno decir lo que no sabes.",
)

# ============================================================ OA 11 · Naturaleza y actividades productivas
L(
    OA11, 1,
    materials="Lápiz y hojas. Las fichas están escritas en el cuaderno.",
    use="Aprenderé qué es una actividad productiva y cómo cada pueblo se relaciona con la naturaleza para realizarla. Sirve para reconocer los saberes de cada pueblo sin mezclarlos.",
    prior=["Sé que cada pueblo vive en un paisaje distinto.", "Sé que una ficha tiene una fuente."],
    explain=[
        "Una actividad productiva es un trabajo con el que las personas consiguen alimentos o hacen cosas útiles. Pueden ser cultivar, criar animales, pescar, tejer o hacer cerámica. Casi todas dependen de lo que da la naturaleza en el lugar donde se vive.",
        "Cada pueblo tiene actividades propias, porque cada territorio es distinto. En el desierto, el agua de los canales permite cultivar. En el altiplano se crían llamas. En el mar se pesca. Estos conocimientos se aprenden de los mayores y se transmiten a las nuevas generaciones.",
        "Para saber qué actividades hace un pueblo, usamos una ficha o una persona que lo cuente. No generalizamos. No todas las personas de un pueblo se dedican a lo mismo. En este cuaderno usamos fichas con datos generales y claros.",
    ],
    vocab=[("actividad productiva", "trabajo con el que se consigue alimento o se hacen cosas útiles"), ("cultivar", "sembrar y cuidar plantas para cosechar"), ("criar", "cuidar animales para que crezcan"), ("pescar", "sacar peces del mar o de un río"), ("conocimiento", "lo que se sabe y se aprende")],
    worked=[
        W("Leer una actividad en una ficha", H_AYM + " ¿Qué actividades productivas nombra?", ["Busco verbos de trabajo.", "Cría llamas y alpacas: crianza.", "Cultiva papas y quinua: cultivo."], "Criar llamas y alpacas, y cultivar papas y quinua."),
        W("No generalizar", "Ana lee la ficha rapa nui y dice que todas las personas de ese pueblo son pescadoras. ¿Qué error comete?", ["La ficha dice que la pesca es una actividad importante.", "No dice que todos pescan.", "Generaliza."], "Generaliza"),
    ],
    mistakes=[
        M("Pensar que todos los pueblos hacen las mismas actividades.", "Cada territorio da cosas distintas.", "Lee la ficha de cada pueblo."),
        M("Decir que todas las personas de un pueblo hacen lo mismo.", "Cada persona se dedica a cosas distintas.", "Di «algunas personas» o «una actividad importante»."),
    ],
    R=[
        ex("Cultivar papas es una actividad productiva. ¿Verdadero o falso?", "Verdadero", "Se consigue alimento sembrando y cosechando."),
        ex("Criar llamas es cuidar animales. ¿Verdadero o falso?", "Verdadero", "Criar es cuidar animales para que crezcan."),
        ex("Pescar es sacar peces del mar. ¿Es una actividad productiva? Responde Sí o No.", "Sí", "La pesca da alimento."),
    ],
    C=[
        ex("¿Por qué los pueblos hacen actividades distintas? A) Porque sus territorios son distintos B) Porque no se parecen en nada", "A", "Cada paisaje da cosas diferentes."),
        ex("Verdadero o falso: todos los pueblos hacen las mismas actividades.", "Falso", "Cada territorio es distinto."),
        ex("Según la ficha lickanantay, ¿qué lleva el agua a los cultivos? (" + H_LICK + ")", "Los canales", "La ficha lo dice."),
    ],
    A=[
        ex("Clasifica en CULTIVAR, CRIAR o PESCAR: a) papas b) llamas c) peces. Escribe cada letra con su verbo.", "a cultivar, b criar, c pescar", "Las papas se cultivan, las llamas se crían y los peces se pescan."),
        ex("Une pueblo y actividad. 1) aymara 2) rapa nui 3) lickanantay. a) pesca b) cría de llamas c) cultivo con agua de canales", "1-b, 2-a, 3-c", "Cada dato está en la ficha de su pueblo."),
        ex("Ficha diaguita: " + H_DIA + " ¿Qué dos actividades nombra?", "Cultivar y hacer cerámica", "La ficha dice que cultiva y hace cerámica."),
    ],
    Z=[
        ex("Pedro dice: «Todos los pueblos viven de pescar». ¿Qué le responderías con las fichas?", "Que el pueblo aymara cría llamas y cultiva papas", "Las fichas muestran actividades distintas."),
        ex("Lía lee que la pesca es importante para el pueblo rapa nui y dice que todas las personas pescan. ¿Qué error comete?", "Generaliza", "La ficha no dice que todos pescan."),
    ],
    D=[
        ex("Ficha lickanantay: " + H_LICK + " ¿Por qué los canales son importantes para cultivar en el desierto?", "Porque llevan el agua a los cultivos", "En el desierto el agua es lo que permite cultivar."),
        ex("Un niño dice que una actividad productiva es solo una que vende cosas. ¿Es correcto? Responde Sí o No.", "No", "También sirve para tener alimento y objetos útiles."),
    ],
    context=[ex("Para la feria escolar, el curso lee la ficha mapuche: " + H_MAP + " Tomás escribe que ese pueblo cría llamas. ¿Está bien?", "No", "Esa actividad está en la ficha aymara.")],
    selfcheck=[ex("Escribe dos actividades productivas.", "Cultivar y pescar", "Son ejemplos de la clase."), ex("¿Por qué no se generaliza?", "Porque cada persona se dedica a cosas distintas", "No todos hacen lo mismo."), ex("Verdadero o falso: las actividades dependen del territorio.", "Verdadero", "Cada lugar da cosas distintas.")],
    task=T("Elige UNA ficha de este cuaderno (aymara, lickanantay, rapa nui, diaguita o mapuche). Haz una tabla con tres columnas: pueblo, actividad productiva y qué da la naturaleza para hacerla. Escribe una fila con datos de la ficha. Dibuja la actividad. No dibujes lugares sagrados.",
           "Pueblo: aymara. Actividad: criar llamas. Naturaleza: el altiplano con pastos. Dibujo: una llama en un cerro.",
           ["usa datos de la ficha", "completa las tres columnas", "no mezcla fichas"], ["tabla", "dibujo"], ["inventar datos", "mezclar fichas"],
           "Verificar con la ficha cada dato."),
    reinforce="Une cada ficha con una actividad que nombre.",
    extend="Escribe una pregunta sobre una actividad productiva para un educador tradicional.",
)

L(
    OA11, 2,
    materials="Lápiz y hojas. Los casos son inventados.",
    use="Aprenderé cómo las actividades productivas siguen los ciclos de la naturaleza (estaciones) y cómo se cuida la tierra y el agua. Sirve para entender por qué se hacen en cierto momento.",
    prior=["Sé qué es una actividad productiva.", "Sé los nombres de las estaciones."],
    explain=[
        "Las actividades de campo siguen los ciclos de la naturaleza. En Chile, las estaciones son primavera, verano, otoño e invierno. Una huerta de práctica se siembra en primavera, se cuida en verano, se cosecha en otoño y se guarda en invierno.",
        "Para cultivar hay pasos que se repiten: sembrar, regar y cuidar, cosechar y guardar. Los mayores conocen cuándo hacer cada paso porque observan el clima, el agua y la tierra. Esos conocimientos se transmiten a los más jóvenes.",
        "También hay reciprocidad con la naturaleza. Se toma lo necesario y se devuelve cuidado. Por ejemplo, se guarda parte de las semillas para el próximo año y se cuida el agua. Así la naturaleza sigue dando alimento para todos.",
    ],
    vocab=[("ciclo", "pasos que se repiten una y otra vez"), ("estación", "una de las cuatro partes del año"), ("sembrar", "poner semillas en la tierra"), ("cosechar", "recoger lo que creció"), ("semilla", "parte de la planta de la que nace otra planta")],
    worked=[
        W("Ordenar los pasos", "Ordena: a) cosechar b) sembrar c) regar y cuidar d) guardar.", ["Primero se siembra.", "Luego se riega y cuida.", "Después se cosecha y se guarda."], "b, c, a, d"),
        W("Estación de la siembra", "En la huerta de práctica se siembra en primavera y se cosecha en otoño. ¿Cuántas estaciones hay entre la primavera y el otoño si el orden es primavera, verano, otoño?", ["Cuento: primavera, verano, otoño.", "Entre ambas hay el verano.", "Es una estación entre medio."], "Una: el verano"),
    ],
    mistakes=[
        M("Cosechar antes de tiempo porque tengo hambre.", "La planta aún no está lista y se pierde.", "Espera el momento que dicen los mayores."),
        M("Usar todas las semillas y no guardar ninguna.", "No habrá cultivo el próximo año.", "Guarda una parte para sembrar de nuevo."),
    ],
    R=[
        ex("En Chile, ¿la primavera viene después del invierno? Responde Sí o No.", "Sí", "Las estaciones se repiten: invierno y luego primavera."),
        ex("Sembrar es poner semillas en la tierra. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
        ex("Cosechar es recoger lo que creció. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
    ],
    C=[
        ex("¿Cuál es el primer paso de un cultivo? A) Sembrar B) Cosechar", "A", "Sin sembrar no hay nada que cosechar."),
        ex("Verdadero o falso: se puede cosechar antes de que la planta esté lista.", "Falso", "Se pierde la cosecha."),
        ex("¿Por qué se guarda parte de las semillas? A) Para sembrar el próximo año B) Para botarlas", "A", "Así hay cultivo en el futuro."),
    ],
    A=[
        ex("Ordena los pasos de una huerta de práctica: 1) cosechar 2) sembrar 3) guardar 4) regar y cuidar. Escribe los números en orden.", "2, 4, 1, 3", "Primero se siembra, luego se riega, después se cosecha y al final se guarda."),
        ex("Une paso y acción. 1) sembrar 2) regar 3) cosechar. a) recoger b) poner semillas c) dar agua", "1-b, 2-c, 3-a", "Cada paso tiene su acción."),
        arith("Una huerta de práctica tiene 4 hileras con 5 plantas en cada una. ¿Cuántas plantas hay?", "4*5", "Se multiplican las hileras por las plantas de cada hilera."),
    ],
    Z=[
        ex("Tomás dice: «Siembro y cosecho el mismo día». ¿Qué le falta entender del ciclo?", "Que las plantas necesitan tiempo para crecer", "Entre sembrar y cosechar hay estaciones."),
        ex("Ema guarda todas las semillas en una caja y no siembra ninguna. ¿Qué pasará?", "No habrá cosecha", "Sin sembrar no hay plantas."),
    ],
    D=[
        arith("Una familia de práctica cosechó 30 papas y guardó 8 como semillas. ¿Cuántas papas le quedan para comer?", "30-8", "Se restan las que se guardan.", " papas"),
        ex("Si la siembra es en primavera y la cosecha en otoño, ¿en qué estación se cuida el cultivo? Elige: verano o invierno.", "Verano", "Es la estación entre primavera y otoño."),
    ],
    context=[ex("El curso planta frijoles de práctica en un vaso con algodón húmedo. Julia quiere cosechar al día siguiente. ¿Qué le dices?", "Que debe esperar, las plantas crecen despacio", "Las plantas necesitan tiempo.")],
    selfcheck=[ex("Escribe los cuatro pasos del cultivo.", "Sembrar, regar y cuidar, cosechar y guardar", "Son los pasos de la clase."), ex("¿Por qué se guardan semillas?", "Para sembrar el próximo año", "Así sigue el ciclo."), ex("Verdadero o falso: los mayores conocen cuándo hacer cada paso.", "Verdadero", "Observan el clima y la tierra.")],
    task=T("Dibuja un ciclo de huerta de práctica con cuatro cuadros: sembrar en primavera, cuidar en verano, cosechar en otoño y guardar semillas en invierno. Escribe debajo de cada cuadro una acción de cuidado de la tierra o del agua. No uses plantas peligrosas.",
           "Cuadros: sembrar (primavera), regar (verano), cosechar (otoño), guardar semillas (invierno). Cuidado: no gastar agua de más; devolver restos de verdura a la tierra.",
           ["ordena las cuatro estaciones", "cada cuadro tiene un paso", "incluye cuidado del agua o la tierra"], ["cuatro cuadros", "acciones"], ["ordenar mal los pasos", "olvidar guardar semillas"],
           "Revisar el orden del ciclo y la acción de cuidado."),
    reinforce="Escribe el orden de las cuatro estaciones empezando por primavera.",
    extend="Escribe una pregunta al educador tradicional sobre cómo saben cuándo sembrar.",
)

L(
    OA11, 3,
    materials="Lápiz y hojas. Los casos son inventados.",
    use="Aprenderé que las actividades productivas de los pueblos siguen hoy, se adaptan y se venden en ferias. Sirve para reconocer el trabajo de las personas actuales.",
    prior=["Sé qué es una actividad productiva.", "Sé que las actividades siguen ciclos."],
    explain=[
        "Las actividades productivas de los pueblos originarios siguen hoy. Hay personas que crían animales, cultivan, pescan, tejen y hacen cerámica. También hay personas que trabajan en otras cosas. Cada una aporta con lo que sabe hacer.",
        "Estas actividades han cambiado. Hoy se pueden usar herramientas nuevas, vender en ferias y mostrar los trabajos por internet con permiso. Lo importante es que los conocimientos de los mayores se sigan enseñando y se reconozca quién los creó.",
        "Cuando compramos un producto hecho por una persona de un pueblo originario, es bueno saber quién lo hizo y pagar un precio justo. También se debe respetar que no todo se puede copiar. Las técnicas y diseños pertenecen a quienes los crearon.",
    ],
    vocab=[("feria", "lugar donde las personas venden y compran productos"), ("precio justo", "pago que reconoce el trabajo de quien hizo algo"), ("herramienta", "objeto que ayuda a hacer un trabajo"), ("creador", "persona que hizo un trabajo"), ("reconocer", "decir quién hizo algo")],
    worked=[
        W("Cambio y continuidad", "Caso inventado: «Una familia cultiva papas como sus abuelos, pero hoy vende en una feria con balanza digital». ¿Qué cambió y qué continúa?", ["Cambió la balanza.", "Continúa el cultivo.", "Lo escribo en dos columnas."], "Cambió: balanza digital. Continúa: cultivo de papas."),
        W("Calcular una venta", "En la feria de práctica, una familia vende 6 bolsas de papas por día durante 5 días. ¿Cuántas bolsas vende?", ["Multiplico 6 por 5.", "6 × 5 = 30.", "Escribo la respuesta."], "30 bolsas"),
    ],
    mistakes=[
        M("Pensar que las actividades de un pueblo ya no existen.", "Muchas personas las hacen hoy.", "Pregunta qué se hace hoy y quién lo hace."),
        M("Copiar un diseño de una artesana sin reconocerla.", "El diseño es de quien lo creó.", "Pregunta quién lo hizo y no lo copies."),
    ],
    R=[
        ex("Una feria es un lugar para vender y comprar. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
        ex("Una familia cultiva papas hoy. ¿Esa actividad continúa o se perdió?", "Continúa", "La siguen haciendo."),
        ex("Un precio justo reconoce el trabajo de quien hizo algo. ¿Verdadero o falso?", "Verdadero", "Es su definición."),
    ],
    C=[
        ex("Verdadero o falso: si usan herramientas nuevas, la actividad deja de ser de la familia.", "Falso", "Puede cambiar y seguir siendo suya."),
        ex("¿Por qué es bueno saber quién hizo un producto? A) Para reconocer su trabajo B) Para copiarlo", "A", "Reconocer al creador es respeto."),
        ex("¿Qué actividades siguen hoy? A) Criar, cultivar, pescar y tejer B) Ninguna", "A", "Muchas personas las hacen."),
    ],
    A=[
        arith("En la feria de práctica, una familia vende 5 bolsas de papas por día durante 4 días. ¿Cuántas bolsas vende?", "5*4", "Se multiplican las bolsas por los días."),
        ex("Clasifica en CAMBIÓ o CONTINÚA: a) usar balanza digital b) cultivar como los abuelos c) vender por teléfono.", "a cambió, b continúa, c cambió", "Solo el cultivo sigue igual."),
        ex("Una artesana inventada hace tejidos con diseños propios. ¿Qué debes hacer si quieres uno? A) Comprarlo y reconocerla B) Copiar el diseño", "A", "Se respeta su creación."),
    ],
    Z=[
        ex("Ema dice: «Si cambió la herramienta, ya no es tradicional». ¿Qué le dirías?", "Que el conocimiento sigue aunque cambie la herramienta", "La técnica y el saber continúan."),
        ex("Pedro quiere copiar el diseño de un tejido de la feria y venderlo como suyo. ¿Qué error comete?", "Se apropia del trabajo de otra persona", "El diseño es de quien lo creó."),
    ],
    D=[
        arith("Una artesana de práctica teje 2 chalecos por semana durante 6 semanas. ¿Cuántos chalecos teje?", "2*6", "Se multiplican por las semanas."),
        ex("Una feria de práctica ofrece papas, tejidos y cerámica. ¿Cuántos tipos de productos hay?", "3", "Hay tres tipos."),
    ],
    context=[ex("Tu curso visita una feria con puestos de familias de pueblos originarios. Lía quiere comprar y regatear mucho el precio. ¿Qué es mejor? A) Pagar un precio justo B) Pedir que lo rebajen a casi nada", "A", "Se reconoce el trabajo de quien lo hizo.")],
    selfcheck=[ex("Escribe una actividad que continúa hoy.", "Cultivar o tejer", "Muchas personas las hacen."), ex("¿Qué es un precio justo?", "Un pago que reconoce el trabajo", "Es su definición."), ex("Verdadero o falso: se puede copiar el diseño de una artesana.", "Falso", "El diseño es suyo.")],
    task=T("Imagina una feria de práctica con tres puestos: papas, tejidos y cerámica. Dibuja los tres puestos. Escribe para cada uno una frase que reconozca quién lo hizo, con un nombre inventado, y otra frase que diga por qué ese trabajo merece un precio justo. No uses nombres de personas reales.",
           "Puesto 1: papas cultivadas por doña Rosa; su trabajo toma muchos meses. Puesto 2: tejidos de don Luis; cada uno se hace a mano. Puesto 3: cerámica de Ana; ella la modela y la decora.",
           ["dibuja tres puestos", "reconoce a cada creador", "explica por qué merece un precio justo"], ["dibujo", "frases"], ["no reconocer a los creadores", "decir que el trabajo no vale"],
           "Revisar que cada puesto tenga un nombre inventado."),
    reinforce="Escribe tres productos que se venden en una feria.",
    extend="Escribe una pregunta para el educador tradicional sobre cómo se vende un trabajo con respeto.",
)

L(
    OA11, 4,
    materials="Lápiz y hojas. Los casos son inventados.",
    use="Aprenderé a cuidar la naturaleza y a actuar con reciprocidad al usar sus recursos: tomar lo necesario, pedir permiso y agradecer. Sirve para no dañar los lugares ni los saberes de otros.",
    prior=["Sé que las actividades dependen de la naturaleza.", "Sé que hay ciclos."],
    explain=[
        "Cuando usamos lo que da la naturaleza, hay que hacerlo con cuidado. Tomar solo lo necesario permite que haya para todos y para el futuro. Esto es parte de la reciprocidad: recibir y devolver. Por ejemplo, si recoges frutos, dejas algunos en el árbol.",
        "También hay lugares y recursos que tienen dueños o que están protegidos. Antes de recoger algo, hay que preguntar si se puede y quién lo cuida. No se debe tomar nada de un terreno ajeno sin permiso. Y es importante respetar las épocas del año.",
        "Podemos agradecer de muchas maneras: compartiendo parte de lo que recibimos, cuidando el agua, y reconociendo el saber de las personas que nos enseñan. Quien enseña un conocimiento merece respeto y que se diga su nombre cuando se usa lo que enseñó.",
    ],
    vocab=[("recurso", "cosa de la naturaleza que usamos"), ("lo necesario", "lo justo para vivir, ni más ni menos"), ("protegido", "cuidado para que no se dañe"), ("compartir", "dar parte de lo que se tiene"), ("terreno ajeno", "lugar que pertenece a otra persona")],
    worked=[
        W("Tomar lo necesario", "Un árbol de práctica tiene 20 frutos. Una familia necesita 12. ¿Cuántos deja en el árbol?", ["Resto lo que toma al total.", "20 − 12 = 8.", "Dejan 8 frutos."], "8 frutos"),
        W("Pedir permiso", "Un niño ve un huerto con tomates maduros en un terreno ajeno. ¿Qué hace? a) los toma b) pregunta si puede c) los pisa.", ["No es mi terreno.", "Preguntar respeta al dueño.", "Elijo preguntar."], "b"),
    ],
    mistakes=[
        M("Recoger todos los frutos del árbol.", "No quedará nada para otros ni para después.", "Deja siempre una parte."),
        M("Entrar a un terreno ajeno sin permiso.", "Puede dañar el trabajo de otros.", "Pregunta antes."),
    ],
    R=[
        ex("Tomar solo lo necesario permite que haya para todos. ¿Verdadero o falso?", "Verdadero", "Evita agotar lo que da la naturaleza."),
        ex("Antes de entrar a un terreno ajeno, ¿qué haces? A) Pedir permiso B) Entrar rápido", "A", "El terreno tiene dueño."),
        ex("Compartir es dar parte de lo que se tiene. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
    ],
    C=[
        ex("Verdadero o falso: se puede recoger todo lo que hay en un lugar.", "Falso", "Hay que dejar para otros."),
        ex("¿Qué es la reciprocidad? A) Recibir y devolver B) Tomar y guardar todo", "A", "Recibir y devolver es la reciprocidad."),
        ex("¿Por qué se respetan las épocas del año para recoger algo? A) Para que la naturaleza se recupere B) Para llegar tarde", "A", "Así hay para el futuro."),
    ],
    A=[
        arith("En un árbol de práctica hay 25 frutos. Una familia toma 15 y deja el resto. ¿Cuántos deja?", "25-15", "Se restan los que toma.", " frutos"),
        ex("Marca las acciones de respeto: a) pedir permiso b) tomar todo c) compartir d) cuidar el agua.", "a, c y d", "Pedir, compartir y cuidar el agua respetan."),
        ex("Ordena: 1) agradezco 2) pregunto si puedo recoger 3) recojo lo necesario. Escribe el orden.", "2, 3, 1", "Primero pregunto, luego recojo y al final agradezco."),
    ],
    Z=[
        ex("Tomás dice: «Si hay muchos frutos, puedo llevármelos todos». ¿Qué error comete?", "No deja para otros ni para después", "La reciprocidad pide tomar lo necesario."),
        ex("Ema usa la técnica de una artesana sin decirle nada y sin pedir permiso. ¿Qué debería hacer?", "Pedir permiso y reconocerla", "Se respeta a quien enseña."),
    ],
    D=[
        arith("Una familia de práctica comparte 4 de las 16 manzanas que recogió con una vecina. ¿Cuántas manzanas se queda?", "16-4", "Se restan las que comparte.", " manzanas"),
        ex("Dos formas de agradecer: a) compartir parte de la cosecha y b) cuidar el agua. ¿Cuántas formas de agradecer hay?", "2", "Hay dos formas distintas."),
    ],
    context=[ex("Durante una excursión, Julia ve un arbusto con frutos y quiere llevarse todos. Su profesor le dice que deje algunos. ¿Cuántos conviene dejar, algunos o ninguno?", "Algunos", "Se deja una parte para otros y para el futuro.")],
    selfcheck=[ex("¿Qué es tomar lo necesario?", "Tomar lo justo y dejar para otros", "Cuida lo que da la naturaleza."), ex("Escribe una forma de agradecer.", "Compartir o cuidar el agua", "Son ejemplos de la clase."), ex("Verdadero o falso: se puede entrar a un terreno ajeno sin avisar.", "Falso", "Hay que pedir permiso.")],
    task=T("Un árbol de práctica de Valle Alto tiene 24 frutos. Tu familia necesita 10. Escribe cuántos frutos quedan en el árbol, qué harías para agradecer y a quién pedirías permiso. Dibuja el árbol con los frutos que quedan.",
           "Quedan 14 frutos. Para agradecer, compartiría algunos con una vecina. Pediría permiso a quien cuida el árbol. Dibujo: un árbol con 14 frutos.",
           ["calcula bien los frutos que quedan", "incluye una forma de agradecer", "menciona el permiso"], ["número", "dibujo", "frases"], ["calcular mal", "olvidar el permiso"],
           "Revisar la resta 24 − 10 = 14 y las acciones de respeto."),
    reinforce="Escribe tres acciones de reciprocidad con la naturaleza.",
    extend="Escribe una regla del curso para cuidar un árbol del patio.",
)
