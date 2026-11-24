"""Lengua y Literatura EPJA Media Nivel 1, módulo 2 (parte 3): OAD-07, evaluar un texto no literario con criterios de veracidad, consistencia y propósito comunicativo. Todos los textos son inventados y se leen en papel."""
from __future__ import annotations

from epja_leli_nm1_b_common import build

O = "EPJA-LELI-NM1-OAD-07"

F1 = ("Reseña (inventada) publicada en el tablón de una sede vecinal sobre el «Taller Don Lalo» (nombre de ejemplo): «Llevé mi camioneta el martes 4 por un ruido en el freno. Me atendieron en 20 minutos "
      "y me mostraron la pieza gastada antes de cambiarla. Cobraron $35.000, lo mismo que me habían dicho por teléfono. Es el mejor taller del mundo y nadie lo supera.» "
      "Pauta de evaluación (inventada): Veracidad: ¿hay datos que se puedan comprobar? Consistencia: ¿el texto se contradice? Propósito: ¿qué busca lograr quien escribe?")

F2 = ("Fuente 1 (inventada), comunicado de la municipalidad de ejemplo, fechado el 1 de octubre: «El desfile del sábado 5 cortará la calle Maipú de 14:00 a 18:00. Habrá desvío por calle Chacabuco». "
      "Fuente 2 (inventada), publicación de un vecino sin dar su nombre: «Cortan Maipú todo el día el sábado y también el domingo». "
      "Fuente 3 (inventada), nota del diario local de ejemplo: «Según la municipalidad, la calle Maipú permanecerá cerrada el sábado 5, de 14:00 a 18:00».")

F3 = ("Nota de prensa (inventada) de la empresa «Transportes del Valle» (nombre de ejemplo): «Mejora histórica de la puntualidad. Antes de este año, 60 de cada 100 viajes llegaban a la hora; ahora llegan 75 de cada 100. "
      "Es decir, la puntualidad mejoró en 20 viajes por cada 100. Nuestro servicio es el favorito de las familias de la comuna. Para más información, escriba a la oficina de la empresa.»")

F4 = ("Texto 1 (inventado), publicación de una persona sobre un curso de cocina de ejemplo: «Es el mejor curso que existe. Aprendí todo en una semana y ahora tengo muchos clientes. Inscríbanse ya.» "
      "Texto 2 (inventado), informe del centro de capacitación de ejemplo, fechado el 12 de septiembre: «El curso de cocina duró 8 semanas. Se inscribieron 40 personas y lo terminaron 32. "
      "Cada persona asistió a 2 clases por semana. El informe completo está disponible en la oficina del centro.»")

F5 = ("Mensaje A (inventado), reenviado en cadena: «Este jarabe casero cura cualquier enfermedad. 100 % garantizado. Lo comprobó un doctor de otro país. Si no lo compartes, no te sirve.» "
      "Mensaje B (inventado), comunicado del consultorio de ejemplo, fechado el 3 de octubre: «El sábado 6, de 9:00 a 13:00, habrá un control de salud gratuito para personas inscritas. Traiga su cédula. Consultas en el mesón de informaciones del consultorio.»")

F6 = ("Nota (inventada) del boletín «El Pregonero» (nombre de ejemplo): «Éxito rotundo de la feria laboral: más de 2.000 personas consiguieron trabajo. Se inscribieron 1.200 personas a la feria. "
      "La organización, el centro de empleo de ejemplo, informó que hubo 30 empresas participantes. Según los organizadores, fue la mejor feria de la historia de la comuna.»")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy conozco tres criterios para evaluar un texto no literario: veracidad, consistencia y propósito.",
    prior=["Reconozco emisor, receptor y propósito.", "Distingo hechos de opiniones.", "Sé revisar sumas y fechas."],
    explain=[
        "Evaluar un texto es emitir un juicio fundamentado sobre él: no basta decir «me gusta» o «no me convence», hay que dar razones tomadas del texto. Ya lo haces cuando decides si confiar en la opinión de alguien sobre un taller o un comercio.",
        "Usamos tres criterios. La veracidad pregunta si los datos se pueden comprobar y de dónde vienen. La consistencia pregunta si el texto se contradice o tiene cifras que no cuadran. El propósito pregunta qué quiere lograr el emisor y si lo logra con razones o solo con presión.",
        "Un juicio bien hecho tiene tres partes: una afirmación («el texto es medianamente confiable»), una razón y una evidencia citada del texto. Así, otra persona puede revisar tu juicio y estar de acuerdo o no.",
    ],
    vocab=[("evaluar", "emitir un juicio fundamentado con razones"), ("criterio", "aspecto que se usa para juzgar algo"), ("evidencia", "dato o cita del texto que respalda un juicio"), ("fundamentar", "apoyar una idea con razones y evidencias")],
    worked=[
        ("Aplicar un criterio", "Frase (inventada): «Me atendieron en 20 minutos».", ["Pregunto si se puede comprobar: sí, con un registro de atención.", "Es un dato verificable, aunque la persona no muestra la prueba."], "Cumple en parte el criterio de veracidad"),
        ("Fundamentar un juicio", "Frase (inventada): «Es el mejor taller del mundo».", ["Afirmación: es una exageración.", "Razón: no se puede comprobar «el mejor del mundo».", "Evidencia: la frase no entrega ningún dato ni comparación."], "Juicio: no es un dato verificable"),
    ],
    mistakes=[("Evaluar solo con «me parece» o «no me gusta».", "Un juicio sin razones no se puede revisar.", "Usa los tres criterios y cita el texto."),
              ("Dar por falso un texto porque es entusiasta.", "El entusiasmo no es falsedad: hay que revisar los datos.", "Separa los datos comprobables de las exageraciones.")],
    T=[
        ("abc", "{F} ¿Qué datos de la reseña se pueden comprobar?", "El día, el tiempo de atención y el precio cobrado", "Que es el mejor taller del mundo", "Que nadie lo supera", "Una fecha, una duración y un precio son datos concretos."),
        ("ab", "{F} ¿«Es el mejor taller del mundo» es un dato comprobable?", "No, es una exageración sin comparación posible", "Sí, porque está escrito en la reseña", "No hay forma de medir cuál es el mejor del mundo."),
        ("=", "{F} Según la reseña, el taller cobró $35.000 y por teléfono dijeron lo mismo. ¿Cuánto es la diferencia entre lo dicho y lo cobrado?", "35000 - 35000", "Si el precio dicho y el cobrado coinciden, la resta da cero.", " pesos"),
        ("abc", "{F} ¿Qué criterio revisa si el texto se contradice?", "La consistencia", "El propósito", "La veracidad", "La consistencia revisa que no haya contradicciones."),
        ("abc", "{F} ¿Qué criterio pregunta qué quiere lograr quien escribe la reseña?", "El propósito", "La veracidad", "La consistencia", "El propósito es la intención del emisor."),
        ("abc", "{F} ¿Cuál es un propósito probable de la reseña?", "Recomendar el taller a otras personas", "Instruir cómo reparar un freno", "Criticar la municipalidad", "Cuenta una experiencia buena y la recomienda."),
        ("ab", "{F} ¿La reseña es consistente en el precio?", "Sí, porque el precio cobrado coincide con el que dijeron por teléfono", "No, porque cobraron más de lo dicho", "El texto indica que cobraron lo mismo que habían anunciado."),
        ("abc", "{F} ¿Qué evidencia respalda que el texto da algunos datos verificables?", "«Me atendieron en 20 minutos»", "«nadie lo supera»", "«el mejor taller del mundo»", "Una duración en minutos se puede comprobar con un registro."),
        ("abc", "¿Qué tres partes tiene un juicio bien fundamentado?", "Afirmación, razón y evidencia", "Saludo, despedida y firma", "Título, imagen y número", "Esas tres partes permiten que otro revise tu juicio."),
        ("ab", "Pablo escribe: «La reseña no me convence». ¿Qué le falta a su juicio?", "Razones y una cita del texto", "Más adjetivos", "Sin razones ni evidencia, nadie puede revisar su juicio."),
        ("abc", "{F} ¿Cuál de estos juicios está mejor fundamentado?", "«La reseña es en parte confiable: da fecha, tiempo y precio, pero exagera al decir que es el mejor del mundo»", "«Es buena porque sí»", "«Es mala porque es larga»", "Tiene afirmación, razones y evidencias del texto."),
        ("abc", "{F} ¿Qué dato sería útil pedir para verificar mejor la reseña?", "Quién escribe y si su experiencia puede comprobarse", "El color de la camioneta", "El número de palabras", "Conocer la fuente permite revisar la información."),
        ("ab", "{F} Si el texto dijera «cobraron $35.000, pero me dijeron $25.000 por teléfono», ¿qué cambiaría?", "Sería menos consistente en el precio, porque aparecerían dos cifras", "Sería más consistente", "Dos precios para lo mismo muestran una diferencia que habría que aclarar."),
    ],
    ctx=("abc", "Antes de dejar tu vehículo en un taller lees tres opiniones de ejemplo. La que más ayuda a decidir es la que dice:", "«Me atendieron en 30 minutos, cobraron lo anunciado y me mostraron la pieza»", "«Es una maravilla total»", "«No vayan nunca, qué horror»", "Da datos concretos y comprobables sobre la atención recibida."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué evalúa el criterio de veracidad?", "Si los datos se pueden comprobar y de dónde vienen", "Veracidad es qué tan cierta es la información."),
        ("En Lengua y Literatura de EPJA: ¿qué evalúa el criterio de consistencia?", "Si el texto se contradice o tiene cifras que no cuadran", "La consistencia revisa la coherencia entre datos."),
        ("En Lengua y Literatura de EPJA: ¿qué partes tiene un juicio fundamentado?", "Una afirmación, una razón y una evidencia del texto", "Esas partes permiten revisar el juicio.")],
    op=("Usa la pauta de evaluación sobre la reseña: {F} Escribe en tu cuaderno un juicio de tres frases: una afirmación sobre qué tan confiable es la reseña, una razón por criterio y una cita del texto como evidencia.",
        "La reseña es en parte confiable. Veracidad: da día, tiempo de atención y precio, pero no dice quién escribe; evidencia: «Cobraron $35.000». Consistencia: el precio coincide con lo dicho por teléfono. Propósito: recomienda el taller y exagera con «el mejor del mundo».",
        ["usa los tres criterios", "cita el texto como evidencia", "da una conclusión clara"],
        ["tres frases con una cita"],
        ["juzgar sin razones", "no citar el texto"],
        "Pregunta: «¿En qué parte del texto te apoyas?»."),
    reinforce="Elige una opinión que hayas leído sobre un comercio y señala un dato comprobable y una exageración.",
    extend="Escribe una reseña de tres líneas sobre un servicio inventado con al menos dos datos comprobables.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aplico el criterio de veracidad: comparo fuentes, reviso fechas y busco coincidencias entre textos distintos.",
    prior=["Reconozco fuentes y datos comprobables.", "Evalúo con tres criterios.", "Leo comunicados y noticias."],
    explain=[
        "Para revisar la veracidad de un dato, mira primero quién lo dice y cuándo lo dijo. Una institución que firma y fecha un comunicado se hace responsable de lo que informa; una publicación anónima no.",
        "Luego contrasta: busca si otras fuentes dicen lo mismo. Si un diario cita al comunicado de la institución y coincide con él, la información tiene más respaldo. Si un texto aislado difiere de las demás fuentes y no explica por qué, conviene tomarlo con cautela.",
        "Contrastar no es votar: no gana la versión más repetida. Gana la que se puede comprobar con su fuente original. Y la fecha importa: un aviso viejo puede haber quedado desactualizado.",
    ],
    vocab=[("contrastar", "comparar varias fuentes para ver si coinciden"), ("fuente original", "documento o persona de donde sale primero un dato"), ("desactualizado", "que ya no corresponde a la situación actual"), ("cita", "palabras o datos tomados de otra fuente")],
    worked=[
        ("Contrastar dos fuentes", "Fuente X: «La feria será el sábado, de 10:00 a 14:00». Fuente Y: «La feria será el sábado, de 10:00 a 14:00, según la sede».", ["Las dos dan la misma información.", "Y cita su fuente."], "Coinciden: hay más respaldo"),
        ("Revisar la fecha", "Aviso (inventado) fechado el 3 de marzo: «El plazo termina el 10».", ["Reviso en qué mes estamos.", "Si hoy es mayo, el aviso ya está desactualizado."], "Aviso desactualizado: hay que confirmar"),
    ],
    mistakes=[("Creer que la versión más repetida es la verdadera.", "Muchas personas pueden repetir un dato sin comprobarlo.", "Vuelve a la fuente original."),
              ("Olvidar mirar la fecha.", "Un dato correcto ayer puede haber cambiado.", "Anota la fecha de cada fuente antes de comparar.")],
    T=[
        ("abc", "{F} ¿Cuál es la fuente original del dato del corte de calle?", "El comunicado de la municipalidad de ejemplo", "La publicación del vecino sin nombre", "Cualquier persona que lo vio", "La nota del diario cita al comunicado."),
        ("ab", "{F} ¿Qué fuentes coinciden en el horario del corte?", "La Fuente 1 y la Fuente 3", "La Fuente 2 y la Fuente 3", "La nota del diario dice lo mismo que el comunicado."),
        ("{F} ¿En qué fecha fue publicado el comunicado de la Fuente 1? Escribe la fecha como en el texto, por ejemplo 2 de mayo.", "1 de octubre", "El comunicado está fechado el 1 de octubre."),
        ("abc", "{F} ¿Qué dice la Fuente 2 que no dicen las otras?", "Que el corte dura todo el día y también el domingo", "Que habrá un desfile", "Que hay desvío por Chacabuco", "Es la única que dice todo el día y el domingo."),
        ("=", "{F} Según la Fuente 1, el corte es de 14:00 a 18:00. ¿Cuántas horas dura?", "18 - 14", "Se resta la hora de inicio a la hora de término.", " horas"),
        ("abc", "{F} ¿Por qué la Fuente 2 es menos confiable?", "No se identifica y difiere de la fuente institucional sin explicar por qué", "Porque está escrita por un vecino", "Porque es más corta", "No se puede revisar quién la escribe."),
        ("ab", "{F} ¿Qué conviene hacer si una persona te dice que el corte es todo el día?", "Contrastarlo con el comunicado o con la municipalidad", "Creerle porque es vecino", "Contrastar con la fuente original evita difundir un error."),
        ("abc", "{F} ¿Qué dato adicional entrega la Fuente 1 útil para las personas conductoras?", "El desvío por calle Chacabuco", "El nombre del diario", "El número de personas", "Indica por dónde circular mientras la calle está cerrada."),
        ("abc", "{F} Si hoy es 7 de octubre, ¿cómo está el comunicado de la Fuente 1?", "Desactualizado, porque el desfile ya pasó", "Vigente, porque se publicó antes del desfile", "Falso, porque tiene fecha", "El desfile fue el sábado 5."),
        ("ab", "{F} ¿Qué diferencia hay entre «según la municipalidad» y «dicen que»?", "La primera identifica la fuente; la segunda no", "Las dos son iguales", "Nombrar la fuente permite comprobar el dato."),
        ("abc", "Un aviso dice: «La charla será el viernes». ¿Qué datos de veracidad le faltan?", "Quién lo emite y la fecha del aviso", "Un adjetivo valorativo", "Una pregunta al lector", "Sin emisor ni fecha no se puede verificar."),
        ("ab", "Marta dice: «Lo vi en cinco grupos distintos, así que es verdad». ¿Qué conviene responder?", "Repetirse no prueba nada: hay que ir a la fuente original", "Tiene razón: cinco grupos son suficientes", "Si todos copian el mismo mensaje, no hay más fuentes."),
        ("abc", "{F} ¿Qué conclusión sobre el horario del corte es mejor?", "El corte es el sábado 5, de 14:00 a 18:00, según la municipalidad", "El corte dura el sábado y el domingo todo el día", "No hay forma de saber nada", "La fuente institucional y el diario coinciden."),
    ],
    ctx=("abc", "Te avisan por un mensaje que mañana no habrá atención en tu oficina de trámites. El mensaje no tiene firma ni fecha. ¿Qué haces?", "Contrastarlo con el aviso oficial de la oficina antes de cambiar tu día", "Faltar sin avisar", "Reenviarlo a todos", "Un mensaje sin firma ni fecha debe verificarse con la fuente institucional."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué significa contrastar fuentes?", "Comparar varias fuentes para ver si coinciden", "Contrastar ayuda a ver qué dato tiene respaldo."),
        ("En Lengua y Literatura de EPJA: ¿qué es una fuente original?", "El documento o la persona de donde sale primero un dato", "Se vuelve a ella para comprobar lo que se dice."),
        ("En Lengua y Literatura de EPJA: ¿por qué importa la fecha de un texto?", "Porque un dato puede quedar desactualizado", "La fecha muestra si el dato sigue vigente.")],
    op=("Compara las tres fuentes: {F} Escribe en tu cuaderno una tabla con tres columnas, una por fuente, y filas: quién informa, qué dice del horario y si trae fecha. Luego escribe dos oraciones con tu conclusión sobre el corte y qué harías para confirmarla.",
        "Fuente 1: municipalidad, sábado 14:00 a 18:00, fecha 1 de octubre. Fuente 2: vecino anónimo, todo el día, sin fecha. Fuente 3: diario, 14:00 a 18:00, cita la municipalidad. Conclusión: es de 14:00 a 18:00; llamaría o iría a la oficina de la municipalidad para confirmar.",
        ["completa la tabla con datos de las fuentes", "concluye con razones", "propone cómo confirmar"],
        ["una tabla y dos oraciones"],
        ["elegir la fuente más repetida sin razón", "no proponer cómo confirmar"],
        "Pregunta: «¿Qué fuente puedes revisar en su origen?»."),
    reinforce="Compara dos mensajes que hablen del mismo tema y anota qué fuente cita cada uno.",
    extend="Escribe un comunicado breve y fechado para tu comunidad con quién informa, qué cambia y dónde consultar.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy reviso consistencia y propósito paso a paso y escribo un juicio fundamentado sobre una nota de prensa.",
    prior=["Uso tres criterios para evaluar.", "Reviso cifras y fuentes.", "Reconozco recursos lingüísticos."],
    explain=[
        "Evaluar una nota de prensa de una empresa exige mirar con cuidado, porque esa empresa tiene un interés: que su servicio se vea bien. Eso no vuelve falso el texto, pero obliga a revisar los datos con atención.",
        "Sigue estos pasos. Primero, identifica quién escribe y qué quiere lograr. Segundo, separa datos de opiniones. Tercero, revisa las cifras: ¿cuadran? Cuarto, anota los recursos de persuasión. Quinto, escribe un juicio con afirmación, razón y evidencia.",
        "Un dato como «de 60 a 75 viajes puntuales por cada 100» se verifica restando: 75 menos 60 es 15. Si el texto dice otra cifra para la mejora, hay una inconsistencia que debe aclararse.",
    ],
    vocab=[("nota de prensa", "texto que una institución envía para dar a conocer algo"), ("interés", "beneficio que obtiene quien escribe si el texto convence"), ("mejora", "aumento o avance respecto de antes"), ("inconsistencia", "contradicción o cifra que no cuadra")],
    worked=[
        ("Verificar una mejora", "Texto (inventado): «Pasamos de 40 a 55 atenciones por día y subimos 20».", ["Resto 55 menos 40: son 15.", "El texto dice 20: no cuadra."], "Inconsistencia: la mejora es de 15 y no de 20"),
        ("Fundamentar", "Juicio sobre el texto anterior.", ["Afirmación: es dudoso.", "Razón: la mejora real es de 15 y el texto dice 20.", "Evidencia: «subimos 20»."], "Juicio fundamentado con cita"),
    ],
    mistakes=[("Descartar el texto solo porque lo escribe una empresa.", "El interés del emisor invita a revisar, no a rechazar sin pruebas.", "Revisa los datos y decide con razones."),
              ("Restar al revés.", "Si restas 60 menos 75 no entiendes cuánto mejoró.", "Resta siempre el dato mayor menos el menor para calcular la mejora.")],
    T=[
        ("abc", "{F} ¿Quién es el emisor de la nota?", "La empresa Transportes del Valle de ejemplo", "Un pasajero", "La municipalidad", "La nota la firma la empresa que presta el servicio."),
        ("ab", "{F} ¿Cuál es el propósito implícito de la nota?", "Que la empresa se vea bien y que más personas usen sus buses", "Enseñar a leer horarios", "La nota resalta mejoras y se llama «favorito de las familias»."),
        ("=", "{F} ¿Cuántos viajes de cada 100 mejoraron realmente, restando 75 menos 60?", "75 - 60", "Se resta la cifra de antes a la de ahora.", " viajes"),
        ("abc", "{F} ¿Qué cifra dice la nota que mejoró la puntualidad?", "20 viajes por cada 100", "15 viajes por cada 100", "25 viajes por cada 100", "La nota afirma una mejora de 20 viajes."),
        ("abc", "{F} ¿Es consistente esa mejora con las dos cifras que da la nota?", "No, porque de 60 a 75 son 15 viajes más y no 20", "Sí, porque 75 menos 60 es 20", "No se puede calcular", "La resta 75 menos 60 da 15, no 20."),
        ("=", "{F} ¿Cuántos viajes más de los 15 reales dice la nota que mejoraron?", "20 - 15", "Se resta la mejora real a la mejora declarada.", " viajes"),
        ("ab", "{F} «Nuestro servicio es el favorito de las familias de la comuna», ¿es un dato o una opinión?", "Una opinión, porque no trae una medición ni una fuente", "Un dato, porque lo dice la empresa", "No muestra encuesta alguna que lo respalde."),
        ("abc", "{F} ¿Qué recurso persuasivo usa «Mejora histórica»?", "Un adjetivo valorativo que exagera la importancia", "Una cifra precisa", "Una fecha", "«Histórica» destaca sin dar una comparación."),
        ("abc", "{F} ¿Qué dato falta para verificar la mejora?", "Quién midió la puntualidad y en qué período", "El color de los buses", "El nombre de un conductor", "Sin fuente de la medición no se puede comprobar."),
        ("ab", "{F} ¿Qué juicio es mejor?", "La nota es dudosa: dice que la mejora es de 20, pero sus propias cifras dan 15", "La nota es buena porque es de una empresa", "El primero se apoya en cifras de la propia nota."),
        ("abc", "{F} Si la nota dijera que la mejora es de 15 viajes, ¿qué cambiaría?", "Mejoraría la consistencia, pero seguiría faltando la fuente de la medición", "Se volvería totalmente verificable", "Dejaría de tener propósito", "La consistencia mejora; la fuente sigue sin mencionarse."),
        ("abc", "{F} ¿A dónde dice la nota que pueden escribir para más información?", "A la oficina de la empresa", "A la municipalidad", "Al diario local", "La nota termina con esa indicación."),
        ("ab", "Una persona dice: «Si una empresa informa algo, no hace falta revisarlo». ¿Qué conviene responder?", "Que igual hay que revisar si sus cifras cuadran", "Que siempre dicen la verdad", "Cualquier emisor, incluida una empresa, puede equivocarse o exagerar."),
    ],
    ctx=("abc", "Un proveedor de ejemplo informa: «Subimos de 30 a 42 entregas por semana: 15 más». Revisa su cálculo. ¿Es consistente?", "No, porque de 30 a 42 son 12 entregas más", "Sí, porque son 15 más", "No se puede saber", "42 menos 30 da 12, no 15."),
    sc=[("En Lengua y Literatura de EPJA: ¿por qué conviene revisar con atención una nota de prensa de una empresa?", "Porque la empresa tiene interés en mostrarse bien", "El interés del emisor invita a verificar los datos."),
        ("En Lengua y Literatura de EPJA: ¿cómo se calcula una mejora entre dos cifras?", "Restando la menor a la mayor", "La resta muestra cuánto cambió entre las dos cifras."),
        ("En Lengua y Literatura de EPJA: ¿qué es una inconsistencia?", "Una contradicción o una cifra que no cuadra", "Muestra que algo del texto necesita aclararse.")],
    op=("Evalúa la nota con los cinco pasos: {F} Escribe en tu cuaderno un juicio de cuatro frases: quién escribe y qué busca, qué cifra no cuadra con su cálculo, una opinión que no tiene respaldo y tu conclusión final con una cita del texto.",
        "La empresa escribe para mostrar su servicio. Dice que la puntualidad mejoró en 20 viajes por cada 100, pero de 60 a 75 son 15. «El favorito de las familias» es una opinión sin respaldo. Conclusión: la nota es dudosa; pediría a la empresa cómo midió la puntualidad.",
        ["identifica emisor y propósito", "señala la cifra que no cuadra con el cálculo", "concluye con evidencia del texto"],
        ["cuatro frases y un cálculo"],
        ["juzgar sin calcular", "no citar el texto"],
        "Pregunta: «¿Cuánto mejoró en realidad y cómo lo calculaste?»."),
    reinforce="Revisa una cifra de mejora que veas en un aviso o en una noticia y comprueba si cuadra.",
    extend="Escribe una nota de prensa breve e inventada de un taller, con cifras que cuadren y una opinión claramente marcada como opinión.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo: puntúo dos textos con una pauta y decido cuál es más confiable.",
    prior=["Evalúo con veracidad, consistencia y propósito.", "Contrasto fuentes.", "Reviso sumas y restas."],
    explain=[
        "Una pauta ordena la evaluación. Cada criterio recibe un puntaje: 0 si no se cumple, 1 si se cumple en parte y 2 si se cumple bien. Al sumar, se ve qué texto tiene más respaldo, pero el puntaje no reemplaza tu razonamiento: siempre debes explicar por qué.",
        "Veracidad: ¿hay fuente, fecha y datos comprobables? Consistencia: ¿las cifras cuadran? Propósito: ¿el texto persuade con razones o solo con presión? Para cada criterio, busca una cita y justifica el puntaje.",
        "Dos textos sobre el mismo curso pueden ser muy distintos. Uno puede ser una opinión entusiasta; el otro, un informe con fecha, cifras y dónde consultar. Practicar con dos textos te ayuda a ver las diferencias con claridad.",
    ],
    vocab=[("pauta", "lista de criterios con puntajes para evaluar"), ("puntaje", "número que muestra cuánto se cumple un criterio"), ("informe", "texto que presenta datos organizados sobre un tema"), ("respaldo", "datos o fuentes que apoyan una afirmación")],
    worked=[
        ("Puntuar un criterio", "Texto (inventado): «Es el mejor curso». Criterio: veracidad.", ["No trae fecha ni fuente.", "No hay dato comprobable."], "Puntaje 0 en veracidad"),
        ("Sumar la pauta", "Veracidad 2, consistencia 2 y propósito 1.", ["Sumo: 2 + 2 + 1.", "Obtengo 5 de 6."], "Puntaje total: 5 de 6"),
    ],
    mistakes=[("Poner puntajes sin explicar.", "Un número sin razones no se puede revisar.", "Escribe una razón y una cita para cada puntaje."),
              ("Confundir lo largo con lo confiable.", "Un texto largo puede no tener datos comprobables.", "Revisa los datos, no el largo.")],
    T=[
        ("=", "{F} Según el Texto 2, se inscribieron 40 personas y lo terminaron 32. ¿Cuántas personas no lo terminaron?", "40 - 32", "Se resta quienes terminaron a quienes se inscribieron.", " personas"),
        ("=", "{F} Cada persona asistió a 2 clases por semana durante 8 semanas. ¿A cuántas clases asistió cada persona?", "2 * 8", "Se multiplican las clases semanales por las semanas.", " clases"),
        ("abc", "{F} ¿Qué texto trae fecha y dónde consultar?", "El Texto 2, el informe del centro", "El Texto 1, la publicación", "Ninguno de los dos", "El Texto 2 trae fecha y dónde conseguir el informe."),
        ("abc", "{F} ¿Qué afirmación del Texto 1 es poco creíble?", "«Aprendí todo en una semana»", "«Inscríbanse ya»", "«Es un curso»", "Aprender todo en una semana contrasta con las 8 semanas del informe."),
        ("ab", "{F} ¿El Texto 1 es consistente con el Texto 2 en cuanto a la duración del curso?", "No: dice que se aprendió todo en una semana y el curso duró 8", "Sí: los dos hablan de la misma duración", "La publicación y el informe dan duraciones muy distintas."),
        ("abc", "{F} ¿Qué puntaje daría a la veracidad del Texto 2, de 0 a 2, si trae fecha, cifras y dónde consultar el informe completo?", "2, porque trae datos comprobables y dónde consultar", "0, porque no tiene firma", "No se puede puntuar", "Trae fecha, cifras y un lugar donde revisar el informe."),
        ("abc", "{F} ¿Qué puntaje daría a la veracidad del Texto 1, de 0 a 2?", "0, porque no trae datos ni fuente", "2, porque está escrito con emoción", "1, porque es largo", "No tiene fecha, fuente ni cifras."),
        ("=", "{F} Si el Texto 2 recibe 2 en veracidad, 2 en consistencia y 1 en propósito, ¿cuántos puntos suma?", "2 + 2 + 1", "Se suman los tres puntajes de la pauta.", " puntos"),
        ("=", "{F} Si el Texto 1 recibe 0 en veracidad, 0 en consistencia y 1 en propósito, ¿cuántos puntos suma?", "0 + 0 + 1", "Se suman los tres puntajes de la pauta.", " puntos"),
        ("ab", "{F} ¿Qué texto tiene más respaldo según la pauta?", "El Texto 2, porque suma más puntos y trae datos que se pueden revisar", "El Texto 1, porque tiene más entusiasmo", "La suma y las razones apuntan al informe del centro."),
        ("abc", "{F} ¿Qué recurso persuasivo domina en el Texto 1?", "Exageración y urgencia con «Inscríbanse ya»", "Cifras y fuentes", "Un cuadro de datos", "No trae respaldo y presiona a inscribirse."),
        ("ab", "Una persona dice: «El puntaje 5 de 6 demuestra que el texto es perfecto». ¿Qué responder?", "Que el puntaje apoya, pero igual hay que explicar los criterios y revisar los datos", "Que sí, que es perfecto", "El puntaje resume, pero no reemplaza las razones."),
        ("abc", "{F} Antes de inscribirte en el curso, ¿qué harías con el informe del Texto 2?", "Pedir el informe completo en la oficina del centro", "Ignorarlo por ser largo", "Darlo por cierto sin leerlo", "El texto dice que el informe completo está disponible allí."),
    ],
    ctx=("abc", "Dos personas te cuentan de un taller de ejemplo. Una dice «es genial». Otra trae un papel con fechas, horas y valor del taller. ¿Con cuál comenzarías a decidir?", "Con el papel con datos que puedes comprobar", "Con la que habla más fuerte", "Con la más entusiasta", "Los datos comprobables dan más respaldo que una opinión."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué indica un puntaje 0 en veracidad?", "Que el texto no trae datos ni fuentes comprobables", "El puntaje se justifica con razones del texto."),
        ("En Lengua y Literatura de EPJA: ¿qué es un informe?", "Un texto que presenta datos organizados sobre un tema", "Un informe entrega datos con fuente."),
        ("En Lengua y Literatura de EPJA: ¿puede un puntaje reemplazar tu razonamiento?", "No: siempre debes explicar tus razones", "El puntaje resume, las razones lo sostienen.")],
    op=("Evalúa los dos textos con la pauta: {F} Escribe en tu cuaderno una tabla con los criterios de veracidad, consistencia y propósito para cada texto, con puntaje de 0 a 2 y una razón corta. Termina con una frase que diga cuál es más confiable.",
        "Texto 1: veracidad 0 (sin datos), consistencia 0 (dice una semana y el curso duró 8), propósito 1 (invita a inscribirse). Texto 2: veracidad 2 (fecha, cifras, dónde consultar), consistencia 2 (32 de 40 terminaron), propósito 1 (informa, con interés del centro). Es más confiable el Texto 2.",
        ["puntúa los tres criterios en ambos textos", "da una razón corta para cada puntaje", "concluye con una frase clara"],
        ["una tabla con seis puntajes y una conclusión"],
        ["poner puntajes sin razones", "concluir sin sumar"],
        "Pregunta: «¿En qué parte del texto te apoyaste para cada puntaje?»."),
    reinforce="Aplica la pauta de puntajes a un aviso que hayas leído esta semana.",
    extend="Crea una pauta propia de cuatro criterios para evaluar un volante de un taller de tu barrio.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy evalúo textos de salud de ejemplo, sin dar consejos clínicos, para saber cuándo confiar y cuándo consultar a una institución.",
    prior=["Evalúo con tres criterios.", "Contrasto fuentes.", "Reconozco promesas exageradas."],
    explain=[
        "Los textos sobre salud circulan mucho en grupos y cadenas. Este cuaderno no da consejos de salud: solo enseña a evaluar cómo está escrito un texto. Para decisiones de salud, consulta siempre a una persona profesional o al consultorio.",
        "Una promesa absoluta («cura cualquier enfermedad», «100 % garantizado») es una señal de alerta, porque en la vida real casi nada garantiza resultados totales. Otras señales: una autoridad sin nombre («un doctor de otro país»), la presión por compartir y la falta de fuente y fecha.",
        "Un comunicado de un consultorio, en cambio, suele dar fecha, horario, requisitos y dónde consultar. Eso permite verificarlo yendo al lugar. Esa es la diferencia entre un texto que pide confianza y uno que ofrece forma de comprobar.",
    ],
    vocab=[("promesa absoluta", "afirmación que asegura un resultado total, sin excepciones"), ("señal de alerta", "pista que invita a revisar con más cuidado"), ("garantizado", "asegurado por completo"), ("consultorio", "centro de atención de salud de nivel básico")],
    worked=[
        ("Detectar una señal de alerta", "Mensaje (inventado): «Remedio milagroso, resultados 100 % garantizados».", ["Promete un resultado total.", "No trae fuente ni fecha."], "Señales: promesa absoluta y falta de fuente"),
        ("Verificar un comunicado", "Comunicado (inventado): «Vacunación infantil el lunes 7, de 9:00 a 12:00 en el consultorio. Consultas al mesón».", ["Trae fecha, hora y lugar.", "Se puede consultar en el mesón."], "Se puede verificar en el consultorio"),
    ],
    mistakes=[("Seguir una receta de salud porque «lo dijo un doctor» sin nombre.", "Una autoridad sin nombre no se puede revisar.", "Consulta a una persona profesional o al consultorio."),
              ("Compartir un mensaje de salud sin verificarlo.", "Puede difundir un error que afecte a otras personas.", "Verifica con la institución antes de compartir.")],
    T=[
        ("abc", "{F} ¿Qué promesa absoluta aparece en el Mensaje A?", "«Cura cualquier enfermedad. 100 % garantizado»", "«Lo comprobó un doctor»", "«Si no lo compartes»", "Asegura un resultado total, sin excepciones."),
        ("ab", "{F} ¿Se puede verificar «lo comprobó un doctor de otro país»?", "No, porque no dice quién es ni dónde lo comprobó", "Sí, porque dice que fue un doctor", "Una autoridad sin nombre ni estudio no se puede revisar."),
        ("abc", "{F} ¿Qué recurso del Mensaje A busca presionar para que lo compartas?", "«Si no lo compartes, no te sirve»", "«Jarabe casero»", "«De otro país»", "Condiciona el supuesto beneficio a compartirlo."),
        ("abc", "{F} ¿Quién emite el Mensaje B?", "El consultorio de ejemplo", "Un doctor de otro país", "Una persona anónima", "El texto lo presenta como comunicado del consultorio."),
        ("{F} ¿En qué fecha está fechado el Mensaje B? Escribe la fecha como en el texto, por ejemplo 2 de mayo.", "3 de octubre", "El Mensaje B está fechado el 3 de octubre."),
        ("=", "{F} El control de salud del Mensaje B es de 9:00 a 13:00. ¿Cuántas horas dura la atención?", "13 - 9", "Se resta la hora de inicio a la hora de término.", " horas"),
        ("abc", "{F} ¿Qué dato del Mensaje B permite comprobarlo?", "Que se puede consultar en el mesón del consultorio", "Que es gratuito", "Que dice «control»", "Se puede ir al consultorio y preguntar."),
        ("ab", "{F} ¿Cuál mensaje es más consistente y verificable?", "El Mensaje B, porque trae fecha, hora, lugar y requisitos", "El Mensaje A, porque promete más", "El B da datos concretos; el A solo promete."),
        ("abc", "{F} ¿Qué propósito implícito tiene el Mensaje A?", "Que se difunda el mensaje y se use el jarabe", "Informar un horario de atención", "Dar instrucciones médicas verificadas", "Busca difusión y confianza en un producto sin respaldo."),
        ("ab", "{F} Una persona te pregunta si debe tomar el jarabe. ¿Qué respuesta es adecuada?", "Que consulte a una persona profesional de salud o al consultorio", "Que lo tome, porque está garantizado", "Las decisiones de salud se consultan con quien tiene formación para orientar."),
        ("abc", "{F} ¿Qué requisito pide el Mensaje B?", "Llevar la cédula", "Llevar una receta", "Llevar dinero", "El texto dice «Traiga su cédula»."),
        ("abc", "Un cartel dice: «Producto natural, sin efectos secundarios, cura todo». ¿Qué señal de alerta tiene?", "Una promesa absoluta sin fuente", "Una cifra con fecha", "Un lugar de consulta", "«Cura todo» y «sin efectos» son promesas totales."),
        ("ab", "Antes de reenviar un mensaje de salud, ¿qué es lo más prudente?", "Confirmarlo con el consultorio o una fuente oficial", "Reenviarlo si suena preocupante", "Reenviar sin verificar puede difundir un error."),
    ],
    ctx=("abc", "Una vecina te muestra un mensaje de cadena que asegura una «cura total» sin fuente. ¿Qué le dices de forma respetuosa?", "Que conviene consultar en el consultorio antes de creerlo o compartirlo", "Que lo comparta de inmediato", "Que nunca lea mensajes de nadie", "Consultar a la institución es la forma segura de verificar."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué es una promesa absoluta?", "Una afirmación que asegura un resultado total", "Es una señal de alerta que exige verificar."),
        ("En Lengua y Literatura de EPJA: ¿qué hacer ante un mensaje de salud sin fuente?", "Consultar al consultorio o a una persona profesional antes de compartirlo", "Verificar evita difundir errores que afecten a otras personas."),
        ("En Lengua y Literatura de EPJA: ¿qué hace verificable a un comunicado de salud?", "Que traiga fecha, hora, lugar y dónde consultar", "Esos datos permiten comprobarlo en el mismo consultorio.")],
    op=("Evalúa los dos mensajes: {F} Escribe en tu cuaderno una evaluación de cada uno con los tres criterios, un puntaje de 0 a 2 y una cita como evidencia. Termina con una frase que diga qué harías con cada mensaje.",
        "Mensaje A: veracidad 0 («un doctor de otro país» sin nombre); consistencia 1 (no se contradice, pero promete todo); propósito 0 (presiona con «si no lo compartes»). Mensaje B: veracidad 2 (fecha y lugar); consistencia 2; propósito 2 (informa un control). A: no lo compartiría y consultaría. B: lo tendría en cuenta y confirmaría en el mesón.",
        ["puntúa los tres criterios en ambos mensajes", "cita una evidencia por mensaje", "dice qué haría con cada mensaje"],
        ["una evaluación de seis puntajes y dos decisiones"],
        ["dar consejo de salud propio", "puntuar sin citar el texto"],
        "Pregunta: «¿Qué dato permite comprobar cada mensaje?»."),
    reinforce="Revisa un mensaje de cadena que hayas recibido y anota qué le falta para ser verificable.",
    extend="Escribe un comunicado de ejemplo para un centro de salud de tu comunidad con fecha, hora, lugar y dónde consultar.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo que he logrado y escribo un juicio completo y argumentado sobre una nota, con pasos para seguir verificando.",
    prior=["Uso tres criterios y una pauta.", "Contrasto fuentes.", "Fundamento juicios con una cita."],
    explain=[
        "Evaluar un texto de principio a fin reúne todo lo aprendido: situación comunicativa, hechos y opiniones, fuentes, consistencia, recursos y propósito. El resultado es un juicio fundamentado que cualquier persona podría revisar.",
        "Un juicio completo tiene cuatro partes: una afirmación clara (por ejemplo, «la nota es dudosa»), razones por cada criterio, evidencias citadas del texto y una decisión sobre qué hacer después, como pedir un dato o consultar la fuente oficial.",
        "Al cerrar, revisa lo logrado: qué criterios aplicas con seguridad y cuáles necesitas practicar. Decidir tus próximos pasos, y con quién practicar, forma parte del aprendizaje.",
    ],
    vocab=[("juicio completo", "evaluación con afirmación, razones, evidencias y decisión"), ("desglose", "detalle de las partes de un total"), ("participantes", "personas o grupos que toman parte en algo"), ("próximo paso", "acción que decides hacer después")],
    worked=[
        ("Detectar una inconsistencia", "Texto (inventado): «Se inscribieron 100 personas y 150 asistieron».", ["Comparo: 150 es más que 100.", "No pueden asistir más personas que las inscritas, salvo que se explique."], "Inconsistencia: asistentes mayores que inscritas"),
        ("Cerrar con una decisión", "Juicio sobre el texto anterior.", ["Afirmación: es dudoso.", "Evidencia: 150 asistentes frente a 100 inscritas.", "Decisión: pedir el dato a la organización."], "Juicio con decisión"),
    ],
    mistakes=[("Terminar la evaluación sin decidir nada.", "Un juicio sin decisión queda incompleto.", "Escribe qué harás: pedir un dato, contrastar o consultar."),
              ("Mezclar tu opinión con la evaluación del texto.", "Evaluar es apoyarse en el texto, no en lo que preferirías que dijera.", "Cita el texto y separa tu opinión.")],
    T=[
        ("abc", "{F} ¿Quién emite la nota?", "El boletín «El Pregonero» de ejemplo, citando al centro de empleo", "Una persona que no se identifica", "Una empresa participante", "El boletín publica y atribuye datos a la organización."),
        ("{F} ¿Cuántas personas se inscribieron a la feria según la nota? Escribe solo el número.", "1.200", "La nota dice «Se inscribieron 1.200 personas»."),
        ("=", "{F} La nota dice que más de 2.000 personas consiguieron trabajo y que se inscribieron 1.200. ¿Cuántas más que las inscritas serían, con 2.000?", "2000 - 1200", "Se resta la cifra de inscritas a la cifra de quienes consiguieron trabajo.", " personas"),
        ("abc", "{F} ¿Qué se puede afirmar con esas dos cifras?", "Hay una inconsistencia, porque no pueden conseguir trabajo más personas que las inscritas", "Que la feria fue un éxito", "Que hubo pocas empresas", "Dos cifras que no pueden ser ciertas a la vez muestran una inconsistencia."),
        ("abc", "{F} ¿Qué expresión es una opinión del texto?", "«fue la mejor feria de la historia de la comuna»", "«Se inscribieron 1.200 personas»", "«hubo 30 empresas participantes»", "«La mejor» es un juicio, no un dato."),
        ("ab", "{F} ¿Qué recurso aparece en «Éxito rotundo»?", "Un adjetivo valorativo que exagera", "Una cifra comprobable", "La palabra «rotundo» califica el éxito sin dar datos."),
        ("abc", "{F} ¿Quién informó que hubo 30 empresas participantes?", "La organización, el centro de empleo de ejemplo", "Un vecino", "El diario nacional", "La nota lo atribuye al centro de empleo."),
        ("abc", "{F} ¿Cuál es el propósito implícito de la nota?", "Dar una imagen de éxito de la feria laboral", "Instruir a las personas sobre cómo postular", "Pedir una opinión", "Destaca el éxito con cifras y adjetivos."),
        ("abc", "{F} ¿Cuál es la mejor decisión para seguir verificando?", "Pedir al centro de empleo cuántas personas consiguieron trabajo y cómo lo midieron", "Dar por cierta la cifra mayor", "No leer más", "Se pide la cifra a la fuente original."),
        ("ab", "{F} ¿Cuál de estos juicios está mejor fundamentado?", "La nota es dudosa: dice que más de 2.000 personas consiguieron trabajo, pero se inscribieron 1.200", "La nota es mala porque exagera", "El primero cita cifras del texto y da una razón."),
        ("abc", "{F} ¿Cuántas empresas dice la nota que hubo?", "30", "20", "12", "El texto dice «30 empresas participantes»."),
        ("abc", "Al cerrar esta unidad, una persona dice que le cuesta verificar fuentes. ¿Qué próximo paso es más concreto?", "Elegir dos mensajes de esta semana y comprobar quién los emite y de dónde salen sus datos", "No leer más mensajes", "Aprender de memoria la pauta", "Una práctica concreta fortalece la habilidad."),
        ("ab", "Camila dice: «Mi evaluación está completa porque dije que el texto me parece malo». ¿Qué le falta?", "Razones, evidencias y una decisión", "Un título más largo", "Sin razones, evidencia ni decisión, el juicio queda incompleto."),
    ],
    ctx=("abc", "Una escuela de oficios de ejemplo informa: «Se inscribieron 80 personas; terminaron 100». Quieres saber qué dato pedir. ¿Qué conviene pedir?", "La cifra correcta de inscritas y de personas que terminaron", "El color del certificado", "El nombre del edificio", "Terminar más personas que las inscritas es inconsistente."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué partes tiene un juicio completo?", "Afirmación, razones, evidencias y decisión", "Incluye una decisión sobre qué hacer."),
        ("En Lengua y Literatura de EPJA: ¿qué hacer con una cifra que no cuadra?", "Pedir a la fuente original que la aclare", "La aclaración viene de quien emite el dato."),
        ("En Lengua y Literatura de EPJA: ¿para qué sirve revisar lo logrado al cerrar una unidad?", "Para ver qué dominas y qué practicar", "Revisar lo logrado permite decidir los próximos pasos.")],
    op=("Escribe tu juicio completo sobre la nota: {F} En tu cuaderno redacta seis frases: una afirmación, una razón por cada criterio (veracidad, consistencia y propósito), una cita del texto y una decisión sobre qué dato pedirías. Después escribe qué criterio te cuesta más y cómo lo practicarás.",
        "La nota es dudosa. Veracidad: la cifra de trabajos no cita una medición. Consistencia: dice «más de 2.000 personas consiguieron trabajo» y «se inscribieron 1.200». Propósito: mostrar éxito, con «la mejor feria de la historia». Pediría al centro de empleo la cifra exacta. Me cuesta contrastar fuentes; practicaré comparando dos noticias esta semana.",
        ["cubre los tres criterios con razones", "cita una evidencia del texto", "incluye una decisión y un plan de práctica"],
        ["seis frases y un plan de práctica"],
        ["no incluir una decisión", "no citar el texto"],
        "Pregunta: «¿Qué dato pedirías y a quién?»."),
    reinforce="Elige un texto de esta semana y escribe un juicio de tres frases con una cita.",
    extend="Compara en dos párrafos cómo cambiaría tu juicio de la nota si el centro de empleo confirmara que 900 personas consiguieron trabajo.",
)
