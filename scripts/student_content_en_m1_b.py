"""Cuaderno del estudiante, 1.º medio Inglés (propuesta): EN1M OA 11, escritura guiada por modelo y criterios con recursos multimodales.

Todos los textos en inglés son originales, breves y ficticios, con pista en español. Los modelos y criterios de cada
género están escritos dentro de la propia clase. Sin audio ni material externo. Cobertura del OA 11: este módulo enseña noticia, instrucciones, biografía, folleto y resumen; QUEDAN COMO VACÍO del OA los cuentos, los artículos, el diario personal (journal), los correos electrónicos y las descripciones, porque el plan solo tiene 5 clases. Los títulos de clase del plan son
genéricos (propósito, evidencia, estrategia, brecha de información, respuesta independiente): aquí se aplican a un
género por clase (noticia con pie de foto, instrucciones con íconos, biografía con línea de tiempo, folleto y resumen).
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA11 = "EN1M OA 11"


def E(rows):
    return [r if isinstance(r, dict) else ex(*r) for r in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ================================================================ clase 1: noticia con titular y pie de foto
lesson(
    OA11, 1,
    "Los modelos, datos y criterios escritos en cada ejercicio, lápiz y una hoja. Un computador es opcional.",
    "Aprenderé a escribir una noticia breve siguiendo un modelo y cinco criterios. Sirve para informar a lectores del diario mural o del sitio del colegio qué pasó, dónde, cuándo y con quiénes.",
    ["Sé usar el pasado simple de verbos regulares e irregulares comunes.", "Conozco las preguntas who, what, where y when."],
    [
        "Una noticia (news report) informa de un hecho real a un lector que no estuvo ahí; su audiencia (audience, quién lee) es el público del diario del colegio. Tiene cuatro partes en este orden: titular (headline), primera oración o lead, cuerpo (body) y cita (quote). Por convención el titular es corto y usa el presente simple aunque el hecho ya ocurrió: «Class 1B cleans the beach». El resto de la noticia se cuenta en pasado simple.",
        "El lead responde en una sola oración who (quién), what (qué), where (dónde) y when (cuándo): «On Friday, 28 students from Class 1B cleaned the beach near our town». El cuerpo agrega al menos un dato con número: «They collected 35 kilos of plastic in two hours». La cita muestra la voz de alguien e incluye said: «We want a clean beach for everyone,» said Fran. El recurso multimodal es una foto con pie de foto (caption), que agrega un dato nuevo y no repite el texto.",
        "Criterios para revisar: 1) titular corto con verbo en presente simple; 2) lead con who, what, where y when; 3) cuerpo con un número o un detalle en pasado simple; 4) una cita con said; 5) pie de foto con un dato nuevo. Al terminar, revisa tu noticia criterio por criterio.",
    ],
    [("headline", "titular: título corto de la noticia"), ("lead", "primera oración: responde who, what, where y when"), ("body", "cuerpo: detalles y números de la noticia"), ("quote", "cita: palabras de una persona entre comillas"), ("said", "dijo (verbo que introduce una cita)"), ("caption", "pie de foto: frase corta bajo una imagen"), ("audience", "audiencia: quién va a leer el texto"), ("purpose", "propósito: para qué escribes")],
    [
        ("Reconocer las partes de una noticia", "Noticia: «Headline: Class 1B cleans the beach. Lead: On Friday, 28 students from Class 1B cleaned the beach near our town. Body: They collected 35 kilos of plastic in two hours. Quote: «We want a clean beach for everyone,» said Fran.» ¿Qué datos de who, what, where y when da el lead?", ["Who: 28 students from Class 1B.", "What: cleaned the beach. Where: near our town.", "When: on Friday."], "Who: 28 estudiantes de 1B; what: limpiaron la playa; where: cerca de nuestra ciudad; when: el viernes."),
        ("Pasar un titular al presente simple", "Hecho: Class 2A planted trees ayer. Escribe el titular para el diario con el verbo plant y el nombre Class 2A.", ["El titular usa presente simple.", "Con Class 2A (tercera persona) el verbo lleva -s.", "Queda: Class 2A plants trees."], "Class 2A plants trees"),
    ],
    [
        ("Escribir el titular en pasado: «Class 2A planted trees».", "Se aplica la regla del cuerpo de la noticia al titular.", "El titular usa presente simple: Class 2A plants trees."),
        ("Poner en el lead solo «Our school had a great day».", "Es una opinión sin los datos who, what, where y when.", "Escribe quién, qué, dónde y cuándo en una oración concreta."),
    ],
    [
        ("En una noticia, ¿cómo se llama el título corto? A) headline B) caption", "A", "Headline es el titular; caption es el pie de foto."),
        ("¿Qué cuatro preguntas responde el lead de una noticia? Escríbelas en inglés, separadas por comas y en el orden de la explicación.", "who, what, where, when", "Son los cuatro datos que el lector necesita en la primera oración."),
        ("El titular «Students plant 60 saplings» usa A) presente simple B) pasado simple", "A", "Plant, sin -ed, es presente simple; así se escriben los titulares."),
    ],
    [
        ("Lead: «On Monday, the school band played in the main square.» ¿Dónde ocurrió el hecho? Responde en español.", "En la plaza principal", "La frase in the main square da el lugar."),
        ("¿Cuál de estas oraciones es el lead de una noticia? A) Everybody enjoyed the music B) On Monday, the school band played in the main square C) «We practiced for a month,» said Lía.", "B", "Responde who, what, where y when; las otras son una opinión y una cita."),
        ("Una foto muestra a estudiantes plantando árboles. ¿Qué pie de foto agrega un dato nuevo? A) Students plant trees B) Volunteers planted 40 young trees on Saturday.", "B", "Agrega número y día; el otro solo repite lo que ya se ve."),
    ],
    [
        ("Ordena las partes de una noticia y escribe las letras en orden: a) lead b) headline c) quote d) body", "b, a, d, c", "El orden del modelo es titular, lead, cuerpo y cita."),
        ("Completa el cuerpo en pasado simple con el verbo collect: «The volunteers ___ 120 bottle caps.»", "collected", "Es un verbo regular: collect más -ed."),
        ("Escribe la cita con said para estas palabras de Eva: «We were nervous but happy». Respuesta con el formato del modelo.", "«We were nervous but happy,» said Eva.", "La cita va entre comillas y la sigue said con el nombre."),
    ],
    [
        ("Lead: «On Saturday, 15 neighbors repaired a fence.» ¿Qué dato de who, what, where y when falta? Responde con una palabra en inglés.", "where", "No dice dónde está la reja, que es el dato where."),
        ("Noticia borrador. Headline: Big day at school! Lead: On Thursday, the choir of Class 3C sang at the town library. Body: They sang six songs for 80 people. Quote: «We were nervous but happy,» said Eva. Caption: The choir at the library. Con los cinco criterios de la clase, ¿cuántos cumple? Responde con un número.", "3", "Falla el titular, que no tiene verbo, y el pie de foto, que no agrega dato nuevo; cumple lead, cuerpo y cita."),
    ],
    [
        ("Hecho: un grupo de 3.º B recogió botellas plásticas en la playa. ¿Qué titular cumple el criterio 1? A) Class 3B collects plastic bottles B) Class 3B collected a lot of plastic bottles yesterday in the afternoon", "A", "Es corto y tiene el verbo en presente simple."),
        ("Pie de foto propuesto: «Volunteers planted 40 young trees on Saturday morning near the school.» La editora pide un pie de foto de máximo 10 palabras. ¿Cuántas palabras tiene y cumple? Responde con el número y sí o no.", "11, no", "Volunteers, planted, 40, young, trees, on, Saturday, morning, near, the, school suman 11."),
    ],
    [("El diario mural del colegio ficticio Los Aromos necesita una noticia. Datos: martes; 18 estudiantes de 1.º medio; hicieron un intercambio de libros en la biblioteca del colegio. ¿Qué lead usa todos los datos? A) On Tuesday, 18 students ran a book swap in the school library B) On Tuesday, 18 students ran a book swap C) A book swap is a good idea for every school.", "A", "Es la única que responde who, what, where y when.")],
    [
        ("¿En qué tiempo verbal se escribe el titular de una noticia?", "Presente simple", "Es la convención del género, aunque el hecho ya ocurrió."),
        ("¿Qué verbo introduce una cita?", "said", "Said va después de la cita y antes o después del nombre."),
        ("¿Qué debe agregar el pie de foto respecto del texto?", "Un dato nuevo", "No debe repetir lo que ya dice la noticia."),
    ],
    task("Lee este encargo: el diario del colegio necesita una noticia sobre una feria de ciencias. Datos de ejemplo: jueves; 40 estudiantes de 1.º medio; presentaron 12 proyectos en el gimnasio; una asistente dijo: «I loved the solar oven». Escribe en una hoja el titular, el lead, el cuerpo, la cita y un pie de foto para una foto imaginaria. Revisa con los cinco criterios y marca cada uno.", "Headline: Students show 12 science projects. Lead: On Thursday, 40 first-year students presented 12 projects in the school gym. Body: Families visited every table and asked questions. Quote: «I loved the solar oven,» said a visitor. Caption: Two students explain their project to a group of visitors.", ["titular corto con verbo en presente simple", "lead con who, what, where y when", "cuerpo en pasado simple con un dato, cita con said y pie de foto con dato nuevo"], ["hoja con la noticia y los cinco criterios marcados"], ["escribir el titular en pasado", "repetir el lead en el pie de foto"], "Lee tu noticia a una persona de tu casa y pregunta si entiende qué pasó, dónde y cuándo sin ver la foto."),
    "Escribe tres titulares de una palabra de acción cada uno sobre hechos del colegio, con el verbo en presente simple.",
    "Escribe una segunda noticia sobre el mismo hecho para un público de apoderados y cambia el tono de una oración.",
)

# ================================================================ clase 2: instrucciones con íconos
lesson(
    OA11, 2,
    "Los pasos y listas escritos en cada ejercicio, lápiz y una hoja. Para la tarea abierta basta con papel y lápiz.",
    "Aprenderé a escribir instrucciones con materiales, pasos numerados, palabras de secuencia e íconos. Sirve para que otra persona haga algo sola, mirando solo tu texto y tus dibujos.",
    ["Conozco verbos de acción como put, fold y write.", "Sé que first y then ordenan acciones."],
    [
        "Las instrucciones (instructions) explican cómo hacer algo y su propósito (purpose) es que el lector actúe sin ayuda. Tienen un título que comienza con How to, una lista de materiales con dos puntos y pasos numerados. Cada paso empieza con un verbo en imperativo, es decir, la forma base del verbo sin sujeto: Write the date. Un paso lleva una sola acción.",
        "Las palabras de secuencia ordenan los pasos: First, Next, Then, After that y Finally. Para advertir de un error posible se usa Don't + verbo: Don't press hard. Para dar un dato útil, Remember to + verbo. El recurso multimodal son los íconos: un dibujo simple junto a cada paso, como un reloj para el tiempo o un lápiz para escribir, que apoya el texto y ayuda a quien lee con prisa. Un ícono no reemplaza al verbo.",
        "Criterios: 1) título con How to; 2) materiales con dos puntos; 3) cada paso comienza con un verbo en imperativo; 4) pasos en orden, numerados o con palabras de secuencia, una acción por paso; 5) un ícono o dibujo por paso, descrito entre corchetes. Modelo: «How to make a study timer. Materials: a phone or clock, a pencil, a sheet. First, write your task on the sheet [pencil icon]. Next, set the clock for 25 minutes [clock icon]. Finally, stop and rest for 5 minutes [chair icon]».",
    ],
    [("instructions", "instrucciones: pasos para hacer algo"), ("imperative", "imperativo: verbo en forma base para dar una orden o un paso"), ("sequence word", "palabra de secuencia: First, Next, Then, Finally"), ("Don't + verb", "no hagas… (advertencia)"), ("Remember to + verb", "recuerda… (dato útil)"), ("materials", "materiales: lo que se necesita"), ("icon", "ícono: dibujo simple que apoya el texto"), ("step", "paso")],
    [
        ("Contar materiales y pasos", "Texto: «How to set up a recycling corner. Materials: three boxes, a marker, three labels. 1. Write PAPER, PLASTIC and CANS on the labels. 2. Stick a label on each box. 3. Put the boxes near the door. 4. Tell your class.» ¿Cuántos materiales y cuántos pasos hay?", ["Los materiales van tras los dos puntos: three boxes, a marker, three labels.", "Hay tres materiales de lista, es decir, boxes, marker y labels.", "Los pasos numerados son 4."], "3 materiales y 4 pasos"),
        ("Pasar una oración a imperativo", "Oración: «You write the date on the sheet.» Escríbela como paso de instrucciones.", ["Se quita el sujeto you.", "El verbo queda en forma base.", "Queda: Write the date on the sheet."], "Write the date on the sheet."),
    ],
    [
        ("Poner dos o tres acciones en un solo paso.", "El lector se confunde sobre el orden.", "Un paso, una acción, con su ícono."),
        ("Escribir «You should maybe think about the sheet» como un paso.", "No dice una acción concreta que se pueda hacer.", "Usa un verbo de acción: Fold the sheet in half."),
    ],
    [
        ("¿Con qué empieza el título de unas instrucciones? A) How to B) All about", "A", "How to anuncia que se explicará cómo hacer algo; All about presenta un tema, pero no pasos."),
        ("¿Cuál empieza como un paso de instrucciones? A) Fold the sheet in half B) You are folding the sheet.", "A", "Un paso comienza con el verbo en forma base."),
        ("¿Qué palabra de secuencia cierra la lista de pasos? Escríbela en inglés.", "Finally", "Finally indica el último paso."),
    ],
    [
        ("Paso: «Remember to save your file.» ¿Qué expresa Remember to? A) un dato útil para el lector B) un material de la lista", "A", "Remember to + verbo recuerda algo importante al lector."),
        ("Pasos del modelo: First, write your task. Next, set the clock for 25 minutes. Finally, stop and rest. ¿Qué haces justo después de poner el reloj?", "Stop and rest", "Finally es el paso siguiente a Next."),
        ("Don't press hard. Esta oración es A) una advertencia B) un material", "A", "Don't + verbo avisa de un error que se debe evitar."),
    ],
    [
        ("Ordena los pasos del temporizador de estudio y escribe las letras en orden: a) Finally, rest for 5 minutes. b) Next, set the timer for 25 minutes. c) Then, press Start. d) First, write your task.", "d, b, c, a", "Las palabras First, Next, Then y Finally marcan el orden."),
        ("Completa con First, Next o Finally: «___, open the file. ___, choose the folder. ___, click Save.»", "First, Next, Finally", "Cada palabra abre, continúa y cierra la secuencia."),
        ("Escribe en imperativo, empezando por el verbo: «You close the box with the lid.»", "Close the box with the lid.", "Se quita you y se deja el verbo en forma base."),
    ],
    [
        ("Texto: «How to make a bookmark. Materials: a paper strip, a pencil. 1. Fold the strip in half. 2. Write your name. 3. Draw a star.» ¿Qué criterio falla? A) El título no empieza con How to B) Los pasos no tienen ícono.", "B", "El título es correcto, pero no hay íconos entre corchetes en los pasos."),
        ("¿Qué paso está mejor escrito? A) Put the cups, the water and the seeds and wait B) Put the cup on the table. Then add water.", "B", "Separa las acciones y usa secuencia."),
    ],
    [
        ("Pasos: 1. Write the title. 2. Choose a picture. 3. Print the page. 4. Stick the page on the wall. Un paso inventado dice: «Check the picture is clear.» ¿Entre qué números debe ir para que tenga sentido, antes de imprimir? Responde con los números.", "Entre 2 y 3", "Se revisa la imagen elegida antes de imprimir."),
        ("Para el paso «Put the poster on the wall» necesitas un aviso. ¿Cuál es mejor? A) Don't use tape on the paint B) Remember to buy more tape.", "A", "Don't advierte de un daño posible a la pared; Remember to da un dato útil, pero no avisa de un daño."),
    ],
    [("El taller de periodismo escolar quiere un afiche para enseñar a subir un trabajo a la plataforma del colegio. Eligen entre un párrafo largo y una lista de cinco pasos numerados, cada uno con verbo y un ícono. ¿Qué opción es mejor? A) La lista de cinco pasos con íconos B) El párrafo sin números ni dibujos", "A", "Los pasos numerados con íconos se siguen más rápido.")],
    [
        ("¿Cómo comienza cada paso?", "Con un verbo en imperativo", "Fold, Write y Close son ejemplos."),
        ("¿Qué signo se escribe después de Materials?", "Dos puntos", "Los dos puntos anuncian la lista."),
        ("¿Cuántas acciones lleva un paso?", "Una", "Un paso, una acción."),
    ],
    task("Lee este encargo: elige una de estas dos instrucciones y escríbela en una hoja con título How to, materiales con dos puntos y de cuatro a seis pasos numerados, con palabras de secuencia y un ícono descrito entre corchetes en cada paso. Opción 1: cómo organizar la mochila para mañana. Opción 2: cómo preparar un horario semanal de estudio. Revisa con los cinco criterios y marca cada uno.", "How to pack your backpack. Materials: your timetable, your backpack. 1. First, read tomorrow's timetable [calendar icon]. 2. Next, put the notebooks in the backpack [notebook icon]. 3. Then add a pencil case [pencil icon]. 4. Finally, check the bag [check icon].", ["título con How to y materiales con dos puntos", "cada paso empieza con un verbo y lleva una sola acción", "pasos en orden con palabras de secuencia y un ícono por paso"], ["hoja con las instrucciones y los cinco criterios marcados"], ["poner dos acciones en un paso", "olvidar el ícono o la lista de materiales"], "Pide a una persona de tu casa que siga tus pasos sin ayudarte y anota dónde se confundió."),
    "Escribe cinco verbos en forma base que sirvan para pasos de unas instrucciones sobre cuidar tus útiles.",
    "Agrega a tus instrucciones dos advertencias con Don't y explica en español qué error evita cada una.",
)

# ================================================================ clase 3: biografía con línea de tiempo
lesson(
    OA11, 3,
    "Los datos, fechas y modelos escritos en cada ejercicio, lápiz y una hoja. Una regla para dibujar la línea de tiempo es opcional.",
    "Aprenderé a escribir una biografía breve de una persona, en orden de fechas y con una línea de tiempo. Sirve para contar la vida de alguien con datos claros y mostrar un resumen visual.",
    ["Sé usar el pasado simple con verbos regulares e irregulares comunes.", "Conozco was y were y sé leer años."],
    [
        "Una biografía (biography) cuenta la vida de una persona en tercera persona: he o she, o el nombre, nunca I. Se escribe en pasado simple porque son hechos terminados: She was born in 1990. She studied engineering. Se ordena cronológicamente, de lo más antiguo a lo más reciente. Para fijar el orden se usan fechas y expresiones como in 2008, at the age of 18, later y in the end. Los textos de esta clase son sobre personas ficticias.",
        "La primera oración dice quién es la persona, cuándo y dónde nació y por qué importa: «Rosa Lagos was born in 1990 in a small town and became an inventor». Después se cuentan de tres a cinco hechos, cada uno con su año. Verbos irregulares útiles: be → was/were, begin → began, win → won, build → built, become → became, go → went. Para saber la edad en un año, se resta el año de nacimiento: en 2008, 2008 − 1990 = 18, so she was 18.",
        "El recurso multimodal es la línea de tiempo (timeline): una línea con los años en orden y una frase corta bajo cada uno. Criterios: 1) título con el nombre; 2) primera oración con nacimiento y por qué es importante; 3) hechos en orden cronológico con año; 4) todo en pasado simple y en tercera persona; 5) línea de tiempo con al menos tres fechas. Modelo breve: «Rosa Lagos. Rosa Lagos was born in 1990 in a small town and became an inventor. In 2008 she won a school science fair. In 2013 she finished university. In 2020 she opened a small lab». Línea: 1990 born; 2008 science fair; 2013 university; 2020 lab.",
    ],
    [("biography", "biografía: texto sobre la vida de una persona"), ("was born", "nació"), ("timeline", "línea de tiempo: fechas en orden con una frase por fecha"), ("in + year", "en + año (in 2008)"), ("at the age of", "a la edad de"), ("later", "más tarde"), ("became", "se convirtió en (pasado de become)"), ("won / built / began", "ganó / construyó / comenzó")],
    [
        ("Leer una línea de tiempo", "Línea de tiempo de Rosa Lagos: 1990 born; 2008 science fair; 2013 university; 2020 lab. ¿Cuántos años pasaron entre la feria de ciencias y la apertura del laboratorio?", ["La feria fue en 2008.", "El laboratorio fue en 2020.", "2020 − 2008 = 12."], "12 años"),
        ("Pasar un dato al pasado simple", "Dato: «Rosa win a school science fair in 2008.» Corrígelo para la biografía.", ["Es un hecho terminado, así que va en pasado.", "El pasado irregular de win es won.", "Queda: Rosa won a school science fair in 2008."], "Rosa won a school science fair in 2008."),
    ],
    [
        ("Escribir «I was born in 1990» en la biografía de otra persona.", "Se mezcla la primera persona con un texto que debe ir en tercera.", "Usa he o she, o el nombre de la persona."),
        ("Escribir los años en desorden: 2020, 2008, 2013.", "Una biografía se ordena cronológicamente.", "Escríbelos de lo más antiguo a lo más reciente: 2008, 2013, 2020."),
    ],
    [
        ("Una biografía se escribe en A) tercera persona B) primera persona", "A", "Se habla de otra persona con he, she o su nombre."),
        ("¿Cuál es el pasado simple de build? Escríbelo en inglés.", "built", "Build es irregular: su pasado es built."),
        ("Una línea de tiempo muestra A) los años en orden con una frase corta B) un dibujo sin fechas", "A", "Une cada año con un hecho breve."),
    ],
    [
        ("Texto: «Mateo Silva was born in 1985. In 2003 he began to study music. In 2010 he built a small studio.» ¿Qué hizo Mateo en 2010? Responde en español.", "Construyó un pequeño estudio", "El texto dice in 2010 he built a small studio."),
        ("¿Qué primera oración cumple el criterio 2? A) Ana Vera was born in 1992 in a coastal town and became a famous diver B) Ana Vera is nice and has a dog.", "A", "Trae nacimiento, lugar y por qué es importante."),
        ("Línea de tiempo de Ana Vera: 1992 born; 2010 first prize; 2016 team captain. ¿Qué pasó en 2010? A) first prize B) team captain", "A", "Cada fecha trae una sola frase y 2010 es first prize."),
    ],
    [
        ("Ordena estos hechos en una biografía y escribe las letras en orden: a) In 2016 she became team captain. b) Ana Vera was born in 1992. c) In 2010 she won a first prize.", "b, c, a", "Se ordena por año: 1992, 2010 y 2016."),
        ("Completa con was o were: «Ana ___ born in 1992 and her parents ___ teachers.»", "was, were", "Ana es singular y parents es plural."),
        arith("Ana nació en 1992 y ganó el primer premio en 2010. ¿Cuántos años tenía cuando ganó?", "2010-1992", "Se resta el año de nacimiento al año del hecho."),
    ],
    [
        ("Borrador: «Ana Vera was born in 1992. In 2016 she became team captain. In 2010 she won a first prize.» ¿Qué criterio falla? A) El orden cronológico B) El uso del pasado simple", "A", "Primero aparece 2016 y después 2010; debería ser al revés."),
        ("Borrador: «Leo Pardo was born in 1980. He studies art in 2001. In 2010 he opened a gallery.» ¿Qué verbo hay que corregir? Escribe la forma correcta en pasado.", "studied", "Un hecho de 2001 va en pasado: studied, no studies."),
    ],
    [
        arith("Línea de tiempo de Leo Pardo: 1980 born; 2001 art school; 2010 gallery; 2022 book. ¿Cuántos años tenía cuando abrió la galería?", "2010-1980", "Se resta el año de nacimiento al año de la galería."),
        ("Una biografía debe tener al menos tres fechas en la línea de tiempo (criterio 5). Una línea trae: 1980 born; 2022 book. ¿Cumple? A) No, tiene solo dos fechas B) Sí, porque las fechas están en orden.", "A", "El criterio exige al menos tres fechas y aquí hay dos."),
    ],
    [("Un museo escolar ficticio publica la vida de la ingeniera ficticia Elisa Prado. Datos: nació en 1978 en un pueblo; en 1996 ganó una beca; en 2002 construyó un puente de pruebas; en 2015 abrió una escuela. ¿Qué oración cuenta bien el dato de 2002 en el cuerpo? A) In 2002 she built a test bridge B) In 2002 she builds a test bridge.", "A", "El hecho ya ocurrió y build en pasado es built.")],
    [
        ("¿En qué persona se escribe una biografía?", "Tercera persona", "Se habla de otra persona."),
        ("¿En qué orden se cuentan los hechos?", "Cronológico", "De lo más antiguo a lo más reciente."),
        ("¿Cuál es el pasado de win?", "won", "Es un verbo irregular, no lleva -ed."),
    ],
    task("Lee este encargo: escribe la biografía de una persona ficticia con estos datos de ejemplo. Nombre: Camila Reyes. Nació en 1999 en un pueblo; en 2012 comenzó a tocar el violín; en 2017 ganó un concurso regional; en 2023 abrió una escuela de música. Escribe en una hoja un título, una primera oración con por qué importa, tres o cuatro hechos en pasado simple y una línea de tiempo con las cuatro fechas. Revisa con los cinco criterios.", "Camila Reyes. Camila Reyes was born in 1999 in a small town and became a music teacher. In 2012 she began to play the violin. In 2017 she won a regional contest. In 2023 she opened a music school. Timeline: 1999 born; 2012 violin; 2017 contest; 2023 school.", ["título con nombre y primera oración que dice por qué importa", "hechos en orden cronológico, en pasado simple y tercera persona", "línea de tiempo con al menos tres fechas"], ["hoja con la biografía, la línea de tiempo y los cinco criterios marcados"], ["mezclar primera persona o presente", "dar los años en desorden"], "Pide a una persona de tu casa que lea tu línea de tiempo y cuente la vida de Camila con sus propias palabras."),
    "Escribe cinco oraciones sobre tu vida escolar con was o were, sin datos personales sensibles.",
    "Escribe dos oraciones sobre la persona ficticia Camila Reyes que no estén en el modelo, con un verbo irregular en pasado.",
)

# ================================================================ clase 4: folleto
lesson(
    OA11, 4,
    "Los datos del evento y los modelos escritos en cada ejercicio, lápiz y una hoja plegada en tres si quieres. Sin materiales especiales.",
    "Aprenderé a escribir el texto de un folleto (brochure) para invitar a un evento con título llamativo, secciones y datos clave. Sirve para que el lector decida ir y sepa cuándo, dónde y cuánto cuesta.",
    ["Sé escribir fechas, horas y precios en inglés.", "Conozco las órdenes Come y Join."],
    [
        "Un folleto (brochure) es una hoja plegada que informa y también invita. Su propósito (purpose) es convencer a un lector rápido, por eso el texto es corto. Tiene un título llamativo (catchy title), secciones con subtítulos (headings) y viñetas (bullet points) con datos clave. Ejemplo de título: «Join the Science Fair!». Ejemplo de subtítulos: What, When, Where y Price.",
        "Los datos clave se escriben con la preposición correcta: on + día (on Friday), at + hora (at 4 p.m.), at/in + lugar (at the school gym), y el precio con free (gratis) o el valor: Price: $1.000. El folleto termina con una invitación o llamado a la acción (call to action): Come and see!, Join us! o Bring a friend! También usa un recurso multimodal: una imagen con descripción corta entre corchetes, como [photo: a student shows a robot].",
        "Criterios para revisar: 1) título llamativo con una invitación; 2) subtítulos con viñetas, uno por dato; 3) los datos what, when, where y price; 4) frases cortas, de máximo 10 palabras por viñeta; 5) una imagen descrita y una invitación final. Modelo: «Join the Science Fair! What: 12 student projects. When: on Friday at 4 p.m. Where: at the school gym. Price: free. [photo: a student shows a robot] Come and see!».",
    ],
    [("brochure", "folleto: hoja plegada que informa e invita"), ("heading", "subtítulo de una sección"), ("bullet point", "viñeta: línea corta con un dato"), ("call to action", "llamado a la acción: invitación final"), ("free", "gratis"), ("price", "precio"), ("on / at", "on + día; at + hora o lugar"), ("catchy", "llamativo")],
    [
        ("Leer los datos clave", "Folleto: «Join the Book Club! What: we read short stories. When: on Wednesday at 3:30 p.m. Where: in the library. Price: free. Come and read with us!» ¿Qué día y a qué hora es?", ["Busca el subtítulo When.", "Dice on Wednesday.", "La hora es at 3:30 p.m."], "El miércoles a las 15:30"),
        ("Acortar una viñeta", "Viñeta larga: «The activity is going to take place in the main hall of the school building.» Escribe una versión de máximo 10 palabras que conserve el lugar, empezando con Where:", ["Se quita lo repetido.", "Se conserva main hall.", "Queda: Where: in the main hall."], "Where: in the main hall."),
    ],
    [
        ("Escribir «Join the Book Club» como título y quitar la invitación final.", "Se olvida el llamado a la acción al terminar.", "Agrega una frase como Come and read with us!"),
        ("Poner un párrafo largo en cada sección.", "El lector rápido no encuentra los datos.", "Usa viñetas cortas con un dato cada una."),
    ],
    [
        ("Un folleto es una hoja A) plegada que informa e invita B) que solo cuenta una historia en pasado", "A", "Un folleto informa y también invita."),
        ("¿Qué significa free en la sección Price? Responde en español.", "Gratis", "Free indica que no cuesta dinero."),
        ("¿Cuál es un llamado a la acción? A) Join us! B) Price: free", "A", "Join us! invita al lector a participar; Price: free es un dato, no una invitación."),
    ],
    [
        ("Folleto: «What: board games. When: on Saturday at 11 a.m. Where: in the community center. Price: $2.000.» ¿Cuánto cuesta y dónde es?", "$2.000; en el centro comunitario", "Price da $2.000 y Where da el lugar."),
        ("¿Cuál es el subtítulo que indica el lugar del evento? A) Where B) Price", "A", "Where pregunta dónde; Price indica cuánto cuesta."),
        ("Elige la preposición correcta: «The party is ___ Friday.» A) on B) at", "A", "Con días de la semana se usa on."),
    ],
    [
        ("Completa con on o at: «The workshop is ___ Thursday ___ 5 p.m.»", "on, at", "Con el día se usa on y con la hora, at."),
        ("Escribe la viñeta de lugar con estos datos, empezando con Where: y usando at: el gimnasio del colegio.", "Where: at the school gym.", "El subtítulo Where va seguido del lugar con at."),
        ("Cuenta las palabras de la viñeta «When: on Friday at 4 p.m.» (sin contar los signos). Responde con el número.", "6", "When, on, Friday, at, 4 y p.m. suman 6."),
    ],
    [
        ("Folleto: «Chess Day! What: a tournament for beginners. When: on Sunday. Price: free.» ¿Qué dato clave falta? Responde en inglés con el subtítulo.", "Where", "No dice en qué lugar será."),
        ("Un folleto trae título, subtítulos con viñetas con los datos what, when, where y price, imagen descrita y un llamado a la acción, pero una viñeta tiene 18 palabras. Con los cinco criterios, ¿cuál criterio falla? Responde con su número.", "4", "El criterio 4 pide máximo 10 palabras por viñeta."),
    ],
    [
        ("Elige el mejor título para un folleto de una feria de libros: A) Book Fair! Come and Find Your Next Story B) A document about a school activity", "A", "Es llamativo y trae una invitación."),
        ("Evento: función de teatro el sábado a las 6 p.m. en el gimnasio; entrada: $1.000. Folleto 1: «When: on Saturday at 6 p.m. Where: at the gym. Price: $1.000.» Folleto 2: «When: on Saturday. Price: free.» ¿Qué folleto da todos los datos correctos? A) El folleto 1 B) El folleto 2", "A", "A incluye hora, lugar y precio correctos; B omite lugar y cambia el precio."),
    ],
    [("Un taller de robótica ficticio ofrece un folleto con estos datos: martes a las 4 p.m.; sala 5; precio $3.000; llevar un cuaderno. ¿Cuál viñeta de When es correcta? A) When: on Tuesday at 4 p.m. B) When: at Tuesday in 4 p.m. C) When: Tuesday on 4 p.m.", "A", "Usa on con el día y at con la hora.")],
    [
        ("¿Qué subtítulo indica cuánto cuesta?", "Price", "Price es el precio."),
        ("¿Cuántas palabras como máximo tiene una viñeta?", "10", "El criterio 4 lo pide."),
        ("¿Cómo se llama la invitación final?", "Call to action", "Es el llamado a la acción."),
    ],
    task("Lee este encargo: escribe el texto de un folleto para el evento ficticio «Concierto de otoño del taller de música». Datos: sábado a las 7 p.m.; en el patio techado; entrada: $2.000; 10 canciones. Escribe en una hoja un título llamativo, subtítulos con viñetas (What, When, Where y Price), una imagen descrita entre corchetes y una invitación final. Revisa con los cinco criterios.", "Join our Autumn Concert! What: 10 songs by the music workshop. When: on Saturday at 7 p.m. Where: in the covered yard. Price: $2.000. [photo: students with guitars] Come and listen!", ["título llamativo e invitación final", "subtítulos con viñetas de máximo 10 palabras", "datos what, when, where y price correctos, e imagen descrita"], ["hoja con el folleto y los cinco criterios marcados"], ["olvidar el lugar o el precio", "escribir párrafos largos"], "Muestra tu folleto a una persona de tu casa y pregunta qué dato encontró primero."),
    "Escribe tres títulos llamativos para folletos de actividades del colegio.",
    "Traduce a inglés las cuatro viñetas del evento con el mismo formato y compáralas con el modelo.",
)

# ================================================================ clase 5: resumen
lesson(
    OA11, 5,
    "El texto, los criterios y los datos escritos en cada ejercicio, lápiz y una hoja. Sin materiales especiales.",
    "Aprenderé a resumir un texto leído en pocas oraciones, con mis propias palabras y con una pequeña imagen que lo apoye. Sirve para estudiar y para contar a otra persona lo esencial de algo que leíste.",
    ["Sé encontrar la idea principal de un párrafo.", "Conozco conectores simples como and, but y because."],
    [
        "Un resumen (summary) es un texto corto que conserva solo lo esencial de un texto más largo. Su propósito (purpose) es que quien lo lee entienda las ideas importantes sin leer el original. Se escribe en tercera persona y en presente si el texto original describe hechos generales. No incluye tu opinión (I think…) ni detalles menores como ejemplos secundarios.",
        "Pasos: 1) lee y subraya la idea principal (main idea), que suele estar en la primera o segunda oración; 2) elige dos o tres detalles clave (key details) que la apoyan; 3) reescribe con tus palabras, sin copiar frases completas; 4) une las ideas con conectores como and, also y so; 5) revisa que sea más corto que el original. El recurso multimodal es un esquema o ícono: un dibujo simple o un cuadro de tres ideas que acompaña el resumen.",
        "Criterios: 1) la primera oración da la idea principal; 2) incluye dos o tres detalles clave; 3) usa tus propias palabras; 4) no tiene opiniones personales; 5) mide como máximo un tercio del original y lleva un esquema. Texto de práctica: «Bike to School Week (original, ficticio). Our town holds Bike to School Week every April. Students ride to school instead of using cars. Last year, 220 students joined. The town painted a bike lane near the school. Families said the street was calmer. The week also helps students stay active».",
    ],
    [("summary", "resumen: texto corto con lo esencial"), ("main idea", "idea principal"), ("key detail", "detalle clave que apoya la idea principal"), ("own words", "con tus propias palabras"), ("opinion", "opinión personal"), ("also", "también"), ("diagram", "esquema: dibujo o cuadro que resume ideas"), ("shorter", "más corto")],
    [
        ("Encontrar la idea principal", "Texto de práctica de la clase (Bike to School Week). ¿Cuál es la idea principal? A) Students ride to school instead of using cars during one week in April B) The town painted a bike lane.", ["La idea principal explica de qué trata todo el texto.", "B es un detalle del texto.", "A resume el tema completo."], "A"),
        ("Contar palabras para el límite", "El texto de práctica tiene 44 palabras. El resumen puede medir como máximo un tercio de ese número. Calcula el máximo y redondea hacia abajo.", ["Se divide 44 entre 3.", "44 ÷ 3 = 14 con resto 2.", "El máximo es 14 palabras."], "14 palabras"),
    ],
    [
        ("Copiar frases enteras del original.", "Se piensa que resumir es solo cortar partes, sin reescribir.", "Usa tus propias palabras: Students ride to school in April."),
        ("Agregar «I think it is a great idea».", "Un resumen informa, no incluye opiniones.", "Quita la opinión y deja solo la información."),
    ],
    [
        ("Un resumen conserva A) solo lo esencial B) todos los detalles", "A", "Es corto porque deja fuera lo menos importante."),
        ("¿Cuál de estas frases es una opinión y no va en un resumen? A) I think it is boring B) Students ride to school.", "A", "I think… expresa una opinión personal."),
        ("¿Dónde suele estar la idea principal? Responde en español.", "En la primera o segunda oración", "Casi siempre se presenta al comienzo."),
    ],
    [
        ("Texto: «Sofía's club plants a mint garden. The club meets every Monday. Students water the plants and sell small bags of mint. They give the money to a pet shelter». ¿Cuál es la idea principal? A) The club plants a mint garden and sells mint for a shelter B) The club meets on Monday.", "A", "Resume el tema completo del texto."),
        ("Texto: «Sofía's club plants a mint garden. The club meets every Monday. Students water the plants and sell small bags of mint. They give the money to a pet shelter». ¿Qué dato es un detalle clave sobre el dinero? Responde en español.", "Lo dan a un refugio de mascotas", "Dice que dan el dinero a un pet shelter."),
        ("¿Cuál reescribe con otras palabras «The club meets every Monday»? A) Members get together on Mondays B) The club meets every Monday.", "A", "A cambia las palabras y mantiene el sentido; B copia la frase."),
    ],
    [
        ("¿Cuál reescribe «Last year the class collected 300 kilos of paper.» con otras palabras sin cambiar el dato? A) Last year the class gathered 300 kilos of paper B) Last year the class collected 30 kilos of paper.", "A", "Gathered es sinónimo de collected y se mantiene la cifra; B cambia el dato."),
        ("Elige el conector que suma un dato al anterior: «The town painted a bike lane. ___ families said the street was calmer.» A) Also B) However", "A", "Also suma un dato del mismo texto; however marcaría un contraste que no existe."),
        ("Resumen de 21 palabras para un texto de 60 palabras. Un tercio de 60 es 20. ¿Cumple el criterio 5? Responde sí o no.", "No", "21 supera el máximo de 20 palabras."),
    ],
    [
        ("Resumen borrador del texto Bike to School Week: «Bike to School Week takes place every April. Students go to school by bike. Last year, 220 students joined. The town painted a bike lane. I think the week is great.» Revisa solo los criterios 1 a 4. ¿Qué criterio falla? Responde con su número.", "4", "I think the week is great es una opinión personal."),
        ("Un resumen ya cumple los criterios 1 a 4 y mide menos de un tercio del original. ¿Qué le falta para cumplir el criterio 5? A) Un esquema o ícono B) Un ejemplo copiado del original", "A", "El criterio 5 pide un esquema que acompañe el texto."),
    ],
    [
        ("Texto: «The school library opened a quiet room. It has 12 desks and 4 lamps. Students use it before exams. It is open from 2 p.m. to 5 p.m.» ¿Qué dos detalles clave pondrías en un resumen de dos oraciones, además de la idea principal? A) El horario y que se usa antes de los exámenes B) El número de lámparas y de escritorios", "A", "Responden para qué sirve y cuándo está abierta; las cifras de muebles son menos importantes."),
        ("Resumen de práctica: «The library has a quiet room open from 2 p.m. to 5 p.m. Students use it before exams.» Cuenta las palabras y escribe el número, contando 2, 5 y p.m. como palabras separadas.", "18", "The library has a quiet room open from 2 p.m. to 5 p.m. suman 13 y Students use it before exams suman 5."),
    ],
    [("La profesora pide resumir en una sola oración este texto ficticio: «The town lake is small and clean. Volunteers clean it every year. Last Sunday, 60 neighbors picked up litter. Now ducks and fish live there». ¿Qué oración es el mejor resumen? A) Volunteers clean the town lake every year, so ducks and fish live there B) Last Sunday, 60 neighbors picked up litter.", "A", "Resume el hecho central con su causa; la otra opción es solo un detalle.")],
    [
        ("¿Qué incluye la primera oración de un resumen?", "La idea principal", "Dice de qué trata todo el texto."),
        ("¿Se pueden incluir opiniones en un resumen?", "No", "Un resumen solo informa."),
        ("¿Cuánto puede medir como máximo?", "Un tercio del original", "El criterio 5 fija ese límite."),
    ],
    task("Lee este texto ficticio y escribe un resumen. Texto: «The school radio starts at 8 a.m. Students read the news for five minutes. Then they play a short song and share the weather. Last month, 30 students asked to join the team. The team meets every Tuesday to practice». El texto tiene 40 palabras, así que tu resumen puede tener como máximo 13. Escribe en una hoja un resumen con la idea principal y dos detalles, sin opiniones, y añade un esquema de tres cajas. Revisa con los cinco criterios.", "The school radio shares news, a song and the weather at 8 a.m. Diagram: [news] [song] [weather].", ["la primera oración da la idea principal", "incluye dos detalles clave con tus propias palabras y sin opiniones", "tiene 13 palabras o menos y un esquema"], ["hoja con el resumen, el esquema y los cinco criterios marcados"], ["copiar frases enteras", "agregar una opinión personal"], "Cuenta a una persona de tu casa el contenido del texto usando solo tu resumen y pregunta si entendió."),
    "Subraya en un texto breve de otro curso la idea principal y dos detalles clave.",
    "Resume el mismo texto en una sola oración y compara qué detalle dejaste fuera.",
)
