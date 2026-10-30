"""Cuaderno del estudiante, 2.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 14 (experimentar con técnicas y producción vinculadas a valores culturales) y
OA 15 (patrimonio cultural: comidas, ceremonias, sitios arqueológicos y espacios naturales).

Criterio de autoría: en OA 14 se experimenta solo con técnicas genéricas y seguras con papel (tejido de papel,
trenza de tres hebras, modelado de masa de sal que no se come), con diseños propios; no se copian diseños,
símbolos ni técnicas restringidas de ningún pueblo. En OA 15 los ejemplos reales (moai y Parque Nacional
Rapa Nui, Pukará de Quitor, umu, Salar de Atacama) son datos ampliamente conocidos y están marcados para
revisión por especialista; los casos de comunidad y de personas son inventados.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA14, OA15 = "LC02 OA 14", "LC02 OA 15"

CONSULT = " Recuerda: lo que es tradicional lo enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales a ellos antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. No copiar diseños ni símbolos de ningún pueblo."


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement + CONSULT, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback + FEEDBACK_ADD}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def L(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


TECN_DIA = "Pueblo diaguita: hace cerámica con dibujos geométricos y vive en valles del Norte Chico, junto a los ríos Elqui, Limarí y Huasco."
TECN_MAP = "Pueblo mapuche: teje y cultiva la tierra."
TECN_RN = "Pueblo rapa nui: vive en una isla del Pacífico, donde están los moai, grandes figuras de piedra."

# ============================================================ OA 14 · Técnicas y producción
L(
    OA14, 1,
    materials="Lápiz, hojas y colores. Las fichas están escritas en el cuaderno. Para el experimento: dos hojas de papel de colores, regla y tijeras con un adulto.",
    use="Aprenderé qué es una técnica, que cada pueblo tiene las suyas y que sus diseños pertenecen a quienes los crean. Sirve para experimentar sin copiar lo que no nos corresponde.",
    prior=["Sé qué es una actividad productiva.", "Sé que una ficha tiene una fuente."],
    explain=[
        "Una técnica es una manera de hacer algo con las manos y con ciertos materiales. Hay técnicas para tejer, para modelar arcilla, para trenzar fibras o para construir canoas. Cada pueblo tiene las suyas, que se aprenden de los mayores durante años.",
        "Los diseños, los símbolos y las técnicas especiales de un pueblo pertenecen a esa comunidad. No se copian sin permiso. En este cuaderno experimentamos solo con técnicas simples y generales, como cruzar tiras de papel, usando nuestros propios diseños.",
        "Experimentar significa probar para aprender, con cuidado y respeto. Antes de empezar, leemos los pasos, preparamos los materiales y vemos qué seguridad necesitamos. Las tijeras las usamos con un adulto. Al terminar, decimos de dónde aprendimos la idea y agradecemos. Las técnicas propias de un pueblo las enseña su educador o educadora tradicional; aquí solo practicamos una técnica general.",
    ],
    vocab=[("técnica", "manera de hacer algo con las manos y ciertos materiales"), ("material", "lo que se usa para hacer un objeto"), ("proceso", "pasos para hacer algo"), ("diseño", "dibujo o forma que se elige para un objeto"), ("experimentar", "probar para aprender con cuidado")],
    worked=[
        W("Leer una técnica en una ficha", TECN_DIA + " ¿Qué técnica nombra la ficha y qué tiene su decoración?", ["Busco el verbo de hacer.", "Hace cerámica.", "Sus dibujos son geométricos."], "Cerámica, con dibujos geométricos"),
        W("Ordenar un proceso", "Ordena los pasos de un experimento de papel: a) cruzar las tiras b) cortar las tiras c) pegar las puntas d) preparar los materiales.", ["Primero preparo.", "Luego corto.", "Después cruzo y al final pego."], "d, b, a, c"),
    ],
    mistakes=[
        M("Copiar el diseño de un tejido que vi en una foto.", "Los diseños pertenecen a quienes los crearon.", "Inventa tu propio diseño y menciona de dónde viene la idea."),
        M("Empezar a cortar sin leer los pasos.", "Puedes cortarte o desperdiciar el material.", "Lee los pasos y usa tijeras con un adulto."),
    ],
    R=[
        ex("Una técnica es una manera de hacer algo con las manos. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
        ex("Cada pueblo tiene sus propias técnicas. ¿Verdadero o falso?", "Verdadero", "Se aprenden de los mayores."),
        ex("Las tijeras se usan con un adulto. ¿Verdadero o falso?", "Verdadero", "Es una regla de seguridad."),
    ],
    C=[
        ex("¿Qué técnica nombra la ficha mapuche de este cuaderno? A) Tejer B) Hacer cerámica", "A", "La ficha dice que teje."),
        ex("Verdadero o falso: se puede copiar el diseño de un tejido de otro pueblo.", "Falso", "Los diseños pertenecen a quienes los crearon."),
        ex("¿Qué es experimentar? A) Probar para aprender con cuidado B) Hacer cualquier cosa sin pensar", "A", "Se hace con cuidado y respeto."),
    ],
    A=[
        ex("Ficha diaguita: " + TECN_DIA + " ¿Qué técnica nombra?", "La cerámica", "La ficha dice que hace cerámica."),
        ex("Une pueblo y técnica. 1) diaguita 2) mapuche. a) tejer b) cerámica", "1-b, 2-a", "Cada técnica está en la ficha de su pueblo."),
        ex("Ordena los pasos de un experimento de papel: 1) cruzar las tiras 2) cortar las tiras 3) preparar los materiales. Escribe el orden.", "3, 2, 1", "Primero preparo, luego corto y al final cruzo."),
    ],
    Z=[
        ex("Julia dice: «Si me gusta un diseño, lo copio». ¿Qué error comete?", "Copia un diseño que no es suyo", "Los diseños pertenecen a quienes los crearon."),
        ex("Pedro corta las tiras sin leer los pasos y se equivoca. ¿Qué debió hacer primero?", "Leer los pasos", "Así evita errores y desperdicio."),
    ],
    D=[
        ex("Dos niñas inventan sus propios diseños de papel. ¿Alguna copia a un pueblo? Responde Sí o No.", "No", "Son diseños propios."),
        ex("Un niño dice que aprendió a cruzar tiras viendo un video de una artesana. ¿Qué debería decir al presentar su trabajo?", "De dónde aprendió la idea", "Reconocer la fuente es respeto."),
    ],
    context=[ex("Tu curso hará un experimento de tejido de papel. Tomás quiere copiar un diseño de una ficha. La profesora le propone otra cosa. ¿Cuál es mejor? A) Inventar su propio diseño B) Copiar igual", "A", "Los diseños propios no copian a nadie.")],
    selfcheck=[ex("¿Qué es una técnica?", "Una manera de hacer algo con las manos", "Es la definición."), ex("¿Qué haces antes de experimentar?", "Leo los pasos y preparo los materiales", "Así trabajas con cuidado."), ex("Verdadero o falso: los diseños de un pueblo se pueden copiar sin permiso.", "Falso", "Hay que respetar a sus creadores.")],
    task=T("Con dos hojas de papel de colores, una regla y unas tijeras (usadas por un adulto), haz tiras: 4 tiras largas de un color y 4 tiras largas del otro. Luego escribe en tu cuaderno los pasos que seguirías para cruzarlas. Dibuja tu propio diseño de color y escribe de dónde viene tu idea. No copies diseños de ningún pueblo.",
           "Pasos: 1. Preparo los materiales. 2. Corto 4 tiras de cada color con un adulto. 3. Las cruzo. Mi diseño es de rayas rojas y azules. La idea viene de las líneas de mi cuaderno.",
           ["ordena los pasos", "usa un diseño propio", "dice de dónde viene la idea"], ["pasos escritos", "dibujo de diseño"], ["copiar diseños", "usar tijeras sin adulto"],
           "Verificar que el diseño sea propio y que se mencione la seguridad."),
    reinforce="Cuenta cuántas tiras necesitas en total para el experimento de papel.",
    extend="Escribe una pregunta sobre una técnica de un pueblo para el educador tradicional.",
)

L(
    OA14, 2,
    materials="Dos hojas de papel de colores distintos, regla y tijeras con un adulto. Los pasos están escritos aquí.",
    use="Aprenderé a experimentar con una técnica de tejido de papel y a relacionar esa técnica con los valores de ayuda mutua, respeto y reciprocidad. Sirve para ver que hacer algo bien también es cuidar.",
    prior=["Sé qué es una técnica.", "Sé qué son el respeto, la ayuda mutua y la reciprocidad."],
    explain=[
        "Vamos a experimentar con una técnica simple: tejer con tiras de papel. Se usan tiras de un color, puestas una al lado de otra, y tiras de otro color que pasan por encima y por debajo. Se cruza una por encima y la siguiente por debajo.",
        "Los valores aparecen al trabajar. Hay respeto cuando cuidamos el material y no lo desperdiciamos. Hay ayuda mutua cuando uno sostiene las tiras mientras otro las cruza. Hay reciprocidad cuando alguien nos enseña y después nosotros enseñamos a otro.",
        "El orden es importante. En cada fila, el cruce empieza al revés de la fila anterior. Si la primera fila empieza por encima, la siguiente empieza por debajo. Así se forma un dibujo ordenado. Lo hacemos despacio, con un compañero si es posible.",
    ],
    vocab=[("tira", "papel largo y angosto"), ("cruce", "lugar donde una tira pasa sobre o bajo otra"), ("fila", "línea de tiras puestas una junto a otra"), ("sostener", "mantener algo firme con la mano"), ("enseñar", "mostrar a otro cómo se hace algo")],
    worked=[
        W("Contar los cruces", "Un tejido de papel tiene 5 tiras horizontales y 5 verticales. ¿Cuántos cruces tiene?", ["Cada tira horizontal se cruza con 5 verticales.", "5 × 5 = 25.", "Hay 25 cruces."], "25 cruces"),
        W("Seguir el patrón", "La primera tira vertical pasa por encima de la primera tira horizontal y por debajo de la segunda. ¿Por dónde pasa en la tercera?", ["Primera: encima.", "Segunda: debajo.", "Tercera: encima, porque se alterna."], "Por encima"),
    ],
    mistakes=[
        M("Pasar la tira por encima en todas las filas.", "No se forma un tejido, solo quedan tiras apoyadas.", "Alterna: encima, debajo, encima, debajo."),
        M("Hacer el experimento sin cuidar el material.", "Desperdicias papel.", "Mide antes de cortar y reutiliza los restos."),
    ],
    R=[
        ex("En un tejido de papel, una tira pasa por encima y la siguiente por debajo. ¿Verdadero o falso?", "Verdadero", "Es el patrón de alternar."),
        ex("Si una tira pasa por encima de la primera, ¿por dónde pasa en la segunda?", "Por debajo", "Así se alterna el tejido."),
        ex("Cuidar el material es una forma de respeto. ¿Verdadero o falso?", "Verdadero", "Así se evita desperdiciar."),
    ],
    C=[
        ex("¿Qué hacen dos niños que se ayudan: uno sostiene las tiras y otro las cruza? A) Ayuda mutua B) Competencia", "A", "Se ayudan entre dos."),
        ex("Verdadero o falso: en la fila siguiente el cruce empieza igual que en la anterior.", "Falso", "Empieza al revés."),
        ex("¿Qué valor muestra alguien que enseña lo que aprendió? A) Reciprocidad B) Competencia", "A", "Devuelve lo que recibió."),
    ],
    A=[
        arith("Un tejido de papel tiene 3 tiras horizontales y 5 verticales. ¿Cuántos cruces tiene?", "3*5", "Se multiplican las tiras de cada dirección.", " cruces"),
        ex("La tira vertical 1 pasa por encima de la horizontal 1. ¿Por dónde pasa en la horizontal 2?", "Por debajo", "Así se alterna el tejido."),
        ex("La primera fila empieza con la tira por encima. ¿Cómo empieza la segunda fila?", "Por debajo", "Cada fila empieza al revés de la anterior."),
    ],
    Z=[
        ex("Ema dice: «Si paso todo por encima es lo mismo». ¿Qué le falta a su tejido?", "Alternar encima y debajo", "Sin alternar no se forma el tejido."),
        ex("Pedro corta tiras de distinto largo y no le calzan. ¿Qué debió hacer?", "Medir con la regla antes de cortar", "Así todas quedan iguales."),
    ],
    D=[
        arith("Un tejido tiene 2 tiras horizontales y 5 verticales. ¿Cuántos cruces hay?", "2*5", "Se multiplican tiras horizontales por verticales.", " cruces"),
        ex("Una niña usa los restos de papel para hacer otro tejido pequeño. ¿Qué valor muestra? A) Respeto por el material B) Desorden", "A", "Aprovecha el material."),
    ],
    context=[ex("Mateo y Lía hacen un tejido de papel juntos. Mateo sostiene las tiras y Lía las cruza. Después ella le enseña cómo cruzar. ¿Cuántos valores aparecen (ayuda mutua y reciprocidad)?", "2", "Hay ayuda mutua y reciprocidad.")],
    selfcheck=[ex("¿Cómo se alterna una tira en un tejido?", "Una por encima y la siguiente por debajo", "Ese es el patrón."), ex("¿Cómo empieza la siguiente fila?", "Al revés de la anterior", "Así se forma el dibujo."), ex("Verdadero o falso: cuidar el papel es respeto.", "Verdadero", "Evita el desperdicio.")],
    task=T("Con 5 tiras horizontales de un color y 5 verticales de otro (cortadas con un adulto), teje un cuadrado de papel alternando encima y debajo. Cuenta los cruces y escribe cuántos hay (deben ser 25). Escribe una frase que diga qué valor viste al trabajar. Usa un diseño de colores propio. No copies diseños de ningún pueblo.",
           "Tejí un cuadrado de papel con 5 tiras de cada color. Hay 25 cruces. El valor que vi fue la ayuda mutua, porque mi compañero sostuvo las tiras.",
           ["alterna encima y debajo", "cuenta bien los cruces", "relaciona la técnica con un valor"], ["tejido de papel", "número de cruces", "frase"], ["no alternar", "contar mal"],
           "Revisar el patrón alternado y el conteo."),
    reinforce="Cuenta los cruces de un tejido de 2 tiras por 2 tiras.",
    extend="Escribe una frase sobre cómo enseñar esta técnica a otra persona.",
)

L(
    OA14, 3,
    materials="Tres hebras de lana o cordón de colores (rojo, azul y verde), o tiras de papel. Los pasos están escritos aquí.",
    use="Aprenderé a hacer una trenza de tres hebras y a entender que las técnicas se transmiten y continúan hoy. Sirve para reconocer a las personas que enseñan y que hacen estos trabajos hoy.",
    prior=["Sé qué es una técnica.", "Sé que los mayores enseñan técnicas."],
    explain=[
        "Una trenza se hace cruzando hebras. Con tres hebras, la de la izquierda pasa sobre la del centro. Luego, la de la derecha pasa sobre la del centro. Se repite una y otra vez. Así se forma un dibujo parecido a una cadena.",
        "Muchas técnicas siguen vivas hoy. Hay artesanos y artesanas de pueblos originarios que hacen su trabajo con técnicas que aprendieron de sus abuelos, pero que también usan materiales nuevos. Es importante reconocer sus nombres cuando mostramos su trabajo y pagar un precio justo si lo compramos.",
        "Experimentamos con la trenza como práctica simple. No copiamos diseños especiales. Si queremos aprender más, invitamos a un artesano o artesana y le agradecemos su tiempo y su saber. Y recordamos que la técnica es solo una parte: también hay valores y respeto.",
    ],
    vocab=[("hebra", "hilo o cuerda delgada"), ("trenza", "unión de hebras cruzadas"), ("artesano", "persona que hace objetos con sus manos"), ("precio justo", "pago que reconoce el trabajo"), ("transmitir", "pasar un saber de una persona a otra")],
    worked=[
        W("Seguir los pasos de la trenza", "Hebras: roja (izquierda), azul (centro), verde (derecha). Pasas la roja sobre la azul. ¿Qué color queda en el centro?", ["La roja pasa al centro.", "La azul queda a la izquierda.", "El centro es rojo."], "Roja"),
        W("Segundo paso", "Después del paso anterior (roja al centro, azul a la izquierda, verde a la derecha), pasas la verde sobre la roja. ¿Qué color queda en el centro?", ["La verde pasa sobre la del centro.", "La verde queda en el centro.", "La roja queda a la derecha."], "Verde"),
    ],
    mistakes=[
        M("Tirar muy fuerte de las hebras.", "La trenza queda apretada o se rompe.", "Tira con suavidad y parejo."),
        M("Comprar un objeto de artesano y no preguntar quién lo hizo.", "Se pierde el reconocimiento de su trabajo.", "Pregunta su nombre y paga un precio justo."),
    ],
    R=[
        ex("En una trenza de tres hebras, la hebra izquierda pasa sobre la del centro. ¿Verdadero o falso?", "Verdadero", "Es el primer paso."),
        ex("Un artesano es una persona que hace objetos con sus manos. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
        ex("Un precio justo reconoce el trabajo. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
    ],
    C=[
        ex("¿Cuántas hebras tiene la trenza de esta clase? A) 3 B) 5", "A", "Es una trenza de tres hebras."),
        ex("Verdadero o falso: las técnicas ya no se usan hoy.", "Falso", "Hay artesanos que las practican."),
        ex("¿Qué haces al mostrar el trabajo de un artesano? A) Reconozco su nombre B) No digo quién lo hizo", "A", "Se reconoce a quien lo creó."),
    ],
    A=[
        ex("Hebras: roja (izquierda), azul (centro), verde (derecha). Pasas la izquierda sobre la del centro. ¿Qué color queda en el centro?", "Roja", "La roja pasa al centro."),
        ex("Ahora el orden es azul, roja, verde (izquierda, centro, derecha). Pasas la derecha sobre la del centro. ¿Qué color queda en el centro?", "Verde", "La verde pasa al centro."),
        ex("Ordena: 1) pasar la derecha sobre el centro 2) comenzar con tres hebras 3) pasar la izquierda sobre el centro. Escribe el orden correcto.", "2, 3, 1", "Primero se prepara, luego la izquierda y luego la derecha."),
    ],
    Z=[
        ex("Lía dice: «Si compro una artesanía no necesito saber quién la hizo». ¿Qué le dirías?", "Que debe reconocer a quien la hizo", "El nombre del creador merece respeto."),
        ex("Tomás dice que las técnicas antiguas no pueden usar materiales nuevos. ¿Qué le responderías?", "Que pueden cambiar los materiales y seguir siendo técnicas vivas", "El saber continúa."),
    ],
    D=[
        arith("Un artesano de práctica hace 4 trenzas por día durante 5 días. ¿Cuántas trenzas hace?", "4*5", "Se multiplican las trenzas por los días.", " trenzas"),
        ex("Una niña aprende a trenzar con su abuela y después enseña a su hermano. ¿Qué valor aparece? A) Reciprocidad B) Competencia", "A", "Devuelve lo que recibió."),
    ],
    context=[ex("En la feria, Ema quiere comprar una trenza hecha por una artesana inventada, Ana. Ana pide un precio justo por su trabajo. Ema quiere pagar casi nada. ¿Qué es mejor? A) Pagar el precio justo B) Pedir que lo regale", "A", "El trabajo debe valorarse.")],
    selfcheck=[ex("¿Qué hebra pasa primero sobre el centro?", "La izquierda", "Es el primer paso."), ex("¿Qué hacemos con el nombre de un artesano?", "Lo reconocemos", "Reconocerlo es una forma de respeto."), ex("Verdadero o falso: una técnica puede seguir viva aunque use materiales nuevos.", "Verdadero", "Lo importante es el saber.")],
    task=T("Con tres hebras (lana, cordón o tiras de papel), pon la hebra roja a la izquierda, la azul al centro y la verde a la derecha. Haz una trenza de 10 cruces, guiándote por esta regla: izquierda sobre centro, luego derecha sobre centro, y repite. Escribe cuántos cruces hiciste, qué color quedó en el centro al final y una frase para agradecer a quien te enseñó. No copies diseños de ningún pueblo.",
           "Hice una trenza de 10 cruces. Al final quedó en el centro la hebra roja. Gracias a mi abuelo por enseñarme a trenzar.",
           ["sigue la regla de los cruces", "registra el resultado", "incluye agradecimiento"], ["trenza", "frase"], ["tirar muy fuerte", "olvidar agradecer"],
           "Revisar el conteo y el agradecimiento."),
    reinforce="Haz una trenza corta y cuéntale los pasos a un adulto.",
    extend="Escribe una pregunta para un artesano o artesana sobre cómo aprendió su técnica.",
)

L(
    OA14, 4,
    materials="Masa de sal (con un adulto): harina, sal y agua, o plasticina. No se come. Los pasos están escritos aquí.",
    use="Aprenderé a modelar con respeto una pieza simple, sin copiar diseños de otros, y a reconocer los valores de la autorización y el reconocimiento. Sirve para crear con cuidado.",
    prior=["Sé que los diseños pertenecen a sus creadores.", "Sé que la técnica y los valores van juntos."],
    explain=[
        "Modelar es dar forma a un material blando con las manos. Se puede modelar con arcilla, con masa de sal o con plasticina. En esta clase usamos masa de sal hecha con un adulto, o plasticina, y hacemos un objeto simple con un diseño propio.",
        "La masa de sal se hace con dos tazas de harina, una taza de sal y una taza de agua, mezcladas con un adulto. No se come. Si hay alergia a algún ingrediente, se usa plasticina. Cuando termines, lava tus manos y guarda el material.",
        "Antes de crear, recordamos tres cosas: usamos diseños propios, reconocemos de dónde viene la idea y agradecemos a quien nos enseñó. Si queremos copiar un diseño de un pueblo, primero pedimos autorización a la comunidad. Sin permiso, creamos el nuestro.",
    ],
    vocab=[("modelar", "dar forma a un material blando"), ("masa de sal", "mezcla de harina, sal y agua que no se come"), ("autorización", "permiso formal para usar algo"), ("alergia", "reacción del cuerpo a algún alimento o material"), ("reconocer", "decir quién hizo o enseñó algo")],
    worked=[
        W("Cantidad de ingredientes", "Una masa de sal usa 2 tazas de harina, 1 de sal y 1 de agua. ¿Cuántas tazas son en total?", ["Sumo 2 + 1 + 1.", "2 + 1 + 1 = 4.", "Son 4 tazas."], "4 tazas"),
        W("Pedir autorización", "Quieres copiar un diseño de una ficha de un pueblo. ¿Qué haces primero? a) lo copio b) pido autorización a la comunidad c) cambio un detalle.", ["Cambiar un detalle no es suficiente.", "Pedir autorización respeta a la comunidad.", "Elijo b."], "b"),
    ],
    mistakes=[
        M("Comer la masa de sal.", "Tiene mucha sal y no es comida.", "Solo se modela; no se come."),
        M("Cambiar un detalle de un diseño ajeno y decir que es tuyo.", "Sigue siendo el diseño de otra persona.", "Crea un diseño propio o pide autorización."),
    ],
    R=[
        ex("La masa de sal no se come. ¿Verdadero o falso?", "Verdadero", "Es solo para modelar."),
        ex("Modelar es dar forma a un material blando. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
        ex("Si tienes alergia a un ingrediente, usas plasticina. ¿Verdadero o falso?", "Verdadero", "Es una alternativa segura."),
    ],
    C=[
        ex("¿Qué haces antes de copiar un diseño de un pueblo? A) Pedir autorización B) Copiar igual", "A", "Se respeta a la comunidad."),
        ex("Verdadero o falso: cambiar un detalle de un diseño ajeno lo convierte en tuyo.", "Falso", "Sigue siendo ajeno."),
        ex("¿Qué haces al terminar de modelar? A) Lavo mis manos y guardo el material B) Dejo todo desordenado", "A", "Es parte del cuidado."),
    ],
    A=[
        arith("Una receta de masa de sal usa 2 tazas de harina, 1 taza de sal y 1 taza de agua. Si la haces dos veces, ¿cuántas tazas de harina necesitas?", "2*2", "Se duplica la cantidad de harina.", " tazas"),
        arith("Para la masa de sal usas 2 tazas de harina, 1 de sal y 1 de agua. ¿Cuántas tazas de ingredientes son en total?", "2+1+1", "Se suman las tres cantidades.", " tazas"),
        ex("Ordena: 1) agradezco a quien me enseñó 2) modelo mi pieza con diseño propio 3) lavo mis manos. Escribe el orden.", "2, 1, 3", "Primero modelo, luego agradezco y al final me lavo las manos."),
    ],
    Z=[
        ex("Rosa dice: «Si copio un diseño con otro color, ya es mío». ¿Qué error comete?", "Sigue siendo el diseño de otra persona", "Cambiar el color no lo convierte en suyo."),
        ex("Tomás dice que puede probar la masa de sal para ver si está rica. ¿Qué le dirías?", "Que no se come", "Tiene mucha sal."),
    ],
    D=[
        arith("Una niña modela 2 figuras por día durante 4 días. ¿Cuántas figuras modela?", "2*4", "Se multiplican las figuras por los días.", " figuras"),
        ex("Un grupo muestra sus piezas con una tarjeta que dice de dónde viene la idea y a quién agradecen. ¿Qué dos valores muestran?", "Reconocimiento y agradecimiento", "Dicen la fuente y dan las gracias."),
    ],
    context=[ex("En la clase, Mateo modela una pieza con un diseño inventado por él. Ema quiere copiar un diseño de un pueblo del cuaderno. ¿Quién actúa con más respeto?", "Mateo", "Su diseño es propio y no copia a nadie.")],
    selfcheck=[ex("¿Qué debes hacer antes de copiar un diseño ajeno?", "Pedir autorización", "Se respeta a la comunidad."), ex("¿Se come la masa de sal?", "No", "Tiene mucha sal."), ex("Verdadero o falso: se debe reconocer de dónde viene la idea.", "Verdadero", "Es una forma de respeto.")],
    task=T("Con masa de sal hecha con un adulto, o con plasticina, modela una pieza simple con un diseño propio, por ejemplo una taza pequeña con rayas inventadas. Escribe una tarjeta que diga qué hiciste, de dónde viene tu idea y a quién agradeces. Dibuja tu pieza. No copies diseños ni símbolos de ningún pueblo.",
           "Modelé una taza con rayas. La idea viene de las rayas de mi cuaderno. Agradezco a mi profesora por enseñarme a modelar.",
           ["usa un diseño propio", "escribe de dónde viene la idea", "incluye agradecimiento"], ["pieza modelada", "tarjeta"], ["copiar diseños", "comer la masa"],
           "Verificar que el diseño sea propio y que la tarjeta tenga agradecimiento."),
    reinforce="Escribe en tu cuaderno los tres ingredientes de la masa de sal.",
    extend="Escribe una pregunta para el educador tradicional sobre cómo se piden autorizaciones para usar un diseño.",
)

# ============================================================ OA 15 · Patrimonio cultural
L(
    OA15, 1,
    materials="Lápiz, hojas y colores. Las fichas con los datos están escritas en el cuaderno.",
    use="Aprenderé qué es el patrimonio cultural y sus tipos: comidas, ceremonias, sitios arqueológicos y espacios naturales. Sirve para reconocer lo que una comunidad quiere cuidar y compartir.",
    prior=["Sé qué es una comunidad y un territorio.", "Sé que una ficha tiene una fuente."],
    explain=[
        "El patrimonio cultural es lo que una comunidad heredó de sus antepasados y quiere cuidar para el futuro. Son manifestaciones propias, es decir, cosas que expresan su cultura. Pueden ser comidas, ceremonias, sitios arqueológicos o espacios naturales.",
        "Una comida es patrimonio cuando se prepara con saberes que se heredan. Una ceremonia lo es cuando la comunidad la celebra con sentido. Un sitio arqueológico es un lugar donde quedan huellas de los antepasados. Un espacio natural es un lugar de la naturaleza importante para una comunidad.",
        "Según fuentes publicadas, ejemplos conocidos son los moai y el Parque Nacional Rapa Nui, el Pukará de Quitor en el territorio lickanantay, y el Salar de Atacama. La comunidad es quien mejor puede explicar su patrimonio y quien decide cómo se visita y se comparte.",
    ],
    vocab=[("patrimonio cultural", "lo que una comunidad heredó y quiere cuidar"), ("manifestación", "forma en que se expresa una cultura"), ("sitio arqueológico", "lugar con huellas de los antepasados"), ("espacio natural", "lugar de la naturaleza importante para una comunidad"), ("heredar", "recibir algo de quienes vivieron antes")],
    worked=[
        W("Clasificar patrimonio", "Clasifica en COMIDA, SITIO ARQUEOLÓGICO o ESPACIO NATURAL: umu (horno de tierra de Rapa Nui), Pukará de Quitor, Salar de Atacama.", ["El umu sirve para cocinar: comida.", "El Pukará de Quitor tiene huellas antiguas: sitio arqueológico.", "El Salar es un lugar de la naturaleza: espacio natural."], "Umu: comida. Pukará de Quitor: sitio arqueológico. Salar de Atacama: espacio natural."),
        W("Leer una ficha", TECN_RN + " ¿Qué patrimonio nombra la ficha?", ["Busco una manifestación propia.", "Los moai son grandes figuras de piedra.", "Son patrimonio de la isla."], "Los moai"),
    ],
    mistakes=[
        M("Pensar que el patrimonio es solo lo que está en un museo.", "También incluye comidas, ceremonias y lugares vivos.", "Piensa en lo que la comunidad hace y cuida hoy."),
        M("Visitar un sitio importante sin saber cómo se cuida.", "Puedes dañarlo sin querer.", "Pregunta las reglas de visita y cumple."),
    ],
    R=[
        ex("El patrimonio cultural es lo que una comunidad heredó y quiere cuidar. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
        ex("Un sitio arqueológico es un lugar con huellas de los antepasados. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
        ex("Un espacio natural es un lugar de la naturaleza importante para una comunidad. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
    ],
    C=[
        ex("¿Cuál es un ejemplo de espacio natural, según fuentes publicadas? A) Salar de Atacama B) Una calculadora", "A", "El Salar de Atacama es un lugar natural."),
        ex("Verdadero o falso: el patrimonio cultural solo está en los museos.", "Falso", "También incluye comidas, ceremonias y lugares vivos."),
        ex("¿Quién decide cómo se visita y se comparte el patrimonio? A) La comunidad B) Cualquier turista", "A", "La comunidad es quien mejor lo conoce."),
    ],
    A=[
        ex("Clasifica en COMIDA, FIESTA O CEREMONIA, SITIO ARQUEOLÓGICO o ESPACIO NATURAL (ejemplos inventados de Valle Alto): a) la sopa de la cosecha b) la fiesta de la cosecha c) las ruinas de un pueblo antiguo d) la laguna donde la comunidad recoge agua. Escribe las categorías.", "a comida, b fiesta o ceremonia, c sitio arqueológico, d espacio natural", "Cada ejemplo corresponde a una categoría."),
        ex("Une patrimonio y tipo, según fuentes publicadas. 1) Pukará de Quitor 2) umu 3) Salar de Atacama. a) comida b) sitio arqueológico c) espacio natural", "1-b, 2-a, 3-c", "Cada uno es de ese tipo."),
        ex("Ficha: " + TECN_DIA + " ¿Qué manifestación cultural nombra la ficha?", "La cerámica con dibujos geométricos", "La ficha la describe."),
    ],
    Z=[
        ex("Pedro dice: «El patrimonio es solo de los turistas». ¿Qué le responderías?", "Que es de la comunidad que lo heredó", "La comunidad lo cuida y decide cómo se comparte."),
        ex("Ema piensa que un sitio arqueológico es solo un montón de piedras. ¿Qué dato falta?", "Que tiene huellas de los antepasados y valor para la comunidad", "Guarda memoria de quienes vivieron allí."),
    ],
    D=[
        ex("Una comunidad cuida una comida, una fiesta y un cerro. ¿Cuántos tipos de patrimonio cuida?", "3", "Una comida, una fiesta (ceremonia o evento) y un espacio natural."),
        ex("Una ficha dice solo: «Sitio importante». No dice pueblo ni fuente. ¿Puedes afirmar de qué pueblo es? Responde Sí o No.", "No", "Faltan los datos."),
    ],
    context=[ex("Tu curso arma una lámina del patrimonio de Chile. Julia pone el umu como espacio natural. ¿Está bien?", "No, es una comida", "El umu es un horno de tierra para cocinar.")],
    selfcheck=[ex("Nombra los cuatro tipos de patrimonio de la clase.", "Comidas, ceremonias, sitios arqueológicos y espacios naturales", "Son los cuatro tipos de la explicación."), ex("¿Quién explica mejor un patrimonio?", "La comunidad", "Es quien lo hereda."), ex("Verdadero o falso: el patrimonio solo es del pasado.", "Falso", "Hay patrimonio vivo hoy.")],
    task=T("Haz una tabla de cuatro filas: comida, ceremonia, sitio arqueológico y espacio natural. En cada fila escribe un ejemplo de esta clase (umu, la fiesta de la cosecha inventada de Valle Alto, Pukará de Quitor y Salar de Atacama). Dibuja el que más te guste, sin copiar símbolos sagrados. Escribe una pregunta para el educador tradicional sobre el patrimonio de tu zona.",
           "Comida: umu. Ceremonia o fiesta: fiesta de la cosecha de Valle Alto (inventada). Sitio arqueológico: Pukará de Quitor. Espacio natural: Salar de Atacama. Pregunta: ¿qué patrimonio cuida la comunidad de mi zona?",
           ["completa las cuatro filas", "usa ejemplos de la clase", "formula una pregunta"], ["tabla", "dibujo", "pregunta"], ["clasificar mal", "inventar ejemplos"],
           "Verificar la clasificación con las definiciones."),
    reinforce="Subraya en la explicación los cuatro tipos de patrimonio.",
    extend="Compara dos ejemplos de patrimonio: escribe en qué se parecen y en qué se diferencian.",
)

L(
    OA15, 2,
    materials="Lápiz y hojas. Las listas y los casos están escritos aquí.",
    use="Aprenderé a reconocer patrimonio de mi comunidad, mi territorio y mi pueblo, y a explicar por qué es importante. Sirve para valorar lo propio y lo de otros.",
    prior=["Sé los tipos de patrimonio.", "Sé que cada comunidad decide cómo compartir su patrimonio."],
    explain=[
        "Cada comunidad tiene su patrimonio propio. Puede incluir una comida que se prepara en las fiestas, un lugar natural importante, un sitio con huellas antiguas o una ceremonia. Todos son manifestaciones propias de la comunidad.",
        "Para reconocer patrimonio hacemos tres preguntas. ¿Qué es? ¿A quién pertenece? ¿Cómo se cuida? Por ejemplo, si hablamos de una comida, decimos qué es, quién la prepara y qué hace la comunidad para mantenerla viva. Cada respuesta debe venir de una fuente.",
        "También hay patrimonio en nuestras familias y barrios. Una receta, una canción, un cerro cercano o una fiesta pueden serlo. No todo patrimonio es de pueblos originarios, pero todo merece respeto. Y el patrimonio de un pueblo originario lo explican las personas de ese pueblo.",
    ],
    vocab=[("pertenecer", "ser de alguien o de un grupo"), ("receta", "pasos para preparar una comida"), ("barrio", "zona donde vive una comunidad"), ("mantener", "hacer que algo siga existiendo"), ("propio", "que pertenece a una persona o comunidad")],
    worked=[
        W("Tres preguntas", "Comida de práctica: «La sopa de la cosecha de Valle Alto, que preparan las familias cada otoño». ¿Qué es, a quién pertenece y cómo se cuida?", ["Qué es: una sopa de la cosecha.", "A quién pertenece: a las familias de Valle Alto.", "Cómo se cuida: preparándola cada otoño."], "Es una sopa; pertenece a las familias de Valle Alto; se cuida preparándola cada otoño."),
        W("Patrimonio cercano", "En tu barrio hay un cerro al que van las familias a pasear. ¿Qué tipo de patrimonio podría ser?", ["Es un lugar de la naturaleza.", "Es importante para las familias.", "Es un espacio natural."], "Espacio natural"),
    ],
    mistakes=[
        M("Decir que algo es patrimonio sin saber a quién pertenece.", "Puedes atribuirlo a quien no corresponde.", "Pregunta a una fuente de la comunidad."),
        M("Pensar que solo es patrimonio lo muy antiguo.", "También hay patrimonio vivo de hoy.", "Pregunta qué se hace hoy y desde cuándo."),
    ],
    R=[
        ex("¿Una sopa de la cosecha que preparan las familias cada otoño puede ser patrimonio? Responde Sí o No.", "Sí", "Es una comida que se mantiene viva."),
        ex("Las tres preguntas son: ¿qué es?, ¿a quién pertenece? y ¿cómo se cuida? ¿Cuántas son?", "3", "Se cuentan las tres."),
        ex("Una receta puede ser patrimonio de una familia. ¿Verdadero o falso?", "Verdadero", "Se hereda y se cuida."),
    ],
    C=[
        ex("¿A quién pertenece una receta de la comunidad de Valle Alto? A) A las familias de Valle Alto B) A todos los turistas", "A", "Es de las familias que la preparan."),
        ex("Verdadero o falso: todo patrimonio debe ser muy antiguo.", "Falso", "También hay patrimonio de hoy."),
        ex("¿De dónde debe venir la respuesta sobre un patrimonio? A) De una fuente B) De una suposición", "A", "Las respuestas deben tener fuente."),
    ],
    A=[
        ex("Une patrimonio y tipo. 1) sopa de la cosecha 2) cerro al que van las familias 3) fiesta anual. a) espacio natural b) comida c) ceremonia o evento", "1-b, 2-a, 3-c", "Cada ejemplo corresponde a un tipo."),
        ex("Ficha inventada: «El cerro Pelado es un lugar donde la comunidad de Valle Alto recoge leña, según don Luis». ¿Qué tipo de patrimonio es?", "Espacio natural", "Es un lugar de la naturaleza importante para la comunidad."),
        ex("Completa: para reconocer patrimonio preguntamos qué es, a quién pertenece y cómo se _____.", "Cuida", "Es la tercera pregunta."),
    ],
    Z=[
        ex("Tomás dice: «Esa fiesta no es patrimonio porque es de hoy». ¿Qué le responderías?", "Que también hay patrimonio vivo de hoy", "El patrimonio incluye lo que se celebra ahora."),
        ex("Lía llama patrimonio de un pueblo originario a una receta de su familia sin pensar en el pueblo. ¿Qué error comete?", "Atribuye sin fuente", "No sabe si pertenece a ese pueblo."),
    ],
    D=[
        ex("Una escuela hace un cartel con tres patrimonios: una comida, un cerro y una fiesta. ¿Cuántos tipos de patrimonio aparecen?", "3", "Son tres tipos."),
        ex("Un visitante pregunta cómo se cuida un patrimonio y la comunidad responde: «Lo cuidamos entre todos». ¿Qué valor aparece?", "Ayuda mutua", "Entre todos lo cuidan."),
    ],
    context=[ex("Tu curso hace una lámina de patrimonio del barrio. Ema pone una receta de su mamá sin preguntarle. ¿Qué debe hacer? A) Pedir permiso B) Seguir sin preguntar", "A", "La familia decide qué compartir.")],
    selfcheck=[ex("Escribe las tres preguntas para reconocer patrimonio.", "Qué es, a quién pertenece y cómo se cuida", "Son las tres preguntas de la clase."), ex("¿Quién explica el patrimonio de un pueblo originario?", "Las personas de ese pueblo", "Son su fuente."), ex("Verdadero o falso: también hay patrimonio en las familias.", "Verdadero", "Recetas, canciones y fiestas lo son.")],
    task=T("Escribe tres ejemplos de patrimonio de tu barrio o familia. Puedes basarte en esta lista: una comida que se prepara en fiestas, un cerro o plaza donde pasea la gente, una fiesta o una canción. Para cada uno escribe qué es, a quién pertenece y cómo se cuida. Pide permiso a tu familia antes de compartir. No escribas direcciones.",
           "1. Comida: sopa de domingo; pertenece a mi familia; se cuida preparándola juntos. 2. Plaza: pertenece a mi barrio; se cuida limpiándola. 3. Fiesta: pertenece a mi barrio; se cuida organizándola entre todos.",
           ["responde las tres preguntas por cada ejemplo", "pide permiso", "no escribe direcciones"], ["tres filas", "permiso"], ["atribuir a un pueblo sin fuente", "escribir direcciones"],
           "Revisar que cada ejemplo tenga sus tres respuestas."),
    reinforce="Escribe tres patrimonios de tu escuela o barrio.",
    extend="Escribe una pregunta sobre un patrimonio de tu zona para el educador tradicional.",
)

L(
    OA15, 3,
    materials="Lápiz y hojas. Los datos están escritos aquí.",
    use="Aprenderé que el patrimonio de los pueblos sigue vivo, que los sitios arqueológicos están protegidos por ley y que hay condiciones de acceso. Sirve para saber cómo visitar y cuidar.",
    prior=["Sé qué es patrimonio.", "Sé que la comunidad decide cómo compartirlo."],
    explain=[
        "El patrimonio no está quieto. Hay patrimonio vivo, como las comidas, las fiestas y las técnicas, que se siguen haciendo hoy. Y hay patrimonio que conserva huellas del pasado, como los sitios arqueológicos. Los dos son importantes y los cuidan personas de hoy.",
        "En Chile, la ley de Monumentos Nacionales protege los sitios arqueológicos. Eso significa que están cuidados por la ley y que no se pueden dañar ni llevarse nada de ellos. Algunos sitios se pueden visitar con guía o con pago de entrada, y otros no se pueden visitar por su fragilidad o por pedido de la comunidad.",
        "Las condiciones de acceso las define la comunidad o la autoridad cultural. Por eso, antes de ir, preguntamos si se puede visitar, en qué horarios y con quién. Visitar un sitio sin saber las reglas puede dañar el lugar, aunque no queramos.",
    ],
    vocab=[("patrimonio vivo", "lo que se sigue haciendo y celebrando hoy"), ("ley", "regla que protege algo y que todos deben cumplir"), ("guía", "persona que acompaña y enseña en una visita"), ("frágil", "que se daña fácilmente"), ("acceso", "permiso o forma de entrar a un lugar")],
    worked=[
        W("Vivo o con huellas", "Clasifica en PATRIMONIO VIVO o HUELLAS DEL PASADO: a) una fiesta de este año b) un pukará antiguo c) una técnica de tejido que se enseña hoy.", ["La fiesta y la técnica se hacen ahora: vivo.", "El pukará antiguo conserva huellas: pasado.", "Los clasifico."], "a vivo, b huellas del pasado, c vivo"),
        W("Condiciones de acceso", "Un sitio arqueológico se visita solo con guía. ¿Puedes entrar sin guía? Responde Sí o No.", ["La condición es ir con guía.", "Si no hay guía, no se puede.", "Cumplo la condición."], "No"),
    ],
    mistakes=[
        M("Entrar a un sitio arqueológico sin guía porque «no hay nadie».", "Puedes dañarlo o romper una regla.", "Pregunta cuándo y cómo se visita."),
        M("Pensar que el patrimonio solo es del pasado.", "También hay patrimonio vivo hoy.", "Pregunta qué se hace hoy en la comunidad."),
    ],
    R=[
        ex("Una fiesta que se celebra hoy es patrimonio vivo. ¿Verdadero o falso?", "Verdadero", "Se sigue celebrando."),
        ex("La ley de Monumentos Nacionales protege los sitios arqueológicos. ¿Verdadero o falso?", "Verdadero", "Los cuida la ley."),
        ex("Un sitio frágil se daña fácilmente. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
    ],
    C=[
        ex("Verdadero o falso: se puede llevar una piedra de un sitio arqueológico como recuerdo.", "Falso", "La ley lo prohíbe y daña el sitio."),
        ex("¿Quién define las condiciones de acceso? A) La comunidad o la autoridad cultural B) Cualquier visitante", "A", "Ellos conocen y cuidan el lugar."),
        ex("¿Qué haces antes de visitar un sitio? A) Pregunto las reglas B) Entro sin preguntar", "A", "Así evitas dañarlo."),
    ],
    A=[
        ex("Clasifica en VIVO o HUELLAS DEL PASADO: a) una comida de las fiestas b) una fortaleza antigua c) una canción que se enseña hoy.", "a vivo, b huellas del pasado, c vivo", "Lo que se hace hoy es vivo."),
        ex("Marca las acciones correctas en un sitio arqueológico: a) preguntar las reglas b) llevarse una piedra c) ir con guía d) escribir en una pared.", "a y c", "Preguntar e ir con guía protegen el sitio."),
        ex("Un sitio permite 10 visitantes por hora. Si ya entraron 7, ¿cuántos pueden entrar todavía en esa hora?", "3", "10 menos 7 es 3."),
    ],
    Z=[
        ex("Pedro dice: «Si nadie me ve, puedo llevarme un trozo de cerámica antigua». ¿Qué le dirías?", "Que la ley lo prohíbe y daña la memoria de la comunidad", "Los restos están protegidos."),
        ex("Rosa dice que si un sitio está cerrado es porque no importa. ¿Qué piensas?", "Que puede cerrarse para cuidarlo", "Cerrar protege lo frágil."),
    ],
    D=[
        arith("Un sitio recibe 5 visitantes por grupo y hoy hay 4 grupos. ¿Cuántos visitantes recibe?", "5*4", "Se multiplican los grupos por los visitantes de cada uno.", " visitantes"),
        ex("Dos reglas: ir con guía y no tocar las paredes. ¿Cuántas reglas hay?", "2", "Hay dos reglas."),
    ],
    context=[ex("Al visitar un sitio de práctica, Lía ve una piedra con dibujos y quiere tocarla. El guía le dice que no. ¿Por qué?", "Para cuidar la piedra", "Tocarla puede dañarla.")],
    selfcheck=[ex("Escribe un ejemplo de patrimonio vivo.", "Una fiesta o una comida", "Se hacen hoy."), ex("¿Qué ley protege los sitios arqueológicos?", "La ley de Monumentos Nacionales", "Es el dato de la clase."), ex("Verdadero o falso: puedes entrar a cualquier sitio sin permiso.", "Falso", "Algunos tienen condiciones de acceso.")],
    task=T("Dibuja dos columnas: «patrimonio vivo» y «huellas del pasado». Escribe tres ejemplos en cada una, usando los de la clase o los de tu barrio. Luego escribe tres reglas para visitar un sitio arqueológico de práctica. No dibujes lugares sagrados reales.",
           "Vivo: fiesta, comida, técnica. Huellas: pukará, cerámica antigua, piedra con dibujos. Reglas: ir con guía; no llevarse nada; preguntar horarios.",
           ["clasifica bien", "escribe tres reglas", "no dibuja lugares sagrados"], ["dos columnas", "tres reglas"], ["clasificar mal", "reglas peligrosas"],
           "Revisar la clasificación y las reglas."),
    reinforce="Copia tres reglas de visita en tu cuaderno.",
    extend="Escribe una pregunta sobre las reglas de visita de un lugar de tu zona para un educador tradicional.",
)

L(
    OA15, 4,
    materials="Lápiz y hojas. Los casos son inventados.",
    use="Aprenderé a cuidar el patrimonio con acciones concretas: no llevarse nada, avisar a un adulto si encuentro algo y devolver cuidado. Sirve para proteger lo que es de todos y de la comunidad.",
    prior=["Sé qué es patrimonio.", "Sé que hay reglas de acceso."],
    explain=[
        "Cuidar el patrimonio es tarea de todos. En un sitio arqueológico o en un espacio natural, no nos llevamos nada, no escribimos ni rayamos nada, y no tocamos lo que no debemos. Tomamos fotos solo si se permite. Cumplimos las reglas.",
        "Si encontramos algo que parece antiguo, como un trozo de cerámica o una piedra trabajada, no lo tomamos ni lo movemos. Avisamos a un adulto, que podrá informar a las autoridades. Así se protege la memoria del lugar y de la comunidad.",
        "También cuidamos el patrimonio vivo. Escuchamos a quienes enseñan, pedimos permiso para fotografiar y agradecemos. Compramos productos a precio justo y reconocemos a quien los hizo. Cuidar el patrimonio es una forma de reciprocidad con las comunidades.",
    ],
    vocab=[("hallazgo", "algo que se encuentra"), ("informar", "avisar a quien debe saberlo"), ("autoridad", "persona o institución encargada de cuidar algo"), ("rayar", "hacer marcas sobre una superficie"), ("reciprocidad", "devolver cuidado por lo que recibimos")],
    worked=[
        W("Qué hacer con un hallazgo", "En una excursión, un niño encuentra un trozo de cerámica que parece antiguo. ¿Qué hace? a) lo guarda en su bolsillo b) lo deja donde está y avisa a un adulto c) lo muestra a todos.", ["No debe moverlo.", "Avisar a un adulto permite informar.", "Elijo b."], "b"),
        W("Cuidar el patrimonio vivo", "Alguien enseña una técnica de tejido a tu curso. ¿Qué haces? a) agradezco y pido permiso para fotos b) grabo sin permiso c) copio su diseño.", ["Agradecer y pedir permiso cuidan.", "Grabar sin permiso o copiar no respetan.", "Elijo a."], "a"),
    ],
    mistakes=[
        M("Llevarse un trozo de cerámica como recuerdo.", "Se pierde parte de la memoria del lugar.", "Déjalo donde está y avisa a un adulto."),
        M("Escribir tu nombre en una piedra de un sitio.", "Daña el lugar para siempre.", "Escríbelo en tu cuaderno."),
    ],
    R=[
        ex("Si encuentras algo antiguo, ¿lo dejas donde está? Responde Sí o No.", "Sí", "Así se protege el lugar."),
        ex("Rayar una piedra de un sitio es dañarlo. ¿Verdadero o falso?", "Verdadero", "Las marcas quedan para siempre."),
        ex("Pedir permiso para fotografiar es una forma de respeto. ¿Verdadero o falso?", "Verdadero", "Respeta a las personas."),
    ],
    C=[
        ex("¿A quién avisas si encuentras algo antiguo? A) A un adulto B) A nadie", "A", "Un adulto puede informar a las autoridades."),
        ex("Verdadero o falso: se puede mover un hallazgo para sacarle una foto.", "Falso", "Moverlo puede perder información."),
        ex("¿Qué haces con un producto de un artesano? A) Pago un precio justo B) Pido que lo regale", "A", "Se reconoce su trabajo."),
    ],
    A=[
        ex("Marca las acciones de cuidado: a) no llevarse nada b) rayar una piedra c) avisar a un adulto d) cumplir las reglas.", "a, c y d", "Cuidan el sitio."),
        ex("Ordena: 1) aviso a un adulto 2) veo algo antiguo 3) lo dejo donde está. Escribe el orden.", "2, 3, 1", "Primero lo veo, luego lo dejo y al final aviso."),
        arith("Un grupo cuida un sitio con 3 reglas por día durante 5 días. ¿Cuántas veces cumplen una regla en total?", "3*5", "Se multiplican las reglas por los días.", " veces"),
    ],
    Z=[
        ex("Tomás dice: «Es solo un pedacito, no importa». ¿Qué le dirías?", "Que si todos se llevan uno, se pierde el sitio", "Cada trozo guarda memoria."),
        ex("Lía quiere publicar en internet la ubicación exacta de un sitio frágil. ¿Qué debe hacer primero?", "Preguntar a la comunidad o a la autoridad", "Pueden pedir que no se publique."),
    ],
    D=[
        ex("Cuatro acciones: pedir permiso, agradecer, pagar un precio justo y reconocer al creador. ¿Cuántas acciones de cuidado hay?", "4", "Se cuentan las cuatro."),
        ex("Un visitante se lleva una piedra de un sitio y luego la devuelve. ¿Qué debe hacer además? A) Avisar y pedir disculpas B) No decir nada", "A", "Repara su error."),
    ],
    context=[ex("Tu curso visita un parque con un sitio de práctica. Julia ve una piedra con dibujos y quiere llevársela. Su profesora le dice que no. ¿Qué debe hacer Julia? A) Dejarla donde está B) Esconderla", "A", "Las piedras con dibujos no se mueven.")],
    selfcheck=[ex("Escribe dos acciones para cuidar un sitio.", "No llevarse nada y avisar a un adulto", "Cuidan el lugar."), ex("¿Qué haces si encuentras algo antiguo?", "Lo dejo y aviso a un adulto", "Se protege el hallazgo."), ex("Verdadero o falso: rayar una piedra de un sitio está bien.", "Falso", "Rayar es dañarlo.")],
    task=T("Crea un afiche de cuidado del patrimonio con cinco reglas para visitar un sitio arqueológico de práctica. Una debe decir qué hacer si encuentras algo antiguo, otra qué hacer con las fotos y otra cómo agradecer. Dibuja el afiche sin lugares sagrados reales.",
           "1. No llevarse nada. 2. Dejar y avisar a un adulto si hallo algo. 3. Pedir permiso para fotos. 4. No rayar. 5. Agradecer al guía.",
           ["escribe cinco reglas", "incluye hallazgo, fotos y agradecimiento", "no dibuja lugares sagrados"], ["afiche", "cinco reglas"], ["reglas peligrosas", "olvidar el hallazgo"],
           "Revisar que las cinco reglas sean seguras y claras."),
    reinforce="Elige dos reglas del afiche y explícalas a un adulto.",
    extend="Escribe una regla más para cuidar el patrimonio de tu barrio.",
)
