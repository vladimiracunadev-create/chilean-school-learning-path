"""Lenguaje y Comunicación EPJA Nivel 2, módulo 1 (parte 4): OAD-04, comunicar las preferencias literarias (oral y escrita). Los guiones son inventados y se leen en papel; no hay audio ni presentación real."""
from __future__ import annotations

from epja_leco_nb2_common import build

O = "EPJA-LECO-NB2-OAD-04"

F1 = ("Guion oral de ejemplo (inventado): «Buenas tardes. Quiero recomendarles el cuento «La olla del sábado». Es breve y cuenta cómo un grupo de vecinos organiza un almuerzo. "
      "Me gustó porque muestra que, cuando cada persona trae algo, alcanza para todos. Se los recomiendo si buscan una lectura tranquila. Gracias.»")

F2 = ("Ficha del cuento (inventada), «El farol de la esquina»: Dora, vecina de un pasaje, nota que el farol de su esquina lleva varios días apagado. Reúne firmas de sus vecinos y las lleva a la municipalidad. Una semana después, un equipo repara el farol. "
      "Guion A: «Les recomiendo «El farol de la esquina». Cuenta que Dora reúne firmas para que arreglen un farol. Me gustó porque muestra que los vecinos pueden lograr cambios si se organizan.» "
      "Guion B: «Les recomiendo «El farol de la esquina». Cuenta que Dora es alcaldesa y que arregla el farol en un mes. Me gustó porque es muy bonito.»")

F3 = ("Cuento (inventado), «La feria sin luz»: Una noche, la feria quedó sin luz. Cada vendedor trajo una linterna y la puso sobre su mesa. La feria brilló como nunca y nadie se fue sin comprar. "
      "Notas desordenadas para la recomendación: (a) Se los recomiendo para leer en grupo. (b) Quiero recomendarles «La feria sin luz». (c) Me gustó porque muestra cómo cada persona aporta una luz. (d) Cuenta que una noche la feria se queda sin luz y los vendedores usan linternas.")

F4 = ("Borrador de guion (inventado), sobre el cuento «La feria sin luz»: «Les recomiendo el cuento «La feria sin luz». Es un cuento muy bueno. Cuenta que una noche la feria quedo sin luz. "
      "Los vendedores trajeron linternas. Es muy bueno y muy lindo, y tiene un final muy bueno.»")

F5 = ("Poema (inventado), «Pan caliente»: Pan caliente en la mañana, / vapor en la ventana; / la calle huele a hogar / y el día empieza a cantar.")

F6 = ("Guion completo (inventado): «Hola a todas y a todos. Quiero recomendarles el cuento «Las llaves del sábado». Cuenta cómo Mario, que cuida una sede vecinal, pierde las llaves y pide ayuda a los vecinos. "
      "Entre todos las encuentran en el patio. Me gustó porque muestra que pedir ayuda no es debilidad: «Solos no las habríamos encontrado», dice Mario. "
      "Se lo recomiendo a quien quiera leer una historia breve y cálida. Muchas gracias.» "
      "Pauta de ejemplo: cinco criterios (saludo y título, resumen claro, razón con dato, cita correcta, cierre) y 2 puntos por criterio cumplido.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy descubro que ya recomiendo cosas oralmente y aprendo a recomendar un cuento ante un grupo.",
    prior=["Sé justificar una preferencia.", "He recomendado algo a alguien.", "Puedo resumir un cuento."],
    explain=[
        "Recomendar es algo que haces a menudo: sugieres un lugar, un trámite, una receta. Comunicar una preferencia literaria es parecido: le cuentas a otras personas qué cuento o poema te gustó y por qué.",
        "Cuando hablas ante un grupo, piensa en la audiencia, que son las personas que te escuchan, y en tu propósito, que es lo que quieres lograr: aquí, que quieran leer el texto. Un guion corto ayuda: saludo, título, de qué trata, por qué te gustó y un cierre.",
        "Al hablar, usa frases cortas, una voz clara y pausas entre las ideas. No cuentes el final del cuento: así dejas algo por descubrir. Y no necesitas memorizar: unas notas con las ideas clave bastan.",
    ],
    vocab=[("audiencia", "personas que escuchan"), ("propósito", "lo que quieres lograr al hablar"), ("guion", "texto breve que ordena lo que se va a decir"), ("pausa", "momento de silencio breve entre ideas")],
    worked=[
        ("Partes del guion", "Guion (inventado): «Buenas noches. Quiero recomendarles el poema «Domingo». Es corto y habla de una tarde tranquila. Me gustó porque transmite calma. Se lo recomiendo a quien quiera un momento de pausa. Gracias».", ["Saludo: «Buenas noches».", "Título: «Domingo».", "Resumen: «Es corto y habla de una tarde tranquila».", "Razón: «Me gustó porque transmite calma».", "Cierre: «Se lo recomiendo...» y «Gracias»."], "Cinco partes: saludo, título, resumen, razón y cierre"),
        ("Frases cortas con pausas", "Frase larga: «Quiero recomendarles un cuento que me gustó mucho porque trata de vecinos que se juntan y comparten lo que tienen en una olla y así alcanza para todos».", ["Parto la frase en ideas cortas.", "Hago una pausa después de cada una."], "Quiero recomendarles un cuento. Trata de vecinos que comparten. Me gustó porque alcanza para todos."),
    ],
    mistakes=[("Leer el guion de corrido, sin pausas.", "La audiencia no alcanza a entender.", "Haz una pausa después de cada idea."),
              ("Contar todo el cuento, incluido el final.", "Quita el interés de leerlo.", "Resume y deja el final sin contar.")],
    T=[
        ("abc", "{F} ¿Cuál es el título del cuento que se recomienda?", "«La olla del sábado»", "«Buenas tardes»", "«Una lectura tranquila»", "El título aparece entre comillas, después de «recomendarles el cuento»."),
        ("ab", "{F} ¿Con qué frase empieza el guion?", "«Buenas tardes»", "«Gracias»", "El guion saluda al comenzar y agradece al terminar."),
        ("{F} ¿Cuántas razones da la persona para su preferencia? Escribe el número.", "1", "Da una razón: muestra que, cuando cada persona trae algo, alcanza para todos."),
        ("abc", "En Lenguaje: ¿qué es la audiencia en una presentación oral?", "Las personas que escuchan", "El texto que se lee", "El tema del texto", "La audiencia es quien recibe lo que dices."),
        ("ab", "{F} ¿Qué parte del guion resume el cuento?", "«Es breve y cuenta cómo un grupo de vecinos organiza un almuerzo»", "«Gracias»", "Esa frase dice de qué trata el cuento."),
        ("abc", "{F} ¿Qué dice el cierre del guion?", "Que lo recomienda a quien busque una lectura tranquila y agradece", "Que el cuento es largo", "Que el cuento termina con un almuerzo", "El cierre del guion recomienda la lectura a quien busque algo tranquilo y agradece."),
        ("abc", "Antes de hablar frente a un grupo anotas ideas clave. ¿Cuál es una buena nota para este guion?", "Título; qué cuenta; por qué me gustó; a quién lo recomiendo", "Todo el texto palabra por palabra", "Solo el saludo", "Las ideas clave ordenan lo que dirás."),
        ("abc", "Vas a recomendar un cuento a un grupo de lectura. ¿Qué voz conviene?", "Clara y tranquila, con pausas entre las ideas", "Muy rápida para terminar pronto", "En susurro", "Una voz clara y con pausas ayuda a entender."),
        ("abc", "¿Qué conviene no hacer al recomendar un cuento?", "Contar el final completo", "Decir el título", "Dar una razón", "Contar el final quita las ganas de leerlo."),
        ("ab", "Luisa lee su guion de corrido, sin pausas. ¿Qué le conviene hacer?", "Hacer pausas entre las ideas para que la audiencia comprenda", "Hablar más rápido para ganar tiempo", "La pausa da tiempo para entender cada idea."),
        ("abc", "{F} ¿Por qué el guion usa frases cortas?", "Porque se entienden mejor al escucharlas", "Porque así dura más", "Porque no tiene razones", "Al escuchar, las frases cortas son más fáciles de seguir."),
        ("abc", "{F} Otra persona dice: «Les recomiendo el cuento porque es bueno.» ¿Qué le falta comparada con el guion?", "Un dato del cuento que apoye la razón", "Un saludo más largo", "Un cuento más largo", "Una razón necesita un dato que la respalde."),
        ("ab", "Tienes solo un minuto para recomendar. ¿Qué parte puedes acortar sin perder el sentido?", "El resumen, dejándolo en una oración", "La razón y el título", "El título y la razón son lo esencial."),
    ],
    ctx=("abc", "En una reunión te dan un minuto para recomendar algo que leíste. ¿Qué haces?", "Digo el título, qué cuenta, por qué lo recomiendo y cierro", "Cuento todo el cuento", "No digo nada", "Un guion breve cabe en un minuto."),
    sc=[("En Lenguaje: ¿qué es el propósito al hablar?", "Lo que quiero lograr con lo que digo", "El propósito orienta qué incluyo en el guion, por ejemplo qué datos y qué razón doy."),
        ("¿Qué partes tiene un guion de recomendación?", "Saludo, título, resumen, razón y cierre", "Esas cinco partes ordenan lo que se dirá y ayudan a que la audiencia siga la idea."),
        ("¿Qué no debo contar?", "El final del cuento", "Si no cuento el final, la audiencia conserva el interés por leerlo.")],
    op=("Con el guion: {F} Escribe tu propio guion de recomendación para otro cuento o poema que conozcas, con saludo, título, qué cuenta, una razón y un cierre. Dilo después en voz alta.",
        "Buenas tardes. Quiero recomendarles el cuento «El farol de la esquina». Cuenta cómo una vecina reúne firmas. Me gustó porque muestra que organizarse sirve. Se los recomiendo para leer en grupo. Gracias.",
        ["cinco partes", "razón con dato", "no cuenta el final", "frases cortas"],
        ["un guion de cinco partes y una lectura en voz alta"],
        ["contar el final", "no dar razón"],
        "Pregunta: «¿Qué quieres que haga la audiencia después?»."),
    reinforce="Recomienda en voz alta, en una oración, algo que leíste.",
    extend="Escribe dos guiones breves para dos audiencias distintas y di qué cambió.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo a ordenar las ideas de una recomendación, a usar información fidedigna y a elegir palabras precisas.",
    prior=["Conozco las partes del guion.", "Sé que hay que justificar.", "Reconozco sinónimos."],
    explain=[
        "Al comunicar una preferencia, la información debe ser fidedigna: son datos correctos que se pueden comprobar en el texto. Si dices que un personaje es alcaldesa y el cuento no lo dice, inventas, y quien escucha puede confundirse.",
        "Las ideas se ordenan en una progresión: primero presentas el texto, luego cuentas de qué trata, después das la razón y al final cierras. Ese orden ayuda a que la audiencia te siga sin perderse.",
        "También conviene usar palabras precisas. En lugar de decir «es muy bueno», di qué lo hace valioso: «es claro», «es esperanzador», «muestra cómo se organiza un barrio». Y puedes usar sinónimos para no repetir.",
    ],
    vocab=[("fidedigno", "digno de confianza, que se puede comprobar"), ("progresión", "orden claro de las ideas, una tras otra"), ("preciso", "que dice exactamente lo que quiere decir"), ("dato", "información concreta del texto")],
    worked=[
        ("Revisar un dato", "Ficha (inventada): «Don Aníbal, vecino de un edificio, arregla el portón del patio con herramientas prestadas». Guion C: «Cuenta que don Aníbal es gasfíter y arregla el portón en una hora».", ["La ficha no dice que don Aníbal sea gasfíter ni que tarde una hora.", "Esos datos no están en el texto."], "El guion C tiene datos que no son fidedignos"),
        ("Ordenar ideas", "Recomendación del cuento de don Aníbal.", ["Presentar: «Les recomiendo...».", "Contar: don Aníbal arregla el portón con herramientas prestadas.", "Razón: muestra que compartir herramientas ayuda a todos.", "Cerrar con una recomendación."], "Presentar, contar, razón y cierre"),
    ],
    mistakes=[("Decir datos de memoria sin comprobarlos.", "Puedes dar información falsa sin querer.", "Vuelve al texto y confirma cada dato."),
              ("Usar «muy bueno» y «muy lindo» como razón.", "No dicen qué del texto es bueno.", "Di qué hace valioso al texto con un dato.")],
    T=[
        ("abc", "{F} ¿Qué hace Dora para lograr que arreglen el farol?", "Reúne firmas de sus vecinos y las lleva a la municipalidad", "Arregla el farol ella misma", "Llama a la prensa", "La ficha dice que reúne firmas y las lleva a la municipalidad."),
        ("ab", "{F} ¿Cuánto tarda el equipo en reparar el farol?", "Una semana", "Un mes", "La ficha dice «una semana después»."),
        ("{F} ¿Qué guion, A o B, entrega información correcta? Escribe la letra.", "A", "El guion A concuerda con la ficha; el B inventa datos."),
        ("abc", "En Lenguaje: ¿qué es información fidedigna?", "Datos correctos que se pueden comprobar en el texto", "Datos que a mí me parecen", "Datos inventados que suenan bien", "Lo fidedigno es correcto y se puede comprobar volviendo al texto."),
        ("{F} ¿Qué palabra del guion B dice mal quién es Dora? Escribe la palabra.", "alcaldesa", "La ficha dice que Dora es vecina de un pasaje, no alcaldesa."),
        ("abc", "{F} ¿Qué razón da el guion A?", "Que los vecinos pueden lograr cambios si se organizan", "Que es muy bonito", "Que Dora es alcaldesa", "La razón del guion A se apoya en lo que ocurre."),
        ("abc", "¿Cuál es el orden correcto de ideas en una recomendación oral?", "Presentar el texto, contar de qué trata, dar la razón y cerrar", "Cerrar, dar la razón y presentar", "Dar la razón y saludar al final", "Es el orden de la progresión."),
        ("abc", "¿Qué expresión es más precisa que «un cuento muy bueno»?", "un cuento claro y esperanzador", "un cuento súper bueno", "un cuento muy muy lindo", "Dice con precisión qué hace valioso al cuento: es claro y esperanzador."),
        ("abc", "Antes de decir un dato en tu presentación, ¿qué haces?", "Compruebo que esté en el texto", "Lo digo de memoria", "Lo cambio un poco", "Comprobar en el texto evita decir datos falsos sin querer."),
        ("ab", "Pedro dice: «Para recomendar basta con decir que es lindo.» ¿Qué le falta?", "Una razón y datos correctos del texto", "Más adjetivos", "Una recomendación necesita justificación y datos."),
        ("abc", "{F} ¿Cuál de estas frases es fidedigna según la ficha?", "Dora lleva las firmas de sus vecinos a la municipalidad", "Dora lleva las firmas a la comisaría", "Dora pinta el farol con sus vecinos", "La ficha dice que Dora lleva las firmas a la municipalidad."),
        ("abc", "{F} ¿Cómo corregirías la segunda oración del guion B?", "Cuenta que Dora reúne firmas y que una semana después arreglan el farol", "Cuenta que Dora es vecina y que arregla el farol en un día", "Cuenta que el farol está apagado en otra ciudad", "La corrección coincide con la ficha."),
        ("ab", "{F} Si dijeras que Dora logró que arreglaran el farol sin ayuda de sus vecinos, ¿sería fidedigno?", "No: la ficha dice que reúne firmas de sus vecinos", "Sí: ella es la protagonista", "La ayuda de los vecinos aparece en el texto."),
    ],
    ctx=("abc", "Vas a recomendar un cuento y no recuerdas bien un dato. ¿Qué haces?", "Releo el cuento y confirmo el dato antes de decirlo", "Digo el dato que me parezca", "Omito toda la recomendación", "Comprobar en el texto evita errores."),
    sc=[("En Lenguaje: ¿qué significa «fidedigno»?", "Que se puede comprobar y es correcto", "Lo fidedigno se apoya en el texto y puede confirmarse en él."),
        ("¿Qué es una progresión de ideas?", "Un orden claro, una idea tras otra", "Ayuda a seguir lo que dices."),
        ("¿Qué hago en vez de decir «muy bueno»?", "Digo qué lo hace valioso", "Una razón se entiende mejor si dice con datos precisos qué hace valioso al texto.")],
    op=("Con la ficha: {F} Escribe en tu cuaderno un guion de cuatro oraciones que presente el cuento, cuente de qué trata, dé una razón y cierre, sin inventar datos.",
        "Les recomiendo «El farol de la esquina». Cuenta que Dora reúne firmas para arreglar el farol. Me gustó porque muestra que organizarse sirve. Se los recomiendo para conversar en grupo.",
        ["cuatro oraciones", "datos que coinciden con la ficha", "razón precisa"],
        ["un guion de cuatro oraciones"],
        ["inventar datos", "usar «muy bueno» como razón"],
        "Pregunta: «¿Dónde dice eso la ficha?»."),
    reinforce="Elige un cuento y escribe tres datos correctos de él.",
    extend="Escribe dos guiones: uno con un dato incorrecto a propósito y otro corregido.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy preparo una recomendación paso a paso: ideas clave, orden, guion, ensayo y presentación, con una cuenta de tiempos.",
    prior=["Sé las partes del guion.", "Ordeno ideas.", "Sé comprobar datos."],
    explain=[
        "Preparar una presentación oral tiene seis pasos. Paso 1: elige el texto y piensa en tu audiencia. Paso 2: anota las ideas clave. Paso 3: ordénalas. Paso 4: escribe un guion con frases cortas. Paso 5: ensaya en voz alta. Paso 6: presenta y escucha las preguntas.",
        "Ensayar sirve para ajustar el ritmo y notar frases difíciles. Si una persona habla a unas 120 palabras por minuto (cifra de ejemplo), un guion de 360 palabras dura 3 minutos. Ajusta el largo del guion al tiempo que te dan.",
        "En vez de leer todo, puedes apoyarte en tarjetas con ideas clave. Así miras a la audiencia y hablas con naturalidad. Y si te preguntan algo que no quieres contar, como el final, puedes decir con tranquilidad que prefieres que lo descubran leyendo.",
    ],
    vocab=[("ensayar", "practicar antes de presentar"), ("ritmo", "velocidad con que se habla"), ("tarjeta", "papel pequeño con ideas clave"), ("idea clave", "idea principal que no se puede olvidar")],
    worked=[
        ("Ordenar las notas", "Notas desordenadas: (a) Gracias por escuchar. (b) Les recomiendo «El pan compartido». (c) Me gustó porque muestra que compartir une. (d) Cuenta que dos vecinos reparten pan a todo el pasaje.", ["Primero presento: (b).", "Luego cuento: (d).", "Después doy la razón: (c).", "Cierro: (a)."], "(b), (d), (c), (a)"),
        ("Calcular el tiempo", "Guion de 180 palabras, a 90 palabras por minuto (cifras de ejemplo).", ["Divido las palabras por la velocidad.", "180 entre 90."], "2 minutos"),
    ],
    mistakes=[("No ensayar antes de presentar.", "No sabes cuánto dura ni dónde trabarte.", "Ensaya en voz alta al menos una vez."),
              ("Escribir un guion más largo que el tiempo disponible.", "Tendrás que cortar al hablar.", "Calcula las palabras que caben.")],
    T=[
        ("abc", "{F} ¿Qué hacen los vendedores cuando la feria queda sin luz?", "Cada uno trae una linterna y la pone sobre su mesa", "Cierran los puestos", "Piden más luz", "El cuento dice que cada vendedor trajo una linterna."),
        ("ab", "{F} ¿Qué nota (a, b, c o d) debe abrir la recomendación?", "(b), porque presenta el cuento", "(a), porque cierra", "La recomendación empieza presentando el texto."),
        ("¿Cuántos pasos tiene el método para preparar una presentación oral?", "6", "Son seis: elegir, anotar, ordenar, escribir, ensayar y presentar."),
        ("abc", "{F} ¿Cuál es el orden correcto de las notas?", "(b), (d), (c), (a)", "(a), (b), (c), (d)", "(d), (b), (a), (c)", "Se presenta el cuento, se cuenta de qué trata, se da la razón y se cierra."),
        ("ab", "¿Qué se hace en el paso 5?", "Ensayar en voz alta con pausas y buen volumen", "Elegir el texto", "El paso 5 es practicar hablando."),
        ("abc", "¿Por qué conviene ensayar?", "Para ajustar el ritmo y detectar frases difíciles", "Para olvidar el guion", "Para cambiar de cuento", "Ensayar permite corregir antes de presentar."),
        ("=", "Un guion tiene 240 palabras y se habla a 120 palabras por minuto (cifras de ejemplo). ¿Cuántos minutos dura?", "240/120", "Se divide el total de palabras por las palabras de cada minuto.", "minutos"),
        ("=", "Tienes 3 minutos y hablas a 120 palabras por minuto (cifra de ejemplo). ¿Cuántas palabras puede tener tu guion como máximo?", "3*120", "Se multiplican los minutos por las palabras de cada minuto.", "palabras"),
        ("abc", "Tu guion tiene 300 palabras, hablas a 100 palabras por minuto y tienes 2 minutos (cifras de ejemplo). ¿Qué haces?", "Lo acorto, porque dura 3 minutos", "Lo dejo igual, porque cabe", "Hablo más lento", "300 entre 100 son 3 minutos, más que los 2 disponibles."),
        ("ab", "Marcela anota ideas clave en tarjetas en vez de escribir todo para leerlo. ¿Qué ventaja tiene?", "Puede mirar a la audiencia y hablar con naturalidad", "Puede hablar sin ensayar", "Las tarjetas permiten hablar sin leer cada palabra."),
        ("abc", "{F} Si empiezas la recomendación con la nota (c), ¿qué pasa?", "La audiencia no sabe aún de qué cuento se habla", "La audiencia entiende mejor", "El cuento se acaba", "Antes de dar la razón hay que presentar el texto."),
        ("abc", "{F} ¿Cuál es una buena frase de cierre?", "Se los recomiendo para leer en grupo; gracias por escuchar", "Eso es todo y ya", "No sé qué más decir", "Un buen cierre recomienda la lectura y agradece a la audiencia."),
        ("abc", "En el paso 6, alguien pregunta: «¿Cómo termina?» y tú no querías contar el final. ¿Qué respondes?", "Prefiero no contarlo para que lo descubran al leerlo", "Lo cuento entero", "No respondo y me voy", "Se puede responder con respeto y mantener el interés."),
    ],
    ctx=("abc", "Mañana presentas una recomendación de un minuto. ¿Qué haces hoy?", "Anoto ideas, las ordeno y ensayo en voz alta", "Memorizo el cuento entero", "No hago nada", "Preparar las ideas y ensayar en voz alta da seguridad al presentar."),
    sc=[("¿Cuántos pasos tiene la preparación?", "Seis", "Elegir, anotar, ordenar, escribir, ensayar y presentar."),
        ("En Lenguaje: ¿para qué sirve ensayar?", "Para ajustar el ritmo y el tiempo", "Ensayar permite corregir el ritmo y las frases difíciles antes de presentar."),
        ("¿Qué hago si me preguntan por el final?", "Digo que prefiero que lo descubran leyendo", "Así se respeta a quien pregunta y se mantiene el interés por leer el cuento.")],
    op=("Con las notas: {F} Escribe un guion de cinco oraciones para recomendar «La feria sin luz». Calcula cuántos minutos dura si tiene 90 palabras y hablas a 120 palabras por minuto (cifras de ejemplo).",
        "Quiero recomendarles «La feria sin luz». Cuenta que una noche la feria se queda sin luz y los vendedores usan linternas. Me gustó porque muestra cómo cada persona aporta una luz. Se los recomiendo para leer en grupo. Gracias. Tiempo: 90 palabras a 120 por minuto dura menos de un minuto.",
        ["cinco oraciones", "orden correcto", "tiempo calculado"],
        ["un guion y una cuenta"],
        ["olvidar el cierre", "equivocar la cuenta"],
        "Pregunta: «¿Cuánto dura en voz alta?»."),
    reinforce="Ensaya en voz alta tu guion y mide cuánto dura.",
    extend="Reduce tu guion a la mitad sin quitar la razón ni el cierre.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo: reviso un guion en pareja y lo mejoro con razón, palabras precisas, tildes y verbos.",
    prior=["Conozco el guion y sus partes.", "Reconozco tildes en agudas.", "Sé qué es un sinónimo."],
    explain=[
        "Revisar el guion con otra persona ayuda mucho. Quien escucha nota repeticiones, frases confusas y datos que faltan que quien escribe ya no ve.",
        "Cuatro cosas conviene revisar. Primero, que haya una razón con un dato. Segundo, que no se repitan palabras: usa sinónimos como «agradable» o «entretenido» en vez de «muy bueno». Tercero, que los verbos estén en el mismo tiempo: si cuentas lo que pasó, «quedó» y «trajeron». Cuarto, las tildes y la puntuación.",
        "Las palabras agudas terminadas en vocal, n o s llevan tilde: «terminó». Los signos de puntuación marcan las pausas: la coma, una pausa breve; el punto, una pausa mayor. Cuando lees en voz alta, esas pausas te guían.",
    ],
    vocab=[("repetición", "usar la misma palabra muchas veces"), ("sinónimo", "palabra de significado parecido"), ("puntuación", "signos que marcan pausas: coma, punto"), ("revisar en pareja", "leer el texto con otra persona para mejorarlo")],
    worked=[
        ("Corregir una tilde", "Palabra sin tilde: «termino» en «Ella termino su turno».", ["«termino» se dice ter-mi-NÓ: la fuerza está en la última sílaba.", "Es aguda y termina en vocal: lleva tilde."], "terminó"),
        ("Evitar repetición", "Frase: «La feria es muy grande y la gente es muy amable».", ["La palabra «muy» se repite.", "Puedo decir «La feria es enorme y la gente, amable»."], "La feria es enorme y la gente, amable"),
    ],
    mistakes=[("Corregir solo las tildes y dejar el guion sin razón.", "El guion sigue sin justificar.", "Revisa primero las ideas y luego la forma."),
              ("Cambiar de tiempo verbal sin darse cuenta.", "El relato se vuelve confuso.", "Mantén los verbos en el mismo tiempo.")],
    T=[
        ("abc", "{F} ¿Qué palabra necesita tilde?", "quedo, que debe ser quedó", "cuento", "feria", "«Quedó» es aguda y termina en vocal."),
        ("{F} ¿Cuántas veces aparece la palabra «muy» en el borrador? Escribe el número.", "4", "Aparece en «muy bueno», «muy bueno», «muy lindo» y «muy bueno»."),
        ("ab", "{F} ¿Qué verbo del borrador está en pretérito?", "trajeron", "es", "«Trajeron» expresa algo que ya ocurrió."),
        ("abc", "{F} ¿Qué le falta al borrador?", "Una razón con un dato del texto y un cierre", "Más repeticiones", "Un título más largo", "No dice por qué se recomienda ni cierra."),
        ("ab", "{F} ¿Cuál es un sinónimo para reemplazar «bueno»?", "agradable", "malo", "«Agradable» significa algo parecido a bueno."),
        ("abc", "En Lenguaje: ¿qué marca la coma en un texto que se dice en voz alta?", "Una pausa breve", "Una pausa larga de final", "El inicio de una cita", "La coma separa partes dentro de una oración."),
        ("abc", "{F} Reescribe «Es un cuento muy bueno.» evitando repetir. ¿Cuál versión sirve?", "Es un cuento entretenido y esperanzador.", "Es un cuento muy muy bueno.", "Es un cuento bueno bueno.", "Usa palabras precisas en lugar de repetir."),
        ("abc", "{F} ¿Qué versión corrige bien «Cuenta que una noche la feria quedo sin luz»?", "Cuenta que una noche la feria quedó sin luz.", "Cuenta que una noche la feria quedo sin luz", "Cuenta que, una noche la feria quedó sin luz.", "La tilde de «quedó» y el punto final completan la oración."),
        ("abc", "{F} ¿Dónde agregarías la razón?", "Después de contar de qué trata y antes del cierre", "Antes del saludo", "Después de decir «gracias»", "La razón sigue a la presentación y al resumen, según la progresión del guion."),
        ("ab", "Ana dice que basta con ordenar el guion. Beto dice que también hay que revisar tildes y repeticiones. ¿Quién tiene razón?", "Beto", "Ana", "Un guion necesita ideas ordenadas y buena escritura."),
        ("abc", "{F} ¿Por qué conviene que otra persona escuche el guion?", "Porque puede notar frases confusas o repeticiones que quien escribe no ve", "Porque así se ahorra tiempo", "Porque cambia el cuento", "Quien escucha por primera vez detecta lo que quien escribe ya no nota."),
        ("abc", "{F} ¿Cuál es la versión más completa?", "Les recomiendo «La feria sin luz». Cuenta que una noche la feria quedó sin luz y los vendedores trajeron linternas. Me gustó porque cada persona aporta una luz. Se los recomiendo para leer en grupo.", "Les recomiendo «La feria sin luz». Es muy bueno y muy lindo.", "Les recomiendo el cuento y ya.", "Tiene presentación, resumen, razón y cierre."),
        ("ab", "{F} Si agregas un dato inventado, como que la feria queda en otra ciudad, ¿qué problema aparece?", "La información deja de ser fidedigna", "El guion queda más corto", "El texto no dice dónde queda la feria; sería un dato inventado."),
    ],
    ctx=("abc", "Una compañera te lee su guion en voz alta y notas que repite «lindo» seis veces. ¿Qué haces?", "Le propongo sinónimos y le pregunto qué lo hace lindo", "Le digo que está mal escrito", "No le digo nada", "Un buen comentario ayuda a mejorar sin juzgar."),
    sc=[("¿Qué reviso primero en un guion?", "Que tenga razón con dato", "Después de las ideas reviso las palabras, las tildes y la puntuación."),
        ("En Lenguaje: ¿qué marca el punto al leer en voz alta?", "Una pausa mayor", "El punto indica el final de una idea y marca una pausa mayor al leer."),
        ("¿Cómo evito repetir una palabra?", "Uso sinónimos", "Los sinónimos dan variedad al texto y evitan repetir la misma palabra.")],
    op=("Reescribe el borrador: {F} Quita las repeticiones, corrige la tilde, agrega una razón con dato y un cierre. Léelo en voz alta a otra persona y pídele un comentario.",
        "Les recomiendo el cuento «La feria sin luz». Cuenta que una noche la feria quedó sin luz y los vendedores trajeron linternas. Me gustó porque muestra cómo cada persona aporta una luz. Se los recomiendo para leer en grupo. Gracias.",
        ["razón con dato", "sin repeticiones", "tildes y verbos correctos", "cierre"],
        ["el guion reescrito"],
        ["cambiar solo una palabra", "perder datos del cuento"],
        "Pregunta: «¿Qué parte te quedó más clara al escucharla?»."),
    reinforce="Cambia dos palabras repetidas de un texto tuyo por sinónimos.",
    extend="Escribe tres frases sobre un cuento usando verbos en pretérito.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a una situación real: escribir y decir una reseña breve de un poema para el diario mural y para una reunión.",
    prior=["Sé armar un guion.", "Cuido tildes y verbos.", "Justifico con datos."],
    explain=[
        "Una reseña es un texto corto que presenta una obra y explica por qué la recomiendas. Puede escribirse para un diario mural o decirse en una reunión. Tiene cuatro partes: título, de qué trata, razón con un verso o una cita, y cierre.",
        "Cuando escribes, cuidas la ortografía y la puntuación. Cuando hablas, cuidas la voz, las pausas y el ritmo. Las ideas son las mismas; lo que cambia es el medio.",
        "En un poema, la cita es un verso. Elige el verso que apoya tu razón y escríbelo entre comillas. Si dices que el poema transmite calidez, cita el verso donde se siente.",
    ],
    vocab=[("reseña", "texto breve que presenta una obra y explica por qué se recomienda"), ("diario mural", "tablero donde se publican textos para que otras personas los lean"), ("cita", "frase exacta del texto, entre comillas"), ("medio", "forma de comunicar: escrito o hablado")],
    worked=[
        ("Las cuatro partes", "Poema (inventado), «Té de la tarde»: Té en la tarde, / vapor en la taza; / la lluvia golpea / y el tiempo se amansa.", ["Título: «Té de la tarde».", "Trata de: una tarde de lluvia con un té.", "Razón con cita: transmite tranquilidad: «el tiempo se amansa».", "Cierre: lo recomiendo para leer en un descanso."], "Reseña de cuatro partes"),
        ("Pasar de lo escrito a lo oral", "Reseña escrita: «Recomiendo...».", ["Agrego un saludo.", "Marco pausas con la voz."], "La misma idea, con voz y pausas"),
    ],
    mistakes=[("Copiar el poema entero en la reseña.", "No queda espacio para tu razón.", "Cita solo el verso que apoya tu razón."),
              ("Escribir «por que» para dar la razón.", "La razón se escribe «porque».", "Usa «porque» junto y sin tilde.")],
    T=[
        ("{F} ¿Cuántos versos tiene el poema? Escribe el número.", "4", "Las líneas separadas por barras son cuatro."),
        ("ab", "{F} ¿Qué palabras riman en los dos primeros versos?", "«mañana» y «ventana»", "«pan» y «calle»", "Esas dos palabras terminan con el mismo sonido."),
        ("abc", "{F} ¿De qué trata el poema?", "De una mañana en que el pan caliente despierta la calle", "De una noche sin luz", "De un viaje en bus", "Los versos hablan de pan caliente, vapor y calle."),
        ("ab", "{F} ¿Qué verso conviene citar para decir que el poema transmite calidez?", "«la calle huele a hogar»", "«vapor en la ventana»", "El verso del hogar expresa calidez."),
        ("ab", "En una reseña, ¿qué parte va justo después de decir de qué trata la obra?", "La razón con una cita", "El título", "Primero se presenta y se cuenta de qué trata; luego se da la razón con la cita."),
        ("abc", "¿Qué diferencia hay entre escribir y decir una reseña?", "Al hablar usas pausas y tono; al escribir usas puntuación y ortografía", "Al hablar no hay datos", "Al escribir no hay razón", "Al hablar se usan la voz y las pausas; al escribir, la puntuación y la ortografía."),
        ("abc", "{F} Completa: «Recomiendo el poema «Pan caliente» ___ transmite calidez: «la calle huele a hogar».»", "porque", "por qué", "porqué", "Es una razón: va junto y sin tilde."),
        ("abc", "{F} ¿Cuál es el cierre más adecuado?", "Lo recomiendo para leer en voz alta al comenzar el día.", "Eso.", "Fin del poema.", "Un cierre adecuado recomienda la lectura y termina la reseña con claridad."),
        ("=", "Tu reseña oral tiene 220 palabras y hablas a 110 palabras por minuto (cifras de ejemplo). ¿Cuántos minutos dura?", "220/110", "Se divide el total de palabras por la velocidad.", "minutos"),
        ("ab", "Un compañero escribe: «Recomiendo el poema por que es lindo.» ¿Qué conviene corregir?", "Escribir «porque» junto y agregar un verso como dato", "Cambiar «poema» por «cuento»", "Falta la razón con dato y la forma de «porque»."),
        ("abc", "{F} Para el diario mural, ¿qué es mejor?", "Citar un verso que apoye la razón", "Copiar todo el poema", "No citar nada", "Un verso apoya la razón sin ocupar todo el espacio."),
        ("abc", "{F} ¿Qué dato apoya la razón «el poema habla de algo cotidiano»?", "Habla de pan, de una ventana y de la calle", "Habla de una batalla", "Habla de un viaje largo", "Esos elementos aparecen en la vida diaria."),
        ("ab", "{F} Si lees la reseña en voz alta a un grupo, ¿qué agregas respecto de la versión escrita?", "Pausas y entonación", "Más versos", "La voz expresa lo que la puntuación marca por escrito."),
    ],
    ctx=("abc", "Para el diario mural del centro debes escribir una reseña breve de un poema. ¿Qué incluyes?", "Título, de qué trata, una razón con un verso citado y un cierre", "Solo el título", "El poema completo", "Esas son las cuatro partes de la reseña."),
    sc=[("En Lenguaje: ¿qué es una reseña?", "Un texto breve que presenta una obra y la recomienda", "Toda reseña incluye una razón que explica por qué se recomienda la obra."),
        ("¿Qué cito en una reseña de poema?", "Un verso que apoye mi razón", "En un poema la cita es un verso escrito igual que en el texto."),
        ("¿Qué cambia entre lo escrito y lo oral?", "El medio: uso puntuación al escribir y pausas al hablar", "Las ideas se mantienen y solo cambia el medio: puntuación al escribir, pausas al hablar.")],
    op=("Con el poema: {F} Escribe una reseña de cuatro oraciones para el diario mural (título, de qué trata, razón con un verso entre comillas y cierre). Después dila en voz alta en un minuto.",
        "«Pan caliente». Es un poema sobre una mañana en que el pan despierta la calle. Lo recomiendo porque transmite calidez: «la calle huele a hogar». Es ideal para leer en voz alta al comenzar el día.",
        ["cuatro partes", "verso entre comillas", "buena ortografía"],
        ["una reseña de cuatro oraciones y una lectura en voz alta"],
        ["no citar un verso", "olvidar el cierre"],
        "Pregunta: «¿Qué verso apoya tu razón?»."),
    reinforce="Escribe la razón de una reseña con «porque» y un verso.",
    extend="Haz una reseña de otro texto breve que conozcas.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo logrado: evalúo una recomendación con una pauta, la escucho con atención y decido mis próximos pasos.",
    prior=["Sé preparar una recomendación.", "Sé revisar un guion.", "Puedo escuchar y anotar."],
    explain=[
        "Evaluar una recomendación sirve para mejorar la tuya. Una pauta es una lista de criterios con puntos. En esta pauta de ejemplo hay cinco criterios: saludo y título, resumen claro, razón con dato, cita correcta y cierre. Cada criterio cumplido suma 2 puntos.",
        "Al escuchar a otra persona, anota ideas clave: personaje, hecho principal y razón. Después comprueba cada criterio con lo que anotaste. Evalúa lo que se dice, no a la persona, y da un comentario amable y concreto.",
        "Para decidir tus próximos pasos, mira qué criterios te salen bien y cuáles quieres practicar. Escribe una meta pequeña y una forma de practicarla esta semana.",
    ],
    vocab=[("pauta", "lista de criterios con puntos para evaluar algo"), ("comentario", "opinión que ayuda a mejorar"), ("criterio cumplido", "aspecto de la pauta que sí aparece"), ("meta", "objetivo concreto que quieres lograr")],
    worked=[
        ("Aplicar la pauta", "Guion (inventado): «Buenas tardes. Les recomiendo el cuento «La escalera». Cuenta cómo una vecina ayuda a otra a subir las compras. Se los recomiendo. Gracias».", ["Saludo y título: sí, 2 puntos.", "Resumen claro: sí, 2 puntos.", "Razón con dato: no, 0 puntos.", "Cita: no, 0 puntos.", "Cierre: sí, 2 puntos."], "Suma 6 de 10 puntos"),
        ("Tomar notas al escuchar", "Escuchas: «Cuando se cortó la luz, don Elías encendió una vela y avisó a sus vecinos».", ["Anoto el personaje: Elías.", "Anoto el hecho: corte de luz, enciende una vela y avisa."], "Notas con personaje y hechos"),
    ],
    mistakes=[("Evaluar a la persona y no al guion.", "El comentario debe ayudar a mejorar lo dicho.", "Habla de los criterios de la pauta."),
              ("Fijar una meta imposible de comprobar, como «hablar mejor».", "No se sabe qué hacer.", "Escribe una acción concreta y medible.")],
    T=[
        ("abc", "{F} ¿Quién es Mario?", "Quien cuida una sede vecinal", "Una vecina que vende pan", "El dueño de un buzón", "El guion dice que cuida una sede vecinal."),
        ("ab", "{F} ¿Dónde encuentran las llaves?", "En el patio", "En la sede", "El guion dice «las encuentran en el patio»."),
        ("=", "La pauta de ejemplo tiene 5 criterios y 10 puntos en total. ¿Cuántos puntos vale cada criterio?", "10/5", "Se reparten los 10 puntos entre los 5 criterios.", "puntos"),
        ("abc", "{F} ¿Cuál es la razón que da la persona para su recomendación?", "Que muestra que pedir ayuda no es debilidad", "Que es un cuento largo", "Que Mario es amigo suyo", "La razón aparece después de «Me gustó porque»."),
        ("ab", "{F} ¿Cuál es la cita incluida en el guion?", "«Solos no las habríamos encontrado»", "«Hola a todas y a todos»", "La cita está entre comillas y la dice Mario."),
        ("abc", "Escuchas el guion leído en voz alta. ¿Qué nota breve es adecuada?", "Mario; llaves; ayuda de vecinos; patio", "Todo el guion copiado", "Solo el saludo", "Una nota recoge personaje, hecho y lugar."),
        ("=", "Un guion obtuvo 2 puntos en tres criterios, 1 punto en uno y 0 en otro. ¿Cuántos puntos suma?", "2+2+2+1+0", "Se suman los puntos de cada criterio.", "puntos"),
        ("{F} ¿Cuántos criterios de la pauta cumple el guion completo? Escribe el número.", "5", "Tiene saludo y título, resumen, razón con dato, cita y cierre."),
        ("{F} ¿Con qué dos palabras agradece al final el guion? Escríbelas.", "muchas gracias", "El guion termina con «Muchas gracias», que agradece a la audiencia."),
        ("ab", "Alguien dice que el guion no tiene cierre. ¿Es cierto?", "No: termina con una recomendación y un agradecimiento", "Sí: no hay frase final", "El cierre es «Se lo recomiendo a quien quiera leer una historia breve y cálida. Muchas gracias»."),
        ("abc", "{F} Si solo tienes 30 segundos, ¿qué mejora haces?", "Acorto el resumen y mantengo la razón y el cierre", "Quito la razón", "Quito el cierre", "La razón y el cierre son lo esencial."),
        ("abc", "{F} ¿Qué dato apoya decir que el cuento es cálido?", "Los vecinos ayudan a Mario a encontrar las llaves", "Las llaves se pierden", "El cuento es breve", "Cuando los vecinos se ayudan entre sí se muestra calidez."),
        ("ab", "{F} ¿Por qué la cita aporta a la recomendación?", "Porque muestra con palabras del texto la razón", "Porque alarga el guion", "La cita respalda la razón con el texto."),
    ],
    ctx=("abc", "Después de escuchar una recomendación, quieres dar un comentario útil. ¿Qué dices?", "Qué criterio de la pauta cumplió y qué podría mejorar, con un ejemplo", "Que no te gustó", "Nada, por respeto", "Un comentario concreto ayuda a mejorar."),
    sc=[("¿Cuántos criterios tiene la pauta de hoy?", "Cinco", "Saludo, resumen, razón, cita y cierre."),
        ("En Lenguaje: ¿qué es una meta?", "Un objetivo concreto que quiero lograr", "Una meta concreta debe poder comprobarse luego, por ejemplo midiendo el tiempo."),
        ("¿Qué evalúo al dar un comentario?", "Lo que se dice, no a la persona", "Un comentario sobre lo dicho ayuda a mejorarlo; uno sobre la persona no.")],
    op=("Evalúa el guion: {F} Completa la pauta con puntos, escribe un comentario amable con un ejemplo y una meta concreta para tu próxima recomendación.",
        "Saludo y título 2; resumen 2; razón con dato 2; cita 2; cierre 2: total 10. Comentario: el resumen es claro y la cita apoya la razón. Meta: escribiré mi guion y mediré su tiempo antes de presentarlo.",
        ["pauta completa", "comentario amable con ejemplo", "meta concreta"],
        ["una pauta, un comentario y una meta"],
        ["comentarios sobre la persona", "meta vaga"],
        "Pregunta: «¿Cómo vas a comprobar tu meta?»."),
    reinforce="Evalúa en silencio tu propio guion con la pauta de cinco criterios.",
    extend="Prepara una recomendación breve de otro texto y pide a otra persona que la evalúe con la pauta.",
)
