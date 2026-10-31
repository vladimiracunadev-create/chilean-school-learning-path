"""Cuaderno del estudiante, 7.º básico Tecnología: OA 05 (contraste de soluciones tecnológicas y contextos), clases 1 a 4.

Los casos son ejemplos generales o inventados para practicar (sin marcas ni fechas); los datos numéricos son de ejemplo y se rotulan así.
Seguridad: nada que implique herramientas con filo, fuego o electricidad de red; las tareas son de lectura, comparación y escritura.
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_content_te7_a import reg
from student_lessons import arith

OA5 = "TE07 OA 05"

# ------------------------------------------------------------------ OA 05, clase 1
reg(
    OA5, 1,
    materials="Hoja, lápiz y los casos escritos en este cuaderno. Si quieres, una persona de tu casa para conversar sobre objetos reparados o adaptados.",
    use="Aprenderé a identificar la necesidad a la que responde una solución que ya existe y a clasificarla como reparación, adaptación o mejora. Sirve para entender por qué existen los objetos que usamos.",
    prior=["Sé distinguir reparar, adaptar y mejorar.", "Sé que una necesidad dice qué se debe lograr.", "Sé que un usuario es quien usa la solución."],
    explain=[
        "Muchos objetos que usamos nacieron como respuesta a una necesidad. Para entender una solución existente conviene hacerse tres preguntas: ¿quién la usa?, ¿qué problema o necesidad resolvía? y ¿es una reparación, una adaptación o una mejora? Por ejemplo, los lentes responden a la necesidad de ver bien a quienes tienen dificultades de visión: modifican la forma en que llega la luz al ojo.",
        "Algunas soluciones conocidas son la rampa de acceso (adapta un lugar para quien no puede subir escalones), los subtítulos en un video (adaptan el contenido para personas sordas o con sonido apagado), el remiendo de una prenda (repara un hoyo), el mango ancho de un cubierto (adapta el objeto a una mano con poca fuerza) y los cambios de velocidad de una bicicleta (mejoran el esfuerzo en subidas y bajadas).",
        "Una misma solución puede responder a más de una necesidad. Los subtítulos ayudan a personas sordas, pero también a quien está en un lugar ruidoso. Por eso al estudiar una solución se anotan la necesidad principal y otros usos. Una solución no es buena en sí misma: lo es en relación con la necesidad a la que responde.",
    ],
    vocab=[("solución existente", "objeto o sistema que ya fue creado y se usa"), ("necesidad principal", "problema principal que resolvía la solución"), ("rampa", "superficie inclinada que permite subir o bajar sin escalones"), ("subtítulos", "texto escrito de lo que se dice en un video"), ("remiendo", "arreglo de un hoyo o rotura en una tela")],
    worked=[
        ("Reconocer la necesidad y el tipo", "Una rampa se instala en la entrada de una biblioteca que solo tenía escalones. ¿Qué necesidad resolvía y qué tipo de solución es?", ["Resuelve que una persona en silla de ruedas, con bastón o con un coche de bebé no podía entrar.", "No arregla algo roto; modifica el lugar para otras personas: es una adaptación."], "Necesidad: poder entrar sin escalones. Tipo: adaptación"),
        ("Reconocer otros usos", "Los subtítulos nacieron para quien no escucha. ¿Quién más se beneficia?", ["Pienso en situaciones en que el sonido no sirve.", "Una persona en un lugar ruidoso o con el sonido apagado también los lee."], "Quien está en un lugar ruidoso o sin sonido"),
    ],
    mistakes=[
        ("Pensar que una solución existente siempre sirve para todos los usuarios.", "Cada solución responde a una necesidad concreta.", "Pregunta «¿para quién y para qué se creó?»."),
        ("Clasificar un mango ancho como reparación.", "El cubierto no estaba roto; se modificó para otra mano.", "Si el objeto se modifica para otro usuario, es adaptación."),
    ],
    R=[
        ("Un remiendo en un pantalón roto, ¿es reparar, adaptar o mejorar?", "Reparar", "Arregla algo dañado."),
        ("Un mango ancho en un cubierto para una mano con poca fuerza, ¿es reparar, adaptar o mejorar?", "Adaptar", "Se modifica para otro usuario."),
        ("Los cambios de velocidad de una bicicleta, ¿son reparar, adaptar o mejorar?", "Mejorar", "Hacen que algo que ya funcionaba sirva mejor en subidas."),
    ],
    C=[
        ("¿A qué necesidad responde principalmente una rampa de acceso? A entrar a un lugar sin usar escalones, B evitar que se resbale quien sube los escalones.", "A", "Una rampa se creó para permitir el acceso sin escalones."),
        ("¿Quién se beneficia de los subtítulos además de las personas sordas? A quien ve un video en un lugar ruidoso, B quien escucha un audio sin imagen.", "A", "Pueden leer lo que no alcanzan a oír."),
        ("Un compañero dice: «Las soluciones son buenas o malas en sí mismas». ¿Qué le respondes?", "Que son buenas según la necesidad a la que responden", "Una solución se evalúa en relación con su necesidad."),
    ],
    A=[
        arith("En una lista hay 10 soluciones: 4 son reparaciones, 3 son adaptaciones y el resto mejoras. ¿Cuántas son mejoras?", "10-4-3", "Se restan las reparaciones y adaptaciones del total.", " mejoras"),
        ("Clasifica en orden con R, AD o M: (1) un parche en una bicicleta con rueda pinchada, (2) un asiento más alto para que lo use una persona de mayor estatura, (3) un manubrio más cómodo que mantiene el mismo funcionamiento.", "1 R, 2 AD, 3 M", "El parche arregla, el asiento se adapta a otro usuario y el manubrio mejora el uso."),
        ("¿Qué necesidad resuelve un portón con un asa a la altura de la cintura de una persona en silla de ruedas? A que quien está sentada pueda abrirlo sola, B que el portón dure más tiempo sin oxidarse.", "A", "El asa adapta el portón a otro usuario."),
    ],
    Z=[
        ("Alguien dice que los lentes solo sirven a personas mayores. Otra persona explica que sirven a cualquiera con dificultad de visión. ¿Quién identifica mejor la necesidad?", "La segunda", "La necesidad es la dificultad de visión, no la edad."),
        ("Una pared tiene un hoyo y se tapa con una placa de madera. Otra pared sin hoyos se cubre con una placa para que no entre el frío. ¿Cuál es reparación y cuál es mejora?", "La del hoyo es reparación; la del frío es mejora", "Una arregla un daño y la otra hace que algo que funciona sirva mejor."),
    ],
    D=[
        arith("Un registro tiene 24 soluciones: 6 son reparaciones y el doble de ese número son adaptaciones. ¿Cuántas son mejoras?", "24-6-6*2", "Las adaptaciones son 6 × 2 = 12 y las demás son mejoras.", " mejoras"),
        ("Una escuela instala una rampa y también barandas. La rampa es para quien no puede subir escalones; las barandas, para que nadie caiga. ¿Qué solución responde a la accesibilidad?", "La rampa", "La baranda responde a la seguridad."),
    ],
    ctx=("Una vecina que usa bastón no puede subir los 3 escalones de la entrada de un edificio. La comunidad instala una rampa. Escribe quién es el usuario, la necesidad, el tipo de solución y quién más se beneficia.", "Usuaria: la vecina con bastón. Necesidad: entrar sin subir escalones. Tipo: adaptación. También se benefician quienes llevan un coche o bultos pesados", "Se nombra usuario, necesidad, tipo y otros beneficiarios."),
    sc=[
        ("¿Qué tres preguntas ayudan a entender una solución existente?", "Quién la usa, qué necesidad resolvía y qué tipo es", "Son las preguntas de la clase."),
        ("¿Un mango ancho es reparar, adaptar o mejorar?", "Adaptar", "Modifica el objeto para otra mano."),
        ("¿Una solución puede servir a más de un usuario?", "Sí", "Los subtítulos sirven a más de un grupo."),
    ],
    open_task=(
        "Escoge una solución. Solución 1: un remiendo en una mochila. Solución 2: subtítulos en un video de la clase. Solución 3: un asiento de bus con un espacio libre para una silla de ruedas. Escribe quién la usa, qué necesidad resolvía, de qué tipo es (reparar, adaptar o mejorar), quién más podría beneficiarse y un posible problema que no resuelve.",
        "Solución 3: usuaria: una persona en silla de ruedas. Necesidad: viajar en bus sin bajarse de la silla. Tipo: adaptación. También sirve a quien lleva un coche. No resuelve cómo subir al bus si no hay rampa",
        ["nombra al usuario", "dice la necesidad", "clasifica el tipo", "identifica otro beneficiario o un límite"],
        ["hoja con ficha de la solución"],
        ["confundir adaptar con reparar", "describir la solución en vez de la necesidad"],
        "Pregunta: «¿para quién se creó y qué problema tenía antes?». Si solo describe el objeto, pídele cambiar de enfoque.",
    ),
    reinforce="Elige un objeto de tu casa y anota para qué problema se creó y de qué tipo de solución es.",
    extend="Explica por qué una solución puede resolver una necesidad y crear otra, con un ejemplo.",
)

# ------------------------------------------------------------------ OA 05, clase 2
reg(
    OA5, 2,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a describir el contexto en que se desarrolló una solución —lugar, época, recursos y costumbres— y a explicar cómo influyó en su forma. Sirve para entender que una misma necesidad se resuelve distinto en lugares y momentos distintos.",
    prior=["Sé identificar la necesidad de una solución existente.", "Sé que hay restricciones, como dinero o materiales.", "Sé distinguir reparar, adaptar y mejorar."],
    explain=[
        "El contexto es todo lo que rodea a una necesidad: el lugar donde ocurre, la época, los recursos disponibles y las costumbres de las personas. Dos soluciones para la misma necesidad pueden ser muy distintas porque sus contextos son distintos. Para describir un contexto se responden cuatro preguntas: ¿dónde?, ¿cuándo?, ¿con qué recursos? y ¿con qué costumbres o reglas?",
        "Ejemplo: mantener frescos los alimentos. En un lugar con electricidad y dinero, se usa un refrigerador. En un lugar cálido y seco sin electricidad, una solución posible es una vasija de barro dentro de otra más grande, con arena húmeda entre ambas, porque al evaporarse el agua las enfría. Misma necesidad, contextos distintos, soluciones distintas.",
        "El contexto también explica por qué se repara o se reemplaza. Donde los materiales son caros o escasos, se repara y se reutiliza. Donde comprar uno nuevo es fácil y barato, se tiende a reemplazar. Cambiar la solución a otro contexto exige adaptarla: lo que funciona en una región fría quizás no funciona igual en una cálida. Describir el contexto evita juzgar una solución como si hubiera sido pensada para otro lugar.",
    ],
    vocab=[("contexto", "lugar, época, recursos y costumbres que rodean una necesidad"), ("recurso", "material, energía, dinero o conocimiento disponible"), ("evaporación", "paso del agua líquida a vapor, que enfría la superficie"), ("escasez", "falta de algo que se necesita"), ("transferir", "llevar una solución a otro contexto")],
    worked=[
        ("Describir un contexto", "Una comunidad de una zona fría y lluviosa necesita secar su ropa. ¿Cómo describes su contexto?", ["Lugar: zona fría y lluviosa.", "Recursos y costumbres: poco sol para secar afuera, se seca bajo techo, por ejemplo cerca de una estufa. Época: no se indica."], "Zona fría y lluviosa, con poco sol; la ropa se seca bajo techo"),
        ("Explicar por qué una solución cambia", "En una zona con poca agua se riega con una manguera que gotea cerca de las raíces. ¿Por qué no se riega a baldazos?", ["El contexto tiene escasez de agua.", "Regar gota a gota evita malgastarla."], "Porque hay escasez de agua y gotear a las raíces la aprovecha mejor"),
    ],
    mistakes=[
        ("Juzgar una solución sin conocer su contexto.", "Se piensa que una solución es mala porque no funcionaría en otro lugar.", "Primero describe dónde, cuándo y con qué recursos se creó."),
        ("Creer que una solución puede llevarse a otro lugar sin cambios.", "El contexto nuevo puede tener otro clima, costumbres o recursos.", "Revisa qué adaptar antes de transferirla."),
    ],
    R=[
        ("Los recursos disponibles de un lugar, ¿son parte del contexto o de la solución?", "Del contexto", "El contexto incluye lo que hay disponible."),
        ("¿Cuántas preguntas se usan en la clase para describir el contexto?", "Cuatro", "Dónde, cuándo, con qué recursos y con qué costumbres."),
        ("Donde un material escasea, ¿se tiende más a reparar o a botar?", "A reparar", "Reparar ahorra el material escaso."),
    ],
    C=[
        ("¿Por qué una vasija dentro de otra con arena húmeda enfría? A porque el agua al evaporarse enfría, B porque la arena guarda calor.", "A", "La evaporación quita calor de la superficie."),
        ("Un grupo critica una solución diciendo que «no funciona en mi barrio». ¿Qué debería revisar primero?", "El contexto en que fue creada", "Quizás fue pensada para otras condiciones."),
        ("Una comunidad tiene mucho sol y poco dinero. ¿Cuál solución encaja mejor para secar ropa? A colgarla al sol, B comprar una máquina eléctrica.", "A", "Aprovecha un recurso disponible y evita un gasto."),
    ],
    A=[
        arith("En una comunidad, 18 de 30 familias reparan objetos en vez de botarlos. ¿Cuántas familias no los reparan?", "30-18", "Se restan las que reparan del total.", " familias"),
        arith("Una solución gasta 20 litros de agua por riego y otra gasta 5 litros. ¿Cuántos litros ahorra la segunda en 6 riegos?", "(20-5)*6", "Se calcula el ahorro por riego y se multiplica por los riegos.", " litros"),
        ("En un lugar con lluvias frecuentes y techos grandes, ¿qué solución encaja mejor para tener agua? A recolectar agua del techo, B traer agua desde lejos todos los días.", "A", "Aprovecha el recurso disponible."),
    ],
    Z=[
        ("Una solución funciona bien en una zona cálida. Se quiere usar en una zona fría y húmeda. ¿Qué conviene hacer?", "Revisar qué adaptar al clima nuevo", "El contexto cambió y la solución puede necesitar cambios."),
        ("Beto dice: «En el pasado se reparaba más porque la gente era distinta». Elena dice: «Se reparaba más donde los materiales eran escasos o caros». ¿Quién explica mejor con el contexto?", "Elena", "Explica con recursos, no con juicios sobre las personas."),
    ],
    D=[
        arith("Una familia gasta $1.500 en reparar un objeto que reemplazarlo costaría $6.000. ¿Cuánto dinero ahorra al reparar?", "6000-1500", "Se resta el costo de la reparación del de reemplazo.", " pesos"),
        ("Una comunidad dispone de 40 botellas plásticas limpias y necesita 50 para construir una pared de botellas. ¿Cuántas botellas debe conseguir aún?", "10", "Se resta lo que tiene de lo que necesita."),
    ],
    ctx=("En una zona cálida y seca, una escuela tiene poco dinero y mucha arena. Necesita mantener frescas las botellas de agua de 40 estudiantes. Escribe el contexto con las cuatro preguntas y una solución que encaje.", "Dónde: zona cálida y seca. Cuándo: hoy. Recursos: poco dinero, mucha arena y algo de agua. Costumbres: tomar agua fresca en el recreo. Solución: una vasija dentro de otra con arena húmeda", "Se describe el contexto y se elige una solución que usa sus recursos."),
    sc=[
        ("En Tecnología: ¿Qué es el contexto?", "El lugar, la época, los recursos y las costumbres que rodean una necesidad", "Es la definición de la clase."),
        ("¿Una misma necesidad puede tener soluciones distintas?", "Sí", "Cambia con el contexto."),
        ("¿Dónde se tiende más a reparar?", "Donde los materiales escasean o son caros", "Reparar ahorra recursos."),
    ],
    open_task=(
        "Escoge una necesidad. Necesidad 1: mantener secas las botas en un lugar de mucha lluvia y poco espacio. Necesidad 2: dar sombra a un patio de escuela en una zona muy soleada, con poco dinero. Escribe el contexto con las cuatro preguntas, dos soluciones posibles que encajen y una solución que no encajaría con una razón basada en el contexto.",
        "Necesidad 2: dónde: zona soleada. Cuándo: verano. Recursos: poco dinero, telas viejas. Costumbres: recreos al aire libre. Soluciones: toldos de tela reutilizada o plantar árboles de sombra. No encajaría: una gran cubierta de metal cara, por el dinero",
        ["describe el contexto con las cuatro preguntas", "propone dos soluciones que encajan", "explica una solución que no encaja", "usa el contexto como razón"],
        ["hoja con contexto y soluciones"],
        ["proponer soluciones sin mirar los recursos", "juzgar a las personas en vez del contexto"],
        "Pregunta: «¿con qué recursos cuenta esa comunidad?». Si no lo menciona, pídele volver al contexto.",
    ),
    reinforce="Describe el contexto de tu casa (lugar, recursos y costumbres) para guardar zapatos.",
    extend="Explica por qué una solución creada hace muchos años puede seguir siendo útil hoy si el contexto es parecido.",
)

# ------------------------------------------------------------------ OA 05, clase 3
reg(
    OA5, 3,
    materials="Hoja, lápiz y las tablas escritas en este cuaderno.",
    use="Aprenderé a contrastar dos soluciones con una tabla comparativa de necesidad, contexto, costo, tiempo y durabilidad. Sirve para ver semejanzas y diferencias con orden y sacar conclusiones con datos.",
    prior=["Sé identificar necesidad y contexto.", "Sé calcular costo por mes.", "Sé leer una tabla."],
    explain=[
        "Contrastar es poner dos soluciones una al lado de la otra para ver en qué se parecen y en qué se diferencian. Se usa una tabla comparativa con filas para los aspectos que se comparan: la necesidad a la que responden, el contexto, el tipo de solución, los materiales, el costo, el tiempo de trabajo, la durabilidad y el efecto en el ambiente.",
        "Para comparar con justicia, ambos casos se describen con los mismos aspectos y las mismas unidades. Los datos numéricos se pueden convertir a una medida común, como el costo por mes: costo total dividido entre los meses que dura. Después se escriben las semejanzas (lo que tienen igual) y las diferencias (lo que cambia), y se explica por qué cambian a partir del contexto.",
        "Contrastar no es decidir cuál es mejor en general. Una solución puede ser mejor en un contexto y peor en otro. Una buena conclusión dice: «En este contexto conviene la solución A porque…, y en este otro, la B porque…». Los datos de los casos de esta clase son de ejemplo, para practicar.",
    ],
    vocab=[("contrastar", "comparar para encontrar semejanzas y diferencias"), ("tabla comparativa", "tabla con aspectos en filas y soluciones en columnas"), ("semejanza", "característica que tienen igual"), ("diferencia", "característica que cambia entre dos casos"), ("aspecto", "característica que se compara")],
    worked=[
        ("Leer una tabla comparativa", "Solución A (remendar un bolso): costo $1.000, dura 10 meses. Solución B (comprar un bolso nuevo): costo $12.000, dura 24 meses. ¿Cuál cuesta menos por mes?", ["A: 1.000 ÷ 10 = 100 por mes.", "B: 12.000 ÷ 24 = 500 por mes."], "A cuesta menos por mes: $100 contra $500"),
        ("Escribir semejanza y diferencia", "A y B resuelven la necesidad de llevar útiles. A repara y B reemplaza. ¿Cuál es una semejanza y cuál una diferencia?", ["Semejanza: ambas responden a la necesidad de llevar útiles.", "Diferencia: A conserva el bolso y B lo reemplaza, con distinto costo."], "Semejanza: misma necesidad. Diferencia: A conserva el bolso y B lo reemplaza"),
    ],
    mistakes=[
        ("Comparar un costo total con un costo por mes como si fueran lo mismo.", "Las unidades no coinciden y la comparación no es justa.", "Convierte todo a la misma medida, como costo por mes."),
        ("Concluir que una solución es la mejor en todos los lugares.", "El contexto cambia lo que conviene.", "Escribe la conclusión para cada contexto."),
    ],
    R=[
        ("Lo que dos soluciones tienen igual, ¿es una semejanza o una diferencia?", "Una semejanza", "Es lo que coincide."),
        ("¿Una tabla comparativa usa los mismos aspectos para las dos soluciones o aspectos distintos?", "Los mismos", "Así la comparación es justa."),
        ("El costo total dividido entre los meses de uso, ¿es el costo por mes o el costo por uso diario?", "El costo por mes", "Se divide entre meses."),
    ],
    C=[
        ("¿Para qué se convierte el costo a una medida común? A para comparar con justicia, B para que el costo total sea menor en las dos.", "A", "La medida común permite comparar."),
        ("Una solución cuesta menos pero dura menos. ¿Qué haces para comparar? A calcular el costo por mes de cada una, B elegir la más barata sin calcular.", "A", "Así se incluye la durabilidad."),
        ("Un grupo dice que la solución A es mejor en todos los contextos porque es más barata. ¿Qué le falta analizar?", "El contexto", "Lo que conviene cambia con el lugar y los recursos."),
    ],
    A=[
        arith("Solución X cuesta $3.000 y dura 15 meses. ¿Cuánto cuesta por mes?", "3000//15", "Se divide el costo entre los meses.", " pesos"),
        arith("Solución Y cuesta $8.000 y dura 20 meses. ¿Cuánto cuesta por mes?", "8000//20", "Se divide el costo entre los meses.", " pesos"),
        ("Tabla (de ejemplo): X mide 20 cm de ancho y Y mide 30 cm de ancho. El espacio libre es de 25 cm. ¿Cuál cabe?", "X", "Y supera los 25 cm."),
    ],
    Z=[
        ("Solución A repara en 2 horas y cuesta $1.000. Solución B reemplaza en 20 minutos y cuesta $8.000. En un lugar con poco dinero y mucho tiempo libre, ¿cuál encaja mejor?", "A", "Cuesta menos y el tiempo no es un problema."),
        ("Solución A repara en 2 horas y cuesta $1.000. Solución B reemplaza en 20 minutos y cuesta $8.000. En un taller con poco tiempo y bastante dinero, ¿cuál encaja mejor?", "B", "Se hace más rápido y el dinero alcanza."),
    ],
    D=[
        arith("A dura 12 meses y cuesta $2.400; B dura 36 meses y cuesta $9.000. ¿Cuántos pesos más por mes cuesta B que A?", "9000//36-2400//12", "B cuesta $250 por mes y A $200 por mes.", " pesos"),
        ("La tabla (de ejemplo) dice: A se hace con material reutilizado y B con material nuevo. Ambas duran lo mismo y cuestan lo mismo. ¿Cuál tiene menor efecto sobre el ambiente?", "A", "Reutilizar evita producir y botar material nuevo."),
    ],
    ctx=("Para guardar los zapatos de una familia hay dos soluciones: arreglar un mueble viejo (cuesta $2.000 y dura 20 meses) o comprar uno nuevo ($10.000 y dura 40 meses). Calcula el costo por mes de cada una y escribe una semejanza y una diferencia.", "Viejo arreglado: $100 por mes. Nuevo: $250 por mes. Semejanza: ambos guardan zapatos. Diferencia: uno conserva el mueble y el otro lo reemplaza", "Se calcula 2.000 ÷ 20 = 100 y 10.000 ÷ 40 = 250."),
    sc=[
        ("En Tecnología: ¿Qué es contrastar?", "Comparar para encontrar semejanzas y diferencias", "Es la definición de la clase."),
        ("¿Por qué usar una medida común como el costo por mes?", "Para comparar con justicia", "Las unidades coinciden."),
        ("¿Una solución puede ser mejor en un contexto y peor en otro?", "Sí", "El contexto cambia lo que conviene."),
    ],
    open_task=(
        "Escoge un contraste. Contraste 1: arreglar una silla (cuesta $2.500, dura 10 meses, se hace en 90 minutos) frente a comprar una nueva ($15.000, dura 30 meses, se compra en 20 minutos). Contraste 2: tapar un hoyo de una mochila con un parche ($800, dura 8 meses) frente a una mochila nueva ($16.000, dura 32 meses). Calcula el costo por mes, completa una tabla con necesidad, contexto, costo por mes y efecto ambiental, y escribe una semejanza, una diferencia y una conclusión por contexto.",
        "Contraste 2: parche $100 por mes, nueva $500 por mes. Semejanza: ambos permiten llevar los útiles. Diferencia: uno conserva la mochila y el otro la reemplaza. Conclusión: con poco dinero conviene el parche; con mucho dinero y una mochila muy dañada, la nueva",
        ["calcula el costo por mes", "tabla con aspectos iguales", "semejanza y diferencia", "conclusión por contexto"],
        ["hoja con tabla y conclusión"],
        ["comparar unidades distintas", "concluir sin mirar el contexto"],
        "Pregunta: «¿en qué contexto conviene cada una?». Si da una sola respuesta, pídele otro contexto.",
    ),
    reinforce="Compara dos objetos de tu casa que sirvan para lo mismo y escribe una semejanza y una diferencia.",
    extend="Explica por qué contrastar con datos es más justo que decir «esta es mejor».",
)

# ------------------------------------------------------------------ OA 05, clase 4
reg(
    OA5, 4,
    materials="Hoja, lápiz y los casos escritos en este cuaderno. Si quieres, una persona mayor de tu entorno para conversar.",
    use="Aprenderé a investigar cómo se resolvía una necesidad en otro tiempo o lugar, a contrastarlo con una solución actual y a decidir qué se podría adaptar a mi propio contexto. Sirve para aprender de otras soluciones sin copiarlas.",
    prior=["Sé contrastar con una tabla.", "Sé describir un contexto.", "Sé anotar fuentes."],
    explain=[
        "Para investigar una solución existente puedes conversar con una persona mayor, leer un texto o mirar un objeto. Antes de preguntar, prepara preguntas abiertas: ¿qué problema había?, ¿cómo lo resolvían?, ¿con qué materiales?, ¿cuánto duraba?, ¿qué haría distinto hoy? Pide permiso, escucha con respeto y anota el nombre de la fuente solo si la persona está de acuerdo.",
        "Luego contrastas la solución de antes con la de hoy en una tabla: necesidad, contexto, materiales, costo, duración y efecto en el ambiente. Fíjate en qué cambió y por qué. A veces cambió el contexto: hay otros materiales, otra energía o otras costumbres. A veces la necesidad es la misma, pero la solución antigua sigue siendo válida.",
        "El último paso es decidir qué se puede transferir a tu contexto. No se copia todo: se adapta lo que sirve y se cambia lo que no. Por ejemplo, la costumbre de remendar prendas puede servir hoy para gastar menos y botar menos, aunque se haga con otros materiales. Tu conclusión debe decir qué conservarías, qué cambiarías y por qué.",
    ],
    vocab=[("transferir", "llevar una idea o solución a otro contexto"), ("conservar", "mantener algo que sigue sirviendo"), ("fuente oral", "persona que cuenta lo que sabe o vivió"), ("pregunta abierta", "pregunta que obliga a explicar"), ("patrimonio", "conocimientos y objetos que se heredan y se cuidan")],
    worked=[
        ("Decidir qué conservar y qué cambiar", "Antes, una familia remendaba la ropa con hilo y aguja para que durara más. Hoy tiene poco tiempo. ¿Qué puede conservar y qué cambiar?", ["Conserva la idea de reparar para gastar menos y botar menos.", "Cambia el tiempo: remienda solo lo que se rompe y usa parches rápidos."], "Conserva reparar y cambia el tiempo usando remiendos rápidos"),
        ("Preparar preguntas abiertas", "Quieres saber cómo se guardaban los alimentos antes de los refrigeradores. ¿Cuál es una pregunta abierta?", ["Una pregunta abierta no se responde con sí o no.", "«¿Cómo guardaban los alimentos para que duraran más días?»."], "«¿Cómo guardaban los alimentos para que duraran más días?»"),
    ],
    mistakes=[
        ("Copiar una solución antigua sin revisar si el contexto cambió.", "Pueden faltar los materiales o el tiempo.", "Revisa qué se puede adaptar al contexto actual."),
        ("Pensar que lo antiguo siempre es peor o siempre es mejor.", "Cada solución sirvió a su contexto.", "Compara con criterios y datos."),
    ],
    R=[
        ("«¿Cómo lo resolvían?», ¿es una pregunta abierta o de sí o no?", "Abierta", "Pide explicar con detalle."),
        ("Antes de entrevistar, ¿pides permiso o preguntas sin avisar?", "Pido permiso", "Se respeta a la persona."),
        ("Llevar una solución a otro contexto, ¿es transferir o conservar?", "Transferir", "Es la definición de la clase."),
    ],
    C=[
        ("¿Qué hace una persona que adapta una solución antigua? A conserva lo que sirve y cambia lo que ya no, B la copia igual.", "A", "Adaptar es mantener y cambiar con criterio."),
        ("¿Qué pregunta es mejor para una entrevista? A «¿qué problema había y cómo lo resolvían?», B «¿le gustaba?».", "A", "A entrega información; B se responde con una palabra."),
        ("Una persona no quiere que anotes su nombre. ¿Qué haces?", "No lo anoto", "Se respeta su decisión."),
    ],
    A=[
        arith("En una tabla comparativa hay 5 aspectos por cada una de 2 soluciones. ¿Cuántas casillas hay que completar?", "5*2", "Se multiplican los aspectos por las soluciones.", " casillas"),
        arith("De 8 preguntas preparadas para una entrevista, 3 se responden con sí o no. ¿Cuántas son abiertas?", "8-3", "Se restan las cerradas del total.", " preguntas"),
        ("Antes se guardaban frutas al fresco, en un lugar sombreado. Hoy se usa un refrigerador. ¿Qué cambió principalmente? A el contexto y los recursos disponibles, B la necesidad de conservar alimentos.", "A", "La necesidad es la misma; cambiaron los recursos."),
    ],
    Z=[
        ("Dani dice: «Remendar es de antes, hoy no sirve». Elena dice: «Remendar sigue sirviendo para botar menos ropa». ¿Quién argumenta con el contexto actual?", "Elena", "Usa el efecto ambiental, que hoy sigue siendo importante."),
        ("Una solución antigua usaba un material que hoy es muy caro. ¿Qué puedes hacer para transferirla?", "Buscar un material parecido y más barato", "Se adapta lo que cambió y se conserva la idea."),
    ],
    D=[
        arith("Una persona mayor cuenta que arreglar un objeto tomaba 2 horas, y hoy un taller lo hace en 40 minutos (datos de ejemplo). ¿Cuántos minutos menos tarda hoy?", "2*60-40", "Se pasan las 2 horas a minutos y se resta.", " minutos"),
        ("De 12 objetos de una casa, 4 fueron reparados al menos una vez. ¿Qué parte de los objetos no fueron reparados?", "8 de 12", "Se restan los reparados del total."),
    ],
    ctx=("Conversas con una persona mayor de tu entorno sobre cómo se arreglaban antes los zapatos y ahora. Escribe dos preguntas abiertas, una semejanza y una diferencia entre antes y hoy (con datos de ejemplo) y qué conservarías.", "Preguntas: «¿Cómo arreglaban los zapatos?» y «¿Cuánto tiempo duraban?». Semejanza: se busca que duren más. Diferencia: antes se arreglaban a mano y hoy hay más talleres. Conservaría la idea de reparar", "Dos preguntas abiertas, una semejanza, una diferencia y una conclusión."),
    sc=[
        ("¿Qué haces antes de entrevistar a una persona?", "Preparar preguntas abiertas y pedir permiso", "Se respeta a la persona."),
        ("¿Qué conclusión se espera al final?", "Qué conservaría, qué cambiaría y por qué", "Es lo que se transfiere al contexto propio."),
        ("¿Lo antiguo es siempre peor?", "No", "Cada solución sirvió a su contexto."),
    ],
    open_task=(
        "Escoge una necesidad. Necesidad 1: guardar alimentos para que duren. Necesidad 2: llevar agua a un lugar lejos de la casa. Necesidad 3: abrigarse del frío sin gastar mucha energía. Escribe tres preguntas abiertas para una persona mayor, una tabla de contraste con antes y hoy (necesidad, contexto, materiales, costo aproximado y efecto ambiental) usando los datos que ella te dé o ejemplos que inventes y rotules como «de ejemplo», y una conclusión con lo que conservarías y cambiarías.",
        "Necesidad 1: preguntas: ¿cómo guardaban los alimentos?, ¿cuánto duraban?, ¿qué materiales usaban? Tabla (de ejemplo): antes: despensa fresca, sin gasto de energía; hoy: refrigerador, con gasto de energía. Conclusión: conservaría guardar en lugares frescos lo que no necesita frío",
        ["tres preguntas abiertas", "tabla con aspectos iguales", "datos rotulados como de ejemplo si son inventados", "conclusión con qué conservar y cambiar"],
        ["hoja con preguntas, tabla y conclusión"],
        ["inventar datos sin decir que son de ejemplo", "copiar la solución antigua sin adaptarla"],
        "Pregunta: «¿qué conservarías y por qué?». Si dice «todo», pídele revisar qué cambió en el contexto.",
    ),
    reinforce="Pregunta a una persona de tu entorno cómo se arreglaba algún objeto cuando ella era joven y anota la respuesta en tres líneas.",
    extend="Explica una solución antigua que podría ayudar hoy a botar menos residuos y qué adaptarías.",
)
