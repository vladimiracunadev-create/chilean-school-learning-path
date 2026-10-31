"""Cuaderno del estudiante, 1.º básico Lenguaje y Comunicación: OA 25 (juego de roles) y OA 26 (recitación expresiva)."""
from __future__ import annotations

from student_lessons import ex, register

OA25, OA26 = "LE01 OA 25", "LE01 OA 26"
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


# ================================================================ OA 25
reg(
    OA25, 1,
    "Las tarjetas de roles escritas en este cuaderno, lápiz y hoja. Para jugar se necesita un adulto, un hermano o un muñeco como compañero.",
    "Aprenderé que en un juego de roles cada rol tiene un propósito, es decir, algo que hace y dice. Sirve para jugar a ser otra persona, hablar más y trabajar con otros.",
    ["Sé jugar a «hacer como si».", "Sé hablar con otra persona por turnos."],
    [
        "Un juego de roles es un juego en que cada persona representa un rol, es decir, a alguien con una tarea. Puedes ser vendedor, doctora, cartero o bibliotecaria. Jugar a esto te ayuda a practicar cómo hablar con otros y a cooperar.",
        "Cada rol tiene un propósito, que es para qué sirve. El vendedor ofrece productos y cobra. La doctora escucha y cuida a las personas. El cartero entrega cartas. La bibliotecaria presta libros y cuida el silencio. Cuando sabes el propósito, sabes qué decir.",
        "En el juego usamos frases del rol. El vendedor dice: «¿Qué desea llevar?». La doctora dice: «¿Dónde le duele?». El cartero dice: «Tengo una carta para usted». Después cada persona escucha a la otra y responde, como en una conversación real.",
    ],
    [("rol", "papel que represento en un juego"), ("propósito", "para qué sirve un rol"), ("vendedor", "persona que ofrece productos"), ("bibliotecaria", "persona que cuida y presta libros"), ("cooperar", "ayudarnos para lograr algo")],
    [
        ("Entender un rol", "En la tienda de frutas, tú eres la vendedora. ¿Cuál es tu propósito y qué puedes decir?", ["Ofrezco frutas.", "Cobro lo que se lleva.", "Hablo con amabilidad."], "Propósito: ofrecer frutas y cobrar. Digo: «¿Qué desea llevar?»."),
        ("Entender otro rol", "Eres el cartero. ¿Cuál es tu propósito y qué puedes decir?", ["Entrego cartas.", "Llamo a la puerta.", "Hablo con cortesía."], "Propósito: entregar cartas. Digo: «Tengo una carta para usted»."),
    ],
    [("Actuar sin pensar qué hace el rol.", "Se juega sin propósito.", "Pregúntate: ¿para qué sirve mi rol?"), ("Hablar solo yo.", "Se olvida que hay otro jugador.", "Escucha a tu compañero y responde.")],
    [
        E("El cartero, ¿entrega cartas o vende frutas?", "Entrega cartas", "Ese es su propósito."),
        E("La bibliotecaria, ¿presta libros o cobra tomates?", "Presta libros", "Cuida y presta libros."),
        E("¿Qué dice el vendedor: «¿Qué desea llevar?» o «¿Dónde le duele?»?", "¿Qué desea llevar?", "La otra frase es de la doctora."),
    ],
    [
        E("¿Qué es un rol?", "El papel que represento en un juego", "Es hacer como si fuera esa persona."),
        E("¿Qué es el propósito de un rol?", "Para qué sirve ese rol", "Dice qué hace la persona."),
        E("¿Por qué escucho a mi compañero en el juego?", "Para responderle y seguir la conversación", "Un juego se hace entre dos."),
    ],
    [
        E("Eres doctora. Escribe una pregunta que le harías a un niño.", "Por ejemplo: ¿Dónde te duele?", "Sirve para cuidar."),
        E("Eres bibliotecaria. Escribe cómo pides silencio con amabilidad.", "Por ejemplo: Hablemos bajito, por favor", "Cuida el silencio con cortesía."),
        E("Eres vendedor de pan. Escribe cómo ofreces pan.", "Por ejemplo: Buenos días, ¿le gustaría llevar pan fresco?", "Ofrece con cortesía."),
    ],
    [
        E("Pablo, que hace de cartero, entrega un libro de la biblioteca. ¿Cumple su rol?", "No", "El cartero entrega cartas."),
        E("Ana, que hace de vendedora, dice «Adiós» a un cliente sin cobrarle. ¿Cumple su rol?", "No", "La vendedora cobra lo que se lleva."),
    ],
    [
        E("Rol: bombero. ¿Cuál es su propósito: apagar incendios o repartir pan?", "Apagar incendios", "Cuida a las personas."),
        E("Rol: profesora. Escribe una frase que diría a su curso.", "Por ejemplo: Buenos días, hoy leeremos un cuento", "Inicia la clase."),
    ],
    [E("Juegas en casa a la tienda. Tu hermano es el cliente y tú el vendedor. Escribe cómo le dices el precio de dos manzanas y cómo lo despides.", "Por ejemplo: Dos manzanas son cuatro pesos; gracias, que le vaya bien", "Cumple el rol con cortesía.")],
    [
        E("¿Juego de roles es hacer como si fuera otra persona?", "Sí", "Se representa un papel."),
        E("¿Un rol tiene un propósito?", "Sí", "Dice para qué sirve."),
        E("¿Un jugador habla solo o se turna?", "Se turna", "Es un juego entre dos."),
    ],
    ("Juega con un adulto al juego de la tienda por 3 minutos. Uno es vendedor y otro cliente, y luego cambian. Usa estas frases: Vendedor: «¿Qué desea llevar?», «Son tantos pesos», «Gracias, hasta luego». Cliente: «Buenos días», «Quiero dos manzanas, por favor», «Gracias». Cada uno habla por turnos y escucha al otro.",
     "Vendedor (yo): Buenos días, ¿qué desea llevar? Cliente (mamá): Quiero dos manzanas, por favor. Yo: Son cuatro pesos. Mamá: Aquí tiene, gracias. Yo: Gracias, hasta luego. Luego cambiamos de rol.",
     ["cumple el propósito del rol", "habla por turnos", "usa frases de cortesía"], ["adulto observa el juego y anota qué rol cumplió"], ["no escuchar al otro", "no cumplir el rol"],
     "Si se sale del rol, pregúntale qué haría un vendedor de verdad y repite la escena."),
    "Juega a ser bibliotecaria con un muñeco y préstale un libro.",
    "Inventa un rol nuevo con su propósito y tres frases.",
)

reg(
    OA25, 2,
    "Las fichas de personajes escritas en este cuaderno, lápiz y hoja. Se juega con un adulto o un muñeco.",
    "Aprenderé a crear un personaje que trate bien a los demás. Sirve para jugar sin herir a nadie y para practicar cómo ser respetuoso.",
    ["Sé representar un rol.", "Sé decir por favor y gracias."],
    [
        "Un personaje es alguien que invento para el juego. Para construirlo pienso en cómo se llama, cómo habla, cómo se mueve y cómo trata a los demás. Si es un personaje respetuoso, saluda, escucha, dice por favor y gracias, y cuida a su compañero de juego.",
        "No todos los personajes tienen que ser iguales. Puedo inventar a Rosa, una vendedora amable, o a Don Pedro, un doctor tranquilo. Pueden ser graciosos o serios, pero no deben burlarse ni ofender a nadie. Jugar es divertido cuando todos se sienten bien.",
        "Una ficha de personaje tiene cuatro datos: nombre, rol, cómo habla y una frase que dice siempre. Por ejemplo: Nombre: Rosa. Rol: vendedora. Habla: suave y alegre. Frase: «¡Qué bueno verte!». Con la ficha puedo recordar cómo actuar mientras juego.",
    ],
    [("personaje", "alguien que invento para el juego"), ("respetuoso", "que trata bien a los demás"), ("ficha", "hoja con datos del personaje"), ("frase de personaje", "frase que dice siempre ese personaje"), ("burlarse", "reírse para ofender a otro")],
    [
        ("Armar una ficha", "Inventa un personaje: Rosa, vendedora amable. ¿Qué datos lleva su ficha?", ["Nombre: Rosa.", "Rol: vendedora.", "Habla suave y dice «¡Qué bueno verte!»."], "Nombre: Rosa. Rol: vendedora. Habla: suave. Frase: «¡Qué bueno verte!»."),
        ("Revisar el respeto", "Un personaje dice: «Eres lento, qué tonto». ¿Cómo lo cambias para que sea respetuoso?", ["La frase ofende.", "Pienso qué diría un personaje amable.", "La cambio."], "Con calma, ¿te ayudo?"),
    ],
    [("Hacer un personaje que se burla.", "Se cree que da risa.", "Haz que el personaje sea gracioso sin ofender."), ("Olvidar cómo habla el personaje.", "No se anota.", "Usa la ficha del personaje.")],
    [
        E("Un personaje respetuoso, ¿saluda o se burla?", "Saluda", "Trata bien a los demás."),
        E("¿Cuántos datos tiene la ficha: nombre, rol, cómo habla y frase?", "4", "Son cuatro datos."),
        E("Rosa dice «Qué bueno verte». ¿Es respetuosa o hiriente?", "Respetuosa", "Es una frase amable."),
    ],
    [
        E("¿Qué es una ficha de personaje?", "Una hoja con los datos del personaje", "Ayuda a recordar cómo actuar."),
        E("¿Por qué un personaje no debe burlarse?", "Porque ofende a los demás", "El juego debe ser sano."),
        E("¿Un personaje puede ser gracioso y respetuoso a la vez?", "Sí", "Se puede jugar sin ofender."),
    ],
    [
        E("Crea la ficha de un doctor: nombre, rol, cómo habla y frase. Usa el nombre Pedro.", "Por ejemplo: Nombre: Pedro. Rol: doctor. Habla: tranquilo. Frase: «No se preocupe»", "Tiene los cuatro datos."),
        E("Escribe una frase de saludo para un personaje respetuoso.", "Por ejemplo: Buenos días, ¿cómo está?", "Es una frase amable."),
        E("Cambia «Eres un tonto» por una frase respetuosa.", "Por ejemplo: Creo que te equivocaste, ¿lo revisamos?", "No ofende y ayuda."),
    ],
    [
        E("Teo hace un personaje que se burla de su compañero. El compañero se pone triste. ¿Fue un buen juego?", "No", "Nadie debe sentirse mal."),
        E("Rosa y Don Pedro son personajes distintos pero ambos amables. ¿Es posible?", "Sí", "Cada uno habla distinto."),
    ],
    [
        E("Un personaje dice siempre «Gracias por esperar». ¿Es una frase respetuosa o hiriente?", "Respetuosa", "Agradece a quien esperó."),
        E("Arma una frase de despedida para Rosa, la vendedora amable.", "Por ejemplo: Gracias por venir; vuelve pronto", "Incluye una frase cortés."),
    ],
    [E("Tu hermano menor quiere ser un lobo malo en el juego, y asusta a sus muñecos. ¿Cómo lo ayudas a convertirlo en un lobo que cuida?", "Por ejemplo: El lobo cuida a los muñecos y les da comida", "Cambia el rol a uno respetuoso.")],
    [
        E("¿Dónde anoto cómo habla mi personaje?", "En la ficha", "Ahí están sus datos."),
        E("¿Un personaje respetuoso dice por favor?", "Sí", "Es una fórmula de cortesía."),
        E("¿Puedo cambiar mi personaje si ofende?", "Sí", "Juego mejor si todos se sienten bien."),
    ],
    ("Crea la ficha de un personaje respetuoso para jugar a la tienda con un adulto. La ficha lleva: nombre (por ejemplo, Rosa, Pedro o Luz), rol (vendedor, doctor o bibliotecaria), cómo habla (suave, alegre o tranquilo) y una frase que siempre dice. Luego juega 2 minutos con ese personaje y pide al adulto que diga si fuiste respetuoso.",
     "Nombre: Luz. Rol: bibliotecaria. Habla: suave y tranquila. Frase: «Con cuidado, por favor». En el juego saludé, presté un libro y dije gracias. Mamá dijo que fui respetuosa.",
     ["completa los cuatro datos", "el personaje trata bien a todos", "usa la frase de personaje"], ["ficha escrita", "adulto observa el juego"], ["personaje que se burla", "ficha incompleta"],
     "Si el personaje ofende, pregunta cómo hablaría uno amable y cambia la frase."),
    "Inventa un personaje y muéstralo a un familiar.",
    "Crea una pareja de personajes respetuosos que trabajen juntos.",
)

reg(
    OA25, 3,
    "Las situaciones escritas en este cuaderno, lápiz y hoja. Se juega con un adulto o un compañero.",
    "Aprenderé a inventar lo que digo en el momento, escuchando a mi compañero. Sirve para que el juego fluya y los dos se sientan escuchados.",
    ["Sé representar un rol.", "Sé mostrar que escucho."],
    [
        "Improvisar es inventar lo que digo y hago en el momento, sin haberlo practicado antes. En un juego de roles improvisamos mucho. Pero para que funcione, hay que escuchar a nuestro compañero y aceptar lo que dice. Si él dice «aquí hay un tesoro», yo no digo «no hay nada»; puedo decir «sí, y lo desenterramos».",
        "Esa forma de improvisar se llama «sí, y…». Primero acepto lo que dijo («sí») y luego le agrego algo nuevo («y…»). Por ejemplo: Compañero: «Llegamos a una cueva». Yo: «Sí, y está muy oscura; saquemos la linterna». Así la historia crece entre los dos.",
        "Si me quedo sin ideas, puedo repetir lo último que dijo mi compañero o hacer una pregunta: «¿Qué hay adentro?». También puedo pedirle ayuda. Lo importante es escuchar y no cortar la historia.",
    ],
    [("improvisar", "inventar sobre la marcha, sin ensayar"), ("aceptar", "decir que sí a lo que propone otro"), ("agregar", "poner algo nuevo a la idea"), ("historia", "lo que vamos contando juntos"), ("idea", "algo que pienso y propongo")],
    [
        ("Aceptar y agregar", "Compañero: «Encontré un barco en la playa.» ¿Cómo respondes con «sí, y…»?", ["Acepto: sí, hay un barco.", "Agrego algo nuevo.", "Armo la frase."], "Sí, y tiene una vela roja."),
        ("Preguntar cuando me falta una idea", "Compañero: «Entramos a una cueva.» No sabes qué agregar. ¿Qué puedes decir?", ["Repito lo que dijo.", "Hago una pregunta.", "Mantengo la historia."], "¿Qué hay adentro de la cueva?"),
    ],
    [("Decir que no a todo.", "Se quiere dirigir la historia.", "Usa «sí, y…»."), ("Hablar sin escuchar.", "Se piensa en lo propio.", "Escucha lo último que dijo tu compañero.")],
    [
        E("Compañero: «Aquí hay un tesoro». ¿Respondo «No hay nada» o «Sí, y lo desenterramos»?", "Sí, y lo desenterramos", "Acepto y agrego."),
        E("¿La frase «sí, y…» acepta o rechaza?", "Acepta", "Empieza con sí."),
        E("Si no tengo ideas, ¿puedo hacer una pregunta?", "Sí", "Ayuda a seguir la historia."),
    ],
    [
        E("¿Qué es improvisar?", "Inventar en el momento", "No se ensaya antes."),
        E("¿Por qué es importante escuchar al improvisar?", "Para aceptar y agregar a su idea", "La historia es entre los dos."),
        E("¿Qué hago si me quedo sin ideas?", "Repito lo último o pregunto", "Sigo sin cortar la historia."),
    ],
    [
        E("Compañero: «Vimos un dragón pequeño». Escribe una respuesta con «Sí, y…».", "Por ejemplo: Sí, y tiene alas azules", "Acepta y agrega."),
        E("Compañero: «Estamos en la luna». Escribe una pregunta para seguir.", "Por ejemplo: ¿Qué hay en la luna?", "Mantiene la historia."),
        E("Compañero: «El tren llegó». Escribe una frase que acepte y agregue algo.", "Por ejemplo: Sí, y se bajaron cinco pasajeros", "Suma nueva información."),
    ],
    [
        E("Compañero: «Encontré una llave.» Tú: «No, eso no existe». ¿Qué ocurre con el juego?", "Se corta la historia", "No aceptaste su idea."),
        E("Compañero: «Hay una puerta.» Tú: «Sí, y está cerrada con candado». ¿Hiciste bien?", "Sí", "Aceptaste y agregaste."),
    ],
    [
        E("Diálogo: A: «Voy a la selva.» B: «Sí, y llevo mi mochila.» A: «Sí, y…» ¿Qué debe hacer A?", "Aceptar y agregar algo nuevo", "Sigue el patrón sí, y."),
        E("Compañero: «Nos perdimos en el bosque». Escribe tres cosas que puedes agregar usando «sí, y…» (separadas por coma).", "Por ejemplo: Sí, y hay un camino; sí, y se oye un río; sí, y vemos humo", "Cada una agrega información."),
    ],
    [E("Juegas con tu prima: ella dice «Soy una astronauta y vamos a Marte». Escribe cómo continúas aceptando y agregando.", "Por ejemplo: Sí, y yo manejo la nave con un volante grande", "Acepta y agrega.")],
    [
        E("¿Digo «no» a todo lo que propone mi compañero?", "No", "La historia se detiene."),
        E("¿Qué empieza a decir quien acepta?", "Sí", "Acepta la idea."),
        E("¿Escucho lo último que dijo mi compañero?", "Sí", "Así continúo bien."),
    ],
    ("Improvisa con un adulto durante 2 minutos con este comienzo: «Estamos en una cueva y encontramos una caja». Alternen frases: uno dice una frase, el otro responde con «Sí, y…» y agrega algo. Hagan al menos 5 intercambios. Pide al adulto que cuente cuántas veces usaste «sí, y…».",
     "Adulto: Estamos en una cueva y hay una caja. Yo: Sí, y brilla. Adulto: Sí, y está cerrada. Yo: Sí, y tiene una llave en la tapa. Usé «sí, y» tres veces.",
     ["acepta lo que dice el otro", "agrega algo nuevo", "completa cinco intercambios"], ["adulto cuenta cuántas veces usó «sí, y…»"], ["decir que no", "no agregar nada"],
     "Si dice no, pídele que repita lo último que dijo su compañero y agregue algo."),
    "Juega a «sí, y…» con alguien de tu casa por un minuto.",
    "Improvisa con dos compañeros una historia de cinco frases.",
)

reg(
    OA25, 4,
    "Las escenas escritas en este cuaderno, lápiz y hoja. Se juega con un adulto o compañero.",
    "Aprenderé a resolver un problema de una escena trabajando juntos. Sirve para cooperar y para que la historia tenga un final.",
    ["Sé improvisar con «sí, y…».", "Sé representar un rol."],
    [
        "Muchas escenas tienen un problema: un perro perdido, una puerta que no abre, una tienda sin pan. En el juego de roles, los personajes resuelven el problema trabajando juntos. Cada uno propone una idea, escucha la del otro y deciden en equipo.",
        "Para resolver juntos puedes seguir tres pasos: nombrar el problema, proponer una solución cada uno y escoger una o unir las dos. Por ejemplo: problema, el gato está en un árbol. Idea 1: llamar a un bombero. Idea 2: traer una escalera. Pueden unir: el bombero trae la escalera.",
        "Para que funcione, usa frases de cooperación: «Yo propongo que…», «¿Qué te parece si…?», «Estoy de acuerdo». Si no estás de acuerdo, di por qué con respeto. Al final, la escena termina cuando el problema se resuelve y todos quedan contentos con la solución.",
    ],
    [("problema", "lo que complica la escena"), ("solución", "lo que arregla el problema"), ("equipo", "personas que trabajan juntas"), ("proponer", "sugerir una idea"), ("estar de acuerdo", "pensar igual que otro")],
    [
        ("Resolver un problema", "Problema: un gato está en un árbol. Idea 1: llamar a un bombero. Idea 2: traer una escalera. ¿Cómo resuelven juntos?", ["Nombro el problema.", "Cada uno propone.", "Unen las ideas."], "El bombero trae una escalera y baja al gato."),
        ("Usar frases de cooperación", "Un compañero propone una idea. Tú estás de acuerdo. ¿Qué dices?", ["Escucho la idea.", "Digo que estoy de acuerdo.", "Agrego algo."], "Estoy de acuerdo; yo sostengo la escalera."),
    ],
    [("Querer resolver solo.", "No se escucha al compañero.", "Pregunta: ¿qué te parece si…?"), ("Cerrar la escena sin resolver.", "Falta tiempo o ideas.", "Busca una solución antes del final.")],
    [
        E("El problema de la escena es «el perro se perdió». ¿Cuál es una solución: buscarlo juntos o dormir?", "Buscarlo juntos", "Resuelve el problema."),
        E("Para resolver en equipo, ¿escucho al otro?", "Sí", "Es necesario cooperar."),
        E("«¿Qué te parece si…?» es una frase de ¿cooperación o pelea?", "Cooperación", "Pregunta la opinión del otro."),
    ],
    [
        E("¿Qué es un problema en una escena?", "Lo que complica la historia", "Hay que resolverlo."),
        E("¿Por qué conviene unir las ideas de los dos?", "Porque ambos participan", "Se aprovechan las ideas de todos."),
        E("¿Cuándo termina la escena?", "Cuando el problema se resuelve", "Es el final lógico."),
    ],
    [
        E("Problema: no hay pan en la tienda. Escribe una idea para resolverlo.", "Por ejemplo: Hornear pan o pedirlo a la panadería", "Resuelve la falta."),
        E("Compañero: «Yo propongo que busquemos al perro por el parque». Escribe cómo respondes si estás de acuerdo.", "Por ejemplo: Estoy de acuerdo; yo reviso los árboles", "Acepta y suma."),
        E("Escribe una frase para proponer una idea con respeto.", "Por ejemplo: Yo propongo que llamemos a un adulto", "Usa una frase de cooperación."),
    ],
    [
        E("Pedro quiere resolver todo solo y no escucha. ¿Es un buen trabajo en equipo?", "No", "Falta escuchar al compañero."),
        E("Rosa dice «No me gusta tu idea» sin explicar. ¿Cómo mejorar?", "Decir por qué y proponer otra", "Así se coopera."),
    ],
    [
        E("Problema: una niña perdió su paraguas. Idea A: buscar. Idea B: usar un impermeable. Une las ideas en una frase.", "Por ejemplo: Buscan el paraguas y mientras usan un impermeable", "Combina las ideas."),
        E("Ordena los pasos para resolver: a) escoger o unir ideas, b) nombrar el problema, c) proponer ideas. Escribe las letras.", "b, c, a", "Primero el problema, luego ideas y después decidir."),
    ],
    [E("En el juego de la veterinaria, un perro muñeco tiene una pata dañada. Tú eres el veterinario y tu hermano el dueño. Escribe cómo resuelven juntos.", "Por ejemplo: Yo le pongo una venda en la pata, tú le das el remedio y lo cargas", "Cooperan para resolver.")],
    [
        E("¿Cada uno propone una idea en equipo?", "Sí", "Así se resuelve mejor."),
        E("¿«Estoy de acuerdo» muestra que acepto la idea?", "Sí", "Dice que pienso igual."),
        E("¿Una escena puede terminar sin resolver el problema?", "No", "Sería un final incompleto."),
    ],
    ("Juega con un adulto esta escena: «El perro de la vecina se escapó». Primero nombren el problema, luego cada uno propone una idea (por ejemplo: buscarlo en el parque, llamar a la vecina, poner un cartel) y decidan juntos cómo resolverlo. Usa al menos dos frases de cooperación: «Yo propongo que…», «¿Qué te parece si…?» o «Estoy de acuerdo».",
     "Yo: El perro se escapó. Yo propongo que lo busquemos en el parque. Adulto: ¿Qué te parece si primero llamamos a la vecina? Yo: Estoy de acuerdo. Lo llamamos y luego lo buscamos juntos. Encontramos al perro.",
     ["nombra el problema", "propone una idea", "usa dos frases de cooperación", "llegan a una solución"], ["escena actuada", "adulto marca las frases de cooperación"], ["resolver solo", "no escuchar al otro"],
     "Si no coopera, pide que pregunte «¿qué te parece si…?» al compañero antes de decidir."),
    "Resuelve en casa un pequeño problema con un familiar usando «¿Qué te parece si…?».",
    "Cambia el problema de la escena y propone una solución nueva.",
)

reg(
    OA25, 5,
    "La pauta de este cuaderno, lápiz y hoja. Se juega con dos o tres personas de la casa, que serán el público.",
    "Aprenderé a presentar una escena de roles y a dar y recibir comentarios amables. Sirve para mejorar y para sentirme más seguro hablando.",
    ["Sé crear un personaje respetuoso, improvisar y resolver una escena."],
    [
        "Una representación es mostrar la escena a otras personas. Antes de actuar, se acuerda quiénes son los personajes, cuál es el problema y cómo se resuelve. Durante la escena se habla claro, se escucha al compañero y se usa el cuerpo para ayudar al rol.",
        "Al terminar, el público da un comentario. Un comentario amable tiene tres partes: algo que me gustó, algo que puedo mejorar y una sugerencia concreta. Por ejemplo: «Me gustó que hablaste claro. Puedes mirar más al público. Intenta levantar la cabeza».",
        "Quien recibe el comentario escucha sin enojarse y dice «gracias». Después puede repetir la escena mejorando una cosa. Con retroalimentación amable, todos aprendemos y ganamos confianza.",
    ],
    [("representar", "mostrar una escena a otros"), ("comentario", "opinión para ayudar a mejorar"), ("sugerencia", "idea para hacerlo mejor"), ("público", "personas que miran"), ("confianza", "sentirme seguro")],
    [
        ("Dar un comentario amable", "Viste una escena de la tienda. Hablaron claro pero no miraron al público. ¿Cómo lo dices?", ["Digo qué me gustó.", "Digo qué puede mejorar.", "Doy una sugerencia."], "Me gustó que hablaron claro; pueden mirar más al público, levantando la cabeza."),
        ("Recibir un comentario", "Te dicen: «Habla un poco más fuerte». ¿Qué respondes?", ["Escucho sin enojarme.", "Digo gracias.", "Pienso cómo mejorar."], "Gracias; hablaré más fuerte."),
    ],
    [("Criticar sin decir qué mejorar.", "Solo se dice «no me gustó».", "Usa las tres partes del comentario."), ("Enojarse con el comentario.", "Se siente como crítica.", "Recuerda que ayuda a mejorar.")],
    [
        E("¿Cuántas partes tiene un comentario amable: lo que gustó, lo que mejorar y una sugerencia?", "3", "Son tres partes."),
        E("Si me dan un comentario, ¿digo «gracias»?", "Sí", "Es un gesto respetuoso."),
        E("¿Una sugerencia sirve para mejorar?", "Sí", "Ofrece una idea concreta."),
    ],
    [
        E("¿Para qué sirve un comentario después de actuar?", "Para mejorar la próxima vez", "Ayuda a crecer."),
        E("¿Por qué conviene empezar por lo que gustó?", "Porque anima a la persona", "Se valora lo bueno primero."),
        E("¿Qué hago después de recibir un comentario?", "Puedo repetir mejorando algo", "Aplico la sugerencia."),
    ],
    [
        E("Viste actuar a Ana, que habló bajito. Escribe un comentario amable con las tres partes.", "Por ejemplo: Me gustó tu personaje; puedes hablar más fuerte; respira antes de hablar", "Incluye gusto, mejora y sugerencia."),
        E("Escribe qué responderías si te dicen «Te moviste mucho».", "Por ejemplo: Gracias, me moveré menos la próxima vez", "Recibe con calma."),
        E("Escribe una sugerencia para un compañero que habla muy rápido.", "Por ejemplo: Habla más despacio y respira entre frases", "Es una sugerencia concreta."),
    ],
    [
        E("Luis comenta: «Fue horrible». ¿Es un comentario amable?", "No", "No dice nada útil ni amable."),
        E("Rosa comenta: «Me gustó tu voz; puedes mirar más al público; mira un punto lejos de ti». ¿Tiene las tres partes?", "Sí", "Tiene gusto, mejora y sugerencia."),
    ],
    [
        E("Después de actuar, tu grupo sugiere: «Usen más gestos». Escribe cómo lo aplicarías en la próxima escena.", "Por ejemplo: Abriré los brazos para mostrar sorpresa", "Aplica la sugerencia."),
        E("Ordena: a) comentario, b) representar, c) repetir mejorando. Escribe las letras en orden.", "b, a, c", "Se actúa, se comenta y se mejora."),
    ],
    [E("Tu familia vio tu escena de la tienda. Tu papá dijo: «Me gustó que fuiste amable. Puedes hablar más fuerte. Respira antes de empezar». ¿Qué le respondes y qué harás?", "Por ejemplo: Gracias, papá; hablaré más fuerte respirando antes", "Agradece y aplica.")],
    [
        E("¿Cómo debe ser un comentario: amable o hiriente?", "Amable", "Debe ayudar a mejorar."),
        E("¿Puedo repetir la escena para mejorarla?", "Sí", "Aplico lo aprendido."),
        E("¿Ayuda el comentario a tener más confianza?", "Sí", "Aprendo a hacerlo mejor."),
    ],
    ("Representa con un adulto o con dos personas de público esta escena (2 minutos): «Una niña llega a la biblioteca y quiere un libro de animales; la bibliotecaria no lo encuentra y juntas lo buscan». Al terminar, el público te da un comentario con las tres partes: lo que gustó, lo que mejorar y una sugerencia. Responde «gracias» y repite la escena mejorando una cosa.",
     "Representé la escena. Mamá dijo: Me gustó tu voz suave. Puedes mirar más a quien hablas. Intenta levantar la cabeza. Yo dije: Gracias. Repetí la escena y miré más a la bibliotecaria.",
     ["actúa su rol", "recibe el comentario con gracias", "mejora una cosa al repetir"], ["escena actuada", "comentario del público", "segunda versión"], ["enojarse", "repetir sin cambiar nada"],
     "Si no mejoró nada, toma una sola sugerencia del público y repite concentrado en ella."),
    "Dale a un familiar un comentario amable con tres partes.",
    "Actúa la escena con otro rol y cuenta qué cambió.",
)

# ================================================================ OA 26
reg(
    OA26, 1,
    "Los poemas y las rimas escritos en este cuaderno, lápiz y hoja. Un adulto puede leerlos en voz alta.",
    "Aprenderé a comprender un poema antes de recitarlo. Sirve para decirlo con sentido y para que quien escucha lo entienda y lo disfrute.",
    ["Sé escuchar un poema.", "Sé que hay palabras que riman."],
    [
        "Un poema es un texto breve que cuenta algo con belleza. Se escribe en versos, que son las líneas, y los versos se agrupan en estrofas. Algunos poemas tienen rimas, que son palabras que terminan con sonidos iguales, como ventana y mañana.",
        "Antes de recitar, hay que entender de qué trata. Me pregunto: ¿quién habla? ¿qué cuenta? ¿cómo se siente? ¿hay palabras que no entiendo? Por ejemplo, el poema «La lluvia» dice: «La lluvia cantora / golpea la ventana. / Mi gato la mira / desde la mañana». Trata de una lluvia y un gato curioso.",
        "Recitar es decir un poema de memoria o leyéndolo con voz clara y con sentimiento. Cuando entiendo el poema, sé dónde hacer una pausa y cómo decir cada verso: con ternura, con alegría o con calma. Comprender primero es el secreto de una buena recitación.",
    ],
    [("poema", "texto en verso que expresa algo con belleza"), ("verso", "cada línea de un poema"), ("estrofa", "grupo de versos"), ("rima", "palabras que terminan con sonidos iguales"), ("recitar", "decir un poema con voz y sentimiento")],
    [
        ("Entender el poema", "«La lluvia cantora / golpea la ventana. / Mi gato la mira / desde la mañana.» ¿De qué trata?", ["Leo los cuatro versos.", "La lluvia golpea la ventana.", "El gato mira la lluvia."], "Trata de la lluvia y de un gato que la mira."),
        ("Encontrar la rima", "En el mismo poema, ¿qué palabras riman?", ["Miro el final de los versos.", "Ventana termina en -ana.", "Mañana termina en -ana."], "Ventana y mañana."),
    ],
    [("Recitar sin entender.", "Se memorizan solo palabras.", "Primero pregunta qué cuenta el poema."), ("Confundir verso con estrofa.", "Parecen lo mismo.", "Verso es una línea; estrofa es un grupo.")],
    [
        E("En «La lluvia cantora / golpea la ventana», ¿cuántos versos hay?", "2", "Hay dos líneas."),
        E("¿Ventana rima con mañana?", "Sí", "Ambas terminan en -ana."),
        E("En el poema de la lluvia, ¿qué mira el gato?", "La lluvia", "El poema dice que la mira."),
    ],
    [
        E("¿Qué es un verso?", "Cada línea de un poema", "Los versos forman estrofas."),
        E("¿Por qué conviene entender el poema antes de recitar?", "Para decirlo con sentido", "Sé cómo darle voz."),
        E("En Lenguaje, ¿qué es una rima?", "Palabras que terminan con sonidos iguales", "Por ejemplo ventana y mañana."),
    ],
    [
        E("Lee: «El sapo en el charco / cantaba una canción; / la luna lo escuchaba / con mucha atención». ¿Qué palabras riman?", "canción y atención", "Terminan en -ión."),
        E("En el poema del sapo, ¿quién escucha al sapo?", "La luna", "El poema lo dice."),
        E("En el poema del sapo, ¿cuántos versos tiene la estrofa?", "4", "Son cuatro líneas."),
    ],
    [
        E("Ana dice que el poema de la lluvia trata de un perro. ¿Entendió bien?", "No, trata de un gato y la lluvia", "El gato mira la lluvia."),
        E("Beto recita el poema del sapo muy rápido y sin pensar. ¿Qué le falta?", "Entender de qué trata", "Comprender permite decirlo bien."),
    ],
    [
        E("En el poema del sapo, ¿qué siente la luna: atención o miedo?", "Atención", "El poema dice «con mucha atención»."),
        E("Escribe una pregunta que ayude a entender un poema.", "Por ejemplo: ¿De qué trata el poema?", "Sirve para comprender."),
    ],
    [E("Tu profesora te pide recitar el poema de la lluvia. Antes de hacerlo, escribe dos preguntas que te harás para comprender.", "Por ejemplo: ¿Qué hace la lluvia? ¿Qué hace el gato?", "Ayudan a entender el poema.")],
    [
        E("¿Leo el poema completo antes de recitarlo?", "Sí", "Así entiendo mejor."),
        E("¿Ventana termina como mañana?", "Sí", "Terminan en -ana."),
        E("¿Qué pregunto: quién habla, qué cuenta o cómo se siente?", "Todas", "Las tres ayudan a comprender."),
    ],
    ("Lee el poema «La lluvia» (un adulto lo lee primero en voz alta): «La lluvia cantora / golpea la ventana. / Mi gato la mira / desde la mañana». Responde por escrito o en voz alta: 1) ¿De qué trata? 2) ¿Qué palabras riman? 3) ¿Cómo se siente el poema: alegre, triste o tranquilo? Explica por qué.",
     "1) Trata de la lluvia que golpea la ventana y de mi gato que la mira. 2) Riman ventana y mañana. 3) Se siente tranquilo porque el gato mira la lluvia con calma.",
     ["dice de qué trata", "encuentra la rima", "explica cómo se siente"], ["tres respuestas escritas o dichas"], ["no explicar", "confundir rima"],
     "Si no explica el sentimiento, pide que lea de nuevo un verso y diga qué le hace sentir."),
    "Lee el poema del sapo a un familiar y cuéntale de qué trata.",
    "Escribe una pregunta propia sobre cada poema.",
)

reg(
    OA26, 2,
    "Los trabalenguas y las rimas escritos en este cuaderno. Un adulto escucha. No se necesita nada más.",
    "Aprenderé a decir trabalenguas y rimas con ritmo y pronunciando claro. Sirve para hablar con más seguridad y para jugar con las palabras.",
    ["Sé que hay palabras que riman.", "Sé separar palabras en sílabas."],
    [
        "El ritmo es la música que tienen las palabras al decirlas. En un poema, el ritmo viene de las sílabas y de las pausas. Para sentir el ritmo, puedes dar palmadas por cada sílaba. Por ejemplo, «ven-ta-na» tiene tres palmadas.",
        "Los trabalenguas son frases difíciles de decir porque repiten sonidos parecidos. Un ejemplo es: «Pablo pela papas pálidas para papá» (pálidas quiere decir de color muy claro). Para decirlo bien, se empieza muy despacio, abriendo la boca y pronunciando cada p. Luego se acelera de a poco, sin comerse las sílabas.",
        "La articulación es mover bien la boca, los labios y la lengua para decir claro cada sonido. Si me equivoco, no pasa nada: vuelvo a empezar más despacio. Con práctica, mi lengua aprende y puedo decir el trabalenguas más rápido sin perder claridad.",
    ],
    [("ritmo", "la música que forman las sílabas y las pausas"), ("trabalenguas", "frase difícil de decir por sus sonidos repetidos"), ("articular", "mover la boca para decir claro cada sonido"), ("sílaba", "parte de una palabra"), ("pausa", "pequeño silencio al hablar")],
    [
        ("Sentir el ritmo", "Da una palmada por sílaba en «ven-ta-na». ¿Cuántas palmadas?", ["Separo en sílabas.", "Cuento: ven, ta, na.", "Son tres."], "3 palmadas"),
        ("Decir un trabalenguas", "Trabalenguas: «Pablo pela papas pálidas para papá». ¿Cómo lo digo bien?", ["Empiezo muy despacio.", "Abro la boca en cada p.", "Acelero poco a poco."], "Lo digo despacio, marcando cada p, y subo la velocidad de a poco."),
    ],
    [("Empezar muy rápido.", "Se quiere ganar.", "Empieza despacio."), ("Comerse sílabas.", "Se apura el habla.", "Marca cada sílaba.")],
    [
        E("¿Cuántas sílabas tiene «papá»?", "2", "Se separa pa, pá."),
        E("¿Cómo empiezo un trabalenguas: rápido o despacio?", "Despacio", "Así lo pronuncio bien."),
        E("¿Cuántas palmadas doy en «pa-pas»?", "2", "Una por sílaba."),
    ],
    [
        E("En Lenguaje: ¿Qué es un trabalenguas?", "Una frase difícil de decir por sus sonidos repetidos", "Se parece a un juego de lengua."),
        E("¿Qué significa articular?", "Mover bien la boca para decir claro", "Ayuda a pronunciar cada sonido."),
        E("¿Para qué sirven las pausas?", "Para dar ritmo y respirar", "Marcan los tiempos."),
    ],
    [
        E("Trabalenguas: «La rana Rosa rasca la rama rugosa» (rugosa quiere decir áspera). ¿Qué sonido se repite mucho?", "La r", "Aparece en rana, Rosa, rasca, rama y rugosa."),
        E("En «La rana Rosa rasca la rama rugosa», ¿cuántas palabras hay?", "7", "Cuento: la, rana, Rosa, rasca, la, rama, rugosa."),
        E("Trabalenguas: «Tito toma té tibio tras el trote». Separa en sílabas «tibio».", "ti-bio", "Tiene dos sílabas."),
    ],
    [
        E("Beto dice el trabalenguas muy rápido y se equivoca. ¿Qué le conviene?", "Hacerlo más despacio", "Así articula mejor."),
        E("Luz dice «Pablo pela papas» comiéndose las sílabas. ¿Qué mejorar?", "Pronunciar todas las sílabas", "Debe marcar cada sílaba."),
    ],
    [
        E("¿Cuántas palabras empiezan con p en «Pablo pela papas pálidas para papá»?", "6", "Pablo, pela, papas, pálidas, para y papá."),
        E("Rima: «gato» y ¿qué palabra rima: plato o puerta?", "Plato", "Terminan en -ato."),
    ],
    [E("Tu abuelo te pide decir un trabalenguas de memoria para reírse un rato. Escribe cómo practicas para decirlo bien.", "Por ejemplo: Lo digo muy despacio, abriendo la boca, y acelero de a poco", "Describe el método.")],
    [
        E("¿Doy palmadas para sentir el ritmo?", "Sí", "Una por sílaba."),
        E("¿Un trabalenguas se aprende de una vez?", "No, se practica", "Requiere mucha práctica."),
        E("¿Qué hago si me equivoco?", "Vuelvo a empezar más despacio", "La práctica ayuda."),
    ],
    ("Aprende este trabalenguas y dilo a un adulto con ritmo y claridad: «Tito toma té tibio tras el trote». Pasos: 1) lo repites 3 veces muy despacio, 2) das una palmada por sílaba, 3) lo dices a velocidad normal 3 veces. Luego repite este otro: «La rana Rosa rasca la rama rugosa».",
     "Practiqué 3 veces despacio. Di palmadas: ti-to to-ma té ti-bio tras el tro-te. Lo dije a velocidad normal sin equivocarme. Luego dije el de la rana sin comerme las r.",
     ["pronuncia claro", "mantiene el ritmo", "practica con pasos"], ["adulto escucha y confirma que se entendió"], ["empezar muy rápido", "comerse sílabas"],
     "Si se enreda, practica solo la parte difícil, muy despacio, y luego junta todo."),
    "Practica el trabalenguas de la rana tres veces con palmadas.",
    "Inventa un trabalenguas corto con la letra s.",
)

reg(
    OA26, 3,
    "Los poemas con signos de este cuaderno. Un adulto lo escucha y puede mostrar con su cara cómo se siente.",
    "Aprenderé a usar la entonación, las pausas y las emociones al recitar. Sirve para que el poema suene vivo y quien me escucha lo sienta.",
    ["Sé leer un verso corto.", "Sé que los signos ¿? y ¡! cambian cómo se dice."],
    [
        "La entonación es el sube y baja de la voz al hablar. Cuando preguntamos, la voz sube al final: «¿Dónde estás?». Cuando exclamamos, decimos con fuerza y emoción: «¡Qué lindo día!». Los signos ¿? y ¡! nos indican cómo decir.",
        "Las pausas son pequeños silencios. Una pausa corta se hace en una coma, y una más larga en un punto. Hacer pausas ayuda a respirar y a que el público entienda. En el poema «Dime, luna, ¿dónde vas? / ¡Qué alta estás!», la pregunta sube y la exclamación se dice con asombro.",
        "También ayudan los sentimientos. Si el poema es alegre, la voz es brillante; si es triste, es suave y lenta; si es asombro, es abierta y fuerte. Piensa en el sentimiento antes de decirlo y tu voz lo mostrará solita.",
    ],
    [("entonación", "sube y baja de la voz"), ("pausa", "pequeño silencio al hablar"), ("signos de exclamación", "¡ y !, indican emoción"), ("signos de interrogación", "¿ y ?, indican pregunta"), ("asombro", "sorpresa por algo admirable")],
    [
        ("Subir la voz en una pregunta", "Verso: «¿Dónde estás, luna?». ¿Cómo lo dices?", ["Veo los signos ¿?.", "Es una pregunta.", "Subo la voz al final."], "Lo digo con la voz subiendo al final."),
        ("Exclamar con asombro", "Verso: «¡Qué alta estás!». ¿Cómo lo dices?", ["Veo los signos ¡!.", "Hay asombro.", "Uso una voz abierta y fuerte."], "Lo digo con asombro y fuerza."),
    ],
    [("Decir todo con la misma voz.", "No se piensa en el sentimiento.", "Cambia la voz según el signo."), ("No hacer pausas.", "Se tiene prisa.", "Respira y haz pausas en comas y puntos.")],
    [
        E("¿Los signos ¿? indican pregunta o exclamación?", "Pregunta", "Son signos de interrogación."),
        E("¿Los signos ¡! indican pregunta o exclamación?", "Exclamación", "Son signos de exclamación."),
        E("¿Dónde hago una pausa más larga: en la coma o en el punto?", "En el punto", "El punto es una pausa larga."),
    ],
    [
        E("¿Qué es la entonación?", "El sube y baja de la voz", "Da vida al poema."),
        E("¿Qué logro al hacer pausas al recitar?", "Respirar y que me entiendan", "Ordenan lo que digo."),
        E("En una pregunta, ¿la voz sube o baja al final?", "Sube", "Marca que se pregunta."),
    ],
    [
        E("Verso: «¡Qué linda mañana!». ¿Cómo lo dices: con asombro o con tristeza?", "Con asombro", "El verso muestra una emoción alegre."),
        E("Verso: «Dime, luna, ¿dónde vas?». ¿Subes la voz en la pregunta?", "Sí", "Los signos ¿? lo indican."),
        E("Verso: «Duerme, duerme, sol cansado». ¿Cómo lo dices: suave o muy fuerte?", "Suave", "Habla de dormir."),
    ],
    [
        E("Rosa recita «¡Qué alta estás!» con voz plana, sin emoción. ¿Qué mejorar?", "Usar asombro en la voz", "Los signos ¡! indican emoción."),
        E("Teo recita un poema triste con voz muy alegre. ¿Combina el sentimiento con la voz?", "No", "Un poema triste pide voz suave."),
    ],
    [
        E("Poema: «Duerme el sol en el cerro. / ¡Qué calma, qué calma! / ¿Quién guarda su sueño? / La luna en su cama.» ¿Qué verso tiene exclamación?", "¡Qué calma, qué calma!", "Tiene signos ¡!."),
        E("En el mismo poema, ¿qué verso tiene pregunta?", "¿Quién guarda su sueño?", "Tiene signos ¿?."),
    ],
    [E("Vas a recitar «Duerme el sol en el cerro» a un niño que no puede dormir. Escribe cómo usarás tu voz y tus pausas.", "Por ejemplo: voz suave y lenta, con pausas largas en los puntos", "Combina voz y sentimiento.")],
    [
        E("¿Respiro en las pausas?", "Sí", "Así me alcanza el aire."),
        E("¿Cambio la voz según el sentimiento?", "Sí", "Hace vivo el poema."),
        E("¿Qué indican los signos ¿?", "Una pregunta", "La voz sube al final."),
    ],
    ("Recita en voz alta al adulto este poema: «Duerme el sol en el cerro. / ¡Qué calma, qué calma! / ¿Quién guarda su sueño? / La luna en su cama». Marca antes con lápiz: las pausas con una raya, la pregunta con una flecha hacia arriba y la exclamación con un círculo. Luego recítalo con voz suave y emocionada.",
     "Marqué: pausa después de cerro. Círculo en ¡Qué calma, qué calma! Flecha hacia arriba en ¿Quién guarda su sueño? Recité despacio con voz suave. El adulto dijo que se sintió calma.",
     ["hace pausas", "sube la voz en la pregunta", "usa emoción en la exclamación"], ["poema marcado", "recitación escuchada por un adulto"], ["voz plana", "no hacer pausas"],
     "Si usa voz plana, pide que cierre los ojos, sienta el poema y lo diga de nuevo."),
    "Practica decir una pregunta y una exclamación de tu casa con distinta voz.",
    "Recita el mismo verso como alegre, triste y asombrado.",
)

reg(
    OA26, 4,
    "El poema y la adivinanza escritos en este cuaderno. Se practica con un adulto como ayudante.",
    "Aprenderé a ensayar un poema con ayudas que se retiran poco a poco. Sirve para recitar de memoria sin miedo.",
    ["Sé comprender un poema y decirlo con ritmo y entonación."],
    [
        "Recitar bien requiere ensayar. Una forma segura de aprender un poema es con apoyos que se van quitando de a poco. Primero lo lees con el texto delante. Luego lo dices mirando el texto solo cuando necesitas. Después lo dices con ayuda de las primeras palabras. Por último, lo recitas de memoria.",
        "Estos son los pasos: 1) lee el poema en voz alta tres veces; 2) di cada verso mirando el papel; 3) tapa el poema y di un verso a la vez; 4) di toda la estrofa de memoria; 5) recita el poema entero. Si te olvidas, no pasa nada: mira el texto y sigue.",
        "Para recordar, puedes asociar cada verso a un dibujo o a un gesto. Por ejemplo, en «Dime, luna, ¿dónde vas?», señala el cielo. Los gestos y los dibujos ayudan a que la memoria encuentre las palabras.",
    ],
    [("ensayar", "practicar antes de presentar"), ("memorizar", "aprender para decir sin leer"), ("apoyo", "ayuda que se usa y luego se retira"), ("estrofa", "grupo de versos"), ("gesto", "movimiento que ayuda a recordar")],
    [
        ("Pasos de ensayo", "Tienes el poema «La lluvia». ¿Qué haces primero?", ["Lo leo en voz alta.", "Lo repito tres veces.", "Después tapo el texto."], "Primero lo leo en voz alta tres veces."),
        ("Usar un gesto", "En el verso «La lluvia cantora» quieres recordar. ¿Qué gesto puedes hacer?", ["Pienso en la lluvia.", "Muevo los dedos hacia abajo.", "El gesto me recuerda el verso."], "Muevo los dedos como gotas que caen."),
    ],
    [("Aprender todo de una vez.", "Se quiere terminar rápido.", "Practica en pasos."), ("Quitar el texto muy pronto.", "Se confía mucho.", "Retira el apoyo poco a poco.")],
    [
        E("¿Qué hago primero para aprender un poema: leerlo o taparlo?", "Leerlo", "Primero necesito conocerlo."),
        E("¿Los gestos pueden ayudar a recordar?", "Sí", "Asocian palabra y movimiento."),
        E("Si me olvido en el ensayo, ¿miro el texto y sigo?", "Sí", "No pasa nada."),
    ],
    [
        E("¿Qué es un apoyo en el ensayo?", "Una ayuda que se usa y luego se retira", "Por ejemplo, el texto escrito."),
        E("¿Por qué se quitan los apoyos de a poco?", "Para ganar seguridad", "Se aprende paso a paso."),
        E("¿Cuántos pasos tiene el ensayo de esta clase?", "5", "Son cinco pasos de ensayo."),
    ],
    [
        E("Poema: «El sapo en el charco / cantaba una canción». Escribe un gesto para el primer verso.", "Por ejemplo: dos manos como boca de sapo", "El gesto recuerda el verso."),
        E("Adivinanza: «Tengo hojas y no soy libro, tengo tronco y no soy gato; doy sombra en el verano. ¿Quién soy?». Escribe la respuesta.", "El árbol", "Tiene hojas, tronco y da sombra."),
        E("Adivinanza: «Tiene cuatro patas y no camina; tiene respaldo y no es persona; te sientas en ella». ¿Qué es?", "Una silla", "Tiene patas y respaldo."),
    ],
    [
        E("Eva tapó el poema desde el primer ensayo y se olvidó de todo. ¿Qué pudo hacer?", "Volver a leerlo y retirar el apoyo de a poco", "Los apoyos se quitan despacio."),
        E("Teo practicó cinco veces, cada vez sin mirar un verso más. ¿Aprende mejor así?", "Sí", "Retira el apoyo gradualmente."),
    ],
    [
        E("Ordena los pasos: a) tapo y digo la estrofa, b) leo tres veces, c) recito entero. Escribe las letras.", "b, a, c", "Primero leo, luego tapo y al final recito."),
        E("Escribe una adivinanza propia con la respuesta «luna» (dos versos).", "Por ejemplo: Brilla en la noche, redonda y blanca; cambia de forma. ¿Quién es?", "Describe la luna sin nombrarla."),
    ],
    [E("Mañana recitarás el poema de la lluvia a tu curso. Hoy tienes media hora. Escribe tu plan de ensayo en tres pasos.", "Por ejemplo: leerlo tres veces; decirlo tapando una parte; recitarlo de memoria", "Plan con apoyo gradual.")],
    [
        E("¿Practico en un solo intento o por pasos?", "Por pasos", "Así se aprende mejor."),
        E("¿Un dibujo puede ayudarme a recordar?", "Sí", "Une imagen y palabra."),
        E("¿Retiro el apoyo de golpe?", "No, de a poco", "Se gana confianza."),
    ],
    ("Ensaya en 5 pasos el poema «El sapo en el charco / cantaba una canción; / la luna lo escuchaba / con mucha atención». 1) Léelo tres veces en voz alta. 2) Dilo mirando el papel. 3) Tapa el poema y di un verso a la vez. 4) Di toda la estrofa de memoria. 5) Recítalo al adulto. Anota qué apoyo usaste en cada paso (texto, gesto o dibujo).",
     "Leí tres veces. Dije mirando el papel. Tapé el poema y dije un verso a la vez con el gesto del sapo. Dije toda la estrofa de memoria. Recité al adulto con voz clara. Apoyos: texto, gesto y dibujo de la luna.",
     ["sigue los cinco pasos", "retira el apoyo poco a poco", "recita con voz clara"], ["lista de los cinco pasos con apoyos", "recitación al adulto"], ["saltarse pasos", "quitar el texto demasiado pronto"],
     "Si se olvida, vuelve al paso anterior y repite dos veces más."),
    "Aprende una adivinanza de memoria y dila a alguien.",
    "Ensaya un poema distinto con tus propios gestos.",
)

reg(
    OA26, 5,
    "El poema de este cuaderno y la pauta. Un adulto será el público y marcará la pauta.",
    "Aprenderé a presentar un recital cuidado, con mi voz, mi cuerpo y mi respeto por el público. Sirve para compartir un poema con otros.",
    ["Sé comprender, ensayar y recitar un poema con entonación y pausas."],
    [
        "Un recital es una presentación en la que se dicen poemas, rimas, adivinanzas o trabalenguas ante un público. Antes de empezar, me paro derecho, respiro y miro al público. Anuncio el título del poema y mi nombre: «Voy a recitar La lluvia».",
        "Durante el recital, uso una voz clara y un ritmo tranquilo. Hago pausas, cambio la voz según el sentimiento y uso gestos pequeños. Miro al público, no al piso. Si me equivoco, respiro, miro el texto si lo tengo y sigo con calma. Un error no arruina el recital.",
        "Al terminar, digo «gracias» y espero el aplauso. Después recibo los comentarios con una sonrisa. Un recital cuidado es el resultado de comprender, ensayar y respetar a quienes escuchan.",
    ],
    [("recital", "presentación de poemas ante un público"), ("título", "nombre del poema"), ("anunciar", "decir el título antes de empezar"), ("gesto pequeño", "movimiento sencillo que acompaña"), ("aplauso", "palmas del público al final")],
    [
        ("Empezar bien", "Vas a recitar «La lluvia». ¿Cómo empiezas?", ["Me paro derecho.", "Respiro y miro al público.", "Anuncio el título."], "Voy a recitar «La lluvia»."),
        ("Seguir tras un error", "Te olvidaste de un verso. ¿Qué haces?", ["Respiro.", "Miro el texto si lo tengo.", "Sigo con calma."], "Respiro, miro el texto y continúo."),
    ],
    [("Empezar sin anunciar.", "Se tiene nervios.", "Di el título y respira."), ("Parar cuando uno se equivoca.", "Se piensa que ya salió mal.", "Respira y sigue.")],
    [
        E("Antes de recitar, ¿anuncio el título?", "Sí", "El público sabe qué escuchará."),
        E("Mientras recito, ¿miro al público o al piso?", "Al público", "Conecta con quien escucha."),
        E("Al terminar, ¿qué digo?", "Gracias", "Agradezco la atención."),
    ],
    [
        E("¿Qué es un recital?", "Una presentación de poemas ante un público", "Se comparten textos."),
        E("¿Por qué respiro antes de empezar?", "Para estar tranquilo y tener aire", "Ayuda a recitar mejor."),
        E("¿Un error arruina el recital?", "No", "Se puede seguir con calma."),
    ],
    [
        E("Escribe cómo anunciarías el poema «El sapo» con tu nombre (usa Ana).", "Por ejemplo: Hola, soy Ana y voy a recitar «El sapo»", "Incluye nombre y título."),
        E("Escribe dos gestos pequeños para acompañar «La lluvia cantora».", "Por ejemplo: dedos como gotas y mirada a la ventana", "Son gestos sencillos."),
        E("Escribe qué dirías al terminar.", "Por ejemplo: Gracias por escucharme", "Cierra con cortesía."),
    ],
    [
        E("Mía recitó sin anunciar, sin mirar y sin decir gracias. ¿Cuántos puntos del recital cuidado olvidó?", "3", "Anunciar, mirar y agradecer."),
        E("Pedro se rió de un compañero que se equivocó en el recital. ¿Es adecuado?", "No", "Un buen público respeta."),
    ],
    [
        E("Una pauta tiene 5 puntos: anuncia, voz clara, pausas, gestos y gracias. Ana cumplió 4. ¿Cuántos le faltan?", "1", "5 − 4 = 1."),
        E("Poema de cierre: «Se acaba el recital, / ya llega el final». Escribe qué dos palabras riman.", "recital y final", "Ambas terminan en -al."),
    ],
    [E("Vas a hacer un recital para tus abuelos con un poema, una adivinanza y un trabalenguas. Escribe en qué orden los dirías y cómo empiezas.", "Por ejemplo: poema, adivinanza y trabalenguas; empiezo anunciando el título", "Organiza el recital.")],
    [
        E("¿Hablo con voz clara en el recital?", "Sí", "El público debe oír."),
        E("¿Recibo los comentarios con una sonrisa?", "Sí", "Es una actitud respetuosa."),
        E("¿Hago pausas durante el poema?", "Sí", "Ayudan al ritmo."),
    ],
    ("Haz un mini recital de 3 minutos para un adulto con: 1) el poema «La lluvia» o «El sapo», 2) esta adivinanza: «Soy redonda y brillo en la noche, cambio de forma y me ven en el cielo» (respuesta: la luna) y 3) el trabalenguas «Tito toma té tibio tras el trote». Antes anuncia tu nombre y el título; al final di gracias. El adulto marca la pauta: anuncia, voz clara, pausas, gestos y gracias.",
     "Hola, soy Ana. Voy a recitar «La lluvia». (Recito con pausas y gestos.) Ahora una adivinanza. (Digo la adivinanza y espero.) Y un trabalenguas: Tito toma té tibio tras el trote. Gracias por escucharme. El adulto marcó cinco puntos.",
     ["anuncia nombre y título", "voz clara con pausas", "gestos pequeños", "dice gracias"], ["recital escuchado", "pauta de cinco puntos marcada"], ["recitar muy bajo", "no mirar al público"],
     "Marca el punto que faltó y pídele repetir solo esa parte."),
    "Haz un mini recital a un familiar.",
    "Escribe una invitación para un recital y preséntalo a tu curso o familia.",
)
