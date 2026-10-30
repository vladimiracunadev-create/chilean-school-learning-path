"""Student material for 1.º básico Inglés, EN01 OA 05 (respuesta personal y creativa a lo escuchado) y OA 06 (leer cuentos, rimas, tarjetas, instrucciones e información).

Las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado.
Las lecturas del OA 06 están escritas completas en cada ejercicio.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA5, OA6 = "EN01 OA 05", "EN01 OA 06"
ADULT = "Un adulto lee en voz alta (el estudiante tapa el guion): "


# ---------------------------------------------------------------- OA 05
register(
    OA5, 1,
    materials="Los textos cortos escritos en cada ejercicio, que lee un adulto; lápiz y papel.",
    use="Aprenderé a relacionar lo que escucho en inglés con mis propias experiencias, de forma segura. Sirve para darle sentido personal a lo que oigo.",
    prior=["Sé qué es una mascota y qué es una fiesta.", "Sé decir «I like» y «I have»."],
    explain=[
        "Cuando escuchas un texto, puedes pensar en tu propia vida. Si el adulto lee «I have a dog», puedes recordar a tu perro, o a un perro que viste, o decir que te gustaría tener uno. Conectar con lo que vives ayuda a recordar y a entender.",
        "Para conectar de forma segura, no necesitas contar cosas privadas. Basta decir algo general: «I like dogs» (me gustan los perros) o «I have a cat» (tengo un gato). Elige lo que quieras compartir; nadie te obliga a decir más.",
        "Una buena manera de empezar es usar una frase corta: «Me too» (yo también), «I like it» (me gusta) o «I don't have a dog» (no tengo un perro). Con eso muestras que escuchaste y piensas en tu propia experiencia.",
    ],
    vocab=[("I like", "me gusta"), ("I have", "yo tengo"), ("me too", "yo también"), ("I don't have", "yo no tengo"), ("dog", "perro"), ("cat", "gato")],
    worked=[
        {"title": "Conectar con una frase", "problem": ADULT + "«I have a dog. I like my dog.» ¿Qué puedes decir tú si tienes un perro?", "steps": ["Escucho I have a dog.", "Pienso en mi experiencia.", "Puedo decir Me too."], "answer": "Me too"},
        {"title": "Decir que no tengo", "problem": "Si no tienes perro, ¿cómo lo dices en inglés?", "steps": ["Uso I don't have.", "Agrego a dog."], "answer": "I don't have a dog"},
    ],
    mistakes=[
        {"wrong": "Pensar que hay que contar mucho de mi vida privada.", "why": "Se confunde conectar con contar todo.", "fix": "Di algo corto y general, como I like dogs."},
        {"wrong": "Decir «Me too» cuando no es verdad.", "why": "Se quiere repetir a los demás.", "fix": "Di lo que sientes: I like it o I don't have a dog."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«I like pizza.» ¿Qué le gusta a la persona?", "La pizza", "I like es me gusta."),
            ex(ADULT + "«I have a cat.» ¿Qué tiene la persona?", "Un gato", "Cat es gato."),
            ex(ADULT + "«I like apples.» ¿Qué le gusta?", "Las manzanas", "Apples son manzanas."),
        ],
        "understand": [
            ex("¿Qué significa «me too»?", "yo también", "Se usa cuando algo también es verdad para mí."),
            ex("¿Qué puedes decir si no tienes mascota?", "I don't have a pet", "Don't have es no tengo."),
            ex("¿Es obligatorio contar cosas privadas para conectar?", "No", "Basta con una frase corta y general."),
        ],
        "apply": [
            ex(ADULT + "«I like blue.» Responde que a ti también te gusta el azul.", "Me too", "Es la forma corta de decir yo también."),
            ex(ADULT + "«I have a dog.» Si tú no tienes perro, ¿qué dices: «Me too» o «I don't have a dog»?", "I don't have a dog", "Es lo que es verdad para ti."),
            ex(ADULT + "«I like the park.» Escribe en inglés una frase tuya sobre un lugar que te gusta.", "Por ejemplo: I like the beach", "I like más un lugar."),
        ],
        "reason": [
            ex("¿Por qué decir «Me too» solo cuando es verdad?", "Porque muestro lo que realmente pienso", "La respuesta debe ser mía."),
            ex("Un niño no quiere contar sobre su casa. ¿Qué frase general puede usar?", "I like dogs", "Es corta y no entrega datos privados."),
        ],
        "challenge": [
            ex("Escribe una frase en inglés con «I like» y un animal.", "Por ejemplo: I like cats", "I like más un animal."),
            ex("Escribe dos frases: una con «I have» y otra con «I don't have» sobre una mascota.", "Por ejemplo: I have a fish. I don't have a dog.", "Contrasta lo que hay y lo que no hay."),
        ],
    },
    context=[ex(ADULT + "«A: I like ice cream. B: ...» Tu amigo dice esto en el recreo y a ti también te gusta. ¿Qué dices?", "Me too", "Es la forma corta de decir yo también.")],
    selfcheck=[
        ex("¿Qué significa «I like»?", "me gusta", "Es la frase para decir un gusto."),
        ex("¿Cómo se dice «yo tengo un gato»?", "I have a cat", "I have más cat."),
        ex("¿Cómo dices que algo no te gusta?", "I don't like it", "Don't like es no me gusta."),
    ],
    open_task=task("Un adulto lee: «I like dogs. I like the park. I have a ball.» Escribe o di tres frases tuyas con «I like» o «I have» sobre cosas que quieras compartir, por ejemplo con animales, lugares o juguetes.", "I like cats. I like the beach. I have a doll.", ["tres frases con I like o I have", "cosas generales", "frases correctas en inglés"], ["frases escritas o dichas", "nota del adulto"], ["contar datos privados", "decir I likes"], "Resalta lo que dijo con claridad y corrige con suavidad si algo no está bien."),
    reinforce="Di «I like» y tres cosas que te gusten, en inglés.",
    extend="Escribe cinco cosas que te gustan y cinco que no, con «I like» y «I don't like».",
)

register(
    OA5, 2,
    materials="Los textos y consignas escritos en cada ejercicio, que lee un adulto; hojas, lápices de colores.",
    use="Aprenderé a mostrar lo que entendí dibujando. Sirve para responder sin hablar mucho y para crear mi propia versión.",
    prior=["Sé algunos colores y animales en inglés.", "Sé dibujar formas simples."],
    explain=[
        "Dibujar es una forma de responder a lo que escuchas. Si el adulto lee «The sun is yellow and the sky is blue», tu dibujo muestra un sol amarillo y un cielo azul. Así demuestras que entendiste, aunque no hables.",
        "Para dibujar bien, escucha las palabras clave: personajes, colores, objetos y lugares. Dibuja primero lo que oíste y luego puedes agregar algo tuyo, como una nube o una flor. Lo importante es que no cambie lo que dijo el texto.",
        "Cuando termines, rotula tu dibujo con una o dos palabras en inglés: sun, sky, tree. Rotular es escribir el nombre al lado de lo que dibujaste. Muestra qué palabras conoces.",
    ],
    vocab=[("draw", "dibujar"), ("sun", "sol"), ("sky", "cielo"), ("flower", "flor"), ("label", "rotular, escribir el nombre"), ("my picture", "mi dibujo")],
    worked=[
        {"title": "Dibujar lo que oigo", "problem": ADULT + "«The sun is yellow. The sky is blue.» ¿Qué dibujas?", "steps": ["Dibujo un sol amarillo.", "Dibujo el cielo azul."], "answer": "Sol amarillo y cielo azul"},
        {"title": "Rotular el dibujo", "problem": "Dibujaste un sol y un árbol. ¿Qué palabras escribes?", "steps": ["Sol se dice sun.", "Árbol se dice tree."], "answer": "sun y tree"},
    ],
    mistakes=[
        {"wrong": "Dibujar algo distinto de lo que dice el texto.", "why": "Se deja llevar por la imaginación.", "fix": "Primero dibuja lo que oíste y después agrega algo tuyo."},
        {"wrong": "No rotular el dibujo.", "why": "Se cree que el dibujo basta.", "fix": "Escribe una o dos palabras en inglés."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«A red flower.» ¿Qué dibujas?", "Una flor roja", "Flower es flor y red es rojo."),
            ex(ADULT + "«A big sun.» ¿Qué dibujas?", "Un sol grande", "Sun es sol y big es grande."),
            ex(ADULT + "«A green tree.» ¿Qué dibujas?", "Un árbol verde", "Tree es árbol."),
        ],
        "understand": [
            ex("¿Para qué sirve rotular un dibujo?", "Para mostrar qué palabras en inglés conozco", "Escribir el nombre da evidencia."),
            ex("¿Qué dibujas primero: lo que oíste o algo tuyo?", "Lo que oí", "Primero se muestra comprensión."),
            ex("¿Qué significa «sky»?", "cielo", "Está arriba de nosotros."),
        ],
        "apply": [
            ex(ADULT + "«The sky is blue and the sun is yellow.» ¿De qué color pintas el sol?", "Amarillo", "Yellow es amarillo."),
            ex(ADULT + "«A cat is under a tree.» ¿Dónde dibujas al gato?", "Debajo del árbol", "Under es debajo."),
            ex(ADULT + "«Two flowers are red and one is yellow.» ¿Cuántas flores dibujas?", "3", "Dos rojas y una amarilla suman tres."),
        ],
        "reason": [
            ex("Un niño dibujó un sol azul cuando el texto decía «yellow sun». ¿Qué debe cambiar?", "El color del sol a amarillo", "Yellow significa amarillo."),
            ex("¿Por qué un dibujo puede mostrar comprensión?", "Porque se parece a lo que dice el texto", "Es una evidencia sin hablar."),
        ],
        "challenge": [
            ex(ADULT + "«A big green tree. A small red bird is on the tree. The sun is yellow.» ¿Cuántos elementos principales dibujas?", "3", "Árbol, pájaro y sol."),
            ex("Escribe tres rótulos en inglés para un dibujo con un sol, un árbol y una flor.", "sun, tree, flower", "Son los nombres en inglés."),
        ],
    },
    context=[ex(ADULT + "«My house is red. It has a big yellow door. There is a green tree.» Es la clase de artes y debes dibujar esto. ¿De qué color es la puerta?", "Amarilla", "Yellow door es puerta amarilla.")],
    selfcheck=[
        ex("¿Qué significa «draw»?", "dibujar", "Es una forma de responder."),
        ex(ADULT + "«A blue fish.» ¿Qué dibujas?", "Un pez azul", "Fish es pez."),
        ex("¿Cómo se dice «flor» en inglés?", "flower", "Flower es flor."),
    ],
    open_task=task("Un adulto lee dos veces: «The sky is blue. The sun is yellow. There is a green tree. A small red bird is on the tree.» Dibuja la escena, rotula tres cosas en inglés (sun, tree, bird) y agrega una flor inventada por ti.", "Dibujo con cielo azul, sol amarillo, árbol verde y pájaro rojo pequeño sobre él; rótulos sun, tree, bird; una flor extra.", ["incluye los 4 elementos del texto", "colores correctos", "tres rótulos en inglés", "agrega algo propio"], ["dibujo", "nota del adulto"], ["pájaro grande o de otro color", "rótulos en español"], "Pide que cuente qué agregó y comprueba que no cambió el texto."),
    reinforce="Dibuja un sol y rotúlalo «sun».",
    extend="Dibuja un paisaje con cinco elementos y rotula cada uno en inglés.",
)

register(
    OA5, 3,
    materials="Las consignas y mini rimas escritas en cada ejercicio, que lee un adulto; espacio libre para moverse.",
    use="Aprenderé a mostrar que entendí con movimientos del cuerpo. Sirve para participar con alegría y comprobar que comprendí.",
    prior=["Sé qué significan jump, clap y stand up.", "Sé escuchar una instrucción."],
    explain=[
        "Mover el cuerpo es otra forma de responder. Si el adulto dice «Jump!», saltas; si dice «Sit down», te sientas; si dice «Spin around» (da una vuelta), giras. Tu cuerpo muestra que entendiste sin usar palabras.",
        "También puedes representar acciones de un cuento. En «The rabbit hops», saltas como conejo. En «The fish swims», mueves los brazos como si nadaras. Haz el movimiento al mismo tiempo que oyes la palabra.",
        "Antes de moverte, asegúrate de que hay espacio y que nadie esté cerca. Mueve el cuerpo con cuidado. Si no recuerdas qué palabra era, mira a los demás y pide «Again, please».",
    ],
    vocab=[("jump", "saltar"), ("spin around", "girar, dar una vuelta"), ("hop", "dar saltitos"), ("swim", "nadar"), ("walk", "caminar"), ("stop", "parar")],
    worked=[
        {"title": "Responder con el cuerpo", "problem": ADULT + "«Jump three times!» ¿Qué haces?", "steps": ["Jump es saltar.", "Three es tres."], "answer": "Salto tres veces"},
        {"title": "Representar un cuento", "problem": ADULT + "«The rabbit hops, hops, hops.» ¿Cómo lo representas?", "steps": ["Hop es dar saltitos.", "Lo repito tres veces."], "answer": "Doy tres saltitos"},
    ],
    mistakes=[
        {"wrong": "Moverse sin escuchar la palabra.", "why": "Se copia a los demás sin pensar.", "fix": "Escucha la palabra y haz el movimiento que corresponde."},
        {"wrong": "Mover el cuerpo sin cuidar el espacio.", "why": "Se hace de forma brusca.", "fix": "Revisa que haya espacio y muévete con cuidado."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Walk!» ¿Qué haces?", "Camino", "Walk es caminar."),
            ex(ADULT + "«Clap your hands!» ¿Qué haces?", "Aplaudo", "Clap es aplaudir."),
            ex(ADULT + "«Stop!» ¿Qué haces?", "Me detengo", "Stop es parar."),
        ],
        "understand": [
            ex("¿Qué significa «spin around»?", "dar una vuelta, girar", "Es un movimiento circular."),
            ex("¿Para qué sirve responder con el cuerpo?", "Para mostrar que entendí sin hablar", "Es una evidencia física."),
            ex("¿Qué debes revisar antes de moverte?", "Que haya espacio y que sea seguro", "Cuidar a los demás es importante."),
        ],
        "apply": [
            ex(ADULT + "«Jump two times and then stop.» ¿Cuántos saltos haces?", "2", "Two es dos."),
            ex(ADULT + "«Walk, walk, stop!» ¿Cuántas veces caminas antes de parar?", "2", "Walk se dice dos veces antes de stop."),
            ex(ADULT + "«Swim, swim, swim like a fish.» ¿Qué animal representas?", "Un pez", "Fish es pez."),
        ],
        "reason": [
            ex("Oíste «sit down» y un niño se puso de pie. ¿Qué palabra confundió?", "Down con up", "Sit down es sentarse."),
            ex("¿Por qué es mejor escuchar antes de moverse?", "Porque así hago el movimiento correcto", "El movimiento depende de la palabra."),
        ],
        "challenge": [
            ex(ADULT + "«Jump, clap, spin and stop!» ¿Cuántas acciones haces?", "4", "Son jump, clap, spin y stop."),
            ex("Escribe en inglés una orden de movimiento para que alguien salte.", "Jump", "Jump es saltar."),
        ],
    },
    context=[ex(ADULT + "«We are the rabbits! Hop, hop, hop! Now sleep.» En el patio juegan a ser conejos. ¿Qué hacen después de saltar?", "Duermen", "Sleep es dormir.")],
    selfcheck=[
        ex("¿Qué significa «walk»?", "caminar", "Walk es caminar."),
        ex(ADULT + "«Clap three times.» ¿Cuántas palmadas das?", "3", "Three es tres."),
        ex("Antes de empezar un juego de movimiento, ¿qué miras a tu alrededor?", "El espacio", "Así evito chocar con otros."),
    ],
    open_task=task("Un adulto lee: «Walk, walk, walk. Jump, jump. Spin around. Stop!» Haz cada movimiento con cuidado en un espacio libre. Luego inventa tu movimiento y dilo: «I can ... !» con una acción en inglés.", "Camina tres pasos, salta dos veces, gira y para. Luego dice «I can clap!» y aplaude.", ["hace los movimientos en orden", "cuida el espacio", "dice una frase con I can"], ["video con permiso", "nota del adulto"], ["cambiar el orden", "no parar al final"], "Repite con él las órdenes que falló, más lento."),
    reinforce="Haz «jump» y «stop» siguiendo la voz de un adulto.",
    extend="Inventa un baile de cuatro movimientos y escribe cada acción en inglés.",
)

register(
    OA5, 4,
    materials="Los diálogos cortos escritos en cada ejercicio; un compañero o familiar y objetos de la casa como una pelota.",
    use="Aprenderé a representar un momento de un diálogo con otra persona, usando mi voz y mi cuerpo. Sirve para practicar el inglés de forma divertida.",
    prior=["Sé decir hello y thank you.", "Sé que un diálogo tiene dos voces."],
    explain=[
        "Dramatizar es actuar un diálogo con otra persona. Cada uno dice sus frases y hace gestos. Por ejemplo: A: «Hello! I'm Ana.» B: «Hello, Ana! I'm Leo.» Los dos se miran, sonríen y hablan.",
        "Para dramatizar bien: aprende tu parte, habla con voz clara, mira a tu compañero y usa tu cuerpo. Si tu personaje está contento, sonríe; si está triste, baja los hombros. Los gestos ayudan a que otros entiendan.",
        "No tienes que decirlo perfecto. Lo importante es que se entienda y que respetes los turnos. Si te equivocas, vuelve a empezar con calma.",
    ],
    vocab=[("act", "actuar"), ("turn", "turno"), ("hello, I'm...", "hola, soy..."), ("nice to meet you", "mucho gusto"), ("smile", "sonreír"), ("voice", "voz")],
    worked=[
        {"title": "Dramatizar un saludo", "problem": "A: «Hello! I'm Ana.» B: «Hello, Ana! I'm Leo.» ¿Qué dice cada uno?", "steps": ["A saluda y dice su nombre.", "B saluda a A y dice el suyo."], "answer": "Ana dice «Hello! I'm Ana» y Leo «Hello, Ana! I'm Leo»"},
        {"title": "Usar gestos", "problem": "En el diálogo, ¿cómo muestras que estás contento?", "steps": ["Sonrío.", "Uso una voz alegre."], "answer": "Sonrío y hablo con voz alegre"},
    ],
    mistakes=[
        {"wrong": "Hablar los dos a la vez.", "why": "No se respetan los turnos.", "fix": "Espera a que termine tu compañero."},
        {"wrong": "Hablar muy bajo y sin mirar.", "why": "Se siente vergüenza.", "fix": "Habla claro y mira a tu compañero."},
    ],
    tiers={
        "recovery": [
            ex("En «A: Hello! B: Hello!», ¿cuántas personas hablan?", "2", "A y B."),
            ex("¿Qué significa «nice to meet you»?", "mucho gusto", "Se dice al conocer a alguien."),
            ex("¿Quién habla primero en «A: Hello! B: Hi!»?", "A", "A habla antes que B."),
        ],
        "understand": [
            ex("¿Qué es dramatizar un diálogo?", "Actuarlo con otra persona usando voz y gestos", "Se representa con el cuerpo y la voz."),
            ex("¿Por qué se respetan los turnos?", "Para que se entienda lo que dice cada uno", "Hablar a la vez confunde."),
            ex("¿Para qué sirven los gestos?", "Para mostrar emociones y ayudar a entender", "Complementan las palabras."),
        ],
        "apply": [
            ex("A dice «Hello! I'm Ana.» ¿Qué responde B si se llama Leo?", "Hello, Ana! I'm Leo", "Saluda y se presenta."),
            ex("A dice «Thank you!» ¿Qué responde B?", "You're welcome", "Es la respuesta de cortesía."),
            ex("A dice «Goodbye!» ¿Qué responde B?", "Goodbye", "Se despide también."),
        ],
        "reason": [
            ex("Dos niños dicen sus frases al mismo tiempo. ¿Qué deben mejorar?", "Respetar los turnos", "Uno habla y el otro escucha."),
            ex("¿Por qué conviene mirar al compañero al dramatizar?", "Porque así se nota que hablo con él", "La mirada ayuda a comunicar."),
        ],
        "challenge": [
            ex("Completa el diálogo: A: «Hello! What's your name?» B: «______» (tu nombre).", "I'm ... (con tu nombre)", "I'm más nombre."),
            ex("Ordena el diálogo con números: (1) B: I'm fine, thank you. (2) A: How are you? (3) A: Hello!", "3, 2, 1", "Primero saluda, luego pregunta y después responde."),
        ],
    },
    context=[ex("En la clase de inglés actúas con una amiga: A dice «Good morning!». ¿Cómo respondes si eres B?", "Good morning!", "Se responde con el mismo saludo.")],
    selfcheck=[
        ex("¿Qué significa «turn»?", "turno", "Es el momento de hablar."),
        ex("¿Cómo responde B a «Hello! I'm Ana.»?", "Hello, Ana!", "Saluda a la persona por su nombre."),
        ex("¿Qué haces con tu cara si tu personaje está contento?", "Sonrío", "Es un gesto de alegría."),
    ],
    open_task=task("Con un adulto o hermano actúa este diálogo. Tú eres B. A: «Hello! I'm Ana. Nice to meet you.» B: «Hello, Ana! Nice to meet you, too. I'm ...» (tu nombre). A: «Goodbye!» B: «Goodbye!»", "«Hello, Ana! Nice to meet you, too. I'm Pedro. Goodbye!» con sonrisa y mirando a A.", ["dice sus frases en orden", "respeta los turnos", "habla claro", "usa gestos"], ["video con permiso", "nota del adulto"], ["hablar encima del otro", "no decir su nombre"], "Hagan el diálogo de nuevo cambiando papeles."),
    reinforce="Practica «Hello! I'm ...» frente a un espejo.",
    extend="Escribe un diálogo de cuatro líneas entre dos amigos y actúalo con alguien.",
)

register(
    OA5, 5,
    materials="Los textos y preguntas escritos en cada ejercicio, que lee un adulto; hoja y lápices de colores.",
    use="Aprenderé a decir si me gusta algo o cómo me siento, con frases simples en inglés. Sirve para expresarme y conocer a otros.",
    prior=["Sé decir «I like».", "Sé nombres de emociones en español."],
    explain=[
        "Para decir cómo te sientes, usa «I'm» más una emoción: I'm happy (estoy contento), I'm sad (estoy triste), I'm tired (estoy cansado), I'm hungry (tengo hambre). Para decir un gusto usa I like y para un no gusto I don't like.",
        "Para preguntar a alguien: «How are you?» (¿cómo estás?). Se responde: «I'm fine, thank you» o «I'm happy». Y para preguntar un gusto: «Do you like pizza?» (¿te gusta la pizza?). Respondes «Yes, I do» o «No, I don't».",
        "Cada persona siente y piensa distinto. Está bien decir «I don't like it». Lo importante es decirlo con respeto y con una frase simple en inglés.",
    ],
    vocab=[("I'm happy", "estoy contento"), ("I'm sad", "estoy triste"), ("I'm tired", "estoy cansado"), ("I'm hungry", "tengo hambre"), ("I like / I don't like", "me gusta / no me gusta"), ("How are you?", "¿cómo estás?")],
    worked=[
        {"title": "Decir cómo me siento", "problem": "Estás contento. ¿Cómo lo dices?", "steps": ["Uso I'm.", "Agrego happy."], "answer": "I'm happy"},
        {"title": "Decir un gusto", "problem": "No te gusta la sopa. ¿Cómo lo dices?", "steps": ["Uso I don't like.", "Agrego soup."], "answer": "I don't like soup"},
    ],
    mistakes=[
        {"wrong": "Decir «I happy» sin el verbo.", "why": "En español no se dice así.", "fix": "Usa I'm: I'm happy."},
        {"wrong": "Responder «Yes, I like» a «Do you like pizza?».", "why": "Se usa la forma de otra pregunta.", "fix": "Responde Yes, I do o No, I don't."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«I'm happy.» ¿Cómo está la persona?", "Contenta", "Happy es contento."),
            ex(ADULT + "«I'm tired.» ¿Cómo está la persona?", "Cansada", "Tired es cansado."),
            ex(ADULT + "«I like pizza.» ¿Qué le gusta?", "La pizza", "I like es me gusta."),
        ],
        "understand": [
            ex("¿Qué significa «I'm hungry»?", "tengo hambre", "Se usa I'm más hungry."),
            ex("¿Cómo respondes a «How are you?» si estás bien?", "I'm fine, thank you", "Es la respuesta común."),
            ex("¿Qué significa «I don't like»?", "no me gusta", "Es lo contrario de I like."),
        ],
        "apply": [
            ex(ADULT + "«Do you like pizza?» Responde que sí.", "Yes, I do", "Do se repite en la respuesta."),
            ex(ADULT + "«Do you like cats?» Responde que no.", "No, I don't", "Don't es la forma negativa."),
            ex(ADULT + "«How are you?» Responde que estás cansado.", "I'm tired", "I'm más tired."),
        ],
        "reason": [
            ex("¿Por qué «I don't like it» es una respuesta aceptable?", "Porque cada persona tiene gustos distintos", "Expresar un gusto propio es válido."),
            ex("Un niño dijo «I sad». ¿Qué le falta?", "El verbo I'm", "Se dice I'm sad."),
        ],
        "challenge": [
            ex("Escribe una frase en inglés que diga que estás contento y te gusta el parque.", "I'm happy. I like the park.", "Dos frases simples."),
            ex("Escribe una pregunta en inglés para saber si a alguien le gustan los gatos.", "Do you like cats?", "Do you like más cats."),
        ],
    },
    context=[ex(ADULT + "«A: How are you today? B: I'm hungry!» En la hora de almuerzo una niña dice esto. ¿Qué tiene?", "Hambre", "Hungry es tener hambre.")],
    selfcheck=[
        ex("¿Qué significa «sad»?", "triste", "Es una emoción."),
        ex("¿Cómo se dice «me gusta el helado»?", "I like ice cream", "I like más ice cream."),
        ex("¿Cómo respondes a «Do you like apples?» si te gustan?", "Yes, I do", "Do se repite."),
    ],
    open_task=task("Un adulto te pregunta: «How are you today?» y «Do you like apples?». Responde con frases completas en inglés. Luego dibuja una cara que muestre cómo te sientes y escribe debajo «I'm ...».", "«I'm happy.» «Yes, I do.» Dibujo de una cara contenta con «I'm happy».", ["responde las dos preguntas", "usa I'm y Yes/No, I do/don't", "dibuja la emoción", "escribe la frase"], ["dibujo", "nota del adulto"], ["decir I happy", "responder Yes, I like"], "Elogia que haya expresado lo que siente y ayuda con la forma de la frase."),
    reinforce="Di «I'm happy» y haz la cara que corresponde.",
    extend="Escribe cinco frases con I like y I don't like sobre comidas.",
)

# ---------------------------------------------------------------- OA 06
register(
    OA6, 1,
    materials="Los textos completos escritos en cada ejercicio (tarjeta, rima, instrucciones, información); lápiz.",
    use="Aprenderé a reconocer qué tipo de texto leo en inglés (tarjeta, rima, instrucciones o información) y para qué sirve. Sirve para saber cómo leerlo.",
    prior=["Sé leer palabras cortas.", "Sé qué es una tarjeta de cumpleaños."],
    explain=[
        "Los textos escritos tienen distintos propósitos. Una tarjeta (card) saluda o felicita: «Happy Birthday, Ana! Love, Leo». Una rima (rhyme) divierte con palabras que suenan parecido. Las instrucciones dicen cómo hacer algo paso a paso. Un texto informativo cuenta datos.",
        "Para reconocer qué es, mira la forma. Una tarjeta tiene un saludo y una despedida. Una rima tiene líneas cortas con finales parecidos. Las instrucciones tienen números y verbos como Draw, Cut o Open. Un texto informativo dice cómo es algo: «A cat has four legs.»",
        "Saber el propósito te dice cómo leer. La tarjeta se lee para sentir, la rima para disfrutar, las instrucciones para hacer algo y la información para aprender.",
    ],
    vocab=[("card", "tarjeta"), ("rhyme", "rima"), ("instructions", "instrucciones"), ("information", "información"), ("Happy Birthday", "feliz cumpleaños"), ("love", "con cariño")],
    worked=[
        {"title": "Reconocer una tarjeta", "problem": "Lee: «Happy Birthday, Ana! Love, Leo.» ¿Qué tipo de texto es?", "steps": ["Tiene un saludo: Happy Birthday.", "Tiene una despedida: Love, Leo.", "Es una tarjeta."], "answer": "Una tarjeta de cumpleaños"},
        {"title": "Reconocer instrucciones", "problem": "Lee: «1. Draw a circle. 2. Color it red.» ¿Qué tipo de texto es?", "steps": ["Tiene números.", "Usa verbos de acción: Draw, Color.", "Dice cómo hacer algo."], "answer": "Instrucciones"},
    ],
    mistakes=[
        {"wrong": "Leer todo igual sin fijarse en qué tipo de texto es.", "why": "No se mira la forma.", "fix": "Mira si tiene saludo, números, líneas cortas o datos."},
        {"wrong": "Pensar que una rima son instrucciones.", "why": "Las dos tienen frases cortas.", "fix": "Las instrucciones tienen números y verbos de acción."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «Happy Birthday, Mia! Love, Tom.» ¿Es una tarjeta?", "Sí", "Tiene saludo y despedida."),
            ex("Lee: «Cat, hat, mat, sat.» ¿Es una rima?", "Sí", "Las palabras suenan parecido."),
            ex("Lee: «1. Open the box. 2. Take a pencil.» ¿Son instrucciones?", "Sí", "Tienen números y verbos."),
        ],
        "understand": [
            ex("¿Para qué sirve una tarjeta?", "Para saludar o felicitar a alguien", "Es una forma de comunicar cariño."),
            ex("¿Qué pistas tienen las instrucciones?", "Números y verbos de acción", "Dicen qué hacer en orden."),
            ex("¿Qué es una rima?", "Un texto con finales que suenan parecido", "Divierte con los sonidos."),
        ],
        "apply": [
            ex("Lee: «A dog has four legs. A dog can run.» ¿Qué tipo de texto es?", "Información", "Cuenta datos sobre algo."),
            ex("Lee: «Dear Ana, Thank you for the book. Love, Pia.» ¿Qué tipo de texto es?", "Una tarjeta", "Tiene saludo, mensaje y despedida."),
            ex("Lee: «Sun, sun, shine on me. Fun, fun, one, two, three.» ¿Qué tipo de texto es?", "Una rima", "Las líneas terminan con sonidos parecidos."),
        ],
        "reason": [
            ex("Un niño dice que «1. Jump. 2. Clap.» es una rima. ¿Por qué no lo es?", "Porque tiene números y verbos que piden hacer algo", "Son instrucciones, no una rima."),
            ex("¿Por qué saber el propósito del texto ayuda a leerlo?", "Porque sé cómo leerlo: para hacer, sentir o aprender", "Cada texto se lee distinto."),
        ],
        "challenge": [
            ex("Une cada texto con su tipo. (a) «Happy Birthday, Leo!» (b) «Draw a star. Color it yellow.» (c) «A cat has a tail.»", "a = tarjeta, b = instrucciones, c = información", "Saludo, orden y dato."),
            ex("Escribe una tarjeta corta en inglés para un amigo que cumple años.", "Happy Birthday, ...! Love, ...", "Tiene saludo y despedida."),
        ],
    },
    context=[ex("Te llega una nota que dice «Get well soon, Pia! Love, Ana». ¿Qué tipo de texto es y qué desea Ana?", "Una tarjeta; que Pía se mejore", "Get well soon es que te mejores pronto.")],
    selfcheck=[
        ex("¿Cómo se dice «tarjeta» en inglés?", "card", "Card es tarjeta."),
        ex("¿Qué tipo de texto tiene números y verbos como Draw?", "Instrucciones", "Dicen cómo hacer algo."),
        ex("¿Qué significa «Happy Birthday»?", "feliz cumpleaños", "Es el saludo típico."),
    ],
    open_task=task("Lee estos tres textos: (A) «Happy Birthday, Sam! Love, Mia.» (B) «1. Draw a circle. 2. Color it blue.» (C) «A cat has four legs.» Escribe junto a cada uno si es tarjeta, instrucciones o información y para qué sirve. Luego crea tu propia tarjeta de dos líneas en inglés.", "A tarjeta (felicitar), B instrucciones (hacer un dibujo), C información (aprender). Mi tarjeta: «Happy Birthday, Leo! Love, Pedro.»", ["clasifica los tres textos", "explica el propósito", "crea su tarjeta con saludo y despedida"], ["texto clasificado", "tarjeta creada"], ["confundir instrucciones con información", "tarjeta sin despedida"], "Revisa con él las pistas de forma de cada texto."),
    reinforce="Lee en voz alta «Happy Birthday!» y di para qué sirve una tarjeta.",
    extend="Crea una rima de dos líneas en inglés con palabras que terminen igual.",
)

register(
    OA6, 2,
    materials="Los textos cortos escritos en cada ejercicio; lápiz.",
    use="Aprenderé a decir de qué trata un texto corto, sin leer palabra por palabra. Sirve para entender la idea principal aunque haya palabras desconocidas.",
    prior=["Sé leer palabras cortas en inglés.", "Sé qué significan algunas palabras como cat, dog y ball."],
    explain=[
        "La idea general (main idea) es de qué trata el texto. Para encontrarla, lee todo el texto una vez y busca las palabras que ya conoces. No necesitas entender cada palabra. Por ejemplo: «Ana has a red kite. She plays in the park.» Reconoces Ana, red kite y park, y entiendes que Ana juega con una cometa roja en el parque.",
        "Para decir la idea general, responde: ¿quién?, ¿qué hace? y ¿dónde? Con esas tres respuestas ya resumes el texto. Si una palabra es desconocida, mira las palabras de alrededor y la imagen si hay una.",
        "Después de leer, di la idea con tus palabras en español o en inglés simple: «Ana plays in the park.» Si tu idea no coincide con el texto, vuelve a leer una sola línea y corrige.",
    ],
    vocab=[("main idea", "idea general"), ("kite", "cometa"), ("park", "parque"), ("plays", "juega"), ("who?", "¿quién?"), ("where?", "¿dónde?")],
    worked=[
        {"title": "Idea general", "problem": "Lee: «Ana has a red kite. She plays in the park.» ¿De qué trata?", "steps": ["¿Quién? Ana.", "¿Qué hace? Juega con una cometa.", "¿Dónde? En el parque."], "answer": "Ana juega con su cometa en el parque"},
        {"title": "Palabra desconocida", "problem": "Lee: «The cat sits on the mat.» Si no conoces mat, ¿cómo entiendes la idea?", "steps": ["Conozco cat y sits on.", "Entiendo que el gato se sienta sobre algo."], "answer": "Un gato se sienta sobre algo (mat es alfombra)"},
    ],
    mistakes=[
        {"wrong": "Decir solo una palabra suelta.", "why": "Se queda con un detalle.", "fix": "Responde quién, qué hace y dónde."},
        {"wrong": "No leer porque hay palabras desconocidas.", "why": "Se piensa que hay que saber todo.", "fix": "Usa las palabras que conoces y las pistas."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «Tom has a dog.» ¿Qué tiene Tom?", "Un perro", "Dog es perro."),
            ex("Lee: «The sun is hot.» ¿Cómo es el sol?", "Caliente", "Hot es caliente."),
            ex("Lee: «Ana is in the park.» ¿Dónde está Ana?", "En el parque", "Park es parque."),
        ],
        "understand": [
            ex("¿Qué es la idea general de un texto?", "De qué trata, dicho de forma breve", "Resume lo más importante."),
            ex("¿Qué tres preguntas ayudan a encontrarla?", "¿Quién? ¿Qué hace? ¿Dónde?", "Con ellas se resume."),
            ex("¿Qué haces si hay una palabra desconocida?", "Uso las palabras que conozco y las pistas", "El resto del texto ayuda."),
        ],
        "apply": [
            ex("Lee: «Leo has a blue ball. He plays with his dog.» ¿Con quién juega Leo?", "Con su perro", "Plays with his dog."),
            ex("Lee: «Mia is sad. She has no pencil. Tom gives her a pencil.» ¿Qué le da Tom a Mia?", "Un lápiz", "Gives her a pencil es le da un lápiz."),
            ex("Lee: «It is rainy. Pia has an umbrella.» ¿Qué tiempo hace?", "Llueve", "Rainy es lluvioso."),
        ],
        "reason": [
            ex("Un niño dice que «Ana plays in the park» trata de un parque. ¿Qué le falta decir?", "Quién juega, que es Ana", "Falta el personaje y la acción."),
            ex("¿Por qué no hace falta entender todas las palabras?", "Porque las palabras clave bastan para la idea general", "Se usa el contexto."),
        ],
        "challenge": [
            ex("Lee: «Sam has a hat. The wind takes the hat. Sam runs.» Escribe la idea general en español.", "Sam corre porque el viento se lleva su sombrero", "Resume el problema y la acción."),
            ex("Lee: «A bird is on a tree. It sings.» Escribe una frase en inglés que diga lo que hace el pájaro.", "The bird sings", "Sings es canta."),
        ],
    },
    context=[ex("En una tarjeta lees: «Dear Ana, I have a new puppy. His name is Max. Love, Leo.» ¿De qué trata?", "De que Leo tiene un perrito nuevo llamado Max", "New puppy es perrito nuevo.")],
    selfcheck=[
        ex("¿Cómo se dice «idea general» en inglés?", "main idea", "Main idea es idea principal."),
        ex("Lee: «The dog runs.» ¿Qué hace el perro?", "Corre", "Runs es corre."),
        ex("¿Qué haces si tu idea no coincide con el texto?", "Vuelvo a leer y la corrijo", "Releer ayuda a corregir."),
    ],
    open_task=task("Lee este texto: «Pia has a small red bag. She puts a book and a pencil in the bag. Then she walks to school.» Escribe o di en español o en inglés simple: (1) ¿Quién es? (2) ¿Qué hace? (3) ¿A dónde va? Y dibuja a Pía con su mochila.", "(1) Pía. (2) Pone un libro y un lápiz en su mochila. (3) Va a la escuela. Dibujo de Pía con una mochila roja pequeña.", ["responde las tres preguntas", "usa palabras del texto", "dibujo coherente"], ["respuestas", "dibujo"], ["decir que Pía va al parque", "dibujar una mochila grande"], "Marca con él las palabras del texto que respaldan cada respuesta."),
    reinforce="Lee «The dog runs» y haz el gesto de correr.",
    extend="Escribe un texto de dos líneas en inglés sobre tu mascota o una mascota que te gustaría tener.",
)

register(
    OA6, 3,
    materials="Los cuentos cortos escritos en cada ejercicio; lápiz y papel.",
    use="Aprenderé a seguir quién hace qué en un cuento corto en inglés. Sirve para entender una historia al leerla.",
    prior=["Sé quiénes son los personajes de un cuento.", "Sé leer palabras como has, runs y says."],
    explain=[
        "En un cuento leído, los personajes tienen nombre (Tom, Ana) o son animales o cosas (the cat, the kite). Para seguir la historia, busca el nombre del personaje y el verbo de acción que viene después. Ejemplo: «Tom runs», «The cat jumps».",
        "Las palabras como he (él), she (ella) o it (eso) reemplazan al nombre para no repetirlo. Si lees «Tom has a ball. He plays with it», he es Tom e it es la pelota. Si no sabes a quién se refiere, mira la frase anterior.",
        "Anota lo que pasa en orden: primero, luego y al final. En inglés: first (primero), then (luego), at the end (al final). Así recuerdas la historia completa.",
    ],
    vocab=[("character", "personaje"), ("he / she / it", "él / ella / eso"), ("first", "primero"), ("then", "luego"), ("at the end", "al final"), ("runs / jumps", "corre / salta")],
    worked=[
        {"title": "Quién hace qué", "problem": "Lee: «Tom has a ball. He kicks it. The ball goes to Ana.» ¿Quién patea?", "steps": ["Tom tiene una pelota.", "He es Tom.", "He kicks it: él patea la pelota."], "answer": "Tom patea la pelota"},
        {"title": "Orden de los hechos", "problem": "Lee: «First, Ana has a seed. Then she puts it in the ground. At the end, a flower grows.» ¿Qué pasa al final?", "steps": ["Busco at the end.", "Una flor crece."], "answer": "Crece una flor"},
    ],
    mistakes=[
        {"wrong": "No saber quién es «he» o «she».", "why": "Se pierde la frase anterior.", "fix": "Vuelve a la frase anterior y busca el nombre."},
        {"wrong": "Contar los hechos desordenados.", "why": "No se usan first, then y at the end.", "fix": "Ordena con esas palabras."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «Ana runs.» ¿Quién corre?", "Ana", "El nombre va antes del verbo."),
            ex("Lee: «The cat jumps.» ¿Qué hace el gato?", "Salta", "Jumps es salta."),
            ex("Lee: «Tom has a kite.» ¿Qué tiene Tom?", "Una cometa", "Kite es cometa."),
        ],
        "understand": [
            ex("¿Qué significa «he»?", "él", "Reemplaza el nombre de un niño."),
            ex("¿Qué significa «then»?", "luego", "Indica lo que sigue."),
            ex("¿Para qué sirven first, then y at the end?", "Para ordenar los hechos del cuento", "Muestran la secuencia."),
        ],
        "apply": [
            ex("Lee: «Mia has a dog. She walks it to the park.» ¿Quién es «she»?", "Mia", "She reemplaza a Mia."),
            ex("Lee: «Leo has a cake. He eats it.» ¿Qué come Leo?", "La torta", "It es la torta."),
            ex("Lee: «First, Pia sees a bird. Then she takes a photo.» ¿Qué hace después de ver al pájaro?", "Toma una foto", "Then indica lo que pasa después."),
        ],
        "reason": [
            ex("Lee: «Sam has a ball. He kicks it.» ¿Por qué «it» no es Sam?", "Porque it se usa para cosas y Sam es una persona", "Se usa he para un niño."),
            ex("¿Por qué es útil ordenar los hechos con first, then y at the end?", "Para recordar la historia completa", "El orden ayuda a comprender."),
        ],
        "challenge": [
            ex("Ordena con números: (1) At the end, Ana is happy. (2) First, Ana has a kite. (3) Then the kite goes up.", "2, 3, 1", "Primero la tiene, luego sube y al final está contenta."),
            ex("Escribe una frase en inglés con first, para decir que primero abres tu libro.", "First, I open my book", "First marca el comienzo."),
        ],
    },
    context=[ex("Lees en un libro: «The little fish is sad. It has no friend. Then a big fish says: Hello!» ¿Qué hace el pez grande?", "Saluda", "Says: Hello! es dice hola.")],
    selfcheck=[
        ex("¿Qué significa «she»?", "ella", "Reemplaza el nombre de una niña."),
        ex("Lee: «Leo jumps.» ¿Quién salta?", "Leo", "El nombre va antes del verbo."),
        ex("¿Qué palabra indica el final de una historia?", "At the end", "Marca el cierre."),
    ],
    open_task=task("Lee este cuento: «First, Ben has a seed. Then he puts the seed in a pot. He gives water to the seed. At the end, a small green plant grows. Ben is happy.» Ordena en tu cuaderno los hechos con 1, 2, 3 y 4 y dibuja el final.", "1 Ben tiene una semilla. 2 La pone en una maceta. 3 Le echa agua. 4 Crece una plantita verde. Dibujo: plantita verde y Ben contento.", ["ordena cuatro hechos", "usa first, then y at the end", "dibuja el final"], ["lista ordenada", "dibujo"], ["poner el final primero", "no mencionar el agua"], "Haz que cuente el cuento con sus dedos: un hecho por dedo."),
    reinforce="Lee «Ana runs» y di quién hace qué.",
    extend="Escribe un cuento de tres frases en inglés con first, then y at the end.",
)

register(
    OA6, 4,
    materials="Los textos con frases frecuentes escritos en cada ejercicio; lápiz.",
    use="Aprenderé a reconocer al leer frases enteras que se repiten mucho en inglés, como «I can», «I have» y «I like». Sirve para leer más rápido y entender mejor.",
    prior=["Sé leer palabras cortas.", "Sé qué significan I can, I have y I like."],
    explain=[
        "Un chunk es un grupo de palabras que se usa junto, como «I like», «I have», «I can», «It's a...» o «Thank you». Aprenderlo como un bloque te ayuda a leer rápido sin traducir palabra por palabra.",
        "Cuando leas «I like apples», reconoce el bloque «I like» y entiende que dice que algo me gusta. Luego mira la palabra que sigue: apples. Con el bloque y la palabra nueva ya entiendes toda la frase.",
        "Para practicar, busca los bloques en un texto y subráyalos. Después puedes cambiar solo la última palabra para crear frases nuevas: I like apples, I like cats, I like blue.",
    ],
    vocab=[("chunk", "grupo de palabras que van juntas"), ("I like", "me gusta"), ("I have", "yo tengo"), ("I can", "yo puedo"), ("It's a", "es un/una"), ("thank you", "gracias")],
    worked=[
        {"title": "Encontrar el bloque", "problem": "Lee: «I like apples.» ¿Cuál es el bloque?", "steps": ["Busco las palabras que van juntas y se repiten mucho.", "I like es un bloque."], "answer": "I like"},
        {"title": "Cambiar una palabra", "problem": "Con el bloque «I have», crea una frase sobre un perro.", "steps": ["Uso I have.", "Agrego a dog."], "answer": "I have a dog"},
    ],
    mistakes=[
        {"wrong": "Leer cada palabra de «I like» por separado y tratar de traducirla.", "why": "No se reconoce el bloque.", "fix": "Lee «I like» como una unidad: me gusta."},
        {"wrong": "Cambiar el bloque en lugar de la última palabra.", "why": "Se pierde el sentido.", "fix": "Cambia solo la palabra final."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «I can run.» ¿Cuál es el bloque?", "I can", "Se usa para decir lo que puedo hacer."),
            ex("Lee: «I have a cat.» ¿Cuál es el bloque?", "I have", "Se usa para decir lo que tengo."),
            ex("Lee: «It's a ball.» ¿Cuál es el bloque?", "It's a", "Se usa para decir qué es algo."),
        ],
        "understand": [
            ex("¿Qué es un «chunk»?", "Un grupo de palabras que se usan juntas", "Se lee como un bloque."),
            ex("¿Qué ventaja tiene leer bloques?", "Se lee más rápido sin traducir cada palabra", "Se reconoce el significado de una vez."),
            ex("¿Qué significa «It's a»?", "es un/una", "Describe qué es algo."),
        ],
        "apply": [
            ex("Lee: «I like cats.» ¿Qué le gusta a la persona?", "Los gatos", "Cats son gatos."),
            ex("Completa con un bloque: «____ swim.» (Yo puedo)", "I can", "Se usa para habilidades."),
            ex("Completa: «____ a pencil.» (Yo tengo)", "I have", "Se usa para tener."),
        ],
        "reason": [
            ex("¿Por qué conviene cambiar solo la última palabra al crear frases?", "Porque el bloque mantiene el sentido", "El patrón queda igual."),
            ex("Un niño leyó «I can run» como tres palabras sueltas. ¿Qué debió hacer?", "Reconocer I can como un bloque", "Así entiende la idea completa."),
        ],
        "challenge": [
            ex("Crea una frase en inglés con «I like» y una fruta.", "Por ejemplo: I like bananas", "Se mantiene el bloque."),
            ex("Subraya los bloques de esta frase: «I have a dog. I can run with it.»", "I have y I can", "Son los grupos que se repiten."),
        ],
    },
    context=[ex("En una tarjeta de cumpleaños lees: «I have a gift for you. I like you!» ¿Qué bloques reconoces?", "I have y I like", "Son frases frecuentes.")],
    selfcheck=[
        ex("¿Qué significa «I can»?", "yo puedo", "Se usa para habilidades."),
        ex("Lee: «It's a dog.» ¿Qué es?", "Un perro", "Dog es perro."),
        ex("¿Qué cambias para crear una frase nueva con el mismo bloque?", "La palabra final", "El bloque se mantiene."),
    ],
    open_task=task("Lee este texto: «I have a cat. It's a black cat. I can play with it. I like my cat.» Subraya los cuatro bloques que reconozcas (I have, It's a, I can, I like) y crea tres frases nuevas cambiando la última palabra.", "Bloques: I have, It's a, I can, I like. Nuevas: I have a dog. It's a red ball. I like apples.", ["subraya los cuatro bloques", "crea tres frases con los bloques", "cambia solo la última palabra"], ["texto subrayado", "frases"], ["subrayar palabras sueltas", "cambiar el bloque"], "Lee con él cada frase nueva en voz alta y celebra las que quedaron correctas."),
    reinforce="Lee «I like» tres veces y di tres cosas que te gusten.",
    extend="Escribe cinco frases con el bloque I can.",
)

register(
    OA6, 5,
    materials="Los textos y consignas escritos en cada ejercicio; lápiz y lápices de colores.",
    use="Aprenderé a mostrar que entendí un texto que leí, dibujando, marcando o respondiendo preguntas. Sirve para demostrar mi comprensión al leer.",
    prior=["Sé leer frases cortas.", "Sé buscar la idea general y los personajes."],
    explain=[
        "Para mostrar que entendiste un texto, puedes dibujar lo que leíste, marcar la respuesta correcta o responder preguntas cortas. Cada una es una evidencia diferente.",
        "Ejemplo: lees «Tom has a red ball. He plays with it in the park.» Puedes dibujar a Tom con una pelota roja en un parque; marcar quién tiene la pelota; y responder «Where does Tom play?» (¿dónde juega Tom?) con «In the park».",
        "Después de responder, vuelve al texto y comprueba. ¿Tu dibujo tiene los colores correctos? ¿Tu respuesta usa palabras del texto? Si algo no coincide, corrige.",
    ],
    vocab=[("who?", "¿quién?"), ("what?", "¿qué?"), ("where?", "¿dónde?"), ("red ball", "pelota roja"), ("park", "parque"), ("check", "comprobar")],
    worked=[
        {"title": "Responder una pregunta", "problem": "Lee: «Tom has a red ball. He plays with it in the park.» Pregunta: Where does Tom play?", "steps": ["Busco in the park.", "Respondo con el lugar."], "answer": "In the park (en el parque)"},
        {"title": "Dibujar", "problem": "Con el mismo texto, ¿qué dibujas?", "steps": ["Un niño llamado Tom.", "Una pelota roja.", "Un parque."], "answer": "Tom con una pelota roja en un parque"},
    ],
    mistakes=[
        {"wrong": "Responder sin volver al texto.", "why": "Se confía en la memoria.", "fix": "Busca la palabra en el texto."},
        {"wrong": "Dibujar sin revisar los colores del texto.", "why": "Se dibuja con los colores que se tienen.", "fix": "Usa los colores que dice el texto."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «Mia has a green book.» ¿De qué color es el libro?", "Verde", "Green es verde."),
            ex("Lee: «Leo has two cats.» ¿Cuántos gatos tiene Leo?", "2", "Two es dos."),
            ex("Lee: «Pia is at school.» ¿Dónde está Pía?", "En la escuela", "School es escuela."),
        ],
        "understand": [
            ex("¿Qué formas hay de mostrar que entendiste un texto?", "Dibujar, marcar o responder preguntas", "Son evidencias de comprensión."),
            ex("¿Por qué conviene volver al texto después de responder?", "Para comprobar que mi respuesta coincide", "Se corrigen errores."),
            ex("¿Qué significa «where»?", "dónde", "Pregunta por un lugar."),
        ],
        "apply": [
            ex("Lee: «Ben has a blue kite. It flies in the sky.» ¿Dónde vuela la cometa?", "En el cielo", "Sky es cielo."),
            ex("Lee: «Ana has a yellow bag. Her book is in the bag.» ¿Dónde está el libro?", "En la mochila", "In the bag."),
            ex("Lee: «Sam is hungry. He eats an apple.» ¿Qué come Sam?", "Una manzana", "Apple es manzana."),
        ],
        "reason": [
            ex("Un niño dibujó una pelota azul pero el texto dice «red ball». ¿Qué debe hacer?", "Cambiar el color a rojo", "Red es rojo."),
            ex("¿Por qué responder preguntas es una evidencia de comprensión?", "Porque muestra que entendí la información del texto", "Respuestas correctas prueban comprensión."),
        ],
        "challenge": [
            ex("Lee: «Pia has three red flowers and two yellow flowers.» ¿Cuántas flores hay en total?", "5", "Tres más dos son cinco."),
            ex("Escribe en inglés una pregunta sobre dónde juega Tom.", "Where does Tom play?", "Where pregunta por el lugar."),
        ],
    },
    context=[ex("En una tarjeta lees: «Dear Leo, I have a new red bike. It's in the garden. Come and see! Love, Ana.» ¿Dónde está la bicicleta?", "En el jardín", "In the garden es en el jardín.")],
    selfcheck=[
        ex("¿Cómo se dice «¿dónde?» en inglés?", "where", "Where pregunta por un lugar."),
        ex("Lee: «The ball is red.» ¿De qué color es la pelota?", "Roja", "Red es rojo."),
        ex("¿Qué haces después de dibujar o responder?", "Reviso con el texto", "Así se comprueba la comprensión."),
    ],
    open_task=task("Lee este texto: «Lola has a small white dog. The dog is called Max. Max likes to run in the garden. Lola is happy.» Dibuja la escena y responde por escrito: (1) Who has a dog? (2) What color is the dog? (3) Where does Max run?", "Dibujo de una niña con un perro blanco pequeño en un jardín. (1) Lola. (2) White. (3) In the garden.", ["dibujo coherente con el texto", "tres respuestas correctas", "usa palabras del texto"], ["dibujo", "respuestas"], ["perro de otro color", "decir que corre en el parque"], "Pide que señale en el texto la palabra que respalda cada respuesta."),
    reinforce="Lee «Mia has a green book» y dibuja el libro.",
    extend="Escribe tres preguntas con Who, What y Where sobre un texto corto que inventes.",
)
