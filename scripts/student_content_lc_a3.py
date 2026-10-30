"""Student material for 1.º básico Lengua y Cultura de los Pueblos Originarios Ancestrales, OA 11 (mensajes de la naturaleza) y OA 12 (eventos socioculturales y ceremoniales)."""
from __future__ import annotations

from student_content_lc_a1 import L, M, T, W
from student_lessons import ex

OA11, OA12 = "LC01 OA 11", "LC01 OA 12"

# ============================================================ OA 11 · Mensajes de la naturaleza en la cosmovisión
L(
    OA11, 1,
    materials="Lápiz y hojas. Las escenas de la naturaleza están escritas en el cuaderno; son ejemplos inventados para practicar.",
    use="Aprenderé a describir con exactitud lo que veo, oigo o siento en la naturaleza antes de interpretarlo. Sirve para no apurarme en decir qué significa.",
    prior=["Sé usar mis sentidos: ver, oír, tocar, oler.", "Sé nombrar colores, formas y sonidos."],
    explain=[
        "En la cosmovisión de muchos pueblos originarios, la naturaleza puede «hablar»: el cielo, el viento, los animales o las plantas pueden mostrar señales que las personas observan con atención. La cosmovisión es la manera en que un pueblo entiende el mundo.",
        "Antes de pensar qué significa algo, hay que describir bien lo que pasó. Describir es decir qué veo, qué oigo y cuándo ocurre, sin agregar mi opinión. Por ejemplo: «hoy a las ocho hay nubes grises y sopla viento fuerte». Eso es una descripción.",
        "Interpretar es decir qué significa. La interpretación cultural no la inventamos nosotros: la enseñan las personas que conocen esa cultura. Por eso primero describimos y después preguntamos qué significa a quien sabe. Si no hay quién nos lo explique, decimos «no lo sé todavía».",
    ],
    vocab=[("cosmovisión", "manera en que un pueblo entiende el mundo y la vida"), ("señal", "algo de la naturaleza que se observa con atención"), ("describir", "decir lo que veo, oigo o siento, sin opinión"), ("interpretar", "decir qué significa algo"), ("fenómeno", "algo que ocurre en la naturaleza, como la lluvia o el viento")],
    worked=[
        W("Describir sin interpretar", "Escena de práctica: «A las ocho de la mañana, una bandada de pájaros vuela hacia el sur». ¿Cuál es una descripción? A) «Vuelan hacia el sur a las ocho» B) «Anuncian lluvia»", ["Describir es decir lo que se ve y cuándo.", "A dice lo que se ve y la hora.", "B ya interpreta sin fuente."], "A"),
        W("Anotar un fenómeno", "Hay nubes grises, viento suave y 12 gotas caen en un vaso en una hora. ¿Qué anotas?", ["Anoto el cielo: nubes grises.", "Anoto el viento: suave.", "Anoto el dato medido: 12 gotas en una hora."], "Nubes grises, viento suave, 12 gotas en una hora."),
    ],
    mistakes=[
        M("Decir qué significa una señal sin haberla descrito bien.", "Se pierde lo que realmente pasó.", "Describe primero: qué, dónde y cuándo."),
        M("Inventar un significado cultural.", "Solo quien conoce la cultura puede explicarlo.", "Escribe «pregunta pendiente» y consulta al educador tradicional."),
    ],
    R=[
        ex("Describir es decir lo que veo u oigo. ¿Verdadero o falso?", "Verdadero", "Eso es describir."),
        ex("«Hay viento fuerte». ¿Es descripción o interpretación?", "Descripción", "Dice lo que se siente, sin significado."),
        ex("«Eso significa que viene una desgracia». ¿Es descripción o interpretación?", "Interpretación", "Dice qué significa."),
    ],
    C=[
        ex("¿Qué se hace primero? A) describir B) interpretar", "A", "Primero se observa bien."),
        ex("Verdadero o falso: puedo inventar el significado cultural de una señal.", "Falso", "Lo enseñan quienes conocen la cultura."),
        ex("¿Qué es la cosmovisión?", "La manera en que un pueblo entiende el mundo", "Es la mirada de un pueblo sobre la vida."),
    ],
    A=[
        ex("Clasifica como DESCRIPCIÓN o INTERPRETACIÓN: a) «Las nubes son grises» b) «Las nubes anuncian una fiesta» c) «El río suena fuerte».", "a) descripción, b) interpretación, c) descripción", "Solo la b dice un significado."),
        ex("Escena de práctica: «A las seis de la tarde, el cielo está naranja y hay 3 nubes pequeñas». Escribe la descripción con la hora.", "A las seis de la tarde, el cielo está naranja y hay 3 nubes pequeñas", "Incluye hora, color y cantidad."),
        ex("Ordena: 1) pregunto qué significa 2) describo lo que pasó 3) anoto la respuesta con la fuente.", "2, 1, 3", "Primero describir, luego preguntar y por último anotar."),
    ],
    Z=[
        ex("Ana dice: «El viento fuerte es una mala señal». ¿Qué le falta para decir eso?", "Una fuente cultural que lo enseñe", "No basta con suponer."),
        ex("¿Por qué conviene anotar la hora y el lugar de lo que observamos?", "Porque ayuda a describir con exactitud", "Sin hora ni lugar no se puede revisar."),
    ],
    D=[
        ex("Pedro anotó: «Hay mucha lluvia, el cielo está raro y seguro es un mensaje». ¿Qué parte sobra en la descripción?", "«Seguro es un mensaje»", "Es una interpretación sin fuente."),
        ex("Una niña observa 2 aves el lunes y 5 aves el martes. ¿Cuántas aves observó en total?", "7", "2 + 5 = 7 aves."),
    ],
    context=[ex("Escena de práctica: «Hoy a las nueve, el sol sale entre nubes y sopla viento del sur». Escribe cuántos elementos distintos del paisaje se describen.", "3", "Sol, nubes y viento son tres elementos.")],
    selfcheck=[ex("¿Qué haces antes de interpretar?", "Describo", "Primero se observa."), ex("¿Quién enseña el significado cultural?", "Quien conoce esa cultura", "Ellos saben su sentido."), ex("Si no sé qué significa, ¿qué digo?", "No lo sé todavía", "No se inventa.")],
    task=T("Mira por la ventana o el patio durante 5 minutos (o usa esta escena de práctica: «A las diez, el cielo tiene nubes blancas, sopla viento suave y un pájaro canta en un árbol»). Escribe una descripción con hora, lugar y tres cosas que ves u oyes. Termina con una pregunta pendiente para el educador tradicional.",
           "A las diez, en el patio, vi nubes blancas, sentí viento suave y oí un pájaro. Pregunta: ¿qué se dice en la comunidad sobre el canto de los pájaros?",
           ["describe con hora y lugar", "no interpreta", "formula una pregunta pendiente"], ["texto breve", "pregunta"], ["agregar un significado inventado"],
           "Revisa que la descripción no incluya interpretaciones; valora la pregunta."),
    reinforce="Describe en voz alta tres cosas que ves desde tu ventana, sin decir qué significan.",
    extend="Escribe dos preguntas para un adulto de tu comunidad sobre cómo mira su pueblo lo que ocurre en el cielo.",
)

L(
    OA11, 2,
    materials="Lápiz y hojas. Una tabla de fuentes y un caso están escritos en el cuaderno. La educadora Marta es un personaje inventado para practicar.",
    use="Aprenderé a identificar quién puede enseñar el significado de una señal de la naturaleza y de dónde viene ese saber.",
    prior=["Sé la diferencia entre describir e interpretar.", "Sé qué es una fuente."],
    explain=[
        "El significado que un pueblo da a un fenómeno de la naturaleza forma parte de su cultura. Lo enseñan quienes conocen y viven esa cultura: personas mayores, sabios y sabias de la comunidad y educadores tradicionales. Ellos saben de dónde viene ese saber.",
        "Una fuente cultural confiable se reconoce porque dice quién enseñó, de qué pueblo es y en qué contexto. Un video de internet sin nombre, una foto con frase bonita o un comentario de alguien que no es de la comunidad no son fuentes confiables.",
        "Cuando recibimos una explicación, anotamos tres cosas: quién la dijo, de qué pueblo habla y cuándo o dónde se practica. Así no atribuimos a «los indígenas» algo que enseñó una sola comunidad y respetamos a quien lo compartió.",
    ],
    vocab=[("fuente cultural", "persona o texto que enseña un saber de un pueblo"), ("educador tradicional", "persona de la comunidad que enseña su cultura en la escuela"), ("contexto", "dónde, cuándo y para qué se dice algo"), ("atribuir", "decir de quién es un saber"), ("confiable", "que merece confianza")],
    worked=[
        W("Elegir la fuente", "Dos fuentes: A) un video sin autor con una frase bonita; B) la explicación de la educadora tradicional de la escuela. ¿Cuál es más confiable?", ["B dice quién enseña y de qué pueblo.", "A no dice nada de su origen.", "Elijo B."], "B"),
        W("Anotar lo importante", "La educadora tradicional te cuenta algo sobre su comunidad. ¿Qué tres datos anotas?", ["Quién lo dijo.", "De qué pueblo o comunidad habla.", "Cuándo o dónde se practica."], "Quién, de qué pueblo y cuándo o dónde."),
    ],
    mistakes=[
        M("Decir «los indígenas creen…» con lo que dijo una sola persona.", "Cada pueblo y comunidad tiene su saber.", "Di de qué pueblo y comunidad habla la fuente."),
        M("Usar un video sin autor como fuente.", "No sabemos quién enseña ni si es cierto.", "Pide a una persona de la comunidad o al educador tradicional."),
    ],
    R=[
        ex("¿Quién puede enseñar el significado de una señal de su cultura? A) la comunidad y el educador tradicional B) cualquiera que lo adivine", "A", "Ellos conocen ese saber."),
        ex("¿Un video sin autor es una fuente confiable? Sí o No.", "No", "No dice quién enseña."),
        ex("Un educador tradicional enseña su cultura. ¿Verdadero o falso?", "Verdadero", "Esa es su tarea."),
    ],
    C=[
        ex("¿Qué dato NO es parte de una fuente confiable? A) quién lo dijo B) un adorno bonito", "B", "Lo bonito no dice de dónde viene."),
        ex("Verdadero o falso: lo que dijo una persona vale para todos los pueblos.", "Falso", "Cada pueblo tiene su saber."),
        ex("¿Qué tres datos se anotan al recibir una explicación?", "Quién, de qué pueblo y cuándo o dónde", "Así se atribuye bien."),
    ],
    A=[
        ex("¿Cuál de estas fuentes es la más confiable? A) un video sin autor B) la educadora tradicional de la escuela C) un comentario anónimo", "B", "Es la que dice quién enseña y de qué pueblo; las otras no tienen autor."),
        ex("Une cada fuente con su valor. 1) libro con autor y pueblo 2) mensaje sin nombre. a) confiable b) poco confiable", "1-a, 2-b", "El libro dice quién escribió y de qué pueblo."),
        ex("La educadora Marta, de una comunidad, cuenta algo a tu curso. Escribe cómo anotas la fuente: «Según ______, de su comunidad».", "la educadora Marta", "Se anota el nombre de quien enseñó."),
    ],
    Z=[
        ex("Tomás dice que «todos los pueblos creen lo mismo» sobre las señales. ¿Qué le respondes?", "Que cada pueblo tiene su propio saber", "No se generaliza."),
        ex("¿Por qué es importante decir quién enseñó algo?", "Para respetar a esa persona y no atribuirlo a todos", "Así se cuida la fuente."),
    ],
    D=[
        ex("Una persona que no es de la comunidad explica con seguridad el significado de una señal. ¿Qué haces?", "Pregunto a alguien de la comunidad o al educador", "La explicación debe venir de quien conoce el saber."),
        ex("Dos fuentes confiables dan explicaciones un poco distintas. ¿Qué haces?", "Las anoto y pregunto, sin elegir una por mí", "Puede haber diferencias entre comunidades."),
    ],
    context=[ex("Tu curso invitó a un educador tradicional. Antes de su visita, preparan 3 preguntas y él responde 2. ¿Cuántas preguntas quedan para otra visita?", "1", "3 − 2 = 1 pregunta pendiente.")],
    selfcheck=[ex("¿Quién enseña el significado?", "Quien conoce esa cultura", "Ellos saben su origen."), ex("¿Qué es un contexto?", "Dónde, cuándo y para qué se dice algo", "Da sentido al saber."), ex("¿Se puede atribuir a todos lo que dijo uno?", "No", "Se dice de qué pueblo es.")],
    task=T("Prepara tres preguntas para el educador tradicional o para una persona mayor de tu comunidad sobre cómo se mira una señal de la naturaleza (el cielo, el viento, un animal). Antes de preguntar, escribe cómo vas a anotar la fuente: quién respondió, de qué pueblo habla y cuándo. Si no puedes preguntar a nadie, escribe las preguntas y déjalas para cuando puedas.",
           "Preguntas: 1) ¿qué se observa del cielo en esta época? 2) ¿quién enseña eso en su comunidad? 3) ¿se puede compartir? Fuente: nombre de la persona, su pueblo y la fecha.",
           ["formula preguntas respetuosas", "prepara la forma de anotar la fuente", "no responde por la comunidad"], ["tres preguntas", "formato de fuente"], ["responder él mismo las preguntas"],
           "Valora las preguntas; no completar las respuestas desde la sala sin la voz de la comunidad."),
    reinforce="Practica en voz alta cómo presentarte y pedir permiso para preguntar a una persona mayor.",
    extend="Escribe una pregunta sobre si lo que te enseñan se puede compartir con el curso.",
)

L(
    OA11, 3,
    materials="Lápiz y hojas. Casos de práctica inventados están escritos en el cuaderno.",
    use="Aprenderé a relacionar lo que se observa en la naturaleza con el momento del año y con las decisiones que toman las personas.",
    prior=["Sé las estaciones del año.", "Sé qué es sembrar y cosechar."],
    explain=[
        "En muchos pueblos originarios, observar la naturaleza ayuda a decidir qué hacer y cuándo. Por ejemplo, mirar el cielo, la luna, las plantas o los animales ayuda a decidir cuándo sembrar o cosechar. Cada pueblo tiene sus formas de observar y sus tiempos.",
        "Para entender una señal necesitamos tres cosas: qué se observa, cuándo ocurre en el año y qué hace la gente después. Por ejemplo, un caso de práctica: «Cuando florece el arbusto del patio, la familia empieza a sembrar». Eso une señal, tiempo y acción.",
        "No todas las señales significan lo mismo en todos los lugares. Una señal del norte puede no valer en el sur. Y una decisión importante no se toma solo por una señal: se conversa con los mayores y se usa la experiencia de la comunidad.",
    ],
    vocab=[("señal", "algo que se observa y orienta una decisión"), ("tiempo del año", "estación o mes en que ocurre algo"), ("decisión", "elegir qué hacer"), ("sembrar", "poner semillas en la tierra"), ("experiencia", "lo aprendido por haber vivido muchas veces algo")],
    worked=[
        W("Señal, tiempo y acción", "Caso de práctica: «En primavera florece el arbusto del patio y la familia empieza a sembrar». ¿Cuáles son la señal, el tiempo y la acción?", ["Señal: florece el arbusto.", "Tiempo: primavera.", "Acción: empezar a sembrar."], "Señal: florece el arbusto; tiempo: primavera; acción: sembrar."),
        W("Cuidado con generalizar", "Marta dice: «Si florece este arbusto, todos los pueblos siembran». ¿Está bien?", ["Esa señal es de un caso de práctica.", "Cada lugar tiene sus señales.", "No se puede generalizar."], "No."),
    ],
    mistakes=[
        M("Decidir algo importante solo por una señal.", "Las decisiones se conversan con los mayores.", "Pregunta y usa la experiencia de la comunidad."),
        M("Creer que una señal vale para todos los lugares.", "Cada lugar tiene sus propias señales.", "Di dónde y para quién vale."),
    ],
    R=[
        ex("Caso de práctica: «Florece el arbusto, la familia siembra». ¿Cuál es la acción?", "Sembrar", "Es lo que hace la familia."),
        ex("Primavera, verano, otoño e invierno son estaciones. ¿Cuántas son?", "4", "Se cuentan cuatro estaciones."),
        ex("¿Sembrar es poner semillas en la tierra? Sí o No.", "Sí", "Esa es la definición."),
    ],
    C=[
        ex("¿Qué tres cosas se relacionan en una señal? A) señal, tiempo y acción B) color, forma y tamaño", "A", "Se une lo que se observa, cuándo y qué se hace."),
        ex("Verdadero o falso: una señal vale igual en todos los lugares.", "Falso", "Cada lugar tiene sus señales."),
        ex("¿Con quién se conversa una decisión importante?", "Con los mayores y la comunidad", "Ellos tienen experiencia."),
    ],
    A=[
        ex("Caso de práctica: «Cuando caen las primeras lluvias de otoño, el vecino guarda la leña». Escribe señal, tiempo y acción.", "Señal: primeras lluvias; tiempo: otoño; acción: guardar la leña", "Cada parte está en la frase."),
        ex("En este caso de práctica, une cada señal con su acción. 1) hace calor y salen hojas nuevas 2) caen lluvias fuertes. a) regar menos b) sembrar", "1-b, 2-a", "En este caso de práctica, las hojas nuevas invitan a sembrar y la lluvia fuerte a regar menos."),
        ex("Ordena una decisión: 1) converso con los mayores 2) observo la señal 3) decido qué hacer.", "2, 1, 3", "Observar, conversar y después decidir."),
    ],
    Z=[
        ex("Pedro decide sembrar solo porque vio una flor. ¿Qué le falta?", "Conversar con los mayores", "La experiencia de la comunidad orienta la decisión."),
        ex("¿Por qué anotamos el lugar de una señal?", "Porque cambia según el lugar", "No es igual en todas partes."),
    ],
    D=[
        ex("Un niño del sur aplica una señal del norte. ¿Es seguro que valga? Sí o No.", "No", "Los lugares son distintos."),
        ex("Si una familia siembra el 1 de septiembre y cosecha 90 días después, ¿cuántos días pasan entre siembra y cosecha?", "90", "Es el dato dado, 90 días."),
    ],
    context=[ex("Caso de práctica: «El abuelo mira el cielo, conversa con su hijo y deciden sembrar mañana». ¿Cuántas personas participan en la decisión?", "2", "El abuelo y su hijo.")],
    selfcheck=[ex("¿Qué se relaciona en una señal?", "Señal, tiempo y acción", "Es lo que se une."), ex("¿Una señal vale en todos los lugares?", "No", "Depende del lugar."), ex("¿Con quién conversas una decisión importante?", "Con los mayores", "Ellos tienen experiencia.")],
    task=T("Usa este caso de práctica: «Cuando aparecen las primeras hojas nuevas en el árbol del patio, es primavera y la familia prepara la tierra». Dibuja tres cuadros: la señal, el tiempo del año y la acción. Escribe una pregunta para el educador tradicional sobre qué señales usa su comunidad.",
           "Cuadro 1: hojas nuevas. Cuadro 2: primavera. Cuadro 3: preparar la tierra. Pregunta: ¿qué señales usan en mi comunidad?",
           ["separa señal, tiempo y acción", "usa el caso dado", "formula una pregunta"], ["tres cuadros", "pregunta"], ["atribuir el caso a un pueblo real"],
           "Aclara que el caso es de práctica y no representa a un pueblo; valora la pregunta."),
    reinforce="Nombra tres señales de la naturaleza que veas en tu barrio, sin decir su significado.",
    extend="Pregunta a un adulto qué hace en cada estación para cuidar la tierra y anota su respuesta con permiso.",
)

L(
    OA11, 4,
    materials="Lápiz y hojas. Un modelo de ficha de tres datos está escrito en el cuaderno. La educadora Marta es un personaje inventado para practicar.",
    use="Aprenderé a explicar a otras personas lo que aprendí sobre las señales de la naturaleza, diciendo de dónde viene y hasta dónde vale.",
    prior=["Sé separar descripción e interpretación.", "Sé citar la fuente."],
    explain=[
        "Comunicar un saber cultural exige cuidado. Decimos qué observamos, quién nos enseñó el significado y de qué pueblo o comunidad es. Eso se llama procedencia. Así nadie cree que hablamos de todos los pueblos.",
        "También decimos el alcance: hasta dónde vale lo que contamos. Por ejemplo, «según la educadora de mi escuela, en su comunidad se mira el cielo antes de sembrar». Eso no quiere decir que todas las comunidades lo hagan igual.",
        "Si no estamos seguros de algo, lo decimos con honestidad: «esto no lo sé» o «lo voy a preguntar». Una explicación con procedencia y alcance respeta a quien nos enseñó y a quienes nos escuchan.",
    ],
    vocab=[("procedencia", "de dónde y de quién viene un saber"), ("alcance", "hasta dónde vale lo que se dice"), ("comunicar", "contar algo a otras personas"), ("honestidad", "decir lo que sé y lo que no sé"), ("generalizar", "decir que algo vale para todos")],
    worked=[
        W("Decir procedencia y alcance", "La educadora Marta contó cómo su comunidad mira el cielo antes de sembrar. ¿Cómo lo comunicas?", ["Digo qué contó: mirar el cielo antes de sembrar.", "Digo de quién: la educadora Marta, de su comunidad.", "Digo el alcance: en su comunidad, no en todas."], "«Según la educadora Marta, en su comunidad se mira el cielo antes de sembrar.»"),
        W("Reconocer lo que no sé", "Te preguntan qué significa una señal que no conoces. ¿Qué respondes?", ["No invento.", "Digo que no lo sé.", "Ofrezco preguntar."], "«No lo sé; lo voy a preguntar.»"),
    ],
    mistakes=[
        M("Decir «todos los pueblos hacen esto».", "Solo hablaste de una comunidad.", "Di de qué comunidad y pueblo es."),
        M("Completar con tu imaginación lo que no sabes.", "Se puede difundir algo falso.", "Di «no lo sé» y pregunta."),
    ],
    R=[
        ex("La procedencia dice de dónde y de quién viene un saber. ¿Verdadero o falso?", "Verdadero", "Esa es la definición."),
        ex("¿Qué dices si no sabes algo? A) «No lo sé; lo preguntaré» B) invento una respuesta", "A", "Eso es ser honesto."),
        ex("«En su comunidad…» ¿habla de todas las comunidades? Sí o No.", "No", "Solo habla de una."),
    ],
    C=[
        ex("¿Qué es el alcance? A) hasta dónde vale lo que digo B) el tamaño de un cartel", "A", "Dice los límites de lo contado."),
        ex("Verdadero o falso: puedo decir «todos los pueblos» si mi fuente habló de una comunidad.", "Falso", "Eso sería generalizar."),
        ex("¿Qué dos cosas dices al comunicar un saber?", "Quién lo enseñó y de qué pueblo o comunidad es", "Eso es la procedencia."),
    ],
    A=[
        ex("Escribe una frase con procedencia y alcance. Datos: la educadora Marta cuenta que en su comunidad se mira el cielo antes de sembrar.", "Según la educadora Marta, en su comunidad se mira el cielo antes de sembrar", "Incluye fuente y alcance."),
        ex("Marca las frases que sí tienen alcance: a) «En mi comunidad se mira el cielo» b) «Todos los pueblos miran el cielo» c) «Según mi abuela, en su familia se mira el cielo».", "a y c", "La b generaliza."),
        ex("Ordena: 1) digo el alcance 2) digo qué observamos 3) digo quién enseñó.", "2, 3, 1", "Primero lo observado, luego la fuente y por último el alcance."),
    ],
    Z=[
        ex("Luz explicó una señal y no dijo quién se la enseñó. ¿Qué falta?", "La procedencia", "Debe decir quién y de qué pueblo."),
        ex("¿Por qué es importante decir «esto no lo sé»?", "Porque no inventamos ni engañamos", "La honestidad cuida a todos."),
    ],
    D=[
        ex("Un compañero dice que una señal «es mapuche» por un video. ¿Qué preguntas le haces?", "¿Quién lo dijo y de qué comunidad es?", "Así pides la procedencia."),
        ex("Una persona dice «con permiso, esto no se comparte afuera». ¿Qué haces con lo que oíste?", "No lo cuento", "Se respeta el límite que pidió."),
    ],
    context=[ex("En una exposición, tres niños hablan de señales. Dos citan su fuente y uno no. ¿Cuántos explicaron con procedencia?", "2", "Solo dos citaron la fuente.")],
    selfcheck=[ex("¿Qué es la procedencia?", "De dónde y de quién viene un saber", "Dice la fuente."), ex("¿Qué dices cuando no sabes?", "No lo sé", "Eso es ser honesto."), ex("¿Qué es el alcance?", "Hasta dónde vale lo que digo", "Marca los límites.")],
    task=T("Escribe una ficha de tres datos con este modelo: 1) Lo que se observa (descripción). 2) Quién lo enseñó y de qué pueblo o comunidad es. 3) Hasta dónde vale (alcance). Usa este caso: «La educadora Marta, de su comunidad, cuenta que antes de sembrar mira el cielo de la mañana». Después escribe una frase para decir lo que no sabes.",
           "1) Se mira el cielo de la mañana antes de sembrar. 2) Lo contó la educadora Marta, de su comunidad. 3) Vale para su comunidad, no para todos. No sé: qué se ve en el cielo.",
           ["incluye procedencia", "incluye alcance", "dice lo que no sabe"], ["ficha de tres datos", "frase de honestidad"], ["generalizar a todos los pueblos"],
           "Valora que no generalizó y que dijo lo que no sabe; ofrecer volver a preguntar a la comunidad."),
    reinforce="Cuenta a alguien algo que aprendiste en esta unidad diciendo quién lo enseñó.",
    extend="Prepara una pregunta para el educador tradicional sobre qué se puede o no compartir en la escuela.",
)

# ============================================================ OA 12 · Eventos socioculturales y ceremoniales
EV = "Tabla de eventos (datos generales): We Tripantu, año nuevo mapuche, alrededor del 21 de junio, invierno. Tapati Rapa Nui, fiesta de la cultura rapa nui, en febrero, en la isla. Año nuevo andino, alrededor del 21 de junio, pueblos andinos del norte."

L(
    OA12, 1,
    materials="Lápiz y hojas. La tabla de eventos con datos generales está escrita en el cuaderno.",
    use="Aprenderé a ubicar un evento cultural de un pueblo diciendo su nombre, cuándo ocurre y dónde, con una fuente.",
    prior=["Sé los meses del año y las estaciones.", "Sé qué es una fiesta."],
    explain=[
        "Los pueblos originarios tienen eventos importantes: fiestas, celebraciones y ceremonias. Cada evento tiene un nombre, un tiempo del año y un lugar. Para hablar bien de un evento necesitamos saber esos tres datos y de qué pueblo es.",
        "Por ejemplo, el We Tripantu es el año nuevo del pueblo mapuche y se celebra cerca de la fecha en que comienza el invierno, alrededor del 21 de junio. La Tapati Rapa Nui es una fiesta de la cultura rapa nui que se realiza en febrero, en la isla. Estos datos son generales; cada comunidad tiene su forma de vivirlo.",
        "Un mismo nombre puede celebrarse distinto en cada comunidad. Por eso decimos «según esta fuente» y evitamos dar detalles que no conocemos. Si queremos saber más, preguntamos al educador tradicional o a la comunidad.",
    ],
    vocab=[("evento", "algo importante que ocurre en un día o varios"), ("ceremonia", "acto especial con un sentido para la comunidad"), ("fiesta", "celebración de la comunidad"), ("tiempo del año", "mes o estación en que ocurre"), ("nombre", "palabra con que se conoce el evento")],
    worked=[
        W("Ubicar un evento", EV + " ¿Cuándo es el We Tripantu?", ["Busco We Tripantu en la tabla.", "Leo el tiempo: alrededor del 21 de junio.", "Digo la fuente: tabla."], "Alrededor del 21 de junio, según la tabla."),
        W("No inventar detalles", "La tabla no dice qué se come en la Tapati Rapa Nui. ¿Qué haces?", ["No invento una comida.", "Escribo que falta el dato.", "Pregunto a una fuente confiable."], "Anoto que falta el dato y pregunto."),
    ],
    mistakes=[
        M("Dar una fecha exacta cuando la fuente dice «alrededor de».", "Cada comunidad puede celebrar en días distintos.", "Di «alrededor de» y cita la fuente."),
        M("Describir cómo se celebra sin conocerlo.", "Puede ser falso o faltar al respeto.", "Cuenta solo lo que dice la fuente."),
    ],
    R=[
        ex(EV + " ¿Qué pueblo celebra el We Tripantu?", "El pueblo mapuche", "La tabla dice año nuevo mapuche."),
        ex(EV + " ¿En qué mes es la Tapati Rapa Nui?", "Febrero", "La tabla dice febrero."),
        ex("Un evento tiene nombre, tiempo y lugar. ¿Cuántos datos son?", "3", "Se cuentan tres datos."),
    ],
    C=[
        ex("¿Qué es una ceremonia? A) un acto especial con sentido para la comunidad B) un recreo", "A", "Tiene un sentido propio."),
        ex("Verdadero o falso: todas las comunidades celebran un evento de la misma manera.", "Falso", "Cada comunidad tiene su forma."),
        ex("¿Qué dices si la fuente dice «alrededor del 21 de junio»?", "Alrededor del 21 de junio", "Se respeta lo que dice la fuente."),
    ],
    A=[
        ex(EV + " Une evento y mes o época. 1) We Tripantu 2) Tapati Rapa Nui. a) febrero b) alrededor del 21 de junio", "1-b, 2-a", "Los datos están en la tabla."),
        ex(EV + " ¿Qué dos eventos ocurren alrededor del 21 de junio?", "We Tripantu y año nuevo andino", "La tabla los nombra con esa fecha."),
        ex("Completa con la tabla: «La Tapati Rapa Nui es una fiesta de la cultura rapa nui en ______.»", "febrero", "Así lo dice la tabla."),
    ],
    Z=[
        ex("Pedro dice que el We Tripantu es siempre el 21 de junio exacto en todos lados. ¿Qué error comete?", "La fuente dice «alrededor de»", "Hay comunidades que lo celebran en días cercanos."),
        ex("¿Por qué decimos «según la tabla»?", "Para citar de dónde viene el dato", "Es la fuente."),
    ],
    D=[
        ex("Una niña dice que su comunidad celebra en otro día que el de la tabla. ¿Es posible que tenga razón? Sí o No.", "Sí", "La tabla es general y las comunidades tienen sus tiempos propios."),
        ex("¿Qué evento de la tabla ocurre en febrero?", "Tapati Rapa Nui", "Es el que tiene esa fecha."),
    ],
    context=[ex("Tu curso hace un calendario con dos eventos: uno en febrero y otro en junio. ¿Cuántos meses distintos hay en el calendario?", "2", "Febrero y junio son dos.")],
    selfcheck=[ex("¿Qué tres datos tiene un evento?", "Nombre, tiempo y lugar", "Son los que ubican el evento."), ex("¿Cuándo es la Tapati Rapa Nui?", "En febrero", "Según la tabla."), ex("¿Inventas detalles que no conoces?", "No", "Se respeta la fuente.")],
    task=T("Con la tabla de eventos de esta clase, haz una tarjeta para uno de los tres eventos con: nombre, pueblo, época del año y la frase «Fuente: tabla del cuaderno». Dibuja algo respetuoso, como una estación del año o un paisaje (no dibujes personas en ceremonia).",
           "Tarjeta: We Tripantu. Pueblo mapuche. Alrededor del 21 de junio, invierno. Fuente: tabla del cuaderno. Dibujé un paisaje de invierno.",
           ["incluye nombre, pueblo y época", "cita la fuente", "no inventa detalles"], ["tarjeta", "dibujo"], ["escribir una fecha exacta no dada", "dibujar personas en ceremonia"],
           "Revisa los datos contra la tabla; si agregó detalles de cómo se celebra, conversar sobre que eso lo enseña la comunidad."),
    reinforce="Lee en voz alta la tabla de eventos y señala el mes de cada uno.",
    extend="Escribe una pregunta para el educador tradicional sobre cómo se vive un evento en su comunidad.",
)

L(
    OA12, 2,
    materials="Lápiz y hojas. Una ficha con datos generales de dos eventos está escrita en el cuaderno.",
    use="Aprenderé para qué se hacen los eventos y quiénes participan, usando solo información general y respetuosa.",
    prior=["Sé qué es una celebración.", "Sé que en una comunidad hay niños, jóvenes y personas mayores."],
    explain=[
        "Los eventos de los pueblos originarios tienen un propósito, es decir, una razón para hacerse. Algunos celebran el cambio de estación, otros agradecen a la tierra, otros reúnen a las familias o recuerdan la historia. El propósito lo explica la comunidad.",
        "En los eventos participan personas con distintos roles: niños, jóvenes, personas mayores, familias y personas que guían, como los sabios y sabias o los líderes de la comunidad. Cada persona tiene un lugar y una tarea que la comunidad reconoce.",
        "Un evento importante suele unir a la comunidad. Según cada comunidad, puede haber alimentos compartidos, cantos, conversación y agradecimientos. Solo podemos contar lo que la comunidad ha autorizado contar. Si tenemos dudas, preguntamos y no suponemos.",
    ],
    vocab=[("propósito", "razón por la que se hace algo"), ("participante", "persona que toma parte en un evento"), ("rol", "tarea que una persona tiene en un evento"), ("comunidad", "grupo de personas que viven y celebran juntas"), ("agradecer", "mostrar gracias por lo recibido")],
    worked=[
        W("Propósito", "Ficha general: «El We Tripantu marca el año nuevo mapuche y reúne a las familias». ¿Cuál es el propósito?", ["Busco la razón del evento.", "Marca el año nuevo.", "También reúne a las familias."], "Marcar el año nuevo y reunir a las familias."),
        W("Participantes", "En un evento hay niños, jóvenes, personas mayores y un sabio que guía. ¿Cuántos grupos distintos participan?", ["Cuento los grupos.", "Niños, jóvenes, personas mayores y quien guía.", "Son cuatro."], "4"),
    ],
    mistakes=[
        M("Decir quién hace cada cosa sin conocer ese evento.", "Cada comunidad define los roles.", "Cuenta solo lo que dice la fuente."),
        M("Pensar que un evento es solo para mirar.", "La comunidad participa y comparte.", "Piensa en quiénes participan y para qué."),
    ],
    R=[
        ex("El propósito es la razón por la que se hace un evento. ¿Verdadero o falso?", "Verdadero", "Eso significa propósito."),
        ex("Ficha: «El We Tripantu marca el año nuevo mapuche». ¿Qué marca?", "El año nuevo mapuche", "Está en la ficha."),
        ex("Una persona que participa en un evento es un ______.", "participante", "Participante es quien toma parte."),
    ],
    C=[
        ex("¿Qué hace un evento por la comunidad? A) la une B) la separa", "A", "Reúne a las familias."),
        ex("Verdadero o falso: todos los participantes tienen la misma tarea.", "Falso", "Cada uno tiene su rol."),
        ex("¿Quién explica el propósito de un evento?", "La comunidad", "Ellos conocen su sentido."),
    ],
    A=[
        ex("Ficha: «La Tapati Rapa Nui reúne a la comunidad en febrero para celebrar su cultura». Escribe el propósito.", "Reunir a la comunidad y celebrar su cultura", "Es lo que dice la ficha."),
        ex("Une cada palabra con su significado. 1) participante 2) propósito 3) rol. a) razón por la que se hace un evento b) persona que toma parte en un evento c) tarea que tiene una persona en un evento", "1-b, 2-a, 3-c", "Son las definiciones de esta clase; los roles de cada evento los explica la comunidad."),
        ex("En una celebración hay 12 niños, 8 jóvenes y 5 personas mayores. ¿Cuántas personas hay?", "25", "12 + 8 + 5 = 25."),
    ],
    Z=[
        ex("Ana dice que en todos los eventos todos hacen lo mismo. ¿Qué error comete?", "Olvida los distintos roles", "Cada persona tiene un lugar."),
        ex("¿Por qué no contamos más allá de lo que la comunidad autorizó?", "Porque debemos respetar sus límites", "Hay cosas que ellos deciden compartir."),
    ],
    D=[
        ex("La ficha no dice quién guía el evento. ¿Qué haces?", "Pregunto a la comunidad o al educador", "No se supone."),
        ex("Si 25 personas participan y 9 son niños, ¿cuántas no son niños?", "16", "25 − 9 = 16."),
    ],
    context=[ex("Una vecina dice: «En mi comunidad los mayores guían y los niños aprenden». ¿Quiénes aprenden según ella?", "Los niños", "Lo dice la frase.")],
    selfcheck=[ex("¿Qué es el propósito?", "La razón por la que se hace un evento", "Es el para qué."), ex("¿Quiénes participan?", "Niños, jóvenes, personas mayores y quien guía", "Hay distintos roles."), ex("¿Quién explica el sentido?", "La comunidad", "Ellos conocen su sentido.")],
    task=T("Con la tabla de la clase anterior, elige un evento y escribe: su propósito general (por ejemplo «marcar el año nuevo» o «reunir a la comunidad»), quiénes participan en general (niños, jóvenes, mayores) y una pregunta que le harías a la comunidad sobre el evento. Dibuja un símbolo neutro (un sol, una luna, una planta).",
           "Evento: Tapati Rapa Nui. Propósito: reunir y celebrar su cultura. Participan niños, jóvenes y mayores. Pregunta: ¿cómo participan los niños?",
           ["escribe el propósito general", "nombra participantes sin inventar detalles", "formula una pregunta"], ["texto breve", "dibujo neutro"], ["describir rituales"],
           "Reconoce lo general; si agregó detalles de rituales, recordar que solo la comunidad puede contarlos."),
    reinforce="Explica con tus palabras qué es el propósito de una fiesta de tu familia.",
    extend="Escribe una pregunta sobre quién guía un evento en una comunidad.",
)

L(
    OA12, 3,
    materials="Lápiz y hojas. Una lista de casos de práctica con situaciones que se pueden o no compartir está escrita en el cuaderno.",
    use="Aprenderé que algunos eventos y conocimientos son públicos y otros son reservados, y que debo respetar esos límites.",
    prior=["Sé qué es un secreto.", "Sé pedir permiso."],
    explain=[
        "En una comunidad, algunos eventos son abiertos y cualquiera puede mirar o participar. Otros son solo para quienes la comunidad ha autorizado. Lo reservado no es malo ni un secreto para esconder: es algo especial que se cuida.",
        "No debemos sacar fotos, grabar ni dibujar cosas reservadas, y tampoco repetirlas sin permiso. Si estamos en un evento y no sabemos si algo se puede registrar, preguntamos a una persona de la comunidad antes de usar cámara o celular.",
        "Respetar lo reservado es una forma de cuidar a la comunidad. También respetamos lo público: si algo es abierto y la comunidad lo autoriza, podemos contarlo con cuidado y citando quién nos lo enseñó.",
    ],
    vocab=[("público", "abierto para que todos puedan ver"), ("reservado", "que se cuida y solo se comparte con quienes la comunidad autoriza"), ("registrar", "tomar foto, grabar o escribir"), ("límite", "hasta dónde se puede llegar"), ("autorizar", "dar permiso")],
    worked=[
        W("Público o reservado", "Una comunidad invita a todos a una fiesta en la plaza. Otra parte de la ceremonia es solo para algunas personas. ¿Qué es público y qué es reservado?", ["La fiesta en la plaza es abierta.", "La parte para algunas personas es reservada.", "No hablo de lo reservado."], "Público: la fiesta en la plaza. Reservado: la parte solo para algunas personas."),
        W("Antes de grabar", "Tomás quiere grabar con el celular. ¿Qué hace primero?", ["Mira si hay un aviso.", "Pregunta a una persona de la comunidad.", "Graba solo si se lo permiten."], "Pregunta y graba solo con permiso."),
    ],
    mistakes=[
        M("Sacar fotos sin preguntar.", "Puede mostrar algo que la comunidad cuida.", "Pregunta antes de usar el celular."),
        M("Contar a otros lo reservado porque lo supe.", "Fue compartido con confianza.", "No lo repitas sin permiso."),
    ],
    R=[
        ex("Reservado significa que se cuida y se comparte solo con autorización. ¿Verdadero o falso?", "Verdadero", "Esa es la idea."),
        ex("Una fiesta abierta en la plaza, ¿es pública o reservada?", "Pública", "Todos pueden mirarla."),
        ex("Antes de grabar, ¿qué haces? A) pregunto B) grabo rápido", "A", "El permiso va primero."),
    ],
    C=[
        ex("¿Por qué se cuida lo reservado? A) para cuidar a la comunidad B) para esconder cosas malas", "A", "Es algo especial que se cuida."),
        ex("Verdadero o falso: si algo es reservado, puedo contarlo si me lo contaron en confianza.", "Falso", "No se repite sin permiso."),
        ex("¿Qué haces si no sabes si puedes registrar algo?", "Pregunto antes", "Es lo respetuoso."),
    ],
    A=[
        ex("Clasifica como PÚBLICO o RESERVADO: a) una feria abierta con venta de comida b) una parte solo para personas autorizadas c) una fiesta en la plaza con invitación a todos.", "a) público, b) reservado, c) público", "Solo b se limita."),
        ex("Une la situación con lo que haces. 1) hay un aviso «no fotos» 2) no sé si puedo grabar 3) me invitaron a mirar. a) no tomo fotos b) pregunto c) miro con respeto", "1-a, 2-b, 3-c", "Cada situación pide una conducta."),
        ex("Ordena antes de grabar: 1) grabo 2) pido permiso 3) espero respuesta.", "2, 3, 1", "Solo se graba tras recibir permiso."),
    ],
    Z=[
        ex("Camila publicó una foto de una ceremonia sin permiso. ¿Qué error cometió?", "No respetó lo reservado ni pidió permiso", "Debió preguntar antes."),
        ex("¿Por qué respetar lo reservado ayuda a la comunidad?", "Porque cuida lo que es especial para ella", "Es una forma de respeto."),
    ],
    D=[
        ex("Un adulto dice «esto sí lo puedes contar, pero esto no». ¿Qué haces con lo segundo?", "No lo cuento", "Se respeta el límite."),
        ex("Una persona invita a todos a un evento abierto y dice que se puede fotografiar la plaza. ¿Puedes fotografiar el interior de una casa? Sí o No.", "No", "El permiso fue solo para la plaza."),
    ],
    context=[ex("En una fiesta hay 3 actividades abiertas y 1 reservada. ¿Cuántas actividades son en total?", "4", "3 + 1 = 4.")],
    selfcheck=[ex("¿Qué es reservado?", "Lo que se cuida y comparte solo con autorización", "Es algo especial."), ex("¿Qué haces antes de grabar?", "Pido permiso", "Siempre se pide permiso."), ex("¿Puedo repetir lo reservado?", "No", "Sin permiso no.")],
    task=T("Lee estos tres casos de práctica y escribe PÚBLICO o RESERVADO con una razón: a) una feria abierta con comida, b) una parte de la ceremonia solo para personas autorizadas, c) una fiesta en la plaza con invitación a todos. Luego escribe qué le dirías a un amigo que quiere grabar la parte b.",
           "a) público, abierto. b) reservado, solo para autorizados. c) público, invitación a todos. Le diría: «No grabemos, es reservado; preguntemos».",
           ["clasifica bien", "da una razón", "respeta lo reservado"], ["tres clasificaciones", "frase para el amigo"], ["dar detalles de lo reservado"],
           "Valora la frase de respeto; no pedir detalles de ceremonias reales."),
    reinforce="Explica con tus palabras qué es público y qué es reservado.",
    extend="Escribe una pregunta para el educador tradicional sobre cómo participar con respeto en un evento abierto.",
)

L(
    OA12, 4,
    materials="Lápiz, hojas y colores. Un guion de una visita respetuosa está escrito en el cuaderno.",
    use="Aprenderé formas respetuosas de aprender sobre un evento sin imitarlo ni actuarlo. Sirve para valorar sin apropiarme.",
    prior=["Sé la diferencia entre público y reservado.", "Sé pedir permiso."],
    explain=[
        "Podemos aprender mucho sobre los eventos de los pueblos originarios. Pero aprender no es disfrazarse ni actuar la ceremonia como una obra de teatro. Actuar una ceremonia puede faltar al respeto, porque tiene un sentido para la comunidad.",
        "Hay maneras respetuosas de aprender: escuchar a una persona de la comunidad, leer una ficha, mirar un evento abierto sin interrumpir, dibujar el paisaje de la época y conversar con el educador tradicional. Así aprendemos sin escenificar.",
        "Cuando hablamos de un evento, usamos las palabras de la fuente y decimos que no somos parte de la comunidad si no lo somos. Si queremos participar en un evento abierto, preguntamos cómo hacerlo bien y agradecemos la invitación.",
    ],
    vocab=[("escenificar", "actuar algo como si fuera una obra de teatro"), ("imitar", "hacer lo mismo que otra persona"), ("respeto", "cuidar lo que es importante para otros"), ("invitación", "permiso para participar"), ("agradecer", "decir gracias por lo recibido")],
    worked=[
        W("Aprender sin actuar", "El curso quiere «hacer la ceremonia» disfrazados. ¿Qué proponen en vez?", ["Disfrazarse puede faltar al respeto.", "Pueden invitar al educador tradicional.", "Pueden leer la ficha y dibujar el paisaje de la época."], "Invitar al educador tradicional, leer la ficha y dibujar el paisaje."),
        W("Visitar con respeto", "Una comunidad invita a todos a una fiesta abierta. ¿Qué haces al llegar?", ["Saludo con respeto.", "Pregunto cómo participar.", "No grabo sin permiso."], "Saludar, preguntar y no grabar sin permiso."),
    ],
    mistakes=[
        M("Disfrazarse para «mostrar» una ceremonia.", "Convierte algo sagrado en un espectáculo.", "Aprende de la fuente y de la comunidad, sin actuar."),
        M("Decir «nosotros hacemos esta ceremonia» sin ser de la comunidad.", "Se apropia de algo que no nos pertenece.", "Di «aprendimos sobre…»."),
    ],
    R=[
        ex("Escenificar es actuar algo como obra de teatro. ¿Verdadero o falso?", "Verdadero", "Esa es la definición."),
        ex("¿Qué es una forma respetuosa de aprender? A) escuchar a la comunidad B) disfrazarse", "A", "Escuchar respeta el saber."),
        ex("Si me invitan a un evento abierto, ¿qué digo al final?", "Gracias", "Agradecer es respeto."),
    ],
    C=[
        ex("Verdadero o falso: actuar una ceremonia es una forma respetuosa de aprender.", "Falso", "Puede faltar al respeto."),
        ex("¿Qué dices de un evento que no es tuyo? A) «aprendimos sobre…» B) «nosotros hacemos esta ceremonia»", "A", "No te apropias."),
        ex("¿Quién puede enseñar sobre un evento?", "La comunidad o el educador tradicional", "Ellos lo conocen."),
    ],
    A=[
        ex("Clasifica como RESPETUOSO o NO RESPETUOSO: a) escuchar una charla del educador b) disfrazarse de una ceremonia c) dibujar un paisaje de invierno.", "a) respetuoso, b) no respetuoso, c) respetuoso", "Solo disfrazarse escenifica."),
        ex("Une lo que haces con lo que cuidas. 1) pido permiso para fotos 2) uso las palabras de la fuente 3) agradezco. a) respeto la privacidad b) no invento c) reconozco el aporte", "1-a, 2-b, 3-c", "Cada acción cuida algo."),
        ex("Ordena: 1) agradezco 2) escucho a la comunidad 3) hago un dibujo del paisaje.", "2, 3, 1", "Escuchar, dibujar y agradecer."),
    ],
    Z=[
        ex("Beto dice: «Para aprender de una ceremonia hay que hacerla». ¿Qué le respondes?", "Se puede aprender escuchando y mirando con respeto, sin actuarla", "Actuar puede faltar al respeto."),
        ex("¿Por qué decimos «aprendimos sobre» y no «nosotros hacemos»?", "Porque no es nuestra ceremonia", "Así evita apropiarse."),
    ],
    D=[
        ex("Un compañero propone una obra de teatro sobre una ceremonia. ¿Qué alternativa propones?", "Una exposición de dibujos y fichas, con ayuda del educador tradicional", "Se aprende sin escenificar."),
        ex("Una comunidad invita a la escuela a una fiesta abierta. Van 20 niños y 3 adultos. ¿Cuántas personas van?", "23", "20 + 3 = 23."),
    ],
    context=[ex("Tu curso presentará lo aprendido de un evento. Tienen 4 dibujos de paisajes y 3 fichas. ¿Cuántos materiales tendrán en la exposición?", "7", "4 + 3 = 7.")],
    selfcheck=[ex("¿Qué es escenificar?", "Actuar como en una obra", "Es hacer teatro."), ex("¿Puedo disfrazarme de una ceremonia?", "No", "Falta el respeto."), ex("¿Qué digo: «aprendimos sobre» o «nosotros hacemos»?", "Aprendimos sobre", "No es nuestra ceremonia.")],
    task=T("Haz una exposición en una hoja con tres partes: un dibujo del paisaje de la época de un evento (por ejemplo, invierno para el We Tripantu o verano para la Tapati Rapa Nui), una ficha con tres datos de la tabla de eventos y una frase que empiece con «Aprendimos sobre…». No dibujes personas en ceremonia ni escribas cómo se hace un rito.",
           "Dibujé un paisaje de invierno. Ficha: We Tripantu, pueblo mapuche, alrededor del 21 de junio. Frase: «Aprendimos sobre el We Tripantu con la tabla del cuaderno».",
           ["no escenifica", "usa datos de la tabla", "usa «aprendimos sobre»"], ["dibujo", "ficha", "frase"], ["dibujar ritos", "decir «nosotros hacemos»"],
           "Valora la frase «aprendimos sobre» y el paisaje; reorientar si dibujó personas en ceremonia."),
    reinforce="Dibuja un paisaje de invierno y escribe una frase de respeto sobre un evento.",
    extend="Escribe una carta corta de agradecimiento a una persona de la comunidad que te enseñó algo.",
)
