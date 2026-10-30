"""Cuaderno del estudiante, 4.º básico Tecnología: OA 01 (diseño de objetos y sistemas tecnológicos simples), clases 1 a 6.

Seguridad: solo papel, cartón, cinta, cordel y tijeras de punta roma; nada de cortadores, fuego, vidrio ni herramientas con filo.
Las medidas se dan en centímetros y no se usan decimales. Los productos y las pantallas son ejemplos sin marcas.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "TE04 OA 01"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    def conv(i):
        return i if isinstance(i, dict) else ex(*i)
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": [conv(i) for i in R], "understand": [conv(i) for i in C], "apply": [conv(i) for i in A], "reason": [conv(i) for i in Z], "challenge": [conv(i) for i in D]},
        context=[conv(ctx)], selfcheck=[conv(i) for i in sc], open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )


# ------------------------------------------------------------------ OA 01, clase 1
reg(
    OA1, 1,
    materials="Hoja, lápiz y los casos escritos en este cuaderno. Si quieres, una persona de tu casa para hacerle preguntas.",
    use="Aprenderé a investigar un problema antes de diseñar: reunir datos de los usuarios y del contexto. Sirve para no elegir un objeto antes de entender qué hace falta.",
    prior=["Sé que un usuario es la persona que usa un objeto.", "Sé que un boceto es un dibujo rápido a mano alzada."],
    explain=[
        "Un problema tecnológico es algo que cuesta lograr y que un objeto o sistema podría resolver. Antes de diseñar hay que investigar. Investigar es reunir datos de tres cosas: el usuario, que es quien usará el objeto; el contexto, que es dónde, cuándo y en qué condiciones se usa; y lo que ya existe.",
        "Para reunir datos hay dos acciones. Observar es mirar con atención y anotar lo que pasa, mejor con números: cuántas veces, cuántas personas, cuántos minutos. Preguntar es pedir información con preguntas abiertas, como «¿qué parte te cuesta más?». Una pregunta cerrada se responde solo con sí o no.",
        "Observa a varios usuarios y no solo a uno, porque un solo caso puede engañar. Cierra tu investigación con una frase: «(Usuario) necesita (lograr algo) en (contexto)». Esa frase no nombra ningún objeto. Si ya escribes «una caja» o «un soporte», todavía estás eligiendo una solución y no describiendo el problema.",
    ],
    vocab=[("usuario", "persona que usará el objeto"), ("contexto", "dónde, cuándo y en qué condiciones se usa"), ("observar", "mirar con atención y anotar lo que ocurre"), ("pregunta abierta", "pregunta que no se responde solo con sí o no"), ("dato", "información anotada, a veces con número")],
    worked=[
        ("Convertir observaciones en la frase del problema", "Observaste a Nina en el patio: lleva 6 lápices en el bolsillo y 2 se le caen cada recreo. Ella dice: «Me cuesta que no se pierdan». Escribe la frase del problema.", ["Usuaria: Nina. Contexto: el patio, en el recreo.", "Lo que necesita lograr: que los lápices no se pierdan.", "Armo la frase sin nombrar ningún objeto."], "Nina necesita que sus lápices no se pierdan en el patio"),
        ("Elegir la mejor pregunta", "Quieres saber cómo riega su huerto Don Hugo. ¿Sirve más A «¿Riegas todos los días?» o B «¿Qué te cuesta más al regar?»", ["A se responde con sí o no.", "B pide contar lo que le pasa.", "B entrega más datos."], "B, porque es una pregunta abierta"),
    ],
    mistakes=[
        ("Escribir «el problema es que falta una caja».", "Nombra el objeto antes de entender el problema.", "Di qué no se logra: «los lápices se pierden»."),
        ("Observar solo a un usuario y decir que todos tienen su problema.", "Un solo caso puede ser distinto del resto.", "Observa a varios usuarios y anota cuántos tienen el problema."),
    ],
    R=[
        ("Si diseñas un portalápices para tu hermana, ¿quién es el usuario?", "Tu hermana", "El usuario es quien usará el objeto."),
        ("«En el patio, bajo la lluvia» ¿describe al usuario o al contexto?", "Al contexto", "Dice dónde y en qué condiciones se usa."),
        ("«¿Qué te cuesta al guardar tus útiles?» ¿es una pregunta abierta o cerrada?", "Abierta", "No se responde solo con sí o no."),
    ],
    C=[
        arith("En 10 días de observación, llovió 4 días. En 3 de esos días de lluvia se mojaron los cuadernos. ¿En cuántos días de lluvia NO se mojaron?", "4-3", "Se restan los días con cuadernos mojados de los días de lluvia."),
        ("¿Por qué conviene observar también el contexto y no solo preguntar al usuario?", "Porque el lugar y las condiciones cambian el problema", "El mismo objeto sirve distinto en lugares distintos."),
        ("En «Ana necesita cruzar el patio con su colación sin que se caiga», ¿cuál es el contexto?", "El patio", "Es el lugar donde ocurre el problema."),
    ],
    A=[
        arith("En un curso de 24 estudiantes, 9 guardan los lápices en un estuche y el resto los lleva sueltos. ¿Cuántos los llevan sueltos?", "24-9", "Se resta quienes usan estuche del total del curso."),
        ("Don Mario cuida un huerto pequeño en el patio y no sabe cuándo regar porque no ve si la tierra está seca. Escribe la frase del problema sin nombrar un objeto.", "Don Mario necesita saber cuándo regar su huerto del patio", "Lleva usuario, qué lograr y contexto, sin objeto."),
        ("¿Cuál es una pregunta abierta? A «¿Usas el pasillo?», B «¿Cómo bajas la escalera con tus cosas?», C «¿Es difícil?»", "B", "A y C se responden con sí o no; B pide explicar."),
    ],
    Z=[
        ("Lola observó a 5 compañeros y a 4 se les cae el estuche en el bus. Dice: «Le pasa a todo el colegio». ¿Qué falla en su conclusión?", "Observó pocos casos para hablar de todo el colegio", "Con 5 casos no se puede asegurar lo de todos."),
        ("¿Cuál frase de problema está mejor? A «Camila necesita llevar 3 libros en el bus sin que se doblen», B «Camila necesita una mochila nueva».", "A", "B ya nombra una solución; A dice qué se debe lograr."),
    ],
    D=[
        arith("Registro de cuatro días de estudiantes que llegan con zapatos mojados: lunes 3, martes 0, miércoles 5, jueves 2. ¿Cuántos fueron en total?", "3+0+5+2", "Se suman los cuatro registros."),
        ("Con el mismo registro (lunes 3, martes 0, miércoles 5, jueves 2), ¿qué día hubo más estudiantes con zapatos mojados?", "Miércoles", "El 5 es el valor mayor del registro."),
    ],
    ctx=("En el recreo observas la banca del patio: en 15 minutos, 6 niños intentan sentarse y 2 no caben. Una niña dice: «Me cuesta encontrar dónde sentarme». Escribe usuario, contexto, un dato con número y la frase del problema.", "Usuarios: niños del recreo. Contexto: la banca del patio. Dato: 2 de 6 no caben. Problema: los niños necesitan un lugar donde sentarse en el recreo", "Cubre los cuatro elementos pedidos."),
    sc=[
        ("¿Qué tres cosas se investigan antes de diseñar?", "Usuario, contexto y lo que ya existe", "Son las tres fuentes de datos de la clase."),
        ("¿La frase del problema nombra un objeto?", "No", "Dice qué cuesta lograr y no la solución."),
        ("¿Se observa a un usuario o a varios?", "A varios", "Un solo caso puede engañar."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: en una casa, a Juan se le caen 3 de 7 prendas al subir al segundo piso. Caso 2: en la sala, 3 de 8 niños no alcanzan el interruptor de la luz. Escribe un dato con número, una pregunta abierta para el usuario, el contexto y la frase del problema sin nombrar un objeto.",
        "Caso 1: dato: caen 3 de 7 prendas. Pregunta: ¿en qué momento se te caen más? Contexto: la escalera de la casa. Problema: Juan necesita subir su ropa sin que se caiga.",
        ["escribe un dato con número", "hace una pregunta abierta", "nombra el contexto", "la frase del problema dice usuario, qué lograr y contexto sin nombrar un objeto"],
        ["ficha con dato, pregunta, contexto y frase del problema"],
        ["nombrar el objeto en el problema", "pregunta que se responde con sí o no"],
        "Pregunta: «¿esto dice lo que no se logra o ya dice un objeto?». Si dice un objeto, pídele reescribir con la necesidad.",
    ),
    reinforce="Observa a alguien de tu casa durante 5 minutos al hacer una tarea y anota 2 cosas que le cuesten.",
    extend="Escribe dos preguntas abiertas para saber qué problema tienen en tu curso con el orden de las mochilas.",
)

# ------------------------------------------------------------------ OA 01, clase 2
reg(
    OA1, 2,
    materials="Hoja, lápiz y regla. Los casos y las medidas están escritos en este cuaderno.",
    use="Aprenderé a escribir criterios y restricciones antes de diseñar. Sirve para saber si una idea es buena antes de construirla.",
    prior=["Sé escribir la frase del problema con usuario, necesidad y contexto.", "Sé medir en centímetros con una regla."],
    explain=[
        "Un criterio es una condición que el diseño debe cumplir para resolver el problema. Un buen criterio se puede comprobar. «Debe ser bonito» es difícil de comprobar. «Debe sostener 10 fichas sin caerse» sí se puede comprobar, porque se cuenta. Los criterios pueden ser de funcionamiento, de seguridad o de cuidado del ambiente.",
        "Una restricción es un límite que no se puede pasar. Puede ser de medida («la base mide como máximo 20 cm»), de materiales («solo cartón reutilizado y cinta»), de tiempo («se termina en 40 minutos») o de seguridad («sin bordes que corten»). Las restricciones vienen del contexto y de lo que tienes disponible.",
        "Escribe los criterios con un número o un verbo observable: «sostiene», «mide menos de», «se abre con una mano». Así dos personas distintas llegan a la misma conclusión al revisar el diseño. Criterios y restricciones se escriben antes de dibujar, y son los que se usan después para elegir entre ideas.",
    ],
    vocab=[("criterio", "condición comprobable que el diseño debe cumplir"), ("restricción", "límite que no se puede pasar"), ("comprobable", "que se puede revisar con una medida, un conteo o una prueba"), ("medida máxima", "tamaño más grande permitido"), ("funcionamiento", "lo que el objeto logra hacer")],
    worked=[
        ("Separar criterio de restricción", "Diseñas un soporte para 10 fichas. Datos: «sostiene las 10 fichas» y «la base mide como máximo 20 cm». ¿Cuál es criterio y cuál restricción?", ["Sostener las 10 fichas es lo que debe lograr el diseño: criterio.", "El máximo de 20 cm es un límite de tamaño: restricción."], "Criterio: sostiene 10 fichas. Restricción: base de 20 cm como máximo"),
        ("Hacer comprobable un criterio", "Un compañero escribe: «El soporte debe ser resistente». Reescríbelo para poder comprobarlo.", ["«Resistente» no dice cuánto.", "Agrego un número y una prueba.", "«Aguanta 10 fichas durante 1 minuto sin inclinarse»."], "Aguanta 10 fichas durante 1 minuto sin inclinarse"),
    ],
    mistakes=[
        ("Escribir criterios como «bonito» o «bueno».", "No se pueden comprobar y cada persona opina distinto.", "Usa un número, una medida o una acción que se pueda ver."),
        ("Confundir una restricción con una idea de solución.", "La restricción es un límite del problema, no el objeto que se usará.", "Pregunta: «¿esto limita lo que puedo hacer?». Si sí, es restricción."),
    ],
    R=[
        ("«Sostiene 10 fichas sin caerse» ¿es un criterio o una restricción?", "Un criterio", "Es lo que el diseño debe lograr."),
        ("«La base mide como máximo 20 cm» ¿es un criterio o una restricción?", "Una restricción", "Es un límite de tamaño."),
        ("¿Se puede comprobar «debe ser bonito»?", "No", "Cada persona opina distinto y no hay medida."),
    ],
    C=[
        ("¿Por qué «aguanta 10 fichas» es mejor criterio que «es fuerte»?", "Porque tiene un número y se puede comprobar", "Con el número se prueba y se obtiene un resultado claro."),
        ("«Solo cartón reutilizado y cinta» ¿es restricción de medida, de materiales o de tiempo?", "De materiales", "Limita con qué se puede construir."),
        ("Un diseño debe quedar listo en 40 minutos. ¿Qué tipo de restricción es?", "De tiempo", "Fija cuánto se puede demorar."),
    ],
    A=[
        arith("La base de un soporte puede medir como máximo 20 cm. Tu pieza mide 12 cm. ¿Cuántos centímetros más podría medir sin pasarse?", "20-12", "Se resta la medida actual del máximo permitido."),
        ("Reescribe como criterio comprobable: «La caja debe ser fácil de abrir».", "Se abre con una sola mano", "Describe una acción que se puede observar."),
        ("Problema: llevar la colación en el bus sin que se aplaste. Escribe un criterio de seguridad para el diseño.", "Sin bordes que corten ni puntas", "Un criterio de seguridad cuida a quien lo usa."),
    ],
    Z=[
        ("Rita escribió estos tres puntos para su soporte: A «mide menos de 20 cm», B «es lindo», C «sostiene 8 fichas». ¿Cuál no sirve como criterio y por qué?", "B, porque no se puede comprobar", "A y C se miden o se cuentan; B es una opinión."),
        ("Un diseño cumple todos los criterios pero tiene una base de 25 cm y el máximo era 20 cm. ¿Se puede aceptar?", "No", "Pasa una restricción, que es un límite que no se puede superar."),
    ],
    D=[
        arith("Un soporte para fichas debe pesar menos de 100 gramos. Usaste 45 g de cartón, 30 g de cinta y 40 g de papel. ¿Cuántos gramos pesa en total?", "45+30+40", "Se suman los pesos de los tres materiales."),
        ("Con el mismo soporte (45 g de cartón, 30 g de cinta y 40 g de papel, 115 g en total) y el máximo de 100 g, ¿cumple la restricción?", "No", "115 g es mayor que 100 g."),
    ],
    ctx=("Debes diseñar un porta-útiles para tu mesa. Datos del problema: tiene que guardar 5 lápices, no puede ocupar más de 15 cm de ancho y solo hay cartón reutilizado y cinta. Escribe dos criterios comprobables y dos restricciones.", "Criterios: guarda 5 lápices; se mantiene parado al soltarlo. Restricciones: ancho máximo 15 cm; solo cartón reutilizado y cinta", "Criterios con número o acción, restricciones con límite."),
    sc=[
        ("En Tecnología: ¿Qué es un criterio?", "Una condición comprobable que el diseño debe cumplir", "Dice qué debe lograr el diseño."),
        ("En Tecnología: ¿Qué es una restricción de diseño?", "Un límite que no se puede pasar", "Fija medida, material, tiempo o seguridad."),
        ("¿«Debe ser bonito» sirve como criterio?", "No", "No se puede comprobar."),
    ],
    open_task=(
        "Escoge un problema. Problema 1: guardar 6 lápices en tu mesa. Problema 2: sostener un libro abierto para leerlo sin usar las manos. Escribe tres criterios comprobables (uno de seguridad) y tres restricciones (una de medida, una de materiales y una de tiempo).",
        "Problema 1: criterios: guarda 6 lápices; no se cae al empujar suave; sin puntas que pinchen. Restricciones: base de 15 cm como máximo; solo cartón y cinta; listo en 40 minutos.",
        ["tres criterios con número o acción observable", "uno es de seguridad", "tres restricciones: medida, materiales y tiempo", "distingue criterio de restricción"],
        ["lista de tres criterios y tres restricciones"],
        ["criterios como «bonito»", "poner una solución en vez de un límite"],
        "Pregunta: «¿cómo comprobaría otra persona este criterio?». Si no puede, ayúdale a poner un número.",
    ),
    reinforce="Elige un objeto de tu casa, como una taza, y escribe dos criterios comprobables que cumple.",
    extend="Escribe un criterio de cuidado del ambiente para un diseño hecho con cartón reutilizado y explica cómo se comprobaría.",
)

# ------------------------------------------------------------------ OA 01, clase 3
reg(
    OA1, 3,
    materials="Hoja y lápiz. Los productos de los ejemplos se describen con palabras; no necesitas comprarlos.",
    use="Aprenderé a generar varias ideas distintas, también transformando productos que ya existen. Sirve para no quedarme con la primera idea.",
    prior=["Sé escribir criterios y restricciones.", "Sé que un producto existente es un objeto ya hecho."],
    explain=[
        "Generar ideas divergentes es crear muchas ideas que se diferencian entre sí en cómo funcionan. Dos ideas son distintas si resuelven el problema de otra manera, no si solo cambian el color. Primero se anotan todas las ideas, sin juzgarlas. Después se elige con los criterios.",
        "Una forma de crear ideas es explorar y transformar productos existentes. Puedes sustituir un material por otro, combinar partes de dos productos, adaptar un producto a otro uso, o quitar una parte que sobra. Por ejemplo, un frasco de plástico limpio y sin tapa se adapta para guardar lápices.",
        "También puedes mirar otras asignaturas. Si en Ciencias aprendiste que las plantas necesitan luz y agua, esa información da ideas para un regador. Registra cada idea con un nombre corto y un boceto rápido. Una lista de cuatro ideas distintas vale más que una sola idea muy pulida.",
    ],
    vocab=[("idea divergente", "idea que resuelve el problema de una manera distinta a las otras"), ("sustituir", "cambiar un material o una parte por otra"), ("combinar", "unir partes de dos productos"), ("adaptar", "usar un producto para otra función"), ("producto existente", "objeto que ya está hecho")],
    worked=[
        ("Transformar un producto existente", "Problema: guardar 6 lápices. Producto existente: un tubo de cartón de papel higiénico. Propón una idea que adapte y otra que combine.", ["Adaptar: parar el tubo en la mesa y usarlo de lapicero.", "Combinar: pegar tres tubos juntos con cinta para tener tres compartimientos.", "Son distintas porque funcionan de manera diferente."], "Adaptar: tubo parado. Combinar: tres tubos pegados"),
        ("Comprobar si dos ideas son distintas", "Idea A: lapicero de cartón rojo. Idea B: el mismo lapicero de cartón, pintado azul. ¿Son ideas distintas?", ["Funcionan igual.", "Solo cambia el color.", "No resuelven de otra manera."], "No, son la misma idea"),
    ],
    mistakes=[
        ("Contar como ideas distintas dos objetos iguales de distinto color.", "Funcionan de la misma manera.", "Cambia el funcionamiento: otra forma, otro material o otra manera de sostener."),
        ("Descartar ideas apenas se anotan.", "Aún no se han comparado con los criterios.", "Anota todas primero y elige después con los criterios."),
    ],
    R=[
        ("Un frasco de plástico limpio, sin tapa, se usa para guardar lápices. ¿Es una idea de adaptar o de quitar una parte?", "Adaptar", "Se usa un producto para un uso nuevo."),
        ("Cambiar un material por otro, por ejemplo cartón por tela, ¿es sustituir o combinar?", "Sustituir", "Se reemplaza un material por otro."),
        ("¿Se eligen las ideas antes o después de anotarlas todas?", "Después", "Primero se anotan sin juzgar y luego se elige con criterios."),
    ],
    C=[
        ("¿Por qué «lapicero rojo» y «lapicero azul» no son ideas divergentes?", "Porque funcionan de la misma manera", "Solo cambia el color."),
        ("Pegar dos cajas pequeñas con cinta para tener dos compartimientos, ¿es combinar o sustituir?", "Combinar", "Se unen partes de dos productos."),
        ("Quitar la tapa que estorba a una caja para que se abra más rápido, ¿es adaptar o quitar una parte?", "Quitar una parte", "Se elimina lo que sobra."),
    ],
    A=[
        ("Problema: colgar la mochila sin que toque el suelo mojado. Producto existente: una percha de ropa. Escribe una idea que adapte la percha.", "Colgar la mochila de la percha en el respaldo de la silla", "Usa la percha para un uso nuevo."),
        ("Problema: cargar 4 libros. Productos: cordel y una caja de cartón. Escribe una idea que combine los dos.", "Atar los libros con cordel y ponerlos en la caja con asas de cordel", "Une cordel y caja para resolver el problema."),
        arith("Una lista tiene 5 ideas, pero 2 son la misma con distinto color. ¿Cuántas ideas distintas hay?", "5-1", "Dos ideas iguales cuentan como una sola, así que se resta una."),
    ],
    Z=[
        ("Ema dice: «Mi idea 2 funciona como la 1, pero con otra tela». ¿Qué debe cambiar para que sea divergente?", "Cambiar cómo funciona", "El color o el material no cambian la manera de resolver."),
        ("Dos estudiantes tienen cuatro ideas cada uno. Ana: cuatro cajas de colores distintos. Beto: caja, cordel, bolsa y tubo. ¿Quién tiene ideas más divergentes?", "Beto", "Sus ideas funcionan distinto; las de Ana son iguales."),
    ],
    D=[
        ("Problema: regar un huerto pequeño sin derramar agua. En Ciencias aprendiste que la planta necesita agua en la tierra. Transforma un producto existente, un vaso de plástico limpio, en una idea de regador.", "Llenar el vaso con poca agua y verterla despacio sobre la tierra", "Adapta el vaso usando el dato de Ciencias."),
        ("Problema: sostener 3 hojas para leer de pie. Escribe tres ideas que funcionen de manera distinta.", "Pinza de ropa en una tabla; atril de cartón doblado; cordel colgado con clip", "Cada idea sostiene las hojas de otra manera."),
    ],
    ctx=("Sol quiere que su lonchera no se mueva en la mochila. Tiene cordel, una caja de cartón con tapa y un trozo de tela. Escribe tres ideas distintas y marca cuál combina dos materiales.", "Atar la lonchera con cordel al asa; meterla en la caja; envolverla en la tela. Combina dos: cordel y caja", "Tres formas distintas y una combinación."),
    sc=[
        ("¿Qué es una idea divergente?", "Una idea que resuelve el problema de una manera distinta", "Se diferencia por cómo funciona."),
        ("¿Cuáles son tres formas de transformar un producto?", "Sustituir, combinar, adaptar o quitar", "Son las formas vistas en la clase."),
        ("¿Cambiar solo el color da una idea nueva?", "No", "El funcionamiento sigue igual."),
    ],
    open_task=(
        "Escoge un problema. Problema 1: guardar 5 lápices en una mesa. Problema 2: sostener 3 hojas para leerlas de pie. Productos: pinza de ropa, caja de cartón, tubo de cartón, cordel. Escribe cuatro ideas distintas: una que sustituya, una que combine dos productos, una que adapte uno y una que quite una parte. Dibuja un boceto de una.",
        "Problema 1: sustituir: lapicero de tela en vez de cartón; combinar: tubo parado en caja; adaptar: pinzas en el borde de la caja; quitar: caja sin tapa. Boceto de la combinación.",
        ["escribe cuatro ideas con las cuatro formas", "usa productos de la lista", "cada idea funciona de manera distinta", "dibuja un boceto de una"],
        ["lista de cuatro ideas con nombre y un boceto"],
        ["ideas iguales con distinto color", "no usar los productos dados"],
        "Pregunta: «¿cómo funciona esta idea comparada con la otra?». Si funcionan igual, pide una forma nueva.",
    ),
    reinforce="Mira dos objetos de tu casa y piensa cómo podrías unirlos para resolver un problema pequeño.",
    extend="Escribe tres ideas para guardar tijeras de punta roma, usando algo que normalmente se bota.",
)

# ------------------------------------------------------------------ OA 01, clase 4
reg(
    OA1, 4,
    materials="Hoja, lápiz y regla. Las medidas y las vistas están descritas en este cuaderno; no necesitas ninguna caja real.",
    use="Aprenderé a representar un diseño con un boceto a mano alzada y con un dibujo técnico simple que lleva medidas. Sirve para que otra persona entienda mi idea.",
    prior=["Sé hacer un boceto rápido.", "Sé medir y escribir centímetros."],
    explain=[
        "Un boceto a mano alzada se dibuja sin regla, rápido y sin borrar mucho. Sirve para pensar y mostrar una idea. Debe verse la forma general y tener rótulos, que son palabras que nombran las partes, como «tapa» o «asa». Un boceto puede cambiar mucho antes de construir.",
        "Un dibujo técnico muestra el objeto con exactitud. Se dibuja con regla y lleva medidas escritas en centímetros, llamadas cotas. Un objeto se puede dibujar en tres vistas: la vista frontal, que es lo que ves de frente; la vista superior, que es lo que ves desde arriba; y la vista lateral, que es lo que ves de costado.",
        "Cada vista muestra solo dos medidas. En una caja, la vista frontal muestra el largo y el alto. La vista superior muestra el largo y el ancho. La vista lateral muestra el ancho y el alto. También se puede dibujar con TIC, usando un programa de dibujo en el computador, pero las reglas de las vistas y las cotas son las mismas.",
    ],
    vocab=[("boceto", "dibujo rápido a mano alzada"), ("dibujo técnico", "dibujo con regla y medidas"), ("cota", "medida escrita en el dibujo"), ("vista frontal", "lo que se ve de frente"), ("vista superior", "lo que se ve desde arriba")],
    worked=[
        ("Elegir la vista para cada medida", "Una caja mide 12 cm de largo, 8 cm de ancho y 10 cm de alto. ¿Qué medidas muestra la vista frontal?", ["La vista frontal se ve de frente.", "Se ve cuánto mide a lo largo y cuánto de alto.", "El ancho queda hacia el fondo y no se ve."], "El largo (12 cm) y el alto (10 cm)"),
        ("Forma de la vista superior", "Un vaso cilíndrico parado en la mesa se mira desde arriba. ¿Qué forma tiene la vista superior?", ["Desde arriba se ve la boca del vaso.", "La boca es redonda."], "Un círculo"),
    ],
    mistakes=[
        ("Escribir una medida en el dibujo sin la unidad.", "Sin «cm» no se sabe si son centímetros, metros u otra unidad.", "Escribe siempre el número con su unidad, por ejemplo 12 cm."),
        ("Pensar que una sola vista muestra las tres medidas.", "Cada vista solo muestra dos medidas.", "Dibuja la vista frontal, la superior y la lateral."),
    ],
    R=[
        ("Un dibujo hecho sin regla, rápido, para mostrar una idea, ¿es un boceto o un dibujo técnico?", "Un boceto", "Se hace a mano alzada y rápido."),
        ("La medida escrita en un dibujo técnico se llama...", "Cota", "Es el nombre de la medida escrita."),
        ("La vista que se ve desde arriba se llama...", "Vista superior", "Es la que mira el objeto desde arriba."),
    ],
    C=[
        ("Una caja mide 12 cm de largo, 8 cm de ancho y 10 cm de alto. ¿Qué dos medidas muestra la vista superior?", "El largo y el ancho", "Desde arriba se ve el largo y el ancho."),
        ("¿Qué dos medidas muestra la vista lateral de esa caja?", "El ancho y el alto", "De costado se ve el ancho y el alto."),
        ("¿Para qué sirve escribir rótulos en un boceto?", "Para nombrar las partes", "Así otra persona entiende cada parte."),
    ],
    A=[
        ("Una caja mide 6 cm de largo, 4 cm de ancho y 6 cm de alto. ¿Su vista frontal puede ser un cuadrado de 6 cm por 6 cm?", "Sí", "La vista frontal muestra largo y alto, y ambos miden 6 cm."),
        arith("En un soporte, la vista frontal muestra el largo de 14 cm y la lateral muestra el ancho de 5 cm. La base del soporte es un rectángulo. ¿Cuántos centímetros mide su contorno (la suma de sus cuatro lados)?", "14+5+14+5", "El contorno suma los cuatro lados del rectángulo."),
        ("¿Qué vistas de una caja muestran su alto: solo la frontal, solo la superior, o la frontal y la lateral?", "La frontal y la lateral", "La frontal muestra largo y alto, la lateral muestra ancho y alto; la superior no muestra el alto."),
    ],
    Z=[
        ("Un compañero dibuja solo la vista superior de un soporte y dice que ya se entiende el alto. ¿Tiene razón?", "No", "La vista superior no muestra el alto."),
        ("Dos dibujos de una caja: A tiene las medidas 12, 8 y 10, sin unidad. B tiene 12 cm, 8 cm y 10 cm. ¿Cuál se puede usar para construir?", "B", "A no dice en qué unidad están las medidas."),
    ],
    D=[
        arith("Una caja para guardar fichas mide 16 cm de largo y 9 cm de alto en la vista frontal. En la vista superior mide 16 cm de largo y 9 cm de ancho. Para la cinta que rodea el borde de la tapa, ¿cuántos centímetros mide el contorno de la tapa (la suma de sus cuatro lados)?", "16+9+16+9", "La tapa es un rectángulo de 16 por 9, y se suman sus cuatro lados."),
        ("Una lata se mira de frente y se ve un rectángulo. Desde arriba se ve un círculo. ¿Qué forma tiene el objeto: un cubo o un cilindro?", "Un cilindro", "El rectángulo de frente y el círculo desde arriba corresponden a un cilindro."),
    ],
    ctx=("Quieres mostrar a tu curso un porta-lápices en forma de caja de 10 cm de largo, 6 cm de ancho y 12 cm de alto. Escribe las medidas con unidad que van en la vista frontal y en la vista superior.", "Frontal: 10 cm de largo y 12 cm de alto. Superior: 10 cm de largo y 6 cm de ancho", "Cada vista lleva dos cotas con su unidad."),
    sc=[
        ("¿Qué diferencia hay entre un boceto y un dibujo técnico?", "El boceto es rápido y a mano alzada; el técnico es exacto y lleva medidas", "El técnico usa regla y cotas."),
        ("¿Qué vista muestra el largo y el alto?", "La frontal", "De frente se ve lo largo y lo alto."),
        ("¿Qué debe llevar cada medida escrita?", "Su unidad", "Sin unidad no se sabe cuánto es."),
    ],
    open_task=(
        "Escoge un objeto: Objeto 1: una caja de 12 cm de largo, 8 cm de ancho y 10 cm de alto. Objeto 2: un lapicero cilíndrico de 7 cm de ancho (diámetro) y 11 cm de alto; visto desde arriba es un círculo, que puedes dibujar rodeando una tapa redonda de 7 cm. Haz un boceto con rótulos y un dibujo técnico con regla de la vista frontal y de la superior, con las medidas escritas con unidad.",
        "Objeto 1: boceto con rótulos «tapa» y «cuerpo»; vista frontal 12 cm por 10 cm; vista superior 12 cm por 8 cm.",
        ["boceto con rótulos", "dibujo con regla", "dos vistas correctas", "cotas con unidad"],
        ["boceto y dibujo de dos vistas con medidas"],
        ["medidas sin unidad", "poner el alto en la vista superior"],
        "Pregunta: «¿esta vista muestra esa medida desde donde la miras?». Si no, pídele cambiar de vista.",
    ),
    reinforce="Mira una caja de tu casa y di cuál es su vista frontal, superior y lateral.",
    extend="Dibuja a mano alzada un objeto de tu mesa en vista frontal y superior, y escribe sus medidas con regla.",
)

# ------------------------------------------------------------------ OA 01, clase 5
reg(
    OA1, 5,
    materials="Papel, cartón reutilizado, cinta y tijeras de punta roma si construyes; si no, solo lápiz y papel. Los datos están escritos en este cuaderno.",
    use="Aprenderé a construir un modelo, concreto o digital, para probar mi idea antes de hacer el objeto final. Sirve para descubrir fallas sin gastar mucho material.",
    prior=["Sé dibujar un boceto con medidas.", "Sé que un criterio se puede comprobar."],
    explain=[
        "Un modelo es una versión simple de un diseño que sirve para probar una idea. Un modelo concreto se hace con materiales: papel, cartón o cinta. Un modelo digital se hace en el computador, con un programa de dibujo, y se puede mover o cambiar de tamaño fácilmente. Los dos permiten ver si la idea funciona.",
        "Un modelo no tiene que ser perfecto, pero sí debe mostrar lo importante del diseño. Si quieres probar si un soporte aguanta fichas, el modelo debe tener la misma forma de la base. A veces el modelo es más pequeño que el objeto real. Entonces las medidas se reducen siempre en la misma proporción: si es a la mitad, todas se dividen por 2.",
        "Después de construir, compara el modelo con los criterios y las restricciones. Anota qué falló y qué cambiarías. Una falla encontrada en el modelo es una buena noticia, porque se corrige antes de gastar los materiales finales. Conserva el modelo o una foto o dibujo, para documentar el proceso.",
    ],
    vocab=[("modelo", "versión simple de un diseño para probar una idea"), ("modelo concreto", "modelo hecho con materiales"), ("modelo digital", "modelo hecho en el computador"), ("reducir a la mitad", "dividir todas las medidas por 2"), ("falla", "algo que no cumple un criterio")],
    worked=[
        ("Reducir un modelo a la mitad", "El soporte real mide 20 cm de largo y 12 cm de alto. Haces un modelo a la mitad. ¿Cuánto miden el largo y el alto del modelo?", ["A la mitad significa dividir por 2.", "20 ÷ 2 = 10.", "12 ÷ 2 = 6."], "10 cm de largo y 6 cm de alto"),
        ("Usar el modelo para encontrar una falla", "Tu modelo de soporte se cae cuando le pones 4 fichas, y el criterio dice que debe sostener 10. ¿Qué haces?", ["La falla se vio en el modelo.", "Cambio la base: la hago más ancha.", "Vuelvo a probar el modelo."], "Ensancho la base y pruebo de nuevo"),
    ],
    mistakes=[
        ("Reducir solo una medida del modelo.", "La forma queda deformada y no sirve para probar.", "Divide todas las medidas por el mismo número."),
        ("Hacer el modelo muy bonito y no probarlo.", "Un modelo sirve para probar, no para adornar.", "Compáralo con los criterios y anota las fallas."),
    ],
    R=[
        ("Un modelo hecho con papel y cinta, ¿es concreto o digital?", "Concreto", "Se construye con materiales reales."),
        ("Un modelo hecho en un programa de dibujo del computador, ¿es concreto o digital?", "Digital", "Se hace con TIC."),
        ("¿El modelo se hace para probar la idea o para guardarla sin usar?", "Para probar la idea", "Sirve para descubrir fallas."),
    ],
    C=[
        ("¿Por qué conviene encontrar una falla en el modelo y no en el objeto final?", "Porque se corrige antes de gastar los materiales finales", "El modelo cuesta menos material."),
        ("Si el modelo es a la mitad, ¿qué se hace con todas las medidas?", "Se dividen por 2", "La mitad significa dividir por 2."),
        ("¿Qué ventaja tiene un modelo digital?", "Se puede cambiar de tamaño y mover fácilmente", "En el computador se corrige sin gastar material."),
    ],
    A=[
        arith("Un soporte real mide 24 cm de largo. Haces un modelo a la mitad. ¿Cuántos centímetros mide el largo del modelo?", "24//2", "A la mitad significa dividir por 2."),
        ("Tu modelo de papel se dobla cuando le pones 3 fichas, y el criterio pide 10. ¿Qué es lo que falló: el criterio o el modelo?", "El modelo", "No cumple el criterio de sostener 10 fichas."),
        ("Quieres probar si una caja de 25 cm de alto cabe en una mochila de 30 cm de alto. ¿Qué modelo sirve: uno de 25 cm de alto o un dibujo sin medidas?", "Uno de 25 cm de alto", "Para probar el tamaño necesitas las medidas reales."),
    ],
    Z=[
        ("Leo hizo un modelo a la mitad con el largo reducido a la mitad, pero dejó el alto igual que el real. ¿Por qué no sirve para probar?", "Porque la forma quedó deformada", "Todas las medidas deben reducirse por igual."),
        ("Un modelo digital y uno concreto muestran la misma falla. ¿Cuál de los dos habría gastado menos materiales?", "El digital", "El digital no usa cartón ni cinta."),
    ],
    D=[
        arith("Un soporte real mide 30 cm de largo, 18 cm de alto y 12 cm de ancho. Haces un modelo a la mitad. ¿Cuántos centímetros mide su alto?", "18//2", "A la mitad significa dividir el alto por 2."),
        arith("Con ese mismo modelo a la mitad, ¿cuántos centímetros mide su ancho? (el ancho real es 12 cm)", "12//2", "También se divide el ancho por 2."),
    ],
    ctx=("Quieres diseñar un soporte para sostener 10 fichas con una base de 20 cm como máximo. Tu primer modelo de cartón mide 15 cm de base y se inclina con 6 fichas. Escribe la falla, un cambio concreto y qué volverás a probar.", "Falla: se inclina con 6 fichas. Cambio: ensanchar la base hasta 20 cm. Probar: con 10 fichas", "Nombra falla, cambio posible dentro de la restricción y nueva prueba."),
    sc=[
        ("¿Para qué sirve un modelo?", "Para probar una idea antes de hacer el objeto final", "Permite descubrir fallas con poco material."),
        ("¿Cuál es la diferencia entre un modelo concreto y uno digital?", "El concreto usa materiales y el digital se hace en el computador", "Cambia dónde se construye."),
        ("Si el modelo es a la mitad, ¿se reducen todas las medidas o solo una?", "Todas", "Si no, la forma se deforma."),
    ],
    open_task=(
        "Escoge un diseño. Diseño 1: soporte de cartón para 10 fichas, con base de 20 cm como máximo. Diseño 2: caja de papel para guardar 5 lápices, de 10 cm de alto como máximo. Construye un modelo con papel y cinta (o, si tienes un computador con programa de dibujo, hazlo como modelo digital), pruébalo con tus criterios y anota una falla y un cambio.",
        "Diseño 1: modelo de cartón con base de 18 cm; con 10 fichas se inclinó; cambio: ensanchar la base a 20 cm.",
        ["construye o dibuja el modelo", "lo prueba con un criterio", "anota una falla", "propone un cambio dentro de la restricción"],
        ["modelo o dibujo y nota de falla y cambio"],
        ["modelo sin probar", "cambiar una medida pasándose del límite"],
        "Pregunta: «¿qué criterio no cumplió el modelo?». Si no puede decirlo, pídele repetir la prueba.",
    ),
    reinforce="Haz con una hoja de papel un modelo simple de una caja y comprueba si cabe un lápiz.",
    extend="Explica con tus palabras por qué un modelo a la mitad debe tener todas las medidas a la mitad.",
)

# ------------------------------------------------------------------ OA 01, clase 6
reg(
    OA1, 6,
    materials="Hoja y lápiz. Las tablas con puntajes están escritas en este cuaderno.",
    use="Aprenderé a elegir entre propuestas con una tabla de criterios y a comunicar mi decisión. Sirve para que otras personas entiendan por qué elegí esa idea.",
    prior=["Sé escribir criterios y restricciones.", "Sé hacer un modelo y probarlo."],
    explain=[
        "Cuando tienes varias propuestas, necesitas elegir una. Para elegir bien se usa una tabla de criterios. En las filas van las propuestas y en las columnas los criterios. Por cada criterio, escribes 1 punto si la propuesta lo cumple y 0 si no lo cumple. Luego sumas los puntos de cada propuesta.",
        "La propuesta con más puntos cumple más criterios. Pero antes revisa las restricciones: si una propuesta rompe una restricción, no se puede elegir aunque tenga muchos puntos. Si dos propuestas empatan, usas un criterio de desempate acordado antes, por ejemplo la que gasta menos material.",
        "Después comunica tu propuesta. Una buena comunicación dice cuatro cosas: para quién es (el usuario), qué problema resuelve, cómo funciona y por qué la elegiste, con datos de las pruebas. Puedes mostrar el boceto, el dibujo técnico y el modelo. También cuenta qué mejorarías si tuvieras más tiempo.",
    ],
    vocab=[("tabla de criterios", "tabla que compara propuestas según criterios"), ("propuesta", "idea de diseño que se presenta para elegir"), ("desempate", "criterio extra para elegir cuando hay igualdad de puntos"), ("comunicar", "mostrar y explicar el diseño a otras personas"), ("argumento", "razón con datos que apoya una decisión")],
    worked=[
        ("Sumar puntos de una tabla", "Propuesta A cumple 3 de los 4 criterios. Propuesta B cumple 2. Ninguna rompe una restricción. ¿Cuál se elige?", ["A obtiene 3 puntos.", "B obtiene 2 puntos.", "3 es mayor que 2."], "La propuesta A"),
        ("Revisar la restricción antes de elegir", "La propuesta C obtiene 4 puntos, pero mide 25 cm de base y el máximo es 20 cm. La propuesta D obtiene 3 puntos y mide 18 cm. ¿Cuál se elige?", ["C rompe la restricción de la base.", "D la cumple.", "Se elige entre las que cumplen las restricciones."], "La propuesta D"),
    ],
    mistakes=[
        ("Elegir la propuesta que más gusta sin mirar la tabla.", "La preferencia personal no es un criterio comprobable.", "Suma los puntos y revisa las restricciones."),
        ("Presentar solo el dibujo sin decir para quién es.", "Falta explicar el problema y el usuario.", "Comunica usuario, problema, funcionamiento y razón de la elección."),
    ],
    R=[
        ("En la tabla de criterios, si una propuesta cumple un criterio, ¿cuántos puntos recibe?", "1 punto", "Cumple vale 1 y no cumple vale 0."),
        ("Si una propuesta rompe una restricción, ¿se puede elegir?", "No", "Las restricciones son límites que no se pueden pasar."),
        ("¿Qué se suma en la tabla para decidir?", "Los puntos de cada propuesta", "Se suman los criterios cumplidos."),
    ],
    C=[
        ("¿Para qué sirve una tabla de criterios?", "Para comparar propuestas con los mismos criterios", "Así la decisión se basa en datos y no en gustos."),
        ("Dos propuestas empatan en 3 puntos. ¿Qué haces?", "Usar el criterio de desempate acordado", "El desempate se decidió antes de comparar."),
        ("¿Cuál de estas es una razón para elegir? A «me gusta el color», B «sostuvo las 10 fichas en las 3 pruebas».", "B", "B es un dato de una prueba y A es un gusto."),
    ],
    A=[
        arith("Una propuesta cumple 4 criterios en una tabla de 5. ¿Cuántos criterios NO cumple?", "5-4", "Se restan los cumplidos del total."),
        ("Propuesta E: 3 puntos y mide 19 cm de base. Propuesta F: 4 puntos y mide 22 cm de base. El máximo de la base es 20 cm. ¿Cuál eliges?", "E", "F rompe la restricción de la base."),
        ("Escribe una frase que diga para quién es el diseño: soporte de cartón para que Pía sostenga 3 hojas al leer de pie.", "Es para Pía, que necesita sostener 3 hojas al leer de pie", "Nombra al usuario y su necesidad."),
    ],
    Z=[
        ("Una propuesta tiene 5 puntos y otra 4, pero la de 5 usa un material que no hay en la sala. ¿Qué restricción rompe?", "La de materiales", "Se pidió usar solo lo disponible."),
        ("Mara dice: «Elegí esta porque es la más linda». ¿Qué le falta a su argumento?", "Datos de criterios o pruebas", "Una razón comprobable usa criterios o resultados."),
    ],
    D=[
        arith("Tres propuestas cumplen 3, 4 y 2 criterios. ¿Cuántos puntos suman entre las tres?", "3+4+2", "Se suman los puntos de las tres."),
        arith("Una tabla tiene 5 criterios y 3 propuestas. Si cada propuesta se evalúa en todos los criterios, ¿cuántas casillas hay que completar?", "5*3", "Hay 5 casillas por cada una de las 3 propuestas."),
    ],
    ctx=("Elegiste entre dos soportes para fichas. Soporte 1: sostiene 10 fichas y mide 18 cm de base. Soporte 2: sostiene 8 fichas y mide 15 cm de base. El criterio es sostener 10 fichas y la base máxima es 20 cm. Elige uno y comunica tu decisión en dos frases.", "Elijo el soporte 1 porque sostiene las 10 fichas pedidas y su base de 18 cm cumple el máximo de 20 cm. El soporte 2 no llega a las 10 fichas", "Elige el 1 y argumenta con criterio y restricción."),
    sc=[
        ("¿Qué se hace primero: revisar restricciones o sumar puntos?", "Revisar restricciones", "Una propuesta que rompe una restricción no se puede elegir."),
        ("¿Qué cuatro cosas dice una buena comunicación?", "Para quién es, qué problema resuelve, cómo funciona y por qué se eligió", "Así se entiende el diseño."),
        ("¿Una razón basada en datos es mejor que una basada en gustos?", "Sí", "Los datos se pueden comprobar."),
    ],
    open_task=(
        "Usa tus ideas de las clases anteriores o escoge un problema: guardar 6 lápices. Compara dos propuestas con una tabla de 4 criterios (guarda 6 lápices, se mantiene de pie, no tiene puntas, se mueve con una mano). La base máxima de 15 cm es una restricción. Suma los puntos, revisa la restricción y presenta tu elección en cuatro frases: usuario, problema, funcionamiento y razón con datos.",
        "Propuesta A: tubos pegados (3 puntos). Propuesta B: caja abierta (4 puntos). Elijo B para Sebastián, que necesita guardar 6 lápices en su mesa. Funciona como una caja con compartimientos y cumple los 4 criterios.",
        ["tabla con cuatro criterios", "suma los puntos", "revisa las restricciones", "comunica usuario, problema, funcionamiento y razón con datos"],
        ["tabla y texto de cuatro frases"],
        ["elegir por gusto", "omitir las restricciones"],
        "Pregunta: «¿qué dato de tu tabla apoya tu elección?». Si no tiene, pídele volver a la tabla.",
    ),
    reinforce="Elige entre dos objetos de tu casa para una tarea y anota tres razones comprobables de tu elección.",
    extend="Prepara una presentación de un minuto con las cuatro frases de la comunicación para un diseño que imagines.",
)
