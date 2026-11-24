"""Lenguaje y Comunicación EPJA Nivel 2, módulo 1 (parte 2): OAD-02, comparar textos literarios aplicando criterios (poesía, narrativa y texto dramático). Textos inventados, en papel."""
from __future__ import annotations

from epja_leco_nb2_common import build

O = "EPJA-LECO-NB2-OAD-02"

F1 = ("Texto A (inventado), poema «Lluvia de abril»: Cae la lluvia en la calle, / moja el pan y la ventana; / todo huele a tierra fresca / y a promesa de mañana. "
      "Texto B (inventado), cuento «La lluvia en la feria»: Cuando empezó a llover, Carmen cubrió sus verduras con un plástico. Los clientes corrieron a refugiarse bajo el toldo de su puesto. "
      "Carmen les convidó pan y esperaron juntos. Al rato dejó de llover y todos compraron algo antes de irse.")

F2 = ("Poema (inventado), «El mercado de la mañana». Primera estrofa: Se abre el toldo del mercado, / el sol llega temprano; / la mañana huele a pan / y a cilantro en la mano. "
      "Segunda estrofa: Una voz pregona frutas, / otra voz ofrece flor; / el día empieza cantando / con el ruido del pregón. "
      "Escena (inventada): (En la entrada de una feria. ROSA ordena las cajas; LUIS llega apurado.) LUIS: ¿Llegó el camión? ROSA (mirando el reloj): Hace diez minutos. LUIS: Entonces vamos, que se enfría el pan.")

F3 = ("Texto A (inventado), poema «La espera»: Miro el reloj en la pared, / el tiempo no quiere andar; / yo sentada en esta silla / aprendo a esperar. "
      "Texto B (inventado), cuento «La sala de espera»: Aurora esperaba su turno en el consultorio. Miraba el reloj y las agujas avanzaban muy lento. "
      "Para pasar el tiempo, leyó los avisos de la pared y conversó con una señora que estaba a su lado. Cuando dijeron su nombre, se dio cuenta de que la espera había sido más corta de lo que pensaba.")

F4 = ("Texto C (inventado), cuento «En la fila»: En la fila del banco, la señora Eva pasó adelante sin darse cuenta. Lucas, que esperaba hacía rato, se lo hizo notar con voz firme. "
      "Eva se sorprendió, explicó que no había visto el número y pidió perdón. Lucas aceptó las disculpas y la fila siguió en orden. "
      "Texto D (inventado), escena «En la fila»: (En la fila de un banco. EVA pasa adelante; LUCAS la mira.) LUCAS (con voz firme): Disculpe, la fila termina allá. EVA (sorprendida): No había visto el número. Perdón. LUCAS: No hay problema. Sigamos en orden. (EVA vuelve a su lugar.)")

F5 = ("Poema (inventado), «Barrio»: Esquina de pan y de ruido, / farol que se enciende al dar la tarde, / vecinos que se saludan / y un perro que nunca se cansa. "
      "Cuento (inventado), «El banco de la plaza»: Mateo vio que una señora mayor llegaba cansada a la plaza y que el único banco tenía un letrero de «pintura fresca». Tocó la madera con un dedo: ya estaba seca. Sacó el letrero y le ofreció sentarse. "
      "Escena (inventada), «La llave del salón»: (En la puerta de la sede vecinal. INÉS busca en su bolso; TOMÁS espera.) TOMÁS: ¿La encontraste? INÉS (aliviada): Aquí está. Pasa tú primero. (TOMÁS entra y enciende la luz.)")

F6 = ("Texto 1 (inventado), poema «Camino a casa»: Doblo la esquina despacio, / el farol me hace una seña; / en la ventana de enfrente / ya alguien dejó la luz puesta. "
      "Texto 2 (inventado), cuento «El turno equivocado»: Gabriela llegó a la municipalidad a las ocho, pero su hora era a las nueve. La funcionaria revisó el papel y le explicó el error. "
      "Gabriela esperó una hora con paciencia y, cuando la llamaron, agradeció la explicación. "
      "Texto 3 (inventado), escena «Dos paquetes»: (En la puerta de un edificio. SOFÍA lleva dos paquetes; DANIEL sostiene la puerta.) DANIEL: Pasa, yo la sostengo. SOFÍA (sonriendo): Gracias. DANIEL: De nada. (SOFÍA entra.)")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy descubro que ya comparo cosas a diario y aprendo a comparar dos textos literarios con criterios.",
    prior=["Reconozco un cuento y un poema.", "Sé nombrar personajes, ambiente y problema.", "Comparo precios, rutas u horarios en mi día a día."],
    explain=[
        "Comparar es algo que haces todos los días: dos rutas para llegar a un trámite, dos precios, dos horarios. Para elegir bien, miras los mismos aspectos en ambos. Con los textos literarios pasa igual.",
        "Cada aspecto que se mira en todos los textos es un criterio. Algunos criterios sirven para cualquier texto: el tema, la forma en que está escrito, quién habla y qué transmite. La forma puede ser verso, como en un poema, o prosa, como en un cuento.",
        "Un texto literario puede tener el mismo tema que otro y ser muy distinto. Dos textos pueden hablar de la lluvia: uno la describe con versos y sensaciones, y otro cuenta lo que hacen las personas cuando llueve.",
    ],
    vocab=[("criterio", "aspecto que se mira en todos los textos que se comparan"), ("forma", "manera en que está escrito un texto: en versos o en prosa"), ("prosa", "escritura en párrafos, sin versos"), ("tema", "asunto de que trata un texto")],
    worked=[
        ("Comparar la forma", "Texto P (inventado): «Sol de mediodía, / sombra en la vereda, / el aire se detiene / y el calor se queda». Texto Q (inventado): «Con el calor del mediodía, Jorge cerró el puesto y repartió agua fría entre sus vecinos».", ["El Texto P está en cuatro versos.", "El Texto Q está en un párrafo, en prosa."], "P en verso; Q en prosa"),
        ("Comparar lo que transmite", "Los mismos textos P y Q.", ["P habla del calor y de la quietud del aire: transmite una sensación.", "Q cuenta lo que hace Jorge: transmite una historia de ayuda entre vecinos."], "P expresa sensaciones; Q cuenta hechos"),
    ],
    mistakes=[("Decir que dos textos son iguales porque tratan el mismo tema.", "El tema es solo un criterio; la forma y lo que cuentan pueden ser muy distintos.", "Compara también la forma, quién habla y qué transmite."),
              ("Comparar con una opinión suelta como «me gusta más».", "Una opinión sin criterio no permite comparar.", "Nombra el criterio y da un dato de cada texto.")],
    T=[
        ("abc", "{F} ¿Qué texto está escrito en versos?", "El Texto A", "El Texto B", "Los dos", "El Texto A está dividido en líneas cortas; el B es un párrafo."),
        ("ab", "{F} ¿Quiénes actúan en el Texto B?", "Carmen y sus clientes", "Solo la lluvia", "Carmen cubre sus verduras y los clientes se refugian en su puesto."),
        ("{F} ¿Cuántos versos tiene el Texto A? Escribe el número.", "4", "Las líneas separadas por barras son cuatro."),
        ("abc", "{F} ¿Qué tienen en común los dos textos?", "Ambos tienen la lluvia como tema", "Ambos cuentan lo que hace Carmen", "Ambos están escritos en versos", "Los dos giran en torno a la lluvia."),
        ("ab", "{F} ¿Qué transmite el Texto A?", "Una sensación de calma y esperanza ante la lluvia", "Instrucciones para vender verduras", "Los versos hablan de tierra fresca y de una promesa de mañana."),
        ("abc", "Comparas un poema y un cuento mirando cómo están escritos y qué cuentan. ¿Cómo se llama cada aspecto que miras?", "Un criterio", "Un verso", "Un desenlace", "Los aspectos que se miran en ambos textos son criterios."),
        ("abc", "{F} Quieres comparar los textos según su forma. ¿Qué anotas?", "A está en versos y B está en prosa", "A tiene personajes y B no", "Ambos están en versos", "Esa anotación describe cómo está escrito cada texto."),
        ("abc", "{F} Quieres comparar según quién habla. ¿Qué anotas?", "En A una voz expresa lo que percibe; en B alguien cuenta lo que hace Carmen", "En A y en B habla Carmen", "En A hablan los clientes", "El poema expresa sensaciones; el cuento narra hechos."),
        ("{F} ¿Qué palabra rima con «ventana» en el Texto A? Escribe una palabra.", "mañana", "Ventana y mañana terminan con el mismo sonido."),
        ("ab", "Jorge dice: «Los dos textos son iguales porque hablan de la lluvia.» ¿Qué responde quien compara con criterios?", "Que el tema es igual, pero la forma y lo que cuentan cambian", "Que tiene razón, porque el tema es lo único que importa", "Con criterios se ve que solo coincide uno de ellos."),
        ("abc", "{F} ¿Qué criterio muestra más claramente que el Texto B es narrativo?", "Que cuenta hechos en orden que hacen los personajes", "Que es corto", "Que nombra la lluvia", "La narrativa cuenta acciones de personajes."),
        ("abc", "{F} Una lectora quiere un texto para sentir calma. Otra quiere uno para enterarse de lo que hace una comerciante. ¿Qué elige cada una?", "La primera elige A; la segunda elige B", "La primera elige B; la segunda elige A", "Ambas eligen B", "A transmite calma; B cuenta lo que hace Carmen."),
        ("ab", "{F} Si el Texto B se reescribiera en versos, ¿qué cambiaría y qué seguiría igual?", "Cambiaría la forma; seguirían los hechos de Carmen", "Cambiaría el tema; seguiría la forma", "Pasar a versos cambia la forma, no lo que ocurre."),
    ],
    ctx=("abc", "En un taller te piden comparar dos textos que hablan del mismo tema. ¿Cómo empiezas?", "Decido qué aspectos voy a mirar en los dos", "Elijo el texto más corto", "Leo solo el título", "Primero se eligen los criterios para comparar lo mismo en ambos."),
    sc=[("En Lenguaje: ¿qué es la prosa?", "Escritura en párrafos, sin versos", "La prosa es la escritura en párrafos, que es la forma en que se escribe un cuento."),
        ("¿Qué criterios sirven para comparar textos literarios?", "Tema, forma, quién habla y qué transmite", "Se pueden mirar en cualquier texto."),
        ("¿Por qué no basta que dos textos tengan el mismo tema?", "Porque pueden ser muy distintos en forma y en lo que cuentan", "Un solo criterio, como el tema, deja fuera la forma y lo que cuenta cada texto.")],
    op=("Compara estos textos: {F} Escribe en tu cuaderno, en una tabla, tres criterios (tema, forma y qué transmite) y lo que dice cada texto en cada uno.",
        "Tema: A y B, la lluvia. Forma: A, en versos; B, en prosa. Qué transmite: A, calma y esperanza; B, ayuda entre personas.",
        ["tres criterios", "datos de cada texto", "datos correctos"],
        ["una tabla de tres filas y dos columnas"],
        ["llenar solo una columna", "usar opiniones sin datos"],
        "Pregunta: «¿Qué dato del texto dice eso?»."),
    reinforce="Piensa en dos textos que conozcas del mismo tema y di un criterio en que se parecen.",
    extend="Compara dos rutas o dos precios que conozcas con tres criterios y luego compara dos textos con tres criterios.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo palabras para hablar de poemas y escenas de teatro: verso, estrofa, rima, hablante lírico y acotación.",
    prior=["Distingo poema, cuento y escena.", "Uso criterios para comparar.", "Sé que en el teatro los personajes hablan."],
    explain=[
        "La poesía se escribe en versos, que son las líneas del poema. Un grupo de versos forma una estrofa. A veces los versos riman: terminan con sonidos parecidos, como «luna» y «cuna». La voz que habla en el poema se llama hablante lírico y expresa lo que ve y siente.",
        "El texto dramático se escribe para que personas lo representen. Cada personaje tiene su nombre antes de sus palabras. Lo que está entre paréntesis es una acotación: una indicación sobre dónde ocurre la escena o cómo actúa y habla alguien.",
        "La narrativa, en cambio, usa un narrador que cuenta lo que ocurre. Conocer estos nombres te permite comparar con precisión: ya no dices «uno tiene líneas cortas y otro no», sino «uno está en versos y otro tiene acotaciones».",
    ],
    vocab=[("estrofa", "grupo de versos de un poema"), ("rima", "sonido parecido al final de dos versos"), ("hablante lírico", "voz que habla en un poema y expresa lo que siente"), ("acotación", "indicación entre paréntesis sobre lugar, gestos o tono de voz"), ("pregonar", "anunciar en voz alta lo que se vende")],
    worked=[
        ("Contar versos y estrofas", "Poema (inventado). Primera estrofa: Llega la tarde / y baja el ruido; / la plaza respira. Segunda estrofa: Un farol se enciende, / un vecino pasa, / alguien cierra la ventana / y la calle queda en calma.", ["Primera estrofa: tres versos.", "Segunda estrofa: cuatro versos.", "Son dos estrofas y siete versos."], "2 estrofas y 7 versos"),
        ("Hallar una acotación", "Escena (inventada): (En una parada. NORA espera; ÓSCAR llega corriendo.) ÓSCAR (sin aire): ¿Pasó el bus? NORA: Recién se fue.", ["Busco lo que está entre paréntesis.", "«(sin aire)» dice cómo habla Óscar."], "«(sin aire)» es una acotación"),
    ],
    mistakes=[("Llamar «narrador» a la voz de un poema.", "En el poema habla el hablante lírico, que expresa lo que siente; el narrador cuenta hechos.", "Pregunta si la voz cuenta hechos o expresa lo que percibe."),
              ("Leer las acotaciones como si las dijera un personaje.", "Las acotaciones no se dicen: indican cómo actuar.", "Lee en voz alta solo lo que dice cada nombre y deja las acotaciones como guía.")],
    T=[
        ("{F} ¿Cuántas estrofas tiene el poema? Escribe el número.", "2", "El poema se divide en una primera y una segunda estrofa."),
        ("ab", "{F} ¿Qué parte de la escena está entre paréntesis y explica cómo actúa un personaje?", "La acotación", "El verso", "Lo que va entre paréntesis indica gestos o tono."),
        ("abc", "En Lenguaje: ¿qué es una estrofa?", "Un grupo de versos de un poema", "Una palabra que rima", "Una frase del narrador", "Los versos se agrupan en estrofas."),
        ("ab", "{F} ¿Qué palabras riman en la primera estrofa del poema?", "«temprano» y «mano»", "«mercado» y «pan»", "Temprano y mano terminan con el mismo sonido."),
        ("abc", "{F} ¿Quién es el hablante lírico del poema?", "La voz que expresa lo que ve y siente en el mercado", "Rosa", "Luis", "Rosa y Luis son personajes de la escena."),
        ("ab", "{F} ¿Cuántos personajes hablan en la escena?", "Dos: Rosa y Luis", "Uno: Luis", "Las líneas de la escena las dicen Luis y Rosa."),
        ("abc", "{F} ¿Qué indica «(mirando el reloj)» junto a Rosa?", "Qué hace Rosa mientras habla", "Lo que dice el narrador", "Un verso del poema", "Lo que va entre paréntesis y dice cómo actúa o habla alguien es una acotación: orienta la actuación."),
        ("Lee: «La noche se acerca, / la calle se calla, / la luna me mira.» ¿Cuántos versos tiene? Escribe el número.", "3", "Las líneas separadas por barras son tres versos."),
        ("abc", "Lee: «ANA (mirando a la puerta): ¿Ya llegó el jefe?» ¿Cuál es la acotación?", "(mirando a la puerta)", "ANA", "¿Ya llegó el jefe?", "La acotación es lo que va entre paréntesis."),
        ("ab", "Silvia dice: «En el poema hay un narrador que cuenta lo que pasa en el mercado.» ¿Es exacta su afirmación?", "No: habla una voz que expresa lo que ve y siente, sin contar hechos de personajes", "Sí: todo texto literario tiene narrador", "El poema usa un hablante lírico; el narrador es propio de la narrativa."),
        ("abc", "{F} ¿Qué diferencia hay entre los versos del poema y las líneas de la escena?", "Los versos expresan lo que siente quien habla; las líneas de la escena son palabras de personajes para representar", "Los versos las dicen personajes; las líneas de la escena las dice un hablante", "No hay diferencia", "El poema usa versos y un hablante; la escena usa nombres de personajes y acotaciones, por eso son elementos distintos."),
        ("abc", "Un texto dice: «MARIO: ¿Vamos? / TERESA: Vamos.» Otro dice: «Mario y Teresa salieron juntos a la plaza.» ¿Cuál es dramático y cuál narrativo?", "El primero es dramático y el segundo narrativo", "El primero es narrativo y el segundo dramático", "Los dos son poemas", "El primero tiene nombres antes de las palabras; el segundo narra."),
        ("ab", "{F} ¿Cuál de estas líneas sería una buena acotación para la escena?", "(LUIS deja una caja en el suelo.)", "Una voz pregona frutas", "Una acotación indica una acción entre paréntesis; la otra es un verso."),
    ],
    ctx=("abc", "En la biblioteca te ofrecen escenas para representar con otra persona. ¿Qué buscas para saber qué debe hacer cada una?", "Las acotaciones entre paréntesis", "Las rimas", "El título", "Las acotaciones dicen qué hace cada personaje."),
    sc=[("En Lenguaje: ¿qué es un verso?", "Cada línea de un poema", "Cada línea es un verso, y varios versos juntos forman una estrofa."),
        ("¿Qué es el hablante lírico?", "La voz que habla en un poema", "Expresa lo que ve y siente."),
        ("En Lenguaje: ¿qué indica una acotación en una escena?", "Una indicación entre paréntesis para actuar la escena", "La acotación guía a quien representa sobre gestos, lugar y tono de voz.")],
    op=("Escribe una estrofa de cuatro versos sobre el mercado o la feria de tu barrio, y una acotación para una escena corta entre dos personas que se encuentran allí. Usa el modelo de esta clase: {F}",
        "Estrofa: Temprano llega el pregón, / el pan sale del cajón, / los puestos se van llenando / de luz y conversación. Acotación: (Dos vecinos se saludan junto a un puesto de frutas.)",
        ["cuatro versos", "una acotación entre paréntesis", "relacionada con el tema"],
        ["una estrofa y una acotación"],
        ["escribir un párrafo en lugar de versos", "una acotación que no indica acción"],
        "Pregunta: «¿Qué verso suena parecido a otro?»."),
    reinforce="Cuenta los versos de un poema corto que recuerdes.",
    extend="Escribe una escena de dos líneas con una acotación para cada personaje.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy comparo un poema y un cuento paso a paso, con una tabla de criterios y una conclusión.",
    prior=["Conozco forma, hablante lírico y narrador.", "Sé usar criterios.", "Puedo anotar datos en una tabla."],
    explain=[
        "Para comparar dos textos literarios en cinco pasos: lee ambos con atención; elige los criterios; anota en una tabla lo que dice cada texto en cada criterio; mira qué se parece y qué cambia; escribe una conclusión.",
        "Cuatro criterios útiles son la forma (verso o prosa), quién habla (hablante lírico o narrador), qué cuenta o expresa y el ambiente. En un poema, la voz expresa lo que siente; en un cuento, el narrador cuenta hechos.",
        "La conclusión usa una frase como «A se diferencia de B en…, pero se parecen en…». Así tu comparación queda clara para otra persona y apoyada en datos de los textos.",
    ],
    vocab=[("conclusión", "frase final que resume lo que descubriste al comparar"), ("ambiente", "lugar y momento de una historia"), ("expresar", "decir lo que se siente o se piensa"), ("diferencia", "aquello en que dos cosas no son iguales")],
    worked=[
        ("Tabla de comparación", "Poema P (inventado): «Domingo sin prisa, / el patio huele a café; / el tiempo se sienta a mi lado». Cuento Q (inventado): «Don Ariel lavó el auto un domingo. Mientras secaba la carrocería, su vecina le pidió prestada la manguera y los dos conversaron un largo rato».", ["Forma: P, versos; Q, prosa.", "Quién habla: P, el hablante lírico; Q, un narrador.", "Qué cuenta o expresa: P, la calma de un domingo; Q, lo que hacen don Ariel y su vecina."], "Tabla de tres criterios completa"),
        ("Conclusión", "Los mismos textos P y Q.", ["Se parecen en que ocurren un domingo.", "Se diferencian en la forma y en cómo lo comunican."], "P expresa la calma de un domingo y Q cuenta lo que hacen dos vecinos ese día"),
    ],
    mistakes=[("Concluir «A y B son lo mismo porque hablan de esperar».", "Solo se comparó el tema.", "Compara también forma y quién habla antes de concluir."),
              ("Anotar en la tabla ideas que los textos no dicen.", "La comparación se aleja de lo que el texto contiene.", "Relee y copia el dato que respalda cada anotación.")],
    T=[
        ("ab", "{F} ¿Cómo está escrito el Texto A?", "En versos", "En un párrafo", "El Texto A está dividido en cuatro líneas cortas."),
        ("abc", "{F} ¿Quién cuenta lo que hace Aurora?", "Un narrador", "El hablante lírico", "La misma Aurora en primera persona", "El Texto B dice «Aurora esperaba», en tercera persona."),
        ("{F} ¿Cuántos versos tiene el Texto A? Escribe el número.", "4", "El poema tiene cuatro líneas separadas por barras."),
        ("abc", "{F} ¿Qué expresa el hablante del Texto A?", "Que le cuesta esperar y que aprende a hacerlo", "Que llegó a tiempo", "Que conversó con una señora", "Los versos hablan de un tiempo que no anda y de aprender a esperar."),
        ("ab", "{F} ¿Qué cuenta el Texto B?", "Lo que hace Aurora para pasar el tiempo hasta que la llaman", "Cómo se escribe un poema", "El texto cuenta hechos en orden: leer avisos, conversar y ser llamada."),
        ("abc", "{F} ¿En qué se parecen A y B?", "Ambos tratan de esperar", "Ambos tienen narrador", "Ambos están en versos", "El tema común es la espera."),
        ("abc", "{F} Completa la tabla, criterio «ambiente», Texto B.", "Un consultorio, mientras se espera el turno", "Una feria al aire libre", "Una plaza de noche", "El texto dice que Aurora esperaba su turno en el consultorio."),
        ("abc", "Para comparar tenemos cinco pasos. ¿Qué paso va entre «elegir los criterios» y «mirar qué se parece y qué cambia»?", "Anotar en una tabla lo que dice cada texto", "Escribir un final", "Contar las sílabas", "Primero se reúnen los datos y luego se comparan."),
        ("ab", "Alguien concluye: «A y B son lo mismo porque hablan de esperar.» ¿Qué le falta a su comparación?", "Comparar también la forma y quién habla", "Nada, el tema basta", "Con un solo criterio no se puede concluir que son iguales."),
        ("abc", "{F} Al final, Aurora descubre que la espera fue corta. ¿Qué texto muestra ese cambio?", "El Texto B", "El Texto A", "Los dos", "Solo B cuenta lo que pasa cuando la llaman."),
        ("abc", "{F} ¿Qué conclusión compara mejor los textos con criterios?", "A, en versos, expresa lo que se siente al esperar; B, en prosa, cuenta lo que hace Aurora", "A es mejor que B", "Los dos hablan de esperar", "Usa criterios y datos de ambos textos."),
        ("ab", "{F} Una persona busca el texto que cuente qué hizo alguien para pasar el tiempo. ¿Cuál elige?", "El Texto B, porque Aurora lee avisos y conversa", "El Texto A, porque hay una silla", "En B se cuentan acciones concretas para pasar el tiempo."),
        ("{F} ¿Cuál es el último verso del Texto A? Escribe sus tres palabras.", "aprendo a esperar", "El poema termina con el verso «aprendo a esperar»."),
    ],
    ctx=("abc", "Un grupo de lectura debe decidir cuál de dos textos sobre la espera leerá. ¿Cómo apoyas tu opinión?", "Comparo forma, quién habla y qué transmite, y cito un dato de cada texto", "Digo que prefiero el primero porque sí", "Elijo el más largo", "Una opinión justificada usa criterios y datos."),
    sc=[("¿Cuántos pasos tiene el método de comparación de hoy?", "Cinco", "Leer, elegir criterios, anotar, comparar y concluir."),
        ("En Lenguaje: ¿qué es una conclusión al comparar?", "Una frase que resume lo que descubrí", "La conclusión reúne las semejanzas y las diferencias que encontraste en la tabla."),
        ("¿Quién habla en los versos de un poema?", "El hablante lírico", "El hablante lírico es la voz del poema y expresa lo que siente y percibe.")],
    op=("Compara los textos: {F} Haz una tabla con tres criterios (forma, quién habla, qué cuenta o expresa) y escribe una conclusión de dos oraciones que comience con «A se diferencia de B en…».",
        "Forma: A, versos; B, prosa. Quién habla: A, hablante lírico; B, narrador. Qué cuenta: A, cómo se siente esperar; B, qué hace Aurora. Conclusión: A se diferencia de B en que expresa una sensación. Se parecen en que tratan de la espera.",
        ["tabla con tres criterios", "datos de ambos textos", "conclusión con semejanza y diferencia"],
        ["una tabla y dos oraciones"],
        ["concluir sin usar los criterios", "mezclar datos de los textos"],
        "Pregunta: «¿Qué dato del texto apoya tu conclusión?»."),
    reinforce="Compara un poema y un cuento que conozcas con el criterio «quién habla».",
    extend="Agrega el criterio «ambiente» a tu tabla y mira si cambia tu conclusión.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo: comparo un cuento y una escena que cuentan la misma situación.",
    prior=["Comparo con una tabla.", "Reconozco acotaciones.", "Sé qué hace un narrador."],
    explain=[
        "Una misma situación puede escribirse como cuento o como texto dramático. En el cuento, un narrador cuenta lo que pasa y lo que sienten los personajes. En el texto dramático, el lector sabe lo que ocurre por los diálogos y por las acotaciones.",
        "Al comparar estos dos géneros fíjate en qué datos entrega cada uno y cómo los entrega. Por ejemplo, el narrador puede decir «se sorprendió»; en una escena, la acotación puede decir «(sorprendida)» para quien la va a representar.",
        "Cuando practicas en pareja, una persona lee el cuento y la otra lee la escena. Después conversan: ¿qué se entiende igual?, ¿qué cambia al leerlo en voz alta repartiendo las voces?",
    ],
    vocab=[("diálogo", "conversación entre personajes"), ("representar", "actuar una escena frente a otras personas"), ("tono de voz", "manera de decir algo: firme, suave, sorprendida"), ("hecho", "cosa que ocurre en una historia")],
    worked=[
        ("Los hechos son los mismos", "Cuento (inventado): «En el bus, Ana descubrió que había olvidado su billetera. Bruno, tranquilo, le prestó el dinero del pasaje». Escena (inventada): (En un bus. ANA busca en su bolso; BRUNO la observa.) ANA (preocupada): Olvidé mi billetera. BRUNO (tranquilo): Yo te presto el pasaje.", ["Ana olvida la billetera.", "Bruno le presta el pasaje.", "Los dos textos cuentan lo mismo."], "Los dos textos cuentan los mismos hechos"),
        ("Cómo se conoce un sentimiento", "Los mismos textos del bus.", ["En el cuento, el narrador dice «tranquilo» al hablar de Bruno.", "En la escena, la acotación dice «(tranquilo)»."], "El cuento lo cuenta; la escena lo indica"),
    ],
    mistakes=[("Pensar que son textos distintos porque tienen otra forma.", "Cuentan lo mismo, pero lo comunican de otro modo.", "Compara hechos y luego la manera de contarlos."),
              ("Leer las acotaciones en voz alta como parte del diálogo.", "Las acotaciones son una guía, no se dicen.", "Léelas en silencio y úsalas para decir bien cada línea.")],
    T=[
        ("abc", "{F} ¿Cuál texto es dramático?", "El Texto D", "El Texto C", "Ninguno", "El Texto D tiene nombres antes de las palabras y acotaciones."),
        ("ab", "{F} ¿Con qué tono de voz dice Lucas su primera frase en el Texto D?", "Con voz firme", "Con voz alegre", "La acotación dice «(con voz firme)»."),
        ("{F} ¿Cuántos personajes con nombre aparecen en los dos textos? Escribe el número.", "2", "Los dos textos presentan solo a dos personajes con nombre: Eva y Lucas."),
        ("abc", "{F} ¿Qué hechos se cuentan en ambos textos?", "Eva pasa adelante, Lucas se lo hace notar y ella se disculpa", "Lucas pasa adelante y Eva se lo hace notar", "Eva llega tarde al banco y no hace la fila", "Los dos textos cuentan esa secuencia."),
        ("ab", "{F} En el Texto C, ¿quién dice que Eva se sorprendió?", "El narrador", "Lucas", "Es el narrador quien describe lo que siente Eva."),
        ("abc", "{F} ¿Cómo conocemos lo que siente Eva en cada texto?", "En C lo dice el narrador; en D lo indica una acotación", "En C lo dice una acotación; en D lo dice un narrador", "En ninguno se conoce", "La narración y la acotación cumplen funciones distintas."),
        ("{F} En el Texto D, ¿cuántas acotaciones hay entre paréntesis? Escribe el número.", "4", "Son cuatro grupos entre paréntesis: la presentación, «con voz firme», «sorprendida» y «EVA vuelve a su lugar»."),
        ("abc", "Quieres representar el Texto D con otra persona. ¿Qué necesitan decidir?", "Quién dice las líneas de Eva y quién las de Lucas", "Quién es el narrador", "Cuántos versos tiene", "En un texto dramático se reparten los personajes."),
        ("ab", "{F} ¿Cómo termina el Texto D?", "Eva vuelve a su lugar", "Lucas se va del banco", "La última acotación dice «(EVA vuelve a su lugar.)»."),
        ("ab", "Marta dice: «El Texto C y el D no se parecen porque uno es cuento y el otro escena.» ¿Quién tiene razón?", "Se parecen: cuentan los mismos hechos, aunque en distinta forma", "Marta, porque el género cambia todo", "Comparten hechos y personajes; cambia la manera de contarlos."),
        ("abc", "{F} ¿Por qué el Texto D no necesita escribir «Eva se sorprendió» como el Texto C?", "Porque la acotación (sorprendida) y la actuación lo muestran", "Porque Eva no se sorprende", "Porque el narrador lo dice después", "En el teatro quien actúa muestra los sentimientos."),
        ("abc", "{F} Dos personas quieren leer en voz alta repartiendo las voces. ¿Qué texto eligen?", "El Texto D", "El Texto C", "Ninguno", "Las voces se reparten por personaje en un texto dramático."),
        ("ab", "{F} Si en el Texto C se agregara «Un guardia pidió calma», ¿qué cambiaría en la comparación?", "Los personajes, porque habría uno más", "El género, que pasaría a ser poema", "Un guardia nuevo sería otro personaje."),
    ],
    ctx=("abc", "En un grupo de lectura proponen representar una escena corta entre dos personas. ¿Qué texto te sirve?", "Uno dramático, con diálogos y acotaciones", "Un poema sin personajes", "Un cuento largo sin diálogos", "El texto dramático está hecho para representarse."),
    sc=[("En Lenguaje: ¿qué es un diálogo?", "Una conversación entre personajes", "En la escena se escribe con el nombre antes de cada línea."),
        ("¿Qué hace un narrador que no hace un texto dramático?", "Cuenta lo que ocurre y lo que sienten los personajes", "En el teatro se muestran en diálogos y acotaciones."),
        ("¿Cómo se leen las acotaciones?", "En silencio, como guía", "Las acotaciones se leen en silencio como guía y no se dicen en voz alta.")],
    op=("Con los textos: {F} Escribe en tu cuaderno dos semejanzas y dos diferencias entre el Texto C y el D, y después una frase que diga cuál te parece más fácil de representar.",
        "Semejanzas: tienen los mismos hechos; tienen los mismos personajes. Diferencias: C tiene narrador; D tiene acotaciones. El D es más fácil de representar porque cada persona sabe qué decir.",
        ["dos semejanzas", "dos diferencias", "una frase con motivo"],
        ["una lista y una frase"],
        ["dar diferencias que no están en los textos", "no dar motivo"],
        "Pregunta: «¿Esto lo dicen los textos?»."),
    reinforce="Elige una situación breve de tu día y cuéntala en dos oraciones, como cuento.",
    extend="Reescribe esa situación como una escena de tres líneas con una acotación.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico la comparación en una situación real: armar una jornada de lectura de barrio con un poema, un cuento y una escena.",
    prior=["Reconozco poesía, narrativa y texto dramático.", "Comparo con criterios.", "He participado o puedo imaginar una lectura en grupo."],
    explain=[
        "Imagina que una biblioteca de barrio prepara una jornada de lectura con tres momentos: abrir, contar y representar. Para decidir qué texto va en cada momento, comparas con criterios.",
        "Un poema breve sirve para abrir, porque se lee rápido y crea un ambiente. Un cuento sirve para contar, porque tiene hechos y personajes. Una escena sirve para representar, porque tiene voces repartidas y acotaciones.",
        "Antes de decidir, revisa también el tiempo y las personas disponibles. Si hay una sola persona para leer, una escena de dos personajes no se puede representar completa.",
    ],
    vocab=[("jornada", "actividad que ocupa un tiempo determinado"), ("selección", "conjunto de textos elegidos"), ("público", "personas que escuchan o ven una lectura"), ("breve", "corto, que ocupa poco tiempo")],
    worked=[
        ("Elegir el texto para abrir", "Opciones (inventadas): un poema de seis versos que se lee en 1 minuto, un cuento de 5 minutos y una escena de 3 minutos. Para abrir quedan 2 minutos.", ["Busco un texto que cree ambiente y cuyo tiempo no pase de 2 minutos.", "Solo el poema, de 1 minuto, cabe."], "Se abre con el poema de 1 minuto"),
        ("Elegir el texto para representar", "Las mismas opciones: poema de 1 minuto, cuento de 5 y escena de 3. Hay dos personas y 4 minutos para representar.", ["Busco voces repartidas entre dos personas.", "La escena dura 3 minutos y cabe en 4."], "Se representa la escena de 3 minutos"),
    ],
    mistakes=[("Elegir un texto sin pensar en quién lo va a leer.", "Una escena de dos personajes necesita dos personas.", "Revisa cuántas personas pueden participar."),
              ("Elegir por el título más bonito.", "El título no dice cómo está escrito el texto ni qué hace.", "Lee y compara con criterios.")],
    T=[
        ("abc", "{F} ¿Qué texto se escribió en versos?", "«Barrio»", "«El banco de la plaza»", "«La llave del salón»", "«Barrio» es un poema y está en versos."),
        ("ab", "{F} ¿Qué texto tiene acotaciones?", "«La llave del salón»", "«Barrio»", "Los paréntesis con indicaciones aparecen solo en la escena."),
        ("{F} ¿Cuántos versos tiene el poema «Barrio»? Escribe el número.", "4", "Hay cuatro líneas separadas por barras."),
        ("abc", "{F} ¿Qué hace Mateo con el letrero?", "Lo saca después de ver que la madera está seca", "Lo pega en otro lugar", "Pinta el banco", "El cuento dice que sacó el letrero y le ofreció sentarse."),
        ("ab", "{F} ¿Qué texto conviene para abrir la jornada con un momento breve y de ambiente?", "El poema «Barrio»", "La escena «La llave del salón»", "El poema es breve y expresa sensaciones."),
        ("abc", "{F} ¿Cuántas personas se necesitan para representar la escena completa?", "Dos", "Una", "Cuatro", "En la escena hablan Inés y Tomás, así que se necesitan dos personas para las voces."),
        ("abc", "{F} Hay solo una persona para leer. ¿Qué texto sirve mejor para leer sola?", "El cuento «El banco de la plaza»", "La escena completa", "Ninguno", "El cuento lo cuenta un narrador y puede leerlo una persona."),
        ("abc", "{F} El público quiere escuchar un texto que muestre una acción amable de una persona hacia otra. ¿Cuál elige?", "El cuento «El banco de la plaza»", "El poema «Barrio»", "La escena, porque tiene una llave", "Mateo ofrece el banco a una señora cansada."),
        ("abc", "{F} Quieres un texto que describa sensaciones del barrio sin contar una historia. ¿Cuál es?", "El poema «Barrio»", "El cuento «El banco de la plaza»", "La escena «La llave del salón»", "El poema expresa imágenes del barrio."),
        ("ab", "{F} Ana elige «La llave del salón» porque tiene dos voces y acotaciones para representarla. ¿Es una buena razón?", "Sí, porque apoya su elección en cómo es el texto", "No, porque las escenas no se pueden representar", "Menciona un dato del texto: dos voces y acotaciones."),
        ("abc", "{F} ¿Qué texto ayuda a que el público sienta la tarde del barrio con pocas palabras?", "El poema «Barrio»", "La escena", "El cuento", "El poema nombra el farol, el ruido y los vecinos en pocos versos."),
        ("abc", "{F} Alguien propone leer los tres textos en este orden: escena, poema, cuento. ¿Qué orden mantiene la jornada «abrir, contar, representar»?", "Poema, cuento, escena", "Escena, poema, cuento", "Cuento, escena, poema", "Se abre con el poema, se cuenta con el cuento y se representa la escena."),
        ("=", "La jornada dura 10 minutos. El poema se lee en 1 minuto, el cuento en 5 y la escena en 3. ¿Cuántos minutos sobran?", "10-(1+5+3)", "Los tres textos suman 9 minutos y la jornada dura 10, por lo que sobra 1.", "minutos"),
    ],
    ctx=("abc", "Te piden elegir un texto para que dos vecinos lo representen en la sede vecinal. ¿Qué eliges?", "Una escena con dos personajes y acotaciones", "Un poema de cuatro versos", "Un cuento largo", "La escena se escribe para ser representada por dos."),
    sc=[("¿Qué texto sirve para abrir una jornada con pocas palabras?", "Un poema breve", "Se lee rápido y crea ambiente."),
        ("¿Qué texto sirve para representar?", "Una escena con acotaciones", "Una escena reparte las voces entre personajes y trae acotaciones para actuar."),
        ("¿Qué reviso antes de elegir?", "Tiempo, personas y tipo de texto", "El tiempo y las personas disponibles son condiciones reales que limitan lo que se puede leer.")],
    op=("Con la selección: {F} Escribe en tu cuaderno qué texto elegirías para abrir, para contar y para representar en una jornada de lectura, y un motivo para cada uno.",
        "Abrir: el poema «Barrio», porque es breve. Contar: el cuento «El banco de la plaza», porque tiene hechos. Representar: la escena, porque tiene dos voces y acotaciones.",
        ["tres elecciones", "un motivo por texto", "motivos con datos del texto"],
        ["tres líneas con motivo"],
        ["no dar motivos", "poner el mismo texto en dos momentos"],
        "Pregunta: «¿Qué rasgo del texto te hizo elegirlo?»."),
    reinforce="Imagina otra jornada de lectura y di qué tipo de texto pondrías al inicio.",
    extend="Escribe un cuarto texto breve para la jornada y di en qué momento lo pondrías.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo logrado: comparo tres textos de géneros distintos con una ficha y decido qué quiero repasar.",
    prior=["Reconozco los tres géneros.", "Sé comparar con tabla.", "Puedo explicar una preferencia."],
    explain=[
        "Revisar es volver sobre lo hecho para ver cómo te fue. En estas clases aprendiste a comparar textos con criterios: forma, quién habla, qué cuentan o expresan y ambiente. Hoy los usas con tres textos a la vez.",
        "Cuando alguien lee en voz alta, también puedes comparar: escuchas con atención, anotas una palabra por criterio y luego completas la tabla. En un poema anotas sensación y voz; en un cuento, personajes y problema; en una escena, personajes y acotaciones.",
        "Al final, escribe qué te sale bien, qué quieres practicar y cómo lo harás. Eso te ayuda a decidir tus próximos pasos con calma.",
    ],
    vocab=[("ficha de comparación", "tabla con criterios y datos de cada texto"), ("escuchar con atención", "seguir lo que se lee para recordarlo y entenderlo"), ("repasar", "volver a practicar algo"), ("balance", "revisión de lo que se logró")],
    worked=[
        ("Completar la ficha de tres textos", "Poema (inventado): «Sale el sol, / la calle despierta / y el pan se calienta». Cuento (inventado): «Manuel abrió el taller y encendió la radio. Los primeros clientes ya hacían fila». Escena (inventada): (En un taller. MANUEL ordena herramientas.) CLIENTE: ¿Está abierto? MANUEL (sonriendo): Pase.", ["Forma: poema, versos; cuento, prosa; escena, diálogo y acotaciones.", "Quién habla: poema, hablante lírico; cuento, narrador; escena, personajes."], "Ficha con dos criterios"),
        ("Tomar notas al escuchar", "Alguien lee en voz alta: «La funcionaria revisó el papel y le explicó el error.»", ["Anoto: funcionaria; papel; error explicado.", "Esas notas recogen personaje, objeto y hecho."], "Notas breves del Texto 2"),
    ],
    mistakes=[("Comparar con un solo criterio.", "Con un solo criterio la comparación queda incompleta.", "Usa al menos tres criterios."),
              ("Escribir una meta vaga como «mejorar».", "No dice qué práctica harás.", "Escribe una acción: «compararé dos textos por semana».")],
    T=[
        ("abc", "{F} ¿Qué texto es un poema?", "El Texto 1", "El Texto 2", "El Texto 3", "El Texto 1 está en versos."),
        ("ab", "{F} ¿Cuántos personajes actúan en el Texto 3?", "Dos: Sofía y Daniel", "Uno: Sofía", "Aparecen Sofía con los paquetes y Daniel sosteniendo la puerta."),
        ("{F} ¿A qué hora llegó Gabriela a la municipalidad? Escribe el número.", "8", "El texto dice que llegó a las ocho."),
        ("abc", "{F} ¿Qué error ocurrió en el Texto 2?", "Gabriela llegó una hora antes de su turno", "Gabriela llegó una hora después", "La funcionaria se equivocó de nombre", "Su hora era a las nueve y llegó a las ocho."),
        ("ab", "{F} ¿Qué texto tiene acotaciones?", "El Texto 3", "El Texto 2", "Los paréntesis con indicaciones están en la escena."),
        ("abc", "{F} ¿Quién habla en el Texto 1?", "El hablante lírico, que expresa lo que ve al volver a casa", "Un narrador que cuenta lo que hace Gabriela", "Sofía y Daniel", "El hablante lírico es la voz que habla en el poema y expresa lo que ve y siente."),
        ("abc", "{F} Compara la forma. ¿Qué es correcto?", "Texto 1, versos; Texto 2, prosa; Texto 3, diálogo con acotaciones", "Texto 1, prosa; Texto 2, versos; Texto 3, prosa", "Los tres están en versos", "Cada texto usa una forma distinta."),
        ("{F} ¿Cuántos versos tiene el Texto 1? Escribe el número.", "4", "Hay cuatro líneas separadas por barras."),
        ("abc", "{F} Quieres el texto que muestre una situación de trámite con un problema resuelto con paciencia. ¿Cuál eliges?", "El Texto 2", "El Texto 1", "El Texto 3", "Gabriela espera una hora y le explican el error."),
        ("ab", "Marcos escribe: «El 1 y el 3 son del mismo género porque los dos ocurren en un lugar del barrio.» ¿Es correcto?", "No: el lugar no define el género; uno está en versos y el otro tiene diálogo", "Sí, porque ambos ocurren en un lugar del barrio", "El género depende de cómo está escrito el texto, no del lugar."),
        ("abc", "Escuchas: «Cuando la llamaron, Gabriela agradeció la explicación.» ¿Qué nota es mejor?", "Gabriela; la llaman; agradece", "Todo el texto de nuevo", "La funcionaria es amable porque sí", "Una nota breve recoge a la persona y los hechos."),
        ("abc", "Una meta clara para repasar es", "Compararé dos textos por semana con tres criterios", "Mejoraré mucho", "Leeré más o menos", "Las otras opciones no dicen qué se hará."),
        ("ab", "{F} Después de comparar, ¿qué dato apoya decir que el Texto 3 es el más fácil de representar entre dos personas?", "Tiene dos personajes con líneas y acotaciones", "Tiene cuatro versos", "Los versos son del Texto 1; el Texto 3 tiene personajes y acotaciones."),
    ],
    ctx=("abc", "Escuchas a una persona leer en voz alta un texto y después tienes que compararlo con otro. ¿Qué haces mientras escuchas?", "Anoto palabras clave por criterio", "Copio cada palabra", "No anoto nada", "Las notas breves ayudan a completar la ficha."),
    sc=[("¿Qué criterios usé para comparar textos?", "Tema, forma, quién habla y qué cuentan o expresan", "Son los criterios de la ficha."),
        ("¿Qué hago al terminar de comparar?", "Escribo una conclusión", "La conclusión resume lo que descubrí al comparar y cierra el trabajo."),
        ("¿Qué anoto al escuchar un poema leído en voz alta?", "La sensación que expresa y la voz que habla", "En un poema importan la sensación y la voz; los hechos de personajes no son lo central.")],
    op=("Revisa: {F} Haz una ficha con los criterios forma, quién habla y qué cuentan o expresan, para los tres textos. Escribe una meta para practicar esta semana.",
        "Forma: 1, versos; 2, prosa; 3, diálogo. Quién habla: 1, hablante lírico; 2, narrador; 3, personajes. Qué cuentan: 1, el camino a casa; 2, un error de hora; 3, un gesto amable. Meta: compararé dos textos por semana.",
        ["tres criterios para tres textos", "datos correctos", "una meta concreta"],
        ["una tabla y una meta"],
        ["llenar solo un texto", "meta vaga"],
        "Pregunta: «¿Cómo vas a practicar eso?»."),
    reinforce="Compara dos textos breves que encuentres hoy con un criterio.",
    extend="Escribe un texto breve en cada género sobre el mismo tema y compáralos.",
)
