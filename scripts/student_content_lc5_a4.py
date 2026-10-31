"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 14 (técnicas productivas y equilibrio con la naturaleza), OA 15 (patrimonio cultural y natural) y
OA 16 (ser humano, naturaleza, cosmos y ciencia).

Las comunidades, las técnicas, los lugares y las personas son INVENTADOS y se rotulan así. No se afirma nada
de técnicas, calendarios, astronomía ni cosmovisión de un pueblo real: eso lo explican la comunidad y el
educador/a tradicional. Datos generales usados: la Luna tarda alrededor de 30 días en completar sus fases y el
Sol nunca se mira directamente.
"""
from __future__ import annotations

from student_content_lc5_a import L, M, MAT, T, W
from student_lessons import arith, ex

OA14, OA15, OA16 = "LC05 OA 14", "LC05 OA 15", "LC05 OA 16"

TLV = ("Testimonio inventado de doña Elena, de Ladera Verde: «Sembramos en terrazas. Tenemos seis parcelas y cada año dos descansan para que la tierra se recupere. "
       "El agua de la quebrada se reparte por turnos entre las familias. Esto lo aprendimos de nuestros abuelos.»")
TIN = ("Testimonio inventado de don Camilo, de Isla Niebla: «Salimos a pescar por turnos para no pescar siempre en el mismo lugar. Devolvemos al mar los peces pequeños. "
       "De la leña del bosque solo tomamos la que está seca en el suelo.»")

# ============================================================ OA 14 · Técnicas productivas y equilibrio con la naturaleza
L(
    OA14, 1, materials=MAT,
    use="Aprenderé a situar una técnica de producción de una comunidad: quién la realiza, qué recurso de la naturaleza usa y cómo cuida el equilibrio. Sirve para valorar el trabajo de las personas sin inventar técnicas de un pueblo real.",
    prior=["Sé situar una fuente con su ficha.", "Sé que la producción es lo que una comunidad cultiva, pesca, cría o elabora."],
    explain=[
        "Una técnica productiva es la manera de hacer un trabajo para obtener algo que la comunidad necesita: sembrar, pescar, tejer, recolectar o construir. Las personas que la realizan la aprendieron de otras y la han mejorado con el tiempo. Su trabajo ayuda a que el pueblo siga viviendo de su territorio.",
        "Muchas técnicas se hacen buscando equilibrio con la naturaleza. Equilibrio significa tomar lo que se necesita y dejar que la naturaleza se recupere. Por ejemplo, dejar descansar la tierra o devolver los peces pequeños. Así el recurso no se acaba y las próximas generaciones también pueden usarlo.",
        "Para situar una técnica miramos cuatro datos de la ficha: la comunidad, la persona o personas que la hacen, el recurso natural que usa y el cuidado que tiene. Los datos de técnicas de un pueblo real los entrega su comunidad. Aquí usamos testimonios inventados.",
    ],
    vocab=[("técnica productiva", "manera de hacer un trabajo para obtener lo que se necesita"), ("recurso natural", "algo de la naturaleza que se usa, como el agua o la leña"), ("equilibrio", "tomar lo necesario y dejar que la naturaleza se recupere"), ("generación", "grupo de personas de edades parecidas"), ("permanencia", "que algo continúe en el tiempo")],
    worked=[
        W("Situar una técnica", TLV + " ¿Qué técnica, qué recurso y qué cuidado hay?", ["La técnica es sembrar en terrazas con parcelas que descansan.", "Los recursos son la tierra y el agua de la quebrada.", "El cuidado es dejar descansar dos parcelas y repartir el agua por turnos."], "Técnica: sembrar en terrazas. Recursos: tierra y agua. Cuidado: parcelas que descansan y agua por turnos."),
        W("Reconocer a quienes la realizan", "En el testimonio, ¿de quién aprendió la comunidad la técnica?", ["Busco «aprendimos».", "Dice «de nuestros abuelos».", "Las personas mayores la transmitieron."], "De sus abuelos."),
    ],
    mistakes=[
        M("Pensar que una técnica de una comunidad vale para todos los pueblos.", "Cada pueblo tiene las suyas.", "Nombra la comunidad y la fuente."),
        M("Creer que cuidar el equilibrio es no usar nunca los recursos.", "Equilibrio es usar lo necesario y dejar que se recupere.", "Describe cómo se toma y cómo se deja recuperar."),
    ],
    R=[
        ex("Doña Elena (inventada) cuenta que tienen seis parcelas y cada año dos descansan. ¿Cuántas parcelas tienen?", "Seis", "El testimonio lo dice."),
        ex("Don Camilo (inventado) dice: «Devolvemos al mar los peces pequeños». ¿Qué devuelven al mar?", "Los peces pequeños", "El testimonio lo dice."),
        ex("¿Qué recurso usa la técnica de repartir el agua de la quebrada por turnos? A) el agua B) la leña", "A", "El agua es el recurso."),
    ],
    C=[
        ex("Verdadero o falso: el equilibrio es tomar lo que se necesita y dejar que la naturaleza se recupere.", "Verdadero", "Es la definición de la clase."),
        ex("¿Qué es una técnica productiva? A) una manera de hacer un trabajo para obtener lo que se necesita B) una fiesta", "A", "Es el modo de trabajar."),
        ex("Verdadero o falso: una técnica de Ladera Verde sirve para explicar a todos los pueblos.", "Falso", "Cada pueblo tiene las suyas."),
    ],
    A=[
        ex("Clasifica en TÉCNICA o CUIDADO DEL EQUILIBRIO, según el testimonio de doña Elena: a) sembrar en terrazas b) dejar descansar dos parcelas cada año.", "a técnica, b cuidado del equilibrio", "Sembrar es el trabajo; el descanso protege la tierra."),
        ex("Don Camilo dice: «De la leña del bosque solo tomamos la que está seca en el suelo». ¿Qué cuidado hay? A) tomar solo leña seca del suelo B) cortar árboles", "A", "El testimonio lo dice."),
        ex("Una ficha trae técnica y recurso, pero no dice quién la hace. ¿Qué falta? A) la persona o la comunidad B) una imagen", "A", "Sin la persona no se sabe de quién es la técnica."),
    ],
    Z=[
        ex("Tomás dice: «Si dejan descansar la tierra, trabajan menos». ¿Qué error comete?", "No ve que el descanso protege la tierra", "El descanso permite que la tierra se recupere."),
        ex("¿Por qué conviene nombrar a quien aprendió y enseña una técnica? A) porque su trabajo permite que el saber continúe B) para ocupar espacio", "A", "Reconoce a las personas que sostienen la técnica."),
    ],
    D=[
        ex("Dos fichas inventadas: Ladera Verde (terrazas y parcelas) e Isla Niebla (pesca por turnos). Alguien escribe «los turnos de pesca evitan pescar siempre en el mismo lugar». ¿De cuál ficha viene?", "De Isla Niebla", "Es el testimonio de don Camilo."),
        ex("Un compañero quiere describir una técnica de un pueblo real que vio en un video. ¿Qué haces? A) pido la fuente al educador tradicional B) la describo igual", "A", "La técnica de un pueblo real la cuenta su comunidad."),
    ],
    context=[ex("Tu curso hace una huerta escolar. Alguien propone usar toda la tierra todos los años sin dejarla descansar. Según la clase, ¿qué aprendes del testimonio de Ladera Verde? A) conviene dejar descansar parte de la tierra B) no importa", "A", "El equilibrio incluye dejar que la tierra se recupere.")],
    selfcheck=[
        ex("Explica con tus palabras qué es el equilibrio con la naturaleza.", "Tomar lo necesario y dejar que la naturaleza se recupere", "Es la definición de la clase."),
        ex("Verdadero o falso: las personas que realizan una técnica merecen reconocimiento.", "Verdadero", "Su trabajo sostiene la comunidad."),
        ex("¿Quién explica las técnicas de un pueblo real? A) su comunidad o el educador tradicional B) cualquiera", "A", "Ellos son la fuente."),
    ],
    task=T("Lee este testimonio inventado de doña Marta, de Pampa Larga: «Sacamos agua del pozo con baldes y por turnos, y nunca vaciamos el pozo del todo. Mi madre me enseñó a cuidar las cuerdas.» Haz una ficha con: comunidad, persona, técnica, recurso natural, cuidado del equilibrio y a quién reconoces. Escribe una frase con «yo pienso que…» sobre por qué ese cuidado es importante.",
           "Comunidad: Pampa Larga. Persona: doña Marta. Técnica: sacar agua con baldes por turnos. Recurso: el agua del pozo. Cuidado: no vaciar el pozo del todo. Reconozco a su madre, que le enseñó. Yo pienso que el cuidado ayuda a que el pozo no se acabe.",
           ["completa la ficha con datos del testimonio", "reconoce a las personas", "marca su idea"], ["ficha de seis campos", "frase con «yo pienso que»"], ["agregar técnicas que no están", "generalizar a todos los pueblos"],
           "Pedir que muestre en qué línea está cada dato."),
    reinforce="Subraya en el testimonio de doña Elena la técnica con un color y el cuidado del equilibrio con otro.",
    extend="Escribe una pregunta que le harías a una persona de tu comunidad sobre una técnica que aprendió de su familia.",
)

L(
    OA14, 2, materials=MAT,
    use="Aprenderé a leer un testimonio sobre una técnica con límites: qué hace la persona, qué cuidados tiene y qué no cuenta. Sirve para valorar su trabajo con datos y cuentas, sin inventar.",
    prior=["Sé situar una técnica con su ficha.", "Sé hacer multiplicaciones y divisiones sencillas."],
    explain=[
        "Al leer un testimonio sobre una técnica separamos tres cosas. Lo que la persona hace, es decir, los pasos de su trabajo. Los cuidados que tiene, es decir, cómo protege la naturaleza. Y lo que no cuenta, como un lugar especial, una forma de guardar semillas o una manera de repartir.",
        "Podemos usar cuentas para entender mejor una técnica. Por ejemplo, si una comunidad tiene 6 parcelas y 2 descansan cada año, quedan 4 parcelas para sembrar. Si 12 familias se reparten el agua en 3 turnos iguales, hay 4 familias por turno. Las cuentas ayudan a ver el cuidado del equilibrio.",
        "No inventamos pasos que el testimonio no cuenta. Si falta información, escribimos «el testimonio no lo dice». Y si queremos saber algo reservado, no insistimos: preguntamos al educador o educadora tradicional qué se puede conocer.",
    ],
    vocab=[("paso", "cada parte de un trabajo, en orden"), ("parcela", "pedazo de tierra para sembrar"), ("turno", "momento que le toca a cada persona o familia"), ("reservado", "lo que la persona prefiere no contar"), ("cuenta", "operación con números")],
    worked=[
        W("Separar tres cosas", TLV + " Separa lo que hace, el cuidado y lo que no dice.", ["Hace: siembra en terrazas y reparte el agua.", "Cuidado: dejar descansar dos parcelas.", "No dice: cómo se decide qué parcelas descansan."], "Hace: siembra y reparte el agua. Cuidado: dos parcelas descansan. No dice: cómo se elige cuáles descansan."),
        W("Cuenta del cuidado", "Si hay 6 parcelas y 2 descansan, ¿cuántas se siembran?", ["Total: 6.", "Descansan: 2.", "Resto: 6 − 2."], "4 parcelas."),
    ],
    mistakes=[
        M("Inventar los pasos de una técnica que no se contaron.", "Cambia la técnica de la comunidad.", "Escribe «el testimonio no lo dice»."),
        M("Insistir en un secreto de la técnica.", "No se respeta la decisión de la persona.", "Pregunta al educador qué se puede conocer."),
    ],
    R=[
        ex("Si de 6 parcelas descansan 2, ¿cuántas se siembran?", "4", "6 − 2 = 4."),
        ex("Doña Elena (inventada) no dice cómo se elige qué parcelas descansan. ¿Qué escribes? A) el testimonio no lo dice B) las elige el más viejo", "A", "No se inventa."),
        ex("Don Camilo (inventado): «Devolvemos al mar los peces pequeños». ¿Es un paso o un cuidado? A) un cuidado B) un secreto", "A", "Protege a los peces pequeños para que crezcan."),
    ],
    C=[
        ex("Verdadero o falso: una cuenta puede ayudar a entender el cuidado del equilibrio.", "Verdadero", "Las cantidades muestran cuánto se deja descansar."),
        ex("¿Qué es un turno? A) el momento que le toca a cada persona o familia B) un tipo de semilla", "A", "Se usa para repartir de manera justa."),
        ex("Verdadero o falso: puedo agregar pasos a la técnica si me parecen lógicos.", "Falso", "Sería inventar la técnica."),
    ],
    A=[
        arith("Doña Elena tiene 6 parcelas y 2 descansan. ¿Cuántas parcelas se siembran este año?", "6-2", "Se resta lo que descansa."),
        arith("12 familias se reparten el agua de la quebrada en 3 turnos iguales. ¿Cuántas familias hay por turno?", "12//3", "Se reparten las familias en grupos iguales."),
        ex("Clasifica en LO QUE HACE o LO QUE NO CUENTA: a) repartir el agua por turnos b) cómo se guarda una semilla especial, que no se contó.", "a lo que hace, b lo que no cuenta", "La primera es un paso del testimonio; la segunda es una reserva."),
    ],
    Z=[
        ex("Marcela dice: «Como 2 de 6 parcelas descansan, la comunidad pierde un tercio de su cosecha». ¿Qué problema tiene?", "No reconoce el cuidado de la tierra", "El descanso es parte de la técnica."),
        ex("¿Qué debe hacer alguien que no entiende un paso del testimonio? A) preguntar al educador tradicional B) inventarlo", "A", "Él o ella es la fuente."),
    ],
    D=[
        arith("En Isla Niebla (inventada) salen 5 botes por turno y hay 3 turnos por semana. ¿Cuántas salidas de botes hay en una semana?", "5*3", "Se repite 5 botes en 3 turnos."),
        arith("Una comunidad inventada recoge 36 atados de leña seca y los reparte en partes iguales entre 9 familias. ¿Cuántos atados recibe cada familia?", "36//9", "Se reparte en partes iguales."),
    ],
    context=[ex("En tu huerta escolar hay 8 camas de cultivo. Siguiendo la idea del descanso de Ladera Verde, dejas descansar 3. ¿Cuántas camas siembras? Responde con un número.", "5", "8 − 3 = 5.")],
    selfcheck=[
        ex("Nombra las tres cosas que separas al leer una técnica.", "Lo que hace, los cuidados y lo que no cuenta", "Están en la explicación."),
        ex("Verdadero o falso: puedo insistir en saber un secreto de la técnica.", "Falso", "Se respeta la decisión de la persona."),
        ex("¿Qué escribes si falta un paso? A) el testimonio no lo dice B) lo invento", "A", "Es la forma honesta."),
    ],
    task=T("Lee este testimonio inventado de don Aurelio, de Río Hondo: «Hacemos hilo con la lana de nuestras ovejas. Esquilamos solo una vez al año. Repartimos la lana en partes iguales entre las 8 familias que tejen y hoy tenemos 48 madejas. Hay una mezcla de tintes que no contamos.» Responde: ¿qué hace la comunidad?, ¿qué cuidado tiene?, ¿qué no cuenta? Calcula cuántas madejas recibe cada familia.",
           "Hacen hilo con lana de sus ovejas. Cuidado: esquilan solo una vez al año. No cuentan la mezcla de tintes. Cada familia recibe 48 ÷ 8 = 6 madejas.",
           ["responde las tres preguntas", "calcula bien", "respeta el límite"], ["tres respuestas", "cuenta con resultado"], ["inventar la mezcla de tintes", "error de cálculo"],
           "Pedir que muestre la cuenta y la frase del testimonio."),
    reinforce="Haz una tabla con tres columnas: hace, cuida y no cuenta, para el testimonio de doña Elena.",
    extend="Inventa una cuenta sobre el reparto de una cosecha en tu huerta escolar y resuélvela.",
)

L(
    OA14, 3, materials=MAT,
    use="Aprenderé a reconocer cómo una técnica se relaciona con el equilibrio, con las personas que la hacen y con la permanencia del pueblo. Sirve para valorar por qué estas técnicas importan hoy.",
    prior=["Sé leer un testimonio de técnicas con límites.", "Sé qué es equilibrio con la naturaleza."],
    explain=[
        "Las técnicas productivas se relacionan con tres cosas. Con la naturaleza: cuidan el recurso para que no se acabe. Con las personas: las hacen, las enseñan y las mejoran. Y con el futuro del pueblo: permiten que sus integrantes tengan lo que necesitan hoy y mañana. A eso se llama permanencia y proyección material y cultural.",
        "Si se rompe el equilibrio, se pone en riesgo todo. Por ejemplo, si una comunidad inventada pesca todo lo que puede cada día, los peces no alcanzan a crecer y mañana habrá menos. Con cuentas lo vemos: si cada día se sacan 10 peces de más, en 5 días faltan 50 peces.",
        "Las técnicas también cambian. Una comunidad puede usar un balde nuevo o una herramienta que no existía antes sin perder el cuidado del equilibrio. Valorar las técnicas es reconocer que continúan en el tiempo y se enseñan a las nuevas generaciones. Esto se anota con la fuente.",
    ],
    vocab=[("permanencia", "que algo continúe en el tiempo"), ("proyección", "que algo pueda seguir hacia el futuro"), ("riesgo", "posibilidad de que algo se dañe"), ("sobreexplotar", "sacar más de lo que la naturaleza puede recuperar"), ("herramienta", "objeto que ayuda a hacer un trabajo")],
    worked=[
        W("Ver el riesgo con una cuenta", "En una caleta inventada se sacan cada día 10 peces más de los que la naturaleza puede recuperar. ¿Cuántos peces faltarán en 5 días?", ["Cada día faltan 10.", "Son 5 días.", "Multiplico 10 × 5."], "50 peces."),
        W("Cambio sin perder el cuidado", "Don Camilo (inventado) dice: «Ahora usamos un bote nuevo, pero seguimos devolviendo los peces pequeños». ¿Qué cambió y qué continúa?", ["Cambió el bote.", "Continúa devolver los peces pequeños.", "El cuidado del equilibrio sigue."], "Cambió el bote; continúa el cuidado de devolver los peces pequeños."),
    ],
    mistakes=[
        M("Pensar que conservar una técnica es no cambiar nada.", "Pueden cambiar las herramientas manteniendo el cuidado.", "Distingue lo que cambia y lo que continúa."),
        M("Creer que tomar más hoy no afecta el mañana.", "Sobreexplotar reduce lo que habrá después.", "Haz una cuenta del riesgo."),
    ],
    R=[
        ex("Don Camilo (inventado) dice: «Seguimos devolviendo los peces pequeños». ¿Qué cuidado continúa?", "Devolver los peces pequeños", "El testimonio lo dice."),
        ex("¿Qué es sobreexplotar? A) sacar más de lo que la naturaleza puede recuperar B) cuidar el recurso", "A", "Es romper el equilibrio."),
        arith("Si cada día se sacan 10 peces de más, ¿cuántos peces habrá de menos en 2 días?", "10*2", "Se repite el exceso de cada día."),
    ],
    C=[
        ex("Verdadero o falso: una técnica puede cambiar de herramientas y mantener el cuidado del equilibrio.", "Verdadero", "Lo importante es el cuidado."),
        ex("Verdadero o falso: sacar más de lo que se puede recuperar pone en riesgo el futuro.", "Verdadero", "Los recursos pueden acabarse."),
        ex("¿Qué es la proyección de un pueblo? A) que pueda seguir hacia el futuro B) un dibujo", "A", "Es la continuidad hacia adelante."),
    ],
    A=[
        arith("Si en una caleta inventada cada día se sacan 10 peces de más, ¿cuántos peces de más se sacan en 7 días?", "10*7", "Se repite 10 siete veces."),
        ex("Clasifica en CAMBIA o CONTINÚA, según don Camilo: a) ahora usan un bote nuevo b) devuelven los peces pequeños.", "a cambia, b continúa", "El bote es nuevo; el cuidado es el mismo."),
        ex("Una comunidad enseña a sus niños a cuidar las terrazas. ¿Qué asegura? A) que la técnica continúe B) que se pierda", "A", "La transmisión asegura continuidad."),
    ],
    Z=[
        ex("Bruno dice: «Usar un bote con motor significa que ya no cuidan el equilibrio». ¿Qué error comete?", "No distingue herramienta y cuidado", "Lo que importa es si continúa el cuidado."),
        ex("¿Por qué las personas que hacen una técnica son importantes para la permanencia del pueblo? A) porque la practican y la enseñan B) porque salen en fotos", "A", "Mantienen y transmiten el saber."),
    ],
    D=[
        arith("En una comunidad inventada hay 40 peces y se sacan 8 cada día sin que se recuperen. ¿Cuántos peces quedan después de 3 días?", "40-8*3", "Se resta lo sacado: 8 × 3 = 24, y 40 − 24 = 16."),
        ex("Un testimonio dice: «Dejamos descansar el río un mes cada año». Quieres escribir que lo hacen «para siempre». ¿Qué haces? A) escribo «cada año, según el testimonio» B) escribo «para siempre»", "A", "No se exagera."),
    ],
    context=[ex("Tu curso propone cosechar de una vez todos los frutos del árbol del patio. Según lo aprendido, ¿qué es mejor? A) cosechar parte y dejar el resto B) cosechar todo", "A", "Dejar parte cuida el equilibrio.")],
    selfcheck=[
        ex("Nombra las tres cosas con que se relaciona una técnica.", "La naturaleza, las personas y el futuro del pueblo", "Están en la explicación."),
        ex("Verdadero o falso: una técnica puede continuar aunque cambien las herramientas.", "Verdadero", "El cuidado puede seguir."),
        ex("¿Qué haces con una afirmación exagerada? A) la ajusto a lo que dice el testimonio B) la dejo", "A", "Se evita exagerar."),
    ],
    task=T("Lee este testimonio inventado de doña Elena, de Ladera Verde: «Antes cargábamos el agua en baldes de cuero. Ahora usamos mangueras para llegar a las terrazas, pero seguimos repartiendo el agua por turnos. Enseñamos a los niños a revisar que no se pierda agua.» Haz una tabla de tres columnas: qué cambió, qué continúa y qué persona o personas lo transmiten. Calcula: si cada niño revisa 4 terrazas y son 7 niños, ¿cuántas terrazas revisan en total? Escribe una frase con «yo pienso que…» sobre por qué ese cuidado ayuda a que la comunidad siga en su territorio.",
           "Cambió: de baldes de cuero a mangueras. Continúa: repartir el agua por turnos. Transmiten: las personas que enseñan a los niños. Terrazas revisadas: 7 × 4 = 28. Yo pienso que cuidar el agua ayuda a que la comunidad pueda seguir sembrando.",
           ["tabla completa", "cuenta correcta", "idea propia marcada"], ["tabla de tres columnas", "cuenta", "frase"], ["inventar datos", "error de cálculo"],
           "Pedir que muestre la línea del testimonio de cada celda."),
    reinforce="Pinta lo que cambia y lo que continúa con dos colores en tu tabla.",
    extend="Escribe una técnica de tu casa o barrio que haya cambiado de herramienta pero mantenga un cuidado.",
)

L(
    OA14, 4, materials=MAT,
    use="Aprenderé a escribir un reconocimiento atribuido del valor de una técnica y de las personas que la realizan. Sirve para valorar su aporte a la permanencia del pueblo y al equilibrio con la naturaleza.",
    prior=["Sé relacionar técnica, equilibrio y personas.", "Sé atribuir y marcar mis ideas."],
    explain=[
        "Un reconocimiento atribuido valora una técnica y a quienes la realizan, y dice de dónde viene cada dato. Tiene cinco partes: quién es la persona o la comunidad; qué técnica realiza y qué recurso usa; qué cuidado tiene con la naturaleza; por qué importa para la permanencia del pueblo (según la fuente) y qué pienso yo; y qué límites y preguntas quedan.",
        "En la parte «por qué importa», uso solo lo que la fuente dice. Por ejemplo, si el testimonio dice que enseñan a los niños, puedo escribir que eso ayuda a que la técnica continúe. Si el testimonio no habla de la importancia, lo marco como idea mía con «yo pienso que».",
        "No exageramos, no comparamos con otras comunidades y no usamos a las personas como adorno. Terminamos agradeciendo y mostrando el texto a la persona o al educador tradicional, que puede decir si algo debe cambiar.",
    ],
    vocab=[("reconocimiento", "texto que valora el aporte de una persona"), ("proyección", "continuidad hacia el futuro"), ("atribuir", "decir de quién viene un dato"), ("exagerar", "decir más de lo que dice la fuente"), ("agradecer", "reconocer con palabras lo recibido")],
    worked=[
        W("Escribir un reconocimiento", TIN + " Escribe un reconocimiento breve.", ["Persona: don Camilo, de Isla Niebla.", "Técnica: pescar por turnos y devolver peces pequeños; recurso: el mar.", "Cuidado e importancia."], "Don Camilo, de Isla Niebla (inventado), pesca por turnos y devuelve los peces pequeños. Yo pienso que así el mar sigue dando peces para la comunidad. No sé cómo se arman los turnos. Gracias por enseñarnos."),
        W("Evitar la exageración", "Un niño escribe: «Gracias a don Camilo nadie en la isla pasa hambre». ¿Qué corriges?", ["El testimonio no habla de hambre.", "Es una exageración.", "Debo ajustarlo."], "Corrijo: «Según don Camilo, pescan por turnos y cuidan los peces pequeños»."),
    ],
    mistakes=[
        M("Escribir que una técnica «salva» a toda la comunidad sin que la fuente lo diga.", "Exagera.", "Usa lo que dice el testimonio."),
        M("Dejar fuera a quien enseñó la técnica.", "No se reconoce a las personas.", "Nombra a quienes la hacen y enseñan."),
    ],
    R=[
        ex("¿Cuántas partes tiene el reconocimiento de esta clase? Escribe el número.", "5", "Persona, técnica, cuidado, importancia con idea propia y límites."),
        ex("¿Con qué marca escribes tu idea? A) «yo pienso que» B) «según la fuente»", "A", "La segunda se usa para datos de la fuente."),
        ex("¿Qué haces al terminar? A) agradezco y muestro el texto B) lo guardo", "A", "Es la devolución."),
    ],
    C=[
        ex("Verdadero o falso: puedo escribir que una técnica salva a toda la comunidad si me parece.", "Falso", "Exagera y no está en la fuente."),
        ex("¿Para qué se nombra a la persona? A) para reconocer su aporte B) para decorar", "A", "Su trabajo sostiene la técnica."),
        ex("Verdadero o falso: en un reconocimiento no se comparan comunidades.", "Verdadero", "Cada una se valora por sí misma."),
    ],
    A=[
        ex("Ordena: A) límites B) persona C) técnica D) cuidado. ¿Cuál va primero?", "B", "Se parte con la persona o comunidad."),
        ex("Clasifica en DATO DE LA FUENTE o MI IDEA: a) según doña Elena, enseñan a los niños a revisar el agua b) yo pienso que así la comunidad cuidará el agua en el futuro.", "a dato de la fuente, b mi idea", "La primera está escrita; la segunda es mía."),
        ex("Don Camilo dice que pescan por turnos, pero no explica cómo se arman. ¿Cuál es un límite bien escrito? A) No sé cómo se arman los turnos B) Seguro que los arma el pescador más antiguo", "A", "El límite declara lo que el testimonio no explica."),
    ],
    Z=[
        ex("Gabriela escribe: «Esta técnica es mejor que las de otras comunidades». ¿Qué error comete?", "Compara y jerarquiza sin fuente", "En un reconocimiento no se comparan."),
        ex("¿Por qué se muestra el texto a la persona? A) para que corrija lo que quedó mal B) para presumir", "A", "Ella conoce su técnica."),
    ],
    D=[
        ex("Dos reconocimientos de Ladera Verde. A: «Según doña Elena, dejan descansar parte de la tierra; yo pienso que cuidan el suelo». B: «Doña Elena inventó el descanso de la tierra». ¿Cuál es correcto?", "A", "B agrega un dato no dicho."),
        ex("Quieres vender dibujos con la técnica de doña Elena, sin avisarle. ¿Qué haces? A) pido permiso y reconozco a la fuente B) vendo", "A", "Hace falta autorización."),
    ],
    context=[ex("Preparas un homenaje en el acto de la escuela a una persona de la comunidad que enseña una técnica. ¿Qué dices? A) reconozco su aporte con datos de lo que ella contó B) invento una historia", "A", "El homenaje se apoya en la fuente.")],
    selfcheck=[
        ex("Nombra tres partes del reconocimiento.", "Tres entre: persona, técnica, cuidado, importancia con idea propia, límites", "Están en la explicación."),
        ex("Verdadero o falso: debo evitar exagerar.", "Verdadero", "Ajusto a lo que dice la fuente."),
        ex("¿A quién puedo preguntar si algo debe cambiar en mi texto? A) a la persona o al educador tradicional B) a nadie", "A", "Ellos pueden corregir."),
    ],
    task=T("Usa este testimonio inventado de doña Marta, de Pampa Larga: «Cuidamos el pozo entre todos y sacamos agua por turnos. Mi madre me enseñó a revisar las cuerdas y yo enseño a mis nietos. Hay un lugar cerca del pozo que no mostramos.» Escribe un reconocimiento de cinco partes: persona, técnica y recurso, cuidado, importancia (con «yo pienso que») y límites con una pregunta para el educador tradicional. No describas el lugar que no se muestra.",
           "Doña Marta, de Pampa Larga (inventada), cuida el pozo entre todos y saca agua por turnos. Su madre le enseñó a revisar las cuerdas y ella enseña a sus nietos. Yo pienso que así la técnica continúa. No se muestra un lugar cerca del pozo. Pregunta: ¿qué otras técnicas del agua se pueden conocer en la escuela?",
           ["incluye las cinco partes", "usa solo datos del testimonio", "respeta el lugar reservado"], ["reconocimiento de cinco partes"], ["describir el lugar reservado", "exagerar"],
           "Pedir que señale de qué línea sale cada dato."),
    reinforce="Numera las cinco partes de tu reconocimiento para comprobar que están todas.",
    extend="Escribe una frase de agradecimiento corta para doña Marta, sin datos reservados.",
)

# ============================================================ OA 15 · Patrimonio cultural y natural
PAT = ("Ficha situada (inventada). Comunidad: Ladera Verde (no es un pueblo real). Patrimonios que menciona doña Elena: las terrazas, la quebrada, el relato de la Abuela Niebla y la forma de repartir el agua por turnos. "
       "Fuente y responsable: doña Elena. Permiso: sí. Límite: no se muestra el lugar de respeto de la quebrada.")

L(
    OA15, 1, materials=MAT,
    use="Aprenderé a reconocer el patrimonio cultural y natural, material e inmaterial, de una comunidad y a situar quién lo cuida. Sirve para valorar lo que heredamos y aportar a su cuidado.",
    prior=["Sé situar una fuente con su ficha.", "Sé que el territorio incluye lugares y memoria."],
    explain=[
        "El patrimonio es lo que una comunidad recibe de quienes vivieron antes y quiere cuidar para quienes vendrán. Hay patrimonio cultural, que son las creaciones y costumbres de las personas, y patrimonio natural, que son los lugares y seres de la naturaleza que se valoran. Cada uno puede ser material o inmaterial.",
        "El patrimonio material se puede tocar y ver: terrazas, caminos, la sede, un cerro, una quebrada. El patrimonio inmaterial no se toca: relatos, lenguas, canciones, saberes, formas de trabajar juntos. Muchas veces los dos se unen: una terraza (material) guarda el saber de sembrar (inmaterial).",
        "Para reconocer el patrimonio de una comunidad, leemos su ficha: qué menciona, quién lo cuenta, con qué permiso y qué no se cuenta. El patrimonio de un pueblo real lo explican su comunidad y su educador tradicional. En tu propio barrio, escuela o familia también hay patrimonio que puedes reconocer con respeto.",
    ],
    vocab=[("patrimonio", "lo que se hereda y se quiere cuidar"), ("patrimonio material", "el que se puede ver y tocar"), ("patrimonio inmaterial", "el que no se toca: relatos, lenguas, saberes"), ("patrimonio natural", "lugares y seres de la naturaleza que se valoran"), ("heredar", "recibir de quienes vivieron antes")],
    worked=[
        W("Clasificar un patrimonio", PAT + " Clasifica «el relato de la Abuela Niebla» y «las terrazas».", ["El relato no se toca: es inmaterial.", "Las terrazas se pueden ver y tocar: son materiales.", "Las terrazas también guardan saberes."], "El relato es patrimonio cultural inmaterial; las terrazas son patrimonio cultural material."),
        W("Patrimonio de mi barrio", "En un barrio hay una plaza antigua, una receta que la vecina enseña a los niños y un árbol grande muy querido. Clasifica.", ["La plaza es cultural material.", "La receta es cultural inmaterial.", "El árbol es natural."], "Plaza: cultural material. Receta: cultural inmaterial. Árbol: natural."),
    ],
    mistakes=[
        M("Pensar que patrimonio es solo lo antiguo o lo caro.", "Es lo que una comunidad hereda y quiere cuidar.", "Pregunta qué cuida la comunidad."),
        M("Creer que lo inmaterial no necesita cuidado.", "Los relatos y saberes se pierden si no se transmiten.", "Piensa cómo se enseñan a las nuevas generaciones."),
    ],
    R=[
        ex("Ficha inventada de Ladera Verde: «el relato de la Abuela Niebla». ¿Se puede tocar un relato? Responde Sí o No.", "No", "Un relato es inmaterial."),
        ex("¿Las terrazas de Ladera Verde son patrimonio material o inmaterial?", "Material", "Se pueden ver y tocar."),
        ex("¿Qué es el patrimonio? A) lo que se hereda y se quiere cuidar B) lo que se compra", "A", "Es una herencia compartida."),
    ],
    C=[
        ex("Verdadero o falso: el patrimonio inmaterial incluye relatos, lenguas y saberes.", "Verdadero", "No se toca, pero se hereda."),
        ex("¿Qué es el patrimonio natural? A) lugares y seres de la naturaleza que se valoran B) un museo", "A", "Pertenece a la naturaleza."),
        ex("Verdadero o falso: el patrimonio es solo lo muy antiguo.", "Falso", "Es lo que se hereda y se cuida."),
    ],
    A=[
        ex("Clasifica en MATERIAL o INMATERIAL: a) una sede comunitaria b) una canción que los abuelos enseñan.", "a material, b inmaterial", "La sede se toca; la canción no."),
        ex("Clasifica en CULTURAL o NATURAL: a) una quebrada con agua b) una técnica para tejer.", "a natural, b cultural", "La quebrada es naturaleza; la técnica la crean las personas."),
        ex("Una ficha nombra un patrimonio pero no dice si hay permiso para contarlo. ¿Puedes usarla? Responde Sí o No.", "No", "Sin permiso no se comparte."),
    ],
    Z=[
        ex("Renata dice: «Los saberes no son patrimonio porque no se pueden tocar». ¿Qué error comete?", "Cree que solo lo material es patrimonio", "El patrimonio inmaterial también se hereda."),
        ex("¿Por qué la terraza se considera material e inmaterial a la vez? A) porque se puede tocar y guarda un saber de sembrar B) porque está en un cerro", "A", "Une el objeto y el saber."),
    ],
    D=[
        ex("En un barrio: un mural del año 1990, un cuento que cuenta una vecina y un cerro cercano. Une cada uno con su clase: 1) mural 2) cuento 3) cerro a) cultural material b) cultural inmaterial c) natural", "1-a, 2-b, 3-c", "El mural se toca, el cuento no, y el cerro es naturaleza."),
        ex("Quieres incluir en tu trabajo un lugar que la comunidad no muestra. ¿Qué haces? A) no lo incluyo B) lo busco en internet", "A", "Se respeta el límite."),
    ],
    context=[ex("Tu curso hará un catálogo del patrimonio de la escuela. Alguien propone incluir un cuento que contó un auxiliar, sin preguntarle. ¿Qué dices? A) hay que pedirle permiso primero B) incluirlo", "A", "El relato es suyo.")],
    selfcheck=[
        ex("Escribe un ejemplo de patrimonio material y uno de inmaterial.", "Por ejemplo: una plaza y una canción", "Cada uno cumple su definición."),
        ex("Verdadero o falso: una misma cosa puede tener parte material y parte inmaterial.", "Verdadero", "Como una terraza y su saber."),
        ex("¿Quién explica el patrimonio de un pueblo real? A) su comunidad B) cualquiera", "A", "Ella es la fuente."),
    ],
    task=T("Lee: «En Isla Niebla (inventada), don Camilo menciona la caleta, el sendero, el relato del Pez Mayor y la manera de devolver los peces pequeños. Permiso: sí. Límite: las historias reservadas no se cuentan.» Haz una tabla con cuatro filas: nombre, si es cultural o natural y si es material o inmaterial. Escribe una frase que diga qué dato sobre su cuidado la ficha no cuenta. Agrega dos ejemplos de patrimonio de tu barrio o escuela (uno material y uno inmaterial) que no necesiten permiso especial.",
           "Caleta: natural, material. Sendero: cultural, material. Relato del Pez Mayor: cultural, inmaterial. Devolver peces pequeños: cultural, inmaterial. La ficha no dice quiénes cuidan cada patrimonio. Mi barrio: una plaza (material) y un juego que enseñan los vecinos (inmaterial).",
           ["clasifica los cuatro", "agrega dos ejemplos propios", "respeta el límite"], ["tabla de cuatro filas", "dos ejemplos"], ["clasificar mal", "contar historias reservadas"],
           "Pedir que explique por qué eligió cada clasificación."),
    reinforce="Haz una lista de tres lugares de tu escuela y clasifícalos en cultural o natural.",
    extend="Escribe una pregunta para el educador tradicional sobre el patrimonio de tu zona.",
)

L(
    OA15, 2, materials=MAT,
    use="Aprenderé a leer un testimonio sobre patrimonio con límites: qué se puede mostrar, qué se cuida en silencio y qué permisos hacen falta. Sirve para respetar el patrimonio de otros y el mío.",
    prior=["Sé clasificar el patrimonio.", "Sé separar lo que dice la fuente de lo que interpreto."],
    explain=[
        "Al leer un testimonio sobre patrimonio buscamos tres cosas. Qué patrimonio nombra la persona, por qué lo valora y cómo se cuida. Luego revisamos los límites: qué se puede mostrar, qué se muestra solo con permiso y qué se cuida sin mostrarlo.",
        "Algunos patrimonios se pueden compartir con todos, como una plaza o una receta que la comunidad quiere enseñar. Otros se comparten solo con permiso, como un canto o un objeto. Y otros la comunidad prefiere cuidar en silencio, como un lugar importante. Por eso no se fotografía ni se publica sin autorización.",
        "Mi interpretación se marca con «yo pienso que». Si la persona no dice por qué valora algo, no lo invento. Si quiero ayudar a cuidar ese patrimonio, primero pregunto qué cuidado necesita y cómo puedo aportar, sin hacer nada por mi cuenta.",
    ],
    vocab=[("valorar", "darle importancia a algo y cuidarlo"), ("compartir", "dar a conocer a otras personas"), ("autorización", "permiso para mostrar o usar algo"), ("cuidar en silencio", "proteger algo sin mostrarlo"), ("aportar", "dar una ayuda al cuidado de algo")],
    worked=[
        W("Clasificar qué se comparte", "Testimonio inventado de doña Elena: «La receta de pan de la comunidad la enseñamos a todos. La canción de la cosecha solo se canta con permiso. El lugar de la quebrada lo cuidamos en silencio.» Clasifica los tres.", ["La receta se enseña a todos.", "La canción se canta con permiso.", "El lugar se cuida en silencio."], "Receta: se comparte. Canción: con permiso. Lugar: se cuida en silencio."),
        W("Preguntar antes de ayudar", "Quieres limpiar la quebrada de Ladera Verde. ¿Qué haces primero?", ["Pregunto qué cuidado necesita.", "Pregunto cómo puedo aportar.", "No actúo por mi cuenta."], "Pregunto a la comunidad qué cuidado necesita y cómo puedo aportar."),
    ],
    mistakes=[
        M("Publicar fotos de un lugar que la comunidad cuida en silencio.", "Puede dañar el cuidado que la comunidad decide.", "Pide autorización y respeta el límite."),
        M("Cuidar un patrimonio ajeno por mi cuenta, sin preguntar.", "Puedo hacerlo mal o faltar a normas.", "Pregunta qué ayuda se necesita."),
    ],
    R=[
        ex("Doña Elena (inventada): «La receta de pan la enseñamos a todos». ¿Se puede compartir la receta? Responde Sí o No.", "Sí", "La comunidad la enseña a todos."),
        ex("Doña Elena: «La canción de la cosecha solo se canta con permiso». ¿Qué se necesita para cantarla? A) permiso B) un micrófono", "A", "El testimonio lo dice."),
        ex("¿Qué patrimonio se cuida en silencio según el testimonio? A) el lugar de la quebrada B) la receta de pan", "A", "El testimonio lo dice."),
    ],
    C=[
        ex("Verdadero o falso: todo patrimonio se puede fotografiar y publicar.", "Falso", "Algunos requieren permiso o se cuidan en silencio."),
        ex("¿Qué significa cuidar en silencio? A) proteger algo sin mostrarlo B) olvidarlo", "A", "Es una forma de cuidado."),
        ex("Verdadero o falso: antes de ayudar a cuidar un patrimonio ajeno, pregunto qué ayuda se necesita.", "Verdadero", "Así se evita hacerlo mal."),
    ],
    A=[
        ex("Clasifica en SE COMPARTE, CON PERMISO o EN SILENCIO, según doña Elena: a) la receta de pan b) la canción de la cosecha c) el lugar de la quebrada.", "a se comparte, b con permiso, c en silencio", "Siguen lo que dice el testimonio."),
        ex("Don Camilo (inventado): «El sendero está abierto a los visitantes que avisan». ¿Qué debe hacer un visitante? A) avisar B) entrar sin avisar", "A", "El testimonio lo dice."),
        ex("Una niña toma una foto del lugar de la quebrada para su álbum. ¿Qué norma no respetó? A) el cuidado en silencio de la comunidad B) la receta de pan", "A", "El lugar se cuida sin mostrarlo."),
    ],
    Z=[
        ex("Esteban dice: «Si es de todos, puedo hacer lo que quiera con el patrimonio». ¿Qué error comete?", "Ignora los cuidados y permisos de la comunidad", "El patrimonio de una comunidad se cuida con ella."),
        ex("¿Por qué es mejor preguntar qué ayuda se necesita? A) porque la comunidad sabe cómo cuidar su patrimonio B) para perder tiempo", "A", "Ella conoce su cuidado."),
    ],
    D=[
        ex("Tres propuestas para ayudar en Isla Niebla (inventada): 1) preguntar al encargado de la caleta qué se necesita 2) entrar al bosque a limpiar sin avisar 3) filmar el sendero para internet sin permiso. ¿Cuál es adecuada?", "La primera", "Las otras ignoran permisos y cuidados."),
        ex("Un compañero quiere copiar un canto que escuchó en una fiesta y subirlo a internet. ¿Qué haces? A) le digo que pida permiso a quienes lo cantan B) lo ayudo", "A", "El canto es de la comunidad."),
    ],
    context=[ex("Tu escuela cuida un árbol muy querido del patio. Un grupo quiere podarlo por su cuenta. ¿Qué es mejor? A) preguntar a la persona encargada qué cuidado necesita B) podarlo ya", "A", "Primero se pregunta.")],
    selfcheck=[
        ex("Nombra las tres formas de compartir el patrimonio de un testimonio.", "Se comparte, con permiso y en silencio", "Están en la explicación."),
        ex("Verdadero o falso: puedo publicar fotos de un patrimonio sin pedir permiso.", "Falso", "Hace falta autorización."),
        ex("¿Qué haces primero para ayudar a cuidar un patrimonio ajeno? A) pregunto qué cuidado necesita B) actúo", "A", "Preguntar evita errores."),
    ],
    task=T("Lee este testimonio inventado de doña Marta, de Pampa Larga: «Los caminos de la llanura los cuidamos entre todos. La historia de las aves que marcaron los caminos solo la contamos en la comunidad. El pozo se puede visitar si se avisa.» Clasifica cada patrimonio en: se comparte, con permiso o se cuida en silencio. Escribe qué le preguntarías a doña Marta para ayudar a cuidar los caminos sin hacer nada por tu cuenta.",
           "Caminos: se cuidan entre todos (se comparte). Historia de las aves: se cuenta solo en la comunidad (en silencio). Pozo: se visita avisando (con permiso). Pregunta: ¿qué cuidado necesitan los caminos y cómo podemos ayudar desde la escuela?",
           ["clasifica los tres patrimonios", "formula una pregunta de ayuda", "respeta los límites"], ["clasificación de tres", "pregunta"], ["contar la historia reservada", "actuar sin preguntar"],
           "Pedir que muestre la frase del testimonio de cada clasificación."),
    reinforce="Haz tres tarjetas, «se comparte», «con permiso» y «en silencio», y reparte los patrimonios del testimonio.",
    extend="Escribe cómo pedirías permiso para fotografiar un patrimonio de tu barrio.",
)

L(
    OA15, 3, materials=MAT,
    use="Aprenderé a reconocer las relaciones entre el patrimonio, los riesgos que enfrenta y las acciones que ayudan a cuidarlo. Sirve para aportar al cuidado del patrimonio de mi comunidad.",
    prior=["Sé clasificar y leer testimonios de patrimonio.", "Sé que algunas cosas se cuidan en silencio."],
    explain=[
        "El patrimonio puede estar en riesgo cuando se deteriora, se olvida o se usa sin cuidado. Un patrimonio material puede dañarse por basura, mal uso o falta de mantención. Uno inmaterial puede olvidarse si las nuevas generaciones no lo conocen. Y uno natural puede afectarse si se toma más de lo que se recupera.",
        "Cada riesgo tiene acciones que ayudan. Para lo material: limpiar con apoyo de un adulto, mantener, no dañar. Para lo inmaterial: escuchar, aprender, preguntar a quienes lo guardan y enseñarlo con permiso. Para lo natural: no dejar basura, usar con moderación y respetar las normas de cuidado.",
        "Relacionamos tres elementos: el patrimonio, el riesgo y la acción de cuidado. Esa relación se anota con la fuente y, si es mi idea, con «puedo pensar que». Las acciones deben ser seguras, hechas con apoyo de un adulto y con permiso de quien cuida el lugar.",
    ],
    vocab=[("riesgo", "posibilidad de que algo se dañe"), ("deterioro", "daño que sufre algo con el tiempo o por mal uso"), ("mantención", "cuidado regular para que algo no se dañe"), ("moderación", "usar solo lo necesario"), ("acción de cuidado", "cosa que se hace para proteger un patrimonio")],
    worked=[
        W("Relacionar patrimonio, riesgo y acción", "Los niños de Ladera Verde (inventada) ya no conocen el relato de la Abuela Niebla. ¿Qué riesgo hay y qué acción ayuda?", ["El patrimonio es un relato inmaterial.", "El riesgo es que se olvide.", "La acción es escucharlo y aprenderlo con quienes lo guardan."], "Riesgo: el olvido. Acción: escucharlo y aprenderlo con permiso."),
        W("Una acción segura", "Hay basura en el sendero de Isla Niebla (inventada). ¿Qué acción es segura? A) recoger con guantes y un adulto, con permiso de la comunidad B) quemarla", ["La basura daña el sendero.", "Quemar es peligroso.", "Elijo la A."], "A"),
    ],
    mistakes=[
        M("Pensar que lo inmaterial no corre riesgos.", "Puede olvidarse si no se transmite.", "Aprende y pregunta a quienes lo guardan."),
        M("Proponer acciones peligrosas, como quemar basura.", "Pone en riesgo a las personas y el lugar.", "Elige acciones seguras con un adulto."),
    ],
    R=[
        ex("Si las nuevas generaciones no conocen un relato, ¿qué riesgo corre? A) que se olvide B) que se rompa", "A", "Es un patrimonio inmaterial."),
        ex("¿Qué es la mantención? A) cuidado regular para que algo no se dañe B) tirar algo", "A", "Evita el deterioro."),
        ex("¿Una acción de cuidado puede hacerse con apoyo de un adulto? Responde Sí o No.", "Sí", "Es una condición de seguridad."),
    ],
    C=[
        ex("Verdadero o falso: la basura puede dañar un patrimonio material y natural.", "Verdadero", "Ensucia y deteriora."),
        ex("Verdadero o falso: quemar la basura de un sendero es una acción de cuidado segura.", "Falso", "El fuego es peligroso."),
        ex("¿Qué ayuda a cuidar un patrimonio inmaterial? A) escuchar y aprender con quienes lo guardan B) ignorarlo", "A", "Se transmite aprendiendo."),
    ],
    A=[
        ex("Une cada riesgo con una acción: 1) un relato que se olvida 2) un camino con basura a) escuchar y aprender con permiso b) recoger la basura con guantes y un adulto", "1-a, 2-b", "Cada acción protege el patrimonio correspondiente."),
        ex("Clasifica en ACCIÓN SEGURA o NO SEGURA: a) limpiar la plaza con guantes y un adulto b) trepar a una pared antigua para pintarla.", "a segura, b no segura", "Trepar y pintar un patrimonio ajeno es riesgoso y dañino."),
        arith("Un curso de 28 estudiantes limpia el patio con apoyo de un adulto. Se forman grupos de 4. ¿Cuántos grupos hay?", "28//4", "Se reparten en grupos iguales."),
    ],
    Z=[
        ex("Olivia dice: «Si el patrimonio es de todos, cualquiera puede pintarlo». ¿Qué error comete?", "No respeta el cuidado y los permisos", "Pintar puede dañar."),
        ex("¿Por qué una acción de cuidado debe hacerse con permiso? A) porque quien cuida el lugar sabe qué se necesita B) para parecer ordenados", "A", "El cuidado se coordina."),
    ],
    D=[
        ex("Un testimonio inventado: «Los caminos de Pampa Larga se llenan de maleza si nadie los cuida». Tres propuestas: 1) arreglarlos con herramientas filosas solos 2) preguntar a la comunidad cómo ayudar sin herramientas peligrosas 3) ignorarlos. ¿Cuál es adecuada?", "La segunda", "Pregunta y evita riesgos."),
        ex("¿Qué acción ayuda a cuidar el relato de Ladera Verde? A) pedir a la comunidad que lo cuente y escucharlo con respeto B) cambiarlo", "A", "Escuchar con permiso ayuda a transmitirlo."),
    ],
    context=[ex("En tu escuela hay un mural antiguo que se está descascarando. ¿Qué haces? A) aviso a un adulto para que lo repare con quien corresponda B) lo pinto yo", "A", "Se pide ayuda a quien sabe repararlo.")],
    selfcheck=[
        ex("Nombra los tres elementos que relacionas en esta clase.", "Patrimonio, riesgo y acción de cuidado", "Están en la explicación."),
        ex("Verdadero o falso: las acciones de cuidado deben ser seguras.", "Verdadero", "La seguridad es obligatoria."),
        ex("¿Qué haces si no sabes cómo cuidar un patrimonio? A) pregunto a quien lo cuida B) lo toco", "A", "Preguntar es lo primero."),
    ],
    task=T("Lee: «Don Aurelio (inventado) cuenta que el sendero del bosque de Río Hondo se está llenando de basura y que las canciones del trabajo en la orilla ya no las canta casi nadie.» Haz una tabla: patrimonio, riesgo y acción de cuidado segura (con adulto y con permiso). Escribe una frase con «puedo pensar que…» sobre qué podría hacer tu curso.",
           "Sendero: material y natural; riesgo: basura; acción: recoger basura con guantes y un adulto, con permiso de la comunidad. Canciones: inmaterial; riesgo: olvido; acción: pedir que las enseñen y escucharlas con respeto. Puedo pensar que mi curso podría hacer una jornada de limpieza en la plaza con ayuda de un adulto.",
           ["relaciona patrimonio, riesgo y acción", "las acciones son seguras", "incluye una idea propia marcada"], ["tabla de dos filas", "frase"], ["proponer acciones peligrosas", "actuar sin permiso"],
           "Pedir que explique por qué cada acción es segura."),
    reinforce="Dibuja un patrimonio de tu escuela, el riesgo que corre y una acción de cuidado.",
    extend="Calcula: si 24 estudiantes se reparten en grupos de 6 para limpiar la plaza, ¿cuántos grupos son?",
)

L(
    OA15, 4, materials=MAT,
    use="Aprenderé a escribir un plan de cuidado atribuido del patrimonio de mi comunidad, con acciones seguras, permisos y límites. Sirve para aportar al cuidado de lo que heredamos.",
    prior=["Sé clasificar el patrimonio y reconocer riesgos.", "Sé proponer acciones seguras."],
    explain=[
        "Un plan de cuidado es un texto breve que dice qué patrimonio queremos cuidar, qué riesgo corre y qué acciones haremos para cuidarlo. Tiene cinco partes: el patrimonio y quién lo cuida; el riesgo, según la fuente; las acciones, que deben ser seguras y hechas con permiso; los pasos de quien las hará; y los límites.",
        "Cada acción debe responder tres preguntas. ¿Es segura? ¿Cuenta con el permiso de quien cuida el patrimonio? ¿Está bien coordinada con un adulto? Si alguna respuesta es no, se cambia la acción. Por ejemplo, limpiar una plaza con un adulto sí cumple; entrar sin avisar a un sendero no.",
        "El plan también reconoce a quienes cuidan hoy el patrimonio y declara lo que no corresponde divulgar. Termina con una pregunta para el educador o educadora tradicional o para la persona encargada, y con un compromiso concreto de devolver el plan para que lo revisen.",
    ],
    vocab=[("plan de cuidado", "texto que dice qué se cuidará y cómo"), ("coordinar", "ponerse de acuerdo para actuar juntos"), ("compromiso", "promesa de hacer algo concreto"), ("encargado", "persona responsable de cuidar un lugar"), ("paso", "cada parte de una acción, en orden")],
    worked=[
        W("Escribir un plan", "Patrimonio: el sendero de Isla Niebla (inventado), que cuidan los vecinos según don Camilo. Riesgo: basura, según don Camilo. Escribe un plan breve.", ["Patrimonio y quién lo cuida: sendero, los vecinos.", "Riesgo: basura.", "Acción: recoger con guantes y un adulto, con permiso."], "Sendero cuidado por los vecinos. Riesgo: basura. Acción: recoger con guantes y un adulto, con permiso de la comunidad. Pregunta: ¿cómo prefieren que ayudemos?"),
        W("Revisar una acción", "Propuesta: «Podar los árboles del bosque». ¿Es segura y con permiso?", ["Podar puede ser peligroso.", "No hay permiso mencionado.", "Hay que cambiarla."], "No: hay que cambiarla por una acción segura y con permiso."),
    ],
    mistakes=[
        M("Proponer acciones sin pedir permiso a quien cuida el patrimonio.", "Puede hacerse un daño.", "Pregunta y coordina."),
        M("No reconocer a quienes ya cuidan el patrimonio.", "Parece que nadie lo cuida.", "Nombra a la comunidad o persona encargada."),
    ],
    R=[
        ex("¿Cuántas partes tiene el plan de cuidado de esta clase? Escribe el número.", "5", "Patrimonio, riesgo, acciones, pasos y límites."),
        ex("¿Qué tres preguntas hace cada acción? A) segura, con permiso y coordinada con un adulto B) cara, grande y rápida", "A", "Son las condiciones de seguridad y respeto."),
        ex("¿Con qué cierra el plan? A) con una pregunta y un compromiso de devolución B) con un dibujo", "A", "Así se revisa con quien corresponde."),
    ],
    C=[
        ex("Verdadero o falso: una acción de cuidado sin permiso es adecuada si es rápida.", "Falso", "Debe tener permiso."),
        ex("Verdadero o falso: el plan reconoce a quienes ya cuidan el patrimonio.", "Verdadero", "Se nombra a la comunidad o persona encargada."),
        ex("¿Qué es coordinar una acción? A) ponerse de acuerdo con las personas involucradas B) hacer cada uno lo suyo", "A", "Es parte del plan."),
    ],
    A=[
        ex("Revisa: «Limpiar la plaza con guantes y con un adulto, con permiso del encargado». ¿Cumple las tres condiciones? Responde Sí o No.", "Sí", "Es segura, con permiso y con adulto."),
        ex("Revisa: «Pintar la pared de una sede antigua sin avisar». ¿Cumple? Responde Sí o No.", "No", "No tiene permiso y puede dañar."),
        ex("Clasifica en SEGURA o NO SEGURA: a) recoger basura con guantes y un adulto b) quemar ramas secas.", "a segura, b no segura", "El fuego es peligroso."),
    ],
    Z=[
        ex("Felipe dice que, si su plan es bueno, no necesita mostrarlo a la comunidad. ¿Qué error comete?", "Cree que no necesita revisión", "La comunidad conoce su patrimonio."),
        ex("¿Por qué conviene un compromiso concreto de devolución? A) para que la comunidad pueda revisar y corregir B) para quedar bien", "A", "Asegura la validación."),
    ],
    D=[
        ex("Dos planes para la quebrada de Ladera Verde. A: «Según doña Elena, se cuida con turnos; haremos un afiche con permiso». B: «Haremos una excursión sin avisar para sacar fotos». ¿Cuál es adecuado?", "A", "B ignora el permiso."),
        ex("Tu plan menciona un lugar que la comunidad cuida en silencio. ¿Qué haces? A) lo quito o lo dejo sin detalles B) agrego su ubicación", "A", "Se respeta el límite."),
    ],
    context=[ex("Tu curso quiere cuidar el humedal cercano a la escuela. ¿Qué debe hacer primero? A) preguntar al encargado o a la comunidad qué cuidados necesita B) entrar a limpiar con palas", "A", "Primero se pregunta.")],
    selfcheck=[
        ex("Nombra tres partes del plan de cuidado.", "Tres entre: patrimonio, riesgo, acciones, pasos, límites", "Están en la explicación."),
        ex("Verdadero o falso: una acción debe ser segura.", "Verdadero", "La seguridad es siempre obligatoria."),
        ex("¿Qué haces con un lugar que se cuida en silencio? A) lo dejo sin detalles B) lo muestro", "A", "El límite de la comunidad se respeta."),
    ],
    task=T("Usa este testimonio inventado de doña Elena, de Ladera Verde: «Las terrazas se desmoronan cuando llueve mucho. Las arreglamos entre todos con piedras que ya están allí. El lugar de la quebrada no se muestra.» Escribe un plan de cuidado de cinco partes. Incluye una acción segura que podría hacer tu curso desde la escuela (no la reparación de las terrazas) y una pregunta para el educador tradicional. No describas el lugar de la quebrada.",
           "Patrimonio: las terrazas, cuidadas por las familias. Riesgo: se desmoronan con mucha lluvia. Acción para mi curso: hacer un afiche de agradecimiento y un mapa de cuidados con permiso. Pasos: pedir permiso, hacer el afiche, mostrarlo a la comunidad. Límite: el lugar de la quebrada no se muestra. Pregunta: ¿qué ayuda necesitan las terrazas?",
           ["incluye las cinco partes", "acción segura y con permiso", "respeta el límite"], ["plan de cinco partes"], ["proponer reparar terrazas sin permiso", "describir el lugar reservado"],
           "Pedir que verifique las tres condiciones de la acción."),
    reinforce="Escribe las tres condiciones de una acción de cuidado en una tarjeta.",
    extend="Reescribe tu plan para un patrimonio de tu barrio.",
)

# ============================================================ OA 16 · Ser humano, naturaleza, cosmos y ciencia
OBS = ("Testimonio inventado de doña Marta, de Pampa Larga: «Mi abuelo miraba la Luna de noche para saber cuándo sembrar. Cuando la Luna estaba creciendo, sembraba lo que da fruto sobre la tierra. "
       "También miraba los pájaros y el viento. Esas observaciones las apuntábamos en la memoria de la familia.»")

L(
    OA16, 1, materials=MAT + " Observar el cielo de noche se hace con un adulto. Nunca se mira el Sol directamente.",
    use="Aprenderé a situar un saber que relaciona al ser humano, la naturaleza y el cosmos, y a reconocer que también es una forma de conocer. Sirve para valorar la mirada de los pueblos indígenas sobre el mundo.",
    prior=["Sé situar una fuente con su ficha.", "Sé que la visión de mundo es la manera en que un pueblo entiende la vida."],
    explain=[
        "El cosmos es todo lo que existe: la Tierra, el Sol, la Luna, las estrellas y el espacio. Muchos pueblos indígenas observan la naturaleza y el cosmos hace mucho tiempo y relacionan lo que ven con su vida: cuándo sembrar, cuándo pescar, cuándo cambiará el tiempo. Esas observaciones y conocimientos, transmitidos por generaciones, son una forma de ciencia desde su perspectiva.",
        "La perspectiva indígena entiende al ser humano como parte de la naturaleza y del cosmos, y no separado de ellos. La ciencia escolar también observa y explica la naturaleza, pero con otros métodos y lenguaje. Las dos miradas pueden dialogar, y ninguna debe despreciar a la otra.",
        "Para situar un saber de este tipo preguntamos: ¿quién lo cuenta?, ¿de qué comunidad?, ¿qué observa?, ¿para qué lo usa? y ¿qué no cuenta? Los saberes de un pueblo real los explica su comunidad. Aquí usamos testimonios inventados. Y por seguridad, el Sol nunca se mira directamente y la observación nocturna se hace con un adulto.",
    ],
    vocab=[("cosmos", "todo lo que existe: Tierra, Sol, Luna, estrellas y espacio"), ("observación", "mirar con atención para anotar lo que ocurre"), ("perspectiva", "manera de mirar algo"), ("ciencia escolar", "conocimientos que se enseñan en la escuela con métodos científicos"), ("transmitir", "pasar un conocimiento a otras personas")],
    worked=[
        W("Situar un saber de observación", OBS + " ¿Quién cuenta, qué observa y para qué lo usa?", ["Cuenta doña Marta, de Pampa Larga.", "Observa la Luna, los pájaros y el viento.", "Lo usa para saber cuándo sembrar."], "Doña Marta cuenta que su abuelo observaba la Luna, los pájaros y el viento para saber cuándo sembrar."),
        W("Dos miradas que dialogan", "Un niño dice: «Eso no es ciencia porque no está en el libro». ¿Qué corriges?", ["La observación repetida y transmitida es una forma de conocer.", "La ciencia escolar es otra manera de conocer.", "Ambas pueden dialogar."], "Corrijo: es otra forma de conocimiento; las dos miradas pueden dialogar."),
    ],
    mistakes=[
        M("Decir que el saber indígena «no es ciencia» sin conocerlo.", "Desprecia una forma de conocer transmitida por generaciones.", "Descríbelo con respeto y compáralo sin jerarquizar."),
        M("Mirar el Sol directamente para «observarlo».", "Daña los ojos.", "Nunca mires el Sol; observa con un adulto sus efectos, como las sombras."),
    ],
    R=[
        ex("Doña Marta (inventada) cuenta que su abuelo miraba la Luna de noche. ¿Para qué? A) para saber cuándo sembrar B) para jugar", "A", "El testimonio lo dice."),
        ex("¿Qué es el cosmos? A) todo lo que existe: Tierra, Sol, Luna, estrellas y espacio B) solo la Luna", "A", "Es la definición de la clase."),
        ex("¿Se puede mirar el Sol directamente para observarlo? Responde Sí o No.", "No", "Daña los ojos."),
    ],
    C=[
        ex("Verdadero o falso: la observación de la naturaleza transmitida por generaciones es una forma de conocimiento.", "Verdadero", "Es una forma de ciencia desde su perspectiva."),
        ex("Verdadero o falso: la ciencia escolar y la mirada indígena pueden dialogar.", "Verdadero", "Ninguna desprecia a la otra."),
        ex("¿Qué entiende la perspectiva indígena del ser humano? A) que es parte de la naturaleza y del cosmos B) que está separado de ellos", "A", "Es su forma de relacionarse con el mundo."),
    ],
    A=[
        ex("Clasifica en OBSERVACIÓN o USO: a) mirar la Luna de noche b) decidir cuándo sembrar.", "a observación, b uso", "Mirar es observar; decidir es usar lo observado."),
        ex("Don Camilo (inventado): «Miramos el color del cielo al amanecer para saber si saldrán los botes». ¿Qué observa? A) el color del cielo B) las olas del mar", "A", "El testimonio lo dice."),
        ex("Una ficha nombra el saber, pero no dice quién lo cuenta ni con qué permiso. ¿Puedes usarla? Responde Sí o No.", "No", "Falta la fuente y el permiso."),
    ],
    Z=[
        ex("Julieta dice: «Si no se explica con fórmulas, no sirve». ¿Qué error comete?", "Desprecia otra forma de conocer", "Los saberes también orientan decisiones."),
        ex("¿Por qué la observación nocturna se hace con un adulto? A) por seguridad B) para que no se vea", "A", "Se cuida a los estudiantes."),
    ],
    D=[
        ex("Dos frases sobre el testimonio de doña Marta. 1) «El abuelo miraba la Luna para saber cuándo sembrar». 2) «La Luna manda sobre las plantas». ¿Cuál se queda en la fuente?", "La primera", "La segunda es una interpretación no dicha."),
        ex("Quieres explicar «por qué» miraba la Luna el abuelo, pero el testimonio no lo explica. ¿Qué haces? A) escribo que no lo dice B) invento la razón", "A", "No se inventan razones."),
    ],
    context=[ex("Tu curso hará una noche de observación del cielo en la escuela con familias. ¿Qué es esencial? A) hacerlo con adultos responsables y sin mirar el Sol B) dejar a cada estudiante solo", "A", "La seguridad es lo primero.")],
    selfcheck=[
        ex("Explica con tus palabras qué es el cosmos.", "Todo lo que existe: Tierra, Sol, Luna, estrellas y espacio", "Es la definición de la clase."),
        ex("Verdadero o falso: nunca se mira el Sol directamente.", "Verdadero", "Daña los ojos."),
        ex("¿Quién explica los saberes de un pueblo real? A) su comunidad B) cualquiera", "A", "Ella es la fuente."),
    ],
    task=T("Lee este testimonio inventado de don Aurelio, de Río Hondo: «Mi madre miraba el color del cielo al atardecer y el vuelo de las aves para saber si vendría lluvia. Nos enseñó a mirar con paciencia. Hay señales que solo contamos a la familia.» Haz una ficha con: comunidad, fuente, qué se observa, para qué se usa, qué no se cuenta y una frase con «yo pienso que…» sobre cómo la ciencia escolar podría dialogar con esta forma de observar.",
           "Comunidad: Río Hondo. Fuente: don Aurelio. Se observa: el color del cielo y el vuelo de las aves. Se usa para saber si vendrá lluvia. No se cuenta: algunas señales de la familia. Yo pienso que la ciencia escolar podría dialogar midiendo la lluvia y comparando con lo que se observó.",
           ["completa la ficha con datos del testimonio", "respeta lo no contado", "propone un diálogo sin jerarquizar"], ["ficha completa", "frase"], ["inventar señales", "decir que no es ciencia"],
           "Pedir que muestre la frase del testimonio de cada campo."),
    reinforce="Dibuja lo que observa el testimonio de don Aurelio y para qué se usa, con una flecha.",
    extend="Escribe una pregunta para el educador tradicional sobre cómo su comunidad observa el cielo o la naturaleza.",
)

L(
    OA16, 2, materials=MAT + " Las observaciones nocturnas se hacen con un adulto. Nunca se mira el Sol directamente.",
    use="Aprenderé a leer un saber de observación con límites: qué se observa, qué dice la comunidad y qué no se cuenta. Sirve para valorar la relación entre las personas, la naturaleza y el cosmos sin mezclar datos.",
    prior=["Sé situar un saber de observación.", "Sé separar fuente e interpretación."],
    explain=[
        "En un testimonio sobre naturaleza y cosmos separamos tres cosas. Lo que se observa: hechos que se pueden ver, como la forma de la Luna, el color del cielo o el vuelo de las aves. La explicación de la comunidad: lo que la comunidad dice que significa. Y lo que no se cuenta: lo que se reserva.",
        "No mezclamos ni corregimos la explicación de la comunidad con la ciencia escolar. Podemos anotar una observación escolar al lado, como que la Luna tarda unos 30 días en completar sus fases, pero sin decir que una explicación es «falsa». Son dos maneras de conocer que pueden aportar la una a la otra.",
        "Mi interpretación se marca con «yo pienso que». Lo que la comunidad guarda sobre el cosmos, como una explicación espiritual, no se pregunta con insistencia ni se inventa. Si queremos saber más, preguntamos al educador o educadora tradicional.",
    ],
    vocab=[("fases de la Luna", "formas que vemos de la Luna: nueva, creciente, llena y menguante"), ("hecho observable", "algo que se puede ver o medir"), ("explicación de la comunidad", "lo que la comunidad dice que algo significa"), ("ciclo", "serie de cambios que se repite"), ("dialogar", "intercambiar miradas con respeto")],
    worked=[
        W("Separar tres cosas", OBS + " Separa lo que se observa, la explicación y lo no contado.", ["Se observa: la Luna creciendo, los pájaros y el viento.", "La explicación: lo usa para decidir cuándo sembrar.", "No se cuenta: por qué esa Luna sirve para ese cultivo."], "Se observa la Luna, los pájaros y el viento; se usa para decidir la siembra; no se cuenta el porqué."),
        W("Un ciclo con una cuenta", "La Luna tarda unos 30 días en completar sus fases. ¿Cuántos ciclos completos hay en 90 días?", ["Un ciclo dura 30 días.", "Hay 90 días.", "Divido 90 ÷ 30."], "3 ciclos."),
    ],
    mistakes=[
        M("Decir que la explicación de la comunidad es falsa porque la ciencia escolar dice otra cosa.", "Son dos maneras distintas de conocer.", "Anota ambas sin jerarquizar."),
        M("Agregar una explicación espiritual que la comunidad no contó.", "Se inventa su visión del cosmos.", "Escribe «no se cuenta»."),
    ],
    R=[
        ex("Doña Marta (inventada) dice que su abuelo miraba los pájaros y el viento. ¿Qué observaba además de la Luna?", "Los pájaros y el viento", "El testimonio lo dice."),
        ex("¿Cuántos días tarda la Luna, aproximadamente, en completar sus fases? A) unos 30 B) unos 3", "A", "Alrededor de 30 días."),
        ex("La comunidad no cuenta por qué esa Luna sirve para ese cultivo. ¿Lo inventas? Responde Sí o No.", "No", "Lo no contado se respeta."),
    ],
    C=[
        ex("Verdadero o falso: la explicación de una comunidad se corrige con la ciencia escolar.", "Falso", "Son maneras distintas de conocer."),
        ex("¿Qué es un hecho observable? A) algo que se puede ver o medir B) una creencia", "A", "Se puede comprobar mirando."),
        ex("Verdadero o falso: las dos miradas pueden aportarse una a la otra.", "Verdadero", "Dialogan sin jerarquía."),
    ],
    A=[
        arith("Un ciclo de la Luna dura unos 30 días. ¿Cuántos ciclos completos hay en 120 días?", "120//30", "Se divide el total entre la duración de un ciclo."),
        ex("Clasifica en HECHO OBSERVABLE o EXPLICACIÓN DE LA COMUNIDAD: a) la Luna está creciendo b) según la comunidad, es buen momento para sembrar.", "a hecho observable, b explicación de la comunidad", "La primera se ve; la segunda es lo que la comunidad dice."),
        ex("Don Camilo (inventado) dice: «Hay señales del cielo que no contamos». ¿Qué escribes en tu trabajo sobre esas señales? A) que no se cuentan B) las que creo que son", "A", "Lo reservado se respeta."),
    ],
    Z=[
        ex("Paula escribe: «La explicación de la comunidad sobre la Luna es un error». ¿Qué problema tiene?", "Jerarquiza y desprecia otra forma de conocer", "No hay base para decirlo."),
        ex("¿Por qué anotar el dato escolar «unos 30 días» al lado, sin corregir? A) para que las dos miradas dialoguen B) para decir quién gana", "A", "Es diálogo y no competencia."),
    ],
    D=[
        arith("Si observas la Luna durante 3 ciclos de unos 30 días cada uno y anotas un dato cada 10 días, ¿cuántos datos anotas en total?", "(3*30)//10", "Primero los días: 3 × 30 = 90; luego, un dato cada 10 días."),
        ex("Tres frases sobre el testimonio de doña Marta. 1) El abuelo miraba la Luna. 2) La Luna crecía y sembraba. 3) La Luna es una diosa. ¿Cuál no está en el testimonio?", "La tercera", "El testimonio no habla de una diosa."),
    ],
    context=[ex("En una noche de observación con familias, un niño quiere apuntar su linterna al Sol al amanecer. ¿Qué haces? A) le explico que nunca se mira el Sol directamente B) lo dejo", "A", "Se evita un daño a los ojos.")],
    selfcheck=[
        ex("Nombra las tres cosas que separas al leer un saber de observación.", "Lo que se observa, la explicación de la comunidad y lo que no se cuenta", "Están en la explicación."),
        ex("Verdadero o falso: puedo marcar mi idea con «yo pienso que».", "Verdadero", "Así no se confunde con la fuente."),
        ex("¿Cuántas fases principales nombra la clase para la Luna? Escribe el número.", "4", "Nueva, creciente, llena y menguante."),
    ],
    task=T("Lee este testimonio inventado de don Camilo, de Isla Niebla: «Miramos las estrellas del atardecer para saber si el mar estará tranquilo. Mi padre me enseñó a mirar. Hay conocimientos del cielo que solo contamos en la comunidad.» Haz tres columnas: lo que se observa, la explicación de la comunidad y lo que no se cuenta. Agrega un dato de la ciencia escolar (por ejemplo, la Luna y sus 30 días) sin decir que corrige al testimonio, y calcula cuántos ciclos de 30 días hay en 60 días.",
           "Se observa: las estrellas del atardecer. Explicación de la comunidad: sirven para saber si el mar estará tranquilo. No se cuenta: otros conocimientos del cielo. Dato escolar: la Luna tarda unos 30 días en completar sus fases; en 60 días hay 2 ciclos. Son miradas distintas que pueden dialogar.",
           ["tres columnas con datos del testimonio", "dato escolar sin corregir", "cuenta correcta"], ["tabla de tres columnas", "cuenta"], ["decir que el testimonio es falso", "inventar conocimientos"],
           "Pedir que explique cómo evitó jerarquizar."),
    reinforce="Dibuja las cuatro fases de la Luna que nombra la clase y escribe su nombre bajo cada una.",
    extend="Escribe una pregunta para el educador tradicional sobre cómo su comunidad observa el cielo.",
)

L(
    OA16, 3, materials=MAT,
    use="Aprenderé a reconocer relaciones entre el ser humano, la naturaleza y el cosmos en dos comunidades, y entre su perspectiva y la ciencia escolar. Sirve para valorar cómo se unen la vida, la naturaleza y el conocimiento.",
    prior=["Sé leer un saber de observación con límites.", "Sé comparar sin jerarquizar."],
    explain=[
        "En muchos pueblos indígenas, el ser humano, la naturaleza y el cosmos forman una red de relaciones: lo que se hace en la tierra se relaciona con lo que ocurre en el cielo y con el cuidado del mundo. Esa idea está en las fuentes de cada pueblo, que son las que la explican. Aquí la estudiamos con testimonios inventados.",
        "Para encontrar relaciones usamos tres preguntas. ¿Qué se observa en la naturaleza o en el cielo? ¿Qué decisión de la vida humana se relaciona con eso? ¿Qué cuidado muestra la comunidad hacia la naturaleza? Las respuestas muestran cómo se unen las personas, la naturaleza y el cosmos.",
        "Luego miramos cómo esa perspectiva puede dialogar con la ciencia escolar. Por ejemplo, la ciencia escolar mide la lluvia con un instrumento y registra las estaciones del año; la comunidad observa el cielo y las aves. Pueden compartir registros, pero cada una conserva su manera de conocer. No decimos cuál es mejor.",
    ],
    vocab=[("red de relaciones", "conjunto de conexiones entre personas, naturaleza y cosmos"), ("decisión", "elección que una persona o comunidad hace"), ("registro", "anotación de lo observado"), ("estación del año", "cada una de las cuatro partes del año: verano, otoño, invierno y primavera"), ("instrumento", "objeto para medir")],
    worked=[
        W("Aplicar las tres preguntas", "Doña Marta (inventada): «Miramos la Luna para saber cuándo sembrar y damos gracias a la tierra antes de sembrar». Responde las tres preguntas.", ["Se observa: la Luna.", "Decisión: cuándo sembrar.", "Cuidado: dar gracias a la tierra."], "Observa la Luna; decide cuándo sembrar; cuida la tierra dando gracias."),
        W("Dialogar sin jerarquizar", "La escuela mide la lluvia con un vaso graduado; la comunidad observa el vuelo de las aves. ¿Cómo pueden dialogar?", ["Cada una usa su manera de observar.", "Pueden comparar sus registros.", "Ninguna reemplaza a la otra."], "Comparan sus registros sin decir que una reemplaza a la otra."),
    ],
    mistakes=[
        M("Decir que la ciencia escolar «confirma» o «niega» el saber indígena.", "Son maneras distintas de conocer.", "Dialoga y compara registros."),
        M("Afirmar que todos los pueblos relacionan igual a las personas con el cosmos.", "Cada pueblo tiene su perspectiva.", "Habla de la comunidad de la fuente."),
    ],
    R=[
        ex("Doña Marta (inventada) da gracias a la tierra antes de sembrar. ¿Qué cuidado muestra?", "Dar gracias a la tierra", "El testimonio lo dice."),
        ex("¿Qué es una estación del año? A) cada una de las cuatro partes del año B) una parada de tren", "A", "Son verano, otoño, invierno y primavera."),
        ex("¿Qué instrumento mide la lluvia en la escuela? A) un vaso graduado B) una cuerda", "A", "El vaso graduado mide cantidad de agua."),
    ],
    C=[
        ex("Verdadero o falso: la ciencia escolar y la perspectiva indígena pueden compartir registros.", "Verdadero", "El diálogo es posible."),
        ex("Verdadero o falso: la ciencia escolar «confirma» o «niega» el saber de una comunidad.", "Falso", "Son maneras distintas de conocer."),
        ex("¿Qué es una red de relaciones? A) conexiones entre personas, naturaleza y cosmos B) una malla de pesca", "A", "Así se entiende en la clase."),
    ],
    A=[
        ex("Clasifica en OBSERVACIÓN, DECISIÓN o CUIDADO, según el testimonio de doña Marta: a) mirar la Luna b) elegir cuándo sembrar c) dar gracias a la tierra.", "a observación, b decisión, c cuidado", "Corresponde a las tres preguntas de la clase."),
        arith("La escuela registra la lluvia cada día durante 4 semanas. ¿Cuántos días son? Una semana tiene 7 días.", "4*7", "Se multiplican las semanas por los días de cada una."),
        ex("Don Camilo (inventado): «Miramos el cielo para saber si saldrán los botes». ¿Qué decisión se relaciona con lo que se observa? A) salir o no a pescar B) construir una casa", "A", "El testimonio lo dice."),
    ],
    Z=[
        ex("Ricardo dice: «Si la escuela mide la lluvia, ya no hace falta mirar el cielo como lo hace la comunidad». ¿Qué error comete?", "Cree que una forma reemplaza a la otra", "Cada una conserva su manera de conocer."),
        ex("¿Por qué conviene hablar de la comunidad de la fuente y no de todos los pueblos? A) porque cada pueblo tiene su perspectiva B) porque es más corto", "A", "Hay muchas perspectivas."),
    ],
    D=[
        ex("Un cuadro con dos columnas: «Comunidad (Pampa Larga): observa la Luna y los pájaros» y «Escuela: registra la lluvia con un vaso graduado». Una afirmación correcta es… A) ambos observan la naturaleza para entenderla B) la escuela observa mejor", "A", "No se jerarquiza."),
        ex("Quieres comparar con el saber del pueblo que corresponde a tu escuela. ¿Qué necesitas? A) un testimonio del educador tradicional B) una suposición", "A", "La fuente es el educador o la comunidad."),
    ],
    context=[ex("Tu curso quiere registrar el clima de 30 días en el patio. Un compañero propone preguntar también a una persona mayor del barrio cómo mira el cielo. ¿Es una buena idea? Responde Sí o No.", "Sí", "Permite dialogar entre dos maneras de observar, con respeto.")],
    selfcheck=[
        ex("Nombra las tres preguntas para encontrar relaciones.", "Qué se observa, qué decisión se relaciona y qué cuidado muestra", "Están en la explicación."),
        ex("Verdadero o falso: no digo cuál manera de conocer es mejor.", "Verdadero", "Se dialoga sin jerarquizar."),
        ex("¿Qué es un registro? Escribe una frase corta.", "Una anotación de lo observado", "Es la definición de la clase."),
    ],
    task=T("Lee: «Doña Elena (inventada) cuenta que, antes de sembrar, la comunidad mira cuántas aves llegan a la quebrada y cuánta agua baja. La escuela anota cada día cuánta lluvia cae en un vaso graduado, durante 4 semanas.» Haz una tabla de tres columnas: qué se observa, qué decisión se relaciona y qué cuidado. Calcula cuántos días registra la escuela (4 semanas de 7 días). Escribe una frase con «yo pienso que…» sobre cómo podrían compartir sus registros.",
           "Comunidad: observa aves y agua; decide cuándo sembrar; cuida la quebrada. Escuela: anota la lluvia; el texto no dice qué decisión toma. Días: 4 × 7 = 28. Yo pienso que podrían comparar cuántas aves llegan los días de más lluvia.",
           ["tabla con tres columnas", "cuenta correcta", "idea de diálogo sin jerarquizar"], ["tabla", "cuenta", "frase"], ["decir cuál es mejor", "inventar rituales"],
           "Pedir que muestre la cuenta y la frase del testimonio."),
    reinforce="Une con flechas lo que observa la comunidad con lo que observa la escuela.",
    extend="Propón un registro que tu curso pueda llevar durante una semana, con un adulto, sobre el cielo o el clima.",
)

L(
    OA16, 4, materials=MAT + " Las observaciones nocturnas se hacen con un adulto. Nunca se mira el Sol directamente.",
    use="Aprenderé a escribir una valoración atribuida de la relación entre el ser humano, la naturaleza y el cosmos, vinculada con la ciencia, desde la perspectiva de una comunidad. Sirve para valorar estos saberes con respeto.",
    prior=["Sé relacionar observación, decisión y cuidado.", "Sé atribuir y marcar mis ideas."],
    explain=[
        "Una valoración atribuida de un saber de naturaleza y cosmos tiene cinco partes. Primero, la ficha: comunidad, fuente y permiso. Segundo, qué observa la comunidad y para qué lo usa. Tercero, qué cuidado muestra hacia la naturaleza. Cuarto, una relación con la ciencia escolar, marcada como idea mía. Quinto, los límites y una pregunta.",
        "La relación con la ciencia escolar debe ser un diálogo. Por ejemplo: «La comunidad observa a las aves; la escuela puede registrar cuántas aves llegan cada día y compartir el registro con la comunidad». No decimos que la ciencia escolar «demuestra» el saber, ni que el saber «supera» a la ciencia.",
        "También valoramos la relación entre las personas y el cosmos sin inventar creencias. Si la comunidad dice que algo es sagrado, lo escribimos como lo dijo ella. Si no lo dice, no lo añadimos. Cerramos mostrando el trabajo a la comunidad o al educador tradicional.",
    ],
    vocab=[("valoración", "texto que reconoce la importancia de algo"), ("diálogo", "intercambio respetuoso entre dos miradas"), ("demostrar", "probar que algo es cierto"), ("creencia", "idea que una persona o comunidad considera verdadera"), ("cerrar", "terminar un trabajo con revisión")],
    worked=[
        W("Escribir una valoración", OBS + " Escribe una valoración breve.", ["Ficha: doña Marta, Pampa Larga, con permiso.", "Observa la Luna, los pájaros y el viento para sembrar.", "Relación con la escuela: yo pienso que podríamos anotar las fases de la Luna y compararlas con el huerto."], "Según doña Marta, de Pampa Larga (inventada), su abuelo observaba la Luna, los pájaros y el viento para saber cuándo sembrar. Yo pienso que la escuela podría anotar las fases de la Luna y compararlas con el huerto. No sé por qué esa Luna sirve para ese cultivo."),
        W("Cuidar las palabras", "Un niño escribe: «La ciencia demuestra que el abuelo tenía razón». ¿Qué corriges?", ["«Demuestra» jerarquiza.", "La ciencia no necesita confirmar el saber de la comunidad.", "Cambio a «dialoga»."], "Corrijo: «La ciencia escolar puede dialogar con el saber de la comunidad»."),
    ],
    mistakes=[
        M("Escribir que la ciencia demuestra o desmiente el saber de una comunidad.", "Son maneras distintas de conocer.", "Habla de diálogo."),
        M("Inventar una creencia sobre el cosmos que la comunidad no contó.", "Falta al respeto.", "Escribe «no se cuenta»."),
    ],
    R=[
        ex("¿Cuántas partes tiene la valoración de esta clase? Escribe el número.", "5", "Ficha, observación, cuidado, relación con la ciencia y límites."),
        ex("¿Qué palabra usas para hablar de la ciencia escolar y el saber de la comunidad? A) diálogo B) competencia", "A", "No se jerarquiza."),
        ex("¿Qué haces con el trabajo terminado? A) lo muestro a la comunidad o al educador B) lo guardo", "A", "Es la revisión."),
    ],
    C=[
        ex("Verdadero o falso: puedo escribir que la ciencia demuestra que la comunidad tiene razón.", "Falso", "Eso jerarquiza dos maneras de conocer."),
        ex("Verdadero o falso: la relación con la ciencia escolar se marca como idea mía.", "Verdadero", "Así no se atribuye a la comunidad."),
        ex("¿Qué haces si la comunidad no cuenta una creencia sobre el cosmos? A) escribo que no se cuenta B) invento una", "A", "Lo no contado se respeta."),
    ],
    A=[
        ex("Ordena: A) límites B) ficha C) relación con la ciencia D) observación. ¿Cuál va primero?", "B", "Se empieza con la ficha."),
        ex("Clasifica en DATO DE LA FUENTE o MI IDEA: a) según doña Marta, su abuelo miraba la Luna b) yo pienso que podríamos anotar las fases de la Luna en el huerto.", "a dato de la fuente, b mi idea", "La primera está escrita; la segunda es mía."),
        ex("El testimonio de doña Marta no explica por qué esa fase de la Luna sirve para sembrar. ¿Cuál es un límite bien escrito? A) El testimonio no explica por qué esa fase sirve para sembrar B) Seguro que la Luna atrae el agua de la tierra", "A", "El límite declara lo que la fuente no cuenta."),
    ],
    Z=[
        ex("Camilo escribe: «El conocimiento de la comunidad supera a la ciencia escolar». ¿Qué error comete?", "Jerarquiza dos maneras de conocer", "No se ordenan."),
        ex("¿Por qué marcar la relación con la ciencia escolar como idea propia? A) porque la comunidad no la dijo B) porque es corta", "A", "No debe atribuirse a la fuente."),
    ],
    D=[
        ex("Dos valoraciones. A: «Según don Camilo (inventado), miran el cielo para saber si saldrán los botes; yo pienso que la escuela podría registrar el viento». B: «Miran el cielo porque creen en espíritus del mar». ¿Cuál respeta la fuente?", "A", "B inventa una creencia."),
        ex("Tu valoración menciona una señal que la comunidad reserva. ¿Qué haces? A) la quito B) la dejo", "A", "Se respeta el límite."),
    ],
    context=[ex("En el acto de ciencias de la escuela, alguien propone mostrar el saber de una comunidad inventada junto a un experimento escolar. ¿Qué cartel es mejor? A) «Dos maneras de observar la naturaleza» B) «Ciencia verdadera contra creencias»", "A", "Dialoga sin jerarquizar.")],
    selfcheck=[
        ex("Nombra tres partes de la valoración.", "Tres entre: ficha, observación, cuidado, relación con la ciencia, límites", "Están en la explicación."),
        ex("Verdadero o falso: puedo decir que la ciencia demuestra el saber de la comunidad.", "Falso", "No se jerarquiza."),
        ex("¿Qué haces con la pregunta final? A) la llevo al educador tradicional B) la olvido", "A", "Él o ella es la fuente."),
    ],
    task=T("Usa este testimonio inventado de doña Elena, de Ladera Verde: «Antes de sembrar, miramos cuántas aves llegan a la quebrada y cuánta agua baja. Damos gracias a la tierra. Hay señales de las estrellas que no contamos.» Escribe una valoración de cinco partes: ficha, qué observa y para qué, qué cuidado muestra, una relación con la ciencia escolar (con «yo pienso que») y límites con una pregunta. No inventes las señales de las estrellas.",
           "Ficha: doña Elena, de Ladera Verde (inventada), con permiso. Observa las aves y el agua de la quebrada para decidir cuándo sembrar. Cuidado: da gracias a la tierra. Yo pienso que la escuela podría anotar cuánta agua cae en su huerto y compararlo. Límite: las señales de las estrellas no se cuentan. Pregunta: ¿cómo observa nuestra comunidad el cielo?",
           ["incluye las cinco partes", "dialoga con la ciencia escolar sin jerarquizar", "respeta las señales no contadas"], ["valoración de cinco partes"], ["inventar las señales", "decir que la ciencia demuestra"],
           "Pedir que señale la frase del testimonio de cada parte."),
    reinforce="Numera las cinco partes de tu valoración para comprobar que están todas.",
    extend="Escribe cómo mostrarías tu valoración a la comunidad para que la revise.",
)
