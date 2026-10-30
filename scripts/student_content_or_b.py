"""Cuaderno del estudiante, 1.º básico Orientación: OA 04 (autocuidado, intimidad e información personal) y OA 05 (buen trato)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA4, OA5 = "OR01 OA 04", "OR01 OA 05"

# ================================================================ OA 04
register(
    OA4, 1,
    materials="Una hoja, lápiz y las rutinas escritas en cada ejercicio; sin materiales especiales.",
    use="Aprenderé rutinas de higiene y descanso y a ordenarlas. Sirve para cuidar mi cuerpo, estar sano y tener energía para jugar y aprender.",
    prior=["Sé lavarme las manos.", "Sé que duermo de noche."],
    explain=[
        "La higiene es lavar y cuidar tu cuerpo para estar sano. Te lavas las manos con agua y jabón antes de comer y después de ir al baño. Te lavas los dientes después de comer y antes de dormir. Te bañas y te cambias de ropa para estar limpio.",
        "El descanso también cuida tu cuerpo. Los niños de tu edad necesitan dormir bastante cada noche, más o menos entre 9 y 11 horas, para tener energía, buen ánimo y poder aprender. Acostarse todos los días a una hora parecida ayuda a dormir mejor.",
        "Una rutina es una secuencia de pasos que haces siempre en el mismo orden. Por ejemplo, por la noche: comer, lavarte los dientes, ponerte pijama, leer un cuento y dormir. Las rutinas ayudan a que no se te olvide nada y a sentirte tranquilo.",
    ],
    vocab=[("higiene", "cuidar la limpieza del cuerpo"), ("descanso", "tiempo para dormir o estar tranquilo"), ("rutina", "pasos que se hacen siempre en el mismo orden"), ("secuencia", "orden de las cosas: primero, luego, al final"), ("sano", "con el cuerpo bien cuidado")],
    worked=[
        {"title": "Ordenar una rutina de mañana", "problem": "Ordena estos pasos de la mañana: A) lavarme los dientes, B) despertarme, C) tomar desayuno.", "steps": ["Primero me despierto: B.", "Luego tomo desayuno: C.", "Después me lavo los dientes: A."], "answer": "B, C, A"},
        {"title": "Cuándo lavarse las manos", "problem": "Beto va a comer su colación. ¿Qué debe hacer antes?", "steps": ["Sus manos tocaron cosas en el recreo.", "Se lava con agua y jabón.", "Luego come."], "answer": "Lavarse las manos con agua y jabón"},
    ],
    mistakes=[
        {"wrong": "Lavarse las manos solo con agua y sin jabón.", "why": "Parece que el agua basta.", "fix": "Usa agua y jabón y frota las manos."},
        {"wrong": "Dormir muy tarde porque «no tengo sueño».", "why": "Es entretenido seguir despierto.", "fix": "Haz tu rutina de la noche y acuéstate a la misma hora."},
    ],
    tiers={
        "recovery": [
            ex("¿Con qué te lavas las manos: agua y jabón o solo con la ropa?", "Agua y jabón", "El jabón saca la suciedad."),
            ex("¿Cuándo te lavas los dientes: después de comer o nunca?", "Después de comer", "Quita restos de comida."),
            ex("¿Dormir bien ayuda a tener energía?", "Sí", "El cuerpo descansa mientras dormimos."),
        ],
        "understand": [
            ex("En Orientación, ¿qué es una rutina?", "Pasos que hago siempre en el mismo orden", "Ayuda a no olvidar nada."),
            ex("¿Por qué conviene lavarse las manos antes de comer?", "Para sacar la suciedad y los gérmenes", "Así no me enfermo."),
            ex("¿Por qué conviene acostarse a una hora parecida cada día?", "Porque el cuerpo se acostumbra y duerme mejor", "Un horario regular da descanso."),
        ],
        "apply": [
            ex("Ordena la noche de Ana: A) dormir, B) lavarse los dientes, C) ponerse el pijama.", "B, C, A", "Primero dientes, luego pijama y al final dormir."),
            ex("Mía llega con las manos llenas de barro del patio y va a comer. ¿Qué debe hacer antes?", "Lavarse las manos con agua y jabón", "El barro lleva suciedad."),
            ex("Tomás se baña. ¿Qué es lo siguiente: secarse y ponerse ropa limpia, o ponerse la ropa sucia?", "Secarse y ponerse ropa limpia", "Seguir limpio es parte de la higiene."),
        ],
        "reason": [
            ex("Dani se salta el lavado de dientes de la noche «porque está cansado». ¿Por qué es mala idea?", "Porque quedan restos de comida y pueden dañar los dientes", "Los dientes se cuidan antes de dormir."),
            ex("Eva duerme 5 horas y se siente cansada en clases. ¿Qué rutina cambiaría?", "Acostarse más temprano", "Dormir más horas ayuda a descansar."),
        ],
        "challenge": [
            ex("Ordena la mañana de Pedro: A) desayunar, B) lavarse los dientes, C) despertarse, D) salir al colegio.", "C, A, B, D", "Primero despierta, luego desayuna, se lava los dientes y al final sale."),
            arith("Una rutina de higiene tiene 4 pasos y se hace 2 veces al día. ¿Cuántos pasos hace en total en un día?", "4+4", "Cuatro pasos de la mañana y cuatro de la noche."),
        ],
    },
    context=[ex("Luis llega de jugar fútbol con la cara sudada y las manos sucias. Su mamá le dice que se lave. ¿Qué dos acciones de higiene puede hacer?", "Lavarse las manos y la cara", "Quita la suciedad y el sudor.")],
    selfcheck=[ex("¿Dormir ayuda a aprender mejor?", "Sí", "Un cuerpo descansado aprende más."), ex("¿Cuándo conviene lavarse los dientes: después de comer y antes de dormir, o una vez a la semana?", "Después de comer y antes de dormir", "Así se mantienen limpios."), ex("¿Una rutina se hace en cualquier orden?", "No", "Sigue una secuencia.")],
    open_task=task("Ordena en tu hoja la rutina de la noche con estos cinco dibujos o frases: pijama, dientes, dormir, cuento, cena. Escribe 1, 2, 3, 4 y 5 en el orden en que los harías. Si tu orden es distinto al del ejemplo, explica por qué.", "1 cena, 2 dientes, 3 pijama, 4 cuento, 5 dormir.", ["usa los cinco pasos", "pone dormir al final", "explica un cambio si lo hay"], ["hoja numerada", "dibujo de los cinco pasos"], ["poner dormir antes de lavarse los dientes", "dejar pasos fuera"], "Valora el orden elegido y sugiere un horario parecido cada día."),
    reinforce="Haz hoy tu rutina de la noche en el orden de tu hoja.",
    extend="Escribe una rutina de mañana con cinco pasos para ir al colegio.",
)

register(
    OA4, 2,
    materials="Una hoja, lápiz y las listas de alimentos y actividades escritas en cada ejercicio.",
    use="Aprenderé a equilibrar alimentación, juego y movimiento. Sirve para crecer sano, tener energía y pasarlo bien.",
    prior=["Sé que debo comer y tomar agua.", "Sé jugar y moverme."],
    explain=[
        "Para cuidarte necesitas comer variado. Las frutas y las verduras, el pan, el arroz, las legumbres, el pescado, la carne, los huevos y los lácteos dan energía y ayudan a crecer. Beber agua durante el día mantiene el cuerpo bien. Los dulces y las bebidas azucaradas se disfrutan de vez en cuando, no todos los días.",
        "El cuerpo también necesita moverse. Correr, saltar, bailar, andar en bici o caminar son formas de movimiento. Los niños necesitan moverse bastante cada día. Cuando juegas al aire libre, además te diviertes, haces amigos y te relajas.",
        "Equilibrar es poner un poco de cada cosa. Si pasas muchas horas sentado frente a una pantalla, conviene parar y moverte. Si estás cansado, descansar es parte del cuidado. Un adulto de confianza te ayuda a elegir y a poner límites a las pantallas.",
    ],
    vocab=[("alimentación", "lo que como y bebo"), ("variado", "con muchas clases distintas"), ("recreación", "tiempo para jugar y divertirme"), ("movimiento", "usar el cuerpo para jugar o hacer ejercicio"), ("equilibrar", "poner un poco de cada cosa")],
    worked=[
        {"title": "Elegir una colación sana", "problem": "Ana puede elegir para su colación: un plátano o un paquete de galletas dulces. ¿Cuál es más sano para todos los días?", "steps": ["El plátano es una fruta.", "Las galletas dulces se comen de vez en cuando.", "Para todos los días conviene la fruta."], "answer": "El plátano"},
        {"title": "Equilibrar el día", "problem": "Tomás pasó dos horas viendo videos sentado. ¿Qué puede hacer después?", "steps": ["Estuvo mucho rato quieto.", "El cuerpo necesita moverse.", "Puede jugar a la pelota o saltar la cuerda."], "answer": "Moverse: jugar a la pelota o saltar la cuerda"},
    ],
    mistakes=[
        {"wrong": "Tomar solo bebida azucarada cuando se tiene sed.", "why": "Es dulce y rica.", "fix": "Cuando tengas sed, toma agua."},
        {"wrong": "Pensar que moverse es solo hacer deporte con equipo.", "why": "Se piensa en partidos.", "fix": "Caminar, bailar y saltar también son movimiento."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál es una fruta: manzana o galleta?", "Manzana", "La manzana es una fruta."),
            ex("¿Qué conviene tomar cuando tienes sed?", "Agua", "El agua hidrata el cuerpo."),
            ex("¿Bailar es una forma de movimiento?", "Sí", "Bailar mueve el cuerpo."),
        ],
        "understand": [
            ex("¿Qué quiere decir comer variado?", "Comer muchos tipos de alimentos", "Cada alimento da algo distinto al cuerpo."),
            ex("¿Por qué los niños necesitan moverse cada día?", "Para crecer fuertes y tener energía", "El movimiento fortalece el cuerpo."),
            ex("¿Para qué sirve jugar al aire libre?", "Para divertirse, moverse y relajarse", "La recreación también cuida."),
        ],
        "apply": [
            ex("Clasifica «lechuga» y «chocolate»: ¿cuál conviene todos los días?", "La lechuga", "Es una verdura."),
            ex("Mía tiene recreo. Elige una actividad de movimiento: saltar la cuerda o mirar la pared.", "Saltar la cuerda", "Es un juego que mueve el cuerpo."),
            ex("Beto quiere ver televisión por mucho rato. Escribe una pausa que puede hacer.", "Por ejemplo: estirarse o jugar un rato afuera", "Cambia la quietud por movimiento."),
        ],
        "reason": [
            ex("Luis come solo pan y dulces. ¿Qué podría agregar para comer más variado?", "Una fruta o una verdura", "Aportan algo distinto."),
            ex("Carla juega todo el día sin descansar ni comer. ¿Está equilibrada?", "No", "Falta descanso y comida."),
        ],
        "challenge": [
            ex("Pedro come variado, toma agua, juega una hora y duerme bien, pero no se lava los dientes ni las manos. ¿Qué cuidado le falta?", "La higiene", "Lavarse es parte del autocuidado."),
            ex("Una colación tiene un jugo, una manzana y un sándwich de queso. ¿Cuántas cosas hay en total?", "3", "Jugo, manzana y sándwich son tres cosas."),
        ],
    },
    context=[ex("Eva se va a un cumpleaños donde hay mucha torta y dulces. Antes comió bien en casa. ¿Qué puede hacer para equilibrar?", "Comer un poco de torta y tomar agua", "Una porción pequeña de vez en cuando está bien.")],
    selfcheck=[ex("¿Las frutas y verduras ayudan a crecer sano?", "Sí", "Aportan lo que el cuerpo necesita."), ex("¿Pasar todo el día sentado es movimiento?", "No", "Sentado no mueve el cuerpo."), ex("¿Descansar también es autocuidado?", "Sí", "El cuerpo necesita recuperarse.")],
    open_task=task("Dibuja un plato con tu comida favorita y agrega una fruta o verdura. Después dibuja o escribe una actividad de movimiento y una de descanso para hoy. Puedes elegir de esta lista: saltar, bailar, caminar, leer tranquilo, escuchar música suave.", "Plato: arroz con pollo y ensalada de lechuga. Movimiento: bailar. Descanso: leer tranquilo.", ["incluye una fruta o verdura", "incluye una actividad de movimiento", "incluye una de descanso"], ["dibujo del plato", "frases o dibujos de las dos actividades"], ["solo dulces en el plato", "dejar fuera el movimiento o el descanso"], "Reconoce el plato variado y sugiere agregar agua si falta."),
    reinforce="Elige hoy una fruta para tu colación y cuéntale a alguien por qué.",
    extend="Haz una lista de cinco juegos de movimiento y marca cuáles puedes jugar en casa.",
)

register(
    OA4, 3,
    materials="Una hoja, lápiz y los casos escritos en cada ejercicio. Lee esta clase con un adulto de confianza cerca; si algo te hace sentir mal, díselo a ese adulto.",
    use="Aprenderé que mi cuerpo es mío, que hay partes íntimas que nadie debe tocar ni mirar sin cuidado, y que puedo decir no y pedir ayuda. Sirve para estar seguro.",
    prior=["Sé que mi cuerpo es mío.", "Sé qué es un adulto de confianza."],
    explain=[
        "Las partes íntimas son las partes del cuerpo que cubre la ropa interior o el traje de baño. Son privadas. Nadie debe tocarlas, ni pedirte que las muestres o las toques, ni sacarte fotos de esas partes. Tampoco tú debes hacerlo con otros.",
        "A veces un adulto de tu familia te ayuda con tu higiene, o un doctor revisa tu salud. Eso se hace con tu familia sabiendo, en forma clara y respetuosa, y nunca es un secreto. Si algo no te gusta, puedes decir «no» y avisar a un adulto de confianza.",
        "Si alguien te toca de una manera que te incomoda o te pide guardar un secreto sobre tu cuerpo, no es tu culpa, aunque sea alguien que conoces. Tienes derecho a decir no, alejarte y contárselo a un adulto de confianza. Si el primer adulto no te escucha, cuéntale a otro hasta que te crean.",
    ],
    vocab=[("partes íntimas", "partes del cuerpo que cubre el traje de baño"), ("privado", "algo que es mío y no se muestra a todos"), ("límite", "lo que me gusta o no que hagan conmigo"), ("decir no", "decir con claridad que no quiero algo"), ("contar", "avisar a un adulto de confianza lo que me pasó")],
    worked=[
        {"title": "Una situación de límite", "problem": "Alguien le dice a Mía: «Muéstrame las partes que cubre tu traje de baño». ¿Qué debe hacer Mía?", "steps": ["Eso no está bien, porque son partes privadas.", "Mía dice «No» con voz firme.", "Se aleja y se lo cuenta a un adulto de confianza."], "answer": "Decir no, alejarse y contar a un adulto de confianza"},
        {"title": "Cuidado de salud", "problem": "En el control médico, la doctora revisa a Luis con su mamá presente y le explica lo que hace. ¿Es una situación de peligro?", "steps": ["La doctora explica y está su mamá.", "Es un cuidado de salud con un adulto conocido y nada es secreto.", "Luis puede preguntar si tiene dudas o decir si algo no le gusta."], "answer": "No es peligro; es un cuidado de salud con un adulto presente"},
    ],
    mistakes=[
        {"wrong": "Pensar que si alguien me pidió un secreto sobre mi cuerpo, debo guardarlo.", "why": "Se dice que los secretos hay que cumplirlos.", "fix": "Un secreto sobre mi cuerpo que me incomoda se cuenta."},
        {"wrong": "Pensar que fue mi culpa.", "why": "A veces los niños se sienten mal o con vergüenza.", "fix": "Nunca es tu culpa; los adultos deben cuidarte."},
    ],
    tiers={
        "recovery": [
            ex("Tu cuerpo, ¿es tuyo?", "Sí", "Cada persona es dueña de su cuerpo."),
            ex("Si alguien te incomoda, ¿puedes decir «no»?", "Sí", "Puedes decir no siempre."),
            ex("¿Debes contar a un adulto de confianza si algo te asusta?", "Sí", "Un adulto puede ayudarte."),
        ],
        "understand": [
            ex("¿Qué son las partes íntimas?", "Las partes que cubre el traje de baño", "Son partes privadas del cuerpo."),
            ex("¿Es tu culpa si alguien te toca de modo que te incomoda?", "No", "Los adultos deben cuidarte."),
            ex("¿Qué haces si el primer adulto no te escucha?", "Cuento a otro adulto de confianza", "Insistes hasta que te crean."),
        ],
        "apply": [
            ex("Un compañero le dice a Beto: «Muéstrame las partes que cubre tu ropa interior». ¿Qué hace Beto?", "Dice no, se aleja y cuenta a un adulto", "Es una petición que no corresponde."),
            ex("Ana va al médico con su papá. El médico le explica lo que va a revisar. ¿Puede preguntar si algo no entiende?", "Sí", "Tiene derecho a preguntar."),
            ex("Una persona le dice a Tomás: «Es nuestro secreto, no cuentes lo que pasó». Tomás se siente mal. ¿Qué hace?", "Lo cuenta a un adulto de confianza", "Un secreto que incomoda se cuenta."),
        ],
        "reason": [
            ex("Mía contó a su tía que alguien le pidió un secreto sobre su cuerpo, y su tía no le creyó. ¿Qué puede hacer Mía?", "Contárselo a otro adulto de confianza", "Debe seguir hasta ser escuchada."),
            ex("Dani cree que si alguien lo tocó es porque él hizo algo mal. ¿Es cierto?", "No", "El adulto debe cuidarlo."),
        ],
        "challenge": [
            arith("Eva tiene tres adultos de confianza: su mamá, su profesora y su abuela. Si el primero no la escucha, ¿cuántos más puede probar?", "3-1", "Quedan los adultos que no probó."),
            ex("Sofía se viste sola. ¿Tiene que mostrar sus partes íntimas a alguien para vestirse?", "No", "Esas partes son privadas y no se muestran."),
        ],
    },
    context=[ex("Luis está en el baño del colegio y entra alguien mayor que le dice que le muestre su cuerpo. Luis se siente asustado. ¿Qué hace?", "Dice no, sale corriendo y avisa a su profesora", "Se aleja y pide ayuda.")],
    selfcheck=[ex("¿Mi cuerpo es privado?", "Sí", "Es solo mío."), ex("¿Puedo decir no a un contacto que no quiero?", "Sí", "Tengo derecho a decir no."), ex("¿Debo guardar un secreto que me hace sentir mal?", "No", "Debo contárselo a un adulto.")],
    open_task=task("Practica con un adulto de confianza esta serie de cuatro pasos y dibújala: 1) Digo «¡No!» fuerte. 2) Me alejo. 3) Busco a un adulto de confianza. 4) Se lo cuento, y si no me escucha, se lo cuento a otro. Dibuja cada paso con una cara de Luis o de Mía, sin dibujar partes del cuerpo.", "Cuatro viñetas: Luis dice «¡No!», camina lejos, llega con su profesora, le cuenta lo que pasó.", ["dibuja los cuatro pasos", "no dibuja partes íntimas", "incluye a un adulto de confianza"], ["cuatro viñetas", "práctica dicha en voz alta"], ["omitir el paso de contar", "creer que debe guardar el secreto"], "Refuerza que siempre puede contar y que nunca es su culpa. Si el estudiante cuenta algo, aplica el protocolo del establecimiento."),
    reinforce="Repite en voz alta los cuatro pasos: decir no, alejarme, buscar un adulto, contar.",
    extend="Nombra dos adultos de tu red a quienes podrías contar algo difícil, sin escribir sus datos.",
)

register(
    OA4, 4,
    materials="Una hoja, tres lápices de colores (verde, amarillo, rojo) o tres marcas de colores y las tarjetas escritas en cada ejercicio.",
    use="Aprenderé a distinguir qué información puedo compartir y cuál debo guardar. Sirve para protegerme en el colegio, la calle y los juegos con pantalla.",
    prior=["Sé mi nombre y que hay cosas privadas.", "Sé qué es un adulto de confianza."],
    explain=[
        "La información pública es la que puedes decir a muchas personas sin riesgo, como tu nombre de pila en clase o tu comida favorita. La información privada es la que solo debe saber tu familia y los adultos que te cuidan, como tu dirección, el nombre de tu colegio, tu teléfono, tus contraseñas y las fotos de tu casa.",
        "Puedes usar un semáforo para decidir. Verde: puedo compartir. Amarillo: primero pregunto a un adulto. Rojo: no lo comparto. Tu dirección, tu contraseña y el horario en que estás solo son rojo. Tu juguete favorito puede ser verde.",
        "En internet y en los juegos con pantalla, nadie debe pedirte datos privados ni fotos tuyas. Si alguien lo hace, no respondas, sal de ahí y avisa a un adulto. Nadie se enojará contigo por contarlo.",
    ],
    vocab=[("información pública", "la que puedo decir a muchos sin riesgo"), ("información privada", "la que solo debe saber mi familia y mis cuidadores"), ("contraseña", "clave secreta que protege algo"), ("semáforo", "verde puedo, amarillo pregunto, rojo no"), ("dirección", "el lugar donde vivo")],
    worked=[
        {"title": "Clasificar con el semáforo", "problem": "Clasifica con colores: «mi color favorito» y «la clave de la tablet de mi casa».", "steps": ["El color favorito no pone en riesgo: verde.", "La clave de la tablet es privada: rojo."], "answer": "Color favorito: verde. Clave: rojo"},
        {"title": "Un desconocido pide datos", "problem": "En un juego, alguien escribe a Mía: «¿Dónde vives? Te mando un regalo». ¿Qué hace Mía?", "steps": ["La dirección es privada: rojo.", "No responde.", "Avisa a un adulto de confianza."], "answer": "No responde y avisa a un adulto"},
    ],
    mistakes=[
        {"wrong": "Compartir la contraseña con un amigo «porque es amigo».", "why": "Se confía en los amigos.", "fix": "Las contraseñas se comparten solo con tu familia."},
        {"wrong": "Responder a un desconocido para ser amable.", "why": "Parece de mala educación no contestar.", "fix": "No contestar protege; avisa a un adulto."},
    ],
    tiers={
        "recovery": [
            ex("Tu dirección, ¿es pública o privada?", "Privada", "Solo la sabe quien me cuida."),
            ex("Tu comida favorita, ¿es pública o privada?", "Pública", "Compartirla no es riesgo."),
            ex("¿Con qué color del semáforo marcas «no lo comparto»?", "Rojo", "El rojo significa no compartir."),
        ],
        "understand": [
            ex("¿Qué significa el amarillo del semáforo de datos?", "Primero pregunto a un adulto", "Es una zona de duda."),
            ex("¿Por qué no debo compartir mi contraseña?", "Porque otro podría usar mi cuenta", "La contraseña protege lo mío."),
            ex("¿Qué hago si alguien me pide datos privados por pantalla?", "No respondo y aviso a un adulto", "Es una situación de riesgo."),
        ],
        "apply": [
            ex("Clasifica «mi número de teléfono». ¿Verde, amarillo o rojo?", "Rojo", "El teléfono es privado."),
            ex("Clasifica «mi juego favorito». ¿Verde, amarillo o rojo?", "Verde", "No pone en riesgo."),
            ex("Una compañera te pide una foto tuya para su álbum privado. ¿Cuál color usas para decidir?", "Amarillo", "Primero pregunto a un adulto."),
        ],
        "reason": [
            ex("Beto cuenta a un desconocido cuándo está solo en casa. ¿Por qué es peligroso?", "Porque el desconocido sabe que no hay adultos", "Eso pone a Beto en riesgo."),
            ex("Dani dice: «Mi nombre de pila lo puedo decir en clase, pero mi dirección no». ¿Tiene razón?", "Sí", "El nombre de pila en clase no es riesgo y la dirección es privada."),
        ],
        "challenge": [
            ex("Una tarjeta dice: nombre de pila, dirección, mascota. ¿Cuántos datos son rojo?", "1", "Solo la dirección es privada."),
            ex("Tomás tiene 5 datos en su ficha: color favorito, contraseña, deporte, calle de su casa, mascota. ¿Cuántos son rojo?", "2", "Contraseña y calle son privados."),
        ],
    },
    context=[ex("En una app de juegos, un usuario escribe a Carla: «Dime tu colegio y tu calle y te regalo monedas». ¿Qué responde Carla?", "No responde y avisa a un adulto", "Colegio y calle son datos privados.")],
    selfcheck=[ex("¿La contraseña es información privada?", "Sí", "Solo la conoce mi familia."), ex("¿Puedo decir mi dirección a cualquier persona?", "No", "Es un dato privado."), ex("¿A quién aviso si alguien me pide datos?", "A un adulto de confianza", "Me ayuda a protegerme.")],
    open_task=task("Mira las seis tarjetas y pinta cada una con el color del semáforo (verde, amarillo o rojo): 1) mi juego favorito, 2) mi dirección, 3) una foto de mi casa, 4) mi dibujo del colegio, 5) la clave de mi tablet, 6) mi animal favorito. Después di en voz alta por qué pintaste una tarjeta de rojo.", "Verde: 1, 4 y 6. Rojo: 2, 3 y 5. Explico: la dirección es rojo porque dice dónde vivo.", ["clasifica las seis tarjetas", "explica un rojo", "no usa datos propios"], ["hoja con las tarjetas pintadas", "explicación oral"], ["pintar la dirección de verde", "compartir la clave"], "Reconoce lo bien clasificado y repasa la tarjeta que dudó con un ejemplo."),
    reinforce="Cuéntale a alguien de tu casa para qué sirve el semáforo de datos.",
    extend="Inventa una tarjeta amarilla y explica por qué primero preguntarías a un adulto.",
)

register(
    OA4, 5,
    materials="Una hoja, lápiz y los casos escritos en cada ejercicio.",
    use="Aprenderé un plan para protegerme: detenerme, alejarme, contar y persistir. Sirve para saber qué hacer ante una situación que me asusta o me incomoda.",
    prior=["Sé qué son partes íntimas e información privada.", "Sé quiénes son mis adultos de confianza."],
    explain=[
        "Un plan de protección son pasos que puedes seguir si algo te incomoda o te asusta. Tiene cuatro pasos: detenerme (decir «no» o «para»), alejarme (irme a un lugar seguro), contar (avisar a un adulto de confianza) y persistir (seguir contando hasta que me escuchen).",
        "Practicar el plan antes ayuda a que sea más fácil usarlo. Lo puedes ensayar con un peluche o con un adulto de confianza. Decir «no» fuerte y claro es una habilidad. También puedes pedir ayuda gritando o corriendo hacia donde hay personas.",
        "Siempre es válido pedir ayuda. Nunca eres culpable de lo que otra persona te hizo. Si algo te incomoda, aunque no sepas explicarlo bien, cuéntalo. Los adultos de confianza quieren escucharte y cuidarte.",
    ],
    vocab=[("plan de protección", "pasos para cuidarme si algo me asusta"), ("detenerme", "decir no o para"), ("alejarme", "irme a un lugar seguro"), ("persistir", "seguir intentando hasta que me escuchen"), ("lugar seguro", "donde hay personas que me cuidan")],
    worked=[
        {"title": "Aplicar los cuatro pasos", "problem": "Un compañero mayor empuja a Beto en el patio y le dice que no cuente. ¿Qué hace Beto?", "steps": ["Se detiene y dice «¡No me empujes!».", "Se aleja hacia la profesora de turno.", "Le cuenta lo que pasó."], "answer": "Detenerse, alejarse y contar a la profesora"},
        {"title": "Persistir", "problem": "Ana cuenta a un adulto, pero este está ocupado y no la escucha. ¿Qué hace?", "steps": ["Ana repite su mensaje.", "Si sigue sin respuesta, va con otro adulto de confianza.", "Sigue hasta que la escuchen."], "answer": "Insiste y cuenta a otro adulto"},
    ],
    mistakes=[
        {"wrong": "Quedarse en el lugar y esperar a que pase.", "why": "Cuesta moverse cuando uno tiene miedo.", "fix": "Alejarse hacia un lugar donde hay personas."},
        {"wrong": "Dejar de contar si el primer adulto no creyó.", "why": "Se siente desánimo.", "fix": "Cuéntalo a otro adulto de confianza."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál es el primer paso del plan: detenerme o esperar?", "Detenerme", "Digo no o para."),
            ex("¿Cuál es el segundo paso: alejarme o quedarme?", "Alejarme", "Voy a un lugar seguro."),
            ex("¿A quién cuento: a un adulto de confianza o a nadie?", "A un adulto de confianza", "Me puede ayudar."),
        ],
        "understand": [
            ex("¿Qué significa persistir?", "Seguir contando hasta que me escuchen", "No me rindo."),
            ex("¿Cuántos pasos tiene el plan de protección?", "4", "Detenerme, alejarme, contar y persistir."),
            ex("¿Es mi culpa si alguien me hace sentir mal?", "No", "Los adultos deben cuidarme."),
        ],
        "apply": [
            ex("Mía recibe un mensaje de un desconocido que le pide una foto. Elige el paso uno: no responder o enviarla.", "No responder", "Así se detiene a tiempo."),
            ex("Tomás está en la plaza y un desconocido lo invita a subir a su auto. ¿Qué hace primero?", "Dice no y se aleja corriendo hacia su familia", "Se aleja a un lugar seguro."),
            ex("Dani cuenta a su profesora que alguien lo asusta. Ella dice que lo va a revisar. ¿Qué paso del plan hizo Dani?", "Contar", "Avisó a un adulto de confianza."),
        ],
        "reason": [
            ex("Luis dice: «No cuento porque no me creerán». ¿Qué le dirías?", "Que cuente igual y si no le creen, cuente a otro", "Persistir lo protege."),
            ex("Eva se aleja pero no cuenta a nadie. ¿Está completo el plan?", "No", "Falta contar y persistir."),
        ],
        "challenge": [
            ex("Ordena el plan: A) contar, B) alejarme, C) detenerme, D) persistir.", "C, B, A, D", "Primero me detengo, luego me alejo, cuento y persisto."),
            arith("Sofía tiene tres adultos de confianza y los dos primeros no la escucharon. ¿A cuántos más puede contar?", "3-2", "Queda el adulto que no probó."),
        ],
    },
    context=[ex("En el parque, un adulto que Pedro no conoce le dice: «Ven, te muestro algo». Pedro no sabe qué hacer. ¿Qué pasos sigue?", "Dice no, se aleja hacia su familia, cuenta lo ocurrido", "Sigue el plan de protección.")],
    selfcheck=[ex("¿Decir no fuerte es una forma de protegerme?", "Sí", "Pone un límite claro."), ex("¿Puedo contar a otro adulto si el primero no me escucha?", "Sí", "Se persiste hasta ser escuchado."), ex("¿Es culpa mía si alguien me incomoda?", "No", "Nunca es culpa del niño.")],
    open_task=task("Lee el caso: «En la plaza, un joven que Mía no conoce le dice: «Ven conmigo a ver unos perritos». Dibuja cuatro viñetas con el plan: Mía dice no, se aleja hacia sus cuidadores, cuenta lo que pasó y vuelve a contar si no la entienden. Ensaya la frase «¡No, no voy contigo!» en voz alta.", "Viñeta 1: «¡No, no voy contigo!». Viñeta 2: corre hacia su papá. Viñeta 3: le cuenta. Viñeta 4: repite si hace falta.", ["dibuja los cuatro pasos", "dice la frase con claridad", "incluye a un adulto de confianza"], ["cuatro viñetas", "frase dicha en voz alta"], ["omitir el paso de contar", "quedarse en el lugar"], "Refuerza cada paso y recuerda que puede contar siempre. Si cuenta algo propio, aplica el protocolo del establecimiento."),
    reinforce="Ensaya con un peluche las palabras «No, para, me voy y voy a contar».",
    extend="Haz una tarjeta con los cuatro pasos y guárdala en tu mochila.",
)

# ================================================================ OA 05
register(
    OA5, 1,
    materials="Una hoja, lápiz y las situaciones escritas en cada ejercicio.",
    use="Aprenderé a saludar y pedir con claridad y amabilidad. Sirve para llevarme bien con otros y que me entiendan.",
    prior=["Sé saludar.", "Sé decir por favor y gracias."],
    explain=[
        "El buen trato es tratar bien a los demás. Una forma de buen trato es saludar: «Hola», «Buenos días», con la mirada y una voz amable. Saludar hace sentir bienvenida a la persona.",
        "Otra forma es pedir con claridad. En vez de decir «¡dame eso!», puedes decir «¿Me prestas el pegamento, por favor?». Es claro porque dice qué quieres, y es amable porque incluye «por favor». También se dice «gracias» y «de nada».",
        "Estas palabras tienen sentido cuando las dices de verdad. «Con permiso» sirve para pasar entre personas. «Perdón» sirve cuando sin querer molestaste. Usarlas cuida la convivencia.",
    ],
    vocab=[("saludar", "decir hola o buenos días"), ("pedir", "decir lo que necesito"), ("por favor", "palabra que hace amable un pedido"), ("gracias", "palabra para agradecer"), ("con permiso", "frase para pasar o pedir espacio")],
    worked=[
        {"title": "Pedir con claridad", "problem": "Luis necesita una tijera de su compañera Ana. ¿Qué frase es más clara y amable: «¡Dame la tijera!» o «¿Me prestas la tijera, por favor?»", "steps": ["La primera es una orden.", "La segunda dice qué necesita y pide con amabilidad."], "answer": "«¿Me prestas la tijera, por favor?»"},
        {"title": "Usar «con permiso»", "problem": "Mía quiere pasar entre dos compañeros que conversan. ¿Qué dice?", "steps": ["No los empuja.", "Dice «con permiso».", "Pasa cuando le dan espacio."], "answer": "«Con permiso»"},
    ],
    mistakes=[
        {"wrong": "Pedir con una orden: «¡Pásame eso!».", "why": "Se hace por apuro.", "fix": "Agrega «por favor» y pregunta."},
        {"wrong": "Decir «gracias» sin mirar y de mala gana.", "why": "Se repite como si fuera tarea.", "fix": "Míralo y dilo de verdad."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál es un saludo: «Buenos días» o «Dame eso»?", "«Buenos días»", "Saluda con amabilidad."),
            ex("Cuando alguien te presta algo, ¿qué dices?", "Gracias", "Agradece el gesto."),
            ex("¿Qué dices para pasar entre personas: «con permiso» o «quítense»?", "«Con permiso»", "Es una forma respetuosa."),
        ],
        "understand": [
            ex("¿Para qué sirve saludar?", "Para que la otra persona se sienta bienvenida", "Es un gesto de buen trato."),
            ex("¿Qué tiene de bueno decir «por favor»?", "Hace el pedido más amable", "El otro se siente respetado."),
            ex("¿Qué dos cosas tiene un buen pedido?", "Dice qué necesito y es amable (por favor)", "Así el otro entiende y se siente respetado."),
        ],
        "apply": [
            ex("Carla necesita el lápiz rojo de Tomás. Escribe cómo lo pide.", "Por ejemplo: «Tomás, ¿me prestas el lápiz rojo, por favor?»", "Dice qué necesita y pide con amabilidad."),
            ex("Pedro llega a la sala por la mañana. Escribe un saludo para su profesora.", "Por ejemplo: «Buenos días, profe»", "Saluda con cortesía."),
            ex("Rosa pisó sin querer el pie de Beto. Escribe qué le dice.", "Por ejemplo: «Perdón, no fue mi intención»", "Se disculpa por el accidente."),
        ],
        "reason": [
            ex("Eva dice «¡Dame agua!» y Dani no le responde. ¿Por qué podría pasar?", "Porque fue una orden poco amable", "Pedir con amabilidad ayuda a que respondan."),
            ex("Luis dice gracias mirando el piso y muy bajito, y su amigo no lo escuchó. ¿Qué podría mejorar?", "Decirlo más fuerte y mirarlo", "Que se note que lo dice de verdad."),
        ],
        "challenge": [
            ex("Dani quiere un turno en el columpio. Escribe un pedido con «por favor» y una pregunta.", "Por ejemplo: «¿Me das un turno en el columpio, por favor?»", "Incluye amabilidad y claridad."),
            ex("¿Qué es mejor para pedir ayuda: «No puedo» o «¿Me ayudas con esto, por favor?»?", "«¿Me ayudas con esto, por favor?»", "Dice qué necesita."),
        ],
    },
    context=[ex("Sofía entra a la biblioteca del curso y necesita el libro de cuentos que tiene Tomás. ¿Cómo lo pide?", "«¿Me prestas el libro de cuentos cuando termines, por favor?»", "Es claro y respeta su turno.")],
    selfcheck=[ex("¿Saludar es buen trato?", "Sí", "Muestra respeto a otros."), ex("¿Qué palabra hace amable un pedido?", "Por favor", "Muestra cortesía al pedir."), ex("¿Qué dices cuando alguien te ayuda?", "Gracias", "Reconoce su ayuda.")],
    open_task=task("Lee las tres escenas: 1) llegas a la sala por la mañana, 2) necesitas un borrador que tiene tu compañero, 3) quieres pasar entre dos niños en el pasillo. Escribe o actúa con un adulto lo que dirías en cada escena.", "1) «Buenos días». 2) «¿Me prestas el borrador, por favor?». 3) «Con permiso».", ["responde las tres escenas", "usa palabras amables", "el pedido es claro"], ["tres frases", "actuación con un adulto"], ["dar órdenes", "olvidar una escena"], "Reconoce las frases amables y ayuda a reemplazar las órdenes por preguntas."),
    reinforce="Saluda hoy a tres personas distintas con una sonrisa.",
    extend="Escribe dos formas de pedir ayuda para atarte un zapato.",
)

register(
    OA5, 2,
    materials="Una hoja, lápiz y los diálogos escritos en cada ejercicio.",
    use="Aprenderé a escuchar, esperar mi turno y mostrar que entendí al otro. Sirve para conversar bien y que todos se sientan escuchados.",
    prior=["Sé que hay turnos para hablar.", "Sé decir cómo me siento."],
    explain=[
        "Escuchar es poner atención a quien habla: miras a la persona, no la interrumpes y esperas tu turno. Cuando todos hablan a la vez nadie se entiende. Si quieres hablar, puedes levantar la mano o esperar una pausa.",
        "Una forma de mostrar que entendiste es repetir con tus palabras lo que escuchaste: «Entiendo que querías jugar a la pelota». Eso se llama reformular. Si no estás seguro, puedes preguntar: «¿Dijiste que…?».",
        "Respetar turnos no significa no hablar. Significa que todos tienen su momento. Si alguien habla mucho rato, puedes decirle con amabilidad: «¿Puedo decir algo ahora?». Y si te interrumpen, puedes decir: «Termino y te escucho».",
    ],
    vocab=[("escuchar", "poner atención a lo que otro dice"), ("turno", "momento en que me toca hablar o jugar"), ("interrumpir", "hablar cuando otro todavía no termina"), ("reformular", "repetir con mis palabras lo que entendí"), ("pausa", "momento corto de silencio")],
    worked=[
        {"title": "Reformular", "problem": "Ana dice: «Quiero jugar con el tren, pero Beto lo tiene hace rato». ¿Cómo reformula Luis?", "steps": ["Luis repite lo esencial.", "Dice: «Entiendo que quieres jugar con el tren y Beto lo tiene hace rato».", "Así muestra que escuchó."], "answer": "«Entiendo que quieres el tren y Beto lo tiene hace rato»"},
        {"title": "Esperar el turno", "problem": "Mía quiere hablar, pero Tomás todavía no termina. ¿Qué hace?", "steps": ["No lo interrumpe.", "Levanta la mano o espera una pausa.", "Habla cuando termina."], "answer": "Esperar su turno"},
    ],
    mistakes=[
        {"wrong": "Hablar encima de otra persona.", "why": "Se tienen muchas ganas de contar algo.", "fix": "Espera una pausa o levanta la mano."},
        {"wrong": "Repetir exactamente las mismas palabras sin entender.", "why": "Se copia lo escuchado.", "fix": "Dilo con tus palabras para mostrar que entendiste."},
    ],
    tiers={
        "recovery": [
            ex("Para escuchar, ¿miras a la persona o miras para otro lado?", "Miro a la persona", "Es una señal de atención."),
            ex("¿Interrumpir es esperar el turno?", "No", "Interrumpir es hablar antes de que el otro termine."),
            ex("¿Qué haces para pedir la palabra: levantar la mano o gritar?", "Levantar la mano", "Respeta el turno."),
        ],
        "understand": [
            ex("¿Qué es reformular?", "Repetir con mis palabras lo que entendí", "Muestra que escuché."),
            ex("¿Por qué conviene esperar el turno?", "Para que todos se escuchen", "Así nadie queda sin hablar."),
            ex("¿Qué haces si no estás seguro de lo que oíste?", "Pregunto: «¿Dijiste que…?»", "Confirmo antes de responder."),
        ],
        "apply": [
            ex("Dani dice: «Me enojé porque me quitaron la pelota». Reformula con «Entiendo que…».", "«Entiendo que te enojaste porque te quitaron la pelota»", "Repite lo esencial con otras palabras."),
            ex("Eva quiere hablar y Luis sigue contando. Escribe una frase amable para pedir su turno.", "«¿Puedo decir algo ahora?»", "Pide turno sin interrumpir."),
            ex("Carla dice: «Mi abuela me trajo un dibujo». Escribe una pregunta para saber más.", "Por ejemplo: «¿Qué dibujo era?»", "Muestra interés en lo que dijo."),
        ],
        "reason": [
            ex("Pedro respondió sin escuchar y dijo algo que no tenía que ver. ¿Qué debió hacer antes de responder?", "Escuchar y reformular", "Así entiende lo que dijo el otro."),
            ex("Sofía dice: «Todos hablan a la vez en mi grupo y nadie entiende». ¿Qué regla ayudaría?", "Hablar de a uno por turno", "Así todos se escuchan."),
        ],
        "challenge": [
            arith("Tres niños quieren hablar en el grupo. Si cada uno habla 1 minuto y esperan en orden, ¿cuántos minutos pasan en total?", "1+1+1", "Un minuto por cada niño."),
            ex("Rosa interrumpió a Tomás sin querer. ¿Qué frase repara: «Perdón, sigue tú» o ignorarlo?", "«Perdón, sigue tú»", "Reconoce y devuelve el turno."),
        ],
    },
    context=[ex("En la ronda del curso habla Mía sobre su paseo. Beto quiere contar su paseo también. ¿Qué hace?", "Espera su turno y escucha a Mía", "Respeta a quien habla.")],
    selfcheck=[ex("¿Escuchar incluye mirar a quien habla?", "Sí", "Demuestra atención real."), ex("¿Puedo hablar cuando otro todavía habla?", "No", "Eso es interrumpir al otro."), ex("¿Qué frase muestra que entendí?", "«Entiendo que…»", "Reformula con mis palabras.")],
    open_task=task("Practica en pareja con un adulto o un compañero. Uno cuenta en dos frases qué hizo ayer (puede ser inventado, por ejemplo: «Fui a la plaza y jugué con la pelota»). El otro escucha sin interrumpir y dice «Entiendo que…». Después cambian de turno.", "A: «Fui a la plaza y jugué con la pelota». B: «Entiendo que fuiste a la plaza y jugaste con la pelota».", ["escucha sin interrumpir", "reformula con «Entiendo que…»", "cambian de turno"], ["práctica en pareja", "dibujo de los dos turnos"], ["interrumpir", "repetir palabra por palabra sin entender"], "Destaca el respeto del turno y propone mejorar la frase de reformulación."),
    reinforce="Escucha a alguien hoy hasta que termine y di «Entiendo que…».",
    extend="Escribe una regla de tres frases para hablar de a uno en tu grupo.",
)

register(
    OA5, 3,
    materials="Una hoja, lápiz y las situaciones escritas en cada ejercicio.",
    use="Aprenderé a cuidar mis cosas, las de otros y las del curso, y a seguir rutinas. Sirve para que el salón esté ordenado y todos puedan trabajar tranquilos.",
    prior=["Sé qué es mío y qué es de otros.", "Sé guardar mis útiles."],
    explain=[
        "Cuidar pertenencias es tratar bien lo que es tuyo, lo que es de otros y lo que es de todos, como los libros de la biblioteca de aula. Se cuida guardando las cosas en su lugar, usándolas con cuidado y avisando si algo se rompe.",
        "Si pides algo prestado, lo devuelves en buen estado y a tiempo. Si se te pierde o rompe sin querer, lo dices y ayudas a arreglarlo. Eso es responsabilidad. Las pertenencias son cuidadas por quienes las usan.",
        "Las rutinas del curso también son una forma de buen trato. Por ejemplo: dejar la silla en su lugar, guardar los materiales al final de la clase y ayudar a ordenar. Cuando todos cumplen una parte, la tarea se hace más rápida y fácil.",
    ],
    vocab=[("pertenencia", "algo que es de una persona"), ("responsabilidad", "hacerme cargo de lo que me toca"), ("prestar", "dejar algo mío por un tiempo"), ("devolver", "dar de vuelta lo que pedí prestado"), ("rutina", "pasos que se repiten siempre")],
    worked=[
        {"title": "Devolver con cuidado", "problem": "Luis pidió prestada una goma a Ana y se le ensució. ¿Qué hace?", "steps": ["Le cuenta a Ana.", "La limpia como puede.", "Se la devuelve y se disculpa."], "answer": "Contar, limpiar y devolver con disculpa"},
        {"title": "Cuidar lo de todos", "problem": "Un libro de la biblioteca del curso tiene la tapa suelta. Mía lo nota. ¿Qué hace?", "steps": ["No lo rompe más.", "Avisa a la profesora.", "Ayuda a arreglarlo si puede."], "answer": "Avisar a la profesora"},
    ],
    mistakes=[
        {"wrong": "Dejar los materiales en el suelo al terminar.", "why": "Se tiene apuro por salir.", "fix": "Guárdalos antes de irte."},
        {"wrong": "Esconder que algo se rompió.", "why": "Da miedo que me reten.", "fix": "Cuéntalo, es la forma de arreglarlo."},
    ],
    tiers={
        "recovery": [
            ex("Si algo se rompe sin querer, ¿lo cuentas o lo escondes?", "Lo cuento", "Se puede arreglar."),
            ex("¿Dónde guardas tus útiles al terminar?", "En su lugar", "Así se encuentran y no se pierden."),
            ex("¿Devuelves lo prestado en buen estado?", "Sí", "Es una forma de responsabilidad."),
        ],
        "understand": [
            ex("¿Qué es una pertenencia?", "Algo que es de una persona", "Puede ser mío o de otro."),
            ex("¿Por qué hay que cuidar lo que es de todos?", "Porque lo usamos entre todos", "Si se daña, nadie puede usarlo."),
            ex("¿Qué haces si pierdes algo que te prestaron?", "Aviso y ayudo a buscarlo o arreglarlo", "Así me hago cargo."),
        ],
        "apply": [
            arith("Al terminar la clase de arte quedan 6 lápices fuera de su caja. Si Dani guarda 2 y Eva guarda 3, ¿cuántos faltan por guardar?", "6-2-3", "Se quitan los que ya guardaron."),
            ex("Tomás ve el estuche de Carla en el suelo. ¿Qué hace: lo pisa, lo deja ahí o lo levanta y se lo avisa?", "Lo levanta y se lo avisa", "Cuida lo de otra persona."),
            ex("Pedro pidió un cuaderno prestado. ¿Cuándo lo devuelve: cuando termine de usarlo o nunca?", "Cuando termine de usarlo", "Lo prestado se devuelve."),
        ],
        "reason": [
            ex("Rosa dejó la silla fuera del puesto y Beto se tropezó. ¿Por qué es importante dejarla en su lugar?", "Para evitar tropezones", "Un salón ordenado es más seguro."),
            ex("Sofía rompió sin querer una regla de plástico del curso y lo contó. ¿Qué mostró?", "Responsabilidad", "Se hizo cargo."),
        ],
        "challenge": [
            arith("Hay 3 grupos con 2 niños cada uno. Si cada niño guarda 1 material, ¿cuántos materiales se guardan?", "2+2+2", "Dos niños por cada uno de los tres grupos."),
            ex("Ana dice: «No me toca ordenar, lo hará otro». ¿Qué le dirías?", "Que todos ayudan a ordenar", "Entre todos se hace más rápido."),
        ],
    },
    context=[ex("Al final de la clase hay hojas y lápices sobre las mesas. La profesora dice: «Cada uno ordena lo que usó». Luis ordena sus lápices y también recoge una hoja del suelo. ¿Qué mostró?", "Responsabilidad y cuidado del salón", "Cuidó lo suyo y lo de todos.")],
    selfcheck=[ex("¿Debo cuidar mis cosas y las de otros?", "Sí", "Es una forma de buen trato."), ex("¿Qué hago si rompo algo sin querer?", "Lo cuento y ayudo a arreglarlo", "Me hago cargo."), ex("¿Una rutina del curso ayuda a todos?", "Sí", "Se trabaja más tranquilo.")],
    open_task=task("Mira estas cinco rutinas del curso y marca las que cumples hoy con una cruz: guardar mis útiles, dejar mi silla en su lugar, devolver lo prestado, avisar si algo se rompe, ayudar a ordenar. Elige una que quieras mejorar y dibuja cómo la harás mañana.", "Marco guardar mis útiles y devolver lo prestado. Quiero mejorar: ayudar a ordenar. Dibujo: yo juntando los lápices.", ["marca las rutinas que cumple", "elige una para mejorar", "dibuja la mejora"], ["hoja con cruces", "dibujo de la mejora"], ["marcar todas sin pensar", "no elegir ninguna"], "Reconoce lo que ya cumple y ayuda a hacer la mejora concreta."),
    reinforce="Revisa que tu mochila y tus útiles estén en su lugar.",
    extend="Escribe tres reglas para cuidar los libros de la biblioteca del curso.",
)

register(
    OA5, 4,
    materials="Una hoja, lápiz y las situaciones escritas en cada ejercicio.",
    use="Aprenderé a compartir y a ayudar sin imponer. Sirve para colaborar, hacer amigos y respetar lo que el otro quiere.",
    prior=["Sé qué es compartir.", "Sé ofrecer ayuda."],
    explain=[
        "Compartir es dejar que otro use algo mío o usar algo juntos. Se puede compartir un juego, un lápiz o un espacio en la mesa. Compartir es una decisión: nadie está obligado a compartir todo, pero es amable cuando se puede.",
        "Ayudar sin imponer es ofrecer ayuda en vez de obligar. Dices: «¿Quieres que te ayude?» y aceptas lo que responda el otro. Si dice «no», lo respetas. Si dice «sí», preguntas cómo quiere que lo ayudes.",
        "Hay compartir y ayudar que alegran, y hay otros que molestan. Quitar algo «para ayudar» o forzar a alguien a compartir su juguete no es buen trato. Un apoyo que admite respuesta deja que el otro decida.",
    ],
    vocab=[("compartir", "usar o dar algo en común"), ("ayudar", "colaborar para que alguien lo logre"), ("imponer", "obligar sin preguntar"), ("respuesta", "lo que el otro decide"), ("turnarse", "usar uno después de otro")],
    worked=[
        {"title": "Compartir con turnos", "problem": "Hay una sola pelota para Ana y Beto. ¿Cómo comparten?", "steps": ["Se turnan: primero uno, luego el otro.", "Acuerdan cuánto tiempo.", "Así los dos juegan."], "answer": "Se turnan con la pelota"},
        {"title": "Ofrecer sin imponer", "problem": "Mía ve que Luis no puede abrir su lonchera. ¿Qué dice?", "steps": ["No se la quita.", "Pregunta: «¿Quieres que te ayude?».", "Espera la respuesta."], "answer": "«¿Quieres que te ayude?»"},
    ],
    mistakes=[
        {"wrong": "Obligar a alguien a compartir su juguete.", "why": "Creemos que compartir es una obligación.", "fix": "Pídelo con amabilidad y acepta si dicen no."},
        {"wrong": "Hacer la tarea de otro «para ayudar».", "why": "Se piensa que así es más rápido.", "fix": "Ofrece ayuda y deja que el otro la haga."},
    ],
    tiers={
        "recovery": [
            ex("¿Turnarse es una forma de compartir?", "Sí", "Cada uno usa el juego un rato."),
            ex("¿Preguntar «¿quieres que te ayude?» es imponer?", "No", "Deja que el otro decida."),
            ex("Si alguien dice no a tu ayuda, ¿insistes?", "No", "Se respeta su respuesta."),
        ],
        "understand": [
            ex("¿Qué es ayudar sin imponer?", "Ofrecer ayuda y aceptar la respuesta", "El otro elige."),
            ex("¿Por qué no se debe quitar algo «para ayudar»?", "Porque el otro no pudo decidir", "Quitarlo es imponer."),
            ex("¿Es obligatorio compartir todo lo mío?", "No", "Compartir es una decisión."),
        ],
        "apply": [
            ex("Dani y Rosa quieren el mismo columpio. Escribe un acuerdo con turnos.", "Por ejemplo: «Tú te meces 10 veces y luego yo»", "Define un orden claro."),
            ex("Eva tiene dos galletas y Tomás ninguna. Ella decide compartir y da una a Tomás. ¿Cuántas galletas tiene cada uno ahora?", "1", "Cada uno tiene una galleta."),
            ex("Pedro ve que Sofía no alcanza el libro del estante. Escribe una frase para ofrecer ayuda.", "Por ejemplo: «¿Quieres que te lo alcance?»", "Ofrece sin quitar."),
        ],
        "reason": [
            ex("Carla armó el rompecabezas de Beto sin preguntar. Beto se puso triste. ¿Por qué?", "Porque no pudo hacerlo él", "Ayudar sin permiso fue imponer."),
            ex("Luis no quiere prestar su juguete nuevo hoy. ¿Está mal?", "No", "Puede decidir cuándo compartir."),
        ],
        "challenge": [
            ex("Hay 6 bloques para Ana y Mía. Los reparten uno a una, por turnos, hasta que no quedan. ¿Cuántos bloques recibe cada una?", "3", "Reparten uno a una: cada niña recibe 3."),
            ex("Una niña dice «no, gracias» a tu ayuda. Luego dice «sí, ahora sí». ¿Puedes ayudar?", "Sí", "Ella cambió de decisión."),
        ],
    },
    context=[ex("En el patio hay un solo balde y dos niños que quieren hacer castillos de arena. Ana dice: «Yo lo uso primero y luego tú». ¿Qué hizo?", "Propuso turnos", "Es una forma de compartir.")],
    selfcheck=[ex("¿Compartir es una decisión?", "Sí", "Nadie obliga a compartir todo."), ex("¿Cómo se ofrece ayuda?", "Preguntando", "El otro responde."), ex("¿Qué es turnarse?", "Usar uno después de otro", "Así todos tienen su momento.")],
    open_task=task("Lee el caso: «Tomás tiene un juego de bloques y Mía quiere usarlos. Beto está tratando de armar una torre con otros bloques y no logra que se sostenga. Ana lo mira». Escribe o di una frase para que Mía pida compartir, una frase para que Ana ofrezca ayuda a Beto, y qué hace Mía si Tomás dice que hoy no.", "Mía: «¿Me prestas los bloques un rato?». Ana: «¿Quieres que te ayude con la torre?». Si Tomás dice no: «Está bien, juego con otra cosa».", ["pide compartir con amabilidad", "ofrece ayuda sin imponer", "respeta un no"], ["tres frases", "dibujo con globos"], ["quitar el juguete", "ayudar sin preguntar"], "Reconoce las frases amables y ayuda a cambiar las que obligan."),
    reinforce="Ofrece hoy ayuda a alguien, preguntando primero.",
    extend="Escribe un acuerdo de turnos para usar un juego entre tres niños.",
)

register(
    OA5, 5,
    materials="Una hoja, lápiz y los casos escritos en cada ejercicio.",
    use="Aprenderé a reparar una relación después de hacer daño: reconocerlo, pedir perdón y hacer algo para arreglarlo. Sirve para volver a llevarme bien.",
    prior=["Sé decir perdón.", "Sé que mis acciones afectan a otros."],
    explain=[
        "A veces, sin querer o queriendo, hacemos daño a alguien. Reparar el vínculo es volver a cuidar la relación. No basta con decir «perdón» rápido; también es importante reconocer qué pasó y hacer algo para arreglarlo.",
        "Una buena disculpa tiene tres partes: 1) digo qué hice («te empujé»), 2) digo cómo creo que te sentiste («te dolió y te enojaste»), 3) propongo una acción para reparar («te ayudo a levantarte y no lo vuelvo a hacer»). Así la otra persona se siente tomada en cuenta.",
        "La otra persona puede aceptar tu disculpa o necesitar un tiempo. Eso se respeta. Cuando alguien te pide perdón, también puedes decir cómo te sentiste. Reparar es un trabajo de dos, y se puede hacer con ayuda de un adulto.",
    ],
    vocab=[("reparar", "arreglar un daño"), ("disculpa", "palabras para reconocer un daño y pedir perdón"), ("reconocer", "decir con sinceridad qué hice"), ("acción reparadora", "algo que hago para arreglar el daño"), ("vínculo", "la relación entre dos personas")],
    worked=[
        {"title": "Una disculpa de tres partes", "problem": "Luis rompió sin querer el dibujo de Ana. Arma su disculpa.", "steps": ["Qué hice: «Rompí tu dibujo».", "Cómo te sentiste: «Te pusiste triste».", "Cómo reparo: «Te ayudo a hacer otro»."], "answer": "«Rompí tu dibujo, te pusiste triste, te ayudo a hacer otro»"},
        {"title": "Aceptar con tiempo", "problem": "Mía pide perdón a Beto, pero Beto dice que aún está enojado. ¿Qué hace Mía?", "steps": ["Respeta que Beto necesita tiempo.", "Le dice: «Estaré aquí cuando quieras».", "No insiste ni se enoja."], "answer": "Respetar el tiempo de Beto"},
    ],
    mistakes=[
        {"wrong": "Decir «perdón» sin reconocer qué pasó.", "why": "Se quiere terminar rápido.", "fix": "Dilo con tres partes: lo que hice, lo que sentiste, lo que haré."},
        {"wrong": "Esperar que el otro perdone enseguida.", "why": "Creemos que decir perdón arregla todo.", "fix": "Da tiempo al otro."},
    ],
    tiers={
        "recovery": [
            ex("Si empujas sin querer a un compañero, ¿qué dices?", "Perdón", "Reconoce el daño."),
            ex("¿Qué hace una acción reparadora: arregla el daño o lo ignora?", "Arregla el daño", "Busca remediar lo ocurrido."),
            ex("¿Debes esperar que te perdonen enseguida?", "No", "Cada uno necesita su tiempo."),
        ],
        "understand": [
            ex("¿Cuáles son las tres partes de una buena disculpa?", "Qué hice, cómo se sintió, cómo reparo", "Cada parte cuenta."),
            ex("¿Por qué no basta con decir solo «perdón»?", "Porque no reconoce qué pasó ni repara", "Falta una acción concreta."),
            ex("¿Qué haces si el otro aún está enojado?", "Respetar su tiempo", "Así no lo presiono."),
        ],
        "apply": [
            ex("Dani rompió el lápiz de Eva. Escribe qué hizo, en la primera parte de su disculpa.", "«Rompí tu lápiz»", "Reconoce lo que hizo."),
            ex("Tomás empujó a Carla en la fila. Escribe una acción reparadora.", "Por ejemplo: «Te ayudo a levantarte y espero mi turno»", "Arregla el daño."),
            ex("Rosa llegó tarde y tapó la vista de su compañero. Escribe cómo reconoce lo que hizo.", "«Tapé tu vista»", "Dice qué hizo."),
        ],
        "reason": [
            ex("Pedro dijo «perdón» y siguió haciendo lo mismo. ¿Por qué no repara?", "Porque no cambió su acción", "Reparar es también cambiar."),
            ex("Sofía le dijo a Beto: «Perdón, me burlé de tu dibujo, te sentiste mal. Voy a decirte lo que me gustó». ¿Tiene las tres partes?", "Sí", "Dice qué hizo, cómo se sintió y qué hará."),
        ],
        "challenge": [
            ex("Luis y Ana discutieron y los dos hicieron daño. ¿Quién debe reparar?", "Los dos", "Cada uno reconoce lo suyo."),
            ex("Ordena una disculpa: A) cómo reparo, B) qué hice, C) cómo te sentiste.", "B, C, A", "Primero qué hice, luego cómo se sintió y al final reparar."),
        ],
    },
    context=[ex("Mía le quitó el juguete a Beto y él lloró. Mía dice: «Te quité el juguete, te pusiste triste. Te lo devuelvo y juguemos juntos». ¿Qué parte es la acción reparadora?", "Te lo devuelvo y juguemos juntos", "Es lo que hace para arreglar.")],
    selfcheck=[ex("¿Una disculpa tiene tres partes?", "Sí", "Qué hice, qué sintió el otro y cómo reparo."), ex("¿Puede el otro necesitar tiempo?", "Sí", "Se respeta su tiempo."), ex("¿Decir solo perdón basta siempre?", "No", "Falta reconocer y reparar.")],
    open_task=task("Lee el caso: «Ana tiró sin querer la torre de bloques de Luis». Escribe o di una disculpa de tres partes para Ana: qué hizo, cómo se sintió Luis y qué hará para arreglarlo. Puedes elegir esta acción reparadora u otra: ayudar a armar la torre de nuevo.", "«Tiré tu torre. Creo que te pusiste triste. Te ayudo a armarla de nuevo».", ["incluye las tres partes", "propone una acción posible", "no culpa a la otra persona"], ["disculpa dicha o escrita", "dibujo de la reparación"], ["decir solo perdón", "culpar a Luis"], "Reconoce cada parte y recuerda que reparar es cuidar la relación."),
    reinforce="Repite la disculpa de tres partes con un peluche.",
    extend="Escribe una situación en que alguien hizo daño sin querer y cómo podría repararlo.",
)
