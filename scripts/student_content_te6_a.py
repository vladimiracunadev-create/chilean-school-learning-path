"""Cuaderno del estudiante, 6.º básico Tecnología: OA 01 (crear diseños de objetos y sistemas tecnológicos), clases 1 a 6.

Seguridad: solo papel, cartón, cinta, cordel y tijeras de punta roma; nada de cortadores, fuego, vidrio ni herramientas con filo.
Medidas enteras en centímetros, milímetros y gramos. Las pantallas se describen con texto, son ejemplos sin marcas y todo tiene alternativa en papel.
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "TE06 OA 01"


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
    materials="Hoja, lápiz y los casos escritos en este cuaderno. Si quieres, una persona de tu casa para comentar tus ideas.",
    use="Aprenderé a encontrar una necesidad en distintos ámbitos y en otras asignaturas, a pensar cómo innovar y a escribir criterios que se puedan comprobar. Sirve para empezar un diseño con una meta clara.",
    prior=["Sé que un usuario es quien usará un objeto.", "Sé que un criterio es una condición que se puede comprobar.", "Sé distinguir un problema de una oportunidad."],
    explain=[
        "Un diseño parte de una necesidad: un problema que resolver o una oportunidad que aprovechar. Las necesidades aparecen en muchos ámbitos tecnológicos, que son áreas de la vida como el hogar, la escuela, el transporte, la alimentación, la comunicación o el cuidado del ambiente. También aparecen en los tópicos, es decir, los temas de otras asignaturas.",
        "En 6.º básico se espera que innoves. Innovar es mejorar un producto que ya existe o crear uno nuevo que aporte algo distinto. Para innovar, mira un objeto conocido y pregúntate qué le falta, qué le sobra o qué podría hacer mejor. Copiar un objeto igual no es innovar.",
        "Antes de dibujar, escribe el usuario, la necesidad sin nombrar el objeto y los criterios. Un criterio es una condición con número o acción que se puede comprobar, como «pesa menos de 400 g». También anota las restricciones, que son los límites del problema, como el tamaño máximo o el dinero disponible.",
    ],
    vocab=[("ámbito tecnológico", "área de la vida donde se usa la tecnología"), ("tópico", "tema de otra asignatura que inspira un diseño"), ("innovar", "mejorar un producto existente o crear uno nuevo que aporte algo"), ("criterio", "condición comprobable que el diseño debe cumplir"), ("restricción", "límite del problema, como tamaño o costo")],
    worked=[
        ("De un tópico a una necesidad", "En Ciencias Naturales, un curso midió que la tierra de una bandeja de germinados se seca en 2 días. Escribe usuario, necesidad sin objeto y un criterio.", ["Usuario: el curso que cuida los germinados.", "Necesidad: mantener la tierra húmeda más tiempo, sin nombrar el objeto.", "Criterio con número: la tierra sigue húmeda al cuarto día."], "Usuario: el curso. Necesidad: mantener húmeda la tierra más tiempo. Criterio: húmeda al cuarto día"),
        ("Innovar sobre un producto conocido", "Una regla de plástico se resbala del cuaderno al medir y no se ve bien en la hoja. Propón una innovación y un criterio.", ["Observo qué falla: se resbala y tapa la línea.", "Innovo agregando una base que agarra la hoja y un borde transparente.", "Criterio: no se desliza al empujarla con un dedo."], "Una regla con base que agarra la hoja; criterio: no se desliza al empujarla con un dedo"),
    ],
    mistakes=[
        ("Escribir «necesito una mochila nueva» como necesidad.", "Nombra la solución antes de entender qué se debe lograr.", "Escribe qué se debe lograr: «transportar mis útiles sin que se mojen»."),
        ("Decir «innovar» y copiar un objeto igual con otro color.", "Un cambio de color no aporta nada a la necesidad.", "Pregunta qué mejora el uso del objeto y cámbialo por eso."),
    ],
    R=[
        ("Un curso tiene 15 cajas de cartón limpias guardadas sin uso. ¿Es un problema o una oportunidad?", "Una oportunidad", "Nada falla; hay un recurso que se puede aprovechar."),
        ("En el recreo la pelota se pierde en unos arbustos casi todos los días. ¿Es un problema o una oportunidad?", "Un problema", "Algo falla: se pierde la pelota."),
        ("«Transporte», «comunicación» y «alimentación», ¿son ámbitos tecnológicos o criterios?", "Ámbitos tecnológicos", "Son áreas de la vida donde se usa la tecnología."),
    ],
    C=[
        ("Innovar es: A copiar exactamente un producto, B mejorar un producto o crear uno nuevo que aporte algo. ¿Cuál es?", "B", "Innovar agrega un aporte nuevo."),
        ("¿Cuál necesidad no nombra la solución? A «Necesito una lámpara de cartón», B «Necesito leer sin molestar a quien duerme».", "B", "B dice qué lograr; A ya nombra el objeto."),
        ("¿Cuál es un criterio comprobable? A «Resiste 20 aperturas sin romperse», B «Es bien bonito», C «Dura harto».", "A", "Solo A se comprueba contando."),
    ],
    A=[
        arith("El nuevo producto debe pesar como máximo 500 g. Su prototipo pesa 380 g. ¿Cuántos gramos le sobran al límite?", "500-380", "Se resta el peso del prototipo del límite.", " g"),
        ("Un criterio dice «ancho máximo de 25 cm para caber en un cajón». La idea X mide 22 cm, la Y 27 cm y la Z 25 cm. ¿Cuáles cumplen?", "X y Z", "22 y 25 no pasan el máximo de 25; 27 sí lo pasa."),
        ("Los vecinos de un pasaje quieren que los autos bajen la velocidad. Escribe el usuario y la necesidad sin nombrar un objeto.", "Usuario: vecinos y conductores del pasaje. Necesidad: lograr que los autos bajen la velocidad", "Se nombra a quién usa y qué se debe lograr, no la solución."),
    ],
    Z=[
        ("Dani escribe el criterio «el envase debe ser ecológico». Elena escribe «usa solo cartón reutilizado y pesa menos de 100 g». ¿Cuál se puede comprobar?", "El de Elena", "Tiene un material y un número que se pueden verificar."),
        ("Un curso quiere aprovechar 60 tapas de botella y no comprar otras. Idea 1 usa 24 tapas, idea 2 usa 72 y idea 3 usa 60. ¿Cuál cumple?", "La idea 3", "La 1 deja tapas sin usar y la 2 obliga a conseguir más."),
    ],
    D=[
        arith("Un organizador tiene 4 compartimentos de 6 cm de ancho cada uno y una pared de 1 cm solo entre compartimentos vecinos. ¿Cuántos centímetros mide de ancho en total?", "4*6+3*1", "Hay 4 compartimentos y 3 paredes entre ellos.", " cm"),
        ("Criterios: pesa menos de 400 g, cuesta $2.000 o menos y se arma en 30 minutos o menos. Idea A: 350 g, $2.500, 25 min. Idea B: 390 g, $1.800, 30 min. Idea C: 410 g, $1.500, 20 min. ¿Cuál cumple los tres?", "La idea B", "A cuesta más de $2.000 y C pesa más de 400 g."),
    ],
    ctx=("En Educación Física el curso pierde 5 minutos de cada clase buscando conos y chalecos que están mezclados en una caja. Escribe el ámbito, si es problema u oportunidad, la necesidad sin nombrar un objeto y un criterio con número.", "Ámbito: la escuela. Es un problema. Necesidad: encontrar el material en menos tiempo. Criterio: se encuentran los conos y chalecos en menos de 1 minuto", "Une ámbito, tipo de necesidad, necesidad sin objeto y criterio con número."),
    sc=[
        ("¿Un tema de otra asignatura puede inspirar un diseño?", "Sí", "Los tópicos de otras asignaturas son fuente de necesidades."),
        ("¿Cambiar solo el color de un objeto es innovar?", "No", "No mejora el uso ni aporta algo nuevo."),
        ("¿Qué debe tener un criterio?", "Un número o una acción que se pueda comprobar", "Así se decide si se cumple."),
    ],
    open_task=(
        "Escoge un caso. Caso 1 (Artes Visuales): el curso guarda sus pinceles en un vaso y se mezclan los gruesos con los finos. Caso 2 (Matemática): para medir en el patio, el curso usa una huincha que se enreda al guardarla. Escribe el usuario, la necesidad sin nombrar un objeto, una idea para innovar y dos criterios con número.",
        "Caso 1: usuario, el curso de Artes. Necesidad: encontrar pronto el pincel que se necesita. Innovación: separar por grosor. Criterios: 2 grupos de pinceles; saca un pincel en menos de 10 segundos",
        ["nombra al usuario", "la necesidad no nombra un objeto", "propone una innovación concreta", "dos criterios con número o acción observable"],
        ["ficha con usuario, necesidad, innovación y dos criterios"],
        ["nombrar el objeto en la necesidad", "criterios que no se pueden comprobar"],
        "Pregunta: «¿cómo contarías o medirías este criterio?». Si no puede, pídele agregar un número.",
    ),
    reinforce="Mira un objeto de tu casa, escribe qué le falta y propone una innovación en una frase.",
    extend="Elige un tema que hayas visto en Ciencias o en Matemática y escribe una necesidad que un objeto podría resolver con ese tema.",
)

# ------------------------------------------------------------------ OA 01, clase 2
reg(
    OA1, 2,
    materials="Hoja, lápiz y regla. Las medidas están escritas en este cuaderno. Si tienes computador, un programa de dibujo; si no, todo se hace en papel.",
    use="Aprenderé a representar un diseño con dibujo a mano alzada, dibujo técnico o un programa de dibujo, y a usar escalas. Sirve para que otra persona pueda construir lo que imaginaste.",
    prior=["Sé que un boceto es un dibujo rápido a mano alzada.", "Sé que las vistas muestran dos medidas cada una.", "Sé que la escala 1:2 hace el dibujo de la mitad del tamaño real."],
    explain=[
        "Un diseño se puede representar de tres maneras. El dibujo a mano alzada es rápido y sirve para probar ideas. El dibujo técnico usa regla, vistas y cotas, que son las medidas escritas sobre el dibujo. El dibujo con TIC se hace en un programa del computador: permite deshacer, copiar formas y guardar versiones.",
        "Recuerda las vistas: la frontal muestra ancho y alto, la superior muestra ancho y fondo, y la lateral muestra fondo y alto. Con las tres vistas, otra persona conoce las tres medidas del objeto. Un objeto grande no cabe en la hoja, por eso se dibuja en escala.",
        "La escala 1:5 significa que 1 cm del dibujo vale 5 cm del objeto real. Para saber cuánto mide el dibujo, divides la medida real entre 5. Para saber cuánto mide el objeto real, multiplicas la medida del dibujo por 5. Siempre escribe la escala en la hoja.",
    ],
    vocab=[("mano alzada", "dibujo hecho sin regla"), ("dibujo técnico", "dibujo con vistas, regla y medidas"), ("cota", "medida escrita sobre el dibujo"), ("escala", "relación entre el dibujo y el tamaño real"), ("TIC", "tecnologías de la información y la comunicación, como un computador")],
    worked=[
        ("Dibujar en escala 1:5", "Una repisa real mide 60 cm de largo. ¿Cuánto mide en un dibujo a escala 1:5?", ["En 1:5, el dibujo es 5 veces más pequeño.", "Divido 60 entre 5."], "12 cm"),
        ("Leer una vista", "Un cajón mide 40 cm de ancho, 30 cm de fondo y 15 cm de alto. ¿Qué dos medidas muestra la vista superior?", ["La vista superior se mira desde arriba.", "Desde arriba se ve el ancho y el fondo."], "40 cm y 30 cm"),
    ],
    mistakes=[
        ("Dibujar a escala y olvidar escribirla.", "Nadie sabrá cuánto mide el objeto real.", "Escribe la escala, por ejemplo «escala 1:5», en una esquina de la hoja."),
        ("Multiplicar por 5 la medida real para dibujar en 1:5.", "El dibujo debe ser más pequeño y así sale más grande.", "Para dibujar, divide la medida real entre 5."),
    ],
    R=[
        ("¿Qué vista muestra el fondo y el alto de un objeto?", "La vista lateral", "Se mira de costado."),
        ("Una medida escrita sobre un dibujo técnico, ¿cómo se llama?", "Cota", "Las medidas del dibujo se llaman cotas."),
        ("En un programa de dibujo, ¿qué permite hacer el botón «deshacer»?", "Volver atrás el último cambio", "Sirve para corregir sin borrar todo."),
    ],
    C=[
        ("Para probar cinco ideas en pocos minutos, ¿conviene dibujo a mano alzada o dibujo técnico?", "Dibujo a mano alzada", "Es rápido y se puede cambiar."),
        ("¿Qué significa escala 1:5?", "Que 1 cm del dibujo vale 5 cm reales", "El dibujo es 5 veces más pequeño."),
        ("Una vista frontal muestra el ancho y el alto de una caja. ¿Qué medida falta para conocer todo el objeto?", "El fondo", "La frontal no muestra la profundidad."),
    ],
    A=[
        arith("Una mesa real mide 90 cm de largo. ¿Cuántos centímetros mide en un dibujo a escala 1:5?", "90//5", "Se divide la medida real entre 5.", " cm"),
        arith("En un dibujo a escala 1:5, el alto de un estante mide 7 cm. ¿Cuántos centímetros mide el estante real?", "7*5", "Se multiplica la medida del dibujo por 5.", " cm"),
        ("Un estante mide 80 cm de ancho, 25 cm de fondo y 35 cm de alto. ¿Qué dos medidas muestra la vista frontal?", "80 cm y 35 cm", "La frontal muestra ancho y alto."),
    ],
    Z=[
        ("Una pieza dibujada en escala 1:10 mide 4 cm. Otra pieza real mide 35 cm. ¿Cuál es más larga?", "La primera", "La primera real mide 4 × 10 = 40 cm, más que 35 cm."),
        ("Una compañera hizo un boceto sin medidas de una caja. Otra persona debe construirla sin hablar con ella. ¿Qué le falta al dibujo?", "Las cotas", "Sin medidas, la persona debe adivinar el tamaño."),
    ],
    D=[
        arith("Una repisa real mide 90 cm de largo y se dibuja en escala 1:5. La hoja tiene 16 cm de ancho. ¿Cuántos centímetros se pasa el dibujo de la hoja?", "90//5-16", "El dibujo mide 18 cm y la hoja tiene 16 cm.", " cm"),
        ("Un banco real mide 60 cm de largo y 45 cm de ancho. Se dibuja en escala 1:5 en una hoja de 14 cm por 10 cm. ¿Cabe el dibujo?", "Sí", "El dibujo mide 12 cm por 9 cm, menor que la hoja."),
    ],
    ctx=("Quieres pedir a alguien de tu casa que arme un porta-cuadernos de cartón que mide 30 cm de ancho, 20 cm de fondo y 25 cm de alto. Escribe las medidas de cada vista y a qué medida quedaría el ancho si lo dibujas a escala 1:5.", "Frontal: 30 y 25. Superior: 30 y 20. Lateral: 20 y 25. Ancho en el dibujo: 6 cm", "Cada vista usa dos medidas y 30 ÷ 5 = 6."),
    sc=[
        ("¿Qué tipo de dibujo sirve para probar ideas rápido?", "El dibujo a mano alzada", "Se hace sin regla y se cambia fácil."),
        ("En escala 1:5, ¿el dibujo es más grande o más pequeño que el objeto?", "Más pequeño", "Cada 1 cm del dibujo vale 5 cm reales."),
        ("¿Para qué sirve guardar versiones de un dibujo en el computador?", "Para volver a una versión anterior si algo sale mal", "Evita perder el trabajo."),
    ],
    open_task=(
        "Escoge un objeto. Objeto 1: un soporte de celular de 10 cm de ancho, 8 cm de fondo y 12 cm de alto. Objeto 2: una repisa de 100 cm de largo, 20 cm de fondo y 25 cm de alto. Haz un boceto a mano alzada y un dibujo técnico con las tres vistas y las cotas. Para el objeto 2, usa escala 1:10 y escríbela.",
        "Objeto 1: tres vistas con cotas 10×12, 10×8 y 8×12. Boceto con flechas que indican el apoyo del celular",
        ["boceto a mano alzada", "tres vistas con cotas correctas", "escala escrita si corresponde", "medidas con unidad"],
        ["hoja con boceto y dibujo técnico"],
        ["mezclar las medidas de cada vista", "olvidar escribir la escala"],
        "Pregunta: «¿qué medida muestra esta vista?». Si no coincide, pídele revisar con el objeto de referencia.",
    ),
    reinforce="Dibuja a escala 1:5 el largo y el alto de la puerta de una pieza de tu casa, usando medidas aproximadas.",
    extend="Escribe cuándo usarías un programa de dibujo y cuándo un lápiz y papel para el mismo diseño, con una razón para cada uno.",
)

# ------------------------------------------------------------------ OA 01, clase 3
reg(
    OA1, 3,
    materials="Hoja, lápiz y los listados escritos en este cuaderno.",
    use="Aprenderé a calcular los materiales de un diseño y a prever los riesgos antes de empezar. Sirve para trabajar sin sorpresas y sin accidentes.",
    prior=["Sé leer medidas de un dibujo técnico.", "Sé sumar y multiplicar.", "Sé que una restricción es un límite."],
    explain=[
        "Antes de construir se planifican los recursos. Se escribe una lista de materiales con la cantidad de cada uno y las herramientas necesarias. La cantidad se calcula con el dibujo técnico: si el diseño lleva 4 patas de 30 cm, necesitas 4 × 30 = 120 cm de material para las patas, y conviene sumar un pequeño margen por si hay errores.",
        "También se revisan las restricciones: el tiempo, el dinero y los materiales que tienes. Si no alcanzan, se busca un material alternativo, por ejemplo cartón reutilizado en vez de cartón nuevo. Reutilizar ayuda a cuidar el ambiente porque se generan menos residuos.",
        "La seguridad se planifica antes. Para cada paso piensa qué riesgo hay y cómo evitarlo: tijeras de punta roma, superficie despejada, pelo recogido y lavado de manos al terminar. Las herramientas con filo o con motor las usa solo una persona adulta. Si un paso es riesgoso, se cambia por otro más seguro.",
    ],
    vocab=[("lista de materiales", "lista con materiales, cantidades y herramientas"), ("margen", "cantidad extra por si hay errores"), ("alternativo", "material que reemplaza a otro"), ("riesgo", "posibilidad de que ocurra un daño"), ("residuo", "material que se bota")],
    worked=[
        ("Calcular cantidad de material", "Una repisa lleva 3 tablas de cartón de 45 cm de largo cada una. ¿Cuántos centímetros de cartón se necesitan?", ["Son 3 piezas iguales.", "Multiplico 3 × 45."], "135 cm"),
        ("Detectar un riesgo y su solución", "Para cortar tiras de cartón grueso, Valentina piensa usar un cortador con filo. ¿Qué haces?", ["El cortador tiene filo y es riesgoso para su edad.", "Se cambia el paso: usa tijeras de punta roma con cartón delgado, o pide que una persona adulta corte."], "Cambiar el paso por tijeras de punta roma o pedir a una persona adulta que corte"),
    ],
    mistakes=[
        ("Empezar a cortar sin calcular cuánto material se necesita.", "Puede faltar material o sobrar mucho.", "Calcula las cantidades con el dibujo técnico antes de cortar."),
        ("Pensar que la seguridad se revisa solo si alguien se lastima.", "Los riesgos se previenen antes de empezar.", "Escribe el riesgo de cada paso y cómo evitarlo."),
    ],
    R=[
        ("¿Quién usa las herramientas con filo o con motor?", "Una persona adulta", "Son riesgosas para estudiantes de esta edad."),
        arith("Un diseño lleva 5 piezas de 10 cm cada una. ¿Cuántos centímetros de material suman?", "5*10", "Se multiplica el número de piezas por su largo.", " cm"),
        ("Reutilizar cartón en vez de comprar cartón nuevo, ¿ayuda o perjudica al ambiente?", "Ayuda", "Se generan menos residuos."),
    ],
    C=[
        ("¿Para qué sirve el margen de material?", "Para tener extra si ocurre un error", "Evita quedarse sin material."),
        ("¿Qué tijeras usas para cortar cartón delgado de forma segura? A de punta roma, B de punta afilada.", "A", "La punta roma reduce el riesgo de pinchazos."),
        ("Falta un frasco de pegamento. ¿Cuál es un recurso alternativo? A cinta adhesiva, B más cartón.", "A", "La cinta también une piezas de papel y cartón."),
    ],
    A=[
        arith("Un diseño lleva 4 patas de 30 cm cada una. ¿Cuántos centímetros de material se necesitan para las patas?", "4*30", "Se multiplica el número de patas por el largo de cada una.", " cm"),
        arith("Un tablero lleva 6 tiras de cartón de 25 cm. Se agrega un margen de 10 cm en total. ¿Cuántos centímetros de cartón se piden?", "6*25+10", "Se calcula el total de las tiras y se suma el margen.", " cm"),
        ("Un paso dice «perforar cartón grueso con un clavo». ¿Es seguro para un estudiante de 6.º? ¿Cómo lo cambias?", "No; pide que una persona adulta perfore o usa cordel y marcas", "El clavo puede pinchar y no es herramienta de estudiantes."),
    ],
    Z=[
        ("Un grupo calcula 150 cm de cartón y tiene una caja con 140 cm reutilizables. ¿Alcanza?", "No", "Faltan 10 cm; se necesita otro recurso o cambiar el diseño."),
        ("Mateo dice: «Mejor no anotar los riesgos porque se me pasa el tiempo». ¿Tiene razón?", "No", "Prevenir riesgos evita accidentes que hacen perder más tiempo."),
    ],
    D=[
        arith("El diseño necesita 8 tiras de 15 cm y 2 tiras de 40 cm. ¿Cuántos centímetros de cartón se necesitan en total?", "8*15+2*40", "Se calcula cada grupo de tiras y se suman.", " cm"),
        ("Lista de riesgos: A tijeras con la punta hacia abajo al caminar, B mesa con papeles y cordeles en el suelo. ¿Cuál es el riesgo de tropiezo?", "B", "El cordel en el suelo hace tropezar."),
    ],
    ctx=("Vas a armar un portalápices de cartón con 4 paredes de 12 cm de ancho y 10 cm de alto. Escribe cuántas paredes necesitas, cuántos centímetros de ancho suman y un riesgo con su forma de evitarlo.", "4 paredes; suman 48 cm de ancho; riesgo: pincharse con la tijera, se evita usando tijera de punta roma", "Se multiplica 4 × 12 = 48 y se nombra un riesgo con su prevención."),
    sc=[
        ("¿Qué incluye una lista de materiales?", "Materiales, cantidades y herramientas", "Sirve para preparar todo antes de empezar."),
        ("¿Cuándo se piensan los riesgos?", "Antes de empezar", "Así se previenen accidentes."),
        ("¿Qué haces si un material no alcanza?", "Busco un material alternativo o ajusto el diseño", "Se resuelve sin parar el proyecto."),
    ],
    open_task=(
        "Escoge un diseño. Diseño 1: una caja para 6 lápices con 5 caras de cartón de 10 cm por 10 cm. Diseño 2: un soporte con 3 tiras de 20 cm y 2 tiras de 12 cm. Escribe la lista de materiales con cantidades, un material alternativo y dos riesgos con su forma de evitarlos.",
        "Diseño 2: 3 × 20 + 2 × 12 = 84 cm de tiras. Alternativa: cartón reutilizado. Riesgos: pinchazo (tijeras de punta roma) y tropiezo (mesa despejada)",
        ["lista con cantidades calculadas", "un material alternativo", "dos riesgos con prevención", "herramientas seguras"],
        ["hoja con lista de materiales y riesgos"],
        ["no calcular las cantidades", "no pensar en riesgos"],
        "Pregunta: «¿qué pasa si este material no alcanza?». Si no tiene respuesta, pídele agregar una alternativa.",
    ),
    reinforce="Haz una lista de lo que necesitas para decorar el borde de una hoja con papeles de colores, con cantidades y un riesgo.",
    extend="Elige un objeto de tu casa y estima cuántos materiales de cartón necesitarías para hacer una versión pequeña.",
)

# ------------------------------------------------------------------ OA 01, clase 4
reg(
    OA1, 4,
    materials="Hoja, lápiz y los datos escritos en este cuaderno. Si quieres practicar, cartón, regla y tijeras de punta roma con una persona de tu casa cerca.",
    use="Aprenderé a elaborar o armar un prototipo siguiendo el plano, a respetar medidas y a llevar un registro de lo que hago. Sirve para que el resultado se parezca al diseño.",
    prior=["Sé leer cotas.", "Sé que una lista de materiales tiene cantidades.", "Sé que hay herramientas seguras e inseguras."],
    explain=[
        "Elaborar es construir un prototipo, que es una primera versión del objeto para probarla. Se sigue el plano paso a paso: medir, marcar, cortar, unir y revisar. Una regla útil es «medir dos veces, cortar una vez», porque un corte equivocado no se puede arreglar.",
        "Ninguna pieza queda exacta. La tolerancia es la diferencia pequeña que se acepta sin que el diseño falle. Por ejemplo, una pieza de 150 mm con tolerancia de 2 mm puede medir entre 148 mm y 152 mm. Recuerda que 1 cm son 10 mm. Si la pieza se sale de la tolerancia, se rehace.",
        "Mientras construyes, lleva un registro: anota cada paso, el material usado, el tiempo y los cambios que hiciste al plano. Si cambias algo, anota por qué. Este registro, llamado bitácora, te sirve después para probar y mejorar, y para explicar tu trabajo a otras personas.",
    ],
    vocab=[("prototipo", "primera versión de un objeto para probarla"), ("tolerancia", "diferencia pequeña que se acepta en una medida"), ("bitácora", "registro de los pasos y cambios del trabajo"), ("milímetro", "unidad de longitud; 10 mm equivalen a 1 cm"), ("ensamblar", "unir las piezas de un objeto")],
    worked=[
        ("Revisar una tolerancia", "Una pieza debe medir 150 mm con tolerancia de 2 mm. Tu pieza mide 153 mm. ¿Sirve?", ["El rango aceptado va de 148 mm a 152 mm.", "153 mm está fuera del rango."], "No sirve; se rehace porque pasa de 152 mm"),
        ("Registrar un cambio", "Al armar, una tira de 20 cm quedó 1 cm corta. Escribe cómo registras el cambio en la bitácora.", ["Anoto la pieza y el problema.", "Anoto la solución y el motivo."], "Tira de 20 cm quedó corta por 1 cm; se cortó otra tira y se anotó por qué"),
    ],
    mistakes=[
        ("Cortar sin volver a medir.", "Un corte equivocado no se puede arreglar.", "Mide dos veces y corta una."),
        ("Cambiar el plano y no anotarlo.", "Después nadie sabe por qué el objeto no coincide con el dibujo.", "Anota cada cambio en la bitácora con su motivo."),
    ],
    R=[
        ("¿Cómo se llama la primera versión de un objeto que se hace para probarlo?", "Prototipo", "Se construye para probar y mejorar."),
        ("En Tecnología: ¿Cuántos milímetros hay en 1 cm?", "10", "1 cm equivale a 10 mm."),
        ("¿Dónde se anotan los pasos y los cambios del trabajo?", "En la bitácora", "Es el registro del trabajo."),
    ],
    C=[
        ("¿Qué significa «medir dos veces, cortar una»?", "Verificar la medida antes de cortar", "Así se evitan errores sin arreglo."),
        ("¿Para qué sirve la tolerancia?", "Para saber cuánta diferencia se acepta en una medida", "Ninguna pieza queda exacta."),
        ("¿Por qué anotar los cambios en la bitácora?", "Para saber qué se cambió y por qué", "Sirve para probar y mejorar después."),
    ],
    A=[
        arith("Una pieza debe medir 150 mm con tolerancia de 2 mm. ¿Cuál es la medida mínima aceptada, en mm?", "150-2", "Se resta la tolerancia a la medida pedida.", " mm"),
        arith("Una pieza debe medir 8 cm. ¿Cuántos milímetros son?", "8*10", "Cada centímetro tiene 10 mm.", " mm"),
        ("Una pieza pedida de 90 mm con tolerancia de 2 mm mide 93 mm. ¿Se acepta?", "No", "El máximo aceptado es 92 mm."),
    ],
    Z=[
        ("Un grupo pegó las paredes y recién después notó que una medía 6 mm de más, con tolerancia de 2 mm. ¿Qué debieron hacer antes de pegar?", "Medir cada pieza antes de unirla", "Revisar antes de unir evita rehacer todo."),
        ("Ana cambió el largo de una pieza de 20 cm a 24 cm y no lo anotó. ¿Qué problema puede causar?", "Que no se sepa por qué el objeto difiere del plano", "Sin registro, nadie entiende el cambio."),
    ],
    D=[
        arith("La caja necesita 4 listones de 15 cm. Cada corte deja 1 cm de recorte sobrante que ya no se puede usar. ¿Cuántos centímetros de material se gastan en total, contando los 4 recortes?", "4*15+4*1", "Cada listón gasta 15 cm y cada corte deja 1 cm de recorte.", " cm"),
        ("Tres piezas miden 148 mm, 150 mm y 153 mm; deben medir 150 mm con tolerancia de 2 mm. ¿Cuántas cumplen?", "2", "Cumplen 148 y 150; 153 se pasa de 152."),
    ],
    ctx=("Estás armando un portalápices y la pieza del fondo debía medir 100 mm con tolerancia de 2 mm. Mides y obtienes 105 mm. Escribe si sirve, qué haces y cómo lo anotas en la bitácora.", "No sirve; pasa de 102 mm. La rehago con el cartón sobrante. Bitácora: fondo de 105 mm fuera de tolerancia; se corta otra pieza", "Compara con el máximo de 102 mm, rehace la pieza y anota."),
    sc=[
        ("En Tecnología: ¿Qué es un prototipo?", "Una primera versión para probar", "Se usa para probar y mejorar."),
        ("¿Qué pasa si una pieza queda fuera de tolerancia?", "Se rehace", "No cumple el plano."),
        ("¿Qué se escribe en la bitácora?", "Pasos, materiales, tiempos y cambios", "Es el registro del trabajo."),
    ],
    open_task=(
        "Escoge una pieza. Pieza 1: una pared de 120 mm de alto con tolerancia de 2 mm. Pieza 2: una base de 18 cm de lado con tolerancia de 2 mm. Escribe el rango aceptado de medidas (en mm), cuántas piezas cortarás, cómo vas a medir antes de cortar y una entrada de bitácora para un posible error.",
        "Pieza 1: 118 mm a 122 mm. Una pieza. Mido dos veces con regla. Bitácora: «La pared midió 124 mm; se rehizo»",
        ["rango de medidas correcto", "indica cuántas piezas corta", "explica cómo mide antes de cortar", "entrada de bitácora con problema y solución"],
        ["hoja con rango y entrada de bitácora"],
        ["no revisar la tolerancia", "cambiar el plano sin anotarlo"],
        "Pregunta: «¿qué pasa si la pieza mide un poco más?». Si no conoce la tolerancia, repasa el rango.",
    ),
    reinforce="Mide con una regla el largo de tu cuaderno en cm y conviértelo a mm.",
    extend="Anota en una bitácora de tres líneas cómo armarías una caja de papel sin pegamento, qué pieza podría fallar y por qué.",
)

# ------------------------------------------------------------------ OA 01, clase 5
reg(
    OA1, 5,
    materials="Hoja, lápiz y los datos escritos en este cuaderno.",
    use="Aprenderé a probar un diseño con varias pruebas iguales, a registrar los resultados y a decidir si cumple los criterios. Sirve para decidir con datos y no por apariencia.",
    prior=["Sé registrar datos en una tabla.", "Sé qué es un criterio.", "Sé que una prueba debe repetirse varias veces."],
    explain=[
        "Probar es comprobar si el prototipo cumple los criterios. Una prueba justa se repite igual cada vez: mismo lugar, mismo material y mismo modo de medir. Si en cada intento cambias algo, no sabrás qué causó el resultado. Por eso se cambia una sola variable a la vez.",
        "Se hacen al menos tres pruebas y se anotan en una tabla. Con los tres resultados se calcula el promedio: se suman y se divide entre 3. Si un resultado es muy distinto a los otros, se revisa qué pasó. El promedio y los datos sirven como evidencia, es decir, pruebas que apoyan tu decisión.",
        "Luego se compara el resultado con el criterio. Si el criterio dice «sostiene al menos 9 fichas» y las pruebas dan 9, 9 y 9, el diseño cumple. Si da 9, 5 y 9, no es confiable. Tu conclusión debe decir qué criterio cumple, cuál no cumple y qué dato lo muestra.",
    ],
    vocab=[("prueba justa", "prueba repetida igual cada vez, cambiando solo una variable"), ("variable", "lo que se puede cambiar en una prueba"), ("promedio", "suma de los datos dividida por la cantidad de datos"), ("evidencia", "datos que apoyan una decisión"), ("conclusión", "decisión final basada en los datos")],
    worked=[
        ("Calcular un promedio", "Tres pruebas de resistencia dan 12, 15 y 15 fichas. ¿Cuál es el promedio?", ["Sumo: 12 + 15 + 15 = 42.", "Divido entre 3."], "14 fichas"),
        ("Decidir si cumple", "Criterio: sostiene al menos 10 fichas en cada prueba. Resultados: 11, 10 y 8. ¿Cumple?", ["Reviso cada prueba contra 10.", "La tercera, 8, no llega a 10."], "No cumple, porque en la tercera prueba sostuvo 8 fichas"),
    ],
    mistakes=[
        ("Cambiar el material y la base a la vez entre pruebas.", "No se sabe cuál cambio produjo el resultado.", "Cambia una sola variable por prueba."),
        ("Decir «funciona» tras una sola prueba.", "Una prueba puede salir bien por casualidad.", "Haz al menos tres pruebas iguales."),
    ],
    R=[
        ("¿Cuántas pruebas se hacen como mínimo en esta clase?", "Tres", "Con tres datos se calcula un promedio."),
        ("¿Una prueba justa cambia una sola variable o varias?", "Una sola", "Así se sabe qué causó el resultado."),
        ("Resultados de 6, 6 y 6 fichas, ¿son parecidos o muy distintos?", "Parecidos", "Los tres números son iguales."),
    ],
    C=[
        ("¿Qué es la evidencia en una prueba?", "Los datos que apoyan la decisión", "Permiten comprobar la conclusión."),
        ("Un diseño sostuvo 8, 8 y 3 fichas. ¿Qué haces con el 3?", "Revisar qué pasó en esa prueba", "Un dato muy distinto indica un posible error."),
        ("¿Por qué repetir la prueba siempre igual?", "Para poder comparar los resultados", "Si cambia algo, no se compara."),
    ],
    A=[
        arith("Tres pruebas dieron 9, 12 y 12 fichas. ¿Cuál es el promedio?", "(9+12+12)//3", "Se suman los datos y se divide entre 3.", " fichas"),
        arith("El criterio pide 15 fichas. El prototipo sostiene 11. ¿Cuántas fichas le faltan?", "15-11", "Se resta lo que sostiene de lo que se pide.", " fichas"),
        ("Criterio: «sostiene al menos 7 fichas». Resultados: 7, 8 y 7. ¿Cumple?", "Sí", "Las tres pruebas llegan a 7 o más."),
    ],
    Z=[
        ("Lía probó con una base de papel y luego con una de cartón y cambió también la mesa. ¿Puede saber qué causó la diferencia?", "No", "Cambió más de una variable."),
        ("Un grupo dice: «sostuvo 10 fichas en una prueba, entonces el diseño cumple». ¿Qué le falta?", "Repetir la prueba al menos tres veces", "Una sola prueba no es evidencia suficiente."),
    ],
    D=[
        arith("Cuatro pruebas dan 8, 10, 12 y 14 fichas. ¿Cuál es el promedio?", "(8+10+12+14)//4", "Se suman los cuatro datos y se divide entre 4.", " fichas"),
        ("Diseño A: 9, 9 y 9 fichas. Diseño B: 12, 12 y 3 fichas. Criterio: sostiene al menos 9 fichas en todas las pruebas. ¿Cuál cumple?", "El diseño A", "B falla en la tercera prueba."),
    ],
    ctx=("Pruebas un puente de papel: soporta 120 g, 120 g y 90 g en tres intentos. El criterio es «soporta al menos 100 g». Calcula el promedio, di si cumple y qué dato lo muestra.", "Promedio: 110 g. No cumple en todas porque una prueba soportó 90 g", "Se calcula (120 + 120 + 90) ÷ 3 y se revisa cada prueba."),
    sc=[
        ("¿Cuántas variables cambias entre una prueba y otra?", "Una", "Así sabes qué causó el cambio."),
        ("¿Cómo se calcula un promedio de tres datos?", "Se suman y se divide entre 3", "Es la definición del promedio."),
        ("¿Qué debe decir la conclusión?", "Qué criterio cumple, cuál no y con qué dato", "Debe apoyarse en evidencia."),
    ],
    open_task=(
        "Escoge un registro. Registro 1: un soporte sostuvo 8, 8 y 5 fichas; el criterio es «al menos 8 fichas». Registro 2: un puente de papel soportó 90 g, 100 g y 110 g; el criterio es «al menos 100 g». Calcula el promedio, di si cumple en todas las pruebas y escribe una conclusión con datos y una variable que cambiarías.",
        "Registro 2: promedio 100 g. No cumple en todas: una prueba dio 90 g. Cambiaría el grosor del papel",
        ["calcula bien el promedio", "revisa cada prueba contra el criterio", "conclusión con datos", "propone cambiar una sola variable"],
        ["hoja con promedio, decisión y conclusión"],
        ["concluir con una sola prueba", "cambiar varias variables a la vez"],
        "Pregunta: «¿qué dato muestra que cumple o no cumple?». Si no cita un número, pídele volver a la tabla.",
    ),
    reinforce="Repite tres veces cuántas hojas de papel sostiene un vaso plástico al ponerlas con cuidado encima, anota los datos y calcula el promedio.",
    extend="Explica con tus palabras por qué una sola prueba no es suficiente para afirmar que un diseño cumple.",
)

# ------------------------------------------------------------------ OA 01, clase 6
reg(
    OA1, 6,
    materials="Hoja, lápiz y los datos escritos en este cuaderno. Si tienes computador, un programa de presentaciones para la ficha final.",
    use="Aprenderé a mejorar un diseño con evidencia, a innovar y a comunicarlo con una ficha de diseño. Sirve para que otras personas entiendan qué problema resolviste.",
    prior=["Sé hacer pruebas con datos y promedios.", "Sé que una mejora cambia una sola variable.", "Sé que las fuentes se anotan."],
    explain=[
        "Mejorar un diseño es cambiar algo para cumplir mejor un criterio. Mira qué criterio falló, elige una sola variable que pueda explicarlo, cámbiala y repite las pruebas. Si los datos mejoran, la mejora se queda. Si no, vuelves al diseño anterior y pruebas otra variable.",
        "Innovar es dar un paso más: no solo arreglar la falla, sino agregar un aporte nuevo, como un uso adicional o un material reutilizado. Una innovación también se prueba con datos. La ficha de diseño tiene seis partes: necesidad con usuario, criterios, dibujo con medidas, registro de pruebas, mejora hecha y lo aprendido.",
        "Al presentar, muestra números y no solo opiniones, y escucha las preguntas de las demás personas. Si usas una imagen, un dato o una idea que no es tuya, anota la fuente. Un diseño nunca está terminado: siempre se puede probar otra mejora.",
    ],
    vocab=[("mejora", "cambio que hace que el diseño cumpla mejor un criterio"), ("innovación", "aporte nuevo que se agrega a un producto"), ("ficha de diseño", "hoja que resume necesidad, dibujo, pruebas y mejora"), ("fuente", "origen de una imagen, dato o idea"), ("comunicar", "mostrar tu trabajo para que otras personas lo entiendan")],
    worked=[
        ("Decidir una mejora con datos", "Un portalápices debía soportar 12 lápices y soportó 12, 7 y 12. Falló cuando se movió la mesa. ¿Qué mejora pruebas primero?", ["La falla ocurrió al mover la mesa: parece un problema de estabilidad.", "Cambio una sola variable: pego una base más ancha y repito las tres pruebas."], "Una base más ancha y repetir las tres pruebas"),
        ("Ordenar la ficha", "Ordena las partes: mejora hecha, necesidad y usuario, registro de pruebas, criterios, lo aprendido y dibujo con medidas.", ["Primero el problema: necesidad con usuario y luego criterios.", "Después el dibujo, el registro de pruebas, la mejora y lo aprendido."], "Necesidad y usuario, criterios, dibujo con medidas, registro de pruebas, mejora y lo aprendido"),
    ],
    mistakes=[
        ("Decir «quedó mejor» sin mostrar datos.", "No hay forma de comprobarlo.", "Muestra el número antes y el número después."),
        ("Usar una imagen de otra persona sin decir de dónde viene.", "No se reconoce el trabajo ajeno.", "Anota la fuente de toda imagen o dato que no sea tuyo."),
    ],
    R=[
        ("¿Cuántas partes tiene la ficha de diseño?", "Seis", "Son necesidad, criterios, dibujo, pruebas, mejora y lo aprendido."),
        ("Si los datos no mejoran tras el cambio, ¿qué haces?", "Vuelvo al diseño anterior y pruebo otra variable", "Una mejora debe mostrar datos mejores."),
        ("Si usas una imagen que no es tuya, ¿qué anotas?", "La fuente", "Así se reconoce de dónde viene."),
    ],
    C=[
        ("¿Por qué una ficha debe mostrar números y no solo opiniones?", "Porque los números permiten comprobar la mejora", "Una opinión no se puede verificar."),
        ("¿En qué se diferencia innovar de arreglar una falla?", "Innovar agrega un aporte nuevo", "Arreglar solo corrige lo que falla."),
        ("Una compañera sugiere agrandar la base. ¿Qué haces con su idea?", "La anoto y digo quién la dio", "Se registra y se reconoce a la persona."),
    ],
    A=[
        arith("Antes de la mejora el portalápices soportaba 6 lápices; después soporta 15. ¿Cuántos lápices más soporta?", "15-6", "Se resta lo de antes de lo de después.", " lápices"),
        ("Elige el mejor registro de mejora. A «Quedó más lindo», B «Con base de 14 cm soportó 15 lápices en las tres pruebas».", "B", "B tiene datos que se pueden comprobar."),
        ("Una ficha tiene necesidad, criterios, dibujo, registro y mejora. ¿Qué parte le falta?", "Lo que aprendiste", "Son seis partes y falta la última."),
    ],
    Z=[
        ("Grupo 1: «lo hicimos más grande». Grupo 2: «subimos de 6 a 11 lápices al ensanchar la base 4 cm». ¿Cuál comunica mejor la mejora?", "El grupo 2", "Da el cambio y el resultado con números."),
        ("Una mejora aumentó la capacidad, pero rompió el límite de base de 20 cm que pedía el problema. ¿Se acepta?", "No", "Pasa una restricción del problema."),
    ],
    D=[
        arith("Un grupo mejora 3 lápices por cada cambio. Parte de 6 y hace 3 mejoras seguidas. ¿Cuántos lápices soporta al final?", "6+3+3+3", "Se suman las tres mejoras a lo que ya soportaba.", " lápices"),
        ("Una ficha usa la fotografía de un puente de un sitio de internet, pero no dice de dónde es. ¿Qué falta?", "La fuente de la imagen", "Toda imagen ajena debe indicar su origen."),
    ],
    ctx=("Tu soporte de cartón para 9 fichas sostuvo 9, 5 y 9 en tres pruebas. Cambiaste solo el alto de las paredes de 8 cm a 5 cm y ahora sostiene 9, 9 y 9. Escribe la mejora, el dato de antes y de después y lo que aprendiste.", "Mejora: paredes de 8 a 5 cm. Antes: falló en la prueba 2. Después: 9, 9 y 9. Aprendí que paredes más bajas dan más estabilidad", "Une cambio, datos y aprendizaje."),
    sc=[
        ("¿Qué muestra que una mejora funcionó?", "Datos mejores que los de antes", "La evidencia permite comprobarlo."),
        ("¿Qué haces con las ideas de otras personas?", "Las anoto y digo quién las dio", "Se reconoce el aporte."),
        ("¿Un diseño puede mejorar más después de terminarlo?", "Sí", "Siempre se puede probar otra mejora."),
    ],
    open_task=(
        "Escoge un diseño. Diseño 1: soporte de cartón para 9 fichas que sostuvo 9, 5 y 9. Diseño 2: un portalápices de cartón que se vuelca con 6 lápices en 2 de 3 pruebas. Escribe la mejora que probarías, qué variable cambias, qué dato mostraría que mejoró, una innovación y arma la ficha con las seis partes.",
        "Diseño 2: mejora: base más ancha. Variable: ancho de la base. Dato: no se vuelca en 3 de 3 pruebas. Innovación: un compartimento para borradores. Ficha completa",
        ["dice la mejora y la variable", "indica el dato que mostraría la mejora", "propone una innovación", "ficha con las seis partes y fuentes"],
        ["ficha de diseño completa"],
        ["mejorar sin datos", "dejar partes de la ficha en blanco"],
        "Pregunta: «¿qué número muestra que mejoró?». Si no tiene, pídele volver a las pruebas.",
    ),
    reinforce="Cuéntale a una persona de tu casa qué problema resolvió tu diseño y qué mejora hiciste, mostrando un número.",
    extend="Escribe dos preguntas que harías al ver el diseño de otra persona para entender cómo lo mejoró.",
)
