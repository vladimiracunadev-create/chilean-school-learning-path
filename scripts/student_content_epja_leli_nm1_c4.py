"""Lengua y Literatura EPJA Media Nivel 1, módulo 3: OAD-12, evaluar su texto y reescribirlo aplicando criterios de coherencia y cohesión textual para comunicarlo. Todos los borradores son inventados; todo se resuelve en papel."""
from __future__ import annotations

from epja_leli_nm1_c_common import build

O = "EPJA-LELI-NM1-OAD-12"

F1 = ("Borrador (inventado) de un mensaje de una persona que trabaja a su jefatura: «Hola necesito permiso el viernes porque tengo que hacer un trámite y no puedo ir el viernes "
      "y también necesito saber si me pagan el día gracias».")

F2 = ("Pauta de revisión (inventada): 1) propósito claro; 2) ideas ordenadas; 3) sin contradicciones; 4) conectores y reemplazos que unen; 5) sin repeticiones innecesarias; 6) puntuación y ortografía. "
      "Borrador (inventado) de un aviso a los vecinos: «La reunión es el jueves. Hay que traer la cédula. La reunión es a las 19 horas. No hay que traer nada. Se tratará el tema del agua. La reunión es en la sede.»")

F3 = ("Informe (inventado) de una persona que trabaja en una bodega, sobre un día de trabajo: «Ayer en la bodega recibimos los pedidos. Los pedidos llegaron tarde. Entonces ordenamos la mercadería. "
      "La mercadería estaba mal ordenada. Los pedidos se revisaron. Terminamos a las 18 horas. Los clientes estaban contentos porque el camión llegó temprano.»")

F4 = ("Oraciones para reescribir (inventadas): 1) «Rosa trabaja en una peluquería y Rosa quiere abrir su propia peluquería». "
      "2) «Llegué tarde al control porque el bus se demoró no alcancé a comprar el pase». "
      "3) «El taller reparó el refrigerador, sin embargo quedó funcionando bien». "
      "4) «Primero cocinamos, luego primero ordenamos la cocina». "
      "5) «Los vecinos propusieron limpiar la plaza. Los vecinos pidieron bolsas a la junta de vecinos».")

F5 = ("Carta (inventada) de una persona del barrio a la municipalidad: «Estimados: les escribo por la luminaria de mi calle. La luminaria no funciona. Hace un mes que la luminaria no funciona. "
      "Es peligroso para los vecinos porque no se ve nada de noche. Pido que la arreglen. Además la luminaria de la esquina funciona bien. Atentamente, Carmen (nombre de ejemplo)».")

F6 = ("Pauta final (inventada): 1) propósito y audiencia claros; 2) ideas ordenadas y sin contradicciones; 3) conectores y reemplazos; 4) sin repeticiones; 5) puntuación y ortografía; 6) título y cierre; 7) fuentes citadas. "
      "Versión 1, para el diario mural: título «La feria que reúne a la plaza». Texto: «La feria vecinal de la plaza funciona los domingos con 15 puestos. Nació en 2021 con ocho puestos (registro de la feria). "
      "Con el tiempo, creció de 8 a 15 puestos. Hoy los vecinos compran verduras y pan sin ir lejos.» "
      "Versión 2, para un mensaje breve a la junta de vecinos: «Feria vecinal: domingos, en la plaza, 15 puestos. Verduras y pan. Nació en 2021.»")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy parto de lo que ya hago, releer un mensaje antes de enviarlo, y lo aplico para evaluar mis textos: claridad, orden, tono y puntuación.",
    prior=["Escribo mensajes y notas en mi vida diaria.", "Sé qué es un conector.", "Reconozco una repetición."],
    explain=[
        "Tú ya relees tus mensajes importantes antes de enviarlos: miras si se entienden, si el tono es adecuado y si no faltó nada. Evaluar tu propio texto es eso mismo, pero con criterios claros.",
        "Se evalúa pensando en el propósito (qué quieres lograr) y en la persona que lo leerá. Pregúntate: ¿se entiende?, ¿van las ideas en orden?, ¿se repite algo?, ¿el tono es adecuado?, ¿la puntuación ayuda a leer?",
        "Después de evaluar, se reescribe: se cambia lo que no funciona sin cambiar lo que quieres decir. Un texto puede escribirse varias veces; mejorarlo no es señal de error, sino parte normal de escribir.",
    ],
    vocab=[("evaluar un texto", "revisar si cumple su propósito con criterios claros"), ("reescribir", "volver a escribir un texto para mejorarlo"), ("tono", "manera de hablar adecuada a quien recibe el mensaje"), ("puntuación", "signos como punto y coma que ayudan a leer")],
    worked=[
        ("Evaluar el tono", "Mensaje a una jefatura que comienza con «Oye, necesito el día» (ejemplo).", ["La jefatura merece un saludo completo.", "Falta cortesía al pedir."], "Cambiar por «Buenos días. Quisiera solicitar…»"),
        ("Detectar una repetición", "Frase: «Pido hora el martes porque el martes tengo libre» (ejemplo).", ["La palabra «martes» se repite sin necesidad.", "Una vez basta."], "Se reescribe: «Pido hora el martes porque tengo libre»"),
    ],
    mistakes=[("Enviar un mensaje importante sin releerlo.", "Pueden quedar repeticiones, faltas de cortesía o ideas confusas.", "Léelo completo pensando en quien lo recibirá."),
              ("Revisar solo las tildes.", "El texto puede seguir siendo confuso o poco adecuado.", "Revisa también orden, repeticiones, tono y puntuación.")],
    T=[
        ("abc", "Antes de enviar un mensaje importante, ¿qué conviene hacer?", "Releerlo pensando en quien lo recibirá y corregir lo que confunda", "Enviarlo de inmediato para no perder tiempo", "Cambiarle la letra para que se vea distinto", "Releer con la persona destinataria en mente evita malentendidos."),
        ("ab", "{F} ¿Cuál es el propósito del mensaje?", "Pedir permiso para el viernes y consultar por el pago de ese día", "Agradecer a la jefatura por el sueldo", "El mensaje pide permiso y pregunta por el pago del día."),
        ("{F} ¿Para qué día se pide el permiso? Escribe solo el día.", "viernes", "El mensaje pide permiso para el viernes."),
        ("abc", "{F} ¿Qué problema tiene la repetición de «el viernes»?", "Repite lo mismo innecesariamente y alarga el mensaje", "Falta el nombre de la jefatura", "Es demasiado formal", "Decir dos veces el día no agrega información."),
        ("abc", "{F} ¿Qué falta al comienzo del mensaje para un tono adecuado a una jefatura?", "Un saludo completo, como «Buenos días»", "Un signo de exclamación", "Un apodo cariñoso", "Una jefatura merece un saludo cortés y completo."),
        ("ab", "{F} ¿Qué pregunta formal conviene para saber si pagan el día?", "«¿Podría informarme si ese día se descuenta del sueldo?»", "«¿Me pagan o no me pagan, ah?»", "La pregunta formal es respetuosa y clara."),
        ("abc", "{F} ¿Qué versión corrige mejor la puntuación y la claridad?", "«Buenos días. Quisiera solicitar permiso el viernes para realizar un trámite. ¿Podría informarme si ese día se descuenta del sueldo? Gracias.»", "«Buenos días quisiera permiso el viernes trámite sueldo gracias»", "«Hola, necesito permiso el viernes porque tengo que hacer un trámite y no puedo ir el viernes. Gracias»", "La primera tiene saludo, orden, pregunta clara y puntuación."),
        ("=", "Un mensaje de 38 palabras quedó en 26 palabras al quitar las repeticiones. ¿Cuántas palabras se quitaron?", "38 - 26", "Se restan las palabras finales a las iniciales para saber cuántas se quitaron.", "palabras"),
        ("abc", "{F} ¿Dónde conviene un punto en el borrador?", "Antes de «gracias», para separar el cierre de la pregunta", "Entre «necesito» y «permiso»", "Después de «Hola», sin ninguna otra marca", "Un punto antes de «gracias» separa la consulta del agradecimiento."),
        ("ab", "Dos personas evalúan el mismo mensaje. Una dice «está raro». La otra dice «repite el viernes y le falta un saludo formal». ¿Qué evaluación ayuda más a reescribir?", "La segunda, porque señala qué cambiar", "La primera, porque es breve", "Una evaluación útil indica qué cambiar y por qué."),
        ("abc", "{F} Una persona dice que con corregir las tildes el mensaje queda bien. ¿Qué respondes?", "No: también hay que ordenar las ideas y cuidar el tono", "Sí: con las tildes ya queda perfecto", "Sí, porque el tono no importa en un mensaje", "El problema principal está en el orden, la repetición y el tono."),
        ("abc", "{F} ¿Qué orden de ideas es mejor al reescribir?", "Saludo, petición, motivo breve, consulta y agradecimiento", "Agradecimiento, motivo, saludo y petición", "Consulta, saludo, agradecimiento y petición", "Ese orden sigue el camino natural de una solicitud respetuosa."),
        ("{F} ¿Cuántas veces aparece la palabra «viernes» en el borrador? Escribe solo el número.", "2", "El borrador la usa en «el viernes» al pedir y al decir que no puede ir."),
    ],
    ctx=("abc", "Vas a enviar por correo una solicitud al centro de estudios para pedir un certificado. ¿Qué haces antes de enviarla?", "Leerla pensando en quien la recibirá y corregir lo confuso", "Enviarla sin leerla para ganar tiempo", "Agregar muchas exclamaciones para que se note urgente", "Releer antes de enviar evita errores y malentendidos."),
    sc=[("En Lengua y Literatura: ¿qué significa evaluar un texto propio?", "Revisar si cumple su propósito con criterios claros", "Se mira si el texto logra lo que quieres con criterios."),
        ("En Lengua y Literatura: ¿qué es reescribir?", "Volver a escribir un texto para mejorarlo", "Reescribir mejora el texto sin cambiar su propósito."),
        ("En Lengua y Literatura: ¿qué es el tono de un mensaje?", "La manera de hablar adecuada a quien lo recibe", "Cambia si le escribes a una jefatura o a un amigo.")],
    op=("{F} Evalúa el borrador con cinco preguntas (propósito, orden, repetición, tono y puntuación) y anota una respuesta breve a cada una. Luego reescribe el mensaje completo, en tres a cinco líneas, para que sea claro y cortés.",
        "Propósito: pedir permiso y consultar por el pago. Orden: falta orden. Repetición: «viernes». Tono: falta saludo formal. Puntuación: faltan puntos. Reescritura: Buenos días. Quisiera solicitar permiso el viernes para realizar un trámite. ¿Podría informarme si ese día se descuenta del sueldo? Gracias.",
        ["responde las cinco preguntas con datos del borrador", "la reescritura elimina la repetición", "la reescritura tiene saludo, orden, puntuación y cortesía"],
        ["cinco respuestas breves y mensaje reescrito de tres a cinco líneas"],
        ["no cambiar el tono", "perder la consulta sobre el pago"],
        "Pregunta de revisión: «¿Qué entiende quien recibe mi mensaje?»."),
    reinforce="Relee un mensaje que hayas escrito esta semana y marca una repetición y una frase que mejorarías.",
    extend="Reescribe el mismo mensaje del ejercicio para enviarlo a una amistad, cambiando el tono pero no el propósito.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy conozco los criterios de coherencia y cohesión y el vocabulario para evaluar un texto con una pauta.",
    prior=["Releo mis textos.", "Reconozco repeticiones.", "Uso conectores simples."],
    explain=[
        "La coherencia se refiere al sentido: el texto trata de un tema, sus ideas siguen un orden y ninguna contradice a otra. La cohesión se refiere a las uniones: conectores, pronombres y puntuación que enlazan las oraciones.",
        "Una pauta de revisión es una lista de criterios. Con ella se marca cada criterio como cumplido o no y se anota la frase que lo muestra. Así no revisas «a ojo», sino con pasos claros.",
        "Los problemas más comunes son las contradicciones, las repeticiones, los conectores que faltan o están mal elegidos, y el orden confuso. Cada problema tiene una solución: quitar, unir, reemplazar o reordenar.",
    ],
    vocab=[("pauta de revisión", "lista de criterios para evaluar un texto"), ("contradicción", "oración que niega lo que dice otra"), ("reemplazo", "palabra que sustituye a otra para no repetirla"), ("reordenar", "cambiar el orden de las ideas para que se entiendan")],
    worked=[
        ("Detectar una contradicción", "Aviso: «La feria es el sábado» y «la feria es el domingo» (ejemplo).", ["Una oración niega la otra.", "Hay que confirmar el dato y dejar una sola."], "Contradicción: se corrige"),
        ("Unir datos repetidos", "«La clase es el lunes. La clase es a las 18. La clase es en la sala 3» (ejemplo).", ["Se repite «la clase es».", "Uno todo en una oración."], "La clase es el lunes a las 18, en la sala 3"),
    ],
    mistakes=[("Agregar conectores para arreglar un texto contradictorio.", "Un conector no corrige una contradicción.", "Primero corrige el dato y después une las ideas."),
              ("Marcar un problema sin escribir cómo corregirlo.", "Quien escribe no sabe qué cambiar.", "Anota el problema y una propuesta de cambio.")],
    T=[
        ("abc", "¿Cuál es un ejemplo de falta de coherencia?", "Un aviso que dice «la sala abre a las 9» y luego «la sala abre a las 10»", "Un aviso con una tilde mal puesta", "Un aviso escrito con letra pequeña", "La contradicción rompe el sentido del texto."),
        ("abc", "¿Cuál es un ejemplo de falta de cohesión?", "Oraciones seguidas que repiten la misma palabra y no se unen", "Un aviso con un dato falso", "Un aviso sin fecha", "La cohesión mira las uniones entre oraciones."),
        ("{F} ¿Cuántas oraciones del aviso comienzan con «La reunión es»? Escribe solo el número.", "3", "Comienzan así la primera, la tercera y la última oración."),
        ("abc", "{F} ¿Qué dos oraciones se contradicen?", "«Hay que traer la cédula» y «No hay que traer nada»", "«La reunión es el jueves» y «La reunión es en la sede»", "«Se tratará el tema del agua» y «La reunión es a las 19 horas»", "Una pide traer algo y la otra dice que no hay que traer nada."),
        ("ab", "{F} ¿Qué criterio de la pauta incumple esa contradicción?", "El 3: sin contradicciones", "El 6: puntuación y ortografía", "Es el criterio que pide que ninguna idea niegue a otra."),
        ("abc", "{F} ¿Qué recurso evita repetir «La reunión es» tres veces?", "Reunir los datos en una sola oración: «La reunión es el jueves a las 19 horas, en la sede»", "Repetirlo una cuarta vez", "Quitar todos los datos", "Una sola oración reúne día, hora y lugar sin repetir."),
        ("=", "{F} El borrador tiene 6 oraciones. Se unen en una sola las tres que dan día, hora y lugar, y se elimina la oración contradictoria. ¿Cuántas oraciones quedan?", "6 - 2 - 1", "Al unir tres en una se pierden dos; al quitar la contradictoria se pierde una más.", "oraciones"),
        ("abc", "{F} ¿Qué reemplazo evita repetir «la reunión» al anunciar el tema?", "«En ella se tratará el tema del agua»", "«La reunión: se tratará el agua de la reunión»", "«Agua»", "El pronombre «ella» reemplaza a «la reunión» y mantiene el sentido."),
        ("ab", "{F} ¿Qué falta en el aviso para cumplir el criterio 1, propósito claro?", "Una frase inicial que diga para qué se convoca", "Más signos de exclamación", "El propósito se entiende mejor si se dice para qué es la reunión."),
        ("abc", "{F} ¿Qué orden de ideas es más claro?", "Qué es, cuándo, dónde, qué llevar y qué se tratará", "Qué llevar, qué se tratará, dónde y cuándo", "Dónde, qué llevar y cuándo, sin decir qué es", "Primero se presenta de qué se trata y luego los datos."),
        ("ab", "{F} Alguien propone solo agregar «por eso» entre las oraciones para arreglar el aviso. ¿Resuelve el problema?", "No: los conectores no corrigen una contradicción ni un orden confuso", "Sí: con conectores cualquier texto queda coherente", "Primero hay que corregir el sentido y después unir."),
        ("abc", "{F} ¿Cuál es la mejor reescritura completa del aviso?", "«Reunión de vecinos: jueves a las 19 horas, en la sede. Traer la cédula. Se tratará el tema del agua.»", "«La reunión es el jueves. La reunión es a las 19 horas. La reunión es en la sede. No hay que traer nada.»", "«Hay que traer la cédula y no hay que traer nada, y la reunión, el agua»", "La primera junta los datos, resuelve la contradicción y es clara."),
        ("=", "{F} La pauta tiene 6 criterios y el borrador incumple 5 (propósito, orden, contradicciones, conectores y repeticiones). ¿Cuántos criterios cumple?", "6 - 5", "Se restan los criterios incumplidos del total de seis.", "criterio"),
    ],
    ctx=("abc", "Escribes un aviso para pegar en la entrada de la sede de tu comunidad y notas que dices dos horarios distintos para la misma reunión. ¿Qué haces?", "Verifico el horario correcto y dejo solo uno", "Dejo los dos, para que cada persona elija", "Agrego un conector entre ambos horarios", "Una contradicción se corrige comprobando el dato."),
    sc=[("En Lengua y Literatura: ¿qué diferencia hay entre coherencia y cohesión?", "La coherencia es el sentido del texto; la cohesión, las uniones entre oraciones", "Una trata del sentido y la otra de cómo se unen las oraciones."),
        ("En Lengua y Literatura: ¿para qué sirve una pauta de revisión?", "Para evaluar un texto con criterios claros", "Ordena la revisión y evita juzgar a ojo."),
        ("En Lengua y Literatura: ¿qué haces con una contradicción?", "Compruebo el dato y dejo solo la versión correcta", "Hay que verificar y mantener una sola versión.")],
    op=("{F} Evalúa el aviso con la pauta: para cada criterio escribe «cumple» o «no cumple» y una frase del borrador que lo muestre. Después reescribe el aviso en dos a tres líneas, resolviendo la contradicción (el aviso debe pedir traer la cédula).",
        "Criterio 3: no cumple, «Hay que traer la cédula» y «No hay que traer nada». Reescritura: Reunión de vecinos: jueves a las 19 horas, en la sede. Traer la cédula. Se tratará el tema del agua.",
        ["marca cada uno de los seis criterios con una frase del borrador", "resuelve la contradicción", "la reescritura une datos sin repetir"],
        ["seis criterios evaluados y aviso reescrito de dos a tres líneas"],
        ["marcar criterios sin dar frases", "mantener la contradicción"],
        "Pregunta de revisión: «¿Se entiende el aviso en una sola lectura?»."),
    reinforce="Escribe dos oraciones contradictorias sobre un horario inventado y luego corrígelas.",
    extend="Revisa con la pauta un aviso real de tu barrio o trabajo (sin copiar datos personales) y anota dos mejoras.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy veo paso a paso cómo diagnosticar un texto y reescribirlo: leer, marcar, decidir, reescribir y releer.",
    prior=["Conozco criterios de coherencia y cohesión.", "Reconozco contradicciones y repeticiones.", "Sé unir oraciones con conectores."],
    explain=[
        "Reescribir sigue cinco pasos. Primero, lee el texto completo. Segundo, marca los problemas: repeticiones, contradicciones, orden confuso y falta de conectores. Tercero, decide cómo corregir cada uno: quitar, unir, reemplazar o reordenar.",
        "Cuarto, reescribe. Cuida que el significado se mantenga: no cambies lo que querías decir. Quinto, vuelve a leer el texto nuevo con los mismos criterios para comprobar que mejoró.",
        "Si una oración contradice a otra, primero verifica cuál dato es el correcto y deja solo ese. No dejes una oración solo porque «suena bien»: debe aportar algo al propósito del texto y a quien lo leerá.",
    ],
    vocab=[("diagnosticar", "marcar los problemas de un texto antes de corregirlo"), ("unir oraciones", "juntar dos oraciones en una con un conector o un relativo"), ("significado", "lo que el texto quiere decir"), ("releer", "leer de nuevo para comprobar la mejora")],
    worked=[
        ("Unir con un conector", "«La caja estaba rota. Cambiamos la caja» (ejemplo).", ["La segunda es consecuencia de la primera.", "Uso «por eso»."], "La caja estaba rota; por eso la cambiamos"),
        ("Resolver una contradicción", "«El local abre a las 9» y «el local abre a las 8» (ejemplo).", ["No pueden ser ciertas las dos.", "Verifico el horario correcto antes de escribir."], "Se deja un solo horario, el verificado"),
    ],
    mistakes=[("Reescribir sin marcar primero los problemas.", "Se corrigen cosas al azar y quedan errores importantes.", "Lee y marca antes de reescribir."),
              ("Cambiar el sentido al reescribir.", "El texto nuevo dice algo distinto de lo que se quería.", "Comprueba que el significado se mantenga.")],
    T=[
        ("abc", "¿Cuál es el primer paso para evaluar un texto propio?", "Leerlo completo, pensando en quien lo leerá", "Cambiar palabras al azar", "Copiarlo a limpio sin leerlo", "Antes de corregir hay que conocer todo el texto."),
        ("ab", "{F} ¿Qué dos oraciones se contradicen en el informe?", "«Los pedidos llegaron tarde» y «el camión llegó temprano»", "«Terminamos a las 18 horas» y «Los pedidos se revisaron»", "Una dice que llegaron tarde y la otra que el camión llegó temprano."),
        ("{F} ¿A qué hora terminaron según el informe? Escribe solo el número.", "18", "El informe dice que terminaron a las 18 horas."),
        ("abc", "{F} ¿Qué palabra se repite en varias oraciones y cansa a quien lee?", "«pedidos»", "«bodega»", "«camión»", "«Pedidos» aparece en tres oraciones distintas."),
        ("ab", "{F} ¿Qué cambio mejora el orden del informe?", "«La mercadería estaba mal ordenada» debe ir antes de «ordenamos la mercadería»", "«Terminamos a las 18 horas» debe ir al comienzo", "Primero va el problema y después la acción para resolverlo."),
        ("abc", "{F} ¿Qué conector une bien «la mercadería estaba mal ordenada» con «ordenamos la mercadería»?", "Por eso", "Aunque", "Sin embargo", "La acción es consecuencia del problema."),
        ("=", "{F} El informe tiene 7 oraciones. Se quita la que contradice, se unen las dos sobre la mercadería y se unen las dos primeras sobre los pedidos. ¿Cuántas oraciones quedan?", "7 - 1 - 1 - 1", "Cada acción quita una oración: la contradictoria y las dos uniones.", "oraciones"),
        ("abc", "{F} ¿Cuál es la mejor reescritura de las dos primeras oraciones?", "Ayer, en la bodega, recibimos los pedidos con retraso.", "Ayer, en la bodega, recibimos los pedidos y los pedidos llegaron tarde.", "Ayer, en la bodega, los pedidos llegaron a tiempo.", "Une las dos ideas, mantiene el sentido y evita repetir."),
        ("abc", "{F} ¿Cuál es la mejor unión de las oraciones 3 y 4 del informe?", "Como la mercadería estaba mal ordenada, la ordenamos.", "La mercadería estaba mal ordenada y ordenamos la mercadería.", "Ordenamos la mercadería porque estaba bien ordenada.", "Conecta causa y acción sin repetir ni contradecirse."),
        ("ab", "{F} Quien escribió quiere dejar la oración sobre los clientes contentos porque «suena bien». ¿Qué conviene?", "Verificar el dato y quitarla si contradice lo anterior", "Dejarla, porque suena bien aunque contradiga", "Una oración que contradice el texto debe corregirse o quitarse."),
        ("abc", "Después de reescribir un texto, ¿qué paso falta?", "Releer el texto nuevo con los mismos criterios", "Guardarlo sin leerlo", "Reescribirlo otra vez al azar", "Releer comprueba que la versión nueva realmente mejoró."),
        ("abc", "{F} ¿Cuál es la reescritura más coherente del informe?", "Ayer, en la bodega, recibimos los pedidos con retraso. Como la mercadería estaba mal ordenada, la ordenamos y revisamos los pedidos. Terminamos a las 18 horas.", "Los pedidos llegaron tarde y el camión llegó temprano y ordenamos la mercadería que estaba mal ordenada y terminamos.", "Recibimos los pedidos. Recibimos los pedidos con retraso. Terminamos.", "Elimina la contradicción, une las ideas y mantiene el orden."),
        ("{F} El procedimiento tiene los pasos leer, marcar, decidir, reescribir y releer. ¿Cuántos pasos son? Escribe solo el número.", "5", "Se cuentan las cinco acciones enumeradas."),
    ],
    ctx=("abc", "Escribiste un informe de una actividad y notas que dos oraciones dicen cosas distintas sobre la hora de entrega. ¿Qué haces?", "Compruebo la hora correcta y dejo solo esa", "Dejo las dos horas para que se elija", "Agrego «sin embargo» entre ellas", "Una contradicción se corrige verificando el dato."),
    sc=[("En Lengua y Literatura: ¿cuáles son los cinco pasos para reescribir?", "Leer, marcar, decidir, reescribir y releer", "Es el procedimiento completo para reescribir."),
        ("En Lengua y Literatura: ¿qué cuidas al reescribir?", "Que el significado se mantenga", "No debe cambiar lo que querías decir."),
        ("En Lengua y Literatura: ¿qué se hace con una oración repetida?", "Se une con otra, se reemplaza o se quita", "Se corrige para evitar repeticiones innecesarias.")],
    op=("{F} Aplica los cinco pasos al informe. Escribe en tu cuaderno: (1) una lista de los problemas que marcaste; (2) la decisión para cada uno; (3) el informe reescrito en cuatro a cinco líneas; (4) una frase que diga qué cambió y por qué.",
        "Problemas: repetición de «pedidos»; contradicción entre «llegaron tarde» y «camión llegó temprano»; orden. Decisión: unir, quitar y reordenar. Reescritura: Ayer, en la bodega, recibimos los pedidos con retraso. Como la mercadería estaba mal ordenada, la ordenamos y revisamos los pedidos. Terminamos a las 18 horas.",
        ["identifica al menos tres problemas", "reescribe sin contradicciones ni repeticiones", "explica qué cambió y por qué"],
        ["lista de problemas, decisiones, informe reescrito y explicación"],
        ["no resolver la contradicción", "cambiar el sentido del informe"],
        "Pregunta de revisión: «¿El texto nuevo dice lo mismo que quería decir el original, pero mejor?»."),
    reinforce="Marca en un texto breve que hayas escrito una repetición y una oración que podrías unir con otra.",
    extend="Escribe tu propia lista de cinco pasos para reescribir y pruébala con un correo o nota tuyo.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo la reescritura de oraciones: evitar repeticiones, puntuar, elegir conectores y mantener el sentido.",
    prior=["Reconozco repeticiones y contradicciones.", "Conozco algunos conectores.", "Sé qué es un pronombre."],
    explain=[
        "Reescribir una oración puede hacerse de varias formas. Para evitar repetir un nombre, se usa un pronombre, un posesivo (suyo, suya) o se omite el sujeto cuando se entiende. Para unir dos ideas, se usa un conector o una coma.",
        "La puntuación ayuda a leer. El punto separa ideas completas. La coma separa partes de una oración o enumera. Una oración muy larga sin signos se confunde; se separa o se une con un conector.",
        "Elige el conector según la relación: «porque» (causa), «por eso» (consecuencia), «sin embargo» (oposición), «además» (suma). Si usas un conector equivocado, cambias el sentido sin querer.",
    ],
    vocab=[("pronombre", "palabra que sustituye a un nombre: él, ella, ellos"), ("posesivo", "palabra que muestra pertenencia: mi, su, suyo"), ("conector", "palabra que une ideas y muestra su relación"), ("omitir el sujeto", "no repetir quien hace la acción cuando ya se entiende")],
    worked=[
        ("Omitir el sujeto", "«Mi vecina vende pan y mi vecina cocina todos los días» (ejemplo).", ["Se repite «mi vecina».", "El sujeto ya se entiende."], "Mi vecina vende pan y cocina todos los días"),
        ("Corregir un conector", "«Llovió, sin embargo se mojó la calle» (ejemplo).", ["No hay oposición: el agua moja la calle.", "Corresponde «por eso» o «y»."], "Llovió y se mojó la calle"),
    ],
    mistakes=[("Elegir un conector que cambia el sentido.", "«Sin embargo» opone ideas; si no hay oposición, confunde.", "Pregunta qué relación hay antes de elegir el conector."),
              ("Cortar una oración con un punto en medio de una idea.", "La idea queda incompleta.", "Cada punto debe cerrar una idea completa.")],
    T=[
        ("abc", "{F} ¿Cómo se evita repetir «Rosa» en la oración 1?", "Rosa trabaja en una peluquería y quiere abrir la suya.", "Rosa trabaja en una peluquería y Rosa quiere abrir una peluquería.", "Rosa trabaja y quiere peluquería.", "Se omite el sujeto repetido y se usa el posesivo «la suya»."),
        ("abc", "{F} ¿Qué versión mejora la puntuación de la oración 2?", "Llegué tarde al control porque el bus se demoró, y no alcancé a comprar el pase.", "Llegué tarde al control porque el bus se demoró no alcancé a comprar el pase.", "Llegué tarde al control. Porque el bus se demoró. No alcancé. A comprar el pase.", "La coma y la «y» separan las dos ideas con claridad."),
        ("ab", "{F} ¿Qué cambio corrige la oración 3?", "Cambiar «sin embargo» por «y», porque no hay oposición", "Dejar «sin embargo», porque suena más formal", "El taller reparó y el refrigerador quedó bien: las ideas se suman."),
        ("{F} ¿Qué palabra sobra en la oración 4? Escribe solo la palabra.", "primero", "El segundo «primero» repite y no tiene sentido tras «luego»."),
        ("abc", "{F} ¿Cómo se unen las dos oraciones de la 5 sin repetir «los vecinos»?", "Los vecinos propusieron limpiar la plaza y pidieron bolsas a la junta de vecinos.", "Los vecinos propusieron los vecinos pidieron limpiar.", "Los vecinos propusieron limpiar la plaza, los vecinos.", "Un solo sujeto con dos verbos evita la repetición."),
        ("=", "{F} Una oración original de 14 palabras quedó en 9 al quitar la repetición. ¿Cuántas palabras se quitaron?", "14 - 9", "Se restan las palabras finales a las iniciales para saber cuántas se quitaron.", "palabras"),
        ("abc", "{F} ¿Qué recurso se usó en «Rosa trabaja en una peluquería y quiere abrir la suya»?", "Se omitió el sujeto repetido y se usó un posesivo", "Se agregó un conector de oposición", "Se cambió el tiempo del verbo", "Se evita repetir «Rosa» y «peluquería»."),
        ("ab", "{F} ¿Qué oración tenía el problema de falta de puntuación?", "La 2", "La 4", "En la 2 faltaba una coma o un conector entre las ideas."),
        ("abc", "¿Qué relación expresa «por eso» en «Llovió mucho; por eso suspendieron la feria»?", "Consecuencia", "Oposición", "Orden en el tiempo", "La suspensión es el resultado de la lluvia."),
        ("abc", "{F} ¿Qué criterio de reescritura se aplica al quitar el «primero» sobrante de la oración 4?", "Eliminar repeticiones innecesarias", "Agregar un conector de causa", "Cambiar la audiencia", "Se elimina una palabra repetida sin aportar."),
        ("ab", "Una persona reescribe una oración y cambia lo que quería decir. ¿Qué falló?", "No cuidó que el significado se mantuviera al reescribir", "Usó demasiados verbos", "Reescribir no debe alterar el mensaje que se quería comunicar."),
        ("abc", "{F} Alguien reescribió la oración 3 como «El taller no reparó el refrigerador y quedó funcionando bien». ¿Qué problema tiene?", "Cambió el sentido y se contradice: si no lo reparó, no pudo quedar funcionando", "Ninguno, porque es una versión más corta", "Solo le falta una coma", "La negación cambia el sentido del original."),
        ("abc", "{F} En la oración 5, ¿qué ocurre si se reemplaza el segundo «los vecinos» por «ellos»?", "Funciona bien: «ellos» evita la repetición y se entiende", "Se pierde todo el sentido", "Se contradice con la oración anterior", "El pronombre se refiere a los vecinos mencionados antes."),
    ],
    ctx=("abc", "Estás escribiendo una nota para un grupo de personas y notas que tres frases seguidas comienzan igual. ¿Qué haces?", "Uno las ideas y reemplazo las repeticiones por pronombres o conectores", "Dejo todo igual para que se vea ordenado", "Quito las oraciones del medio sin leerlas", "Variar el comienzo y unir ideas mejora la lectura."),
    sc=[("En Lengua y Literatura: ¿para qué sirve un pronombre?", "Para sustituir un nombre y no repetirlo", "Evita repetir palabras y da cohesión al texto."),
        ("En Lengua y Literatura: ¿qué conector expresa oposición?", "Sin embargo", "Presenta una idea contraria a la anterior."),
        ("En Lengua y Literatura: ¿qué haces con una oración larga sin signos?", "La separo con puntos o la uno con conectores y comas", "Los signos ayudan a leer con claridad.")],
    op=("{F} Reescribe en tu cuaderno las cinco oraciones corrigiendo lo que haga falta. Al lado de cada una escribe qué cambiaste (repetición, puntuación, conector o palabra sobrante). Después une la 1 y la 5 en un párrafo de tres líneas con un conector.",
        "1) Rosa trabaja en una peluquería y quiere abrir la suya (omití el sujeto repetido). 3) El taller reparó el refrigerador y quedó funcionando bien (cambié el conector). Párrafo: Rosa trabaja en una peluquería y quiere abrir la suya. Además, los vecinos propusieron limpiar la plaza.",
        ["reescribe las cinco oraciones", "explica el cambio de cada una", "une dos oraciones con un conector adecuado"],
        ["cinco oraciones reescritas con explicación y un párrafo de tres líneas"],
        ["cambiar el significado", "usar «sin embargo» sin que haya oposición"],
        "Pregunta de revisión: «¿Cada oración dice lo mismo que antes, pero con más claridad?»."),
    reinforce="Reescribe dos oraciones de tu vida diaria para evitar una repetición.",
    extend="Escribe cuatro oraciones sobre un oficio que conozcas que repitan una palabra y luego reescríbelas con pronombres y conectores.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico los criterios a un texto de trabajo o trámite: evalúo una carta con una pauta y la reescribo para comunicarla.",
    prior=["Evalúo y reescribo oraciones.", "Conozco partes de una carta formal.", "Uso conectores y pronombres."],
    explain=[
        "Una carta formal tiene saludo, propósito claro, motivos y una despedida cortés. Para evaluarla, revisa si cada parte cumple su función y si el tono es respetuoso. Una solicitud debe decir con claridad qué se pide.",
        "Al reescribir, une las ideas repetidas, quita lo que no ayuda al propósito y ordena los datos: qué ocurre, por qué es importante y qué se solicita. Cuida la puntuación y cierra con una fórmula de cortesía.",
        "Un dato que no se relaciona con la petición, aunque sea verdadero, distrae. Pregúntate si ayuda a lograr tu propósito. Si no, déjalo fuera. Así la persona que lee entiende rápido qué necesitas.",
    ],
    vocab=[("solicitud", "texto que pide algo a una persona o institución"), ("fórmula de cortesía", "saludo o despedida respetuosa: Estimados, Atentamente"), ("propósito", "lo que se quiere lograr con el texto"), ("dato ajeno", "dato que no ayuda al propósito del texto")],
    worked=[
        ("Evaluar el propósito", "Una carta dice «la calle está mala» sin pedir nada concreto (ejemplo).", ["No se sabe qué se solicita.", "El propósito no es claro."], "Falta una petición clara"),
        ("Quitar un dato ajeno", "En una solicitud de reparación aparece «mi vecino tiene un perro» (ejemplo).", ["No se relaciona con la reparación.", "Distrae del propósito."], "Se quita"),
    ],
    mistakes=[("Dejar datos verdaderos pero ajenos a lo que pides.", "Distraen y alargan el texto.", "Incluye solo lo que ayuda a tu petición."),
              ("Cerrar una carta formal con una despedida de confianza.", "El tono no corresponde a quien la recibe.", "Usa «Atentamente» u otra fórmula cortés.")],
    T=[
        ("abc", "{F} ¿Cuál es el propósito de la carta?", "Solicitar que se repare una luminaria", "Agradecer a la municipalidad", "Informar un cambio de calle", "La carta termina pidiendo que arreglen la luminaria."),
        ("{F} ¿Cuántos meses lleva sin funcionar la luminaria? Escribe solo el número.", "1", "La carta dice que hace un mes que no funciona."),
        ("abc", "{F} ¿Qué oración aporta un dato que no se relaciona con la petición?", "«Además la luminaria de la esquina funciona bien»", "«Es peligroso para los vecinos porque no se ve nada de noche»", "«Pido que la arreglen»", "El estado de otra luminaria no ayuda a pedir la reparación."),
        ("abc", "{F} ¿Qué palabra se repite demasiado en la carta?", "«luminaria»", "«calle»", "«vecinos»", "La palabra «luminaria» aparece cuatro veces en la carta."),
        ("=", "{F} La palabra «luminaria» aparece 4 veces. Si en la reescritura quedan 2, ¿cuántas veces se reemplazó o se quitó?", "4 - 2", "Se restan las apariciones finales a las iniciales para saber cuántas cambiaron.", "veces"),
        ("ab", "{F} ¿Qué fórmula de cierre es adecuada en una carta formal?", "Atentamente", "Chao, nos vemos", "Una carta a una institución usa un cierre cortés y formal."),
        ("abc", "{F} ¿Cuál es una mejor versión de «Pido que la arreglen»?", "Solicito que la reparen a la brevedad, porque afecta la seguridad de los vecinos.", "Arréglenla ya, que es una vergüenza.", "Pido, pido que la arreglen, por favor, pido.", "Es clara, cortés y da una razón."),
        ("abc", "{F} ¿Cómo se unen «La luminaria no funciona» y «Hace un mes que la luminaria no funciona»?", "La luminaria no funciona desde hace un mes.", "La luminaria no funciona, la luminaria no funciona un mes.", "No funciona luminaria mes.", "Une las dos ideas en una oración sin repetir."),
        ("abc", "{F} En «Es peligroso porque no se ve nada de noche», ¿qué relación expresa «porque»?", "Causa", "Oposición", "Orden en el tiempo", "La falta de luz explica por qué es peligroso."),
        ("ab", "{F} ¿Por qué conviene quitar la oración sobre la luminaria de la esquina?", "No ayuda a lograr el propósito de la carta y distrae", "Las cartas no pueden tener más de cinco oraciones", "Un dato que no apoya la petición se deja fuera."),
        ("abc", "Antes de enviar la carta reescrita, ¿qué conviene hacer?", "Releerla con la pauta y comprobar que el propósito se entienda", "Enviarla enseguida, sin releer", "Agregar más datos ajenos al tema", "Releer con la pauta asegura que la carta cumpla su propósito."),
        ("abc", "{F} ¿Cuál es la mejor reescritura completa?", "«Estimados: les escribo para solicitar la reparación de la luminaria de mi calle, que no funciona desde hace un mes. Es peligroso para los vecinos, porque de noche no se ve nada. Agradezco su pronta respuesta. Atentamente, Carmen.»", "«Estimados: la luminaria no funciona. La luminaria no funciona hace un mes. Pido que la arreglen. Atentamente.»", "«Hola, la calle está mal, arreglen todo. Chao.»", "Es clara, ordenada, cortés y sin repeticiones."),
        ("=", "{F} El cuerpo de la carta original tenía 6 oraciones. En la reescritura quedaron 3. ¿Cuántas oraciones se quitaron o se unieron?", "6 - 3", "Se restan las oraciones finales a las iniciales para ver cuántas se quitaron o se unieron.", "oraciones"),
    ],
    ctx=("abc", "Debes escribir una solicitud a la municipalidad para pedir la reparación de una vereda de tu calle. ¿Qué incluyes?", "Saludo, qué se pide, por qué es importante y una despedida cortés", "Solo una queja sin pedir nada", "Datos sobre otras calles, para comparar", "Una solicitud clara tiene petición, razón y cortesía."),
    sc=[("En Lengua y Literatura: ¿qué es una solicitud?", "Un texto que pide algo a una persona o institución", "Pide algo con claridad y cortesía."),
        ("En Lengua y Literatura: ¿qué haces con un dato que no ayuda a tu petición?", "Lo quito, porque distrae del propósito", "Lo ajeno al propósito se deja fuera."),
        ("En Lengua y Literatura: ¿cómo se cierra una carta formal?", "Con una fórmula cortés como «Atentamente»", "El cierre de una carta debe ser respetuoso y cortés.")],
    op=("{F} Evalúa la carta con estas preguntas: propósito claro, orden, repeticiones, datos ajenos y tono. Anota una respuesta breve a cada una. Luego reescribe la carta completa en cuatro a cinco líneas, sin agregar datos nuevos, y subraya los conectores que usaste.",
        "Propósito: se pide reparar. Repeticiones: «luminaria». Dato ajeno: la luminaria de la esquina. Tono: «Pido» es poco formal. Reescritura: Estimados: les escribo para solicitar la reparación de la luminaria de mi calle, que no funciona desde hace un mes. Es peligroso porque de noche no se ve nada. Atentamente, Carmen.",
        ["responde las cinco preguntas con frases de la carta", "quita el dato ajeno y las repeticiones", "mantiene propósito, tono formal y cierre cortés"],
        ["cinco respuestas breves y carta reescrita de cuatro a cinco líneas"],
        ["agregar datos nuevos", "mantener «Pido que» sin cambiar el tono"],
        "Pregunta de revisión: «Si la municipalidad lee solo mi carta, ¿entiende qué pido y por qué?»."),
    reinforce="Escribe en dos líneas una solicitud clara y cortés para pedir una hora de atención en un consultorio (sin datos personales).",
    extend="Escribe una carta de cuatro líneas con una petición a tu centro de estudios y revísala con la pauta de cinco preguntas.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso mi texto con una pauta final, lo comunico para audiencias distintas y decido los pasos siguientes.",
    prior=["Evalúo y reescribo textos.", "Conozco una pauta de revisión.", "Cito mis fuentes."],
    explain=[
        "Al terminar, revisa tu texto con una pauta completa: propósito y audiencia, orden y coherencia, conectores, repeticiones, puntuación, título, cierre y fuentes. Marca cada criterio y corrige lo que falle antes de entregar.",
        "Un mismo texto puede comunicarse de formas distintas según la audiencia. Para un diario mural, escribes más extenso y con detalles. Para un mensaje breve, conservas los datos esenciales y reduces las explicaciones.",
        "Los datos no cambian al adaptar el texto: lo que cambia es cuánto se explica y el tono. Antes de entregar, léelo en voz alta o pide a otra persona que lo lea y te diga qué entendió.",
    ],
    vocab=[("audiencia", "personas a quienes se dirige el texto"), ("versión definitiva", "texto ya revisado y listo para entregar"), ("adaptar", "cambiar el nivel de detalle y el tono según quien lee"), ("datos esenciales", "información sin la cual el texto no se entiende")],
    worked=[
        ("Adaptar a un mensaje breve", "Un texto de cuatro oraciones sobre un taller de costura (ejemplo).", ["Conservo cuándo, dónde y cuántas socias.", "Quito explicaciones largas."], "Mensaje: Taller de costura, jueves, en la sede"),
        ("Revisar con la pauta", "Texto sin fuentes citadas (ejemplo).", ["El criterio 7 pide fuentes.", "No cumple."], "Se agrega la cita antes de entregar"),
    ],
    mistakes=[("Cambiar los datos al adaptar el texto a otra audiencia.", "La información debe ser la misma en todas las versiones.", "Cambia el detalle y el tono, no los datos."),
              ("Entregar sin releer una última vez.", "Quedan errores que ya habías detectado.", "Relee con la pauta antes de entregar.")],
    T=[
        ("abc", "{F} ¿Cuál es la audiencia de la Versión 1?", "Las personas del barrio que leen el diario mural", "La junta de vecinos, por mensaje", "Autoridades nacionales", "La ficha dice que está escrita para el diario mural."),
        ("{F} ¿Cuántos puestos tiene hoy la feria? Escribe solo el número.", "15", "Las dos versiones indican 15 puestos."),
        ("=", "{F} ¿Cuántos puestos más tiene hoy la feria que cuando nació?", "15 - 8", "Se restan los puestos iniciales a los actuales para ver el aumento.", "puestos"),
        ("ab", "{F} ¿Qué diferencia principal hay entre las dos versiones?", "La Versión 2 es más breve y directa, para un mensaje rápido", "La Versión 2 tiene más datos y más párrafos", "La Versión 2 conserva lo esencial en pocas palabras."),
        ("abc", "{F} ¿Qué criterio de la pauta cumple el título «La feria que reúne a la plaza»?", "El 6: título y cierre", "El 5: puntuación y ortografía", "El 7: fuentes citadas", "El criterio 6 incluye tener un título adecuado."),
        ("ab", "{F} ¿Qué criterio cumple la cita «(registro de la feria)»?", "El 7: fuentes citadas", "El 3: conectores y reemplazos", "La cita indica de dónde sale el dato."),
        ("abc", "{F} ¿Qué expresión de la Versión 1 cumple la función de conector de tiempo?", "«Con el tiempo»", "«del barrio»", "«y pan»", "Indica que ocurrió un cambio con el paso de los años."),
        ("abc", "{F} ¿Qué conviene conservar al adaptar la Versión 1 a un mensaje breve?", "Los datos esenciales: cuándo, dónde y cuántos puestos", "Los adjetivos de la entrada", "Solo el título", "Sin los datos esenciales el mensaje no sirve."),
        ("abc", "{F} ¿Qué oración de la Versión 1 sería un buen cierre?", "«Hoy los vecinos compran verduras y pan sin ir lejos.»", "«La feria vecinal de la plaza funciona los domingos con 15 puestos.»", "«Nació en 2021 con ocho puestos (registro de la feria).»", "Termina mostrando el efecto de la feria en los vecinos."),
        ("ab", "¿Por qué al adaptar un texto cambia el detalle y no los datos?", "Porque los datos deben ser los mismos; cambia cuánto se explica según la audiencia", "Porque a cada audiencia hay que cambiarle los datos", "Una información distinta según la audiencia sería engañosa."),
        ("abc", "{F} Alguien dice que la Versión 2 puede omitir el año. ¿Qué respondes?", "Puede omitirse si la audiencia no lo necesita, pero no debe cambiarse", "Siempre debe llevar todos los datos de la Versión 1", "Debe cambiarse por otro año", "Se puede reducir el detalle, pero no alterar los datos."),
        ("abc", "{F} ¿Qué paso final conviene antes de entregar la versión definitiva?", "Releerla con la pauta de siete criterios y corregir lo que falle", "Entregarla sin leer", "Agregar datos nuevos al azar", "La relectura con la pauta confirma que está lista."),
        ("=", "{F} La pauta tiene siete criterios y la versión definitiva cumple seis. ¿Cuántos faltan por cumplir?", "7 - 6", "Se restan los criterios cumplidos del total de siete.", "criterio"),
    ],
    ctx=("abc", "Debes entregar en tu centro un texto breve sobre un oficio o una actividad que conozcas y después contarlo en un mensaje corto a un grupo. ¿Qué haces?", "Escribo la versión completa y adapto una breve con los mismos datos", "Escribo dos textos con datos distintos", "Entrego solo el mensaje breve en ambos casos", "Se adapta el detalle y el tono, no los datos."),
    sc=[("En Lengua y Literatura: ¿qué es la versión definitiva de un texto?", "El texto ya revisado y listo para entregar", "Es la versión que pasó la revisión final."),
        ("En Lengua y Literatura: ¿qué cambia al adaptar un texto a otra audiencia?", "El nivel de detalle y el tono, no los datos", "Los datos se mantienen iguales en todas las versiones."),
        ("En Lengua y Literatura: ¿qué haces antes de entregar un texto?", "Lo releo con la pauta y corrijo lo que falle", "La última revisión evita errores que ya habías detectado.")],
    op=("{F} Elige una de estas dos tareas: A) Aplica la pauta de siete criterios a la Versión 1 y escribe una frase por criterio, marcando si cumple o no. B) Escribe una Versión 3 para una persona de otro barrio que no conoce la plaza, en tres a cuatro líneas, con los mismos datos. En ambos casos termina con dos pasos siguientes para mejorar tu forma de escribir.",
        "Opción A: 1) cumple: se entiende que es para el diario mural. 7) cumple: cita el registro. Pasos siguientes: leer en voz alta y pedir que otra persona revise. Opción B: Feria vecinal de la plaza: funciona los domingos con 15 puestos, nació en 2021 con ocho puestos y ofrece verduras y pan.",
        ["usa los datos de la ficha sin cambiarlos", "aplica los criterios o adapta con otro nivel de detalle", "propone dos pasos siguientes realistas"],
        ["siete frases de evaluación o versión nueva de tres a cuatro líneas, y dos pasos siguientes"],
        ["cambiar los datos", "no proponer pasos siguientes"],
        "Pregunta de revisión: «¿Una persona que no conoce el tema entiende mi texto?»."),
    reinforce="Elige un texto breve que hayas escrito y reduce su extensión a la mitad conservando los datos esenciales.",
    extend="Pide a otra persona que lea tu texto en voz alta y anota dos lugares donde tropezó; corrige esos lugares.",
)
