"""Cuaderno del estudiante, 4.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 13 (valores, armonía e interdependencia) y OA 14 (técnicas productivas ancestrales y conocimientos).

Criterio de autoría: las comunidades, las personas, los valores, las técnicas y los calendarios de práctica son
INVENTADOS y se rotulan así. No se afirma nada sobre los valores, la concepción de persona, las técnicas ni los
conocimientos astronómicos, simbólicos, matemáticos o espaciales de un pueblo concreto. Lo tradicional lo
enseñan el educador o la educadora tradicional y la comunidad; ningún ejercicio exige saber una lengua indígena.
"""
from __future__ import annotations

from student_content_lc4_a import FC4, FV4, L, M, T, W  # noqa: F401
from student_lessons import arith, ex  # noqa: F401

OA13, OA14 = "LC04 OA 13", "LC04 OA 14"

VALORES = ("Ficha de práctica (inventada). Comunidad: Valle Alto (no es un pueblo real). Fuente: doña Rosa. "
           "Testimonio: «Aquí decimos que el río nos da y nosotros le devolvemos. Quien usa el agua ayuda a limpiar el cauce. "
           "Una persona íntegra cumple su palabra, cuida lo que es de todos y ayuda a quien lo necesita.» Permiso: sí. Límite: no se cuentan las historias que la comunidad reserva.")
SIEMBRA = ("Ficha de práctica (inventada). Comunidad: Valle Alto (no es un pueblo real). Fuente: doña Rosa. Técnica: siembra en surcos en la huerta comunitaria. "
           "Etapas: 1) mirar por dónde sale el sol sobre el cerro y esperar a que terminen las lluvias, 2) preparar la tierra, 3) sembrar en surcos parejos, "
           "4) marcar cada surco con una piedra pintada que identifica a la familia, 5) cuidar y cosechar juntos, repartiendo la cosecha en partes iguales entre las familias. Permiso: sí. Límite: no se cuentan los saberes reservados.")

# ============================================================ OA 13 · Vida en armonía e interdependencia
L(
    OA13, 1,
    materials="Lápiz y hojas. La ficha está escrita aquí y es inventada.",
    use="Aprenderé a reconocer relaciones concretas entre las personas y la naturaleza, y a ver cómo se necesitan unos a otros. Sirve para entender qué significa vivir en armonía y de manera interdependiente.",
    prior=["Sé situar una fuente con permiso y límite.", "Sé que cada comunidad entiende el mundo a su manera."],
    explain=[
        "Interdependencia significa que los seres y las personas dependen unos de otros. El agua ayuda a que crezcan las plantas, las plantas alimentan a las familias y las familias cuidan el agua. Si falla uno de los eslabones, los demás se afectan. Vivir en armonía es cuidar esas relaciones para que haya equilibrio.",
        "Muchas comunidades tienen valores y principios que orientan cómo viven esas relaciones: respeto, cuidado, ayuda y cumplir la palabra, entre otros. Cada pueblo tiene su concepción de lo que es una persona íntegra, es decir, una persona coherente con sus valores. Esa concepción la cuenta cada comunidad con sus palabras.",
        "En esta clase usamos la ficha de Valle Alto (inventada). Para reconocer relaciones concretas, anotamos quién da y quién recibe en cada caso. Lo que dice la ficha vale para esa comunidad, no para todos los pueblos. Si queremos conocer los valores de un pueblo real, preguntamos al educador o educadora tradicional.",
    ],
    vocab=[("interdependencia", "relación en que los seres y las personas se necesitan unos a otros"), ("armonía", "equilibrio y buena relación entre seres y entorno"), ("valor", "idea que una comunidad considera importante para vivir bien"), ("persona íntegra", "persona coherente con los valores de su comunidad"), ("relación", "vínculo entre dos seres o cosas")],
    worked=[
        W("Reconocer relaciones", "Con la ficha de Valle Alto: «" + VALORES + "» ¿Qué relación hay entre el río y las personas?", ["El río da agua.", "Las personas ayudan a limpiar el cauce.", "Cada uno cuida al otro."], "El río da agua y las personas lo cuidan limpiándolo."),
        W("Cadena de dependencia", "El agua riega la huerta, la huerta da alimento y las familias limpian el cauce. ¿Qué pasa si nadie limpia el cauce?", ["El agua se puede ensuciar.", "La huerta recibe peor agua.", "Hay menos alimento."], "El agua se ensucia, la huerta se perjudica y hay menos alimento."),
    ],
    mistakes=[
        M("Pensar que la naturaleza solo existe para servir a las personas.", "En la ficha, las personas también cuidan y devuelven.", "Busca qué da cada uno y qué recibe."),
        M("Decir que todos los pueblos entienden la armonía igual.", "Cada pueblo tiene su concepción.", "Nombra la comunidad de la ficha."),
    ],
    R=[
        ex("Según doña Rosa, ¿qué hace quien usa el agua: ayuda a limpiar el cauce o la deja sucia?", "Ayuda a limpiar el cauce", "La ficha lo dice."),
        ex("¿Qué dice doña Rosa que hace una persona íntegra? Escribe una de las tres cosas.", "Cumple su palabra, cuida lo de todos o ayuda a quien lo necesita", "La ficha enumera las tres."),
        ex("¿Qué da el río a la comunidad según la ficha: agua o ropa?", "Agua", "La ficha lo dice."),
    ],
    C=[
        ex("¿Qué significa interdependencia? A) que los seres y las personas se necesitan unos a otros B) que cada uno vive solo", "A", "Es relación de necesidad mutua."),
        ex("Verdadero o falso: vivir en armonía es cuidar las relaciones entre seres y entorno.", "Verdadero", "Es la idea central."),
        ex("Verdadero o falso: todos los pueblos entienden lo que es una persona íntegra de la misma manera.", "Falso", "Cada pueblo tiene su concepción."),
    ],
    A=[
        ex("Ordena la cadena de dependencia de Valle Alto: a) la huerta da alimento b) el agua riega la huerta c) las familias cuidan el agua. Escribe las letras en orden.", "b, a, c", "Primero riega, luego alimenta y después las familias cuidan."),
        ex("Clasifica en DA o DEVUELVE según la ficha: a) el río entrega agua b) la comunidad limpia el cauce.", "a da, b devuelve", "El río da; la comunidad devuelve."),
        ex("Ficha inventada de Costa Clara: «El mar nos da pesca y nosotros no pescamos todos los días». ¿Qué hace la comunidad para cuidar el mar?", "No pesca todos los días", "La ficha lo dice."),
    ],
    Z=[
        ex("Felipe dice: «Como el río nos da agua, podemos ensuciarlo si queremos». ¿Qué relación olvida?", "Que la comunidad debe devolver cuidando el cauce", "La ficha habla de dar y devolver."),
        ex("¿Por qué se dice que el equilibrio se rompe si falla un eslabón? A) porque los demás dependen de él B) porque es un cuento", "A", "Todo está conectado."),
    ],
    D=[
        ex("Dos frases: 1) «En Valle Alto se cuida el cauce» 2) «Todos los pueblos limpian cauces». ¿Cuál se apoya en la ficha?", "La primera", "La segunda generaliza."),
        ex("Si quieres saber qué valores guían a un pueblo real, ¿a quién preguntas? A) al educador tradicional o a la comunidad B) a quien lo imagine", "A", "Ellos lo cuentan."),
    ],
    context=[ex("En tu patio hay plantas que se riegan con el agua de un recipiente reutilizable. ¿Qué relación de interdependencia se cuida al regar sin desperdiciar? A) agua, plantas y personas B) solo las personas", "A", "Todos se necesitan.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es la interdependencia.", "Que los seres y las personas se necesitan unos a otros", "Es la definición de la clase."),
        ex("Verdadero o falso: el valor de una comunidad vale para todos los pueblos.", "Falso", "Cada pueblo tiene sus valores."),
        ex("¿Qué haces para conocer los valores de un pueblo real? A) pregunto al educador tradicional B) los invento", "A", "Es la fuente."),
    ],
    task=T("Lee la ficha de Costa Clara (inventada): «Comunidad: Costa Clara. Fuente: don Luis. Testimonio: El mar nos da pesca y nosotros no pescamos todos los días. Las redes se arreglan entre todos. Una persona íntegra comparte lo que pesca y cuida la caleta.» Haz una cadena de al menos tres eslabones (por ejemplo: mar → pesca → familias → cuidado del mar). Escribe una frase con «da» y otra con «devuelve» y una pregunta al educador tradicional sobre los valores de tu zona.",
           "Cadena: mar → pesca → familias → cuidado del mar. El mar da pesca. La comunidad devuelve no pescando todos los días. Pregunta: ¿qué valores guían a nuestra comunidad?",
           ["usa solo datos de la ficha", "identifica lo que da y lo que devuelve", "formula una pregunta respetuosa"], ["cadena de eslabones", "dos frases", "pregunta"], ["agregar valores que la ficha no dice", "generalizar a todos los pueblos"],
           "Pedir que muestre en la ficha cada eslabón; valorar que distinga dar y devolver."),
    reinforce="Dibuja una cadena de tres eslabones con el agua, la huerta y las familias de Valle Alto.",
    extend="Escribe una relación de interdependencia en tu escuela entre dos o más personas o seres.",
)

L(
    OA13, 2,
    materials="Lápiz y hojas. La ficha está escrita aquí y es inventada.",
    use="Aprenderé a analizar la reciprocidad (dar y recibir) y sus consecuencias en la vida de una comunidad. Sirve para entender por qué los valores importan en las decisiones.",
    prior=["Sé reconocer relaciones de interdependencia.", "Sé que cada comunidad tiene sus valores."],
    explain=[
        "La reciprocidad es dar y recibir de manera equilibrada: si recibo ayuda o agua, devuelvo cuidado, trabajo o gratitud. Es un valor que sostiene la vida en comunidad. Cuando hay reciprocidad, las relaciones se mantienen sanas; cuando falta, alguien queda cargando todo o se rompe la confianza.",
        "Toda acción tiene consecuencias, es decir, resultados que ocurren a causa de ella. Una acción de cuidado, como limpiar el cauce, tiene consecuencias positivas. Una acción que no cuida, como dejar basura junto al río, puede tener consecuencias negativas para las personas, las plantas y los animales.",
        "Para analizar reciprocidad y consecuencias hacemos dos preguntas: ¿qué da y qué recibe cada uno?, ¿qué pasa si alguien no devuelve? Usamos solo los datos de la ficha. En una comunidad real, la forma de entender la reciprocidad la explica el educador o educadora tradicional.",
    ],
    vocab=[("reciprocidad", "dar y recibir de manera equilibrada"), ("consecuencia", "resultado de una acción"), ("equilibrio", "situación en que nadie da ni recibe demasiado"), ("gratitud", "reconocimiento por lo que se recibe"), ("confianza", "seguridad de que el otro cumplirá")],
    worked=[
        W("Dar y recibir", "Ficha inventada de Valle Alto: «15 familias comparten el agua. Cada familia aporta 2 horas de limpieza del cauce al mes.» ¿Cuántas horas de limpieza se juntan?", ["Hay 15 familias.", "Cada una aporta 2 horas.", "Multiplico 15 × 2."], "30 horas."),
        W("Consecuencias", "Si una familia no aporta sus 2 horas, ¿qué consecuencia puede haber?", ["Faltan 2 horas de limpieza.", "Las otras familias deben compensar o el cauce queda más sucio.", "Se afecta la confianza."], "Faltan horas de limpieza y se puede afectar la confianza."),
    ],
    mistakes=[
        M("Pensar que la reciprocidad es solo cambiar objetos.", "También incluye cuidado, trabajo y gratitud.", "Busca todo lo que se da y recibe."),
        M("Decir que no pasa nada si una persona no devuelve.", "Su falta puede afectar a los demás.", "Piensa en las consecuencias."),
    ],
    R=[
        ex("¿Cuántas horas de limpieza aporta cada familia de Valle Alto al mes según la ficha de la clase?", "2", "La ficha dice 2 horas."),
        ex("¿Qué es la reciprocidad: dar y recibir de manera equilibrada o solo recibir?", "Dar y recibir de manera equilibrada", "Es la definición."),
        ex("¿Limpiar el cauce es una acción de cuidado o de descuido?", "De cuidado", "Cuida el agua."),
    ],
    C=[
        ex("¿Qué es una consecuencia? A) resultado de una acción B) una persona de la comunidad", "A", "Ocurre a causa de lo que se hizo."),
        ex("Verdadero o falso: cuando hay reciprocidad, las relaciones se mantienen sanas.", "Verdadero", "Cuando todos aportan se sostienen."),
        ex("Verdadero o falso: dejar basura junto al río no tiene consecuencias.", "Falso", "Ensucia el agua y daña a otros."),
    ],
    A=[
        arith("En otra temporada, en Valle Alto hay 16 familias y cada una aporta 2 horas al mes de limpieza. ¿Cuántas horas se juntan?", "16*2", "Se repiten 2 horas quince veces."),
        arith("Si una de esas 16 familias no aporta sus 2 horas, ¿cuántas horas de limpieza se juntan en total? (Con las 16 familias eran 32 horas).", "32-2", "Se resta lo que falta."),
        ex("Clasifica en CONSECUENCIA POSITIVA o NEGATIVA: a) el agua llega limpia a la huerta b) el cauce se llena de basura.", "a positiva, b negativa", "El agua limpia ayuda; la basura perjudica."),
    ],
    Z=[
        ex("Camilo dice: «Si yo no aporto mis horas, igual me sirve el agua». ¿Qué principio olvida?", "La reciprocidad", "Recibe sin devolver."),
        ex("¿Por qué la confianza es importante en la reciprocidad? A) porque cada uno espera que los demás cumplan B) porque no sirve", "A", "Sin confianza se rompen los acuerdos."),
    ],
    D=[
        arith("Si 12 de las 15 familias aportan 2 horas cada una, ¿cuántas horas de limpieza se juntan?", "12*2", "Solo cuentan las familias que aportaron."),
        ex("Dos frases: 1) «Cuando todos aportan, el cauce se mantiene limpio» 2) «Da igual que algunos no aporten». ¿Cuál se apoya en la ficha de reciprocidad?", "La primera", "La segunda ignora la reciprocidad."),
    ],
    context=[ex("En tu curso cada estudiante aporta 5 minutos para ordenar la sala. Son 20 estudiantes. ¿Cuántos minutos de orden se juntan? Responde con un número.", "100", "20 × 5 = 100 minutos.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es la reciprocidad.", "Dar y recibir de manera equilibrada", "Es la definición de la clase."),
        ex("Verdadero o falso: la reciprocidad puede incluir trabajo y gratitud.", "Verdadero", "No es solo cambiar objetos."),
        ex("¿Qué pasa si una persona no devuelve lo que recibe? A) se afecta a otros B) no pasa nada", "A", "Se rompe el equilibrio."),
    ],
    task=T("Lee la ficha de Costa Clara (inventada): «Cada una de las 8 familias aporta 3 cajas de pescado a una olla común que se reparte entre las familias que más lo necesitan.» Calcula cuántas cajas se juntan y escribe el cálculo. Después escribe dos consecuencias posibles: una si todos aportan y otra si dos familias no aportan. Finaliza con una pregunta al educador tradicional sobre la reciprocidad en tu zona.",
           "8 × 3 = 24 cajas. Si todos aportan: hay 24 cajas para repartir. Si dos familias no aportan: hay 6 cajas menos, 18 cajas. Pregunta: ¿cómo se comparte lo que se produce en nuestra comunidad?",
           ["calcula bien", "describe consecuencias coherentes", "formula una pregunta respetuosa"], ["cálculo escrito", "dos consecuencias", "pregunta"], ["inventar valores que la ficha no dice", "olvidar la consecuencia de no aportar"],
           "Revisar el cálculo; pedir que explique la reciprocidad."),
    reinforce="Escribe una acción de reciprocidad que ocurra en tu curso.",
    extend="Explica con tus palabras cómo se relaciona la reciprocidad con ser una persona íntegra en la ficha de Valle Alto.",
)

L(
    OA13, 3,
    materials="Lápiz y hojas. Las fichas están escritas aquí y son inventadas.",
    use="Aprenderé a comparar decisiones de cuidado de dos comunidades inventadas sin decir cuál es mejor. Sirve para reconocer que hay varias formas de cuidar.",
    prior=["Sé analizar reciprocidad y consecuencias.", "Sé comparar sin jerarquizar."],
    explain=[
        "Una decisión de cuidado es una elección que toma una comunidad para proteger algo: el agua, el mar, las plantas o a las personas. Dos comunidades pueden proteger lo que necesitan de maneras distintas, según su territorio y sus valores. Comparar nos ayuda a ver esas diferencias.",
        "Para comparar usamos tres preguntas: ¿qué se cuida?, ¿quiénes participan? y ¿qué consecuencia se evita? Por ejemplo, Valle Alto cuida el agua con turnos y limpieza; Costa Clara cuida el mar con descansos de pesca. No son iguales, pero ambas buscan que el recurso dure.",
        "No decimos que una decisión es mejor que otra. Cada una responde a su territorio. Comparar sirve para comprender, no para calificar. Y si queremos conocer las decisiones de cuidado de un pueblo real, la guía es el educador o educadora tradicional.",
    ],
    vocab=[("decisión de cuidado", "elección de una comunidad para proteger algo"), ("recurso", "cosa de la naturaleza que se usa, como el agua o el pescado"), ("turno", "orden para usar algo por partes"), ("descanso", "tiempo en que no se usa un recurso para que se recupere"), ("comparar", "mirar semejanzas y diferencias")],
    worked=[
        W("Comparar con tres preguntas", "Valle Alto (inventada): «Cuidamos el agua con turnos entre las familias y limpiando el cauce». Costa Clara (inventada): «Cuidamos el mar con días de descanso de pesca». Compara.", ["Se cuida: agua en Valle Alto, mar en Costa Clara.", "Participan: las familias en ambas.", "Se evita: que falte el recurso."], "Cuidan recursos distintos de maneras distintas, y ambas evitan que falte el recurso."),
        W("Evitar jerarquizar", "Un niño dice: «El descanso de pesca es mejor que los turnos de agua». ¿Qué se responde?", ["Cada decisión responde a su territorio.", "No se puede decir que una es mejor.", "Se comparan sin ordenar."], "No se jerarquiza: cada decisión responde a su territorio."),
    ],
    mistakes=[
        M("Decir cuál comunidad cuida mejor.", "Cada una responde a su territorio.", "Compara sin calificar."),
        M("Pensar que todas las comunidades cuidan igual.", "Cada una elige según lo que necesita.", "Nombra las decisiones de cada una."),
    ],
    R=[
        ex("¿Qué cuida Valle Alto con turnos y limpieza: el agua o el mar?", "El agua", "Lo dice la ficha."),
        ex("¿Qué cuida Costa Clara con descansos de pesca: el mar o el cerro?", "El mar", "Lo dice la ficha."),
        ex("¿Qué es un turno: orden para usar algo por partes o un tipo de pescado?", "Orden para usar algo por partes", "Es la definición."),
    ],
    C=[
        ex("¿Qué es una decisión de cuidado? A) una elección para proteger algo B) un regalo", "A", "Protege un recurso o a las personas."),
        ex("Verdadero o falso: comparar sirve para decir cuál comunidad es mejor.", "Falso", "Sirve para comprender."),
        ex("Verdadero o falso: dos comunidades pueden cuidar de maneras distintas y ambas valer.", "Verdadero", "Cada una responde a su territorio."),
    ],
    A=[
        ex("Escribe una semejanza entre las decisiones de Valle Alto y Costa Clara.", "Ambas cuidan un recurso para que no falte", "Es lo que comparten."),
        ex("Clasifica en VALLE ALTO o COSTA CLARA: a) turnos de agua b) días de descanso de pesca.", "a Valle Alto, b Costa Clara", "Cada decisión es de su comunidad."),
        ex("Completa: Valle Alto cuida el agua con turnos y limpieza; Costa Clara cuida el mar con ___ de pesca. Escribe la palabra.", "descansos", "Es la decisión de Costa Clara."),
    ],
    Z=[
        ex("Pedro dice: «Los turnos son mejores que los descansos porque son más ordenados». ¿Qué error comete?", "Jerarquiza decisiones que responden a territorios distintos", "No se califica."),
        ex("¿Qué consecuencia evita el descanso de pesca? A) que el mar se quede sin peces B) que la gente se canse", "A", "Permite que el recurso se recupere."),
    ],
    D=[
        arith("Costa Clara descansa 2 días a la semana de pesca. ¿Cuántos días pesca en una semana de 7 días?", "7-2", "Se restan los días de descanso."),
        ex("Dos conclusiones: 1) «Las dos comunidades cuidan para que el recurso dure» 2) «Solo una comunidad cuida». ¿Cuál es válida con las fichas?", "La primera", "Ambas fichas muestran cuidado."),
    ],
    context=[ex("En tu escuela deciden cuidar el agua del patio con turnos de riego por curso. ¿Se parece más a Valle Alto o a Costa Clara? Responde con el nombre.", "Valle Alto", "Usa turnos para cuidar el agua.")],
    selfcheck=[
        ex("Escribe las tres preguntas para comparar decisiones de cuidado.", "¿Qué se cuida?, ¿quiénes participan? y ¿qué consecuencia se evita?", "Son las de la clase."),
        ex("Verdadero o falso: una decisión de cuidado es mejor porque es más conocida.", "Falso", "No se jerarquiza."),
        ex("¿Qué haces para conocer decisiones de cuidado de un pueblo real? A) pregunto al educador tradicional B) las invento", "A", "Es la fuente."),
    ],
    task=T("Compara las decisiones de Valle Alto (turnos de agua y limpieza del cauce) y de Costa Clara (descansos de pesca) con una tabla de tres filas (qué se cuida, quiénes participan, consecuencia que se evita) y dos columnas. Escribe una semejanza, una diferencia y una frase que explique por qué no se debe decir cuál es mejor.",
           "Qué se cuida: agua / mar. Participan: las familias / las familias. Consecuencia que se evita: que falte agua / que falte pescado. Semejanza: ambas cuidan un recurso. Diferencia: cuidan recursos distintos con decisiones distintas. No es mejor una: cada una responde a su territorio.",
           ["completa la tabla con datos de las fichas", "escribe semejanza y diferencia", "explica por qué no jerarquiza"], ["tabla", "tres frases"], ["calificar una comunidad como mejor", "agregar datos que no están"],
           "Pedir que justifique cada casilla; valorar que no jerarquice."),
    reinforce="Marca con un color las semejanzas y con otro las diferencias en tu tabla.",
    extend="Escribe una decisión de cuidado de tu curso y compárala con una de las dos comunidades.",
)

L(
    OA13, 4,
    materials="Lápiz y hojas. Los materiales de la acción (plantas del patio, recipientes reutilizables) son opcionales; no se usan objetos peligrosos.",
    use="Aprenderé a proponer una acción pequeña y segura que cuide algo de mi entorno, inspirada en los valores de una ficha. Sirve para pasar del aprendizaje a la acción.",
    prior=["Sé analizar reciprocidad y comparar decisiones de cuidado.", "Sé que las acciones tienen consecuencias."],
    explain=[
        "Una acción situada es una acción que responde a un lugar concreto, a un problema real y a quienes viven allí. No se trata de copiar lo que hace otra comunidad, sino de inspirarnos en sus valores, como el cuidado y la reciprocidad, para pensar algo para nuestro entorno, por ejemplo, el patio o la sala.",
        "Una buena propuesta tiene cinco partes: qué observo (el problema), qué valor me guía (cuidado, reciprocidad, respeto), qué acción pequeña propongo (segura y posible), quién participa y a quién consulto. También se piensa cómo se revisará si funcionó. Las acciones son pequeñas y no ponen a nadie en riesgo.",
        "Cuando una acción involucra a una comunidad real, se consulta antes al educador tradicional o a la comunidad y no se actúa en sus lugares sin permiso. En esta clase proponemos acciones para la escuela, que sí podemos decidir con nuestros docentes.",
    ],
    vocab=[("acción situada", "acción pensada para un lugar y un problema concretos"), ("propuesta", "idea que se presenta para que otros la evalúen"), ("participar", "ser parte de una acción"), ("revisar", "comprobar si lo hecho funcionó"), ("seguro", "que no pone en riesgo a nadie")],
    worked=[
        W("Armar una propuesta", "Observo que en el patio sobran restos de papel. Quiero cuidar el entorno inspirado en el cuidado de Valle Alto. ¿Qué propongo?", ["Observo: restos de papel en el patio.", "Valor: cuidado.", "Acción: poner una caja para reutilizar papel y turnos de curso para vaciarla."], "Caja de reutilización de papel con turnos por curso."),
        W("Revisar la acción", "¿Cómo compruebo si funcionó?", ["Cuento cuántos papeles quedan en el patio antes y después.", "Comparo los números.", "Pregunto a mis compañeros."], "Comparo el conteo y escucho a mis compañeros."),
    ],
    mistakes=[
        M("Proponer una acción grande o riesgosa.", "Debe ser segura y posible.", "Elige una acción pequeña."),
        M("Copiar una práctica de una comunidad sin consultarla.", "Esa práctica es de ellos.", "Inspírate en su valor, no en su práctica."),
    ],
    R=[
        ex("¿Una acción situada responde a un lugar concreto o a cualquier lugar?", "A un lugar concreto", "Es la definición."),
        ex("¿Qué debe ser una acción para un curso: segura o riesgosa?", "Segura", "No debe poner en riesgo a nadie."),
        ex("¿Cuántas partes tiene una propuesta en esta clase? Escribe el número.", "5", "Son observo, valor, acción, quién participa y revisión."),
    ],
    C=[
        ex("¿Para qué sirve revisar la acción? A) para comprobar si funcionó B) para castigar", "A", "Se evalúa el resultado."),
        ex("Verdadero o falso: puedo copiar una práctica de una comunidad si me gusta.", "Falso", "Se necesita permiso; lo que se toma es el valor."),
        ex("Verdadero o falso: una acción pequeña también puede cuidar el entorno.", "Verdadero", "Importa que sea posible y constante."),
    ],
    A=[
        ex("Ordena los pasos: a) revisar si funcionó b) observar el problema c) proponer una acción segura. Escribe las letras.", "b, c, a", "Primero se observa, luego se propone y al final se revisa."),
        arith("Un curso de 28 estudiantes pone una caja de reutilización de papel y cada estudiante aporta 3 hojas. ¿Cuántas hojas se reutilizan?", "28*3", "Se repiten 3 hojas veintiocho veces."),
        ex("Clasifica cada acción en SEGURA o RIESGOSA: a) poner una caja de reutilización de papel b) subirse a un árbol para recoger basura.", "a segura, b riesgosa", "La primera no pone en riesgo; la segunda sí."),
    ],
    Z=[
        ex("Ema propone limpiar un lugar importante de una comunidad real sin avisarle. ¿Qué falla?", "No consultó ni pidió permiso", "Esos lugares se tocan con permiso."),
        ex("¿Por qué conviene decir qué valor guía tu propuesta? A) porque justifica la acción B) porque la hace larga", "A", "Explica el sentido."),
    ],
    D=[
        arith("Si en la semana se juntan 84 hojas y el curso las usa en 7 días por igual, ¿cuántas hojas se usan por día?", "84//7", "Se reparte en partes iguales."),
        ex("Dos propuestas: 1) «Regar las plantas del patio con una botella reutilizable, con turnos» 2) «Quemar la basura del patio». ¿Cuál es adecuada?", "La primera", "La segunda es peligrosa."),
    ],
    context=[ex("En tu escuela hay plantas que se secan en el verano. ¿Qué propuesta es adecuada y segura? A) turnos de riego con un recipiente reutilizable, con ayuda de un adulto B) usar productos desconocidos", "A", "Es segura y posible.")],
    selfcheck=[
        ex("Nombra dos partes de una propuesta de acción.", "Dos entre: qué observo, valor, acción, quién participa, revisión", "Están en la explicación."),
        ex("Verdadero o falso: una acción puede poner en riesgo a alguien si es muy útil.", "Falso", "Siempre debe ser segura."),
        ex("¿Qué haces antes de actuar en un lugar de una comunidad real? A) consulto y pido permiso B) actúo sin avisar", "A", "Se respeta a la comunidad."),
    ],
    task=T("Propón una acción pequeña y segura para cuidar algo de tu escuela o de tu casa. Completa una ficha con cinco partes: qué observo, qué valor me guía (puedes usar uno de la ficha de Valle Alto: cuidar lo de todos), qué acción propongo, quién participa y cómo reviso si funcionó. Si es posible, hazla con ayuda de una persona de tu casa o de un docente y no uses objetos peligrosos.",
           "Observo: restos de papel en el patio. Valor: cuidar lo de todos. Acción: caja para reutilizar papel con turnos de aseo. Participa: mi curso. Revisión: cuento los papeles antes y después.",
           ["completa las cinco partes", "la acción es pequeña y segura", "incluye cómo revisará"], ["ficha de cinco partes", "acción registrada"], ["acción riesgosa", "copiar una práctica sin permiso"],
           "Pedir que explique el valor de la propuesta; valorar la seguridad de la acción."),
    reinforce="Revisa que tu acción sea segura con una lista de tres preguntas.",
    extend="Explica cómo cambiaría tu propuesta si participara otro curso y cómo lo consultarías.",
)

# ============================================================ OA 14 · Técnicas productivas ancestrales y vida comunitaria
L(
    OA14, 1,
    materials="Lápiz y hojas. La ficha está escrita aquí y es inventada.",
    use="Aprenderé a identificar el propósito de una técnica productiva, quién la cuenta y con qué permiso. Sirve para comprender que producir también es un saber de la comunidad.",
    prior=["Sé situar una fuente con permiso y límite.", "Sé que la producción es lo que una comunidad cultiva, pesca o elabora."],
    explain=[
        "Una técnica productiva es una manera organizada de producir algo: sembrar, pescar, tejer, elaborar alimentos. Las comunidades originarias han desarrollado técnicas que se transmiten de generación en generación y que se siguen practicando y adaptando hoy. Producir es también una forma de saber.",
        "Toda técnica tiene un propósito: para qué se hace. Puede ser alimentar a las familias, intercambiar con otras comunidades o cuidar el territorio. Para estudiarla, preguntamos: ¿cuál es su propósito?, ¿quién la cuenta?, ¿hay permiso para compartirla? y ¿qué parte no se cuenta?",
        "En esta unidad usamos una técnica inventada de Valle Alto: la siembra en surcos. No describe ninguna técnica real de ningún pueblo. Sirve para practicar cómo se lee una ficha de técnica y para identificar sus conocimientos astronómicos, simbólicos, matemáticos y espaciales. Si el trabajo es sobre una técnica real, el educador tradicional es el guía.",
    ],
    vocab=[("técnica productiva", "manera organizada de producir algo"), ("propósito", "para qué se hace algo"), ("etapa", "paso dentro de un proceso"), ("saber", "conocimiento que se aprende y se enseña"), ("autorización", "permiso para compartir")],
    worked=[
        W("Leer la ficha", "Lee: «" + SIEMBRA + "» ¿Cuál es el propósito, quién cuenta y hay permiso?", ["Propósito: sembrar en surcos para cosechar en la huerta comunitaria.", "Cuenta doña Rosa.", "Hay permiso."], "Propósito: sembrar y cosechar; fuente: doña Rosa; permiso: sí."),
        W("Identificar el límite", "¿Qué no se cuenta en la ficha?", ["Busco «Límite».", "Dice que no se cuentan los saberes reservados.", "No se debe completar."], "Los saberes reservados."),
    ],
    mistakes=[
        M("Pensar que producir es solo trabajo y no saber.", "Las técnicas reúnen muchos conocimientos.", "Busca qué se necesita saber para hacerla."),
        M("Decir que la siembra en surcos es la técnica de todos los pueblos.", "La ficha habla de una comunidad inventada.", "Nombra la comunidad."),
    ],
    R=[
        ex("Según la ficha, ¿qué se hace en la huerta comunitaria: sembrar en surcos o construir un bote?", "Sembrar en surcos", "La ficha lo dice."),
        ex("¿Quién cuenta la técnica de la ficha: doña Rosa o don Luis?", "Doña Rosa", "La ficha la nombra."),
        ex("¿Hay permiso para usar la ficha? Responde Sí o No.", "Sí", "La ficha lo dice."),
    ],
    C=[
        ex("¿Qué es una técnica productiva? A) manera organizada de producir algo B) un tipo de juego", "A", "Es una manera organizada de producir."),
        ex("Verdadero o falso: toda técnica tiene un propósito.", "Verdadero", "Se hace para algo."),
        ex("Verdadero o falso: la técnica de siembra de esta ficha es real y de todos los pueblos.", "Falso", "Es un ejemplo inventado."),
    ],
    A=[
        ex("Ficha inventada de Costa Clara: «Técnica: secado de pescado al sol sobre rejillas. Propósito: guardar alimento para el invierno. Fuente: don Luis. Permiso: sí». Escribe el propósito.", "Guardar alimento para el invierno", "La ficha lo dice."),
        ex("Une cada técnica con su propósito. 1) siembra en surcos 2) secado de pescado a) guardar alimento b) cosechar en la huerta", "1-b, 2-a", "La siembra es para cosechar; el secado es para guardar."),
        ex("Una ficha trae la técnica y el propósito, pero no dice quién la cuenta. ¿Puedes usarla en tu trabajo? Responde Sí o No.", "No", "Falta la fuente."),
    ],
    Z=[
        ex("Tomás dice: «La siembra en surcos de Valle Alto la usan todos los pueblos». ¿Qué error comete?", "Generaliza una ficha inventada a todos los pueblos", "Cada comunidad tiene su técnica."),
        ex("¿Por qué conviene declarar el límite de la ficha? A) porque reconoce lo que no se cuenta B) porque alarga el texto", "A", "Respeta lo reservado."),
    ],
    D=[
        ex("Dos textos: 1) «Según doña Rosa, en Valle Alto se siembra en surcos» 2) «Los indígenas siembran en surcos». ¿Cuál identifica la fuente?", "El primero", "El segundo no nombra la fuente."),
        ex("Si quieres saber cómo siembra un pueblo real, ¿a quién preguntas? A) al educador tradicional o a la comunidad B) a un video al azar", "A", "Son la fuente."),
    ],
    context=[ex("Tu curso hará una huerta escolar y alguien dice «copiamos la técnica de Valle Alto». ¿Qué respondes? A) es un ejemplo inventado; consultamos a un profesor o a una persona de la comunidad real B) sí", "A", "No se copia una técnica real sin consultar.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es una técnica productiva.", "Manera organizada de producir algo", "Es la definición de la clase."),
        ex("Verdadero o falso: una técnica puede enseñarse sin nombrar a quien la guarda.", "Falso", "Se nombra la fuente."),
        ex("¿Qué haces si falta el permiso? A) me detengo y pregunto B) la uso igual", "A", "Sin permiso no se comparte."),
    ],
    task=T("Lee la ficha de práctica de Costa Clara: «Técnica: secado de pescado al sol sobre rejillas. Propósito: guardar alimento para el invierno. Fuente: don Luis. Permiso: sí. Límite: no se cuentan las historias reservadas de la caleta.» Completa una tabla con cinco filas: técnica, propósito, fuente, permiso y límite. Escribe una frase que atribuya bien la técnica y una pregunta al educador tradicional sobre una técnica de tu zona.",
           "Técnica: secado de pescado. Propósito: guardar alimento. Fuente: don Luis. Permiso: sí. Límite: historias reservadas. Frase: La comunidad de Costa Clara seca pescado para guardar alimento. Pregunta: ¿qué técnicas de producción se practican en nuestra comunidad?",
           ["completa las cinco filas con datos de la ficha", "atribuye bien la técnica", "formula una pregunta respetuosa"], ["tabla de cinco filas", "frase de atribución", "pregunta"], ["generalizar a todos los pueblos", "agregar datos que no están"],
           "Pedir que muestre en la ficha cada dato; valorar que nombre la comunidad."),
    reinforce="Subraya en la ficha de Valle Alto el propósito y la fuente con colores distintos.",
    extend="Explica por qué producir es también una forma de saber.",
)

L(
    OA14, 2,
    materials="Lápiz y hojas. La ficha está escrita aquí y es inventada.",
    use="Aprenderé a observar las etapas de una técnica y los conocimientos que hay detrás: astronómicos, simbólicos, matemáticos y espaciales. Sirve para valorar el saber de las comunidades.",
    prior=["Sé identificar propósito, fuente y permiso de una técnica.", "Sé contar, multiplicar y repartir."],
    explain=[
        "Una técnica productiva se hace por etapas, y en cada etapa se usan conocimientos. Los conocimientos astronómicos son los que observan el cielo, como el sol, la luna o las estrellas, para saber cuándo hacer algo. Los matemáticos incluyen contar, medir y repartir. Los espaciales ordenan dónde va cada cosa. Los simbólicos usan marcas o señales con significado para la comunidad.",
        "En la técnica inventada de Valle Alto, la comunidad mira por dónde sale el sol sobre el cerro (astronómico), espera que terminen las lluvias, siembra en surcos parejos (espacial), marca cada surco con una piedra pintada (simbólico) y reparte la cosecha en partes iguales entre las familias (matemático).",
        "Esto es un ejemplo inventado: no afirma que un pueblo real haga estas cosas. Lo que sí aprendemos es a mirar una técnica y reconocer que detrás hay mucho saber. Para conocer los conocimientos de una técnica real, el educador o educadora tradicional es quien explica qué se puede compartir.",
    ],
    vocab=[("conocimiento astronómico", "saber que observa el cielo, como el sol y la luna, para decidir cuándo hacer algo"), ("conocimiento matemático", "saber que cuenta, mide y reparte"), ("conocimiento espacial", "saber que ordena dónde va cada cosa"), ("conocimiento simbólico", "saber que usa marcas con significado"), ("surco", "línea de tierra donde se siembra")],
    worked=[
        W("Identificar el saber de cada etapa", "Con la ficha de siembra de Valle Alto: ¿qué conocimiento hay al mirar por dónde sale el sol y al marcar cada surco con una piedra pintada?", ["Mirar por dónde sale el sol: observa el cielo, astronómico.", "Marcar el surco con una piedra pintada: usa una marca con significado, simbólico.", "Los clasifico."], "Astronómico en la primera etapa; simbólico en la marca del surco."),
        W("Cuenta de surcos", "La huerta tiene 24 surcos y son 6 familias. Si se reparten por igual, ¿cuántos surcos corresponden a cada una?", ["Hay 24 surcos.", "Son 6 familias.", "Divido 24 ÷ 6."], "4 surcos por familia."),
    ],
    mistakes=[
        M("Pensar que sembrar es solo echar semillas.", "Detrás hay observación, orden y cuentas.", "Mira las etapas completas."),
        M("Creer que el saber astronómico es solo mirar el cielo con telescopio.", "Es observar el cielo para decidir actividades.", "Busca qué se observa y para qué."),
    ],
    R=[
        ex("En la ficha de siembra, ¿qué se mira por dónde sale: el sol sobre el cerro o el mar?", "El sol sobre el cerro", "La ficha lo dice."),
        ex("¿Con qué se marca cada surco según la ficha: con una piedra pintada o con una bandera?", "Con una piedra pintada", "La ficha lo dice."),
        ex("¿Cuántas etapas tiene la técnica de la ficha? Escribe el número.", "5", "La ficha enumera cinco etapas."),
    ],
    C=[
        ex("¿Qué es un conocimiento matemático en una técnica? A) el que cuenta, mide y reparte B) el que observa el cielo", "A", "Cuenta, mide y reparte."),
        ex("Verdadero o falso: un conocimiento astronómico observa el cielo para decidir cuándo hacer algo.", "Verdadero", "Es la definición."),
        ex("Verdadero o falso: la técnica de la ficha es real y la hace un pueblo concreto.", "Falso", "Es un ejemplo inventado."),
    ],
    A=[
        arith("En la huerta de Valle Alto hay 24 surcos y son 6 familias. Si cada familia recibe la misma cantidad, ¿cuántos surcos corresponden a cada familia?", "24//6", "Se reparte en partes iguales."),
        ex("Clasifica en ASTRONÓMICO, MATEMÁTICO, ESPACIAL o SIMBÓLICO según la ficha: a) sembrar en surcos parejos b) marcar con piedra pintada c) mirar por dónde sale el sol.", "a espacial, b simbólico, c astronómico", "Ordenar surcos es espacial; la marca es simbólica; mirar el sol es astronómico."),
        arith("Si cada surco tiene 8 semillas, ¿cuántas semillas se necesitan para los 24 surcos?", "24*8", "Se repiten 8 semillas veinticuatro veces."),
    ],
    Z=[
        ex("Lucía dice: «Contar los surcos no es un saber». ¿Qué saber matemático hay en contar y repartir?", "Contar y repartir en partes iguales", "Es un saber matemático."),
        ex("¿Por qué observar por dónde sale el sol ayuda a sembrar? A) porque permite reconocer el momento del año B) porque da suerte", "A", "Se observa el cielo para ubicar el momento."),
    ],
    D=[
        arith("La huerta de Valle Alto tiene 6 familias y cada una cuida 4 surcos. Cada surco tiene 8 semillas. ¿Cuántas semillas hay en total?", "6*4*8", "Primero los surcos totales y luego las semillas."),
        ex("Dos frases: 1) «La comunidad de la ficha usa saberes astronómicos y matemáticos para sembrar» 2) «Todos los pueblos usan los mismos saberes». ¿Cuál se apoya en la ficha?", "La primera", "La segunda generaliza."),
    ],
    context=[ex("En tu huerta escolar tienes 20 semillas y quieres repartirlas en 4 surcos iguales. ¿Cuántas van en cada surco? Responde con un número.", "5", "20 ÷ 4 = 5.")],
    selfcheck=[
        ex("Nombra los cuatro tipos de conocimiento de la clase.", "Astronómico, matemático, espacial y simbólico", "Son los de la clase."),
        ex("Verdadero o falso: sembrar solo requiere echar semillas.", "Falso", "Detrás hay observación, orden y cuentas."),
        ex("¿Dónde conoces una técnica real? A) con el educador tradicional B) inventándola", "A", "Es la guía."),
    ],
    task=T("Lee la ficha de siembra de Valle Alto (inventada) de esta clase. Haz una tabla con las cinco etapas y escribe al lado qué conocimiento hay en cada una (astronómico, espacial, matemático, simbólico) o «no se indica». Después calcula con 18 surcos y 6 familias cuántos surcos corresponden a cada familia y escribe el cálculo. No agregues etapas que la ficha no tiene.",
           "Etapa 1: astronómico (mirar el sol sobre el cerro). Etapa 2: no se indica. Etapa 3: espacial (surcos parejos). Etapa 4: simbólico (piedra pintada). Etapa 5: matemático (repartir en partes iguales). Cálculo: 18 ÷ 6 = 3 surcos por familia.",
           ["asocia conocimientos con las etapas de la ficha", "calcula bien", "no inventa etapas"], ["tabla de etapas", "cálculo"], ["agregar conocimientos que la ficha no dice", "olvidar la cuenta"],
           "Pedir que muestre en la ficha cada etapa; revisar el cálculo."),
    reinforce="Subraya en la ficha cada conocimiento con un color distinto.",
    extend="Escribe una pregunta que le harías al educador tradicional sobre los conocimientos de una técnica de tu zona.",
)

L(
    OA14, 3,
    materials="Un vaso transparente o un frasco limpio, algodón o papel absorbente, 3 semillas de poroto o lenteja secas, agua y una regla. Con ayuda de una persona de tu casa. No se prueban las semillas ni se usan productos químicos.",
    use="Aprenderé a practicar una versión autorizada y segura de una técnica de siembra: germinar semillas y registrar con medidas. Sirve para experimentar el valor de observar, contar y cuidar.",
    prior=["Sé reconocer las etapas y los conocimientos de una técnica.", "Sé medir con una regla en centímetros."],
    explain=[
        "Practicar una versión autorizada significa hacer una actividad inspirada en una técnica, con permiso y sin copiar lo que pertenece a una comunidad. La ficha de Valle Alto (inventada) nos autoriza a practicar una versión escolar: germinar semillas en el aula. No es la técnica real de ningún pueblo.",
        "El germinador es una forma segura de observar el inicio del crecimiento. Se pone algodón húmedo en un vaso y se colocan 3 semillas contra la pared del vaso. Cada día se observa, se agrega un poco de agua si el algodón se seca y se mide con una regla cuánto creció la raíz o el tallo. Registrar en una tabla muestra el saber de observar y contar.",
        "Seguridad: las semillas no se comen ni se llevan a la boca, las manos se lavan después y el vaso es de plástico o de un material que no se rompa. Se trabaja con ayuda de una persona de la casa o de un docente. Los resultados pueden variar y no hay un resultado único correcto.",
    ],
    vocab=[("germinar", "comenzar a crecer una semilla"), ("germinador", "recipiente donde se hace germinar una semilla"), ("registrar", "anotar lo que se observa"), ("raíz", "parte de la planta que crece hacia abajo"), ("tallo", "parte de la planta que crece hacia arriba")],
    worked=[
        W("Armar el germinador", "¿Qué pasos sigo para armar el germinador?", ["Pongo algodón húmedo en el vaso.", "Coloco 3 semillas contra la pared.", "Dejo el vaso en un lugar con luz y observo cada día."], "Algodón húmedo, 3 semillas y observación diaria."),
        W("Registrar medidas", "El día 3 una raíz mide 1 cm y el día 5 mide 3 cm. ¿Cuánto creció entre el día 3 y el día 5?", ["Medida del día 3: 1 cm.", "Medida del día 5: 3 cm.", "Resto 3 − 1."], "2 cm."),
    ],
    mistakes=[
        M("Empapar el algodón con demasiada agua.", "Las semillas pueden pudrirse.", "Mantén el algodón húmedo, no mojado."),
        M("Anotar solo lo que me gusta y no lo que observo.", "Pierdo datos para comparar.", "Registra todo, aunque una semilla no crezca."),
    ],
    R=[
        ex("¿Dónde se ponen las semillas para germinar: en un germinador con algodón húmedo o dentro de la boca?", "En un germinador con algodón húmedo", "Es el procedimiento seguro."),
        ex("¿Se comen las semillas del germinador? Responde Sí o No.", "No", "No se llevan a la boca."),
        ex("¿Qué instrumento mide cuánto creció la raíz: una regla o una balanza?", "Una regla", "Se mide en centímetros."),
    ],
    C=[
        ex("¿Qué es germinar? A) comenzar a crecer una semilla B) cortar una planta", "A", "Es el inicio del crecimiento."),
        ex("Verdadero o falso: todas las semillas deben crecer igual de rápido.", "Falso", "Los resultados pueden variar."),
        ex("Verdadero o falso: esta práctica es una técnica real de un pueblo originario.", "Falso", "Es una versión escolar inspirada en una ficha inventada."),
    ],
    A=[
        arith("El día 2 la raíz de una semilla mide 1 cm y el día 6 mide 5 cm. ¿Cuántos centímetros creció?", "5-1", "Se resta la medida inicial."),
        arith("Si pones 3 semillas en cada uno de 4 vasos, ¿cuántas semillas usas en total?", "3*4", "Se repiten 3 semillas cuatro veces."),
        ex("Si el día 1 la raíz mide 0 cm, el día 3 mide 1 cm y el día 5 mide 3 cm, ¿en qué intervalo creció más: del día 1 al 3 o del 3 al 5?", "Del día 3 al 5", "Creció 2 cm entre los días 3 y 5, y 1 cm entre los días 1 y 3."),
    ],
    Z=[
        ex("Tomás dice: «Mi semilla no creció, así que me equivoqué y mi registro no vale». ¿Qué responde la clase?", "Registrar que no creció también es un dato válido", "Los resultados pueden variar."),
        ex("¿Por qué se toma la medida a la misma hora cada día? A) para comparar mejor B) para cansarse", "A", "Las medidas son más comparables."),
    ],
    D=[
        ex("Un germinador tiene 3 semillas y solo 2 crecieron. ¿Cuántas no crecieron? Responde con un número.", "1", "3 − 2 = 1."),
        ex("¿Por qué no se debe decir que esta práctica es «la técnica de la comunidad»? A) porque es una versión escolar inspirada en una ficha inventada B) porque es difícil", "A", "No es una técnica real."),
    ],
    context=[ex("Una compañera quiere probar las semillas del germinador. ¿Qué le dices? A) no se comen, solo se observan B) pruébalas", "A", "Es una norma de seguridad.")],
    selfcheck=[
        ex("Escribe dos pasos del germinador.", "Algodón húmedo y semillas contra la pared", "Son pasos de la clase."),
        ex("Verdadero o falso: puedo registrar solo las semillas que crecieron.", "Falso", "Se registra todo."),
        ex("¿Qué haces después de tocar las semillas? A) me lavo las manos B) me llevo las manos a la boca", "A", "Es una norma básica de seguridad."),
    ],
    task=T("Arma tu germinador con ayuda de una persona de tu casa: vaso, algodón húmedo y 3 semillas. Observa durante 5 días. Haz una tabla con dos columnas (día y medida en centímetros) y anota cuánto mide la raíz o el tallo de una semilla cada día. Calcula cuánto creció entre el primer y el último día y escribe una frase que diga qué conocimiento usaste (matemático, por contar y medir). Si no tienes semillas, usa estos datos de práctica (inventados): día 1, 0 cm; día 3, 1 cm; día 5, 3 cm.",
           "Día 1: 0 cm. Día 2: 0 cm. Día 3: 1 cm. Día 4: 2 cm. Día 5: 3 cm. Creció 3 − 0 = 3 cm. Usé conocimiento matemático al medir y comparar.",
           ["registra medidas cada día", "calcula el crecimiento", "nombra el conocimiento usado"], ["tabla de medidas", "cálculo", "frase"], ["anotar solo lo que crece", "decir que es una técnica real"],
           "Pedir que muestre sus medidas; valorar el registro honesto."),
    reinforce="Dibuja cómo se ve tu semilla en el día 1 y en el último día.",
    extend="Escribe una pregunta que le harías a una persona de tu comunidad sobre cómo se prepara la tierra antes de sembrar.",
)

L(
    OA14, 4,
    materials="Lápiz y hojas. La ficha está escrita aquí y es inventada.",
    use="Aprenderé a relacionar la producción con la vida de la comunidad: quiénes participan, cómo se reparte y para qué sirve. Sirve para comprender que la técnica es parte de la vida en común.",
    prior=["Sé identificar etapas y conocimientos de una técnica.", "Sé repartir en partes iguales."],
    explain=[
        "La producción no es solo un trabajo individual: en muchas comunidades se organiza en conjunto. Se reparten tareas según lo que cada persona sabe y puede, se comparte lo producido y se guarda parte para la próxima vez. Así la técnica sostiene a la comunidad y los lazos entre familias.",
        "Para relacionar producción y comunidad, miramos cuatro cosas: quiénes participan, qué tarea hace cada uno, cómo se reparte lo producido y qué se guarda. Con una ficha de práctica podemos calcular cuánto se produce y cuánto toca a cada familia, usando multiplicación y división.",
        "Cada comunidad tiene su manera de organizarse. En esta clase usamos una ficha inventada de Valle Alto. No decimos que todas las comunidades se organizan igual. Para conocer cómo se organiza una comunidad real, la guía es el educador o educadora tradicional.",
    ],
    vocab=[("tarea", "trabajo que le toca a una persona"), ("reparto", "entrega de partes iguales o justas a cada uno"), ("organización comunitaria", "manera en que una comunidad se coordina para trabajar"), ("semilla guardada", "parte de la cosecha que se reserva para sembrar de nuevo"), ("lazos", "vínculos entre personas")],
    worked=[
        W("Repartir lo producido", "Ficha inventada de Valle Alto: «Se cosecharon 120 kilos de papas. Se guardan 20 kilos para semilla y el resto se reparte por igual entre 10 familias.» ¿Cuántos kilos recibe cada familia?", ["Total: 120 kilos.", "Se guardan 20, quedan 100.", "Divido 100 ÷ 10."], "10 kilos por familia."),
        W("Reconocer tareas", "En la huerta, unas personas riegan, otras siembran y otras cuidan el cauce. ¿Qué muestra esto sobre la comunidad?", ["Cada uno hace una tarea.", "Todas son necesarias.", "Trabajan en conjunto."], "Muestra una organización en conjunto con tareas repartidas."),
    ],
    mistakes=[
        M("Creer que solo importa lo que produce cada familia por separado.", "En la ficha, se comparte y se guarda para todos.", "Mira cómo se reparte."),
        M("Olvidar guardar semilla para la próxima siembra.", "Sin semillas no hay cosecha futura.", "Cuenta lo que se guarda."),
    ],
    R=[
        ex("Según la ficha, ¿cuántos kilos de papas se guardan para semilla? Escribe el número.", "20", "La ficha dice 20 kilos."),
        ex("¿Entre cuántas familias se reparte el resto?", "10", "La ficha dice 10 familias."),
        ex("¿Para qué se guarda semilla: para sembrar de nuevo o para botar?", "Para sembrar de nuevo", "Asegura la próxima cosecha."),
    ],
    C=[
        ex("¿Qué es el reparto? A) entrega de partes iguales o justas a cada uno B) quedarse con todo", "A", "Es dar a cada uno su parte."),
        ex("Verdadero o falso: en la ficha de Valle Alto la producción se organiza en conjunto.", "Verdadero", "Se reparte y se comparte."),
        ex("Verdadero o falso: todas las comunidades reparten igual.", "Falso", "Cada comunidad tiene su manera."),
    ],
    A=[
        arith("Se cosecharon 120 kilos de papas y se guardan 20 para semilla. ¿Cuántos kilos quedan para repartir?", "120-20", "Se resta lo guardado."),
        arith("Los 100 kilos que quedan se reparten por igual entre 10 familias. ¿Cuántos kilos recibe cada una?", "100//10", "Se divide en partes iguales."),
        ex("Clasifica en TAREA o REPARTO: a) regar la huerta b) entregar 10 kilos a cada familia.", "a tarea, b reparto", "Regar es una tarea; entregar partes es reparto."),
    ],
    Z=[
        ex("Pedro dice: «Mejor no guardamos semillas, así repartimos más». ¿Qué problema tiene?", "No habría semillas para la próxima siembra", "La producción depende de guardar semilla."),
        ex("¿Por qué el reparto en partes iguales fortalece los lazos? A) porque todos sienten que se los considera B) porque todos reciben menos", "A", "El reparto justo une."),
    ],
    D=[
        arith("En Valle Alto cosechan 150 kilos de choclo, guardan 30 para semilla y reparten el resto por igual entre 8 familias. ¿Cuántos kilos recibe cada familia?", "(150-30)//8", "Primero se resta lo guardado y luego se reparte."),
        ex("Dos frases: 1) «La técnica de la ficha organiza tareas y reparto» 2) «Las comunidades indígenas reparten siempre igual». ¿Cuál se apoya en la ficha?", "La primera", "La segunda generaliza."),
    ],
    context=[ex("Tu curso hace una venta de plantas con 60 plantas y 5 grupos. Si reparten en partes iguales, ¿cuántas plantas tiene cada grupo? Responde con un número.", "12", "60 ÷ 5 = 12.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es un reparto.", "Entrega de partes iguales o justas a cada uno", "Es la definición de la clase."),
        ex("Verdadero o falso: guardar semilla es necesario para sembrar de nuevo.", "Verdadero", "Asegura la próxima siembra."),
        ex("¿Qué haces para conocer cómo se organiza una comunidad real? A) pregunto al educador tradicional B) lo supongo", "A", "Es la fuente."),
    ],
    task=T("Lee esta ficha inventada de Costa Clara: «Se pescaron 96 kilos de pescado. Se guardan 6 kilos para la olla común y el resto se reparte por igual entre 9 familias.» Calcula cuántos kilos quedan para repartir y cuántos recibe cada familia, mostrando las operaciones. Escribe una frase que explique cómo esta organización fortalece la comunidad, y una pregunta al educador tradicional.",
           "96 − 6 = 90 kilos. 90 ÷ 9 = 10 kilos por familia. Frase: se reparte por igual y se guarda para la olla común, así todos reciben y se ayuda a quien lo necesita. Pregunta: ¿cómo se reparten las cosas que producimos en nuestra comunidad?",
           ["calcula correctamente", "explica el vínculo con la comunidad", "formula una pregunta respetuosa"], ["operaciones escritas", "frase explicativa", "pregunta"], ["errores de cálculo", "generalizar a todas las comunidades"],
           "Revisar las operaciones; pedir que explique el reparto."),
    reinforce="Haz una tabla con el reparto: total, guardado, para repartir y por familia.",
    extend="Escribe cómo se podría repartir una cosecha de 100 kilos entre 4 grupos si se guardan 20 kilos.",
)
