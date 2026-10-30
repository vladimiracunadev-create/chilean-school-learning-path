"""Student material for 1.º básico Tecnología, OA 03 (elaboración segura de un objeto) y OA 04 (prueba y explicación de resultados)."""
from __future__ import annotations

from student_lessons import ex, register

OA3, OA4 = "TE01 OA 03", "TE01 OA 04"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": [ex(*i) for i in R], "understand": [ex(*i) for i in C], "apply": [ex(*i) for i in A], "reason": [ex(*i) for i in Z], "challenge": [ex(*i) for i in D]},
        context=[ex(*ctx)], selfcheck=[ex(*i) for i in sc], open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )


# ------------------------------------------------------------------ OA 03
reg(
    OA3, 1,
    materials="Una mesa despejada, una hoja de papel, una caja de cartón limpia, regla, lápiz, tijera de punta roma y pegamento escolar. Un adulto está cerca para ayudar. Si no tienes todo, haz el ejercicio solo con los dibujos y la lista de este cuaderno.",
    use="Aprenderé a preparar mi lugar de trabajo y mis materiales antes de empezar. Sirve para trabajar sin accidentes y sin perder cosas.",
    prior=["Sé qué herramienta sirve para cada acción.", "Sé que un plan tiene pasos en orden."],
    explain=[
        "Antes de construir, se prepara el lugar. Primero deja la mesa despejada: solo lo necesario encima. Luego junta todos los materiales y herramientas y ponlos al alcance de la mano. Así no te levantas con la tijera en la mano.",
        "Revisa tu lista. Para un contenedor de tarjetas necesitas: cartón limpio, regla, lápiz, tijera de punta roma y pegamento escolar. Si falta algo, avisa a un adulto antes de empezar. Elige también tus materiales: papel, cartón, lana o hilo (fibras), un trozo de tela, una bolsa o botella de plástico limpia y desechos limpios, como una caja o una tapa. Cada material sirve para algo distinto. El papel se pliega. La lana se une con un nudo. El plástico se pega con cinta. No uses vidrio ni latas, porque cortan.",
        "Recuerda tres reglas de seguridad. Tu cabello recogido y tus mangas arremangadas. La tijera siempre cerrada cuando no la usas. Y un adulto cerca cuando cortes. Al terminar, guardas todo y te lavas las manos. Un buen espacio de trabajo es el primer paso de un buen trabajo.",
    ],
    vocab=[("espacio de trabajo", "lugar donde construyo"), ("despejar", "sacar lo que no necesito"), ("lista de materiales", "papel que dice qué necesito"), ("seguridad", "cuidar que nadie se haga daño"), ("al alcance", "cerca para tomarlo sin pararme")],
    worked=[
        ("Revisar la lista", "Necesitas 5 cosas: cartón, regla, lápiz, tijera y pegamento. Ya tienes cartón, regla y lápiz. ¿Cuántas te faltan?", ["Cuento lo que necesito: 5.", "Cuento lo que tengo: 3.", "5 − 3 = 2."], "Faltan 2: tijera y pegamento"),
        ("Elegir un material seguro", "Tienes una botella de plástico limpia y un frasco de vidrio. Quieres hacer un portalápices. ¿Cuál eliges?", ["El vidrio puede romperse y cortar.", "El plástico limpio no corta si está entero.", "Elijo el plástico limpio y un adulto me ayuda."], "La botella de plástico limpia"),
        ("Despejar la mesa", "En tu mesa hay un vaso, una pelota, tu cuaderno de lectura y tus materiales. ¿Qué dejas sobre la mesa?", ["Pienso en qué necesito para construir.", "El vaso, la pelota y el cuaderno no se usan.", "Dejo solo los materiales."], "Solo los materiales de la construcción"),
    ],
    mistakes=[
        ("Empezar a cortar sin revisar que tengo todo.", "Puedo interrumpir y levantarme con la tijera.", "Revisa la lista antes de empezar."),
        ("Dejar la tijera abierta sobre la mesa.", "Alguien puede hacerse daño.", "Ciérrala y guárdala cuando no la uses."),
    ],
    R=[
        ("Antes de construir, ¿la mesa debe estar despejada o llena de juguetes?", "Despejada", "Así hay espacio y no te distraes."),
        ("Para hacer un portalápices, ¿eliges una lata o una botella de plástico limpia?", "Una botella de plástico limpia", "La lata tiene bordes que cortan."),
        ("¿Quién debe estar cerca cuando cortas?", "Un adulto", "Puede ayudar si hace falta."),
    ],
    C=[
        ("¿Para qué sirve la lista de materiales?", "Para revisar que tengo todo antes de empezar", "Evita interrupciones y olvidos."),
        ("¿Por qué se despeja la mesa antes de construir?", "Para tener espacio y evitar accidentes", "Menos cosas, menos riesgos."),
        ("¿Qué haces con las herramientas al terminar?", "Las guardas en su lugar", "Es parte del orden y la seguridad."),
    ],
    A=[
        ("Necesitas 6 cosas para un contenedor y ya reuniste 4. ¿Cuántas te faltan?", "2", "6 − 4 = 2."),
        ("Tu lista dice: cartón, regla, lápiz, tijera, pegamento. Ya tienes cartón, lápiz, tijera y pegamento, pero no tienes regla. ¿Qué te falta de la lista?", "La regla", "Es lo único que falta."),
        ("Sobre tu mesa hay 8 objetos y solo 5 son de la construcción. ¿Cuántos debes sacar?", "3", "8 − 5 = 3."),
    ],
    Z=[
        ("Tomás empieza a cortar y a mitad del trabajo se levanta a buscar pegamento. ¿Qué paso de preparación se saltó?", "Revisar la lista de materiales", "No juntó todo antes de empezar."),
        ("Nico quiere unir dos trozos de lana y piensa en doblarlos como el papel. ¿Qué técnica sirve mejor para unir lana: nudo o pliegue?", "Nudo", "La lana es una fibra y se une atándola."),
    ],
    D=[
        ("Preparar la mesa lleva estos pasos: despejar, juntar materiales, revisar la lista. Escribe el orden que se explicó en la clase.", "Despejar, juntar materiales, revisar la lista", "Primero hay espacio, luego se junta y se revisa."),
        ("Tienes: papel, lana, un vidrio roto, una tapa limpia y una lata. El vidrio y la lata no se usan. ¿Cuántos materiales sí puedes usar?", "3", "Papel, lana y tapa limpia: 5 − 2 = 3."),
    ],
    ctx=("Lía va a construir un contenedor de tarjetas. Sobre su mesa hay una pelota, su lista, un cuaderno, cartón, regla, lápiz, tijera de punta roma y pegamento escolar. La lista se queda sobre la mesa. ¿Cuántos objetos debe sacar de la mesa?", "2", "La pelota y el cuaderno no se usan."),
    sc=[
        ("¿Qué haces primero: despejar la mesa o empezar a cortar?", "Despejar la mesa", "Primero se prepara."),
        ("¿Se puede empezar sin revisar los materiales? Responde sí o no.", "No", "Podría faltar algo."),
        ("¿Cómo llevas la tijera cuando caminas?", "Cerrada", "Así evita accidentes."),
    ],
    open_task=(
        "Prepara tu lugar de trabajo para el contenedor de tarjetas con esta lista: cartón limpio, regla, lápiz, tijera de punta roma, pegamento escolar. Dibuja tu mesa con los 5 objetos y un papel de diario debajo. Elige un material extra de esta lista: lana, tela, bolsa de plástico limpia o tapa limpia, y escribe para qué sirve. Escribe 3 reglas de seguridad que cumplirás, una de ellas sobre lavarte las manos al terminar.",
        "Dibujé mi mesa con los 5 objetos. Elegí lana: sirve para unir con un nudo. Reglas: la tijera cerrada cuando no la uso, un adulto cerca, y me lavo las manos al terminar.",
        ["junta los 5 materiales", "despeja el espacio", "elige un material y dice para qué sirve", "escribe 3 reglas de seguridad"],
        ["foto o dibujo de la mesa", "lista de reglas"],
        ["empezar sin revisar", "dejar la tijera abierta"],
        "Pide mostrar la lista y marcar cada material con una cruz cuando lo ve. Refuerza la regla de la tijera.",
    ),
    reinforce="Prepara tu mesa para dibujar y revisa que tengas todo.",
    extend="Escribe una lista de materiales para otra construcción de papel.",
)

reg(
    OA3, 2,
    materials="Regla, lápiz, tijera de punta roma, una hoja de papel o cartón limpio y una plantilla descrita en este cuaderno. Un adulto ayuda con el corte.",
    use="Aprenderé a medir, marcar y cortar con cuidado siguiendo una plantilla. Sirve para que las partes de mi objeto salgan del tamaño correcto.",
    prior=["Sé usar una regla desde el cero.", "Sé que la tijera se usa con ayuda de un adulto."],
    explain=[
        "Para medir, pon el cero de la regla en el borde del papel y mira el número donde termina lo que necesitas. Luego haz una marca pequeña con el lápiz en ese punto. Mide de nuevo desde el otro lado, y une las marcas con una línea recta.",
        "Una plantilla es un modelo que guía el tamaño. Si la plantilla dice 10 cm de ancho y 6 cm de alto, marcas esas medidas en el cartón y trazas un rectángulo. Así todas las piezas salen iguales.",
        "Las fibras, como la lana o el hilo, se miden estirándolas junto a la regla, sin arrugas. La tela y la bolsa de plástico limpia también se marcan y se cortan, pero con un adulto cerca y tijera de punta roma. Nunca cortes vidrio ni latas. Para cortar, pide ayuda a un adulto. Corta sobre la línea con calma, con la punta de la tijera lejos de tu cuerpo. Sujeta el papel con la otra mano, lejos del filo. Pon los restos en una caja y lávate las manos al terminar. Si te equivocas por poco, no pasa nada: ajusta después con cuidado.",
    ],
    vocab=[("plantilla", "modelo que muestra el tamaño de una pieza"), ("marca", "punto hecho con lápiz"), ("línea de corte", "línea por donde se corta"), ("recto", "sin curvas"), ("filo", "borde que corta")],
    worked=[
        ("Medir una pieza", "La plantilla pide 10 cm de largo. Pones el cero en el borde. ¿Dónde marcas?", ["El cero está en el borde.", "Busco el número 10 en la regla.", "Hago una marca en el 10."], "En el número 10 de la regla"),
        ("Medir una fibra", "Estiras un hilo de lana junto a la regla desde el cero y termina en el 14. ¿Cuánto mide?", ["Pongo el hilo recto, sin arrugas.", "Pongo el cero en un extremo.", "Leo el número donde termina."], "14 cm"),
        ("Calcular el sobrante", "Tu cartón mide 14 cm de largo y la pieza mide 10 cm. ¿Cuántos cm sobran?", ["Resto 14 − 10.", "Da 4.", "Sobran 4 cm."], "Sobran 4 cm"),
    ],
    mistakes=[
        ("Empezar a medir desde el 1 de la regla.", "La pieza queda 1 cm más corta.", "Pon el cero de la regla en el borde del papel."),
        ("Cortar sin línea marcada.", "El corte sale chueco.", "Marca y une las marcas con lápiz antes de cortar."),
    ],
    R=[
        ("¿Dónde pones el borde del papel al medir: en el cero de la regla o en el 5?", "En el cero", "Desde el cero se mide el largo."),
        ("Al cortar, ¿la punta de la tijera apunta lejos de tu cuerpo o hacia tu cuerpo?", "Lejos de tu cuerpo", "Así no te puedes lastimar."),
        ("¿Qué haces antes de cortar: trazar la línea o cortar al ojo?", "Trazar la línea", "La línea guía el corte."),
    ],
    C=[
        ("¿Qué es una plantilla?", "Un modelo que muestra el tamaño de la pieza", "Sirve para que todas salgan iguales."),
        ("¿Por qué hay que marcar con lápiz antes de cortar?", "Para saber por dónde cortar", "La marca guía la tijera."),
        ("¿Cómo mides un hilo de lana: estirado junto a la regla o hecho un ovillo?", "Estirado junto a la regla", "Si está arrugado, la medida sale equivocada."),
    ],
    A=[
        ("La plantilla pide 12 cm de largo. Tu cartón mide 18 cm. ¿Cuántos cm sobran?", "6", "18 − 12 = 6."),
        ("Marcas una pieza de 10 cm de ancho y otra de 10 cm de ancho, una al lado de la otra. ¿Cuántos cm de cartón ocupan juntas?", "20", "10 + 10 = 20."),
        ("Cortas un trozo de lana de 15 cm y otro de 9 cm. ¿Cuántos cm más largo es el primero?", "6", "15 − 9 = 6."),
    ],
    Z=[
        ("Rita puso el borde del papel en el número 1 de la regla y marcó en el 10. La pieza debía medir 10 cm. ¿Salió bien? Responde sí o no.", "No", "De 1 a 10 hay solo 9 cm; debía empezar en el cero."),
        ("Ema quiere cortar una botella de plástico, pero no hay un adulto cerca. ¿Debe cortarla ahora? Responde sí o no.", "No", "Con objetos cortantes siempre debe haber un adulto."),
    ],
    D=[
        ("Del cartón de 20 cm de largo cortas una pieza de 12 cm. De lo que sobra cortas otra de 5 cm. ¿Cuántos cm sobran al final?", "3", "20 − 12 − 5 = 3."),
        ("Para una caja necesitas 2 piezas de 10 cm y 2 piezas de 6 cm. ¿Cuántos cm de cartón se usan en total?", "32", "10 + 10 + 6 + 6 = 32."),
    ],
    ctx=("Tato fabrica un contenedor de tarjetas. La plantilla del frente pide 10 cm de ancho y 6 cm de alto. Su cartón mide 15 cm de ancho. ¿Cuántos cm le sobran de ancho?", "5", "15 − 10 = 5 cm sobran."),
    sc=[
        ("¿Desde qué número de la regla se empieza a medir normalmente?", "Desde el cero", "Ahí está el inicio de la medida."),
        ("¿Se corta antes o después de marcar?", "Después", "Se corta por la marca."),
        ("¿Para qué sirve una plantilla?", "Para repetir el mismo tamaño", "Todas las piezas salen iguales."),
    ],
    open_task=(
        "Con esta plantilla marca y corta una pieza de papel: 10 cm de ancho y 6 cm de alto. Mide con la regla, marca con lápiz, une las marcas con línea recta y corta con un adulto. Después mide y corta también un trozo de lana de 10 cm. Escribe cuánto mide cada lado, cuánto mide la lana y si las piezas salieron iguales a la plantilla.",
        "Medí 10 cm de ancho y 6 cm de alto, uní las marcas, corté con ayuda y salió igual a la plantilla. Corté un hilo de lana de 10 cm estirado junto a la regla. Anoté las medidas de mis dos lados y de la lana.",
        ["mide desde el cero", "marca y une con línea recta", "corta con ayuda y cuidado", "compara con la plantilla"],
        ["pieza de papel cortada y trozo de lana", "notas de las medidas"],
        ["no empezar en cero", "cortar sin línea"],
        "Pide medir de nuevo la pieza y comparar con la plantilla. Si hay diferencia, que diga cuánto y por qué.",
    ),
    reinforce="Mide el largo de tu cuaderno con una regla y anota.",
    extend="Corta una pieza de 8 cm por 5 cm y compárala con otra.",
)

reg(
    OA3, 3,
    materials="Piezas de papel o cartón ya cortadas, regla, lápiz, pegamento escolar y papel de diario para proteger la mesa. Si no tienes pegamento, usa cinta adhesiva con ayuda de un adulto.",
    use="Aprenderé a plegar, unir y terminar las piezas de mi objeto. Sirve para que las partes queden firmes y bien armadas.",
    prior=["Sé medir y cortar una pieza con ayuda.", "Sé el orden de las tareas de fabricación."],
    explain=[
        "Plegar es doblar el papel o el cartón por una línea marcada. Marca el pliegue con la regla y el lápiz, apoya la regla y dobla por ahí. Presiona con el dedo para que el pliegue quede firme y recto.",
        "Unir es pegar dos partes. Pon poco pegamento, solo en la orilla que se une, y presiona durante un rato. Si pones demasiado, el papel se arruga y tarda en secar. Espera hasta que seque antes de usar el objeto. Cada material se une a su manera: el papel y el cartón, con pegamento; el plástico, con cinta, porque el pegamento escolar no lo agarra bien; la lana, el hilo y la tela, con un nudo.",
        "Terminar es revisar y dejar listo. Mira si hay bordes que sobresalen, restos de pegamento o esquinas que se doblan. Corrige con cuidado. Si quieres pintar, hazlo al final, con pintura escolar sobre papel o cartón y cuando el pegamento ya esté seco. El plástico delgado no guarda un pliegue marcado como el papel. Al final, limpia la mesa y lávate las manos. Un buen terminado hace que el objeto sea más seguro y más lindo.",
    ],
    vocab=[("plegar", "doblar por una línea marcada"), ("pliegue", "la marca que deja el doblez"), ("unir", "pegar dos partes"), ("terminar", "revisar y dejar listo el objeto"), ("secar", "esperar a que el pegamento se endurezca")],
    worked=[
        ("Contar pliegues de una caja", "Una caja de cartón tiene 4 paredes que se doblan hacia arriba. ¿Cuántos pliegues se hacen?", ["Cada pared se dobla una vez.", "Hay 4 paredes.", "Son 4 pliegues."], "4 pliegues"),
        ("Cantidad de pegamento", "Debes unir una orilla de 5 cm. ¿Pones pegamento en toda la mesa, en toda la pieza o solo en la orilla?", ["Se une una orilla.", "Pongo poco pegamento.", "Solo en la orilla."], "Solo en la orilla que se une"),
    ],
    mistakes=[
        ("Poner mucho pegamento.", "El papel se arruga y tarda en secar.", "Usa un hilo delgado de pegamento solo en la orilla."),
        ("Usar el objeto antes de que seque.", "Se despega.", "Espera hasta que el pegamento esté seco."),
    ],
    R=[
        ("¿Plegar es doblar o cortar?", "Doblar", "Se dobla por una línea."),
        ("¿Dónde pones el pegamento: en la orilla que se une o en toda la pieza?", "En la orilla que se une", "Solo ahí se necesita."),
        ("¿Antes de usar el objeto, esperas a que seque o lo usas de inmediato?", "Esperas a que seque", "Si no, se despega."),
    ],
    C=[
        ("¿Por qué se marca el pliegue antes de doblar?", "Para que el doblez salga recto", "Una línea guía el doblez."),
        ("¿Qué pasa si pones demasiado pegamento?", "El papel se arruga y tarda en secar", "Sobra pegamento en el papel."),
        ("Quieres unir dos trozos de lana. ¿Sirve mejor un nudo o un pliegue?", "Un nudo", "Las fibras se atan; no se doblan como el papel."),
    ],
    A=[
        ("Una caja tiene 4 paredes y cada una necesita 2 pliegues (uno a cada lado). ¿Cuántos pliegues hay en total?", "8", "2 + 2 + 2 + 2 = 8."),
        ("Debes pegar 3 orillas de 6 cm cada una. ¿Cuántos cm de orilla debes pegar en total?", "18", "6 + 6 + 6 = 18."),
        ("Un pliegue está a 2 cm del borde de una hoja de 10 cm de ancho. ¿Cuántos cm quedan del otro lado del pliegue?", "8", "10 − 2 = 8."),
    ],
    Z=[
        ("Teo pegó las orillas y de inmediato llenó la caja con 8 tarjetas. Se despegó. ¿Qué paso olvidó?", "Esperar a que seque", "El pegamento necesita tiempo."),
        ("Luis unió dos trozos de bolsa plástica con pegamento escolar y se despegaron. ¿Qué le conviene usar: cinta o más pegamento?", "Cinta", "El pegamento escolar no agarra bien el plástico."),
    ],
    D=[
        ("Una tira de 20 cm se pliega en 4 partes del mismo largo. Pista: busca el número que sumado 4 veces da 20. ¿Cuánto mide cada parte?", "5 cm", "5 + 5 + 5 + 5 = 20."),
        ("Una solapa pegada mide 1 cm. Si la pieza mide 11 cm de largo y la solapa se pega por debajo, ¿cuántos cm de largo se ven por fuera?", "10", "11 − 1 = 10."),
    ],
    ctx=("Pía arma un contenedor de tarjetas. Tiene 4 paredes con 1 pliegue cada una y una solapa en cada esquina. Hay 4 esquinas. ¿Cuántas solapas debe pegar?", "4", "Hay una por cada esquina."),
    sc=[
        ("¿Qué es plegar?", "Doblar por una línea marcada", "Se hace un pliegue."),
        ("¿Poco o mucho pegamento?", "Poco", "Así no se arruga."),
        ("¿Qué material se pliega bien y se pega con pegamento: el papel o la lana?", "El papel", "La lana es una fibra y se une con nudo."),
    ],
    open_task=(
        "Arma una cajita con una pieza de papel cuadrada de 12 cm de lado. Marca un pliegue a 3 cm de cada borde, un adulto corta 3 cm desde cada esquina hacia adentro, por la línea del pliegue. Dobla las 4 orillas hacia arriba y une las esquinas con poco pegamento o cinta. Con un trozo de lana de 20 cm haz un lazo y une sus extremos con un nudo. Anota cuántos pliegues hiciste, qué técnica usaste para cada material y cómo quedó el terminado. Lávate las manos al terminar.",
        "Hice 4 pliegues a 3 cm de cada borde. Pegué las 4 esquinas con poco pegamento. Esperé a que secara y quedó firme. Un borde sobresale y lo recorté con ayuda. La lana la uní con un nudo y me lavé las manos.",
        ["marca los pliegues", "dobla recto", "usa poco pegamento", "une la lana con un nudo", "revisa el terminado"],
        ["caja de papel armada", "nota con pliegues y terminado"],
        ["mucho pegamento", "usar antes de que seque"],
        "Pide mostrar los 4 pliegues y explicar cómo comprobó que están rectos.",
    ),
    reinforce="Dobla una hoja en 4 partes iguales y cuéntalas.",
    extend="Arma una caja con otra medida de papel y compara con la anterior.",
)

reg(
    OA3, 4,
    materials="Una caja de papel de 10 cm por 7 cm descrita en este cuaderno, 10 tarjetas o rectángulos de papel de 9 cm por 6 cm, regla y lápiz. Si no tienes todo, haz las cuentas con los datos del cuaderno.",
    use="Aprenderé a terminar un contenedor de tarjetas y a comprobar si sirve para lo que lo hice. Sirve para saber si mi objeto cumple y qué mejorar.",
    prior=["Sé medir, cortar, plegar y unir con cuidado.", "Sé escribir qué debe cumplir un objeto."],
    explain=[
        "Construir es seguir el plan paso a paso: medir, marcar, cortar, plegar y unir. Al final se comprueba, que es probar si el objeto cumple lo que se pidió. Comprobar no es mirar si es bonito, sino usarlo. También sirve para elegir material: se prueba cuál resiste más. Por ejemplo, se pone el mismo peso sobre un papel doblado y sobre un cartón, y se ve cuál se hunde.",
        "Para un contenedor de tarjetas, el criterio es que quepan 10 tarjetas de 9 cm por 6 cm. Si el contenedor mide 10 cm de largo y 7 cm de ancho por dentro, caben las tarjetas, porque 10 es más que 9 y 7 es más que 6. Se comprueba poniendo las tarjetas adentro.",
        "Después anota el resultado: qué cumplió y qué no. Si no cumple, piensa qué cambiar, por ejemplo hacer la caja un poco más grande o pegar mejor las orillas. Tu objeto no tiene que ser perfecto, pero sí debe servir para su usuario.",
    ],
    vocab=[("comprobar", "usar el objeto para ver si cumple"), ("cabe", "entra en el espacio que hay"), ("interior", "lo de adentro"), ("resultado", "lo que pasó al probar"), ("ajustar", "cambiar un poco para mejorar")],
    worked=[
        ("Comprobar el tamaño", "Una tarjeta mide 9 cm por 6 cm. El interior de la caja mide 10 cm por 7 cm. ¿Cabe?", ["Comparo el largo: 10 es mayor que 9.", "Comparo el ancho: 7 es mayor que 6.", "Cabe en las dos medidas."], "Sí, cabe"),
        ("Probar cuál resiste", "Pones 5 lápices sobre un papel doblado y se hunde. Los pones sobre un cartón del mismo tamaño y no se hunde. ¿Qué material resiste más?", ["Pruebo los dos con el mismo peso.", "El papel se hundió.", "El cartón aguantó."], "El cartón"),
        ("Cuántas caben", "10 tarjetas apiladas ocupan 1 cm de alto. La caja tiene 2 cm de alto adentro. ¿Cuántas tarjetas caben apiladas?", ["10 tarjetas ocupan 1 cm.", "2 cm es dos veces 1 cm.", "10 + 10 = 20."], "20 tarjetas"),
    ],
    mistakes=[
        ("Decir que funciona porque se ve lindo.", "Lo lindo no prueba que cumple.", "Pon las tarjetas y cuenta cuántas caben."),
        ("No anotar el resultado de la prueba.", "Después no se recuerda qué pasó.", "Escribe qué cumplió y qué no."),
    ],
    R=[
        ("Una tarjeta mide 9 cm. La caja mide 10 cm por dentro. ¿Cabe o no cabe?", "Cabe", "10 es mayor que 9."),
        ("Una tarjeta mide 9 cm. La caja mide 8 cm por dentro. ¿Cabe o no cabe?", "No cabe", "8 es menor que 9."),
        ("¿Comprobar es usar el objeto o solo mirarlo?", "Usarlo", "Se prueba lo que hace."),
    ],
    C=[
        ("¿Qué se hace al comprobar un contenedor de tarjetas?", "Se ponen las tarjetas adentro y se cuenta", "Se prueba la capacidad."),
        ("¿Por qué se anota el resultado?", "Para recordar qué cumplió y qué mejorar", "Sirve para decidir cambios."),
        ("¿Cómo sabes si el cartón resiste más que el papel: lo miras o pones el mismo peso en los dos?", "Pones el mismo peso en los dos", "Probar con lo mismo permite comparar."),
    ],
    A=[
        ("El interior de una caja mide 12 cm de largo. Las tarjetas miden 9 cm. ¿Cuántos cm sobran?", "3", "12 − 9 = 3."),
        ("Caben 8 tarjetas por fila y hay 2 filas. ¿Cuántas tarjetas caben en total?", "16", "8 + 8 = 16."),
        ("El cartón sostuvo 6 libros y el papel doblado sostuvo 2. ¿Cuántos libros más sostuvo el cartón?", "4", "6 − 2 = 4."),
    ],
    Z=[
        ("Tato dice que su caja funciona porque la pintó de azul. Pero al poner 10 tarjetas, solo caben 6. ¿Funciona para 10 tarjetas? Responde sí o no.", "No", "Solo caben 6."),
        ("Teo dice que su bolsa plástica sostendrá 10 tarjetas porque se ve fuerte, pero no la probó. ¿Qué debe hacer?", "Probarla con las tarjetas", "Solo usar el objeto muestra si resiste."),
    ],
    D=[
        ("Una caja guarda 15 tarjetas. Ya pusiste 9. ¿Cuántas caben todavía?", "6", "15 − 9 = 6."),
        ("Las tarjetas miden 9 cm por 6 cm. La caja mide por dentro 8 cm por 7 cm. ¿Caben las tarjetas? Responde sí o no.", "No", "El largo de la caja, 8 cm, es menor que 9 cm."),
    ],
    ctx=("Lía fabricó un contenedor con interior de 10 cm por 7 cm para tarjetas de 9 cm por 6 cm. Puso 10 tarjetas y entraron todas. ¿Cumplió su criterio de guardar 10 tarjetas? Responde sí o no.", "Sí", "Las 10 tarjetas entraron."),
    sc=[
        ("¿Qué es comprobar?", "Usar el objeto para ver si cumple", "Se prueba lo que hace."),
        ("¿Se anota el resultado? Responde sí o no.", "Sí", "Sirve para mejorar."),
        ("10 cm contra 9 cm: ¿cabe lo de 9 cm en un espacio de 10 cm?", "Sí", "10 es mayor que 9."),
    ],
    open_task=(
        "Comprueba este contenedor: interior de 10 cm por 7 cm y alto de 3 cm. Las tarjetas miden 9 cm por 6 cm, y 10 tarjetas apiladas ocupan 1 cm de alto. Necesitas guardar 10 tarjetas. Para la tapa, probaste papel y cartón con el mismo peso: el papel se hundió con 2 libros y el cartón aguantó 6. Escribe si caben, cuántas caben apiladas, qué material elegirías para la tapa y un ajuste si algo no cumple.",
        "Las tarjetas caben porque 10 es mayor que 9 y 7 es mayor que 6. En 3 cm de alto caben 30 tarjetas. Cumple. Para la tapa elijo el cartón, porque aguantó 6 libros y el papel solo 2. No necesita ajustes, pero revisaría los pliegues.",
        ["compara largo y ancho", "calcula cuántas caben", "elige el material que resiste más", "anota el resultado", "propone un ajuste si hace falta"],
        ["hoja con comparación y cálculo", "frase de resultado"],
        ["decir que funciona sin probar", "no anotar"],
        "Pide mostrar la comparación de medidas y el cálculo con los datos.",
    ),
    reinforce="Mete tus lápices en un vaso y cuenta cuántos caben.",
    extend="Diseña un contenedor para 20 tarjetas y calcula su alto.",
)

# ------------------------------------------------------------------ OA 04
reg(
    OA4, 1,
    materials="Los criterios y datos escritos en este cuaderno, una hoja y un lápiz. Si quieres, usa un marcador de papel y un libro, pero no es obligatorio.",
    use="Aprenderé a escribir criterios que se pueden observar antes de probar un objeto. Sirve para saber con claridad si mi objeto funciona.",
    prior=["Sé qué es un criterio.", "Sé usar un objeto que hice para probarlo."],
    explain=[
        "Antes de probar, escribe qué esperas que pase. Eso se llama criterio. Un buen criterio se puede observar: se puede ver, contar o medir. «Funciona bien» no sirve, porque cada persona lo entiende distinto.",
        "Por ejemplo, para un marcador de página: «se mantiene en su lugar al dar vuelta el libro», «se retira sin romper la hoja» y «al abrir el libro, se ve dónde quedó la lectura». Cada uno se puede probar y responder con sí o no.",
        "Escribir los criterios antes evita decir después «me parece que sí». Si ya sabes qué miras, la prueba es justa. Pide a otra persona que lea tus criterios: si los entiende igual que tú, están bien escritos.",
    ],
    vocab=[("criterio observable", "algo que se puede ver, contar o medir"), ("prueba", "intento para ver si algo funciona"), ("sí o no", "respuesta clara a un criterio"), ("antes de probar", "cuando aún no usé el objeto"), ("justo", "que se mide igual para todos")],
    worked=[
        ("Elegir criterio observable", "¿Cuál es un criterio observable: «es hermoso» o «se mantiene al dar vuelta el libro»?", ["«Es hermoso» es una opinión.", "«Se mantiene al dar vuelta el libro» se puede mirar.", "Se responde con sí o no."], "Se mantiene al dar vuelta el libro"),
        ("Convertir un criterio vago", "El criterio «sirve bien» es vago. Escríbelo mejor para un marcador.", ["Pienso qué debe hacer un marcador.", "Debe mostrar dónde quedó la lectura.", "Lo escribo como algo que se puede ver."], "Al abrir el libro, se ve dónde quedó la lectura"),
    ],
    mistakes=[
        ("Escribir «funciona bien» como criterio.", "No se puede comprobar con claridad.", "Escribe qué se ve o se mide: «se mantiene 3 veces»."),
        ("Cambiar el criterio después de la prueba.", "Hace que el resultado parezca mejor.", "Escribe los criterios antes y no los cambies."),
    ],
    R=[
        ("«Caben 5 lápices» ¿es un criterio observable? Responde sí o no.", "Sí", "Se pueden contar los lápices."),
        ("«Me gusta» ¿es un criterio observable? Responde sí o no.", "No", "Es una opinión."),
        ("¿Cuándo se escriben los criterios: antes o después de probar?", "Antes", "Orientan la prueba."),
    ],
    C=[
        ("¿Qué quiere decir que un criterio sea observable?", "Que se puede ver, contar o medir", "Todos podrían comprobarlo."),
        ("¿Por qué «funciona bien» no es un buen criterio?", "Porque no se sabe qué mirar", "Es demasiado general."),
        ("¿Con qué se responde un buen criterio?", "Con sí o no", "Se cumple o no se cumple."),
    ],
    A=[
        ("Un marcador debe mantenerse en su lugar. Escribe un criterio observable que lo diga.", "Se mantiene en su lugar al dar vuelta el libro", "Se puede ver si se cae."),
        ("¿Cuál es observable: «el vaso aguanta 3 lápices de pie» o «el vaso es especial»?", "El vaso aguanta 3 lápices de pie", "Se puede contar."),
        ("Un portalápices debe quedar derecho. Escribe un criterio observable.", "Queda derecho al poner 5 lápices", "Se puede mirar."),
    ],
    Z=[
        ("Ema escribe: «el marcador es lindo». Tomás dice que ese criterio no sirve para probar. ¿Tiene razón? Responde sí o no.", "Sí", "No se puede comprobar con claridad."),
        ("Luis ve que su objeto no pasó el criterio y lo borra del papel. ¿Hace bien? Responde sí o no.", "No", "Cambiar el criterio no mejora el objeto."),
    ],
    D=[
        ("Escribe un criterio observable para un cartel que se lea desde lejos. Usa una medida o un número de pasos.", "Se lee desde 3 pasos de distancia", "Se puede comprobar contando los pasos."),
        ("Un criterio dice «la tapa cierra sin dejar espacios». ¿Cómo se responde: sí o no, o con una opinión?", "Sí o no", "Es un criterio observable."),
    ],
    ctx=("Pía prueba un marcador. Escribe tres criterios: 1) se mantiene al dar vuelta el libro, 2) se retira sin romper la hoja, 3) al abrir el libro se ve dónde quedó la lectura. Cuando prueba, el marcador se mantiene y se retira bien, pero no se ve dónde quedó la lectura. ¿Cuántos criterios cumplió?", "2", "Cumple el 1 y el 2."),
    sc=[
        ("¿Se escriben criterios antes o después de probar?", "Antes", "Para saber qué mirar."),
        ("¿Un criterio observable se puede ver o medir? Responde sí o no.", "Sí", "Esa es su característica."),
        ("¿Una opinión sirve como criterio? Responde sí o no.", "No", "No se puede comprobar."),
    ],
    open_task=(
        "Piensa en un portalápices para 5 lápices. Escribe tres criterios observables. Por ejemplo: queda derecho al poner 5 lápices, no se mueve al empujarlo suave, y los lápices se sacan con una mano. Elige uno de estos o escribe uno tuyo, y di cómo lo vas a mirar.",
        "Criterios: queda derecho con 5 lápices; no se mueve al empujarlo suave; los lápices se sacan con una mano. Lo miraré poniendo los lápices y empujando con un dedo.",
        ["escribe criterios observables", "dice cómo los comprobará", "no usa opiniones"],
        ["tres criterios escritos", "frase de cómo comprobar"],
        ["criterios vagos", "cambiar criterios después"],
        "Pide que otra persona lea los criterios y diga qué entiende. Si no coincide, hay que precisar.",
    ),
    reinforce="Escribe un criterio observable para una mochila.",
    extend="Escribe tres criterios para un cartel que se pegue en la puerta.",
)

reg(
    OA4, 2,
    materials="La tabla de pruebas escrita en este cuaderno, lápiz y hoja. Para repetir la prueba en casa usa un marcador de papel y un libro.",
    use="Aprenderé a hacer una prueba que otras personas puedan repetir y a registrarla. Sirve para saber con datos si un objeto funciona.",
    prior=["Sé escribir criterios observables.", "Sé contar hasta 10."],
    explain=[
        "Una prueba observable se puede repetir y se registra con datos. Si pruebas una vez y funciona, quizás fue suerte. Por eso se repite varias veces, por ejemplo tres. Si funciona las tres veces, es más seguro que funciona.",
        "Para registrar, haz una tabla con una fila por cada intento y marca con un ✔ si cumple el criterio o con una ✘ si no cumple. Después cuenta cuántos ✔ hay. Si hay 3 de 3, cumple. Si hay 1 de 3, falla muchas veces.",
        "Una prueba justa cambia una sola cosa a la vez. Si cambias el material y el tamaño al mismo tiempo, no sabrás cuál produjo el resultado. Usa siempre el mismo libro y la misma forma de dar vuelta las hojas.",
    ],
    vocab=[("registrar", "anotar lo que pasó"), ("intento", "cada vez que pruebo"), ("✔", "marca que dice que cumple"), ("✘", "marca que dice que no cumple"), ("prueba justa", "prueba en la que cambio una sola cosa")],
    worked=[
        ("Leer un registro", "Intentos del marcador: 1 ✔, 2 ✔, 3 ✘. ¿Cuántas veces se mantuvo?", ["Cuento los ✔.", "Hay dos.", "Fueron 3 intentos."], "2 de 3 veces"),
        ("Prueba justa", "Quieres saber si un marcador de cartón se mantiene mejor que uno de papel. ¿Cambias solo el material o el material y el libro?", ["Para comparar cambio solo una cosa.", "Cambio el material.", "Uso el mismo libro."], "Solo el material"),
    ],
    mistakes=[
        ("Probar una sola vez y decidir.", "Puede haber sido suerte.", "Repite la prueba al menos tres veces."),
        ("Cambiar dos cosas a la vez.", "No se sabe cuál causó el resultado.", "Cambia una sola cosa y mantén lo demás igual."),
    ],
    R=[
        ("Intentos: ✔ ✔ ✔. ¿Cuántos ✔ hay?", "3", "Se cuentan las marcas."),
        ("Intentos: ✔ ✘ ✘. ¿Cuántas veces no cumplió?", "2", "Hay dos ✘."),
        ("¿Una prueba se repite o se hace una sola vez?", "Se repite", "Más intentos dan más seguridad."),
    ],
    C=[
        ("¿Para qué se repite una prueba?", "Para saber si funciona siempre o fue suerte", "Los intentos dan seguridad."),
        ("¿Qué significa la marca ✘?", "No cumple el criterio", "La cruz indica fallo."),
        ("¿Por qué se cambia solo una cosa a la vez?", "Para saber qué produjo el resultado", "Así la prueba es justa."),
    ],
    A=[
        ("Intentos de un marcador: ✔ ✔ ✘ ✔ ✔. ¿Cuántos cumplió?", "4", "Hay cuatro ✔."),
        ("Se hicieron 5 intentos y 3 fallaron. ¿Cuántos cumplieron?", "2", "5 − 3 = 2."),
        ("Pía hizo 3 pruebas del vaso con 3 lápices, 4 lápices y 5 lápices. ¿Cuántas pruebas hizo en total?", "3", "Hizo una prueba por cada cantidad."),
    ],
    Z=[
        ("Rita probó una vez y cumplió. Dice: «siempre funciona». ¿Tiene datos suficientes? Responde sí o no.", "No", "Solo hay un intento."),
        ("Tato probó un marcador de cartón con el libro A y uno de papel con el libro B. Dice que el cartón es mejor. ¿Fue una prueba justa? Responde sí o no.", "No", "Cambió el material y el libro."),
    ],
    D=[
        ("Haces el mismo número de intentos con 3 materiales distintos, y son 9 intentos en total. Pista: busca el número que sumado 3 veces da 9. ¿Cuántos intentos haces por material?", "3", "3 + 3 + 3 = 9."),
        ("Un objeto cumple 8 intentos de 10. ¿Cuántos no cumple?", "2", "10 − 8 = 2."),
    ],
    ctx=("Ana probó su portalápices 3 veces con 5 lápices. Resultado: intento 1 ✔, intento 2 ✔, intento 3 ✘. ¿Cuántas veces quedó derecho?", "2", "Hay dos ✔."),
    sc=[
        ("¿Cuántas veces conviene probar al menos?", "Tres", "Con tres ya se ve un patrón."),
        ("¿Un ✔ quiere decir cumple? Responde sí o no.", "Sí", "Es la marca de cumplir."),
        ("¿Se cambian varias cosas a la vez en una prueba justa? Responde sí o no.", "No", "Solo se cambia una."),
    ],
    open_task=(
        "Haz una tabla con tres intentos para este criterio de un marcador: «se mantiene al dar vuelta el libro». Usa los resultados que te damos: intento 1 se mantuvo, intento 2 se cayó, intento 3 se mantuvo. Marca ✔ o ✘, cuenta cuántos cumplió y escribe una frase de resultado con un número.",
        "Intento 1 ✔, intento 2 ✘, intento 3 ✔. Cumplió 2 de 3 intentos. El marcador se mantuvo 2 veces de 3.",
        ["registra cada intento", "cuenta los ✔", "escribe resultado con número"],
        ["tabla de tres intentos", "frase con número"],
        ["probar una sola vez", "cambiar varias cosas"],
        "Pide explicar qué cuenta como ✔. Si dice «funcionó» sin número, pide el conteo.",
    ),
    reinforce="Lanza una pelota de papel a un vaso 5 veces y anota ✔ o ✘.",
    extend="Repite la prueba con un cambio y compara los resultados.",
)

reg(
    OA4, 3,
    materials="Las tablas de resultados escritas en este cuaderno, lápiz y hoja. No necesitas ningún objeto para resolver los ejercicios.",
    use="Aprenderé a leer el resultado de una prueba y a pensar una causa posible. Sirve para saber por qué algo no funcionó y qué cambiar.",
    prior=["Sé registrar una prueba con ✔ y ✘.", "Sé que una prueba justa cambia una sola cosa."],
    explain=[
        "El resultado de una prueba dice qué pasó. Por ejemplo: «el marcador se mantuvo 1 vez de 3». Una causa posible es una explicación de por qué pasó, como «el pegamento era poco». Una causa posible no es una verdad segura: hay que comprobarla.",
        "Para encontrar una causa, mira qué pasó cuando falló. Si el marcador se cayó siempre que el libro se dio vuelta rápido, la causa posible es la velocidad. Si se cayó siempre que era de papel delgado, la causa posible es el material.",
        "Para comprobar una causa, cambia solo esa cosa y prueba otra vez. Si el marcador de papel grueso se mantiene 3 de 3, la causa era el material delgado. Di siempre «puede ser» o «quizás», porque aún estás aprendiendo.",
    ],
    vocab=[("resultado", "lo que pasó en la prueba"), ("causa posible", "explicación que puede ser verdad y hay que comprobar"), ("patrón", "algo que se repite"), ("comprobar una causa", "cambiar solo esa cosa y probar otra vez"), ("quizás", "palabra que dice que no estoy seguro")],
    worked=[
        ("Buscar un patrón", "El marcador A (papel delgado) falló 3 de 3. El marcador B (papel grueso) funcionó 3 de 3. ¿Cuál es una causa posible?", ["Comparo los dos marcadores.", "Lo que cambia es el grosor del papel.", "Quizás el papel delgado falla."], "El grosor del papel"),
        ("Comprobar la causa", "Tu causa posible es «poco pegamento». ¿Qué pruebas para comprobarla?", ["Cambio solo el pegamento.", "Pongo más pegamento.", "Pruebo otra vez 3 veces."], "Aumentar solo el pegamento y probar otra vez 3 veces"),
    ],
    mistakes=[
        ("Decir una causa como si fuera segura sin comprobarla.", "Puede haber otra explicación.", "Usa «quizás» y comprueba cambiando una sola cosa."),
        ("Culpar a una persona del resultado.", "El resultado habla del objeto, no de la persona.", "Habla del material, la forma o el tamaño."),
    ],
    R=[
        ("El marcador cumplió 2 de 3 intentos. ¿Cuál es el resultado: «cumplió 2 de 3» o «es mi culpa»?", "Cumplió 2 de 3", "Es el dato de la prueba."),
        ("«El pegamento era poco» ¿es una causa posible o un resultado?", "Una causa posible", "Explica por qué pasó."),
        ("¿Una causa posible hay que comprobarla o ya es segura?", "Hay que comprobarla", "Puede no ser la causa real."),
    ],
    C=[
        ("¿Qué es una causa posible?", "Una explicación de por qué pasó algo", "Se debe comprobar después."),
        ("¿Cómo se comprueba una causa posible?", "Cambiando solo esa cosa y probando otra vez", "Así se ve si cambia el resultado."),
        ("¿Qué palabra ayuda a decir que no estás seguro?", "Quizás", "Indica una posibilidad."),
    ],
    A=[
        ("El vaso de cartón delgado se volcó 3 veces de 3. El vaso de cartón grueso no se volcó. ¿Cuál es una causa posible?", "El grosor del cartón", "Es lo que cambia entre ambos."),
        ("La base de un portalápices mide 5 cm y se vuelca. Con base de 10 cm no se vuelca. ¿Qué cambió?", "El ancho de la base", "Pasó de 5 a 10 cm."),
        ("Un marcador sobresale 1 cm y se pierde. Con 4 cm se ve. ¿Cuántos cm más sobresale el segundo?", "3", "4 − 1 = 3."),
    ],
    Z=[
        ("Ema dice: «se rompió porque soy mala para construir». ¿Es una buena explicación del resultado? Responde sí o no.", "No", "Culpa a la persona y no habla del objeto."),
        ("Luis dice: «la tapa se cayó porque se pegó con poco pegamento, seguro». ¿Qué palabra debería cambiar para no sonar tan seguro?", "Seguro por quizás", "Aún no lo comprobó."),
    ],
    D=[
        ("Prueba de una caja: con pared de 1 capa de cartón falla 3 de 3; con 2 capas falla 0 de 3. ¿Cuántas capas hacen que funcione?", "2", "Con 2 capas no falla."),
        ("Una caja falla 4 veces de 5 intentos. ¿Cuántas veces cumple?", "1", "5 − 4 = 1."),
    ],
    ctx=("Pía probó su contenedor 3 veces: las tarjetas se cayeron 3 de 3 cuando lo inclinó. Notó que la tapa no cierra del todo. ¿Cuál es una causa posible?", "La tapa no cierra del todo", "Deja un espacio por donde salen."),
    sc=[
        ("¿Qué es el resultado de una prueba?", "Lo que pasó", "Es el dato de la prueba."),
        ("¿La causa posible es segura? Responde sí o no.", "No", "Hay que comprobarla."),
        ("¿Cómo comprobar una causa posible?", "Cambiando una sola cosa y probando", "Así la prueba es justa."),
    ],
    open_task=(
        "Lee este resultado: el marcador A, de papel delgado, se cayó 3 de 3 veces; el marcador B, de cartón de caja, se mantuvo 3 de 3. Escribe el resultado con números, una causa posible con la palabra quizás y qué cambiarías en A para comprobarla.",
        "Resultado: A se cayó 3 de 3 y B se mantuvo 3 de 3. Quizás el papel delgado pesa poco. Cambiaría A por un papel más grueso y probaría otra vez 3 veces.",
        ["escribe el resultado con números", "da una causa posible", "propone cómo comprobarla"],
        ["frase de resultado", "frase de causa con quizás", "cambio propuesto"],
        ["decir la causa como segura", "culpar a una persona"],
        "Pide cambiar «es porque sí» por una causa posible y preguntar cómo la comprobaría.",
    ),
    reinforce="Mira un juguete que no funciona y di una causa posible.",
    extend="Comprueba una causa posible cambiando una sola cosa.",
)

reg(
    OA4, 4,
    materials="Los resultados de prueba escritos en este cuaderno, hoja y lápiz. No hace falta nada más.",
    use="Aprenderé a proponer una mejora concreta y a decirla con respeto. Sirve para hacer mejores objetos sin ofender a nadie.",
    prior=["Sé leer un resultado de prueba.", "Sé pensar una causa posible."],
    explain=[
        "Una mejora es un cambio que ayuda a que el objeto cumpla mejor. Una buena mejora es concreta: dice qué cambiar y cuánto. «Que sea mejor» no es concreta, pero «hacer la base de 10 cm en vez de 5 cm» sí lo es.",
        "Cuando hablas del trabajo de otra persona, primero di algo que sí funciona. Después propón la mejora usando una frase amable, como «podría mejorar si cambias la base». Habla del objeto, no de la persona. Así todos aprenden y nadie se siente mal.",
        "Cambia solo una cosa a la vez y prueba otra vez. Si cambias una cosa y mejora, ya sabes que ese cambio sirvió. Anota el antes y el después con números. Mejorar no es empezar de cero: es hacer que lo que existe funcione mejor.",
    ],
    vocab=[("mejora", "cambio que ayuda a cumplir mejor"), ("concreto", "que dice exactamente qué hacer"), ("respetuoso", "que no ofende a nadie"), ("antes y después", "cómo era y cómo quedó"), ("autoría", "quién hizo la idea")],
    worked=[
        ("Mejora concreta", "El portalápices se vuelca porque su base mide 5 cm. ¿Qué mejora concreta propones?", ["Pienso qué cambiar.", "La base es muy angosta.", "Propongo una base de 10 cm."], "Hacer la base de 10 cm"),
        ("Comentario respetuoso", "El vaso de Teo no se cae pero la tapa no cierra. ¿Qué dices primero?", ["Primero digo algo que funciona.", "El vaso no se cae.", "Luego propongo mejorar la tapa."], "Tu vaso no se cae; podría mejorar si la tapa cerrara"),
    ],
    mistakes=[
        ("Decir «está feo, hazlo de nuevo».", "Ofende y no dice cómo mejorar.", "Di qué funciona y propone un cambio concreto."),
        ("Cambiar tres cosas a la vez.", "No se sabe cuál ayudó.", "Cambia una cosa y vuelve a probar."),
    ],
    R=[
        ("«Hacer la base más ancha» ¿es una mejora concreta o vaga?", "Concreta", "Dice qué cambiar."),
        ("«Que sea mejor» ¿es una mejora concreta o vaga?", "Vaga", "No dice qué cambiar."),
        ("Al hablar del trabajo de otro, ¿primero dices algo que funciona o algo que falla?", "Algo que funciona", "Es más respetuoso."),
    ],
    C=[
        ("¿Qué hace que una mejora sea concreta?", "Dice qué cambiar y cuánto", "Se puede hacer."),
        ("¿De qué hablas al dar una opinión: del objeto o de la persona?", "Del objeto", "Así se respeta a la persona."),
        ("Si pruebas una mejora, ¿cuántas cosas cambias a la vez?", "Una sola", "Así se sabe cuál cambio ayudó."),
    ],
    A=[
        ("El marcador mide 10 cm y se ve poco. Quieres que sobresalga 3 cm más. ¿Cuántos cm medirá?", "13", "10 + 3 = 13."),
        ("Antes la caja guardaba 4 tarjetas y después de la mejora guarda 9. ¿Cuántas tarjetas más guarda?", "5", "9 − 4 = 5."),
        ("Antes fallaba 3 de 3 y después falla 1 de 3. ¿Cuántas fallas menos hay?", "2", "3 − 1 = 2."),
    ],
    Z=[
        ("Ana dice a Tomás: «tu torre es horrible». ¿Es una forma respetuosa de comentar? Responde sí o no.", "No", "Ofende a la persona."),
        ("Luis cambió el material y el tamaño del vaso a la vez y mejoró. ¿Sabe cuál cambio ayudó? Responde sí o no.", "No", "Cambió dos cosas juntas."),
    ],
    D=[
        ("Reescribe con respeto la frase «tu cofre se rompe todo». Empieza con algo que funciona (el cofre se ve firme) y propón una mejora (pegar mejor las esquinas).", "Tu cofre se ve firme; podría mejorar si pegaras mejor las esquinas", "Dice algo positivo y una mejora concreta."),
        ("Un objeto con base de 5 cm cae 3 de 3. Con 8 cm cae 1 de 3. Con 10 cm cae 0 de 3. ¿Qué medida de base propones?", "10 cm", "Con esa medida no cae."),
    ],
    ctx=("Rita probó su cartel: se lee desde 2 pasos pero no desde 4. Las letras miden 2 cm. Escribe una mejora concreta que cambie solo el tamaño de las letras, con una medida.", "Hacer las letras más grandes, por ejemplo de 4 cm", "Letras más grandes se leen desde más lejos."),
    sc=[
        ("¿Una mejora debe ser concreta? Responde sí o no.", "Sí", "Debe poder hacerse."),
        ("¿Se habla del objeto o de la persona?", "Del objeto", "Así se respeta."),
        ("¿Qué dices primero al comentar: lo que funciona o lo que falla?", "Lo que funciona", "Así se empieza bien."),
    ],
    open_task=(
        "Mira este resultado de un contenedor hecho por un compañero: las tarjetas caben, la tapa cierra, pero las esquinas se despegan 2 veces de 3. Escribe una frase respetuosa que diga algo que funciona, una mejora concreta (por ejemplo usar más pegamento en las esquinas o poner cinta) y cómo vas a probarla.",
        "Tu contenedor guarda bien las tarjetas y la tapa cierra. Podría mejorar si pones cinta en las esquinas. Después prueba otra vez 3 veces para ver si se despegan.",
        ["dice primero algo que funciona", "propone mejora concreta", "habla del objeto", "dice cómo probar la mejora"],
        ["frase escrita", "mejora y forma de probar"],
        ["comentarios ofensivos", "mejoras vagas"],
        "Pide leer el comentario como si lo recibiera él. Si suena duro, pide reformularlo.",
    ),
    reinforce="Di algo que funciona y una mejora para un dibujo de tu casa.",
    extend="Comprueba una mejora y anota el antes y el después con números.",
)
