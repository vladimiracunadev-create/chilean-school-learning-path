"""Taller de literatura (electivo 3.º y 4.º medio HC): OAC-01 (producir géneros escritos y audiovisuales para comunicar interpretaciones, clases 1 a 5) y OAC-02 (producir textos literarios propios, clases 1 a 5)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno. Todos los textos literarios, fichas y casos de los ejercicios son originales, inventados para este cuaderno y están escritos completos en el enunciado: no necesitas libros ni internet. "
             "Para leer una obra real (cuento, poema, novela) tu docente o tu biblioteca te darán el texto; este cuaderno no lo reproduce. En las actividades abiertas trabajas con los insumos que la propia actividad entrega. "
             "Si grabas audio o video, hazlo solo con personas que den su permiso y sin mostrar datos personales; no subas el material a redes sin hablar antes con tu docente.")
build = make_build(MATERIALS)

O1 = "LL-TALI-3y4-OAC-01"
O2 = "LL-TALI-3y4-OAC-02"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (texto original de ejemplo). Microrrelato «El farol»: «Cada noche Irene encendía el farol de la esquina para que su hermano volviera. Pasaron los años; el hermano no volvió, pero el farol nunca se apagó. "
     "Los vecinos, que ya no preguntaban, aprendieron a caminar hacia esa luz.» Productos posibles: P) reseña escrita con pasajes citados; Q) guion de un video de un minuto con voz en off; R) carta dirigida a la autora; S) podcast de dos voces para el curso.")
build(
    O1, 1, F,
    use="Aprenderé a elegir el género y el soporte (escrito o audiovisual) para comunicar una interpretación de una obra, según lo que quiero decir y a quién. Sirve para no empezar un producto sin saber qué comunicar.",
    prior=["Sé distinguir un resumen de una opinión.", "Conozco la diferencia entre un texto escrito y uno audiovisual.", "Sé que un texto se escribe para alguien y con un propósito."],
    explain=[
        "Una interpretación es una lectura razonada del sentido de una obra, apoyada en pasajes del propio texto. No es un resumen, que cuenta lo que ocurre, ni una opinión de gusto, que dice si algo agradó. Producir un género para comunicar una interpretación significa convertir esa lectura en un texto, un guion o una grabación que otra persona pueda entender y evaluar.",
        "Los géneros escritos más usados para esto son la reseña, el comentario, el ensayo breve y la carta a la autora o al autor. Los audiovisuales son el guion de video, el podcast y la presentación con imágenes y voz. Cada uno tiene ventajas: lo escrito permite citar con precisión; lo audiovisual permite mostrar ritmo, imagen y voz; la conversación en podcast permite confrontar lecturas distintas.",
        "Para elegir, responde tres preguntas: qué quiero comunicar (mi interpretación), a quién (audiencia) y qué soporte lo muestra mejor (propósito). Elegir el soporte antes de tener una interpretación lleva a productos vistosos pero vacíos. Y el soporte nunca reemplaza la evidencia: un video también necesita mostrar en qué pasajes se apoya la lectura.",
    ],
    vocab=[("interpretación", "lectura razonada del sentido de una obra, apoyada en el texto"), ("género", "tipo de texto o producción con forma y propósito reconocidos"), ("soporte", "medio en que se presenta el producto: papel, video, audio"), ("audiencia", "personas a quienes se dirige el producto"), ("evidencia", "pasaje de la obra que respalda una interpretación")],
    worked=[
        ("Elegir producto según la audiencia", "Quieres comunicar a tu curso, que no leyó la obra, que «El farol» muestra cómo un gesto repetido une a una comunidad. ¿Qué haces primero?",
         ["Defines la interpretación en una oración: un gesto repetido une a la comunidad.", "Notas que la audiencia no leyó la obra: tu producto debe presentarla brevemente.", "Eliges un video con voz en off, que presenta la obra y muestra imágenes de la luz y los vecinos."],
         "Presentar la obra y elegir un video con voz en off"),
        ("Soporte que no reemplaza la evidencia", "Un compañero hace un video de un farol con música, pero no cita nada de la obra. ¿Qué le falta?",
         ["Revisa si el video dice qué interpreta: no lo dice.", "Busca un pasaje de apoyo: el texto dice que el farol nunca se apagó.", "Agrega ese pasaje en voz o en pantalla, junto con la interpretación."],
         "Una interpretación explícita y un pasaje de evidencia"),
    ],
    mistakes=[("Elegir el soporte por lo vistoso («hago un video») antes de tener una interpretación.", "El soporte debe servir a lo que quiero comunicar; sin interpretación el producto queda vacío.", "Escribe primero tu interpretación en una oración y después elige el soporte que mejor la muestra."),
              ("Creer que un resumen de la historia es una interpretación.", "El resumen cuenta qué pasa, pero no propone un sentido apoyado en el texto.", "Agrega qué significa la historia según tú y el pasaje que lo respalda.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué es una interpretación de una obra?", "Una lectura del sentido de la obra apoyada en pasajes del texto", "El resumen de lo que ocurre en la obra", "Lo que me gustó o no me gustó de la obra", "La interpretación propone un sentido y lo respalda con pasajes; el resumen y el gusto no hacen ninguna de las dos cosas."),
        ("ab", "{F} Alguien escribe: «Irene enciende un farol y su hermano no vuelve». ¿Es una interpretación?", "No: cuenta lo que ocurre, pero no propone un sentido apoyado en el texto", "Sí: toda mención de la historia es una interpretación", "Esa oración solo resume los hechos; interpretar exige proponer qué significan."),
        ("{F} ¿Cuál producto (P, Q, R o S) se dirige a una sola persona determinada, la autora?", "R", "La carta se escribe para alguien concreto; los otros tres se dirigen a un público."),
        ("abc", "Un compañero propone: «el farol representa el amor que no se rinde». ¿Qué le falta a su interpretación para estar bien construida?", "Un pasaje del texto que la respalde, como que el farol nunca se apagó", "Un final distinto para el microrrelato", "Una opinión sobre si le gustó o no", "Una interpretación se sostiene con evidencia textual; cambiar el final u opinar de gusto no la respalda."),
        ("abc", "{F} Se quiere mostrar con imagen y sonido que los vecinos aprendieron a caminar hacia la luz. ¿Qué producto lo permite?", "Q, el guion de un video con voz en off", "S, el podcast de dos voces, porque tiene imagen y sonido", "P, la reseña escrita, porque tiene imagen", "Solo el video reúne imagen y sonido; el podcast tiene solo sonido y la reseña escrita no tiene ninguno de los dos."),
        ("ab", "Tu producto lo verá un público que no leyó la obra. ¿Qué conviene incluir?", "Una breve presentación de la obra antes de la interpretación", "Solo la interpretación, porque el público ya conoce la obra", "Quien no leyó la obra necesita contexto mínimo para entender tu lectura."),
        ("abc", "{F} Se quiere conversar con el curso, que sí leyó el microrrelato, sobre dos lecturas distintas. ¿Qué producto sirve mejor?", "S, el podcast de dos voces", "R, la carta a la autora", "P, una reseña escrita por una sola persona", "El podcast reúne dos voces que pueden contrastar lecturas; la carta y la reseña tienen una sola voz."),
        ("abc", "{F} Quieres explicar con pasajes citados por qué el texto muestra una comunidad que se une, para que tu profesora lo evalúe. ¿Qué elección es más adecuada?", "P, la reseña escrita con pasajes citados", "Q, un video de imágenes sin voz ni texto", "R, una carta que solo diga que te gustó", "La reseña permite citar con precisión y explicar; sin voz ni texto o sin interpretación no hay lectura que evaluar."),
        ("{F} Escribe la frase del microrrelato que sirve de evidencia para decir que la espera de Irene duró mucho tiempo.", "Pasaron los años", "Esa frase marca el paso de un tiempo largo sin que el hermano regrese."),
        ("ab", "Una estudiante hace un video lleno de efectos, pero no sabe qué quiere decir sobre la obra. ¿Cuál es el problema principal?", "Eligió el soporte antes de tener una interpretación que comunicar", "El video no puede usarse para interpretar obras", "Un producto vistoso sin interpretación no comunica una lectura; el video sí puede interpretar."),
        ("abc", "{F} Ana dice: «el texto trata de la soledad de Irene». Beto dice: «trata de cómo un gesto sostiene a una comunidad». ¿Qué diferencia hay entre ambas?", "Ana pone el foco en el personaje y Beto en la comunidad; cada una necesita su propia evidencia", "Solo una puede apoyarse en el texto y la otra no", "Son iguales, porque las dos nombran el farol", "Son lecturas con focos distintos que se pueden respaldar con pasajes diferentes, así que ninguna se descarta por existir la otra."),
        ("abc", "Elige el plan más completo para comunicar a un curso que leyó el microrrelato {F}", "Interpretación en una oración, dos pasajes como evidencia, soporte elegido por el propósito y una pregunta final al curso", "Resumen de la historia, título llamativo y música de fondo", "Opinión personal, imagen de un farol y despedida", "Solo el primer plan tiene interpretación, evidencia, soporte justificado y diálogo con la audiencia."),
        ("abc", "Un video sobre un farol que muestra solo imágenes, sin voz ni texto, ¿qué riesgo corre?", "Que la audiencia no entienda cuál es la interpretación propuesta", "Que incumpla las reglas de todo género audiovisual", "Que el farol no pueda usarse como símbolo", "Sin voz ni texto, la imagen sola no dice qué lectura se propone y cada espectador entenderá otra cosa."),
    ],
    ctx=("abc", "Contexto: en tu liceo habrá una muestra «Leemos y creamos» abierta a las familias. Debes comunicar tu lectura de {F} a personas que no la leyeron y que pasarán pocos segundos frente a tu puesto. ¿Qué producto conviene?", "Un cartel con el microrrelato completo, tu interpretación en una oración y un pasaje destacado", "Un ensayo de seis páginas pegado en la pared", "Una carta privada a la autora guardada en una carpeta", "El cartel se entiende de un vistazo, trae el texto, la lectura y la evidencia; el ensayo largo y la carta privada no sirven a visitantes apurados."),
    sc=[
        ("En Taller de literatura: ¿qué dos preguntas ayudan a elegir el género de un producto?", "Qué quiero comunicar y a quién se lo comunico", "El género se decide por la interpretación que se quiere comunicar y por la audiencia."),
        ("ab", "Una interpretación debe apoyarse en:", "Pasajes de la obra", "La cantidad de imágenes del producto", "La evidencia textual es lo que hace razonable una interpretación."),
        ("ab", "Un soporte audiovisual, ¿elimina la necesidad de evidencia del texto?", "No: la evidencia sigue siendo necesaria", "Sí: la imagen basta para sostener la lectura", "Una lectura sin pasajes que la respalden no se puede evaluar, sea cual sea el soporte."),
    ],
    op=("Con el microrrelato de la ficha {F} haz lo siguiente: (1) escribe tu interpretación en una sola oración; (2) elige uno de los productos P, Q, R o S; (3) escribe para quién es, qué pasaje usarás como evidencia y por qué ese soporte comunica mejor tu idea.",
        "(1) El farol muestra que un gesto repetido por amor termina uniendo a una comunidad. (2) Q, el guion de un video. (3) Para el curso, que no leyó la obra; evidencia: «los vecinos aprendieron a caminar hacia esa luz»; el video permite mostrar la luz y a los vecinos mientras la voz en off dice la interpretación.",
        ["interpretación en una oración que va más allá del resumen", "producto elegido entre P, Q, R o S", "audiencia nombrada", "pasaje del texto como evidencia", "razón de la elección del soporte"],
        ["tres respuestas numeradas"],
        ["resumir en vez de interpretar", "elegir el soporte sin justificarlo", "no citar ningún pasaje"],
        "Pregunta: «¿qué entendería alguien que no leyó la obra si solo viera tu producto?»."),
    reinforce="Escribe tres oraciones de interpretación sobre «El farol» que sean distintas entre sí y marca con qué pasaje podrías respaldar cada una.",
    extend="Explica por qué dos productos distintos (por ejemplo, una reseña y un podcast) pueden comunicar la misma interpretación con efectos diferentes.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (poema original de ejemplo). «Marea baja»: «Marea baja: / la playa enseña sus huesos, / conchas vacías, un zapato, / el nombre que alguien escribió / y el agua ya no recuerda. / Vuelvo a casa con las manos / llenas de una arena / que se escurre.» "
     "Tres formulaciones de ejemplo: X) «Me dio pena el poema.» Y) «El poema trata del tiempo.» Z) «El poema sugiere que lo que se intenta guardar se escurre, como la arena entre las manos de la voz que habla.»")
build(
    O1, 2, F,
    use="Aprenderé a pasar de una impresión de lectura a una tesis interpretativa que pueda comunicar en un producto. Sirve para saber qué quiero decir antes de producir un texto, un guion o una grabación.",
    prior=["Sé qué es una interpretación.", "Reconozco el tema de un texto.", "Sé que una interpretación necesita evidencia."],
    explain=[
        "Una lectura personal parte casi siempre de una impresión: «me dio pena», «me intrigó». La impresión es el punto de partida, pero no basta para comunicar. El paso siguiente es preguntarse por qué ocurrió: qué pasajes, imágenes o silencios del texto produjeron esa impresión. Así la impresión se convierte en una pregunta de lectura.",
        "El tema es la idea general del texto: el tiempo, la espera, la pérdida. La tesis interpretativa va más lejos: afirma algo sobre el tema que se puede discutir y probar con el texto. Por ejemplo, «trata del tiempo» es un tema; «el poema sugiere que lo que se intenta guardar se escurre» es una tesis, porque dice qué hace el texto con el tema y se apoya en sus imágenes.",
        "Una buena tesis cumple tres condiciones: se puede respaldar con pasajes, no es obvia y no contradice lo que el texto dice. Para formularla, observa el texto, pregunta qué efecto tiene cada imagen, propone una hipótesis y comprueba si los pasajes la sostienen. Si encuentras pasajes que la contradicen, ajusta la hipótesis antes de producir.",
    ],
    vocab=[("impresión", "primera reacción personal ante un texto"), ("tema", "idea general de la que trata un texto"), ("tesis interpretativa", "afirmación sobre el sentido del texto que se puede probar con pasajes"), ("hipótesis", "propuesta de lectura que aún se debe comprobar"), ("imagen", "expresión que hace percibir algo con los sentidos")],
    worked=[
        ("De la impresión a la tesis", "Sientes que «Marea baja» es triste. ¿Cómo llegas a una tesis?",
         ["Preguntas por qué: aparecen conchas vacías, un zapato y un nombre que el agua no recuerda.", "Notas que todo lo que se muestra está perdido o borrado.", "Propones: el poema muestra que el paso del tiempo borra lo humano."],
         "El poema muestra que el paso del tiempo borra lo humano"),
        ("Comprobar una hipótesis", "Tu hipótesis es: «la voz del poema logra guardar la arena». ¿La sostiene el texto?",
         ["Busca el pasaje: «llenas de una arena / que se escurre».", "El pasaje dice lo contrario: la arena se escurre.", "Corriges la hipótesis: la voz no logra guardar lo que recoge."],
         "No: el texto la contradice; hay que ajustarla"),
    ],
    mistakes=[("Presentar el tema como si fuera una tesis: «mi interpretación es que trata del tiempo».", "El tema nombra de qué trata, pero no afirma nada discutible sobre cómo lo trata el texto.", "Añade un verbo y una afirmación: «el poema sugiere que el tiempo borra lo humano»."),
              ("Mantener una hipótesis aunque un pasaje la contradiga.", "Una tesis debe ser coherente con todo el texto, no solo con los pasajes que la favorecen.", "Reformula la hipótesis hasta que ningún pasaje importante la contradiga.")],
    T=[
        ("{F} ¿Cuántos versos tiene el poema «Marea baja»?", "8", "Se cuentan las ocho líneas: marea baja, huesos, conchas, nombre, agua, manos, arena y se escurre."),
        ("abc", "En Taller de literatura: ¿qué es el tema de un texto?", "La idea general de la que trata", "La afirmación que se prueba con pasajes", "La reacción que produjo en quien lee", "El tema es la idea general; la afirmación probada es la tesis y la reacción es la impresión."),
        ("{F} ¿Cuál de las formulaciones X, Y o Z es solo una impresión?", "X", "«Me dio pena» expresa una reacción personal, sin afirmar nada sobre el texto."),
        ("{F} ¿Cuál de las formulaciones X, Y o Z es una tesis interpretativa?", "Z", "Z afirma algo discutible sobre el poema y se apoya en una imagen del texto."),
        ("ab", "{F} La formulación Y dice «el poema trata del tiempo». ¿Qué es?", "Un tema, porque nombra de qué trata sin afirmar nada que se pueda discutir", "Una tesis, porque nombra una idea importante", "Nombrar una idea general es proponer un tema; una tesis dice algo del modo en que el texto lo trata."),
        ("abc", "{F} Para respaldar que alguien intentó dejar una huella personal en la playa, ¿qué pasaje sirve?", "«el nombre que alguien escribió»", "«Vuelvo a casa con las manos»", "«Marea baja»", "Un nombre escrito en la arena es la huella humana que el poema menciona; los otros pasajes no hablan de eso."),
        ("abc", "{F} Una compañera dice: «el nombre que alguien escribió en la playa sigue allí, intacto». ¿Qué pasaje contradice su hipótesis?", "«y el agua ya no recuerda»", "«un zapato»", "«Marea baja»", "Si el agua ya no recuerda el nombre, este se perdió; el pasaje contradice que siga intacto."),
        ("ab", "{F} Alguien propone la tesis: «el poema muestra que el mar es peligroso». ¿Qué problema tiene?", "Ningún pasaje habla de peligro; no se puede respaldar con el texto", "Es demasiado obvia para ser tesis", "En el poema no hay amenaza ni daño; el mar solo se retira, así que la tesis carece de evidencia."),
        ("ab", "{F} La expresión «la playa enseña sus huesos» le atribuye a la playa un cuerpo. ¿Qué efecto puede tener en la lectura?", "Hace sentir la playa como algo vivo que queda expuesto cuando el agua se va", "Hace que el poema explique cómo se forman las playas", "Es una imagen que da cuerpo a la playa y la muestra vulnerable; el poema no explica fenómenos naturales."),
        ("abc", "Dos tesis sobre «Marea baja». Tesis 1: «el poema sugiere que la voz se va de la playa con algo que no puede conservar». Tesis 2: «el poema sugiere que la voz se queda a vivir en la playa». {F} ¿Cuál es incoherente con el verso «Vuelvo a casa con las manos»?", "La tesis 2", "La tesis 1", "Ambas por igual", "La voz vuelve a casa, así que la tesis 2 contradice el texto; la tesis 1 coincide con él."),
        ("abc", "{F} ¿Qué paso ocurre antes de formular una tesis?", "Preguntar por qué el texto produjo esa impresión", "Escribir el producto final", "Elegir la música de fondo", "La tesis nace de preguntar por las causas de la impresión en el texto; producir viene después."),
        ("abc", "{F} Una estudiante dice: «mi tesis es que el poema es bonito». ¿Qué le responderías?", "Que es una impresión, y que debe indicar qué hace el poema y qué pasajes lo muestran", "Que es una tesis excelente porque es sincera", "Que es un tema porque nombra una cualidad", "«Bonito» es un juicio de gusto; una tesis necesita afirmar algo del sentido y apoyarse en el texto."),
        ("{F} Completa con una palabra del poema: la tesis Z compara lo que se intenta guardar con la ____ que se escurre entre las manos.", "arena", "El poema nombra la arena que se escurre y Z la usa como imagen central."),
    ],
    ctx=("abc", "Contexto: para el diario mural debes presentar «Marea baja» en dos líneas, de modo que quien pase se interese y entienda tu lectura. ¿Cuál es la mejor entrada?", "«Marea baja»: un poema que sugiere que lo que intentamos guardar se escurre como arena", "«Marea baja»: un poema triste que me gustó mucho", "«Marea baja»: un poema sobre el mar", "La primera entrada contiene una tesis y una imagen del poema; las otras solo dan una impresión o un tema."),
    sc=[
        ("ab", "Una tesis interpretativa debe:", "Poder respaldarse con pasajes del texto", "Ser imposible de discutir", "Solo una afirmación que se apoya en pasajes puede comprobarse o discutirse."),
        ("En Taller de literatura: ¿qué paso permite ajustar una hipótesis que un pasaje contradice?", "Reformularla hasta que sea coherente con el texto", "Una hipótesis se corrige cuando el texto la contradice; no se defiende contra la evidencia."),
        ("ab", "«Me intrigó el poema» es:", "Una impresión", "Una tesis", "Es una reacción personal y todavía no afirma nada del sentido del texto."),
    ],
    op=("Escribe, con la ficha {F} a la vista: (1) tu impresión de «Marea baja» en una oración; (2) dos preguntas que esa impresión te deja sobre el poema; (3) una tesis interpretativa distinta de Z; (4) un pasaje del poema que la respalde.",
        "(1) Me dejó una sensación de vacío. (2) ¿Por qué todo lo que aparece está abandonado? ¿Qué significa volver con las manos llenas de lo que se escurre? (3) El poema sugiere que recordar es intentar retener algo que no se puede sostener. (4) «llenas de una arena / que se escurre».",
        ["impresión distinta de una tesis", "dos preguntas sobre el texto", "tesis que afirma algo discutible", "pasaje que respalda la tesis"],
        ["cuatro respuestas numeradas"],
        ["usar el tema como tesis", "copiar la tesis Z sin cambiarla", "elegir un pasaje que no respalda la tesis"],
        "Pregunta: «¿qué pasaje del poema te haría cambiar de opinión sobre tu tesis?»."),
    reinforce="Convierte estas tres impresiones en preguntas de lectura sobre «Marea baja»: «me dio frío», «me dio calma», «me quedé pensando».",
    extend="Explica por qué dos personas pueden proponer tesis distintas sobre un mismo poema y ambas ser razonables.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (fragmento original de ejemplo). «Marta contó las ventanas del vagón: eran siete, todas empañadas. Nadie bajó. Desde afuera, un hombre golpeó el vidrio con el nudillo, dos veces, como quien pregunta si hay alguien dentro. "
     "Ella no respondió; apoyó la frente en el frío y escuchó el silencio que se apretaba contra el metal.» Tesis de ejemplo: «El fragmento muestra el aislamiento de Marta, que prefiere no responder al mundo exterior.»")
build(
    O1, 3, F,
    use="Aprenderé a respaldar una interpretación con evidencia del texto: citar, parafrasear y comentar recursos literarios. Sirve para que mi producto, escrito o audiovisual, demuestre mi lectura y no solo la afirme.",
    prior=["Sé formular una tesis interpretativa.", "Reconozco imágenes y comparaciones en un texto.", "Sé usar comillas para citar."],
    explain=[
        "La evidencia textual es el pasaje que respalda una interpretación. Se puede incluir de dos modos: la cita textual, que copia las palabras exactas entre comillas, y la paráfrasis, que dice lo mismo con palabras propias. Una cita corta y bien elegida convence más que un párrafo entero pegado. Después de citar, se debe comentar: explicar cómo el pasaje respalda la tesis.",
        "Un comentario eficaz sigue tres pasos: afirmar (la tesis), mostrar (la cita) y explicar (el vínculo entre ambas). Sin explicación, la cita queda suelta; sin cita, la afirmación queda sin respaldo. En un producto audiovisual ocurre lo mismo: el pasaje se muestra en pantalla o se lee en voz, y la voz en off explica su sentido.",
        "Los recursos literarios son modos de decir que producen un efecto: la comparación une dos cosas con «como»; la personificación atribuye rasgos humanos a algo que no lo es; la imagen sensorial hace percibir con los sentidos; el narrador es la voz que cuenta. Nombrar un recurso no basta: hay que explicar qué efecto produce y cómo apoya tu tesis.",
    ],
    vocab=[("cita textual", "palabras exactas del texto, entre comillas"), ("paráfrasis", "idea del texto dicha con palabras propias"), ("comparación", "recurso que une dos cosas con «como» u otro nexo"), ("personificación", "recurso que da rasgos humanos a algo que no lo es"), ("imagen sensorial", "expresión que hace percibir algo con los sentidos")],
    worked=[
        ("Citar y comentar", "Quieres respaldar la tesis de aislamiento de Marta. ¿Cómo lo haces?",
         ["Afirmas: Marta se aísla del mundo exterior.", "Citas: «Ella no respondió; apoyó la frente en el frío».", "Explicas: no contesta al hombre y busca el contacto con el vidrio, no con una persona."],
         "Afirmación, cita y explicación de cómo la cita respalda la tesis"),
        ("Identificar un recurso y su efecto", "La expresión «como quien pregunta si hay alguien dentro». ¿Qué recurso es y qué efecto tiene?",
         ["Une el golpe en el vidrio con una acción humana mediante «como»: es una comparación.", "Efecto: el golpe parece una pregunta, y Marta no la responde."],
         "Comparación; hace que el golpe suene a pregunta sin respuesta"),
    ],
    mistakes=[("Pegar una cita larga y no comentarla.", "Sin explicación, quien lee no sabe qué parte de la cita respalda la tesis.", "Acorta la cita a lo esencial y escribe una o dos oraciones que expliquen su relación con la tesis."),
              ("Nombrar un recurso («hay una comparación») y no decir qué efecto produce.", "Nombrar no es analizar; el análisis explica el efecto y su vínculo con la interpretación.", "Después del nombre del recurso agrega «lo cual produce…» y relaciónalo con la tesis.")],
    T=[
        ("{F} ¿Cuántas ventanas cuenta Marta en el vagón?", "7", "El fragmento dice que eran siete ventanas."),
        ("abc", "En Taller de literatura: ¿qué es una cita textual?", "Las palabras exactas del texto, entre comillas", "La idea del texto dicha con palabras propias", "Una opinión sobre el texto", "La cita copia las palabras exactas del texto y las pone entre comillas."),
        ("ab", "{F} «Marta no quiso hablar con el hombre del vidrio». Esta frase, ¿es cita o paráfrasis?", "Paráfrasis, porque dice la idea con palabras propias", "Cita textual, porque aparece en el fragmento", "El fragmento dice «Ella no respondió»; la frase lo dice con otras palabras, así que es paráfrasis."),
        ("abc", "{F} La expresión «el silencio que se apretaba contra el metal» da al silencio rasgos de algo que empuja o presiona. ¿Qué recurso es?", "Personificación", "Comparación", "Paráfrasis", "Atribuye una acción física a algo que no la realiza, lo que es característico de la personificación."),
        ("abc", "{F} ¿Qué pasaje sirve para respaldar que Marta no está interesada en comunicarse?", "«Ella no respondió»", "«eran siete, todas empañadas»", "«Nadie bajó»", "No responder al golpe en el vidrio es la evidencia más directa de no querer comunicarse."),
        ("abc", "{F} ¿Cuál es el mejor comentario para unir la tesis con la cita «Nadie bajó»?", "Que nadie salga del vagón muestra un encierro en que cada persona permanece aparte, lo que refuerza el aislamiento", "La cita demuestra que el tren estaba detenido en una estación", "Nadie es una palabra que no nombra a ninguna persona", "Solo el primero explica cómo la cita respalda la tesis; los otros solo describen o repiten."),
        ("ab", "{F} Una estudiante cita todo el fragmento sin comentar. ¿Qué le recomiendas?", "Citar solo la frase más relevante y explicar cómo respalda la tesis", "Citar aún más texto para que sea más convincente", "Una cita sin explicación deja suelto el vínculo con la tesis; más texto no lo mejora."),
        ("abc", "{F} Se desea mostrar que el aislamiento de Marta se acentúa por el ambiente. ¿Qué imagen sensorial del fragmento sirve?", "«todas empañadas»", "«eran siete»", "«dos veces»", "Las ventanas empañadas impiden ver hacia afuera, lo que refuerza el encierro."),
        ("ab", "{F} En un video de este fragmento, ¿cuál es el equivalente audiovisual de citar y comentar?", "Mostrar o leer el pasaje y luego explicar con voz en off cómo respalda la tesis", "Poner música triste durante todo el fragmento", "La música sola no demuestra nada; hay que mostrar el pasaje y explicarlo."),
        ("abc", "{F} Una compañera afirma: «el narrador es una persona que viaja en el tren». ¿Qué se puede responder con el texto?", "El narrador cuenta desde afuera lo que hace Marta («Marta contó», «Ella no respondió») y no dice «yo», así que no se presenta como pasajero", "Tiene razón, porque el texto describe un tren", "Es imposible saber si hay narrador", "El texto cuenta con verbos en tercera persona, lo que indica una voz que narra desde afuera."),
        ("abc", "{F} Para sostener que el hombre del vidrio quiere comunicarse con Marta, ¿qué pasaje elegirías?", "«golpeó el vidrio con el nudillo, dos veces, como quien pregunta si hay alguien dentro»", "«Nadie bajó»", "«eran siete, todas empañadas»", "El golpe que pregunta si hay alguien es el único pasaje en que otro personaje busca contacto."),
        ("abc", "{F} Se propone la tesis «el hombre es una amenaza para Marta». ¿Qué ocurre con la evidencia?", "El texto no muestra ninguna agresión; solo un golpe suave comparado con una pregunta", "Está bien respaldada por la cita del golpe", "Está respaldada por «Nadie bajó»", "Un golpe comparado con una pregunta no prueba amenaza; la tesis atribuye una intención sin evidencia."),
        ("{F} Completa con una palabra del fragmento: el hombre golpeó el vidrio con el ____.", "nudillo", "El fragmento dice que golpeó el vidrio con el nudillo."),
    ],
    ctx=("abc", "Contexto: en una exposición de tu curso debes defender, en un minuto y con la ficha {F}, que el fragmento muestra el aislamiento de Marta. ¿Cuál es la secuencia más convincente?", "Decir la tesis, leer «Ella no respondió; apoyó la frente en el frío» y explicar qué muestra", "Leer todo el fragmento en voz alta sin decir tu tesis", "Decir que te gustó el fragmento y que está bien escrito", "La secuencia afirmar, citar y explicar demuestra la lectura; leer sin tesis o dar gusto no la comunica."),
    sc=[
        ("ab", "Una paráfrasis es:", "La idea del texto dicha con palabras propias", "El texto copiado entre comillas", "Parafrasear conserva la idea, pero con otras palabras; copiar entre comillas es citar."),
        ("En Taller de literatura: ¿qué tres pasos tiene un comentario eficaz?", "Afirmar, mostrar la cita y explicar el vínculo", "Un comentario eficaz afirma una tesis, cita un pasaje y explica cómo lo respalda."),
        ("ab", "Después de nombrar un recurso, hay que:", "Explicar qué efecto produce y cómo apoya la tesis", "Pasar a otro recurso sin explicar", "El análisis exige relacionar el efecto del recurso con la tesis."),
    ],
    op=("Con la ficha {F}: (1) elige una cita corta del fragmento; (2) identifica el recurso literario que hay en ella; (3) escribe un comentario de dos oraciones que explique el efecto del recurso y cómo respalda la tesis de la ficha, o una tesis propia si prefieres.",
        "(1) «el silencio que se apretaba contra el metal». (2) Personificación. (3) El silencio parece empujar el metal, lo que da sensación de encierro. Eso refuerza el aislamiento de Marta, que solo escucha ese silencio y no responde al mundo.",
        ["cita breve y exacta", "recurso bien identificado", "explicación del efecto", "relación con la tesis"],
        ["cita, recurso y comentario escritos"],
        ["cita sin comentar", "nombrar el recurso sin efecto", "comentar algo que la cita no dice"],
        "Pregunta: «¿tu comentario convencería a alguien que no está de acuerdo con tu tesis?»."),
    reinforce="Elige otra frase del fragmento, preséntala como cita y luego como paráfrasis, y escribe una oración que explique qué pierde o gana cada forma.",
    extend="Explica por qué un recurso literario no tiene un único efecto fijo y por qué hay que mirar el contexto del pasaje.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (texto original de ejemplo). «La carta sin sobre»: «Julián dejó la carta sobre la mesa, sin sobre ni nombre. Su madre la leyó de pie, la dobló en cuatro y la guardó entre las cucharas. Esa noche puso la mesa para tres.» "
     "Lecturas de ejemplo. L1) La madre acepta que Julián se fue, pero sigue incluyéndolo en su vida diaria. L2) La madre rechaza la carta y finge que nada ocurrió. L3) Julián volvió esa noche y cenaron juntos.")
build(
    O1, 4, F,
    use="Aprenderé a contrastar dos interpretaciones de un mismo texto y a decidir cuál se sostiene mejor con evidencia, para poder comunicarla con un producto propio. Sirve para no confundir una lectura posible con una invención.",
    prior=["Sé formular una tesis.", "Sé citar y comentar un pasaje.", "Sé reconocer cuándo una afirmación no tiene respaldo."],
    explain=[
        "Un texto literario puede admitir más de una interpretación, pero no cualquiera. Una interpretación es plausible cuando la respaldan pasajes del texto y no la contradice ningún pasaje importante. Una interpretación es una invención cuando atribuye hechos o intenciones que el texto no dice ni deja inferir. Contrastar lecturas sirve para decidir cuál tiene más respaldo.",
        "Para contrastar, sigue cuatro pasos. Primero, escribe cada lectura en una oración. Segundo, busca para cada una los pasajes que la respaldan. Tercero, busca los pasajes que la complican o contradicen. Cuarto, compara: ¿cuál explica más detalles del texto sin forzarlos? A veces dos lecturas pueden convivir si no se contradicen; otras veces una debe descartarse.",
        "Un texto con vacíos deliberados, como una carta que no se cita, pide inferir. Inferir es concluir algo a partir de pistas del texto. Se infiere bien cuando las pistas llevan a la conclusión; se infiere mal cuando se agrega información que no está. Al producir tu texto, escribe qué es dicho por el texto y qué es inferido por ti, para que la audiencia pueda evaluar tu lectura.",
    ],
    vocab=[("plausible", "que es razonable porque el texto la respalda"), ("inferencia", "conclusión sacada a partir de pistas del texto"), ("contrastar", "comparar para ver semejanzas, diferencias y cuál se respalda mejor"), ("pasaje contradictorio", "parte del texto que no calza con una lectura"), ("vacío", "información que el texto no entrega")],
    worked=[
        ("Contrastar dos lecturas", "¿Cuál se respalda mejor: L1 o L2?",
         ["L1: guardó la carta entre las cucharas y puso la mesa para tres, lo que muestra un cuidado cotidiano.", "L2: la madre leyó la carta de pie, pero no hay pasaje que muestre que finge que nada ocurrió; guardarla contradice el rechazo.", "L1 explica más detalles sin forzarlos."],
         "L1"),
        ("Descartar una invención", "L3 dice que Julián volvió esa noche. ¿Qué hacer?",
         ["Busca un pasaje que lo diga o deje inferir: no hay ninguno.", "Poner la mesa para tres no prueba que alguien haya vuelto.", "Se descarta como lectura del texto: atribuye un hecho que el texto no dice."],
         "Descartarla: agrega un hecho sin evidencia"),
    ],
    mistakes=[("Defender una lectura mostrando solo los pasajes que la favorecen.", "Hay que revisar también los pasajes que la complican, o la lectura puede ser parcial.", "Busca al menos un pasaje que complique tu lectura y explica cómo lo integras."),
              ("Dar por cierto un hecho que el texto no dice («Julián volvió»).", "El texto solo muestra la mesa para tres; el regreso es una invención.", "Distingue lo que el texto dice de lo que tú infieres y presenta lo segundo como inferencia.")],
    T=[
        ("{F} ¿En cuántas partes dobló la madre la carta?", "cuatro", "El texto dice que la dobló en cuatro."),
        ("abc", "En Taller de literatura: ¿qué es una inferencia?", "Una conclusión sacada a partir de pistas del texto", "Una cita textual", "Un resumen de la historia", "Inferir es concluir algo que el texto no dice explícitamente, pero que sus pistas permiten deducir."),
        ("{F} ¿Dónde guardó la madre la carta?", "Entre las cucharas", "El texto dice que la guardó entre las cucharas."),
        ("abc", "{F} La lectura L1 dice que la madre «sigue incluyéndolo en su vida diaria». ¿Qué pasaje respalda esa parte?", "«Esa noche puso la mesa para tres»", "«Su madre la leyó de pie, la dobló en cuatro»", "«sin sobre ni nombre»", "Un puesto más en la mesa es la acción cotidiana que incluye a Julián; los otros pasajes no muestran eso."),
        ("abc", "{F} Un compañero afirma que la madre lloró al leer la carta. ¿Cómo se clasifica su afirmación?", "Una invención: el texto no menciona llanto ni da pistas que lo hagan inferir", "Una inferencia plausible, porque toda carta de despedida hace llorar", "Una cita textual del segundo párrafo", "El texto solo dice que la madre leyó, dobló y guardó la carta; el llanto no aparece ni se deduce de una pista."),
        ("ab", "{F} ¿Pueden convivir L1 y L2 como lecturas del mismo texto?", "No: L1 dice que la madre acepta lo ocurrido y L2 que finge que nada ocurrió, así que se contradicen", "Sí: las dos hablan de la madre y de la carta", "L1 sostiene que la madre acepta lo ocurrido y L2 que lo niega; dos lecturas solo conviven si no se contradicen."),
        ("abc", "{F} Si una compañera dice «la mesa para tres significa que la madre espera a Julián», ¿qué tipo de afirmación es?", "Una inferencia que debe presentarse como tal y respaldarse con el pasaje", "Una cita textual", "Un hecho que el texto afirma sin duda", "El texto no dice que lo espere; es una conclusión a partir de una pista, o sea, una inferencia."),
        ("abc", "{F} Dos lecturas pueden convivir cuando:", "Ninguna contradice a la otra y ambas se respaldan con pasajes", "Las dos están escritas en el mismo producto", "Las dos fueron propuestas por personas del mismo curso", "La convivencia depende de que no se contradigan y de que el texto las respalde."),
        ("abc", "{F} Se quiere comunicar L1 en un video. ¿Cuál es la escena que más evidencia aporta?", "Las manos de la madre guardando la carta y luego poniendo un tercer plato", "Un plano largo del cielo nocturno", "La madre mirando por la ventana al que se fue", "La primera escena muestra los dos gestos que respaldan L1; la ventana agregaría un hecho que el texto no dice."),
        ("ab", "{F} Un estudiante defiende L2 diciendo: «ella leyó de pie, entonces no le importó». ¿Es suficiente?", "No: leer de pie es un detalle ambiguo y otros pasajes lo complican", "Sí: leer de pie prueba indiferencia", "Un solo detalle ambiguo no basta si otros pasajes muestran lo contrario, como guardar la carta."),
        ("abc", "{F} ¿Qué haría más fuerte la comunicación de L1 en un texto escrito?", "Separar lo que el texto dice de lo que se infiere y citar los pasajes", "Escribir con más adjetivos", "Evitar mencionar L2 y L3", "Distinguir lo dicho de lo inferido y citar permite que otros evalúen la lectura."),
        ("abc", "{F} Una compañera dice que la madre conoce a quien dejó la carta aunque no tenga nombre. ¿Qué pasaje apoya mejor esa inferencia?", "«la guardó entre las cucharas. Esa noche puso la mesa para tres»", "«sin sobre ni nombre»", "«Su madre la leyó de pie»", "Guardar la carta y poner un puesto más sugiere que sabe de quién es, aunque la carta no lo diga."),
        ("{F} ¿Qué verbo del texto muestra que la madre hizo algo con la carta después de leerla: «guardó» o «dejó»?", "guardó", "El verbo «guardó» describe la acción de la madre; «dejó» describe la acción de Julián."),
    ],
    ctx=("abc", "Contexto: en el taller se hará un debate sobre {F} y debes aportar una lectura. ¿Cuál es el aporte más sólido?", "«Leo que la madre acepta la partida, pero mantiene a Julián en la mesa: guarda la carta y pone un puesto extra»", "«Leo que Julián volvió porque hay tres puestos»", "«Leo que es un texto triste y lindo»", "Solo el primer aporte tiene una lectura clara con pasajes del texto; los otros inventan un hecho o son solo impresiones."),
    sc=[
        ("ab", "Una interpretación es plausible cuando:", "La respaldan pasajes y nada importante la contradice", "La propone la mayoría del curso", "La plausibilidad depende de la evidencia textual y no del número de personas que la apoyen."),
        ("En Taller de literatura: ¿qué hay que hacer con un pasaje que contradice mi lectura?", "Buscar cómo integrarlo o ajustar la lectura", "Ignorar la contradicción deja una lectura parcial; hay que integrarla o corregir."),
        ("ab", "Al comunicar una lectura, conviene:", "Marcar qué es dicho por el texto y qué es inferido", "Presentar todo como dicho por el texto", "Separar lo dicho de lo inferido permite que la audiencia evalúe la lectura."),
    ],
    op=("Con la ficha {F}: (1) elige entre L1 y L2 la lectura que te parezca mejor respaldada, o escribe una L4 propia; (2) cita dos pasajes que la respalden; (3) cita un pasaje que la complique y explica cómo lo integras; (4) escribe una oración que diga qué infieres tú y no dice el texto.",
        "(1) L1. (2) «la guardó entre las cucharas»; «puso la mesa para tres». (3) «sin sobre ni nombre»: la carta es anónima, pero la madre igual la conserva, lo que muestra que sabe de quién es. (4) Infiero que el tercer puesto es para Julián.",
        ["lectura elegida o L4 propia", "dos pasajes de respaldo", "un pasaje complicador integrado", "una inferencia marcada como tal"],
        ["cuatro respuestas numeradas"],
        ["no incluir un pasaje complicador", "presentar la inferencia como hecho", "citar pasajes que no respaldan la lectura"],
        "Pregunta: «¿qué diría alguien que defienda L2 y cómo le responderías con el texto?»."),
    reinforce="Escribe una lectura L5 del texto «La carta sin sobre» y cita dos pasajes que la respalden.",
    extend="Explica por qué un texto con vacíos deliberados invita a inferir y qué diferencia hay entre inferir y agregar un hecho.",
)

# ============================================================ OAC-01, clase 5
F = ("Ficha 5 (plan de ejemplo). Interpretación: «un gesto repetido sostiene a una comunidad». Obra de ejemplo: microrrelato «El farol», con una mujer que enciende cada noche un farol y vecinos que aprenden a caminar hacia su luz. Audiencia: familias en una muestra del liceo. Duración: 2 minutos, es decir, 120 segundos. "
     "Escenas previstas: 1) el farol de día, apagado; 2) Irene lo enciende al anochecer; 3) una silla vacía; 4) vecinos caminando hacia la luz; 5) el farol al amanecer, aún encendido. Ritmo de voz en off de ejemplo: 2 palabras por segundo.")
build(
    O1, 5, F,
    use="Aprenderé a planificar un producto escrito o audiovisual para una audiencia concreta: propósito, estructura, tiempo y revisión. Sirve para pasar de mi interpretación a un plan que pueda producir.",
    prior=["Sé elegir un género según propósito y audiencia.", "Sé respaldar una interpretación con evidencia.", "Sé calcular duraciones simples."],
    explain=[
        "Planificar es decidir, antes de producir, qué dirá el producto, en qué orden y con qué recursos. Un buen plan responde cinco preguntas: ¿cuál es mi interpretación?, ¿a quién se dirige?, ¿qué soporte uso?, ¿qué evidencia mostraré? y ¿cuánto tiempo o espacio tengo? La última pregunta importa: un video de dos minutos no puede explicar todo lo que cabe en un ensayo de cinco páginas.",
        "En un producto audiovisual, el guion organiza el plan en dos columnas: lo que se ve (imagen) y lo que se oye (voz en off, sonido). Cada escena aporta algo a la interpretación y dura un tiempo medido. Si el producto es escrito, el plan equivale a un esquema con introducción, desarrollo y cierre, en que cada párrafo trae una idea y una cita.",
        "Adaptar a la audiencia significa decidir cuánto contexto dar, qué vocabulario usar y qué tono tomar. Una audiencia que no leyó la obra necesita una presentación inicial; una audiencia especialista tolera más términos técnicos. Revisar el plan antes de producir evita rehacer el trabajo: comprueba que cada parte sirve a la interpretación y que el tiempo alcanza.",
    ],
    vocab=[("guion", "plan escrito de un producto audiovisual con imágenes y voz"), ("escena", "unidad del guion que muestra un momento"), ("plano", "encuadre de una imagen"), ("voz en off", "voz que se oye sin que se vea a quien habla"), ("esquema", "plan escrito de las partes de un texto")],
    worked=[
        ("Repartir el tiempo", "Un video de 120 segundos tiene 5 escenas de igual duración. ¿Cuánto dura cada una?",
         ["Se divide el tiempo total entre las escenas.", "120 dividido en 5 es 24."],
         "24 segundos"),
        ("Comprobar que el plan sirve a la interpretación", "La escena 3 es «una silla vacía». ¿Qué aporta a «un gesto repetido sostiene a una comunidad»?",
         ["La silla vacía muestra la ausencia del hermano.", "Esa ausencia explica por qué Irene repite el gesto cada noche.", "Aporta el motivo del gesto, así que se mantiene."],
         "Aporta el motivo del gesto y se mantiene"),
    ],
    mistakes=[("Planificar sin calcular el tiempo: seis escenas de 30 segundos en un video de 120.", "Las escenas suman más que el tiempo disponible y habrá que recortar a último minuto.", "Divide el tiempo total entre las escenas antes de escribir el guion."),
              ("Escribir el mismo guion para una audiencia que leyó la obra y otra que no.", "La audiencia que no leyó necesita una presentación inicial; la que sí leyó la puede saltar.", "Decide cuánto contexto necesita cada audiencia antes de planificar.")],
    T=[
        ("=", "{F} Las escenas 2 y 4 duran 21 segundos cada una y las otras tres duran lo mismo entre sí. Si el video dura 120 segundos, ¿cuánto dura cada una de las otras tres?", "(120-2*21)//3", "Se restan al total las dos escenas conocidas y lo que queda se reparte entre las tres restantes.", " segundos"),
        ("abc", "En Taller de literatura: ¿qué es un guion de video?", "Un plan escrito con lo que se ve y lo que se oye en cada escena", "Un resumen de la obra leída", "La lista de libros de una biblioteca", "El guion organiza imagen y voz escena por escena antes de producir."),
        ("{F} ¿A qué audiencia se dirige el producto planificado?", "A familias en una muestra del liceo", "La ficha nombra a las familias de la muestra como audiencia."),
        ("abc", "{F} Las familias no necesariamente leyeron el microrrelato. ¿Qué conviene hacer en la primera escena?", "Presentar la obra con una breve voz en off", "Comenzar con una cita larga sin explicar", "Omitir toda mención del texto", "Una audiencia que no leyó la obra necesita una presentación mínima para seguir la interpretación."),
        ("=", "{F} La voz en off lleva 2 palabras por segundo. ¿Cuántas palabras puede decir en una escena de 24 segundos?", "2*24", "Se multiplican las palabras por segundo por los segundos de la escena.", " palabras"),
        ("ab", "{F} ¿Qué escena muestra el gesto repetido de Irene, que es el centro de la interpretación?", "La 2, Irene enciende el farol al anochecer", "La 1, el farol de día, apagado", "El gesto repetido es encender el farol; la escena 1 solo muestra el farol sin que nadie lo encienda."),
        ("abc", "{F} ¿Qué escena sirve como evidencia de que la comunidad se une?", "La 4, vecinos caminando hacia la luz", "La 1, el farol apagado", "La 3, la silla vacía", "Los vecinos caminando juntos hacia la luz es la imagen que muestra a la comunidad uniéndose."),
        ("abc", "{F} Se agrega una sexta escena de 24 segundos al video de 120 segundos. ¿Qué ocurre?", "Las escenas suman 144 segundos y exceden el tiempo", "Todo sigue calzando", "El video queda con 96 segundos", "Seis escenas de 24 segundos suman 144, que supera los 120 disponibles."),
        ("=", "{F} Si el video queda con seis escenas de igual duración en 120 segundos, ¿cuánto dura cada una?", "120//6", "Con seis partes iguales cada escena dura la sexta parte del total.", " segundos"),
        ("ab", "{F} La escena 5 muestra el farol al amanecer, aún encendido. ¿Qué cierra mejor?", "La idea de que el gesto continúa más allá de la noche", "La idea de que el farol se rompió", "El farol sigue encendido, lo que cierra la idea de un gesto que persiste."),
        ("abc", "{F} Una compañera quiere agregar una escena con una fiesta en la plaza que el texto no menciona. ¿Qué conviene hacer?", "Evaluar si apoya la interpretación y señalar que es una invención del video", "Agregarla sin avisar, porque nadie lo notará", "Eliminar todas las escenas del texto", "Agregar elementos nuevos es posible si se declaran y apoyan la interpretación."),
        ("abc", "{F} ¿Qué cambio de audiencia obliga a cambiar el lenguaje del plan?", "Pasar de familias a un seminario de especialistas en literatura", "Pasar de 120 a 100 segundos", "Cambiar el color del fondo de las escenas", "Una audiencia especialista tolera más términos técnicos y menos presentación; el color no modifica el lenguaje."),
        ("=", "{F} El video final se recorta a 100 segundos con cinco escenas iguales. ¿Cuánto dura cada una?", "100//5", "Se divide el nuevo tiempo total en cinco partes iguales.", " segundos"),
    ],
    ctx=("abc", "Contexto: tu docente da cuatro minutos a cada grupo para presentar un producto sobre el microrrelato de la ficha {F}, y tu grupo tiene cuatro integrantes. ¿Qué plan reparte el tiempo con claridad?", "Una presentación inicial y tres escenas con evidencia, cada persona a cargo de una parte, y ensayo previo", "Dejar que cada persona hable lo que quiera sin orden", "Usar los cuatro minutos solo para la música", "Un reparto con orden, evidencia y ensayo hace que el tiempo alcance; improvisar o solo música no comunica la lectura."),
    sc=[
        ("ab", "Un plan completo responde, entre otras, a:", "Qué interpretación comunico, a quién y con qué evidencia", "Cuántos colores usaré", "El plan debe ordenar interpretación, audiencia y evidencia antes de producir."),
        ("En Taller de literatura: ¿qué dos columnas tiene un guion de video?", "Lo que se ve y lo que se oye", "El guion de video organiza la imagen y el sonido de cada escena."),
        ("ab", "Revisar el plan antes de producir sirve para:", "Comprobar que cada parte aporta y que el tiempo alcanza", "Cambiar de obra al final", "Una revisión previa evita rehacer el trabajo cuando ya se produjo."),
    ],
    op=("Elige una de estas opciones de audiencia: (a) estudiantes de primero medio; (b) personas de tu barrio. Para la ficha {F}, o para otra obra de tu elección que tengas a mano, escribe un plan de producto de 90 segundos con tres escenas: audiencia, interpretación en una oración, lo que se ve y se oye en cada escena (qué dice la voz en off), y el cálculo de cuántos segundos dura cada escena.",
        "Audiencia: personas de mi barrio. Interpretación: el farol reúne a los vecinos. Escena 1 (30 s): farol apagado; voz: presentación de la obra. Escena 2 (30 s): Irene lo enciende; voz: «cada noche…». Escena 3 (30 s): vecinos caminando hacia la luz; voz: la interpretación. Cálculo: 90 dividido en 3 es 30 segundos por escena.",
        ["audiencia elegida", "interpretación en una oración", "tres escenas con imagen y voz", "cálculo correcto de duración", "evidencia visible o dicha"],
        ["plan escrito con tres escenas y cálculo"],
        ["escenas que no suman 90 segundos", "no ajustar el lenguaje a la audiencia", "escenas sin relación con la interpretación"],
        "Pregunta: «¿qué escena cortarías si tuvieras 30 segundos menos y por qué?»."),
    reinforce="Divide 150 segundos en cinco escenas iguales y escribe qué pasaría en cada una para un video sobre «Marea baja».",
    extend="Explica cómo cambiaría tu plan si lo presentaras en un podcast sin imágenes.",
)

# ============================================================ OAC-02, clase 1
F = ("Ficha 1 (proyectos de ejemplo, inventados). P: una estudiante quiere contar un recuerdo real de su infancia en una calle de su ciudad, con humor y detalles. Q: un estudiante quiere expresar en pocas líneas la sensación de esperar una respuesta, usando imágenes. "
     "R: un grupo quiere que dos personajes discutan y se reconcilien en un texto para leer en voz alta. S: una estudiante quiere contar, en menos de cien palabras, un hecho extraño que ocurre a las tres de la mañana.")
build(
    O2, 1, F,
    use="Aprenderé a elegir el género literario más adecuado para un proyecto personal de escritura: poema, relato, crónica, microrrelato o texto dramático. Sirve para que mi texto tenga la forma que mejor cumple lo que quiero lograr.",
    prior=["Reconozco un poema, un cuento y un diálogo.", "Sé que un texto se escribe para alguien y con un propósito.", "Sé leer una obra con atención al sentido."],
    explain=[
        "Un género literario es un tipo de obra con rasgos reconocidos. El poema usa el verso y la imagen para condensar una experiencia; el relato (cuento) narra hechos con personajes en un tiempo y un espacio; el microrrelato cuenta una historia en muy pocas palabras y deja mucho por inferir; la crónica narra hechos reales desde una mirada personal; el texto dramático se compone de diálogos y acotaciones para ser representado o leído en voz alta.",
        "Elegir un género es una decisión de escritura. Se pregunta qué quiero provocar en quien lee (emoción, sorpresa, risa, reflexión), qué materia tengo (un recuerdo, una sensación, un conflicto entre personas, un hecho extraño) y qué extensión admite mi proyecto. Cada género favorece algo: el poema favorece la imagen y el ritmo; el relato, la secuencia de hechos; el texto dramático, el conflicto entre voces.",
        "Un mismo tema puede escribirse en varios géneros con resultados diferentes. La despedida de una persona puede ser un poema (la sensación), un relato (lo que ocurrió), una crónica (un hecho real contado con detalle) o un diálogo (la conversación final). Un proyecto bien definido nombra su género y justifica por qué es el más adecuado para lo que se quiere lograr.",
    ],
    vocab=[("género literario", "tipo de obra con rasgos reconocidos, como el poema o el cuento"), ("verso", "línea de un poema"), ("microrrelato", "relato de muy pocas palabras que sugiere más de lo que dice"), ("crónica", "texto que narra hechos reales desde una mirada personal"), ("acotación", "indicación entre paréntesis en un texto dramático sobre lo que se hace o cómo se dice")],
    worked=[
        ("Elegir un género por la materia", "Un estudiante quiere expresar la sensación del último día de clases, mezcla de alegría y vacío. ¿Qué género favorece esa sensación?",
         ["Su materia es una sensación, no una secuencia de hechos.", "Quiere usar imágenes y pocas líneas.", "El poema condensa sensaciones con imagen y ritmo."],
         "Un poema"),
        ("Un tema, dos géneros", "El tema es una mudanza. ¿Cómo cambia el texto si es poema o si es texto dramático?",
         ["En poema se centra en una imagen, como la casa vacía.", "En texto dramático se centra en una conversación entre dos personas que se despiden."],
         "El poema condensa una imagen; el drama pone voces en conflicto o conversación"),
    ],
    mistakes=[("Elegir el género por moda o por facilidad y no por lo que se quiere lograr.", "El género debe servir al propósito del proyecto; si no, el texto no consigue su efecto.", "Escribe primero qué quieres provocar y qué materia tienes, y después elige el género."),
              ("Creer que un microrrelato es un cuento resumido.", "El microrrelato no resume: sugiere y deja inferir con muy pocas palabras.", "Elimina todo lo explicativo y deja que unas pistas bien elegidas sugieran la historia.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué es el microrrelato?", "Un relato de muy pocas palabras que sugiere más de lo que dice", "Un poema de dos versos", "Un resumen de una novela", "El microrrelato es un relato brevísimo que deja mucho por inferir."),
        ("{F} ¿Qué género conviene al proyecto P, un recuerdo real contado con humor y detalle?", "Crónica", "Una crónica narra hechos reales desde una mirada personal, que es lo que pide P."),
        ("{F} ¿Qué género conviene al proyecto S, un hecho extraño contado en menos de cien palabras?", "Microrrelato", "La brevedad extrema y la sugerencia son rasgos del microrrelato."),
        ("abc", "{F} ¿Qué género conviene al proyecto Q, la sensación de esperar una respuesta con imágenes y pocas líneas?", "Poema", "Texto dramático", "Crónica", "El poema condensa una sensación en imágenes y versos breves."),
        ("abc", "{F} ¿Qué género conviene al proyecto R, dos personajes que discuten y se reconcilian para leer en voz alta?", "Texto dramático", "Poema", "Microrrelato", "El texto dramático organiza un conflicto en diálogos y acotaciones que se pueden leer en voz alta."),
        ("ab", "{F} El proyecto P cuenta un recuerdo real. ¿Por qué sería un problema escribirlo como cuento de ficción con personajes inventados?", "Porque se perdería el carácter de hecho real que define a la crónica", "Porque la ficción no se puede escribir", "La crónica se apoya en hechos reales; inventar personajes cambia el género y el propósito."),
        ("abc", "{F} Una autora de R escribe: «MARTA: (cruza los brazos) No te escucho». ¿Qué es lo que está entre paréntesis?", "Una acotación", "Un verso", "Una cita", "Las indicaciones entre paréntesis en un texto dramático se llaman acotaciones."),
        ("abc", "{F} Un estudiante tiene la sensación de nostalgia por un lugar al que no puede volver. ¿Qué materia tiene?", "Una sensación, que favorece el poema", "Un conflicto entre dos voces, que favorece el drama", "Un hecho real narrado, que favorece la crónica", "Una sensación sin hechos concretos se condensa mejor en imágenes, es decir, en poema."),
        ("ab", "{F} Para el proyecto S, ¿qué recurso favorece el género elegido?", "Sugerir el hecho extraño con pocas pistas y dejar el final abierto", "Explicar con detalle todo lo que ocurre", "El microrrelato logra efecto al sugerir; explicarlo todo contradice su brevedad."),
        ("abc", "Un mismo tema, el primer día en un liceo nuevo, se escribe como poema y como crónica. ¿Qué cambia?", "El poema condensa una sensación en imágenes; la crónica cuenta con detalle lo realmente ocurrido", "Cambia solo la extensión", "No cambia nada importante", "Cada género favorece algo distinto: la imagen y el ritmo, o el relato de hechos reales."),
        ("abc", "{F} Una estudiante quiere provocar risa con una anécdota real de su calle. ¿Qué elección es coherente?", "Crónica con humor y detalles", "Poema de versos muy oscuros", "Microrrelato sin humor", "La crónica admite anécdota real y humor; los otros no sirven al efecto deseado."),
        ("abc", "{F} Un proyecto dice: «quiero un género porque es fácil». ¿Qué falta en esa decisión?", "Qué quiere provocar y qué materia tiene", "Más páginas", "Una portada", "El género se elige por el efecto y la materia, no por la facilidad."),
        ("ab", "{F} Un grupo quiere escribir R como microrrelato en vez de texto dramático. ¿Qué perdería?", "La posibilidad de leer el conflicto en voces distintas", "Su capacidad de usar palabras", "El microrrelato condensa en pocas palabras y dificulta el cruce de voces de una discusión."),
    ],
    ctx=("abc", "Contexto: el liceo abre un concurso con cuatro categorías: poema, crónica, microrrelato y texto dramático. Tienes la idea de la ficha {F} S, el hecho extraño de las tres de la mañana. ¿A qué categoría te presentarías?", "Microrrelato, porque S pide un relato de menos de cien palabras", "Poema, porque es el género más corto", "Texto dramático, porque tiene hora", "El proyecto S ya declara su extensión y su carácter narrativo breve, que corresponden al microrrelato."),
    sc=[
        ("En Taller de literatura: ¿qué rasgo distingue a una crónica de un cuento?", "Narra hechos reales desde una mirada personal", "La crónica se apoya en hechos reales; el cuento puede ser ficción."),
        ("ab", "Un género se elige según:", "Lo que quiero provocar y la materia que tengo", "La moda del momento", "El efecto buscado y la materia son criterios de la escritora o escritor, no de la moda."),
        ("ab", "Un texto dramático se compone de:", "Diálogos y acotaciones", "Versos y estrofas", "El drama se escribe en voces de personajes y con indicaciones de acción."),
    ],
    op=("Tienes una de estas tres ideas: (a) una mudanza; (b) un regalo que nadie esperaba; (c) un ruido en la noche. Elige una y escribe: (1) el género literario que usarás; (2) qué quieres provocar en quien lea; (3) por qué ese género sirve a ese efecto; (4) las dos primeras líneas del texto.",
        "(c) un ruido en la noche. (1) Microrrelato. (2) Inquietud y sorpresa. (3) Porque con pocas palabras puedo sugerir lo que ocurre y dejar el final abierto. (4) «A las tres de la mañana, el ruido se detuvo. En el pasillo, alguien también contenía la respiración.»",
        ["idea elegida entre (a), (b) y (c)", "género nombrado", "efecto buscado", "justificación del género", "dos líneas iniciales propias"],
        ["cuatro respuestas numeradas"],
        ["elegir el género sin justificarlo", "empezar a escribir sin decir qué quiere provocar", "líneas iniciales que no corresponden al género"],
        "Pregunta: «¿cómo cambiaría el efecto si cambiaras el género?»."),
    reinforce="Elige otra de las ideas (a), (b) o (c) y escríbela como poema de cuatro versos, sin copiar frases del ejemplo.",
    extend="Explica por qué una misma idea puede producir efectos muy distintos según el género en que se escribe.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 2 (ideas de ejemplo, inventadas). I1) Un niño encuentra un paraguas en el cerro. I2) Dos hermanas heredan una casa y no se ponen de acuerdo en qué hacer con ella. I3) Una voz que habla desde el interior de una radio apagada. "
     "Preguntas creativas posibles. Q1) ¿Cómo muestro la soledad del niño sin nombrarla? Q2) ¿Qué objeto de la casa hará que cada hermana recuerde algo distinto? Q3) ¿Qué sabe la voz que nadie más sabe?")
build(
    O2, 2, F,
    use="Aprenderé a pasar de una idea a un proyecto de escritura: definir el propósito, el efecto y las restricciones del texto. Sirve para escribir con una dirección y no solo con un tema.",
    prior=["Sé elegir un género literario.", "Sé qué es un narrador y qué es un personaje.", "Sé que un texto tiene un propósito."],
    explain=[
        "Una idea es el punto de partida de un texto: un objeto, una situación, una frase. Pero una idea no es todavía un proyecto. Para convertirla en proyecto se necesita un propósito creativo, es decir, qué quiero lograr con el texto, y una pregunta de escritura que guíe las decisiones, como «¿cómo muestro la soledad sin nombrarla?». La pregunta convierte la idea en un problema que se puede resolver escribiendo.",
        "Las restricciones son condiciones que se fijan al inicio: la extensión, el punto de vista (quién cuenta: en primera persona dice «yo»; en tercera persona cuenta desde fuera), el tiempo, el número de personajes o el lugar. Parecen limitar, pero ayudan a decidir. Un texto de cien palabras obliga a elegir qué contar; un solo personaje obliga a mostrar el conflicto con objetos y gestos. Elegir restricciones propias es parte del trabajo del escritor o escritora.",
        "Un proyecto bien formulado se puede enunciar en tres partes: la idea, el efecto que se desea en quien lee y las restricciones que se adoptan. Por ejemplo: «un paraguas encontrado en el cerro; quiero provocar ternura inquieta; usaré tercera persona y 120 palabras». Con ese enunciado, cada decisión del texto se puede comprobar: ¿ayuda al efecto?, ¿cabe en las restricciones?",
    ],
    vocab=[("idea", "punto de partida de un texto: un objeto, una situación o una frase"), ("propósito creativo", "lo que quien escribe quiere lograr con su texto"), ("efecto", "impresión que el texto busca producir en quien lee"), ("restricción", "condición que se fija al escribir, como la extensión o el punto de vista"), ("pregunta de escritura", "problema que guía las decisiones al escribir")],
    worked=[
        ("De la idea al proyecto", "La idea I1 es «un niño encuentra un paraguas en el cerro». ¿Cómo la conviertes en proyecto?",
         ["Defines el efecto: ternura inquieta.", "Formulas la pregunta Q1: ¿cómo muestro la soledad sin nombrarla?", "Fijas restricciones: tercera persona y 120 palabras."],
         "Idea + efecto + pregunta + restricciones"),
        ("Usar una restricción a favor", "El texto sobre I2 debe tener solo dos personajes y ningún narrador que explique. ¿Qué te obliga a hacer?",
         ["Sin narrador explicativo, el conflicto debe mostrarse en lo que dicen y hacen.", "Con solo dos personajes, cada gesto cuenta mucho.", "La restricción te lleva a escribir diálogo y objetos con significado."],
         "Mostrar el conflicto con diálogo, gestos y objetos"),
    ],
    mistakes=[("Empezar a escribir con una idea, sin saber qué efecto se busca.", "Sin efecto buscado no hay criterio para decidir qué incluir ni qué eliminar.", "Escribe antes una oración que diga qué quieres que sienta o piense quien lea."),
              ("Pensar que las restricciones empobrecen el texto.", "Las restricciones guían las decisiones y suelen hacer el texto más preciso.", "Elige una o dos restricciones claras y úsalas como pauta.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué es una restricción de escritura?", "Una condición fijada al escribir, como la extensión o el punto de vista", "Un error en el texto", "Una crítica de un lector", "Las restricciones se eligen de antemano y guían las decisiones del texto."),
        ("{F} ¿Cuál de las ideas I1, I2 o I3 incluye dos personajes que entran en desacuerdo?", "I2", "Solo I2 habla de dos hermanas que no se ponen de acuerdo."),
        ("{F} ¿Cuál de las ideas es una voz que habla desde un objeto?", "I3", "I3 describe una voz que habla desde el interior de una radio apagada."),
        ("abc", "{F} ¿Cuál de estas es una pregunta de escritura?", "¿Qué sabe la voz que nadie más sabe?", "El paraguas es de color azul", "Una radio es un aparato", "Una pregunta de escritura abre una decisión por resolver; los otros enunciados describen algo ya dado."),
        ("abc", "{F} La pregunta Q1 dice «sin nombrarla». ¿Qué obliga a hacer?", "Mostrar la soledad con acciones, objetos o imágenes", "Escribir la palabra soledad varias veces", "Cambiar la idea por otra", "«Sin nombrarla» obliga a sugerir la soledad en lugar de decirla."),
        ("ab", "{F} Un proyecto dice: «I2; quiero provocar incomodidad; usaré diálogo y dos personajes». ¿Qué parte del enunciado es la restricción?", "Usar diálogo y dos personajes", "Provocar incomodidad", "El efecto es la incomodidad; el uso de diálogo y de dos personajes son condiciones de escritura."),
        ("abc", "{F} Se escribirá sobre I3 con la restricción «solo una voz, sin descripción del lugar». ¿Qué se logra?", "Que todo el misterio dependa de lo que dice la voz", "Que haya muchas descripciones", "Que desaparezca la radio", "Sin descripción del lugar, la voz sostiene el texto y concentra el misterio en lo que dice."),
        ("abc", "{F} Una estudiante dice: «quiero escribir sobre I1 porque es bonita». ¿Qué le falta para tener un proyecto?", "Un efecto buscado, una pregunta y restricciones", "Un título más largo", "Más personajes", "Una idea necesita efecto, pregunta y restricciones para ser proyecto."),
        ("abc", "{F} ¿Qué restricción es compatible con un texto de 100 palabras sobre I1?", "Un solo personaje y un solo lugar", "Diez personajes y cinco escenarios", "Una descripción de cada árbol del cerro", "En poco espacio hay que concentrar; un personaje y un lugar permiten hacerlo."),
        ("ab", "Un texto fija como restricción «solo diálogos, sin narrador». ¿Qué problema debe resolver quien escribe?", "Cómo dar a conocer el lugar y la acción solo con lo que dicen los personajes", "Cómo escribir sin palabras", "Sin narrador, el contexto debe aparecer en el diálogo."),
        ("abc", "{F} Dos estudiantes parten de I2. A quiere provocar ternura; B quiere provocar tensión. ¿Qué cambia?", "Las decisiones: A elegirá recuerdos tiernos; B, conflictos y silencios", "El tema de la idea, que debe ser distinto", "Nada, porque la idea es la misma", "El efecto buscado cambia las decisiones aunque la idea sea la misma."),
        ("abc", "{F} ¿Cuál es el proyecto mejor formulado?", "I3; misterio sereno; una sola voz, 90 palabras", "Quiero escribir algo bonito", "Voy a escribir sobre cosas", "Solo el primero declara idea, efecto y restricciones."),
        ("=", "{F} Tu proyecto sobre I3 tiene 90 palabras y ya escribiste 62. ¿Cuántas palabras faltan?", "90-62", "Se resta lo escrito de la extensión fijada.", " palabras"),
    ],
    ctx=("abc", "Contexto: un compañero te cuenta que tiene la idea de {F} I3, la voz en la radio apagada, pero no sabe cómo empezar. ¿Qué consejo le das?", "Que defina qué efecto quiere, una pregunta de escritura y una o dos restricciones", "Que cambie de idea por una más fácil", "Que empiece a escribir sin planificar nada", "Un proyecto necesita efecto, pregunta y restricciones; sin ellos la idea se queda sin dirección."),
    sc=[
        ("En Taller de literatura: ¿qué diferencia hay entre una idea y un proyecto de escritura?", "El proyecto añade efecto buscado, pregunta y restricciones", "La idea es el punto de partida; el proyecto define qué se quiere lograr y cómo."),
        ("ab", "Una restricción de escritura puede ser:", "La extensión del texto", "El color del lápiz", "La extensión es una condición que influye en las decisiones del texto."),
        ("ab", "Una pregunta de escritura sirve para:", "Guiar las decisiones del texto", "Reemplazar el texto", "La pregunta orienta qué incluir, qué mostrar y qué omitir."),
    ],
    op=("Elige una de las ideas I1, I2 o I3 de la ficha {F}. Escribe tu proyecto con estas partes: (1) idea elegida; (2) efecto que quieres provocar; (3) una pregunta de escritura (puedes usar Q1, Q2, Q3 o crear otra); (4) dos restricciones, una de extensión y otra de punto de vista o de personajes.",
        "(1) I2. (2) Tensión contenida. (3) Q2: ¿qué objeto de la casa hará que cada hermana recuerde algo distinto? (4) 150 palabras y solo dos personajes, sin narrador que explique.",
        ["idea elegida de la ficha", "efecto nombrado", "pregunta de escritura clara", "dos restricciones precisas"],
        ["cuatro respuestas numeradas"],
        ["efecto vago como «bonito»", "pregunta que no guía decisiones", "restricciones que no se pueden comprobar"],
        "Pregunta: «¿qué decisión de tu texto cambiaría si cambiaras una restricción?»."),
    reinforce="Escribe tres preguntas de escritura distintas para la idea I1 de la ficha, cada una con un efecto diferente.",
    extend="Explica por qué fijar una restricción puede ayudar a escribir mejor, con un ejemplo propio.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 3 (tres versiones originales de un mismo hecho). A: «Yo vi cuando se llevaron el piano. Nadie me preguntó si quería que se fuera.» B: «Se llevaron el piano. La sala quedó con un eco nuevo.» "
     "C: «El piano salió por la puerta, lento, como un animal viejo al que ayudan a bajar una escalera.»")
build(
    O2, 3, F,
    use="Aprenderé a elegir y usar recursos de escritura literaria, como el narrador, la imagen, la comparación y el ritmo, para lograr el efecto de mi proyecto. Sirve para decidir cómo escribir y no solo qué escribir.",
    prior=["Sé qué es un narrador.", "Reconozco una comparación.", "Tengo un proyecto con efecto buscado."],
    explain=[
        "Los recursos de escritura son las decisiones de forma con que se logra un efecto. El narrador es la voz que cuenta: en primera persona dice «yo» y participa; en segunda persona se dirige a un «tú»; en tercera persona cuenta desde fuera. La elección cambia lo que sabemos y lo que sentimos. Una voz que dice «yo vi» nos acerca a una emoción; una voz externa permite más distancia.",
        "La imagen hace percibir algo con los sentidos («un eco nuevo»); la comparación une una cosa con otra mediante «como» y revela una semejanza («como un animal viejo»); el ritmo es la manera en que suenan y se organizan las frases, largas o cortas. Frases cortas dan sensación de golpe o de pausa; frases largas dan sensación de fluir o de acumulación. Todos estos recursos se eligen para un efecto.",
        "Un mismo hecho, la salida de un piano, produce efectos distintos según los recursos: A muestra una pérdida sentida desde la voz de un personaje; B deja que sea el eco quien diga la pérdida; C humaniza el piano con una comparación. Para elegir bien, pregunta primero qué efecto quieres y luego qué recurso lo logra; prueba dos versiones y compara.",
    ],
    vocab=[("narrador", "voz que cuenta la historia"), ("primera persona", "voz que dice «yo» y forma parte de lo que cuenta"), ("imagen", "expresión que hace percibir algo con los sentidos"), ("comparación", "recurso que une dos cosas mediante «como» y revela una semejanza"), ("ritmo", "modo en que suenan y se organizan las frases")],
    worked=[
        ("Elegir narrador según el efecto", "Quieres que la pérdida del piano se sienta cercana y personal. ¿Qué versión de la ficha sirve?",
         ["La versión A usa «yo vi» y «nadie me preguntó».", "La primera persona acerca a quien lee a la emoción del que cuenta."],
         "La versión A, en primera persona"),
        ("Efecto de una comparación", "En C, el piano se compara con un animal viejo al que ayudan a bajar una escalera. ¿Qué efecto tiene?",
         ["Une el piano con un ser vivo y frágil.", "Sugiere cuidado, lentitud y despedida.", "Por eso la salida del piano se siente como la de alguien querido."],
         "Humaniza el piano y sugiere cuidado y despedida"),
    ],
    mistakes=[("Llenar el texto de comparaciones porque «se ven literarias».", "Un recurso sin efecto buscado distrae y pierde fuerza.", "Usa solo los recursos que ayuden al efecto de tu proyecto y revisa si se pueden quitar."),
              ("Elegir el narrador sin pensar qué sabe y qué muestra.", "El narrador decide qué información tiene el lector y cómo se siente.", "Antes de escribir, decide quién cuenta y qué sabe, y mantén esa voz.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué es un narrador?", "La voz que cuenta la historia", "La persona que escribió el texto", "El título del texto", "El narrador es la voz que cuenta; no siempre coincide con quien escribe."),
        ("{F} ¿En qué versión, A, B o C, aparece la palabra «yo»?", "A", "Solo la versión A usa «yo vi»."),
        ("{F} ¿Qué versión contiene una comparación con «como»?", "C", "Solo C compara el piano con un animal viejo mediante «como»."),
        ("abc", "{F} En la versión B, «un eco nuevo» es:", "Una imagen sensorial", "Una cita textual", "Un narrador en primera persona", "El eco se percibe con el oído, así que es una imagen sensorial."),
        ("ab", "{F} En la versión A, ¿qué sentimiento sugiere «Nadie me preguntó si quería que se fuera»?", "Impotencia ante una decisión ajena", "Indiferencia, porque la voz solo describe un hecho", "La voz no pudo opinar y lo siente, lo que expresa impotencia y no indiferencia."),
        ("abc", "{F} ¿Qué diferencia hay entre B y C respecto al efecto?", "B sugiere la pérdida con un eco vacío; C la sugiere humanizando al piano", "Ambas usan primera persona", "B usa comparación y C usa «yo»", "B se apoya en una imagen sonora y C en una comparación con un ser vivo."),
        ("abc", "{F} Quieres un efecto de golpe seco al comunicar la pérdida. ¿Qué ritmo conviene?", "Frases cortas", "Una sola frase muy larga con muchos conectores", "Frases largas que se acumulan", "Las frases cortas producen sensación de golpe y pausa."),
        ("ab", "{F} Una estudiante dice: «B tiene narrador». ¿Qué tipo de narrador es?", "Tercera persona, porque cuenta desde fuera sin decir «yo»", "Primera persona, porque dice «se llevaron»", "En B nadie dice «yo»: se cuenta lo que ocurre desde fuera."),
        ("abc", "{F} Un compañero quiere sugerir la ausencia del piano mediante un sonido. ¿Qué versión lo logra?", "B, porque el eco nuevo de la sala sugiere el vacío", "A, porque dice «nadie me preguntó»", "C, porque compara el piano con un animal viejo", "Solo B recurre a un sonido, el eco, para sugerir el vacío que dejó el piano."),
        ("abc", "{F} Se quiere reescribir C en primera persona. ¿Cuál versión lo hace?", "«Vi salir el piano, lento, como un animal viejo al que ayudan a bajar una escalera.»", "«El piano salió lento, como un animal viejo.»", "«Salió el piano de la sala.»", "Solo la primera incorpora «vi» y mantiene la comparación."),
        ("ab", "{F} Si el efecto buscado es distancia fría, ¿qué narrador conviene más?", "Tercera persona, sin adjetivos emotivos", "Primera persona, con exclamaciones", "La tercera persona sin emociones explícitas produce distancia."),
        ("abc", "Un estudiante usa tres comparaciones en dos líneas. ¿Qué riesgo corre?", "Que los recursos se amontonen y resten fuerza al efecto", "Que el texto sea ilegible por tener comparaciones", "Que no sea literario", "Muchos recursos juntos se estorban y se pierde el efecto."),
        ("{F} Completa con una palabra de la versión B: «La sala quedó con un eco ____».", "nuevo", "La versión B dice que la sala quedó con un eco nuevo."),
    ],
    ctx=("abc", "Contexto: escribirás un microrrelato de la ficha {F} para una lectura en voz alta y quieres que el público sienta cercanía con quien cuenta. ¿Qué narrador eliges?", "Primera persona, como en la versión A", "Tercera persona fría", "Segunda persona con órdenes", "La primera persona acerca al público a la emoción de quien cuenta."),
    sc=[
        ("En Taller de literatura: ¿qué hace una comparación en un texto?", "Une dos cosas y revela una semejanza", "La comparación conecta dos cosas con «como» o similar para mostrar algo que comparten."),
        ("ab", "Las frases cortas producen:", "Sensación de golpe o de pausa", "Sensación de fluir sin parar", "El corte frecuente marca pausas y golpes en el ritmo."),
        ("ab", "Un recurso se elige:", "Según el efecto que se busca", "Según lo que parezca más literario", "El recurso debe servir al efecto del proyecto."),
    ],
    op=("Con la misma situación de la ficha {F} (la salida de un piano), escribe una versión D de dos oraciones, distinta de A, B y C, que use un recurso a tu elección entre narrador en segunda persona, imagen visual o frases cortas. Indica qué efecto buscas y qué recurso usaste.",
        "D: «Tú no miras. Te quedas en la sala, donde el piano dejó cuatro marcas en la alfombra.» Recurso: segunda persona e imagen visual. Efecto: una ausencia que se ve en el piso.",
        ["dos oraciones propias", "recurso nombrado entre los permitidos", "efecto buscado", "coherencia entre recurso y efecto"],
        ["versión D con recurso y efecto"],
        ["copiar frases de A, B o C", "no explicar el efecto", "mezclar recursos sin necesidad"],
        "Pregunta: «¿qué perdería D si cambias el recurso por otro?»."),
    reinforce="Reescribe la versión A en tercera persona y escribe qué efecto cambia.",
    extend="Explica por qué un recurso literario no tiene efecto por sí mismo, sino en el contexto del texto.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 4 (dos inicios originales de un cuento). V1: «Era una noche oscura y yo estaba muy asustado porque pasaban cosas raras en mi casa.» "
     "V2: «A las tres de la mañana, el timbre sonó una vez. Nadie en la calle. En el felpudo, un paraguas abierto, todavía mojado.» Criterios de ejemplo: a) crea intriga; b) usa detalles concretos; c) deja inferir en lugar de explicar.")
build(
    O2, 4, F,
    use="Aprenderé a comparar versiones de un mismo texto y a decidir cuál logra mejor el efecto de mi proyecto, con criterios y evidencia. Sirve para tomar decisiones de escritura fundamentadas.",
    prior=["Sé qué es un efecto en un texto.", "Reconozco recursos como la imagen y el ritmo.", "Sé qué es un criterio."],
    explain=[
        "Escribir implica decidir entre alternativas. Una versión puede decir las cosas de forma explícita («estaba muy asustado») y otra mostrarlas con detalles («un paraguas abierto, todavía mojado»). Mostrar es presentar acciones, objetos o imágenes para que quien lee saque la conclusión; decir es nombrar la emoción o la idea. En muchos géneros narrativos, mostrar produce intriga y cercanía, aunque a veces decir es lo apropiado.",
        "Para comparar dos versiones se usan criterios, es decir, preguntas que se aplican a ambas con la misma vara. Algunos criterios útiles: ¿crea intriga?, ¿usa detalles concretos?, ¿deja inferir en lugar de explicar?, ¿mantiene la voz del narrador? Se aplica cada criterio a las dos versiones y se cita el pasaje que lo muestra. La decisión no se basa en el gusto, sino en el cumplimiento del efecto buscado.",
        "El cliché es una expresión tan repetida que perdió fuerza, como «noche oscura y tormentosa». Un cliché no siempre es un error, pero resta originalidad. Para renovarlo, se reemplaza por un detalle específico y propio. Por ejemplo, en lugar de «noche oscura», se escribe «a las tres de la mañana», que sitúa el momento y sugiere inquietud sin recurrir a la fórmula gastada.",
    ],
    vocab=[("mostrar", "presentar acciones, objetos o imágenes para que quien lee saque la conclusión"), ("decir", "nombrar directamente la emoción o la idea"), ("criterio", "pregunta que se aplica por igual a las versiones para compararlas"), ("cliché", "expresión muy repetida que perdió fuerza"), ("detalle concreto", "dato específico que se puede percibir con los sentidos")],
    worked=[
        ("Comparar con un criterio", "Criterio b) usa detalles concretos. ¿Qué versión lo cumple mejor?",
         ["V1 usa «oscura», «asustado» y «cosas raras», que son generales.", "V2 usa «las tres de la mañana», «el timbre sonó una vez», «un paraguas abierto, todavía mojado».", "V2 tiene detalles concretos que se pueden percibir."],
         "V2"),
        ("Renovar un cliché", "V1 comienza con «noche oscura». ¿Cómo lo renuevas sin perder la inquietud?",
         ["Identifica la fórmula repetida.", "Piensa en un detalle propio: una hora, un sonido, un objeto.", "Escribe: «A las tres de la mañana, la nevera se apagó».", "El detalle da inquietud sin la fórmula."],
         "Reemplazarlo por un detalle propio como la hora y un sonido"),
    ],
    mistakes=[("Elegir una versión porque «suena más bonita» sin aplicar criterios.", "El gusto no siempre coincide con el efecto buscado; hay que comprobarlo.", "Aplica a las dos versiones los mismos criterios y cita el pasaje que cumple cada uno."),
              ("Eliminar todas las emociones nombradas del texto.", "A veces nombrar una emoción es la mejor decisión; lo importante es que sirva al efecto.", "Mantén una emoción nombrada solo si el efecto la necesita y no la puedes mostrar mejor.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué es un cliché?", "Una expresión tan repetida que perdió fuerza", "Una imagen original", "Un narrador en primera persona", "El cliché es una fórmula gastada por el uso."),
        ("{F} ¿En qué versión aparece la hora exacta del suceso?", "V2", "V2 dice «a las tres de la mañana»."),
        ("{F} ¿Qué versión nombra directamente que el narrador está asustado?", "V1", "Solo V1 dice «estaba muy asustado» al comenzar."),
        ("abc", "{F} Criterio a) crea intriga. ¿Qué versión lo cumple mejor?", "V2, porque un paraguas mojado sin dueño plantea un enigma", "V1, porque dice que pasaban cosas raras", "Ambas por igual", "V2 plantea un misterio con un detalle concreto; V1 lo anuncia sin mostrarlo."),
        ("abc", "{F} Criterio c) deja inferir en lugar de explicar. ¿Qué versión lo cumple mejor?", "V2, porque no nombra el miedo y lo deja sentir", "V1, porque explica el miedo", "V1, porque usa «yo»", "V2 muestra y deja inferir; V1 explica la emoción."),
        ("ab", "{F} La expresión «cosas raras» en V1 es:", "Una expresión general sin detalle concreto", "Una imagen sensorial precisa", "No dice qué cosas son ni qué se percibe, así que es una expresión vaga y no una imagen."),
        ("abc", "{F} Un compañero dice que V2 es mejor «porque es más corta». ¿Qué le respondes?", "Que la extensión no es un criterio de la ficha y hay que aplicar a), b) y c) a las dos versiones", "Que lo más corto siempre es mejor", "Que no se pueden comparar versiones de distinto largo", "La comparación se hace con criterios del efecto buscado, no con la extensión."),
        ("abc", "{F} Se renueva el cliché de V1 con otro detalle. ¿Cuál es una buena opción?", "«La luz del pasillo parpadeó tres veces y se apagó»", "«Era una noche muy muy oscura»", "«Había oscuridad total»", "La primera opción introduce un detalle concreto y propio; las otras repiten la fórmula."),
        ("ab", "{F} Si el efecto buscado fuera ternura y no intriga, ¿cambiaría la elección?", "Sí: habría que revisar qué versión cumple criterios de ternura", "No: V2 siempre es mejor", "Los criterios dependen del efecto; con otro efecto los criterios cambian."),
        ("abc", "{F} Para comparar V1 y V2 de forma justa, ¿qué conviene?", "Aplicar los mismos criterios a ambas y citar pasajes", "Leer solo la que más te gusta", "Cambiar los criterios para cada versión", "Una comparación justa usa los mismos criterios y los respalda con pasajes."),
        ("abc", "Alguien escribe: «Estaba triste porque se fue mi amigo». ¿Cuál es una forma de mostrar la tristeza en lugar de decirla?", "«Dejó dos platos en la mesa y sirvió solo uno»", "«Estaba muy, muy triste»", "«La tristeza lo invadía»", "La primera muestra la pérdida con una acción y un objeto; las otras nombran la emoción."),
        ("ab", "{F} ¿Cuándo es adecuado decir en vez de mostrar?", "Cuando nombrar la emoción sirve al efecto y no hay mejor modo de mostrarla", "Siempre, porque es más fácil", "Decir es una decisión legítima si cumple el efecto buscado; no es un error en sí."),
        ("{F} Completa con una palabra de V2: «En el felpudo, un paraguas ____, todavía mojado».", "abierto", "V2 dice que el paraguas estaba abierto."),
    ],
    ctx=("abc", "Contexto: en el taller, dos compañeros eligen entre V1 y V2 para el inicio de su cuento colectivo, con el efecto de intriga. Uno dice «V1 porque es más clara»; la otra «V2 porque deja un misterio». ¿Cuál es el argumento mejor fundamentado en el efecto?", "V2, porque su detalle concreto abre un misterio y deja inferir", "V1, porque tiene más palabras", "Ninguno, porque no se puede decidir", "La decisión se apoya en el efecto de intriga y en un detalle concreto, no en la claridad ni en la extensión."),
    sc=[
        ("En Taller de literatura: ¿qué significa «mostrar» en lugar de «decir»?", "Presentar acciones u objetos para que lea quien saque la conclusión", "Mostrar deja que quien lee infiera en vez de recibir la emoción nombrada."),
        ("ab", "Para comparar dos versiones se usan:", "Los mismos criterios para ambas", "Criterios distintos para cada una", "Una comparación justa aplica los mismos criterios a las dos versiones."),
        ("ab", "Un cliché se renueva con:", "Un detalle propio y concreto", "La misma fórmula repetida", "El detalle concreto reemplaza la fórmula gastada."),
    ],
    op=("Elige uno de estos dos inicios para continuar: V1 o V2 de la ficha {F}. (1) Aplica los tres criterios a) b) c) a tu inicio elegido y escribe sí o no con una razón breve para cada uno; (2) reescribe el inicio que no elegiste para que cumpla mejor los tres criterios, en dos o tres oraciones.",
        "(1) Elijo V2. a) sí: el paraguas mojado plantea un misterio. b) sí: hora, timbre y paraguas. c) sí: no nombra el miedo. (2) V1 reescrito: «La luz del pasillo parpadeó tres veces. Desde el cuarto de al lado, alguien movía un mueble muy despacio.»",
        ["tres criterios aplicados con razón", "elección coherente", "reescritura que cumple los criterios", "detalles concretos propios"],
        ["aplicación de criterios y reescritura"],
        ["decidir solo por gusto", "reescritura que conserva el cliché", "razones sin pasajes"],
        "Pregunta: «¿qué criterio nuevo agregarías y qué versión lo cumpliría mejor?»."),
    reinforce="Reescribe esta frase para mostrar el miedo en vez de decirlo: «Tenía mucho miedo de entrar a la bodega».",
    extend="Explica por qué mostrar no siempre es mejor que decir y en qué casos una emoción nombrada es la mejor decisión.",
)

# ============================================================ OAC-02, clase 5
F = ("Ficha 5 (plan de ejemplo). Proyecto: microrrelato «El paraguas del felpudo», de 120 palabras, para leer en voz alta en una muestra del taller ante compañeros y familias. Plazo total: 14 días. "
     "Etapas: a) planificar y escribir el primer borrador; b) leer en voz alta para escuchar el ritmo; c) revisar con un compañero; d) reescribir; e) ensayo final y entrega. Pauta de ejemplo: el texto debe tener una hora, un objeto concreto y un final abierto.")
build(
    O2, 5, F,
    use="Aprenderé a planificar la escritura de un proyecto personal para una audiencia: etapas, tiempos, pauta de revisión y forma de compartirlo. Sirve para terminar un texto en plazo y con calidad.",
    prior=["Sé formular un proyecto con efecto y restricciones.", "Sé elegir recursos de escritura.", "Sé sumar y repartir días."],
    explain=[
        "Un proyecto de escritura se logra con un plan: etapas, tiempos y una pauta de calidad. Las etapas habituales son planificar, escribir un primer borrador, leer en voz alta, revisar con otra persona, reescribir y entregar. Poner fechas a cada etapa evita el error de dejar todo para el final y permite comprobar si el plazo alcanza.",
        "La pauta de revisión es una lista de condiciones que el texto debe cumplir, escrita antes de revisar. Puede incluir el efecto buscado, los recursos elegidos y las restricciones: por ejemplo, tener un objeto concreto, mantener la voz del narrador y no pasar de 120 palabras. Con la pauta, la revisión deja de ser una impresión y se vuelve comprobable.",
        "Pensar en la audiencia incluye decidir cómo se compartirá: lectura en voz alta, texto impreso o publicación en un mural. La lectura en voz alta exige oraciones que se puedan decir sin perder el aliento y pausas bien marcadas; el texto impreso permite más extensión. Un ensayo previo ante una persona de confianza ayuda a detectar frases difíciles y a ajustar el ritmo.",
    ],
    vocab=[("etapa", "fase de un proceso de trabajo"), ("borrador", "primera versión de un texto, que se espera mejorar"), ("pauta", "lista de condiciones que el texto debe cumplir"), ("plazo", "tiempo total disponible para terminar"), ("lectura en voz alta", "presentación de un texto leyéndolo ante un público")],
    worked=[
        ("Repartir un plazo", "Un proyecto tiene 14 días y cinco etapas. Se asignan 4, 2, 3, 3 y 2 días. ¿Alcanza el plazo?",
         ["Se suman los días: 4 + 2 + 3 + 3 + 2.", "El total es 14.", "El total coincide con el plazo."],
         "Sí, suman 14 días"),
        ("Usar la pauta", "El texto no tiene ninguna hora. ¿Qué hace la pauta de la ficha?",
         ["La pauta exige una hora, un objeto concreto y un final abierto.", "Compara el texto con la pauta: falta la hora.", "Agrega una hora precisa, por ejemplo a las tres de la mañana."],
         "Detecta lo que falta y se corrige"),
    ],
    mistakes=[("Dejar todo el trabajo para el último día.", "Sin etapas no hay tiempo para revisar ni reescribir, y la calidad baja.", "Pon fecha a cada etapa y comprueba que los días suman el plazo."),
              ("Revisar «a ojo» sin una pauta.", "Sin pauta la revisión depende del ánimo del día y se pasan por alto fallas.", "Escribe la pauta antes de revisar y compara el texto con ella.")],
    T=[
        ("{F} ¿Cuántas palabras debe tener el microrrelato?", "120", "La ficha fija 120 palabras como extensión del proyecto."),
        ("abc", "En Taller de literatura: ¿qué es una pauta de revisión?", "Una lista de condiciones que el texto debe cumplir", "Una opinión de la profesora", "Una versión final del texto", "La pauta se escribe antes de revisar y permite comprobar el texto."),
        ("{F} ¿Cuántas etapas tiene el plan?", "5", "Las etapas son a, b, c, d y e: cinco."),
        ("=", "{F} Otro plan reparte las etapas en 3, 2, 3, 2 y 2 días. ¿Cuántos días suman?", "3+2+3+2+2", "Se suman los días de cada etapa para compararlos con el plazo.", " días"),
        ("=", "{F} Si las primeras tres etapas duran 3, 2 y 4 días, ¿cuántos días quedan de los 14 para las dos últimas?", "14-(3+2+4)", "Se resta del plazo lo que ya se usó.", " días"),
        ("abc", "{F} ¿Cuál condición de la pauta puede comprobarse contando?", "El texto tiene 120 palabras", "El texto es bonito", "El texto es original", "Contar palabras es una comprobación objetiva; belleza y originalidad dependen de criterios más amplios."),
        ("abc", "{F} Un texto de 134 palabras ¿cumple la restricción de extensión?", "No: se pasa por 14 palabras", "Sí: la cantidad no importa", "No: faltan 14 palabras", "134 menos 120 es 14, así que excede la extensión."),
        ("ab", "{F} ¿Por qué conviene leer el borrador en voz alta antes de revisarlo con un compañero?", "Para escuchar el ritmo y detectar frases difíciles", "Para que el texto cambie de género", "La lectura en voz alta revela frases largas o confusas que a simple vista pasan inadvertidas."),
        ("abc", "{F} Un estudiante dedica 10 de los 14 días al primer borrador. ¿Qué problema tiene?", "Le quedan solo 4 días para leer, revisar, reescribir y ensayar", "Ninguno, porque es la etapa más importante", "Le sobran días", "Con 4 días restantes tocaría un solo día por etapa, muy poco para revisar y reescribir con calma."),
        ("=", "{F} Si 10 de los 14 días van al borrador, ¿cuántos días quedan para las otras etapas?", "14-10", "Se resta al plazo lo usado en el borrador.", " días"),
        ("abc", "{F} ¿Qué cambio es adecuado si el texto se va a leer ante familias y mide 120 palabras?", "Ensayar y marcar pausas en oraciones que se dicen sin perder el aliento", "Leerlo muy rápido para que alcance el tiempo", "Agregar un párrafo más largo para completar", "La lectura en voz alta pide oraciones dichas con claridad y pausas, no velocidad."),
        ("abc", "{F} Dos compañeros revisan tu texto. Uno dice «me gustó», otro dice «falta una hora precisa, como pide la pauta». ¿Cuál es el comentario más útil para reescribir?", "El segundo, porque se refiere a un criterio de la pauta", "El primero, porque es amable", "Ninguno es útil", "El comentario vinculado a la pauta indica qué cambiar; el de gusto no orienta la reescritura."),
        ("ab", "{F} Si tras la revisión descubres que el final no es abierto, ¿qué etapa corresponde?", "Reescribir, la etapa d", "Entrega final, la etapa e", "El final se corrige reescribiendo, antes del ensayo y la entrega."),
    ],
    ctx=("abc", "Contexto: tienes 10 días y cuatro etapas: escribir (3), leer y revisar (3), reescribir (2) y ensayar (2). Una amiga dice «con 10 días me sobra tiempo, empiezo mañana». ¿Qué le sugieres?", "Fijar fechas para las cuatro etapas, porque sumadas usan exactamente los 10 días", "Esperar a que le dé inspiración", "Dedicar los 10 días solo a escribir", "Las etapas suman 3 + 3 + 2 + 2 = 10, por lo que no sobra tiempo; hay que fijar fechas."),
    sc=[
        ("En Taller de literatura: ¿para qué sirve una pauta de revisión?", "Para comprobar si el texto cumple lo que se propuso", "La pauta convierte la revisión en comprobación y no en impresión."),
        ("ab", "Poner fecha a cada etapa permite:", "Comprobar que el plazo alcanza", "Evitar escribir", "Las fechas muestran si los días sumados caben en el plazo."),
        ("ab", "La lectura en voz alta ayuda a:", "Detectar frases difíciles y ajustar el ritmo", "Reemplazar la revisión por escrito", "Oír el texto revela problemas de ritmo y claridad."),
    ],
    op=("Para tu propio proyecto (puedes usar el de la ficha {F} o el que definiste en una clase anterior), escribe un plan con: (1) cinco etapas con los días de cada una, que sumen un plazo de 12 días; (2) una pauta de tres condiciones que el texto debe cumplir; (3) cómo lo compartirás y qué ensayo harás antes.",
        "(1) Planificar y escribir: 4; leer en voz alta: 1; revisar con compañero: 2; reescribir: 3; ensayo y entrega: 2 (total 12). (2) Tiene una hora, tiene un objeto concreto, mide máximo 120 palabras. (3) Lectura en voz alta ante el curso; ensayo con una persona de mi casa.",
        ["cinco etapas con días", "suma exacta de 12 días", "tres condiciones comprobables", "forma de compartir y ensayo"],
        ["plan de tres partes"],
        ["etapas que no suman 12", "pauta de condiciones vagas como «que quede bien»", "no prever un ensayo"],
        "Pregunta: «¿qué etapa recortarías si perdieras tres días y qué efecto tendría en el texto?»."),
    reinforce="Reparte 10 días entre escribir, revisar, reescribir y ensayar, de modo que los días sumen exactamente 10.",
    extend="Explica por qué una pauta de revisión escrita antes de revisar da mejores resultados que revisar «a ojo».",
)
