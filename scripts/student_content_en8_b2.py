"""Cuaderno del estudiante, 8.º básico Inglés (propuesta): EN08 OA 11, clases 4 y 5 (noticia breve; biografía y resumen).

Todos los textos y datos son originales y ficticios, con pista en español. Sin audio ni material externo.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA11 = "EN08 OA 11"


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


# ================================================================ clase 4: noticia breve
lesson(
    OA11, 4,
    "Las notas y los textos escritos en cada ejercicio, lápiz y una hoja. Todas las noticias de la clase son ficticias.",
    "Aprenderé a escribir una noticia breve con titular, primera oración con los datos esenciales y pie de foto. Sirve para informar con claridad lo que pasó a un lector que no estuvo ahí.",
    ["Conozco el pasado simple de verbos regulares, como cleaned.", "Sé usar who, what, when y where como preguntas."],
    [
        "Una noticia (news report) cuenta un hecho reciente. Tiene un titular (headline), que es corto y resume el hecho; una primera oración (lead) con los datos esenciales; detalles; y una foto con pie de foto. Modelo ficticio: «Headline: Class 8B Cleans Beach. Last Saturday, thirty students from Class 8B cleaned a local beach. They collected 45 kilos of plastic in two hours. “We want a clean beach for everyone,” said Valentina, a student». Pie de foto: «Students collect plastic on Saturday morning».",
        "El lead responde las preguntas who (quién), what (qué), when (cuándo) y where (dónde). Aquí: who = thirty students from Class 8B; what = cleaned a beach; when = last Saturday; where = a local beach. Los hechos pasados se cuentan en pasado simple: cleaned, collected, planted; y hay verbos irregulares como won, built y said. Las palabras exactas de una persona van entre comillas con said.",
        "Criterios: 1) titular corto; 2) lead con who, what, when y where; 3) verbos en pasado simple; 4) al menos un número o una cita; 5) pie de foto con un dato. Si dos personas tienen partes distintas de la información (una brecha de información, information gap), deben juntarlas antes de escribir: la noticia solo puede usar datos que alguien entregó.",
    ],
    [("headline", "titular: título corto de la noticia"), ("lead", "primera oración con los datos esenciales"), ("who / what / when / where", "quién / qué / cuándo / dónde"), ("said", "dijo (pasado de say)"), ("won", "ganó (pasado de win)"), ("collected", "recolectó"), ("caption", "pie de foto"), ("quote", "cita: palabras exactas entre comillas")],
    [
        ("Reconocer los datos del lead", "Oración: «Last Monday, 30 students planted 12 trees in the yard.» ¿Qué es who y qué es when?", ["Who responde quién: 30 students.", "When responde cuándo: Last Monday.", "Eso es todo lo que se pide."], "Who: 30 students. When: last Monday."),
        ("Pasar a pasado", "Completa: «Last week, the team ___ a prize.» (win)", ["La noticia cuenta un hecho pasado.", "El pasado de win es irregular.", "El pasado es won."], "won"),
    ],
    [
        ("Escribir el titular como una oración larga con muchos detalles.", "Un titular debe ser corto.", "Resume: Class 8B Cleans Beach."),
        ("Contar un hecho pasado con presente simple: «Thirty students clean the beach».", "El hecho ya ocurrió.", "Usa cleaned."),
    ],
    [
        ("Un headline es A) el título corto de la noticia B) la firma del periodista", "A", "El titular resume el hecho en pocas palabras."),
        ("El pasado de collect es A) collected B) collect", "A", "Es un verbo regular: se agrega -ed."),
        ("En «Thirty students cleaned the beach», ¿quién realizó la acción? Copia la respuesta.", "Thirty students", "Es el sujeto de la oración: quienes limpiaron."),
    ],
    [
        ("Texto: «Twenty-five students from Class 8A planted trees in the school yard.» ¿Cuál de estos cuatro datos falta: who, what, when o where?", "when", "El texto dice quién, qué y dónde, pero no cuándo."),
        ("¿Qué oración sirve de lead? A) Many people were happy. B) Last Monday, 30 students planted 12 trees in the yard.", "B", "Da quién, qué, cuándo y dónde; la otra no."),
        ("¿Qué signos encierran las palabras exactas de una persona en una noticia?", "Comillas", "Las comillas muestran que es una cita textual."),
    ],
    [
        ("Notas: who = 40 students of the choir; what = won first prize; when = last Thursday; where = the town theatre. ¿Qué oración es correcta? A) Last Thursday, 40 students of the choir won first prize in the town theatre. B) Last Thursday, 40 students of the choir win first prize in the town theatre.", "A", "Es un hecho pasado; won es el pasado de win."),
        ("Ana tiene: «Who: Class 8C. What: collected books. Where: school library.» Bruno tiene: «When: last Monday. How many: 120 books.» Al juntar las notas, ¿qué curso recolectó los libros y cuándo?", "Class 8C, last Monday", "Una nota da el curso y la otra el día."),
        ("Completa con la cita: «We worked hard,» ___ Ana. Opciones: said / say.", "said", "La cita se cuenta en pasado con said."),
    ],
    [
        ("Foto de estudiantes que cargan cajas con libros. ¿Qué pie de foto agrega información? A) Students with boxes. B) Class 8C carries 120 books to the library.", "B", "Dice quiénes, qué llevan y a dónde."),
        ("¿Cuál es un titular? A) The students of Class 8B cleaned the beach last Saturday morning B) Class 8B Cleans Beach", "B", "Es corto y resume el hecho."),
    ],
    [
        ("Ordena la noticia siguiendo el modelo de la clase (titular, lead, detalle y cita) y escribe las letras en orden. a) “We want a clean beach,” said Valentina. b) Class 8B Cleans Beach c) Last Saturday, thirty students cleaned a beach. d) They collected 45 kilos of plastic.", "b, c, d, a", "Va el titular, luego el lead, el detalle y por último la cita."),
        ("Corrige el verbo: «Last Saturday, thirty students clean the beach.» Escribe la oración corregida.", "Last Saturday, thirty students cleaned the beach.", "El hecho es pasado, así que el verbo clean pasa a cleaned."),
    ],
    [("El boletín del colegio recibe estas notas: Class 8D, chess tournament, won second place, Friday, school hall. ¿Qué oración no inventa datos? A) On Friday, Class 8D won second place in the chess tournament in the school hall. B) On Friday, Class 8D won first place in the chess tournament in the gym.", "A", "Usa solo los datos entregados; la otra cambia el lugar y el premio.")],
    [
        ("¿Qué cuatro preguntas responde el lead?", "Who, what, when y where", "Quién, qué, cuándo y dónde."),
        ("¿Cómo se llama el título corto de una noticia?", "Headline", "Es el titular."),
        ("¿En qué tiempo se cuenta un hecho que ya ocurrió?", "Pasado simple", "Por ejemplo cleaned o won."),
    ],
    task("Lee este encargo: escribe una noticia breve con estas notas ficticias. Notas: Class 8A, science fair, 18 projects, Wednesday, school gym, first prize to a solar oven model (modelo de horno solar). Escribe titular, lead, un detalle con un número y un pie de foto. No agregues datos que no estén en las notas, salvo una cita inventada y rotulada «cita de ejemplo». Revisa con los cinco criterios.", "Headline: Class 8A Shines at Science Fair. On Wednesday, Class 8A presented 18 projects in the school gym. A solar oven model won first prize. Caption: Class 8A shows its prize-winning project.", ["titular corto y lead con who, what, when y where", "verbos en pasado simple", "usa solo datos de las notas y tiene pie de foto"], ["hoja con la noticia y los criterios marcados"], ["inventar datos que no están en las notas", "usar presente para un hecho pasado"], "Lee tu noticia a una persona de tu casa y pregunta qué dato le faltó para entender qué pasó."),
    "Escribe cinco verbos regulares en pasado simple y úsalos en oraciones de noticia.",
    "Reescribe el mismo lead con otro orden de los datos y explica cuál suena mejor.",
)

# ================================================================ clase 5: biografía y resumen
lesson(
    OA11, 5,
    "Los textos y las fechas escritos en cada ejercicio, lápiz y una hoja. Las biografías de la clase son ficticias.",
    "Aprenderé a escribir una biografía breve con una línea de tiempo y a resumir un texto leído. Sirve para presentar la vida de una persona o el contenido de un texto en pocas líneas.",
    ["Conozco el pasado simple, incluido was born, built y studied.", "Sé ordenar hechos en secuencia."],
    [
        "Una biografía (biography) cuenta la vida de una persona. La primera oración dice quién es y cuándo nació: «Mario Vidal was born in 1980». Los hechos van en orden cronológico (chronological order), de lo más antiguo a lo más reciente, con el año y el verbo en pasado: «In 1990, he built a radio. In 2005, he studied engineering. In 2012, he opened a workshop». Para terminar, una oración dice por qué la persona es importante. Estas biografías son ficticias.",
        "Un recurso multimodal para una biografía es la línea de tiempo (timeline): una línea con los años ordenados y una frase corta por año, con una imagen o un pie de foto. Un resumen (summary) cuenta solo las ideas principales de un texto, con tus propias palabras. Es más corto que el original y no lleva detalles pequeños, ejemplos ni opiniones nuevas.",
        "Criterios de la biografía: 1) nombre y año de nacimiento en la primera oración; 2) hechos en orden cronológico con años; 3) verbos en pasado simple; 4) una oración final sobre su importancia; 5) línea de tiempo o pie de foto. Criterios del resumen: más corto que el texto, solo ideas principales, palabras propias y sin opiniones nuevas.",
    ],
    [("biography", "biografía: la vida de una persona contada por otra"), ("was born", "nació"), ("timeline", "línea de tiempo: años en orden con un hecho cada uno"), ("chronological order", "orden cronológico: del hecho más antiguo al más reciente"), ("summary", "resumen: las ideas principales en pocas palabras"), ("main idea", "idea principal"), ("built", "construyó (pasado de build)"), ("opened", "abrió")],
    [
        ("Ordenar años en una línea de tiempo", "Ordena los años de una línea de tiempo: 2012, 1980, 2005, 1990.", ["El hecho más antiguo va primero.", "El menor es 1980; sigue 1990, luego 2005.", "El último es 2012."], "1980, 1990, 2005, 2012"),
        ("Calcular una edad", "Mario nació en 1980 y abrió su taller en 2012. ¿Cuántos años pasaron entre su nacimiento y la apertura del taller?", ["Resta el año de nacimiento al año del hecho.", "2012 − 1980.", "Son 32 años."], "32 años"),
    ],
    [
        ("Escribir «he builded a radio».", "Build es irregular y no usa -ed.", "El pasado de build es built."),
        ("Poner en el resumen todos los ejemplos y datos pequeños.", "Un resumen solo conserva las ideas principales.", "Deja afuera los detalles y escribe con tus palabras."),
    ],
    [
        ("«She was born in 2001» significa A) Nació en 2001 B) Murió en 2001", "A", "Was born indica el momento del nacimiento."),
        ("El pasado de build es A) built B) builded", "A", "Es un verbo irregular."),
        ("Los hechos de una biografía se ordenan A) del más antiguo al más reciente B) por orden alfabético", "A", "Se sigue el orden cronológico."),
    ],
    [
        ("Mini biografía: «Lucía Paz was born in 1985. In 1995, she won a science prize. In 2010, she studied biology.» ¿En qué año ganó el premio?", "1995", "El texto lo indica con In 1995, she won."),
        ("Texto original: «Honey bees make honey. They also help flowers grow when they carry pollen. Some bees live in big groups.» ¿Qué resumen es mejor? A) Honey bees make honey and help flowers grow. B) Bees are the best insects and everyone loves them.", "A", "Conserva las ideas principales; la otra agrega una opinión nueva."),
        ("Texto: «Honey bees make honey. They also help flowers grow when they carry pollen. Some bees live in big groups.» ¿Qué oración se puede dejar fuera de un resumen de dos ideas principales? Copia la oración.", "Some bees live in big groups.", "Es un dato secundario frente a la miel y las flores."),
    ],
    [
        ex("Elisa nació en 1992 y publicó su primer libro en 2019. ¿Cuántos años pasaron entre su nacimiento y la publicación del libro?", "27", "Se resta el año de nacimiento al año de la publicación.", "2019 - 1992"),
        ("Completa con el pasado: «In 2010, she ___ to a new city.» (move)", "moved", "Move es regular y lleva -ed."),
        ("Ordena los años de una línea de tiempo, de menor a mayor: 2018, 2003, 2011, 1999", "1999, 2003, 2011, 2018", "Se ordena del año más antiguo al más reciente."),
    ],
    [
        ("¿Qué primera oración es mejor para una biografía? A) Mario Vidal was born in 1980 in a small town. B) Mario is nice and I like him.", "A", "Dice el nombre y el año de nacimiento; la otra es solo una opinión."),
        ("Una compañera dice que un resumen debe agregar tu opinión sobre el tema. ¿Tiene razón? Responde sí o no.", "No", "El resumen solo cuenta las ideas principales del texto."),
    ],
    [
        ("Corrige: «He was born in 1980 and he builded a radio in 1990.»", "He was born in 1980 and he built a radio in 1990.", "El pasado irregular de build es built."),
        ("Bio: «Lucía Paz was born in 1985. In 1995, she wins a science prize. In 2010, she studied biology.» ¿Qué verbo no está en pasado? Copia la palabra.", "wins", "Debería ser won, porque el hecho es de 1995."),
    ],
    [("Para el muro del colegio, una biografía ficticia debe llevar una línea de tiempo. ¿Cuál está bien armada? A) 1980 nació; 1990 construyó una radio; 2012 abrió un taller B) 2012 abrió un taller; 1980 nació; 1990 construyó una radio", "A", "Los años van de menor a mayor.")],
    [
        ("¿Qué es una línea de tiempo?", "Años en orden con un hecho cada uno", "Muestra el orden cronológico."),
        ("¿Qué debe conservar un resumen?", "Las ideas principales", "No conserva ejemplos ni detalles pequeños."),
        ("¿Qué verbo significa nació en inglés?", "was born", "Se usa en pasado."),
    ],
    task("Lee este encargo: elige uno. Opción 1: escribe una biografía de seis oraciones de la persona ficticia Pablo Reyes con estos datos: nació en 1975; en 1985 aprendió a tocar guitarra; en 1998 estudió música; en 2008 abrió una escuela para niños; hoy enseña a 40 estudiantes. La última oración dice por qué es importante. Opción 2: resume en una o dos oraciones este texto: «Honey bees make honey. They also help flowers grow when they carry pollen. Some bees live in big groups». Añade una línea de tiempo (opción 1) o una palabra clave (opción 2). Revisa con los criterios.", "Pablo Reyes was born in 1975. In 1985, he learned to play the guitar. In 1998, he studied music. In 2008, he opened a school for children. Today, he teaches 40 students. He is important because he helps children learn music. Timeline: 1975 – 1985 – 1998 – 2008.", ["primera oración con nombre y año, o resumen más corto que el texto", "hechos en orden cronológico con pasado simple, o solo ideas principales", "tiene línea de tiempo o palabra clave"], ["hoja con el texto y su línea de tiempo"], ["desordenar los años", "copiar el texto completo en el resumen"], "Pide a una persona de tu casa que lea tu texto y diga con sus palabras cuál es la idea principal."),
    "Escribe una línea de tiempo con cinco hechos de tu propia vida, con años en orden.",
    "Resume en dos oraciones un texto breve de otra asignatura y explica qué detalle dejaste afuera.",
)
