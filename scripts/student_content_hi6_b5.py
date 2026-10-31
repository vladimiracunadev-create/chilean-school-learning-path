"""Cuaderno del estudiante, 6.º básico Historia, Geografía y Ciencias Sociales: OA 20 (actitudes cívicas) y OA 21 (trabajo en equipo)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA20, OA21 = "HI06 OA 20", "HI06 OA 21"

# ================================================================ OA 20 · clase 1
lesson(
    OA20, 1,
    "Aprenderé a reconocer las cuatro actitudes cívicas, respeto, buena convivencia, honestidad y responsabilidad, y cuidado del patrimonio y del medioambiente, y a ubicarlas en la casa, la escuela y el barrio. Sirve para saber cómo actuar cada día como ciudadano.",
    ["Sé que los derechos generan deberes.", "Sé que el bien común ayuda a que todos vivamos bien."],
    [
        "Una actitud cívica es una forma de actuar que ayuda a vivir bien con los demás y a cuidar lo que es de todos. Hay cuatro grandes grupos. Respetar a todas las personas: tratar a todos como iguales en derechos y escuchar opiniones distintas. Contribuir a la buena convivencia: dialogar, proponer soluciones, llegar a acuerdos y cooperar. Actuar con honestidad y responsabilidad: decir la verdad, cumplir lo que prometimos y no copiar ni plagiar. Cuidar el patrimonio y el medioambiente: reciclar y ahorrar luz, agua y gas.",
        "El patrimonio son los bienes culturales y naturales que heredamos y que debemos cuidar, como las iglesias de Chiloé, las figuras moái de Rapa Nui, un parque, una plaza antigua o una fiesta tradicional. Cuidar el medioambiente es proteger el aire, el agua, el suelo y los seres vivos para que sigan existiendo.",
        "Estas actitudes se practican en todos los espacios: en la casa, en la escuela, en el barrio y en el país. Y en cualquier momento del día: al llegar a clases, en el recreo, al cuidar la plaza, al votar. No hace falta ser adulto para practicarlas.",
    ],
    [("actitud cívica", "forma de actuar que ayuda a vivir bien con los demás"), ("patrimonio", "bienes culturales y naturales que heredamos y debemos cuidar"), ("diálogo", "conversación en la que se escucha y se habla por turnos"), ("plagio", "presentar como propio algo que escribió otra persona"), ("reciclar", "reutilizar materiales para que no se vuelvan basura")],
    [
        ("Clasificar una acción", "Un niño escucha sin interrumpir a una compañera que piensa distinto. ¿Qué actitud cívica practica?", ["Escucha una opinión distinta.", "Eso es respetar a las personas.", "Es respeto."], "Respetar a todas las personas"),
        ("Ubicar el espacio", "Unos vecinos limpian juntos una plaza del barrio. ¿En qué espacio y con qué actitud?", ["El lugar es el barrio.", "Cuidan un espacio común y cooperan.", "Es cuidado del patrimonio y la convivencia."], "En el barrio; cuidado de lo común y cooperación"),
    ],
    [
        ("Creer que las actitudes cívicas son solo para adultos.", "Cualquier persona puede practicarlas.", "Piensa en lo que puedes hacer hoy."),
        ("Pensar que solo se practican en la escuela.", "También se practican en la casa y en el barrio.", "Ubica el espacio y la actitud."),
    ],
    [
        ("Apagar la luz al salir de una pieza vacía, ¿es cuidado del medioambiente o respeto a una opinión distinta?", "Cuidado del medioambiente", "Así se ahorra energía eléctrica."),
        ("Decir la verdad aunque cueste, ¿es honestidad o ahorro de agua?", "Honestidad", "Es actuar con verdad."),
        ("Un compañero propone un turno para usar el balón en el recreo. ¿Es buena convivencia o plagio?", "Buena convivencia", "Propone una solución para todos."),
    ],
    [
        ("¿Por qué escuchar una opinión distinta es una actitud cívica?", "Porque respeta a la persona y su derecho a opinar", "Todas las personas tienen derechos."),
        ("¿Qué es el patrimonio?", "Los bienes culturales y naturales que heredamos y debemos cuidar", "Así se definió en el vocabulario."),
        ("¿Por qué estas actitudes sirven en la casa, la escuela y el barrio?", "Porque en todos esos espacios las personas conviven", "Donde hay convivencia hacen falta actitudes cívicas."),
    ],
    [
        arith("Una familia de ejemplo recicla 4 botellas cada día durante 7 días. ¿Cuántas botellas recicla en una semana?", "4*7", "Se multiplica por los días de la semana.", " botellas"),
        ("Un estudiante lee un texto, lo explica con sus palabras y nombra el libro. ¿Practica honestidad o plagio?", "Honestidad", "Reconoce de dónde sacó la idea."),
        ("Una niña y un niño quieren usar la cancha a la misma hora, y se turnan por igual. ¿Practican igualdad de derechos o desorden?", "Igualdad de derechos", "Ambos tienen derecho a usarla."),
    ],
    [
        ("Pedro dice: «Las actitudes cívicas solo sirven en el colegio». ¿Qué error comete?", "Sirven en todos los espacios, como la casa y el barrio", "La convivencia ocurre en todas partes."),
        ("Ema dice: «Si nadie me ve, puedo copiar». ¿Qué actitud no practica?", "La honestidad y la responsabilidad", "Copiar es presentar como propio lo ajeno."),
    ],
    [
        ("Ordena de menor a mayor espacio: A) barrio, B) casa, C) país.", "B, A, C", "La casa es lo más pequeño, luego el barrio y por último el país."),
        arith("Un curso de ejemplo tiene 30 estudiantes y 24 cumplieron su compromiso de reciclaje. ¿Cuántos no lo cumplieron?", "30-24", "Se resta los que cumplieron al total.", " estudiantes"),
    ],
    [("En una escuela, un curso decide limpiar el patio los viernes. Un estudiante propone turnos para que todos participen. ¿Qué actitud muestra con su propuesta: cooperación o plagio?", "Cooperación", "Busca que todos colaboren.")],
    [("En Historia: ¿qué es una actitud cívica?", "Una forma de actuar que ayuda a vivir bien con los demás", "Es la definición de la clase."), ("¿Qué ejemplo de patrimonio vimos: las iglesias de Chiloé o un lápiz?", "Las iglesias de Chiloé", "Son un bien cultural que heredamos."), ("¿Cuántos grupos de actitudes cívicas vimos?", "Cuatro", "Respeto, convivencia, honestidad y cuidado del patrimonio y medioambiente.")],
    (
        "Completa esta tabla con una acción real o posible tuya por cada casilla: filas respeto, convivencia, honestidad y responsabilidad, cuidado del patrimonio y medioambiente; columnas casa, escuela y barrio. Si no se te ocurre una, usa estas ideas: escuchar a un hermano, ordenar la sala, no copiar en una prueba, apagar la luz, regar una planta, cuidar un mural.",
        "Respeto / escuela: escuchar al compañero sin interrumpir. Medioambiente / casa: apagar la luz.",
        ["completa al menos cuatro casillas", "empareja bien la acción con la actitud", "indica el espacio"],
        ["tabla con cuatro acciones o más"],
        ["poner una acción en la actitud equivocada", "no indicar el espacio"],
        "Muestra tu tabla a una persona de tu casa y pídele que agregue una acción que ella practica.",
    ),
    "Escribe una acción que hiciste hoy que muestre una actitud cívica.",
    "Escribe una actitud cívica que te gustaría practicar más y cómo lo harías.",
)

# ================================================================ OA 20 · clase 2
lesson(
    OA20, 2,
    "Aprenderé a usar fuentes con honestidad: a citar, a escribir con mis palabras y a evitar la copia textual y el plagio. Sirve para que mis trabajos sean verdaderos y respeten el esfuerzo de quien escribió.",
    ["Sé qué es una fuente y quién la hizo.", "Sé que la honestidad es decir la verdad."],
    [
        "Cuando hacemos un trabajo usamos fuentes, como libros o páginas de internet. Usarlas es bueno, pero hay que hacerlo con honestidad. La copia textual es escribir exactamente lo mismo que la fuente. Si se copia sin decirlo, se llama plagio: es presentar como propio lo que escribió otra persona. El plagio es una falta de honestidad y de respeto por el trabajo ajeno.",
        "Hay dos formas correctas de usar una fuente. La primera es la cita textual: copiar entre comillas y decir de dónde viene. La segunda es el parafraseo: explicar la idea con tus propias palabras y también decir la fuente. Por ejemplo, si el libro dice «Los humedales son terrenos cubiertos de agua poco profunda», puedes escribir: «Según el libro Naturaleza de Chile, los humedales son lugares con agua poco profunda».",
        "La procedencia nos dice quién escribió la fuente, cuándo y para qué. Anotarla permite que otros comprueben tu trabajo. Por eso, al terminar, escribimos una lista de las fuentes que usamos. Eso es actuar con honestidad y responsabilidad.",
    ],
    [("plagio", "presentar como propio lo que escribió otra persona"), ("cita textual", "texto copiado entre comillas con su fuente"), ("parafraseo", "explicar una idea con tus propias palabras, nombrando la fuente"), ("fuente", "lo que entrega información, como un libro o una página web"), ("referencia", "dato de dónde viene una idea, como el título del libro")],
    [
        ("Reconocer el plagio", "Texto original: «Los humedales son terrenos cubiertos de agua poco profunda». Un estudiante entrega exactamente esa frase como si fuera suya. ¿Es plagio o cita?", ["Copió igual.", "No dijo de dónde la sacó.", "Es plagio."], "Plagio"),
        ("Corregir con parafraseo", "Mismo original. Otro estudiante escribe: «Según el libro Naturaleza de Chile, los humedales son lugares con agua poco profunda». ¿Es plagio o parafraseo con fuente?", ["Cambió las palabras.", "Nombró el libro.", "Es parafraseo con fuente."], "Parafraseo con fuente"),
    ],
    [
        ("Creer que copiar de internet no es plagio.", "Si no dices la fuente y presentas como propio, es plagio.", "Cita o parafrasea y nombra la fuente."),
        ("Cambiar solo una palabra y decir que es propio.", "Sigue siendo casi igual al original.", "Explica la idea con tus palabras y nombra la fuente."),
    ],
    [
        ("Copiar un texto igual y decir que lo escribiste tú, ¿es plagio o cita?", "Plagio", "No se reconoce a quien lo escribió."),
        ("Copiar entre comillas y nombrar la fuente, ¿es cita textual o plagio?", "Cita textual", "Se reconoce el origen."),
        ("Si usas un libro para tu trabajo, ¿conviene nombrarlo o esconderlo?", "Nombrarlo", "Es honesto y permite comprobar."),
    ],
    [
        ("¿Por qué el plagio es una falta de honestidad?", "Porque presenta como propio el trabajo de otra persona", "No se dice la verdad sobre quién lo hizo."),
        ("¿Qué diferencia hay entre cita textual y parafraseo?", "La cita copia entre comillas; el parafraseo explica con palabras propias", "Ambas nombran la fuente."),
        ("¿Para qué sirve anotar la fuente?", "Para que otros puedan comprobar la información", "Permite revisar de dónde viene."),
    ],
    [
        ("Original: «Las aves migratorias recorren grandes distancias cada año». Versión A: «Las aves migratorias recorren grandes distancias cada año» sin comillas ni fuente. Versión B: «Según una guía de aves, muchas viajan lejos cada año». ¿Cuál versión es plagio?", "La A", "Copia igual y no nombra la fuente."),
        ("Con el mismo original, ¿la versión B nombra la fuente?", "Sí, nombra una guía de aves", "Dice «según una guía de aves»."),
        ("Un estudiante quiere usar una frase igual al libro. ¿Qué debe hacer: ponerla entre comillas y nombrar el libro o cambiar de lugar las comas?", "Ponerla entre comillas y nombrar el libro", "Así se hace una cita textual."),
    ],
    [
        ("Ana dice: «Si le cambio una palabra a lo que copié, ya no es plagio». ¿Qué error comete?", "Sigue siendo casi igual y sin nombrar la fuente", "Debe explicar con sus palabras y citar."),
        ("Luis copia un texto de internet y dice que es suyo porque lo «encontró». ¿Qué actitud no practica?", "La honestidad", "Presenta como propio algo ajeno."),
    ],
    [
        ("Ordena los pasos para usar una fuente: A) escribir la idea con tus palabras, B) leer y entender, C) nombrar la fuente.", "B, A, C", "Primero se entiende, luego se explica y por último se cita."),
        ("Un trabajo usó 4 fuentes y la lista de referencias nombra solo 3. ¿Cuántas fuentes faltan en la lista?", "1", "4 menos 3 es 1.", "4-3"),
    ],
    [("Un niño usa tres libros. Del primero copia una frase sin comillas ni fuente; del segundo explica una idea con sus palabras y nombra el libro; del tercero copia otra frase sin comillas ni fuente. ¿Cuántos de los tres usos son plagio?", "2", "Son las dos copias sin comillas ni fuente.")],
    [("¿Qué es el plagio?", "Presentar como propio lo que escribió otra persona", "Es la definición de la clase."), ("¿Qué es el parafraseo?", "Explicar una idea con tus palabras, nombrando la fuente", "Es la definición de la clase."), ("¿Por qué anotar las fuentes?", "Para que otros comprueben la información", "Es parte de la honestidad.")],
    (
        "Lee este texto original inventado: «El cóndor es un ave grande que vive en la cordillera de los Andes. Puede volar largas distancias sin mover mucho las alas». Escribe: 1) una cita textual con comillas y fuente (inventa un título de libro); 2) un parafraseo con tus palabras y la fuente; 3) una frase que NO sería válida porque es plagio.",
        "1) «El cóndor es un ave grande que vive en la cordillera de los Andes» (Aves de Chile). 2) Según Aves de Chile, el cóndor es grande y habita los Andes. 3) Copiar igual sin nombrar la fuente.",
        ["incluye las tres versiones pedidas", "usa comillas en la cita", "nombra la fuente en las versiones válidas"],
        ["tres frases escritas"],
        ["olvidar las comillas", "no nombrar la fuente"],
        "Muestra tus tres frases a una persona de tu casa y pídele que diga cuál es la plagiada.",
    ),
    "Anota el título de un libro o página que hayas usado en un trabajo reciente.",
    "Escribe cómo explicarías con tus palabras qué es el plagio a un compañero menor.",
)

# ================================================================ OA 20 · clase 3
lesson(
    OA20, 3,
    "Aprenderé a relacionar acciones de ahorro de luz, agua y gas y de reciclaje con sus consecuencias para el medioambiente y para las personas. Sirve para ver que lo que hago en mi casa y en mi escuela tiene efecto.",
    ["Sé qué es una actitud cívica.", "Sé que una causa explica por qué ocurre algo."],
    [
        "Cuidar el medioambiente significa proteger el agua, el aire, el suelo y los seres vivos. Una acción tiene una causa y una consecuencia. Si cerramos la llave mientras nos lavamos los dientes, la consecuencia es que se gasta menos agua. Si apagamos las luces que no usamos, se consume menos electricidad. Si cuidamos el gas, por ejemplo cerrando la llave de paso cuando un adulto termina de cocinar, usamos menos combustible y evitamos riesgos.",
        "El reciclaje es otra acción: se separan envases de vidrio, papel, cartón, plástico y latas para que se reutilicen como materia prima en vez de convertirse en basura. La consecuencia es menos residuos y menos recursos gastados. Los actores son las familias, las escuelas, las municipalidades y las empresas de reciclaje.",
        "Las acciones pequeñas suman. Para saber su efecto podemos calcular. Por ejemplo, si una llave gotea 2 litros por hora, en 24 horas son 48 litros. Los números de esta clase son de ejemplo. También hay consecuencias a largo plazo: si muchas personas ahorran agua, los embalses duran más y hay agua para el futuro.",
    ],
    [("medioambiente", "conjunto de agua, aire, suelo y seres vivos que nos rodea"), ("residuo", "cosa que ya no se usa y se tira"), ("reciclaje", "reutilizar materiales para hacer cosas nuevas"), ("consumo", "cantidad que se gasta de algo, como agua o luz"), ("recurso", "algo de la naturaleza que usamos, como el agua")],
    [
        ("Calcular un ahorro", "En un ejemplo, una llave gotea 2 litros por hora. ¿Cuántos litros pierde en 24 horas?", ["Multiplico litros por horas.", "2 por 24 es 48.", "Pierde 48 litros."], "48 litros"),
        ("Causa y consecuencia", "Una familia separa envases de papel y de latas. Nombra una consecuencia.", ["Los envases se reutilizan.", "Hay menos basura.", "Esa es la consecuencia."], "Hay menos basura y se reutilizan materiales"),
    ],
    [
        ("Pensar que una acción pequeña no sirve.", "Muchas acciones pequeñas suman un gran efecto.", "Calcula cuánto se ahorra con el tiempo."),
        ("Creer que reciclar es solo botar la basura.", "Reciclar es separar y reutilizar materiales.", "Separa por tipo."),
    ],
    [
        ("Cerrar la llave al lavarse los dientes, ¿ahorra agua o ahorra luz?", "Ahorra agua", "La llave controla el agua."),
        ("Apagar las luces que no se usan, ¿ahorra electricidad o ahorra gas?", "Ahorra electricidad", "Las luces funcionan con electricidad."),
        ("Separar botellas, papeles y latas, ¿es reciclaje o plagio?", "Reciclaje", "Se preparan los materiales para reutilizarlos."),
    ],
    [
        ("¿Por qué ahorrar agua beneficia a las personas del futuro?", "Porque hay más agua disponible para después", "Los embalses y pozos duran más."),
        ("¿Por qué el reciclaje reduce la cantidad de basura?", "Porque los materiales se reutilizan en lugar de botarse", "Se les da una nueva vida."),
        ("¿Por qué una acción pequeña de muchas personas es importante?", "Porque suma un gran efecto", "Mil acciones pequeñas ahorran mucho."),
    ],
    [
        arith("Un curso de ejemplo ahorra 3 litros de agua por estudiante al día. Son 30 estudiantes. ¿Cuántos litros ahorran en un día?", "3*30", "Se multiplica por el número de estudiantes.", " litros"),
        arith("Una escuela de ejemplo gastó 120 unidades de luz en marzo y 100 en abril. ¿Cuántas unidades ahorró?", "120-100", "Se resta el consumo menor al mayor.", " unidades"),
        arith("Una familia de ejemplo junta 45 latas en 3 semanas, la misma cantidad cada semana. ¿Cuántas latas junta por semana?", "45//3", "Se reparten 45 entre 3 semanas.", " latas"),
    ],
    [
        ("Rosa dice: «Mi ahorro de agua no sirve porque soy una sola persona». ¿Qué error comete?", "Muchas acciones individuales suman un gran efecto", "Lo que hace cada uno cuenta."),
        ("Un niño deja encendido el calefactor de la sala vacía. ¿Qué consecuencia tiene para el medioambiente: gasta energía innecesariamente o no tiene efecto?", "Gasta energía innecesariamente", "Consume recursos sin necesidad."),
    ],
    [
        ("Ordena la cadena: A) se ahorra agua, B) se cierra la llave, C) los embalses duran más.", "B, A, C", "Primero la acción, luego el ahorro y después el efecto a largo plazo."),
        ("En una escuela se reciclaron 80 kilos de papel en febrero y 20 kilos más en marzo. ¿Cuántos kilos reciclaron en total?", "100", "80 más 20 son 100.", "80+20"),
    ],
    [("Una comunidad de ejemplo puso un contenedor de reciclaje de vidrio en la plaza y los vecinos juntaron 150 kilos en un mes. ¿Qué actor llevó el vidrio al contenedor: los vecinos o una empresa de reciclaje?", "Los vecinos", "El enunciado dice que los vecinos juntaron el vidrio.")],
    [("En Historia: ¿Qué es reciclar?", "Reutilizar materiales para hacer cosas nuevas", "Es la definición de la clase."), ("¿Qué ahorra cerrar una llave?", "Agua", "Controla el agua."), ("¿Las acciones pequeñas importan?", "Sí", "Muchas suman un gran efecto.")],
    (
        "Elige una acción (cerrar la llave al lavarte los dientes, apagar luces que no usas o separar envases) y escribe: causa, consecuencia a corto plazo, consecuencia a largo plazo, actores y un cálculo con números de ejemplo propios (por ejemplo, litros o kilos en una semana).",
        "Acción: cerrar la llave. Causa: gasto innecesario. Corto plazo: se gastan menos litros. Largo plazo: el agua dura más. Cálculo: 3 litros por día en 7 días son 21 litros.",
        ["nombra causa y consecuencias", "incluye un cálculo correcto", "menciona al menos un actor"],
        ["cinco frases y un cálculo"],
        ["calcular mal", "olvidar el largo plazo"],
        "Muestra tu cálculo a una persona de tu casa y pídele que lo repita.",
    ),
    "Anota dos acciones de ahorro que podrías hacer en tu casa esta semana.",
    "Escribe una pregunta sobre cómo se recicla en tu comuna.",
)

# ================================================================ OA 20 · clase 4
lesson(
    OA20, 4,
    "Aprenderé a comparar cómo se actúa ante opiniones distintas y ante problemas de convivencia, y a reconocer perspectivas diferentes. Sirve para practicar el respeto, el diálogo y los acuerdos.",
    ["Sé reconocer las cuatro actitudes cívicas.", "Sé que comparar exige criterios iguales."],
    [
        "Respetar a todas las personas significa tratarlas con igualdad de derechos y escuchar sus opiniones aunque piensen distinto. Contribuir a la buena convivencia significa usar el diálogo para plantear ideas, proponer soluciones, llegar a acuerdos y cooperar. Dialogar es hablar y escuchar por turnos, sin gritar ni burlarse.",
        "Veamos dos reacciones ante un desacuerdo. Dos compañeros quieren proyectos distintos: uno propone una campaña de reciclaje y el otro un mural sobre el patrimonio. En la reacción 1 se gritan y no resuelven nada. En la reacción 2 cada uno explica sus razones, se escuchan, buscan ideas comunes y acuerdan hacer primero el mural y después el reciclaje. La segunda reacción cumple los criterios de respeto, diálogo y cooperación.",
        "Cada persona tiene una perspectiva, que es su mirada según su situación. Entenderla ayuda a llegar a acuerdos, pero no significa que todas las ideas valgan igual: no se justifica un maltrato. Para comparar usamos criterios iguales: si hubo respeto, si se escuchó, si se llegó a un acuerdo y si todos cooperaron.",
    ],
    [("diálogo", "conversación donde se habla y se escucha por turnos"), ("acuerdo", "solución que aceptan las personas que conversaron"), ("cooperar", "trabajar juntos para lograr una meta común"), ("perspectiva", "mirada de una persona según su situación"), ("igualdad de derechos", "que todas las personas tengan los mismos derechos")],
    [
        ("Comparar dos reacciones", "Reacción 1: se gritan y no resuelven. Reacción 2: se escuchan y acuerdan un orden. Compara el criterio «se llegó a un acuerdo».", ["En la 1 no hubo acuerdo.", "En la 2 sí hubo acuerdo.", "La 2 cumple el criterio."], "La reacción 2 llegó a un acuerdo y la 1 no"),
        ("Reconocer una perspectiva", "Un niño quiere jugar a la pelota y una niña quiere leer en el patio. ¿Son perspectivas iguales o distintas?", ["Cada uno quiere algo diferente.", "Piensan según su situación.", "Son distintas."], "Distintas"),
    ],
    [
        ("Pensar que dialogar es hablar más fuerte.", "Dialogar es escuchar y hablar por turnos.", "Pide la palabra y escucha."),
        ("Creer que respetar es estar de acuerdo con todo.", "Respetar es escuchar y tratar bien a quien piensa distinto.", "Se puede discrepar con respeto."),
    ],
    [
        ("Escuchar a un compañero que piensa distinto sin burlarse, ¿es respeto o desorden?", "Respeto", "Se valora su opinión."),
        ("Cooperar, ¿es trabajar juntos para una meta común o competir para ganar solo?", "Trabajar juntos para una meta común", "Así se definió en el vocabulario."),
        ("Un acuerdo, ¿es una solución que aceptan los que conversaron o una orden de uno solo?", "Una solución que aceptan los que conversaron", "Así se definió en el vocabulario."),
    ],
    [
        ("¿Por qué dialogar es mejor que gritar?", "Porque permite escuchar y llegar a acuerdos", "Gritar no resuelve el problema."),
        ("¿Por qué entender una perspectiva no significa estar de acuerdo con todo?", "Porque se puede comprender sin justificar un maltrato", "Entender no es aprobar todo."),
        ("¿Por qué una niña y un niño tienen igualdad de derechos al usar la cancha?", "Porque ambos tienen el mismo derecho a usar el espacio", "No importa el sexo para ejercer derechos."),
    ],
    [
        ("Cuatro estudiantes votan por un proyecto: 2 por reciclaje, 1 por mural y 1 por huerto. ¿Qué proyecto tiene más apoyo?", "Reciclaje", "Tiene 2 votos, más que los otros."),
        ("Tabla de ejemplo: Reacción 1 cumple 1 de 4 criterios (respeto, escucha, acuerdo, cooperación); Reacción 2 cumple los 4. ¿Cuántos criterios más cumple la 2?", "3", "4 menos 1 es 3.", "4-1"),
        ("Dos compañeros discuten qué proyecto hacer. Uno propone alternar: primero mural y después reciclaje. ¿Es una propuesta de solución o una burla?", "Una propuesta de solución", "Busca que ambos puedan hacer su proyecto."),
    ],
    [
        ("Marta dice: «Escuchar a quien piensa distinto es perder tiempo». ¿Qué error comete?", "Escuchar permite entender y llegar a acuerdos", "Es parte del respeto."),
        ("Un estudiante dice que su idea es la única válida y no deja hablar. ¿Qué actitud no practica?", "El respeto y el diálogo", "No escucha ni reconoce a los demás."),
    ],
    [
        ("Ordena los pasos del diálogo: A) llegar a un acuerdo, B) escuchar la idea del otro, C) explicar la propia idea.", "C, B, A", "Primero se explica, luego se escucha y al final se acuerda."),
        ("Un curso de 28 estudiantes vota. 15 prefieren la propuesta X y 13 la Y. Un acuerdo respetuoso: ¿cuántos estudiantes más apoyan a X que a Y?", "2", "15 menos 13 es 2.", "15-13"),
    ],
    [("Dos compañeros quieren hacer proyectos distintos. Uno propone mezclar ambas ideas en un solo trabajo. ¿Qué actitud cívica muestra: cooperación o plagio?", "Cooperación", "Busca un acuerdo que incluya a ambos.")],
    [("¿Qué es dialogar?", "Hablar y escuchar por turnos", "Es la definición de la clase."), ("¿Qué es cooperar?", "Trabajar juntos para una meta común", "Es la definición de la clase."), ("¿Respetar es estar de acuerdo con todo?", "No", "Es escuchar y tratar bien.")],
    (
        "Lee este desacuerdo inventado: Ana quiere hacer un afiche sobre ahorro de agua y Beto quiere hacer un video sobre reciclaje; tienen solo una semana. Escribe un diálogo de seis líneas entre Ana y Beto en que se escuchen, expliquen sus razones y lleguen a un acuerdo. Luego marca qué criterio de la clase muestra cada línea.",
        "Ana: Quiero un afiche porque es rápido. Beto: Yo quiero un video porque explica mejor. Ana: Podemos hacer un afiche con un código para ver el video. Beto: Me parece bien...",
        ["incluye razones de ambos", "muestra escucha", "termina con un acuerdo"],
        ["diálogo de seis líneas"],
        ["que uno imponga su idea", "que no haya acuerdo"],
        "Lee tu diálogo con una persona de tu casa, cada uno una voz, y pídele que diga si se llegó a un acuerdo justo.",
    ),
    "Recuerda un desacuerdo que tuviste y escribe cómo lo resolviste.",
    "Escribe una frase que ayude a pedir la palabra con respeto.",
)

# ================================================================ OA 20 · clase 5
lesson(
    OA20, 5,
    "Aprenderé a argumentar con evidencia por qué conviene practicar actitudes cívicas, usando datos de ejemplo sobre ahorro, reciclaje, honestidad y respeto. Sirve para convencer con razones y no solo con opiniones.",
    ["Sé reconocer y comparar actitudes cívicas.", "Sé que un argumento tiene afirmación, evidencia y razón."],
    [
        "Argumentar es defender una idea con evidencia y razones. Un buen argumento tiene tres partes: una afirmación, que es lo que sostengo; una evidencia, que es un dato o hecho que la apoya; y una razón, que explica por qué la evidencia apoya la afirmación. También se dice el límite: lo que la evidencia no permite saber.",
        "Ejemplo con datos inventados. Afirmación: «Conviene reciclar en nuestra escuela». Evidencia: en un mes, el curso 6.º A recicló 60 botellas y el curso 6.º B, que no recicló, botó esas mismas 60 botellas a la basura. Razón: reciclar evita que se conviertan en basura. Límite: es el dato de un solo mes y de dos cursos.",
        "También se pueden argumentar la honestidad y el respeto. Si en un curso nadie copia, las notas muestran lo que cada uno realmente aprendió, y el profesor puede ayudar mejor. Si se escucha a todos, se encuentran ideas más variadas. Las evidencias pueden ser hechos del curso, números o experiencias. Un argumento convence porque se puede comprobar.",
    ],
    [("afirmación", "lo que una persona sostiene"), ("evidencia", "dato o hecho que apoya una afirmación"), ("razón", "explicación de por qué la evidencia apoya la afirmación"), ("límite", "lo que la evidencia no permite saber"), ("campaña", "conjunto de acciones para informar o convencer")],
    [
        ("Identificar la evidencia", "«Hay que cuidar el agua porque en un curso de ejemplo se ahorraron 90 litros en una semana al cerrar las llaves.» ¿Cuál es la evidencia?", ["La afirmación es que hay que cuidar el agua.", "La evidencia es el ahorro de 90 litros.", "Los separo."], "Que se ahorraron 90 litros en una semana"),
        ("Reconocer un límite", "El dato de 90 litros viene de un solo curso. ¿Qué no permite saber?", ["Es un curso.", "No dice qué pasa en otros cursos.", "No permite afirmar lo mismo de toda la escuela."], "Qué pasaría en toda la escuela"),
    ],
    [
        ("Defender una idea solo porque «me gusta».", "Un gusto no se puede comprobar con datos.", "Agrega un hecho o un número."),
        ("Usar como evidencia algo que no se relaciona con la afirmación.", "La evidencia debe apoyar justo lo que se afirma.", "Revisa si el dato sirve."),
    ],
    [
        ("Una afirmación, ¿es lo que alguien sostiene o el dato que la apoya?", "Lo que alguien sostiene", "El dato es la evidencia."),
        ("«En un mes recicló 60 botellas», ¿puede ser evidencia?", "Sí", "Es un dato que se puede comprobar."),
        ("La razón, ¿explica por qué la evidencia apoya la afirmación o repite la afirmación?", "Explica por qué la evidencia apoya la afirmación", "Conecta el dato con la idea."),
    ],
    [
        ("¿Por qué un argumento sobre el reciclaje necesita datos?", "Para que se pueda comprobar y convencer", "Sin datos queda como una opinión."),
        ("¿Por qué es importante decir el límite de la evidencia?", "Para no afirmar más de lo que muestran los datos", "Así se evita exagerar."),
        ("¿Por qué argumentar con evidencia respeta a quien nos escucha?", "Porque le permite comprobar nuestras razones", "Se puede revisar si es verdad."),
    ],
    [
        ("Afirmación: «Ahorrar luz reduce el consumo». ¿Qué evidencia sirve: «el consumo bajó de 120 a 100 unidades» o «hay más focos en la sala»?", "El consumo bajó de 120 a 100 unidades", "Es un dato sobre el consumo."),
        arith("Un curso recicló 60 botellas en un mes y quiere duplicar esa cantidad. ¿Cuántas debe reciclar el mes siguiente?", "60*2", "Duplicar es multiplicar por 2.", " botellas"),
        ("Afirmación: «Copiar perjudica el aprendizaje». ¿Qué evidencia sirve: «el estudiante que copió no supo responder en una conversación» o «la prueba tenía 20 preguntas»?", "El estudiante que copió no supo responder en una conversación", "Muestra que no aprendió lo que entregó."),
    ],
    [
        ("Eva escribe: «Hay que reciclar porque sí». ¿Qué le falta a su argumento?", "Evidencia y razones", "Un «porque sí» no se puede comprobar."),
        ("Teo dice: «Mi curso ahorró agua, así que en todo Chile se ahorra». ¿Qué límite no respeta?", "Un curso no representa a todo Chile", "Generaliza más allá de la evidencia."),
    ],
    [
        ("Ordena un argumento: A) razón, B) afirmación, C) evidencia.", "B, C, A", "Primero se afirma, luego se da el dato y al final se explica."),
        ("Dos campañas de ejemplo: la A consiguió 80 firmas y la B 50. Afirmación: «La campaña A tuvo más apoyo». ¿Cuántas firmas más tuvo la A?", "30", "80 menos 50 son 30.", "80-50"),
    ],
    [("En una escuela se quiere cuidar el patrimonio de un mural antiguo. Una estudiante argumenta: «Hay que cuidarlo porque nos recuerda la historia del barrio». ¿Cuál es la afirmación?", "Que hay que cuidar el mural", "Es lo que sostiene; lo demás es la razón.")],
    [("¿Qué partes tiene un buen argumento?", "Afirmación, evidencia y razón", "Así se enseñó en la clase."), ("En Historia: ¿Qué es un límite?", "Lo que la evidencia no permite saber", "Es la definición de la clase."), ("¿Se argumenta con «porque sí»?", "No", "Se necesita evidencia.")],
    (
        "Elige una de estas afirmaciones y escribe un argumento con evidencia, razón y límite, usando estos datos inventados: a) «Conviene ahorrar agua»: un curso cerró las llaves y gastó 40 litros menos por semana; b) «Conviene cuidar el patrimonio»: un mural cuidado fue visitado por 120 personas en un año; c) «Conviene ser honesto en las pruebas»: en un curso sin copia, el profesor identificó 5 temas que necesitaban refuerzo.",
        "Afirmación a: conviene ahorrar agua. Evidencia: 40 litros menos por semana. Razón: se gasta menos. Límite: es un solo curso.",
        ["incluye afirmación y evidencia", "explica la razón", "reconoce un límite"],
        ["cuatro frases escritas"],
        ["no usar los datos", "no reconocer el límite"],
        "Lee tu argumento a una persona de tu casa y pídele que diga si el dato la convence.",
    ),
    "Escribe una acción cívica que hagas y un dato que muestre su efecto.",
    "Escribe qué dato necesitarías para convencer a tu curso de reciclar.",
)

# ================================================================ OA 21 · clase 1
lesson(
    OA21, 1,
    "Aprenderé a planificar un proyecto de equipo, asignando roles y tiempos acordados. Sirve para que cada integrante sepa qué hacer, en qué lugar y para qué fecha.",
    ["Sé que dialogar es hablar y escuchar por turnos.", "Sé calcular días y cantidades."],
    [
        "Trabajar en equipo es lograr juntos una meta común. Para eso conviene planificar. Primero se define la meta: qué queremos lograr. Luego se asignan roles, es decir, tareas para cada persona. Algunos roles frecuentes son coordinador (guía la conversación), secretario (anota los acuerdos), investigador (busca información), responsable de materiales y encargado del tiempo.",
        "También se acuerdan los tiempos. Un calendario muestra qué tarea se hace cada día y cuándo se entrega el proyecto. Cumplir las responsabilidades asignadas y los plazos acordados permite que el equipo avance. Si una persona no puede, avisa antes para que el grupo se reorganice.",
        "Un buen equipo escucha los argumentos de los demás, expresa opiniones fundamentadas y llega a un punto de vista común. Los espacios de trabajo también importan: dónde se reúnen, cuánto dura la reunión y qué materiales usan. Todo esto se anota en un plan.",
    ],
    [("equipo", "grupo de personas que trabajan juntas por una meta común"), ("rol", "tarea o función que cumple cada integrante"), ("plazo", "tiempo acordado para terminar una tarea"), ("meta", "lo que el equipo quiere lograr"), ("coordinador", "persona que guía la conversación y el trabajo del equipo")],
    [
        ("Asignar un rol", "Un equipo anota los acuerdos en una libreta. ¿Qué rol cumple quien escribe: coordinador o secretario?", ["Quien anota acuerdos cumple una función.", "Esa función es del secretario.", "Es el secretario."], "Secretario"),
        ("Calcular un plazo", "Un equipo tiene el lunes 3 para empezar y debe entregar el viernes 7. ¿Cuántos días hay del lunes 3 al viernes 7, contando ambos días?", ["Cuento 3, 4, 5, 6 y 7.", "Son 5 días.", "Esos son los días de trabajo."], "5 días"),
    ],
    [
        ("Pensar que un equipo funciona sin roles.", "Sin roles, algunas tareas no las hace nadie o las hacen varias personas.", "Reparte tareas desde el inicio."),
        ("Creer que cumplir plazos no importa.", "Si un integrante se atrasa, todo el equipo se atrasa.", "Acuerda fechas y avisa si no puedes cumplir."),
    ],
    [
        ("El secretario, ¿anota los acuerdos o guarda los materiales?", "Anota los acuerdos", "Es su rol."),
        ("Una meta, ¿es lo que el equipo quiere lograr o el nombre de un integrante?", "Lo que el equipo quiere lograr", "Así se definió en el vocabulario."),
        ("Un plazo, ¿es el tiempo acordado para terminar o el color del cuaderno?", "El tiempo acordado para terminar", "Así se definió en el vocabulario."),
    ],
    [
        ("¿Por qué conviene asignar roles?", "Para que cada persona sepa qué hacer", "Se evita que se repitan o se olviden tareas."),
        ("¿Por qué conviene avisar antes si no se puede cumplir una tarea?", "Para que el grupo se reorganice a tiempo", "Así se evitan los atrasos."),
        ("¿Por qué es útil un calendario de trabajo?", "Porque muestra qué se hace cada día y cuándo se entrega", "Permite coordinar los tiempos."),
    ],
    [
        ("Equipo de 4 personas con 4 roles: coordinador, secretario, investigador y encargado de materiales. Si Ana es investigadora y Beto secretario, ¿qué roles quedan sin asignar?", "Coordinador y encargado de materiales", "Quedan los dos que no se nombraron."),
        arith("Un equipo se reúne 3 veces por semana durante 4 semanas. ¿Cuántas reuniones hace en total?", "3*4", "Se multiplica por las semanas.", " reuniones"),
        ("Un proyecto se entrega el jueves 13. El equipo quiere terminar 2 días antes para revisar. ¿Qué día debe terminar: el martes 11 o el miércoles 12?", "El martes 11", "13 menos 2 es 11."),
    ],
    [
        ("Luis dice: «No necesito avisar si no puedo cumplir, otro lo hará». ¿Qué error comete?", "El grupo se reorganiza mejor si se avisa a tiempo", "Avisar es una responsabilidad."),
        ("Un equipo tiene 3 tareas para 3 integrantes, pero dos eligen la misma tarea y nadie la tercera. ¿Qué problema aparece?", "Una tarea queda sin hacer", "Falta asignación clara de roles."),
    ],
    [
        ("Ordena los pasos para planificar: A) acordar fechas, B) definir la meta, C) repartir roles.", "B, C, A", "Primero la meta, luego los roles y después los tiempos."),
        arith("Un proyecto necesita 12 horas de trabajo entre 4 integrantes, repartidas por igual. ¿Cuántas horas trabaja cada uno?", "12//4", "Se reparten 12 horas entre 4 personas.", " horas"),
    ],
    [("Un equipo de 5 estudiantes debe presentar una maqueta del barrio. Acuerdan reunirse en la biblioteca los martes y jueves. ¿Cuántas reuniones tendrán en 2 semanas?", "4", "2 reuniones por semana por 2 semanas son 4.", "2*2")],
    [("En Historia: ¿qué es un rol?", "Una tarea o función que cumple cada integrante", "Es la definición de la clase."), ("¿Para qué sirve un plazo acordado?", "Para saber cuándo terminar una tarea", "Ordena el trabajo."), ("¿Qué hace un coordinador?", "Guía la conversación y el trabajo del equipo", "Es su rol.")],
    (
        "Planifica este proyecto inventado: un equipo de cuatro personas debe hacer un afiche sobre cómo cuidar la plaza del barrio en cinco días hábiles (lunes a viernes). Asigna un rol a cada integrante (coordinador, secretario, investigador y encargado de materiales) y escribe una tarea por día. Escribe también un lugar para reunirse y qué harán si alguien no puede.",
        "Lunes: acordar meta (coordinador). Martes: buscar información (investigador). Miércoles: diseñar (todos). Jueves: preparar materiales. Viernes: revisar y entregar. Lugar: la biblioteca. Si alguien falta, avisa antes.",
        ["asigna los cuatro roles", "escribe una tarea por día", "indica un lugar y qué hacer si alguien falta"],
        ["plan de cinco días con roles"],
        ["dejar un día sin tarea", "no asignar todos los roles"],
        "Lee tu plan a una persona de tu casa y pídele que diga si es realista.",
    ),
    "Anota un plazo que hayas acordado esta semana con otra persona.",
    "Escribe qué rol te gusta más en un equipo y por qué.",
)

# ================================================================ OA 21 · clase 2
lesson(
    OA21, 2,
    "Aprenderé a repartir la búsqueda de información entre los integrantes del equipo y a revisar las fuentes entre todos. Sirve para que la investigación sea ordenada, honesta y confiable.",
    ["Sé asignar roles y plazos en un equipo.", "Sé que una fuente tiene una procedencia."],
    [
        "En una investigación de equipo, cada integrante puede buscar información en una fuente distinta. Así se avanza más rápido. Pero luego hay que compartir lo encontrado y revisar las fuentes entre todos. Cada fuente se anota con su procedencia: quién la hizo, cuándo y para qué. Se anota también quién del equipo la encontró.",
        "El equipo contrasta lo que dijo cada fuente. Si dos fuentes dicen cosas diferentes, se conversa y se busca una tercera. Se separa lo que dice la fuente, lo que el equipo interpreta y lo que no se puede saber. Cada integrante debe contar con sus palabras lo que encontró, sin copiar textualmente, para actuar con honestidad.",
        "También se cumplen los tiempos acordados. Si el equipo se demora en la búsqueda, se pierde tiempo para escribir. Por eso se fija un plazo para la búsqueda y otro para la revisión. Escuchar los argumentos de los demás sobre si una fuente es confiable ayuda a decidir mejor.",
    ],
    [("investigación", "búsqueda ordenada de información sobre un tema"), ("contrastar", "comparar fuentes para ver en qué coinciden y en qué no"), ("procedencia", "quién hizo la fuente, cuándo y para qué"), ("registro", "anotación ordenada de lo que se hace o se encuentra"), ("fuente confiable", "fuente que se sabe quién la hizo y que entrega datos comprobables")],
    [
        ("Repartir la búsqueda", "Un equipo de 3 busca información sobre una plaza: Ana lee un libro, Beto pregunta a un vecino y Carla revisa un plano. ¿Cuántas fuentes distintas usan?", ["Cuento cada fuente.", "Un libro, un vecino y un plano.", "Son 3."], "3 fuentes distintas"),
        ("Contrastar", "Ana lee que la plaza tiene 4 bancas y Beto, que tiene 6. ¿Qué debe hacer el equipo?", ["Las fuentes no coinciden.", "Hay que revisar de nuevo.", "Se busca una tercera fuente."], "Buscar una tercera fuente o contar las bancas"),
    ],
    [
        ("Creer que basta una sola fuente para el equipo.", "Una sola fuente puede dejar cosas fuera o equivocarse.", "Usa varias fuentes y contrástalas."),
        ("Copiar palabra por palabra el texto de la fuente que encontró otro integrante, sin citarla.", "Sigue siendo plagio de la fuente original, aunque la haya encontrado un compañero.", "Explica con tus palabras y registra la fuente."),
    ],
    [
        ("Contrastar fuentes, ¿es compararlas o copiarlas?", "Compararlas", "Así se definió en el vocabulario."),
        ("Un registro de fuentes, ¿es una anotación ordenada o un dibujo?", "Una anotación ordenada", "Sirve para saber de dónde viene cada dato."),
        ("En un equipo, ¿cada integrante puede buscar una fuente distinta o todos deben buscar la misma?", "Pueden buscar fuentes distintas", "Así se avanza más rápido."),
    ],
    [
        ("¿Por qué conviene anotar quién encontró cada fuente?", "Para saber a quién preguntar y organizar el trabajo", "Facilita coordinar al equipo."),
        ("¿Por qué conviene buscar una tercera fuente si dos no coinciden?", "Para comprobar cuál es correcta", "Una tercera fuente ayuda a decidir."),
        ("¿Por qué cada integrante debe contar con sus palabras lo que encontró?", "Para actuar con honestidad y no copiar", "Así evita el plagio."),
    ],
    [
        ("Tabla del equipo: Fuente 1, un libro de 2019; Fuente 2, un vecino de la plaza; Fuente 3, un cartel de la municipalidad de 2023. ¿Cuál es la más reciente?", "El cartel de 2023", "2023 es el año mayor."),
        ("Con la misma tabla: ¿cuántos años pasaron entre el libro y el cartel?", "4", "2023 menos 2019 son 4.", "2023-2019"),
        ("El equipo debe buscar en 3 días y revisar en 2 días. ¿Cuántos días necesita en total?", "5", "3 más 2 son 5.", "3+2"),
    ],
    [
        ("Pedro anota: «Libro: Plazas de Chile». Falta quién lo escribió y cuándo. ¿Qué parte del registro está incompleta?", "La procedencia", "No dice quién lo hizo ni cuándo."),
        ("Una compañera copia casi palabra por palabra un artículo y dice: «Lo encontró mi equipo, no importa». ¿Qué error comete?", "Es plagio aunque el artículo lo haya encontrado un compañero", "Debe parafrasear y citar al autor del artículo."),
    ],
    [
        ("Ordena los pasos de la investigación en equipo: A) escribir las conclusiones, B) contrastar las fuentes, C) buscar información por separado.", "C, B, A", "Primero se busca, luego se contrasta y al final se concluye."),
        ("Un equipo de 4 reparte 12 páginas de lectura por igual. ¿Cuántas páginas lee cada integrante?", "3", "12 dividido en 4 es 3.", "12//4"),
    ],
    [("Un equipo estudia un parque. Ana usa un plano, Beto un folleto de turismo y Carla el relato de un guardaparque. ¿Qué fuente es más probable que muestre solo lo atractivo: el folleto o el plano?", "El folleto", "Se hace para atraer visitantes.")],
    [("¿Qué es contrastar?", "Comparar fuentes para ver en qué coinciden", "Es la definición de la clase."), ("¿Qué debe tener el registro de una fuente?", "Su procedencia", "Quién la hizo, cuándo y para qué."), ("¿Cada integrante puede buscar una fuente distinta?", "Sí", "Así el equipo avanza más rápido.")],
    (
        "Completa un registro de fuentes para este tema inventado: «Cómo cuidar la plaza del barrio». Un equipo de tres dispone de: un cartel de la municipalidad (2023), el relato de una vecina y un plano de la plaza. Anota para cada fuente: nombre, quién la encontró (Ana, Beto o Carla), qué dice (una idea inventada), y una pregunta de procedencia. Luego escribe qué harían si dos fuentes se contradicen.",
        "Cartel (Ana): la plaza abre a las 8:00. Pregunta: ¿quién lo hizo? Si dos se contradicen: buscar una tercera.",
        ["anota las tres fuentes con sus datos", "incluye una pregunta de procedencia por fuente", "explica qué hacer ante una contradicción"],
        ["registro de tres fuentes y una frase"],
        ["no anotar la procedencia", "copiar textualmente sin citar"],
        "Muestra tu registro a una persona de tu casa y pídele que diga si podría encontrar cada fuente con tus datos.",
    ),
    "Anota dos fuentes que usarías para investigar un tema que te interese.",
    "Escribe una regla de tu equipo para evitar el plagio.",
)

# ================================================================ OA 21 · clase 3
lesson(
    OA21, 3,
    "Aprenderé a relacionar el cumplimiento de roles y plazos con los resultados del equipo. Sirve para entender qué pasa cuando alguien cumple o no su responsabilidad y cómo reorganizarse.",
    ["Sé asignar roles y tiempos.", "Sé investigar en equipo con varias fuentes."],
    [
        "En un equipo, la causa de un buen resultado es que cada integrante cumpla su rol y los plazos. La consecuencia es que la meta se logra a tiempo. Si un integrante no cumple, la consecuencia afecta a todos: el trabajo se atrasa, otros deben hacer más o la calidad baja. Por eso se dice que la responsabilidad es compartida.",
        "Los actores son todos los integrantes del equipo, el profesor que guía y a veces los compañeros que usarán el resultado. Cuando hay un problema, el equipo puede hacer una cadena: causa del atraso, quién fue afectado, qué se hizo y qué consecuencia tuvo. Una buena respuesta es avisar, pedir ayuda y proponer una solución.",
        "Para reorganizarse, el equipo conversa, escucha a todos y acuerda nuevas tareas o nuevos plazos. Cumplir lo que se prometió genera confianza. Y cuando alguien tiene una dificultad real, el equipo puede ayudar. Todo esto fortalece el trabajo colaborativo.",
    ],
    [("responsabilidad compartida", "idea de que el resultado depende de todos los integrantes"), ("atraso", "demora respecto del plazo acordado"), ("reorganizar", "volver a repartir tareas o tiempos"), ("confianza", "seguridad de que otros cumplirán lo que prometen"), ("calidad", "qué tan bien está hecho un trabajo")],
    [
        ("Armar la cadena", "En un equipo de 4, un integrante no entrega su parte el día acordado. El equipo debe terminar de noche. Nombra causa y consecuencia.", ["Causa: una parte no se entregó.", "Consecuencia: el equipo trabaja hasta tarde.", "El atraso afecta a todos."], "Causa: parte no entregada; consecuencia: trabajo hasta tarde"),
        ("Reorganizar", "Una integrante se enferma el día antes de la entrega. ¿Qué es mejor: avisar y repartir su tarea o esperar a ver si llega?", ["Avisar permite reorganizarse.", "Esperar puede atrasar al grupo.", "Conviene avisar y repartir."], "Avisar y repartir su tarea"),
    ],
    [
        ("Pensar que el atraso de uno no afecta al resto.", "En un equipo todo está conectado.", "Revisa quién depende de cada tarea."),
        ("Quitarle toda la responsabilidad a quien tuvo una dificultad.", "Mejor ayudar y reorganizar.", "Conversa y propón una solución."),
    ],
    [
        ("Si alguien no cumple su rol, ¿se afecta solo él o todo el equipo?", "Todo el equipo", "El resultado depende de todos."),
        ("Avisar a tiempo, ¿ayuda a reorganizar o atrasa más?", "Ayuda a reorganizar", "Permite repartir la tarea."),
        ("Cumplir lo prometido, ¿genera confianza o desconfianza?", "Confianza", "Los demás saben que pueden contar con esa persona."),
    ],
    [
        ("¿Por qué la responsabilidad es compartida en un equipo?", "Porque el resultado depende de todos los integrantes", "Cada parte es necesaria."),
        ("¿Por qué un buen equipo escucha a quien tiene una dificultad?", "Para buscar una solución entre todos", "Escuchar permite ayudar."),
        ("¿Qué consecuencia a largo plazo tiene que un equipo cumpla siempre sus plazos?", "Gana confianza y trabaja mejor", "Los integrantes se apoyan en la seguridad."),
    ],
    [
        ("Un equipo de ejemplo tiene 20 horas de trabajo repartidas por igual entre 4 integrantes. ¿Cuántas horas le tocan a cada uno?", "5", "20 dividido en 4 es 5.", "20//4"),
        ("Si un integrante no entrega sus 5 horas y las otras 3 personas se las reparten, ¿cuántas horas de trabajo hay que repartir en total entre esas 3?", "5", "Son las horas que faltaban de la persona que no cumplió."),
        ("Un equipo se atrasa 2 días en una tarea de 3 días. ¿Cuántos días en total toma la tarea?", "5", "3 más 2 son 5.", "3+2"),
    ],
    [
        ("Ema dice: «Si me atraso, que lo resuelvan los demás». ¿Qué actitud de equipo no practica?", "La responsabilidad", "Debe asumir lo que prometió o avisar."),
        ("Un integrante tuvo una dificultad y avisó. Otro dice: «Que lo echen del grupo». ¿Qué mejor respuesta hay?", "Conversar y reorganizar las tareas", "Ayudar y escuchar fortalece al equipo."),
    ],
    [
        ("Ordena la cadena: A) el equipo entrega a tiempo, B) todos cumplen sus roles, C) se acuerdan roles y plazos.", "C, B, A", "Primero el acuerdo, luego el cumplimiento y después el resultado."),
        ("Un equipo de 5 integrantes reparte 15 tareas por igual. Una persona se enferma. Las 3 tareas que le tocaban se reparten entre los otros 4. ¿Cuántas tareas por persona tenía originalmente cada integrante?", "3", "15 dividido en 5 es 3.", "15//5"),
    ],
    [("Un equipo prometió entregar el sábado y se atrasa. Un integrante propone entregar el lunes con un plan de trabajo. ¿Qué actitud muestra: responsabilidad y propuesta de solución o abandono?", "Responsabilidad y propuesta de solución", "Reconoce el atraso y propone cómo seguir.")],
    [("¿Qué es la responsabilidad compartida?", "Que el resultado depende de todos los integrantes", "Es la definición de la clase."), ("¿Qué conviene hacer si no se puede cumplir una tarea?", "Avisar a tiempo", "Así el grupo puede reorganizarse."), ("¿Qué genera cumplir lo prometido?", "Confianza", "Los demás pueden contar contigo.")],
    (
        "Elige uno de estos casos y escribe causa, actores, consecuencia y una forma de reorganizarse. Caso a) un integrante olvidó su parte del afiche; caso b) dos integrantes discutieron y no avanzaron; caso c) el equipo terminó antes y ayudó a otro grupo.",
        "Caso a: causa: olvido; actores: el integrante, el equipo y la profesora; consecuencia: retraso; solución: repartir su parte y fijar nuevo plazo.",
        ["nombra la causa y los actores", "explica la consecuencia", "propone una forma de reorganizarse"],
        ["cuatro frases escritas"],
        ["culpar sin proponer solución", "olvidar a algún actor"],
        "Lee tu respuesta a una persona de tu casa y pídele que diga si la solución es justa.",
    ),
    "Anota una responsabilidad que cumpliste esta semana y qué pasó gracias a eso.",
    "Escribe una frase para pedir ayuda a tu equipo cuando tienes una dificultad.",
)

# ================================================================ OA 21 · clase 4
lesson(
    OA21, 4,
    "Aprenderé a comparar opiniones distintas en el equipo, escuchar los argumentos de todos y llegar a un punto de vista común. Sirve para decidir juntos sin gritar y sin que uno imponga su idea.",
    ["Sé que dialogar es hablar y escuchar por turnos.", "Sé que cumplir roles ayuda a lograr la meta."],
    [
        "En un equipo es normal que haya opiniones distintas. Una opinión fundamentada es una opinión con razones y datos. Para llegar a un punto de vista común, el equipo hace varios pasos: cada persona expone su idea con razones, los demás escuchan sin interrumpir, se repite con otras palabras lo que se entendió para comprobar, se comparan las ideas con criterios y se busca un acuerdo.",
        "Los criterios son reglas iguales para comparar las ideas: si cumplen la meta, si caben en el tiempo, si se pueden hacer con los materiales y si respetan a todos. Un acuerdo puede ser elegir una idea, mezclar dos o decidir por votación. En una votación gana la que tiene más votos y las demás personas respetan el resultado.",
        "Cada persona tiene una perspectiva, es decir, una mirada según su situación. Una persona prefiere hacer un video porque le gusta filmar. Otra prefiere un afiche porque dibuja bien. Entender las perspectivas ayuda a repartir roles: quien dibuja puede hacer el afiche y quien filma puede grabar. Un punto de vista común no significa que todos piensen igual, sino que todos aceptan un acuerdo.",
    ],
    [("opinión fundamentada", "opinión con razones y datos"), ("criterio", "regla igual para comparar ideas"), ("punto de vista común", "acuerdo que aceptan todos los integrantes"), ("votación", "forma de decidir contando los votos de cada persona"), ("perspectiva", "mirada de una persona según su situación")],
    [
        ("Comparar ideas con criterios", "Idea A: hacer un video (tarda 6 días). Idea B: hacer un afiche (tarda 2 días). El plazo es de 4 días. ¿Cuál cumple el criterio «cabe en el tiempo»?", ["Comparo con el plazo de 4 días.", "El video tarda 6, que es más.", "El afiche cabe."], "La idea B, el afiche"),
        ("Contar votos", "En una votación hay 5 votos para A y 3 para B. ¿Qué idea gana?", ["Comparo los votos.", "5 es mayor que 3.", "Gana A."], "La idea A"),
    ],
    [
        ("Pensar que el punto de vista común significa que todos piensan igual.", "Significa que todos aceptan un acuerdo.", "Respeta el acuerdo aunque no sea tu idea."),
        ("Imponer la propia idea por gritar más.", "Una idea vale por sus razones, no por el volumen.", "Explica con razones y datos."),
    ],
    [
        ("Una opinión fundamentada, ¿tiene razones y datos o es solo «porque sí»?", "Tiene razones y datos", "Así se definió en el vocabulario."),
        ("En una votación, ¿gana la idea con más votos o la que propone el más alto?", "La que tiene más votos", "Así se decide por votación."),
        ("Un criterio de comparación, ¿es una regla igual para todas las ideas o una opinión?", "Una regla igual para todas las ideas", "Permite comparar con justicia."),
    ],
    [
        ("¿Por qué conviene repetir con otras palabras lo que dijo un compañero?", "Para comprobar que se entendió bien", "Así se evitan los malentendidos."),
        ("¿Por qué entender las perspectivas ayuda a repartir roles?", "Porque cada uno puede aportar según lo que hace mejor", "Se aprovechan las fortalezas."),
        ("¿Por qué se respeta el resultado de una votación?", "Porque todos acordaron decidir así", "Es una regla acordada."),
    ],
    [
        ("Idea A cuesta $2.000 y la B cuesta $6.000. El equipo tiene $4.000. ¿Cuál cumple el criterio «alcanza el dinero»?", "La A", "$2.000 es menos que $4.000; $6.000 no alcanza."),
        arith("En una votación de ejemplo hay 12 votos: 7 para A, 3 para B y el resto para C. ¿Cuántos votos recibió C?", "12-7-3", "Se resta a los 12 los votos de A y de B.", " votos"),
        ("Una compañera dibuja muy bien y otro filma muy bien. ¿Qué rol conviene asignar a quien dibuja: hacer el afiche o filmar el video?", "Hacer el afiche", "Aprovecha lo que hace mejor."),
    ],
    [
        ("Luis dice: «Mi idea es mejor porque la dije primero». ¿Qué error comete?", "Una idea vale por sus razones, no por el orden", "Debe compararse con criterios."),
        ("En un equipo hay 6 personas: 3 quieren una idea y 3 otra. ¿Qué técnica puede ayudar a decidir además de votar?", "Mezclar las dos ideas", "Un acuerdo puede combinar propuestas."),
    ],
    [
        ("Ordena los pasos para llegar a un acuerdo: A) elegir una idea o mezclarlas, B) comparar con criterios, C) cada uno expone su idea con razones.", "C, B, A", "Primero se expone, luego se compara y después se acuerda."),
        ("Tres ideas se comparan con 3 criterios: la A cumple 3, la B cumple 2 y la C cumple 1. ¿Cuántos criterios cumple la A más que la C?", "2", "3 menos 1 es 2.", "3-1"),
    ],
    [("Dos compañeros discuten por el color del afiche. Uno dice «rojo», el otro «azul». Una tercera propone usar ambos: azul para el fondo y rojo para el título. ¿Qué técnica de acuerdo usa: mezclar ideas o votar?", "Mezclar ideas", "Integra las dos propuestas.")],
    [("¿Qué es un punto de vista común?", "Un acuerdo que aceptan todos los integrantes", "Es la definición de la clase."), ("¿Qué es una opinión fundamentada?", "Una opinión con razones y datos", "Es la definición de la clase."), ("¿Cómo se decide en una votación?", "Gana la opción con más votos", "Es la regla acordada.")],
    (
        "Escenario inventado: un equipo de cuatro debe elegir el tema de su proyecto con estas opciones: A) la plaza del barrio, B) el reciclaje en la escuela, C) los oficios del barrio. Plazo: 5 días. Dos integrantes prefieren A, uno B y uno C. Escribe un diálogo corto donde cada uno diga su opinión con una razón, comparen con dos criterios (tiempo y materiales) y lleguen a un acuerdo.",
        "Ana: Prefiero la plaza porque está cerca. Beto: Yo el reciclaje porque hay datos. Carla: Los oficios requieren entrevistas. Acuerdo: elegir A porque cabe en 5 días.",
        ["cada integrante da una razón", "usa dos criterios", "termina con un acuerdo aceptado"],
        ["diálogo de seis líneas"],
        ["imponer una idea", "no usar criterios"],
        "Pide a una persona de tu casa que lea un papel y diga si el acuerdo le parece justo.",
    ),
    "Recuerda una decisión en tu curso y anota cómo se tomó.",
    "Escribe una frase para discrepar con respeto.",
)

# ================================================================ OA 21 · clase 5
lesson(
    OA21, 5,
    "Aprenderé a argumentar con evidencia las decisiones del equipo y a evaluar cómo trabajó. Sirve para mejorar la próxima vez y para explicar por qué se eligió algo.",
    ["Sé comparar ideas y llegar a un acuerdo.", "Sé que un argumento tiene afirmación, evidencia y razón."],
    [
        "Argumentar en un equipo es defender una decisión con evidencia y razones. La afirmación es lo que se sostiene, la evidencia es el dato o hecho que la apoya y la razón explica por qué. Por ejemplo: «Elegimos hacer un afiche». Evidencia: el afiche cabe en 4 días y el video necesitaba 6. Razón: el plazo es de 4 días. Límite: no sabemos si a todos les gusta más el afiche.",
        "También se evalúa el trabajo del equipo. Se pregunta si cumplió la meta, si todos cumplieron sus roles y plazos, si se escuchó a todos y qué se puede mejorar. Una evaluación honesta usa hechos: cuántas tareas se cumplieron a tiempo y cuántas no. No se culpa a nadie; se buscan soluciones.",
        "Una evaluación puede usar una tabla simple: criterio, evidencia y mejora. Por ejemplo, criterio «cumplimos los plazos»; evidencia «4 de 5 tareas a tiempo»; mejora «avisar antes si hay atraso». Así el equipo aprende de lo que hizo bien y de lo que puede mejorar.",
    ],
    [("evaluación", "revisión de cómo se hizo un trabajo para aprender y mejorar"), ("evidencia", "dato o hecho que apoya una afirmación"), ("razón", "explicación de por qué la evidencia apoya la afirmación"), ("límite", "lo que la evidencia no permite saber"), ("mejora", "cambio que se propone para hacerlo mejor la próxima vez")],
    [
        ("Identificar la evidencia", "«Elegimos el afiche porque cabía en 4 días y el video necesitaba 6.» ¿Cuál es la evidencia?", ["La afirmación es que elegimos el afiche.", "La evidencia son los días: 4 y 6.", "Los separo."], "Que el afiche cabía en 4 días y el video necesitaba 6"),
        ("Evaluar con un dato", "El equipo cumplió 4 de 5 tareas a tiempo. ¿Cuántas tareas no cumplió a tiempo?", ["Resto las cumplidas al total.", "5 menos 4.", "Es 1."], "1 tarea"),
    ],
    [
        ("Evaluar sin datos y solo con impresiones.", "Una impresión no se puede comprobar.", "Usa números o hechos."),
        ("Culpar a una persona en vez de buscar mejoras.", "El objetivo es aprender y mejorar entre todos.", "Propón cambios para el futuro."),
    ],
    [
        ("Una evaluación, ¿revisa cómo se hizo un trabajo o inventa excusas?", "Revisa cómo se hizo un trabajo", "Así se definió en el vocabulario."),
        ("«4 de 5 tareas a tiempo», ¿es un dato o una opinión?", "Un dato", "Se puede contar y comprobar."),
        ("Una mejora, ¿es un cambio para hacerlo mejor o un castigo?", "Un cambio para hacerlo mejor", "Así se definió en el vocabulario."),
    ],
    [
        ("¿Por qué conviene evaluar el trabajo en equipo?", "Para aprender y mejorar la próxima vez", "Se reconocen aciertos y fallas."),
        ("¿Por qué la evaluación no debe buscar culpables?", "Porque el objetivo es mejorar juntos", "Culpar no resuelve el problema."),
        ("¿Por qué una evaluación con datos es más útil que una impresión?", "Porque se puede comprobar", "Los datos dan precisión."),
    ],
    [
        arith("El equipo se reunió 10 veces y 8 de ellas empezaron a la hora. ¿Cuántas veces empezaron tarde?", "10-8", "Se resta las puntuales al total.", " veces"),
        ("Afirmación: «Nuestro equipo escuchó a todos». ¿Qué evidencia sirve: «las 4 personas hablaron en la reunión» o «hicimos un afiche grande»?", "Las 4 personas hablaron en la reunión", "Se relaciona con que todos fueron escuchados."),
        ("Tabla: criterio «plazos», evidencia «4 de 5 tareas a tiempo». ¿Qué mejora se relaciona con ese criterio: avisar antes si hay atraso o reunirse en otra sala?", "Avisar antes si hay atraso", "Se relaciona con el criterio de plazos."),
    ],
    [
        ("Eva dice: «Nos fue bien porque sí». ¿Qué le falta a su evaluación?", "Evidencia, es decir, un dato o hecho", "Una opinión sin dato no se puede comprobar."),
        ("Un equipo de ejemplo cumplió sus plazos una vez y concluye: «Siempre cumplimos». ¿Qué límite no respeta?", "Un caso no demuestra que siempre ocurra", "Generaliza más allá de la evidencia."),
    ],
    [
        ("Ordena la evaluación: A) proponer una mejora, B) revisar si se cumplió la meta, C) anotar la evidencia.", "B, C, A", "Primero la meta, luego la evidencia y después la mejora."),
        ("Un equipo tenía 5 roles y 4 se cumplieron. ¿Qué porcentaje de los roles se cumplió?", "80 %", "4 de 5 es 80 de cada 100.", "4*100//5"),
    ],
    [("Un equipo explica a su profesora: «Elegimos hacer una maqueta porque cabía en el tiempo y teníamos los materiales». ¿Cuántos criterios usó el equipo para justificar su decisión?", "2", "Tiempo y materiales.")],
    [("¿Qué es una evaluación?", "Una revisión de cómo se hizo un trabajo para aprender y mejorar", "Es la definición de la clase."), ("¿Qué es una mejora?", "Un cambio para hacerlo mejor la próxima vez", "Es la definición de la clase."), ("¿Debe una evaluación buscar culpables?", "No", "Busca mejorar juntos.")],
    (
        "Evalúa este equipo inventado con una tabla de tres columnas: criterio, evidencia, mejora. Datos: de 5 tareas, 4 se entregaron a tiempo; 3 de los 4 integrantes hablaron en las reuniones; el afiche se terminó un día antes del plazo. Escribe tres filas y una frase final que explique por qué el equipo logró su meta, con afirmación, evidencia y razón.",
        "Plazos: 4 de 5 tareas a tiempo; avisar antes si hay atraso. Participación: 3 de 4 hablaron; dar la palabra a todos. Meta: terminaron un día antes; mantener el calendario.",
        ["completa tres filas con datos", "propone mejoras relacionadas", "escribe una frase con afirmación, evidencia y razón"],
        ["tabla de tres filas y una frase"],
        ["inventar datos distintos a los dados", "culpar a alguien"],
        "Lee tu evaluación a una persona de tu casa y pídele que diga qué mejora le parece más útil.",
    ),
    "Anota qué hiciste bien en un trabajo en equipo reciente y qué mejorarías.",
    "Escribe un dato que usarías para saber si tu equipo cumplió sus plazos.",
)
