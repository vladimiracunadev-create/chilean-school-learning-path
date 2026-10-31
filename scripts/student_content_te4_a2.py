"""Cuaderno del estudiante, 4.º básico Tecnología: OA 02 (planificar la elaboración de un objeto), clases 1 a 5, y OA 03 (elaborar con dominio técnico), clases 1 a 5.

Seguridad: papel, cartón, cinta, cordel, témpera y tijeras de punta roma. Perforar con perforador de papel y serrar madera solo con una persona adulta;
los cuadernos describen las técnicas, pero nunca piden usar cortadores, fuego, vidrio ni herramientas con filo. Medidas enteras en centímetros.
"""
from __future__ import annotations

from student_content_te4_a import reg
from student_lessons import arith

OA2, OA3 = "TE04 OA 02", "TE04 OA 03"

# ------------------------------------------------------------------ OA 02, clase 1
reg(
    OA2, 1,
    materials="Hoja y lápiz. Las tareas y los datos están escritos en este cuaderno.",
    use="Aprenderé a dividir el resultado que quiero lograr en tareas ordenadas. Sirve para saber qué hacer primero y qué hacer después.",
    prior=["Sé ordenar pasos en una secuencia.", "Sé que un diseño tiene criterios que se pueden comprobar."],
    explain=[
        "Planificar es decidir de antemano qué hacer, en qué orden y con qué. Para planificar la elaboración de un objeto, primero escribes el resultado deseado: cómo debe quedar el objeto terminado. Después lo descompones en tareas pequeñas. Una tarea es una acción que se puede hacer y comprobar, como «medir la base» o «pegar las dos paredes».",
        "Una buena tarea empieza con un verbo, es corta y dice qué queda hecho. «Caja» no es una tarea. «Marcar los 4 lados de 10 cm» sí lo es. Si una tarea tiene muchas acciones juntas, se divide en dos. Ninguna tarea debería ser tan grande que no sepas por dónde empezar.",
        "La lista de tareas es la secuencia de acciones. Se anota con números para ver el orden. Antes de construir, revisa que no falte nada: si el resultado necesita una tapa, debe haber una tarea para la tapa. Una lista completa te permite trabajar sin detenerte y repartir el trabajo si lo haces en equipo.",
    ],
    vocab=[("planificar", "decidir de antemano qué hacer, en qué orden y con qué"), ("resultado deseado", "cómo debe quedar el objeto terminado"), ("tarea", "acción pequeña que se puede hacer y comprobar"), ("secuencia", "lista de acciones en orden"), ("descomponer", "dividir algo grande en partes pequeñas")],
    worked=[
        ("Descomponer en tareas", "Resultado deseado: una caja de cartón sin tapa, de 10 cm de lado, para guardar lápices. Escribe tres tareas.", ["Cada tarea empieza con un verbo.", "Primero se mide y marca, luego se cortan las piezas, luego se unen.", "Escribo tareas cortas."], "1. Marcar las piezas de 10 cm. 2. Cortar las piezas. 3. Unir las piezas con cinta"),
        ("Dividir una tarea grande", "La tarea «Hacer la caja» es muy grande. ¿Por qué no sirve y qué puedes hacer?", ["No dice qué acciones incluye.", "Tiene muchas acciones juntas.", "La divido en tareas que se puedan comprobar."], "Se divide en tareas más pequeñas: medir, cortar y unir"),
    ],
    mistakes=[
        ("Escribir tareas sin verbo, como «caja» o «tapa».", "No dicen qué acción hay que hacer.", "Empieza con un verbo: «marcar», «cortar», «pegar»."),
        ("Olvidar una parte del objeto en la lista.", "El objeto quedará incompleto.", "Compara tu lista con el resultado deseado antes de construir."),
    ],
    R=[
        ("«Cortar las piezas de cartón» ¿es una tarea o un resultado?", "Una tarea", "Es una acción que se puede hacer y comprobar."),
        ("Una lista de acciones ordenadas se llama...", "Secuencia", "Es el nombre de una lista de acciones en orden."),
        ("Para planificar, ¿se escribe primero el resultado deseado o las tareas?", "El resultado deseado", "Sin saber cómo debe quedar no se pueden definir las tareas."),
    ],
    C=[
        ("¿Por qué «Hacer la caja» no es una buena tarea?", "Porque tiene muchas acciones juntas", "Se debe dividir en acciones pequeñas."),
        ("¿Con qué tipo de palabra empieza una buena tarea?", "Con un verbo", "Dice la acción que se debe hacer."),
        ("¿Para qué sirve numerar la lista de tareas?", "Para ver el orden", "Los números muestran qué va primero."),
    ],
    A=[
        ("Resultado deseado: un lapicero de cartón con una base y un tubo. Escribe tres tareas que empiecen con verbo.", "Cortar la base; enrollar el tubo; pegar el tubo a la base", "Cubre las tres partes del objeto."),
        arith("Un objeto necesita 6 tareas. Ya hiciste 2. ¿Cuántas tareas faltan?", "6-2", "Se restan las hechas del total."),
        ("Tu lista tiene: 1. Medir, 2. Cortar, 3. Pegar. El resultado deseado incluye una tapa. ¿Qué falta?", "Una tarea para la tapa", "Todo lo que lleva el resultado debe tener su tarea."),
    ],
    Z=[
        ("Dos listas para una caja: A «1. Pegar, 2. Cortar, 3. Medir», B «1. Medir, 2. Cortar, 3. Pegar». ¿Cuál tiene un orden que funciona?", "B", "Se mide antes de cortar y se corta antes de pegar."),
        ("Una compañera dice: «No necesito lista, lo hago de memoria». ¿Qué problema puede ocurrir?", "Olvidar una tarea o repetirla", "La lista evita olvidos y ordena el trabajo en equipo."),
    ],
    D=[
        arith("Un plan lleva 3 tareas para la base, 2 para las paredes y 1 para la tapa. ¿Cuántas tareas hay en total?", "3+2+1", "Se suman las tareas de las tres partes."),
        ("Resultado deseado: un porta-lápices de cartón con 3 compartimientos. Divide «armar los compartimientos» en dos tareas.", "Cortar las divisiones; pegar las divisiones dentro de la caja", "Se separan cortar y pegar, que son acciones distintas."),
    ],
    ctx=("Resultado deseado: un soporte de cartón que sostenga 10 fichas, con una base de 20 cm de largo y una pared de 10 cm de alto. Escribe una secuencia de cuatro tareas con verbo.", "1. Marcar la base de 20 cm. 2. Cortar la base y la pared de 10 cm. 3. Unir la pared a la base con cinta. 4. Probar con 10 fichas", "Cuatro tareas ordenadas que empiezan con verbo."),
    sc=[
        ("¿Qué es una tarea?", "Una acción pequeña que se puede hacer y comprobar", "Es la parte de una secuencia."),
        ("¿Qué es descomponer un resultado?", "Dividirlo en tareas pequeñas", "Así es más fácil planificar."),
        ("¿Qué se revisa antes de construir?", "Que no falte ninguna parte", "Cada parte del resultado necesita su tarea."),
    ],
    open_task=(
        "Escoge un resultado deseado. Resultado 1: una caja de papel de 10 cm de lado para guardar clips. Resultado 2: un atril de cartón para sostener 3 hojas. Escribe una secuencia de cinco tareas numeradas, cada una con verbo, y marca cuál puede hacer cada integrante si trabajan dos personas.",
        "Resultado 1: 1. Marcar el cuadrado de 30 cm. 2. Doblar los lados. 3. Pegar las esquinas. 4. Revisar que quede de 10 cm. 5. Probar con 5 clips. Persona A hace las tareas 1 y 2; persona B hace la 3; las dos hacen la 4 y la 5.",
        ["cinco tareas numeradas", "cada una empieza con verbo", "orden que funciona", "no falta ninguna parte del resultado"],
        ["secuencia numerada de cinco tareas"],
        ["tareas sin verbo", "orden que no funciona"],
        "Pregunta: «¿qué queda hecho cuando terminas esta tarea?». Si no se sabe, divide o reescribe la tarea.",
    ),
    reinforce="Escribe en cinco tareas con verbo cómo preparas una colación en tu casa.",
    extend="Elige un objeto de tu sala y escribe las tareas que habría que hacer para construirlo desde cero.",
)

# ------------------------------------------------------------------ OA 02, clase 2
reg(
    OA2, 2,
    materials="Hoja y lápiz. Las listas de materiales y herramientas están escritas en el cuaderno.",
    use="Aprenderé a relacionar cada tarea con los materiales, herramientas, técnicas y medidas de seguridad que necesita, y a pensar en el ambiente. Sirve para no empezar sin lo necesario.",
    prior=["Sé escribir una secuencia de tareas.", "Sé que algunos materiales se pueden reutilizar."],
    explain=[
        "Para cada tarea hay que decidir con qué se hace. El material es lo que se transforma: cartón, papel, cordel. La herramienta es lo que se usa para trabajar: regla, tijeras de punta roma, pegamento. La técnica es la manera de hacer la acción: medir, marcar, cortar, plegar, unir, pegar. Una tarea completa dice las tres cosas.",
        "También se anota la medida de seguridad de cada tarea. Al cortar, se usan tijeras de punta roma, se cortan lejos del cuerpo y se trabaja sentado. Al pegar con pegamento, se cubre la mesa y se lavan las manos al terminar. Si una tarea necesita una herramienta peligrosa, la hace una persona adulta.",
        "Por último, se piensa en el ambiente. Un recurso es un material que se usa para construir. Usar cartón reutilizado gasta menos recursos que cartón nuevo. Conviene usar solo lo necesario, guardar los retazos para otro trabajo y separar lo que se bota para reciclar. Eso es discutir las implicancias ambientales.",
    ],
    vocab=[("material", "lo que se transforma al construir"), ("herramienta", "objeto que se usa para trabajar el material"), ("técnica", "manera de realizar una acción"), ("medida de seguridad", "cuidado que evita accidentes"), ("recurso", "material que se usa para construir")],
    worked=[
        ("Completar una tarea con material, herramienta, técnica y seguridad", "Tarea: «Cortar la pared de cartón de 10 cm». Escribe material, herramienta, técnica y seguridad.", ["Material: cartón reutilizado.", "Herramienta: tijeras de punta roma. Técnica: cortar.", "Seguridad: cortar lejos del cuerpo y sentado."], "Cartón reutilizado, tijeras de punta roma, cortar, lejos del cuerpo y sentado"),
        ("Decidir pensando en el ambiente", "Puedes hacer un lapicero con un tubo de cartón que ibas a botar o con cartón nuevo. ¿Cuál gasta menos recursos?", ["El tubo ya existe y se iba a botar.", "El cartón nuevo gasta más recursos."], "El tubo reutilizado"),
    ],
    mistakes=[
        ("Usar una herramienta distinta de la que corresponde a la tarea.", "Puede dañar el material o causar un accidente.", "Relaciona la tarea con la herramienta y la técnica adecuadas."),
        ("Pensar que lo que se bota no importa.", "Se pierde material que se podría reutilizar o reciclar.", "Guarda los retazos y separa lo que se recicla."),
    ],
    R=[
        ("Las tijeras de punta roma, ¿son un material o una herramienta?", "Una herramienta", "Se usan para trabajar el material."),
        ("«Plegar» y «cortar», ¿son técnicas o materiales?", "Técnicas", "Son maneras de hacer una acción."),
        ("El cartón, ¿es un material o una herramienta?", "Un material", "Es lo que se transforma."),
    ],
    C=[
        ("¿Por qué conviene usar cartón reutilizado?", "Porque gasta menos recursos", "No se fabrica ni se compra cartón nuevo."),
        ("Para pegar con pegamento, ¿qué medida de seguridad se aplica?", "Cubrir la mesa y lavarse las manos", "Evita manchas y deja las manos limpias."),
        ("Si una tarea necesita una herramienta peligrosa, ¿quién la hace?", "Una persona adulta", "Las herramientas con riesgo no se usan sin adulto."),
    ],
    A=[
        ("Tarea: «Medir y marcar la base de 20 cm». Elige herramienta y técnica de esta lista: regla, tijeras, cinta, medir, cortar, pegar.", "Regla y medir", "Para medir y marcar se usa la regla."),
        ("Tarea: «Unir la pared a la base». Material: cartón. Escribe una herramienta o material para unir y una medida de seguridad.", "Cinta o pegamento; cubrir la mesa", "Une las piezas y cuida el lugar de trabajo."),
        arith("Para la base necesitas 20 cm de cartón y para la pared 10 cm. ¿Cuántos centímetros de cartón necesitas en total?", "20+10", "Se suman los dos pedazos."),
    ],
    Z=[
        ("Ana dice: «Uso cartón nuevo porque es más lindo». ¿Qué implicancia ambiental no está considerando?", "Que gasta más recursos que el reutilizado", "El cartón nuevo requiere fabricar más material."),
        ("Una tarea dice «cortar con cortador». ¿Qué debes hacer con esa herramienta en la clase?", "No usarla sin una persona adulta", "Tiene filo y no es adecuada sin supervisión."),
    ],
    D=[
        ("Tienes dos opciones para el soporte: A) cartón de una caja reutilizada y cinta, B) cartón nuevo y pegamento. Escribe cuál elegirías por el ambiente y una razón.", "A, porque reutiliza una caja y gasta menos recursos", "La opción reutilizada evita fabricar material nuevo."),
        arith("Un trabajo usa 3 trozos de cartón de 15 cm cada uno. ¿Cuántos centímetros de cartón hay en total?", "3*15", "Se multiplican los 3 trozos por 15 cm."),
    ],
    ctx=("Para hacer un porta-lápices de cartón tienes: cartón reutilizado, regla, tijeras de punta roma, cinta y témpera. Escribe para la tarea «Cortar las paredes» el material, la herramienta, la técnica y una medida de seguridad.", "Material: cartón reutilizado. Herramienta: tijeras de punta roma. Técnica: cortar. Seguridad: cortar lejos del cuerpo y sentado", "Incluye los cuatro elementos para la tarea."),
    sc=[
        ("¿Qué es una herramienta?", "Un objeto que se usa para trabajar el material", "No se transforma, ayuda a transformar."),
        ("En Tecnología: ¿Qué es una técnica?", "La manera de realizar una acción", "Como medir, cortar o plegar."),
        ("¿Qué es una implicancia ambiental?", "Cómo el uso de recursos afecta el ambiente", "Se piensa en material usado y residuos."),
    ],
    open_task=(
        "Escoge un resultado. Resultado 1: una caja de cartón con tapa para guardar clips. Resultado 2: un atril de cartón. Escribe una tabla con tres tareas y, para cada una, material, herramienta, técnica y medida de seguridad. Agrega una frase sobre cómo cuidarás el ambiente.",
        "Resultado 1: tarea: medir y marcar; material: cartón reutilizado; herramienta: regla; técnica: medir; seguridad: sentado. Ambiente: usaré cartón de una caja que iba a botar.",
        ["tres tareas con los cuatro datos", "herramientas y técnicas correctas", "una medida de seguridad por tarea", "una frase sobre el ambiente"],
        ["tabla de tres tareas y frase ambiental"],
        ["herramienta que no corresponde", "sin medida de seguridad"],
        "Pregunta: «¿qué herramienta y qué cuidado necesita esta tarea?». Si no lo dice, pídele revisar la tabla.",
    ),
    reinforce="Mira un objeto de cartón de tu casa y di con qué herramientas se pudo haber cortado y pegado.",
    extend="Escribe tres formas de reutilizar los retazos que sobran de un trabajo de cartón.",
)

# ------------------------------------------------------------------ OA 02, clase 3
reg(
    OA2, 3,
    materials="Hoja y lápiz. Las tareas y tiempos están escritos en este cuaderno.",
    use="Aprenderé a ordenar las tareas según cuáles dependen de otras y a poner puntos de control. Sirve para no pegar o pintar antes de tiempo.",
    prior=["Sé escribir tareas con verbo.", "Sé relacionar tareas con materiales y herramientas."],
    explain=[
        "Algunas tareas no se pueden hacer hasta que otra termine. Eso se llama dependencia. Por ejemplo, no puedes pegar una pared antes de cortarla, ni pintar una caja antes de armarla. Para ordenar bien, pregúntate de cada tarea: «¿qué necesito tener hecho antes?». Si la respuesta es una tarea, esa va antes.",
        "Otras tareas son independientes: no dependen una de otra. Pueden hacerse al mismo tiempo si trabajan dos personas, o en cualquier orden si trabaja una. Cortar la base y cortar la pared son independientes, porque las dos solo necesitan el cartón marcado.",
        "Un punto de control es un momento para revisar antes de seguir. Se pone después de tareas importantes: «medir otra vez antes de cortar» o «ver que la caja cierre antes de pintar». Un error corregido en el punto de control cuesta poco. El mismo error descubierto al final puede obligar a rehacer todo.",
    ],
    vocab=[("dependencia", "relación en que una tarea necesita que otra esté hecha antes"), ("tareas independientes", "tareas que no dependen una de otra"), ("punto de control", "momento en que se revisa antes de seguir"), ("orden", "lugar de cada tarea en la secuencia"), ("rehacer", "volver a hacer algo que quedó mal")],
    worked=[
        ("Ordenar por dependencias", "Tareas: A pintar la caja, B armar la caja, C cortar las piezas. Ordénalas.", ["Para armar necesito las piezas cortadas: C va antes de B.", "Para pintar necesito la caja armada: B va antes de A."], "C, B, A (cortar, armar, pintar)"),
        ("Poner un punto de control", "Tareas: marcar 10 cm, cortar, pegar. ¿Dónde pondrías un punto de control para no desperdiciar cartón?", ["Si marcas mal, cortarás mal.", "Reviso la medida antes de cortar."], "Después de marcar y antes de cortar"),
    ],
    mistakes=[
        ("Pintar la pieza antes de comprobar que encaja.", "Si hay que cortar de nuevo, la pintura se pierde.", "Revisa el encaje en un punto de control antes de pintar."),
        ("Pensar que todas las tareas deben hacerse una tras otra.", "Algunas son independientes y se pueden hacer a la vez.", "Pregunta qué tarea necesita estar hecha antes."),
    ],
    R=[
        ("¿Se puede pegar una pared antes de cortarla?", "No", "Pegar depende de que la pared esté cortada."),
        ("Revisar la medida antes de cortar, ¿es un punto de control o una tarea independiente?", "Un punto de control", "Es un momento de revisión antes de seguir."),
        ("Cortar la base y cortar la pared sin que una dependa de la otra, ¿son tareas independientes o dependientes?", "Independientes", "Las dos solo necesitan el cartón marcado."),
    ],
    C=[
        ("¿Qué pregunta ayuda a encontrar una dependencia?", "¿Qué necesito tener hecho antes?", "La respuesta dice qué tarea va primero."),
        ("¿Por qué conviene un punto de control antes de pintar?", "Porque si hay una falla, se corrige antes de gastar pintura", "Después de pintar corregir es más difícil."),
        ("Dos personas trabajan: una corta la base y otra la pared. ¿Qué tipo de tareas son?", "Independientes", "Se pueden hacer al mismo tiempo."),
    ],
    A=[
        ("Ordena estas tareas: A pegar la tapa, B cortar la tapa, C medir la tapa.", "C, B, A", "Se mide, se corta y se pega."),
        ("Tareas: marcar la base, cortar la base, pegar la base a la pared. ¿Después de cuál pondrías un punto de control para revisar que la pieza ya cortada mide 20 cm?", "Después de cortar la base", "Se revisa la medida de la pieza ya cortada."),
        arith("Un plan tiene 8 tareas y 2 son puntos de control. ¿Cuántas tareas de construcción tiene?", "8-2", "Se restan los puntos de control del total."),
    ],
    Z=[
        ("Tom pinta la tapa y después descubre que no cierra la caja. ¿Qué punto de control faltó?", "Probar que la tapa cierra antes de pintar", "Se debió comprobar el encaje antes de pintar."),
        ("Una compañera dice: «Pintar y cortar son tareas independientes». ¿Tiene razón si se pinta el cartón ya cortado?", "No", "Pintar la pieza depende de que ya esté cortada."),
    ],
    D=[
        arith("Plan de tiempos: medir 5 minutos, cortar 10, revisar 3, pegar 8. ¿Cuántos minutos dura todo?", "5+10+3+8", "Se suman los tiempos de las cuatro tareas."),
        ("Para el plan anterior, ¿qué tarea es un punto de control: medir, cortar, revisar o pegar?", "Revisar", "Es el momento en que se comprueba antes de seguir."),
    ],
    ctx=("Plan para un lapicero: A) pegar el tubo a la base, B) cortar la base, C) cortar el tubo, D) probar que el tubo queda parado, E) decorar. Escribe un orden que funcione y señala el punto de control.", "B, C, A, D, E. Punto de control: D, antes de decorar", "Primero cortes, luego unir, probar y decorar."),
    sc=[
        ("¿Qué es una dependencia entre tareas?", "Una tarea que necesita que otra esté hecha antes", "Marca el orden de las tareas."),
        ("¿Para qué sirve un punto de control?", "Para revisar antes de seguir", "Evita rehacer todo al final."),
        ("¿Dos tareas independientes se pueden hacer a la vez?", "Sí", "No dependen una de la otra."),
    ],
    open_task=(
        "Escoge un plan. Plan 1: caja con tapa (marcar, cortar paredes, cortar tapa, unir paredes, unir tapa, pintar). Plan 2: atril (marcar, cortar base, cortar apoyo, unir, probar con hojas). Ordena las tareas, señala una pareja de tareas independientes y pon dos puntos de control con la razón de cada uno.",
        "Plan 1: marcar, cortar paredes, cortar tapa, unir paredes, unir tapa, pintar. Independientes: cortar paredes y cortar tapa. Controles: después de marcar (medida) y antes de pintar (la tapa cierra).",
        ["ordena con dependencias", "señala tareas independientes", "dos puntos de control", "da la razón de cada control"],
        ["secuencia con controles y razones"],
        ["pintar antes de unir", "controles sin razón"],
        "Pregunta: «¿qué error se evita con este control?». Si no responde, pídele pensar qué falla puede aparecer.",
    ),
    reinforce="Piensa en tres tareas de tu casa, como vestirte y hacer la mochila, y di cuál debe ir antes.",
    extend="Agrega a un plan de tu elección un tercer punto de control y explica qué error evita.",
)

# ------------------------------------------------------------------ OA 02, clase 4
reg(
    OA2, 4,
    materials="Hoja, lápiz y los datos escritos en este cuaderno. Si quieres, un reloj.",
    use="Aprenderé a construir un plan completo, seguro y que se pueda hacer con los recursos y el tiempo que tengo. Sirve para trabajar sin sorpresas.",
    prior=["Sé ordenar tareas por dependencias.", "Sé poner puntos de control."],
    explain=[
        "Un plan completo reúne todo lo que vimos: el resultado deseado, la lista de tareas en orden, los materiales con sus cantidades, las herramientas, las técnicas, las medidas de seguridad, los puntos de control y el tiempo de cada tarea. Con esto otra persona podría seguir tu plan y construir lo mismo.",
        "Un plan es realizable cuando cabe en el tiempo y en los recursos disponibles. Para saberlo, suma el tiempo de todas las tareas y compáralo con el tiempo que tienes. Si tardas 50 minutos y tienes 40, hay que reducir tareas o simplificar el diseño. También se suma el material: si necesitas 60 cm de cordel y tienes 50, falta material.",
        "Un plan es seguro cuando cada tarea tiene su cuidado y ninguna usa herramientas peligrosas sin una persona adulta. Revisa tu plan con una lista: ¿está completo?, ¿es seguro?, ¿cabe en el tiempo?, ¿cabe en los materiales?, ¿cuida el ambiente? Si alguna respuesta es no, ajusta el plan antes de empezar.",
    ],
    vocab=[("plan realizable", "plan que se puede hacer con el tiempo y los recursos que hay"), ("plan seguro", "plan en que cada tarea tiene su cuidado"), ("cantidad de material", "cuánto material hace falta"), ("tiempo disponible", "minutos que tienes para el trabajo"), ("ajustar", "cambiar el plan para que cumpla lo pedido")],
    worked=[
        ("Revisar si el plan cabe en el tiempo", "Tareas: marcar 8 min, cortar 12 min, unir 10 min, probar 5 min. Tienes 40 minutos. ¿Cabe?", ["8 + 12 + 10 + 5 = 35.", "35 es menor que 40.", "Sobran 5 minutos."], "Sí, cabe: 35 minutos de 40"),
        ("Revisar los materiales", "El plan pide 60 cm de cordel y tienes 50 cm. ¿Qué haces?", ["Faltan 10 cm.", "Puedo usar menos cordel o buscar más.", "Ajusto el plan."], "Reducir el cordel a 50 cm o conseguir 10 cm más"),
    ],
    mistakes=[
        ("Escribir el plan sin sumar los tiempos.", "Puede que no alcance el tiempo para terminar.", "Suma los minutos y compáralos con el tiempo disponible."),
        ("Dejar una herramienta peligrosa en el plan.", "El plan no es seguro para el curso.", "Cámbiala por una herramienta segura o pide a una persona adulta."),
    ],
    R=[
        ("Un plan que cabe en el tiempo y en los materiales, ¿es realizable o no realizable?", "Realizable", "Se puede hacer con lo que hay."),
        ("Si cada tarea tiene su cuidado, ¿el plan es seguro o inseguro?", "Seguro", "Cada riesgo está considerado."),
        ("Si faltan materiales, ¿hay que ajustar el plan?", "Sí", "No se puede hacer con lo que falta."),
    ],
    C=[
        ("¿Para qué se suma el tiempo de todas las tareas?", "Para saber si cabe en el tiempo disponible", "Se compara con el tiempo que hay."),
        ("¿Qué cinco cosas revisa la lista final del plan?", "Completo, seguro, tiempo, materiales y ambiente", "Son las cinco preguntas de la lista."),
        ("Un plan pide cortar con un cortador. ¿Es seguro para el curso?", "No", "Debe cambiarse por una herramienta de punta roma."),
    ],
    A=[
        arith("Tareas: marcar 10 min, cortar 15 min, unir 12 min, probar 8 min. ¿Cuántos minutos suma el plan?", "10+15+12+8", "Se suman los tiempos de las cuatro tareas."),
        arith("Tienes 60 minutos. El plan dura 45. ¿Cuántos minutos sobran?", "60-45", "Se resta el tiempo del plan al disponible."),
        arith("El plan pide 40 cm de cinta y tienes 25 cm. ¿Cuántos centímetros faltan?", "40-25", "Se resta lo que tienes de lo que pide."),
    ],
    Z=[
        ("Un plan dura 50 minutos y tienes 40. Beto propone quitar el punto de control para ahorrar 3 minutos. ¿Es buena idea?", "No", "El control evita errores; mejor simplificar el diseño."),
        ("Un plan tiene tareas, materiales y tiempos, pero ninguna medida de seguridad. ¿Qué le falta para estar completo?", "Las medidas de seguridad", "Cada tarea debe tener su cuidado."),
    ],
    D=[
        arith("Dos personas hacen el plan: una tarda 20 minutos y la otra 15, trabajando a la vez. Si trabajaran una después de la otra, ¿cuántos minutos serían?", "20+15", "Se suman los tiempos si trabajan una tras otra."),
        ("En el plan de dos personas (20 y 15 minutos a la vez), ¿cuántos minutos se necesitan si trabajan al mismo tiempo?", "20 minutos", "Mientras una termina en 20, la otra ya terminó en 15."),
    ],
    ctx=("Plan para un porta-lápices: marcar 8 min, cortar 12 min, unir 10 min, probar 5 min. Tienes 30 minutos y necesitas 50 cm de cartón; tienes 45 cm. ¿El plan es realizable? Di qué ajustarías.", "No. Suma 35 minutos y tengo 30; faltan 5 cm de cartón. Ajusto reduciendo el tamaño del porta-lápices", "Detecta tiempo y material insuficientes y propone ajuste."),
    sc=[
        ("¿Qué datos reúne un plan completo?", "Resultado, tareas, materiales, herramientas, técnicas, seguridad, controles y tiempos", "Sirve para que otra persona lo repita."),
        ("¿Cómo se sabe si el plan cabe en el tiempo?", "Sumando los minutos de las tareas", "Se compara con el tiempo disponible."),
        ("¿Qué se hace si el plan no cabe?", "Se ajusta", "Se reducen tareas o se simplifica el diseño."),
    ],
    open_task=(
        "Escoge un resultado. Resultado 1: caja de cartón con tapa para guardar clips, 40 minutos. Resultado 2: atril de cartón para 3 hojas, 30 minutos. Escribe un plan con: cinco tareas con tiempo en minutos, materiales con cantidad, herramientas, una medida de seguridad por tarea y dos puntos de control. Suma el tiempo y di si cabe.",
        "Resultado 2: marcar 4, control de la medida 2, cortar 8, unir 7, control del encaje 2, probar 5 = 28 minutos de 30. Sí cabe.",
        ["cinco tareas con tiempo", "materiales y herramientas", "seguridad en cada tarea", "dos controles", "suma el tiempo y decide"],
        ["plan escrito con suma de tiempo"],
        ["no sumar los tiempos", "olvidar la seguridad"],
        "Pregunta: «¿cabe en el tiempo y en los materiales?». Si no lo calculó, pídele sumar.",
    ),
    reinforce="Calcula cuánto demoras en prepararte para salir de tu casa y compáralo con el tiempo que tienes.",
    extend="Reduce un plan de 50 minutos a 40 minutos quitando solo una tarea que no sea esencial.",
)

# ------------------------------------------------------------------ OA 02, clase 5
reg(
    OA2, 5,
    materials="Hoja y lápiz. Los planes y cambios de condición están escritos en el cuaderno.",
    use="Aprenderé a adaptar un plan cuando cambia una condición, como el material, el tiempo o la herramienta. Sirve para resolver problemas reales sin empezar de cero.",
    prior=["Sé armar un plan con tareas, materiales, tiempos y seguridad.", "Sé qué es un plan realizable."],
    explain=[
        "Cuando algo cambia, un buen plan se adapta. Transferir es usar lo aprendido en una situación nueva. Las condiciones que pueden cambiar son tres: el material (se acabó el cartón), la herramienta (no hay tijeras) o el tiempo (hay menos minutos de los previstos). El resultado deseado casi siempre se mantiene.",
        "Para adaptar, haz tres pasos. Primero, identifica qué cambió. Segundo, revisa qué tareas, materiales o herramientas se ven afectados. Tercero, cambia solo lo necesario y vuelve a comprobar que el plan sea completo, seguro, realizable y cuide el ambiente. No tires el plan entero si solo cambió una cosa.",
        "A veces el cambio obliga a una decisión: usar otro material, quitar un detalle del diseño o pedir más tiempo. La decisión se justifica con un criterio, como «el material alternativo también aguanta 10 fichas». También se revisan las implicancias ambientales del cambio: un material reutilizado sigue siendo mejor que uno nuevo.",
    ],
    vocab=[("transferir", "usar lo aprendido en una situación nueva"), ("condición", "dato que puede cambiar, como material, herramienta o tiempo"), ("adaptar", "cambiar lo necesario para que algo siga funcionando"), ("alternativa", "otra opción que sirve para lo mismo"), ("justificar", "dar una razón con datos")],
    worked=[
        ("Cambia el material", "Tu plan usaba cartón, pero solo tienes papel grueso. El soporte debe aguantar 10 fichas. ¿Qué cambias?", ["Cambió el material.", "El papel es más débil que el cartón.", "Lo doblo en capas para reforzarlo y compruebo con la prueba de 10 fichas."], "Reforzar el papel doblándolo en capas y volver a probar"),
        ("Cambia el tiempo", "Tu plan dura 35 minutos y ahora tienes 25. ¿Qué haces?", ["Faltan 10 minutos.", "Quito una tarea que no es esencial, como la decoración.", "Mantengo los puntos de control."], "Quitar la decoración y mantener los controles"),
    ],
    mistakes=[
        ("Botar todo el plan cuando cambia una condición.", "Solo hay que cambiar lo afectado.", "Revisa qué cambió y adapta solo eso."),
        ("Cambiar un material sin comprobar que cumple el criterio.", "El nuevo material podría no sostener lo pedido.", "Prueba el material alternativo con el criterio del diseño."),
    ],
    R=[
        ("Si se acaba el cartón, ¿cambió el material, la herramienta o el tiempo?", "El material", "Es lo que se transforma."),
        ("Usar lo aprendido en una situación nueva se llama...", "Transferir", "Es el nombre de esta idea."),
        ("¿Se bota todo el plan si cambia solo una condición?", "No", "Se cambia solo lo afectado."),
    ],
    C=[
        ("¿Cuáles son los tres pasos para adaptar un plan?", "Identificar qué cambió, revisar lo afectado y cambiar solo lo necesario", "Evitan rehacer todo el plan."),
        ("¿Por qué hay que comprobar que el nuevo material cumpla el criterio?", "Porque podría no sostener lo que se pide", "Un material distinto puede tener otra resistencia."),
        ("Si el plan era seguro y cambias el material, ¿vuelves a revisar la seguridad?", "Sí", "El nuevo material puede traer otros riesgos."),
    ],
    A=[
        arith("El plan dura 45 minutos y ahora hay 30. ¿Cuántos minutos hay que ahorrar?", "45-30", "Se resta el nuevo tiempo del plan original."),
        ("No hay cinta, pero hay pegamento. La tarea es «unir la pared a la base». ¿Qué cambias?", "La herramienta o material para unir, de cinta a pegamento", "La acción es la misma y cambia con qué se hace."),
        arith("Tu plan usaba trozos de cartón de 10 cm y ahora solo tienes una tira de 20 cm. ¿Cuántos trozos de 10 cm puedes cortar?", "20//10", "Se divide el largo de la tira por el largo de cada trozo."),
    ],
    Z=[
        ("Dani cambió el cartón por servilletas de papel en un soporte que debe aguantar 10 fichas, y no probó. ¿Qué error cometió?", "No comprobó que el nuevo material cumpliera el criterio", "Las servilletas pueden no aguantar el peso."),
        ("Entre quitar la prueba o quitar la decoración para ahorrar tiempo, ¿qué conviene quitar?", "La decoración", "La prueba comprueba que el objeto cumple el criterio."),
    ],
    D=[
        arith("El plan original usaba 60 cm de cordel. Ahora solo hay 40 cm. ¿Cuántos centímetros de cordel hay que ahorrar?", "60-40", "Se resta lo que hay de lo que pedía el plan."),
        arith("Cada punto de atado usa 10 cm de cordel. Con los 40 cm que hay, ¿cuántos puntos de atado puedes hacer?", "40//10", "Se divide el cordel disponible por lo que usa cada punto."),
    ],
    ctx=("Tu plan para un porta-lápices usa cartón de una caja reutilizada y tijeras de punta roma. Ahora no hay tijeras, pero puedes plegar el cartón y usar cinta, y debes guardar 5 lápices. Escribe qué técnica cambiarías y qué comprobarías.", "Cambiaría cortar por plegar el cartón en forma de cajita; comprobaría que guarda 5 lápices y que no tiene puntas", "Adapta la técnica y comprueba el criterio."),
    sc=[
        ("En Tecnología: ¿Qué es transferir?", "Usar lo aprendido en una situación nueva", "Permite resolver cambios sin empezar de cero."),
        ("¿Qué tres condiciones suelen cambiar?", "Material, herramienta y tiempo", "Son las tres de la clase."),
        ("¿Se justifica un cambio con gustos o con un criterio?", "Con un criterio", "El criterio se puede comprobar."),
    ],
    open_task=(
        "Escoge un cambio. Cambio 1: en el plan de la caja con tapa se acabó el cartón y solo hay papel grueso. Cambio 2: el plan del atril dura 35 minutos (marcar 5, cortar 8, unir 7, control 3, probar 5, decorar 7) y ahora solo quedan 30 minutos. Escribe qué cambió, qué partes del plan se ven afectadas, qué ajustes harás y cómo comprobarás que sigue siendo seguro y realizable.",
        "Cambio 2: cambió el tiempo (faltan 5 minutos). Quito decorar (7 minutos) y mantengo el control y la prueba. Comprobaré: 5+8+7+3+5 = 28 minutos, que cabe en 30.",
        ["identifica la condición que cambió", "indica las partes afectadas", "ajusta solo lo necesario", "comprueba seguridad y que sea realizable"],
        ["texto de adaptación del plan"],
        ["botar todo el plan", "no comprobar el criterio"],
        "Pregunta: «¿qué es lo único que cambió y qué partes toca?». Si responde todo, pídele distinguir.",
    ),
    reinforce="Piensa qué harías si, al hacer una receta, te falta un ingrediente. ¿Cambias toda la receta o solo una parte?",
    extend="Elige un plan tuyo y escribe cómo lo adaptarías si tuvieras la mitad del tiempo.",
)

# ------------------------------------------------------------------ OA 03, clase 1
reg(
    OA3, 1,
    materials="Hoja y lápiz. Los materiales se describen con palabras y no necesitas tenerlos. Si quieres, observa objetos de tu casa.",
    use="Aprenderé a comparar materiales y a elegir el que sirve mejor para la función del objeto. Sirve para que lo que construyo cumpla su tarea.",
    prior=["Sé nombrar materiales como papel y cartón.", "Sé qué es un criterio comprobable."],
    explain=[
        "Los materiales tienen propiedades, que son características que se pueden observar o probar. Algunas son: flexible (se dobla sin romperse), rígido (casi no se dobla), resistente (aguanta peso o golpes), impermeable (no deja pasar el agua) y frágil (se rompe fácil). El papel es flexible, el cartón es más rígido, la madera es rígida y resistente, y un recipiente de cerámica es frágil.",
        "Los materiales se agrupan en familias: papeles, cartones, maderas, fibras como el cordel o la tela, plásticos, cerámicos y desechos reutilizables, como tubos o cajas. Cada familia tiene propiedades distintas. Elegir bien es elegir según la función del objeto: un soporte que aguanta peso necesita un material rígido; una cubierta para la lluvia, uno impermeable.",
        "Para comparar, usa una prueba sencilla y el mismo criterio para todos. Por ejemplo, pon 10 fichas sobre un puente de papel y otro de cartón de igual tamaño y observa cuál se dobla. Anota los resultados. El material elegido no es el más bonito, sino el que cumple mejor la función y cuida el ambiente.",
    ],
    vocab=[("propiedad", "característica de un material que se observa o prueba"), ("flexible", "se dobla sin romperse"), ("rígido", "casi no se dobla"), ("resistente", "aguanta peso o golpes"), ("impermeable", "no deja pasar el agua")],
    worked=[
        ("Elegir según la función", "Quieres un soporte que aguante 10 fichas. Opciones: A papel, B cartón. ¿Cuál eliges y por qué?", ["Necesito un material rígido y resistente.", "El papel es flexible y se dobla.", "El cartón es más rígido."], "El cartón, porque es más rígido"),
        ("Comparar con una prueba", "Pusiste 10 fichas sobre un puente de papel y se dobló 3 cm. Sobre uno de cartón de igual tamaño se dobló 1 cm. ¿Cuál es más rígido?", ["3 cm es más que 1 cm.", "Se dobló menos el de cartón."], "El cartón"),
    ],
    mistakes=[
        ("Elegir el material por el color o por gusto.", "El color no dice si cumple la función.", "Elige por propiedades y por una prueba."),
        ("Comparar materiales en piezas de tamaños distintos.", "La prueba no es justa.", "Usa piezas del mismo tamaño y la misma carga."),
    ],
    R=[
        ("Un material que se dobla sin romperse, ¿es flexible o rígido?", "Flexible", "Esa es la definición de flexible."),
        ("Un material que no deja pasar el agua, ¿es impermeable o frágil?", "Impermeable", "Esa es la definición de impermeable."),
        ("El cordel y la tela, ¿son fibras o maderas?", "Fibras", "Son materiales hechos de hilos."),
    ],
    C=[
        ("¿Por qué se compara con piezas del mismo tamaño?", "Para que la prueba sea justa", "Así la diferencia viene del material."),
        ("Un recipiente de cerámica se rompe si cae. ¿Qué propiedad tiene?", "Es frágil", "Se rompe fácilmente."),
        ("¿El material se elige por la función o por el color?", "Por la función", "Debe cumplir lo que el objeto necesita."),
    ],
    A=[
        ("Necesitas cubrir un trabajo de la lluvia. Opciones: A papel, B plástico. ¿Cuál es más adecuado?", "B", "El plástico es impermeable y el papel se moja."),
        ("Necesitas atar un paquete. Opciones: A cordel, B cerámica. ¿Cuál sirve?", "A", "El cordel es una fibra flexible; la cerámica no se ata."),
        arith("Un puente de papel se dobló 4 cm y uno de cartón se dobló 1 cm. ¿Cuántos centímetros menos se dobló el de cartón?", "4-1", "Se resta lo que se dobló el cartón de lo que se dobló el papel."),
    ],
    Z=[
        ("Eli dice: «El papel es mejor para el soporte porque pesa menos». ¿Qué propiedad falta considerar?", "La rigidez", "Pesar menos no asegura que aguante las fichas."),
        ("Dos puentes del mismo tamaño: de cartón con 10 fichas se dobló 1 cm y de madera con 10 fichas se dobló 0 cm. ¿Cuál es más rígido?", "El de madera", "No se dobló nada con la misma carga."),
    ],
    D=[
        ("Una funda para guardar un estuche debe doblarse sin romperse. ¿Conviene un material flexible o uno rígido?", "Flexible", "La función pide doblarse sin romperse."),
        ("Si usas un tubo de cartón que ibas a botar como lapicero, ¿fabricas material nuevo o aprovechas un desecho?", "Aprovechas un desecho", "El tubo ya existía y se reutiliza."),
    ],
    ctx=("Quieres construir un puente para que pasen 10 fichas. Pruebas dos materiales de igual tamaño: papel (se dobló 5 cm) y cartón (se dobló 1 cm). Elige uno y justifica con los datos.", "El cartón, porque con las mismas 10 fichas se dobló 1 cm contra 5 cm del papel, es decir, es más rígido", "Elige con datos de la prueba."),
    sc=[
        ("En Tecnología: ¿Qué es una propiedad de un material?", "Una característica que se observa o prueba", "Describe cómo se comporta el material."),
        ("¿Se elige el material por función o por gusto?", "Por función", "Debe cumplir lo que el objeto necesita."),
        ("¿Qué propiedad tiene un material que aguanta mucho peso?", "Es resistente", "Resistente significa que aguanta peso o golpes."),
    ],
    open_task=(
        "Escoge un objeto. Objeto 1: un soporte que aguante 10 fichas. Objeto 2: una cubierta para proteger un trabajo de la lluvia. Materiales disponibles: papel, cartón, cordel, plástico limpio de una bolsa. Compara dos materiales para tu objeto, anota una propiedad de cada uno y elige uno, justificando con la función.",
        "Objeto 2: comparo plástico y papel; el plástico es impermeable y el papel se moja. Elijo plástico limpio reutilizado.",
        ["compara dos materiales", "anota una propiedad de cada uno", "elige según la función", "justifica con la propiedad"],
        ["tabla de dos materiales y elección justificada"],
        ["elegir por color", "no dar una propiedad"],
        "Pregunta: «¿qué necesita hacer este objeto?». Si responde con gustos, pídele volver a la función.",
    ),
    reinforce="Toca tres objetos de tu casa y di si el material parece flexible, rígido o frágil.",
    extend="Haz una prueba de doblado con una hoja y una cartulina del mismo tamaño y anota cuál se dobla más.",
)

# ------------------------------------------------------------------ OA 03, clase 2
reg(
    OA3, 2,
    materials="Hoja y lápiz. Si quieres practicar, usa retazos de papel y cartón y tijeras de punta roma, con una persona adulta cerca. Las demás técnicas están descritas.",
    use="Aprenderé técnicas para medir, marcar, cortar, plegar, unir y pegar, y cómo practicarlas en retazos antes de usar el material final. Sirve para trabajar con precisión.",
    prior=["Sé elegir un material según su función.", "Sé medir en centímetros."],
    explain=[
        "Una técnica es una manera ordenada de hacer una acción. Medir es usar una regla para saber cuánto mide algo: se pone el cero de la regla en el borde. Marcar es dibujar con lápiz una línea o un punto donde se va a cortar o plegar. Cortar es separar el material con tijeras de punta roma, sentado y lejos del cuerpo.",
        "Plegar es doblar el material sobre una línea marcada, apretando con el dedo para que el doblez quede recto. Unir es juntar dos piezas con cinta, cordel o pegamento. Pegar es unir con pegamento: se pone poco, se aprieta y se espera a que seque. Perforar con perforador de papel y serrar madera los hace una persona adulta, con la pieza sujeta.",
        "Antes de usar el material final, practica cada técnica en un retazo, que es un pedazo que sobra. Si fallas en el retazo, no pierdes material. Repite hasta que la línea sea recta y la medida correcta. Anota qué hiciste y cómo lo mejoraste. Así demuestras dominio de la técnica, no solo un resultado.",
    ],
    vocab=[("retazo", "pedazo de material que sobra"), ("medir", "usar la regla para saber cuánto mide algo"), ("marcar", "dibujar la línea donde se cortará o plegará"), ("plegar", "doblar sobre una línea marcada"), ("unir", "juntar dos piezas con cinta, cordel o pegamento")],
    worked=[
        ("Medir con regla", "Para medir una tira, la pones con el cero de la regla en el borde izquierdo y el otro borde llega a la marca de 14 cm. ¿Cuánto mide la tira?", ["El cero está en el borde.", "El otro borde llega a 14.", "La medida es la que marca el otro borde."], "14 cm"),
        ("Practicar en un retazo", "Quieres plegar una cartulina en una línea recta, pero tu primer doblez salió torcido. ¿Qué haces antes de usar el material final?", ["Practico en un retazo.", "Marco la línea con regla y lápiz.", "Aprieto con el dedo para que quede recto."], "Practicar de nuevo en el retazo con la línea marcada con regla"),
    ],
    mistakes=[
        ("Medir sin poner el cero de la regla en el borde.", "La medida sale con error.", "Alinea el cero con el borde antes de leer."),
        ("Practicar la técnica directamente en el material final.", "Si falla, se pierde material.", "Practica primero en un retazo."),
    ],
    R=[
        ("Dibujar con lápiz la línea donde se va a cortar, ¿es medir o marcar?", "Marcar", "Marcar es dejar una línea o punto."),
        ("Doblar sobre una línea marcada, ¿es plegar o cortar?", "Plegar", "Doblar es plegar."),
        ("Un pedazo de material que sobra, ¿cómo se llama?", "Retazo", "Es el nombre de ese pedazo."),
    ],
    C=[
        ("¿Por qué se practica en un retazo?", "Para no perder el material final si algo sale mal", "El retazo es material que sobra."),
        ("¿Quién perfora con perforador de papel y sierra la madera?", "Una persona adulta", "Son acciones con riesgo."),
        ("¿Qué se hace antes de leer una medida en la regla?", "Poner el cero en el borde", "Así la medida es correcta."),
    ],
    A=[
        arith("Necesitas una tira de 15 cm y tu retazo mide 22 cm. ¿Cuántos centímetros sobran después de cortar?", "22-15", "Se resta lo que usas de lo que tienes."),
        ("Quieres que dos piezas queden pegadas sin chorrear pegamento. ¿Pones mucho o poco?", "Poco", "Con poco pegamento no rebalsa y pega bien."),
        ("Para cortar un cartón con tijeras de punta roma, ¿cómo te sientas y hacia dónde cortas?", "Sentado y lejos del cuerpo", "Es la medida de seguridad para cortar."),
    ],
    Z=[
        ("Mara dice: «Si mi retazo quedó mal, ya sé hacerlo bien en el material final». ¿Qué falta?", "Repetir hasta que salga bien en el retazo", "Dominar una técnica requiere practicarla hasta que salga bien."),
        ("Entre pegar el borde con mucho pegamento o con poco, ¿cuál evita que el trabajo se arrugue?", "Con poco", "El exceso moja el papel y lo deforma."),
    ],
    D=[
        arith("Practicas cortar 4 tiras de 6 cm en un retazo. ¿Cuántos centímetros de retazo necesitas para las cuatro tiras?", "4*6", "Se multiplican las tiras por su medida."),
        arith("Si el retazo mide 30 cm de largo y usaste 24 cm, ¿cuántos centímetros quedan?", "30-24", "Se resta lo usado del largo total."),
    ],
    ctx=("Vas a construir una caja de cartón. Tu retazo tiene una línea de 10 cm marcada. Practica en la cabeza y escribe, en orden, cuatro técnicas que usarás: medir, marcar, cortar y plegar. Di una medida de seguridad para cortar.", "Medir 10 cm con la regla; marcar la línea con lápiz; cortar con tijeras de punta roma sentado y lejos del cuerpo; plegar sobre la línea", "Cuatro técnicas en orden con una medida de seguridad."),
    sc=[
        ("¿Para qué sirve un retazo?", "Para practicar una técnica sin perder el material final", "Es material que sobra."),
        ("¿Qué técnica es doblar sobre una línea?", "Plegar", "Es la acción de doblar."),
        ("¿Quién perfora o sierra?", "Una persona adulta", "Las acciones con riesgo las hace un adulto."),
    ],
    open_task=(
        "Escoge una práctica en un retazo. Práctica 1: medir y marcar una línea de 12 cm en un trozo de cartulina y plegarla. Práctica 2: medir y marcar dos tiras de 8 cm, cortarlas con tijeras de punta roma y unirlas con cinta. Hazla y anota las medidas, qué falló y qué mejoraste.",
        "Práctica 1: línea de 12 cm; primer doblez torcido; mejoré usando la regla para guiar el doblez.",
        ["mide y marca con regla", "practica en un retazo", "anota qué falló", "anota qué mejoró"],
        ["retazo practicado y nota de lo que mejoró"],
        ["no poner el cero de la regla en el borde", "practicar en el material final"],
        "Pregunta: «¿qué hiciste distinto en el segundo intento?». Si nada, pídele cambiar una cosa.",
    ),
    reinforce="Mide con una regla tres objetos pequeños de tu casa y anota sus largos en centímetros.",
    extend="Explica con tus palabras por qué practicar en un retazo ahorra material.",
)

# ------------------------------------------------------------------ OA 03, clase 3
reg(
    OA3, 3,
    materials="Hoja y lápiz. Los datos y las medidas están escritos en el cuaderno. Si construyes, usa papel, cartón y cinta.",
    use="Aprenderé a construir un objeto paso a paso con puntos de control. Sirve para encontrar errores a tiempo y mejorar la calidad.",
    prior=["Sé medir, marcar, cortar, plegar y unir.", "Sé qué es un punto de control en un plan."],
    explain=[
        "Construir con puntos de control significa que después de cada parte importante te detienes y revisas antes de seguir. Se revisa con una pregunta concreta: «¿la pieza mide lo que dice el plan?», «¿encaja con la otra?», «¿está recta?». Un dato comprobable evita adivinar.",
        "Una regla muy útil es medir dos veces y cortar una. Primero marcas la medida; luego la compruebas de nuevo con la regla; recién entonces cortas. Si cortas mal, no puedes devolver el material. Otro control importante es probar el encaje en seco, es decir, sin pegamento, para ver si las piezas calzan antes de unirlas.",
        "Si encuentras una falla, no la escondas: corrígela o anótala. Por ejemplo, si una pieza quedó 1 cm más corta, puedes rehacerla con el retazo. Llevar un registro breve de cada control ayuda a explicar tus decisiones: qué revisaste, qué encontraste y qué hiciste. Eso muestra dominio y no solo un objeto terminado.",
    ],
    vocab=[("control", "revisión que se hace antes de seguir"), ("encaje en seco", "probar que las piezas calzan sin pegar"), ("calzar", "encajar bien una pieza en otra"), ("registro", "anotación de lo que se revisó y se hizo"), ("falla", "algo que no cumple lo planificado")],
    worked=[
        ("Medir dos veces", "Marcaste una pieza de 18 cm. Al medir de nuevo, la marca está en 17 cm. ¿Qué haces antes de cortar?", ["Las dos medidas no coinciden.", "Hay un error de 1 cm.", "Corrijo la marca a 18 cm y vuelvo a medir."], "Corregir la marca a 18 cm y medir otra vez antes de cortar"),
        ("Encaje en seco", "Cortaste una pared de 10 cm y la base tiene un espacio de 12 cm. Antes de pegar, pruebas el encaje. ¿Qué observas?", ["La pared es 2 cm más corta.", "No calza.", "Mejor lo descubro antes de pegar."], "No calza; la pared es 2 cm más corta"),
    ],
    mistakes=[
        ("Cortar apenas se marca, sin revisar.", "Si la marca está mal, no se puede devolver el material.", "Mide dos veces y corta una."),
        ("Pegar antes de probar el encaje en seco.", "Si no calza, ya no se puede corregir sin romper.", "Prueba sin pegamento y recién después pega."),
    ],
    R=[
        ("«Medir dos veces y cortar una», ¿evita errores antes o después de cortar?", "Antes de cortar", "Es una revisión previa."),
        ("Probar que las piezas calzan sin pegar, ¿cómo se llama?", "Encaje en seco", "Es una prueba sin pegamento."),
        ("Anotar lo que revisaste y lo que hiciste, ¿es un registro o una falla?", "Un registro", "Sirve para explicar tus decisiones."),
    ],
    C=[
        ("¿Por qué conviene probar el encaje antes de pegar?", "Porque si no calza, se corrige antes de unir", "Después de pegar es difícil corregir."),
        ("¿Qué haces si la pieza queda más corta?", "La rehago o la anoto como falla", "No se esconde la falla."),
        ("¿Para qué sirve un registro de controles?", "Para explicar qué se revisó y qué se decidió", "Muestra el proceso."),
    ],
    A=[
        arith("La pared debía medir 15 cm y mide 13 cm. ¿Cuántos centímetros faltan?", "15-13", "Se resta lo que mide de lo que debía medir."),
        ("Pieza A mide 10 cm y pieza B mide 10 cm. Las probaste en seco y calzan. ¿Puedes pegarlas?", "Sí", "El control de encaje salió bien."),
        ("Marcaste 20 cm y al repetir la medida sale 20 cm. ¿Cortas o vuelves a marcar?", "Cortas", "Las dos medidas coinciden."),
    ],
    Z=[
        ("Fer dice: «Si pego rápido, termino antes». ¿Qué riesgo corre si no prueba el encaje?", "Que las piezas no calcen y deba rehacer", "El tiempo ganado se pierde al corregir."),
        ("Dos estudiantes tienen una pieza 1 cm corta. Uno la esconde y otro la anota y la rehace. ¿Quién demuestra más dominio?", "El que la anota y la rehace", "Reconocer y corregir la falla es parte del dominio."),
    ],
    D=[
        arith("Una caja necesita 4 paredes de 10 cm. Ya cortaste 3. ¿Cuántos centímetros de pared te faltan por cortar?", "4*10-3*10", "Se calcula el total de las 4 paredes y se resta lo cortado."),
        ("Registra en una frase: el control, lo que encontraste y lo que hiciste, para este caso: la tapa medía 11 cm en vez de 12 cm.", "Revisé la tapa; mide 11 cm y debía medir 12; la rehice con un retazo", "Incluye control, hallazgo y acción."),
    ],
    ctx=("Estás construyendo una caja con base de 12 cm. Marcaste una pared de 12 cm, la mediste otra vez y marca 12 cm. La cortas y pruebas el encaje en seco: calza. Escribe los dos controles que hiciste y qué harás ahora.", "Control 1: medí dos veces la pared, 12 cm. Control 2: encaje en seco, calza. Ahora puedo pegar", "Dos controles y una decisión coherente."),
    sc=[
        ("¿Qué significa medir dos veces?", "Comprobar la medida antes de cortar", "Evita errores que no se pueden devolver."),
        ("¿Qué es el encaje en seco?", "Probar que las piezas calzan sin pegar", "Se hace antes de unir."),
        ("¿Se esconden las fallas?", "No", "Se corrigen o se anotan."),
    ],
    open_task=(
        "Escoge una construcción. Construcción 1: una caja de cartulina de 10 cm de lado. Construcción 2: un atril de cartulina de 12 cm de alto. Construye con papel y cinta, mide dos veces antes de cortar, prueba el encaje en seco y anota tres controles: qué revisaste, qué encontraste y qué hiciste.",
        "Construcción 1: medí dos veces el lado de 10 cm; el encaje en seco mostró un borde de 9 cm; lo rehice con un retazo de 10 cm.",
        ["mide dos veces", "prueba el encaje en seco", "anota tres controles", "corrige o registra una falla"],
        ["objeto y registro de tres controles"],
        ["cortar sin comprobar", "esconder una falla"],
        "Pregunta: «¿qué comprobaste antes de pegar?». Si nada, pídele repetir el encaje.",
    ),
    reinforce="Mide dos veces un objeto de tu casa y comprueba que las dos medidas coinciden.",
    extend="Escribe una regla personal de tres pasos para construir con control.",
)

# ------------------------------------------------------------------ OA 03, clase 4
reg(
    OA3, 4,
    materials="Hoja y lápiz. Si pintas, usa témpera, un paño de protección y lava tus manos al terminar. Los casos están en este cuaderno.",
    use="Aprenderé a dar un buen acabado, como pintar o limpiar bordes, sin ocultar las fallas. Sirve para que el objeto se vea bien y se pueda revisar con honestidad.",
    prior=["Sé construir con controles.", "Sé que el color no cambia el funcionamiento."],
    explain=[
        "El acabado es el último trabajo sobre el objeto: pintar, limpiar los bordes, decorar o proteger. Un buen acabado hace que el objeto se vea mejor y dure más. Pero el acabado no debe esconder fallas. Si una unión quedó débil, pintarla no la arregla; solo la oculta, y la falla seguirá ahí.",
        "Por eso el orden importa: primero revisas el funcionamiento y las uniones, luego haces el acabado. Para pintar, usa una capa fina y pareja, deja secar entre capas y protege la mesa. Los bordes se alisan con cuidado: no uses nada con filo. Si hay una arista que pincha, se dobla hacia dentro o se cubre con cinta.",
        "El acabado también puede mostrar tu cuidado ambiental: usar témpera con poca agua y pocos restos, reutilizar pinceles lavándolos en un recipiente y guardar los retazos. Al final, documenta con una frase qué parte quedó mejor y qué dejarías para mejorar. Reconocer una falla es parte de un trabajo bien hecho.",
    ],
    vocab=[("acabado", "último trabajo sobre el objeto, como pintar o alisar bordes"), ("capa", "una mano de pintura sobre una superficie"), ("arista", "borde que puede pinchar o cortar"), ("ocultar", "tapar algo para que no se vea"), ("secar", "esperar a que la pintura o el pegamento se endurezca")],
    worked=[
        ("Elegir el orden correcto", "Tienes una caja con una unión floja en una esquina. ¿Pintas primero o arreglas primero?", ["Pintar solo tapa la falla.", "La unión seguirá floja.", "Primero la arreglo y compruebo."], "Arreglar la unión primero y después pintar"),
        ("Cuidar un borde que pincha", "Una arista de cartón queda con punta. ¿Qué haces?", ["Una punta puede lastimar.", "La doblo hacia dentro o la cubro con cinta."], "Doblar la punta hacia dentro o cubrirla con cinta"),
    ],
    mistakes=[
        ("Pintar para tapar una unión floja.", "La falla sigue y puede romperse después.", "Repara y comprueba antes de pintar."),
        ("Pintar con una capa muy gruesa.", "Gotea, tarda en secar y arruga el papel.", "Pasa capas finas y deja secar."),
    ],
    R=[
        ("Pintar y alisar bordes, ¿es parte del acabado o de la medición?", "Del acabado", "Es el trabajo final sobre el objeto."),
        ("¿La pintura arregla una unión floja?", "No", "Solo la oculta."),
        ("¿Se usa una capa fina o gruesa de pintura?", "Fina", "Seca mejor y no arruga el papel."),
    ],
    C=[
        ("¿Por qué se revisa el funcionamiento antes de pintar?", "Porque pintar puede ocultar una falla", "Se corrige antes de cubrirla."),
        ("¿Qué se hace con una arista que pincha?", "Se dobla hacia dentro o se cubre con cinta", "Así no lastima."),
        ("¿Qué beneficio ambiental tiene lavar el pincel en un recipiente?", "Se reutiliza el pincel y se usa poca agua", "Evita desechar y gastar de más."),
    ],
    A=[
        ("Tu caja tiene una esquina floja. Pasos: A pintar, B reforzar la esquina con cinta y comprobar. ¿Cuál va primero?", "B", "Se repara antes del acabado."),
        arith("La pintura necesita 15 minutos para secar entre capas. Das 2 capas. ¿Cuántos minutos de secado necesitas en total, si secas después de cada capa?", "15*2", "Se multiplican los minutos por las dos capas."),
        ("Notas que la tapa de la caja no cierra. ¿Aplicas el acabado o corriges?", "Corriges", "El funcionamiento va antes del acabado."),
    ],
    Z=[
        ("Ana dice: «Pinto fuerte esa unión para que nadie vea que quedó mal». ¿Qué le responderías?", "Que debe repararla, porque pintarla solo la oculta", "La falla sigue y puede romperse."),
        ("Entre dos trabajos, uno con una esquina floja bien anotada y reparada y otro con la esquina floja pintada, ¿cuál es mejor?", "El primero", "Reconoció y corrigió la falla."),
    ],
    D=[
        arith("Una caja tiene 6 caras. Si pintas solo 4, ¿cuántas caras quedan sin pintar?", "6-4", "Se restan las pintadas del total."),
        arith("Tienes 3 cajas y cada una lleva 2 capas de pintura. ¿Cuántas capas das en total?", "3*2", "Se multiplican las cajas por las capas de cada una."),
    ],
    ctx=("Pintaste una caja de cartón con témpera. Al secar, notas que una esquina se despegó. Escribe qué harías con ella, qué evitarías hacer y cómo cuidas el ambiente al terminar.", "Volvería a pegar la esquina con cinta, sin pintar encima; evitaría ocultar la falla; lavaría el pincel con poca agua", "Repara, no oculta y cuida el ambiente."),
    sc=[
        ("¿Qué es el acabado?", "El último trabajo sobre el objeto, como pintar o alisar bordes", "Ocurre después de revisar el funcionamiento."),
        ("¿El acabado puede ocultar fallas?", "No debe", "Debe mostrar un trabajo honesto."),
        ("¿Pintas con una capa fina o gruesa?", "Fina", "Seca mejor y queda pareja."),
    ],
    open_task=(
        "Escoge un acabado. Acabado 1: pintar una caja de papel con témpera en dos capas finas. Acabado 2: alisar los bordes de una tira de cartón y cubrir una arista con cinta. Revisa primero el funcionamiento, haz el acabado, deja secar y anota qué quedó bien y una falla que no ocultaste.",
        "Acabado 1: revisé que cierra la tapa; pinté dos capas finas; quedó pareja; una esquina quedó con arrugas y la dejé anotada.",
        ["revisa el funcionamiento antes", "acabado limpio", "no oculta fallas", "anota una mejora"],
        ["objeto con acabado y nota de revisión"],
        ["pintar una falla", "capas muy gruesas"],
        "Pregunta: «¿qué falla ves y qué hiciste con ella?». Si dice que ninguna, pídele observar con calma.",
    ),
    reinforce="Mira un objeto pintado de tu casa y busca una zona donde se nota la pintura gruesa o despareja.",
    extend="Escribe tres cuidados para pintar con témpera de forma segura y cuidando el ambiente.",
)

# ------------------------------------------------------------------ OA 03, clase 5
reg(
    OA3, 5,
    materials="Hoja y lápiz. Los datos del registro están escritos en el cuaderno. Si quieres, usa un objeto que ya hiciste.",
    use="Aprenderé a documentar las decisiones de construcción y a explicar el uso seguro del objeto. Sirve para que otras personas entiendan y usen bien lo que hice.",
    prior=["Sé construir con controles y acabado.", "Sé elegir un material según su función."],
    explain=[
        "Documentar es dejar por escrito lo que hiciste y por qué. Una buena documentación tiene cuatro partes: qué construiste y para quién; qué materiales, herramientas y técnicas usaste; qué decisiones tomaste, con la razón; y qué fallas encontraste y cómo las trataste. Puede ser una ficha corta con dibujos.",
        "Las decisiones se explican con razones comprobables. «Usé cartón porque aguantó las 10 fichas en la prueba» es una razón. «Lo usé porque me gusta» no lo es. También se anotan las medidas finales, para que otra persona pueda repetir el objeto. Si cambiaste algo del plan, anótalo y di por qué.",
        "El uso seguro explica cómo usar el objeto sin riesgos: dónde ponerlo, cuánto peso soporta, qué no hacer y cómo limpiarlo o guardarlo. Por ejemplo: «No apoyar más de 10 fichas; no usar cerca del agua». Por último, escribe cómo cuidas el ambiente: qué reutilizaste, qué sobró y cómo lo separarás.",
    ],
    vocab=[("documentar", "dejar por escrito lo que hiciste y por qué"), ("decisión", "elección entre varias opciones, con una razón"), ("ficha técnica", "hoja corta que describe un objeto y cómo se hizo"), ("uso seguro", "forma de usar el objeto sin riesgos"), ("repetir", "volver a hacer lo mismo siguiendo las instrucciones")],
    worked=[
        ("Escribir una decisión con razón", "Elegiste cartón reutilizado para la base porque aguantó 10 fichas en la prueba. Escribe la decisión con su razón.", ["Decisión: cartón reutilizado para la base.", "Razón: aguantó 10 fichas en la prueba."], "Usé cartón reutilizado para la base porque aguantó 10 fichas en la prueba"),
        ("Escribir una indicación de uso seguro", "Tu soporte aguanta como máximo 10 fichas y no resiste el agua. Escribe una indicación de uso seguro.", ["Incluyo el límite de peso.", "Incluyo qué evitar."], "No poner más de 10 fichas y no usarlo cerca del agua"),
    ],
    mistakes=[
        ("Documentar solo lo que salió bien.", "Otra persona repetirá el error si no lo sabe.", "Anota también las fallas y cómo las trataste."),
        ("Explicar una decisión con «porque me gusta».", "No se puede comprobar.", "Da una razón con datos de la prueba."),
    ],
    R=[
        ("Dejar por escrito lo que hiciste y por qué, ¿es documentar o decorar?", "Documentar", "Esa es la definición."),
        ("Una hoja corta que describe un objeto y cómo se hizo, ¿es una ficha técnica o un boceto?", "Una ficha técnica", "Reúne los datos del objeto."),
        ("¿Se anotan las fallas en la documentación?", "Sí", "Ayudan a no repetirlas."),
    ],
    C=[
        ("¿Por qué se anotan las medidas finales?", "Para que otra persona pueda repetir el objeto", "Sin medidas no se puede repetir."),
        ("¿Cuál es una razón mejor? A «lo hice azul», B «aguantó 10 fichas en las 3 pruebas».", "B", "B se puede comprobar."),
        ("¿Para qué sirve el uso seguro?", "Para usar el objeto sin riesgos", "Dice qué hacer y qué evitar."),
    ],
    A=[
        ("Tu atril soporta 3 hojas y no debe mojarse. Escribe una indicación de uso seguro.", "No poner más de 3 hojas y no usarlo cerca del agua", "Incluye el límite y qué evitar."),
        ("En tu ficha escribiste: «cartón reutilizado», «tijeras de punta roma», «cortar» y «cinta». ¿Cuántos de esos cuatro son materiales?", "2", "El cartón reutilizado y la cinta son materiales; las tijeras son herramienta y cortar es técnica."),
        ("Cambiaste el cordel por cinta porque faltó cordel. ¿Debes anotarlo?", "Sí", "Los cambios al plan se documentan con su razón."),
    ],
    Z=[
        ("Una compañera escribe «hice un buen soporte». ¿Qué datos le faltan para que sea una documentación?", "Materiales, decisiones con razón, medidas y fallas", "Esa frase no dice cómo se hizo ni se puede repetir."),
        ("Entre «no usar con agua» y «tener cuidado», ¿cuál indicación de uso seguro es más clara?", "No usar con agua", "Dice exactamente qué evitar."),
    ],
    D=[
        arith("Tu ficha tiene 4 partes y ya completaste 3. ¿Cuántas faltan?", "4-3", "Se restan las completas del total."),
        arith("Documentaste 5 decisiones y 2 no tenían razón. ¿Cuántas decisiones sí tenían razón?", "5-2", "Se restan las que no tienen razón del total."),
    ],
    ctx=("Construiste un porta-lápices de 10 cm de largo, 6 cm de ancho y 12 cm de alto con cartón reutilizado y cinta. Guarda 6 lápices sin caerse. Escribe una ficha corta con: qué es, materiales, una decisión con razón y una indicación de uso seguro.", "Porta-lápices de 10 × 6 × 12 cm para 6 lápices. Materiales: cartón reutilizado y cinta. Usé cartón porque aguantó los 6 lápices. No poner más de 6 lápices ni usarlo cerca del agua", "Cubre las cuatro partes pedidas."),
    sc=[
        ("¿Qué es documentar?", "Dejar por escrito lo que hiciste y por qué", "Sirve para que otros lo entiendan."),
        ("¿Cuál es una buena razón?", "Una que se pueda comprobar con datos", "Una razón con datos se puede verificar."),
        ("¿Qué incluye el uso seguro?", "Dónde ponerlo, cuánto soporta y qué no hacer", "Así se evitan los riesgos."),
    ],
    open_task=(
        "Escoge un objeto de los que hiciste en las clases o uno de estos casos: Caso 1: soporte de cartón para 10 fichas (base de 20 cm). Caso 2: caja de papel para 8 clips. Escribe una ficha técnica con cuatro partes: qué es y para quién, materiales y técnicas, una decisión con razón y una falla que encontraste, y una indicación de uso seguro con el cuidado del ambiente.",
        "Caso 1: soporte de cartón para 10 fichas, para Pía. Materiales: cartón reutilizado y cinta. Decisión: base de 20 cm porque con 18 cm se inclinó. Falla: una esquina floja que reforcé. Uso seguro: no más de 10 fichas.",
        ["ficha con las cuatro partes", "decisión con razón comprobable", "anota una falla", "indica uso seguro"],
        ["ficha técnica escrita"],
        ["razón sin datos", "no anotar fallas"],
        "Pregunta: «¿qué dato de la prueba apoya tu decisión?». Si no hay dato, pídele volver a la prueba.",
    ),
    reinforce="Explica a una persona de tu casa cómo usar con seguridad un objeto que tengan en la cocina.",
    extend="Escribe una ficha técnica de tres líneas de un objeto de tu sala.",
)
