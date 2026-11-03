"""Cuaderno del estudiante, 8.º básico Inglés (propuesta): EN08 OA 12, clases 4 y 5 (información esencial o adicional con who y which; voz pasiva).

Textos originales y breves, con pista en español. Los títulos de clase del plan son genéricos; aquí cada clase
aplica una función del OA.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA12 = "EN08 OA 12"


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


# ================================================================ clase 4: who y which
lesson(
    OA12, 4,
    "Los textos y oraciones escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a agregar información esencial o adicional a una oración con who y which. Sirve para escribir textos más precisos sin repetir muchas oraciones cortas.",
    ["Sé escribir oraciones simples con be y con verbos en presente y pasado.", "Conozco las comas y los puntos."],
    [
        "Una cláusula con who o which agrega información a un sustantivo. Who se usa para personas: Simon is the boy who lives next door. Which se usa para cosas: The book which I borrowed was long. Con esta estructura unes dos oraciones cortas en una: «I have a friend. He plays the guitar» pasa a «I have a friend who plays the guitar».",
        "Hay dos usos. Cuando la información es esencial, sin ella no sabríamos de quién o de qué se habla, y no lleva comas: Simon is the boy who lives next door. Cuando la información es adicional, solo agrega un dato extra, va entre comas: The science book, which I borrowed from the library, is very interesting. Si quitas la parte entre comas, la oración sigue teniendo sentido.",
        "Al revisar un texto, pregunta primero si el sustantivo es persona (who) o cosa (which). Luego decide si el dato identifica o solo agrega algo, y pon las comas según corresponda. Usa estas cláusulas con mesura: una o dos por texto bastan para que se lea con fluidez.",
    ],
    [("who", "que / quien (para personas)"), ("which", "que / el cual (para cosas)"), ("essential information", "información esencial: identifica de quién o de qué hablas"), ("extra information", "información adicional: agrega un dato extra, entre comas"), ("borrowed", "pidió prestado"), ("next door", "en la casa de al lado"), ("noun", "sustantivo: palabra que nombra personas, cosas o lugares"), ("clause", "cláusula: parte de una oración con su propio verbo")],
    [
        ("Elegir who o which", "Completa: «The girl ___ sings is my cousin.» Opciones: who / which.", ["Girl es una persona.", "Para personas se usa who.", "Queda The girl who sings is my cousin."], "who"),
        ("Poner comas a un dato adicional", "Escribe con comas: «My bike which is blue was a gift.»", ["Which is blue es un dato extra.", "Va entre comas.", "Queda My bike, which is blue, was a gift."], "My bike, which is blue, was a gift."),
    ],
    [
        ("Usar which para una persona: «The girl which sings».", "Which no se usa para personas.", "Usa who: The girl who sings."),
        ("Poner comas en un dato esencial: «The boy, who lives next door, is Simon» cuando hay varios chicos.", "Si el dato identifica al chico, no lleva comas.", "Escribe The boy who lives next door is Simon."),
    ],
    [
        ("Completa: «The girl ___ sings is my cousin.» A) who B) which", "A", "Girl es una persona y pide who."),
        ("Completa: «The book ___ I borrowed is long.» A) which B) who", "A", "Book es una cosa y pide which."),
        ("La información adicional de una oración se escribe entre A) comas B) dos puntos", "A", "Las comas separan el dato extra del resto."),
    ],
    [
        ("«Simon is the boy who lives next door.» ¿Qué hace la parte who lives next door? A) Identifica de cuál chico se habla B) Agrega un dato que no es necesario", "A", "Sin esa parte no sabríamos qué chico es Simon."),
        ("«The science book, which I borrowed from the library, is very interesting.» Si quitas la parte entre comas, ¿la oración sigue teniendo sentido? Responde sí o no.", "Sí", "La parte entre comas es solo información adicional."),
        ("Completa: «The museum ___ opens at 9:00 is free.» Opciones: who / which.", "which", "Museum es una cosa."),
    ],
    [
        ("Une con who: «I have a friend. He plays the guitar.»", "I have a friend who plays the guitar.", "Who reemplaza al sujeto he y une las dos ideas."),
        ("Une con which: «We read a poster. It announced the fair.»", "We read a poster which announced the fair.", "Which reemplaza al sujeto it, que es una cosa."),
        ("Agrega comas: «The library which opens at 8:00 is in the center.» (el dato es adicional)", "The library, which opens at 8:00, is in the center.", "El horario es un dato extra y va entre comas."),
    ],
    [
        ("«The girl who won the race is in my class.» ¿La parte who won the race identifica a la niña o es un dato extra?", "Identifica a la niña", "Dice cuál de las niñas es, así que es esencial."),
        ("¿Qué oración es correcta? A) The teacher who teaches music is Ms. Soto. B) The teacher which teaches music is Ms. Soto.", "A", "Teacher es una persona y pide who."),
    ],
    [
        ("¿Qué oración es correcta? A) My cousin, who lives in Osorno, plays chess. B) My cousin, which lives in Osorno, plays chess.", "A", "Un primo es una persona, por lo que corresponde who."),
        ("Une las dos oraciones con which y comas, como dato adicional el horario de apertura: «The library is the best in town. It opens at 7:30.» Empieza con «The library» y termina con «is the best in town».", "The library, which opens at 7:30, is the best in town.", "Which agrega el horario como dato extra entre comas."),
    ],
    [("Aviso para el diario mural: «The girl ___ lost a blue scarf should go to the office.» ¿Qué palabra completa la oración? A) who B) which", "A", "La oración habla de una persona, por lo que corresponde who.")],
    [
        ("¿Qué palabra se usa para personas: who o which?", "who", "Who es para personas."),
        ("¿Qué palabra se usa para cosas?", "which", "Which es para cosas."),
        ("¿Dónde se escribe la información adicional?", "Entre comas", "Las comas la separan del resto."),
    ],
    task("Lee este encargo: une en tu hoja cada par de oraciones usando who o which, y marca con comas solo la información adicional. Pares: 1) I have a neighbour. He grows tomatoes. 2) The park has a small lake. It is very old. 3) Ms. Rojas teaches Art. She is my favourite teacher. Escribe además una oración propia con who sobre alguien que conozcas.", "1) I have a neighbour who grows tomatoes. 2) The park has a small lake, which is very old. 3) Ms. Rojas, who teaches Art, is my favourite teacher.", ["elige who para personas y which para cosas", "usa comas solo con información adicional", "escribe una oración propia correcta"], ["hoja con las oraciones y los dos recursos marcados"], ["usar which para una persona", "poner comas en un dato esencial"], "Lee tus oraciones a una persona de tu casa y pregunta cuál dato es esencial y cuál adicional."),
    "Escribe cuatro oraciones sobre tus amigos con who y cuatro sobre objetos con which.",
    "Une tres pares de oraciones sobre tu barrio con who o which y explica dónde pusiste comas.",
)

# ================================================================ clase 5: voz pasiva
lesson(
    OA12, 5,
    "Los textos y oraciones escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a describir procesos y acciones con la voz pasiva, cuando quien hace la acción no se conoce o no importa. Sirve para escribir carteles, informes y descripciones de procesos.",
    ["Conozco el pasado simple y los participios, como made y found.", "Sé usar am, is, are, was y were."],
    [
        "En la voz pasiva el objeto pasa a ser el centro de la oración. Se forma con be + participio pasado. En presente: Rooms are cleaned daily; Plastic is produced from oil. En pasado: The money was found on the floor. Es útil cuando no sabes quién hizo la acción o cuando no importa: «My bike was stolen» no dice quién.",
        "Usa is o are en presente (is con singular, are con plural) y was o were en pasado. El participio puede ser regular (cleaned, dried) o irregular (made, found, broken, written, taken, built). Para describir un proceso, la pasiva permite centrarse en las etapas: Paper is made from wood. First, wood is cut. Then it is mixed with water. Finally, the paper is dried.",
        "Al escribir, pregúntate si necesitas decir quién hace la acción. Si no, usa la pasiva. Comprueba tres cosas: el verbo be concuerda con el sujeto, el participio es el correcto y el tiempo (presente o pasado) calza con el texto. En un cartel, usa el presente: Litter is collected every Friday.",
    ],
    [("passive voice", "voz pasiva: be + participio"), ("was / were + participle", "pasiva en pasado"), ("is / are + participle", "pasiva en presente"), ("found", "encontrado (participio de find)"), ("made", "hecho (participio de make)"), ("broken", "roto (participio de break)"), ("stolen", "robado (participio de steal)"), ("process", "proceso: etapas ordenadas de algo")],
    [
        ("Elegir was o were", "Completa: «The money ___ found on the floor.» Opciones: was / were.", ["Money es singular.", "El hecho es pasado.", "Queda The money was found."], "was"),
        ("Contar pasivas en un proceso", "Texto: «Paper is made from wood. First, wood is cut. Then it is mixed with water. Finally, the paper is dried.» ¿Cuántas oraciones están en pasiva?", ["Busca is + participio: made, cut, mixed, dried.", "Hay una en cada oración.", "Son cuatro."], "4"),
    ],
    [
        ("Escribir «The window was break».", "Después de was se necesita el participio.", "Escribe The window was broken."),
        ("Usar were con un sujeto singular: «The wallet were found».", "Wallet es singular y pide was.", "Escribe The wallet was found."),
    ],
    [
        ("Completa: «The window ___ broken yesterday.» A) was B) is", "A", "Yesterday indica pasado."),
        ("¿Qué oración no dice quién hace la acción? A) Rooms are cleaned daily. B) The staff cleans the rooms daily.", "A", "La pasiva se centra en las salas, no en quién limpia."),
        ("El participio de find es A) found B) finded", "A", "Find es irregular: find, found, found."),
    ],
    [
        ("¿Por qué se usa la pasiva en «My bike was stolen»? A) No se sabe quién lo hizo B) Importa mucho quién lo hizo", "A", "La pasiva sirve cuando quien actúa es desconocido."),
        ("«Plastic is produced from oil.» ¿Está en presente o en pasado?", "Presente", "Is indica presente."),
        ("¿Cuál es el participio de make?", "made", "Make es irregular: make, made, made."),
    ],
    [
        ("Pasa a pasiva sin decir quién actúa. Empieza con «The rooms»: «People clean the rooms daily.»", "The rooms are cleaned daily.", "Se usa are con rooms y el participio cleaned."),
        ("Completa: «Today, plastic bottles ___ collected at school every Friday.» Opciones: are / were.", "are", "Es un hecho habitual del presente y bottles es plural."),
        ("Escribe en pasiva y pasado, sin decir quién: «Someone broke the window.» Empieza con «The window».", "The window was broken.", "Se usa was y el participio irregular broken."),
    ],
    [
        ("¿Qué oración usa bien la pasiva? A) The wallet was found in the yard. B) The wallet was find in the yard.", "A", "Después de was va el participio found."),
        ("Aviso de objeto perdido: «My pencil case ___ yesterday.» ¿Qué completa bien? A) was taken B) took", "A", "No se sabe quién lo tomó, por lo que se usa la pasiva."),
    ],
    [
        ("Ordena las etapas del reciclaje de botellas y escribe las letras en orden. a) The bottles are washed. b) The bottles are collected. c) New bottles are made. d) The plastic is melted.", "b, a, d, c", "Primero se recolectan, luego se lavan, se funde el plástico y al final se fabrican botellas nuevas."),
        ("Corrige el error: «The rooms is cleaned daily.»", "The rooms are cleaned daily.", "Rooms es plural y pide are."),
    ],
    [("Nadie sabe quién pintó un mural en la pared del colegio anoche. ¿Qué oración lo informa mejor? A) The wall was painted last night. B) Someone painted the wall last night, nobody knows who.", "A", "La pasiva evita decir quién actuó cuando no se sabe.")],
    [
        ("¿Con qué verbo se forma la pasiva?", "be", "Be + participio."),
        ("¿Qué auxiliar va con rooms en presente?", "are", "Rooms es plural."),
        ("¿Cuál es el participio de break?", "broken", "Break es irregular."),
    ],
    task("Lee este encargo: escribe en una hoja un cartel de cuatro oraciones que describa un proceso del colegio, por ejemplo cómo se recicla el papel o cómo se cuida el patio. Usa la pasiva con is o are en tres oraciones y was o were en una. Datos de ejemplo: el papel se recolecta, se pesa, se guarda y se entrega a una empresa de reciclaje.", "Paper is collected in each classroom. Then it is weighed on Fridays. The paper is kept in a big box. Last month, the boxes were taken to a recycling company.", ["usa is o are + participio en tres oraciones", "usa was o were + participio en una", "los participios son correctos y el proceso está en orden"], ["hoja con el cartel y las pasivas subrayadas"], ["usar un participio equivocado", "mezclar singular y plural"], "Lee tu cartel a una persona de tu casa y pregunta si se entiende el orden del proceso."),
    "Escribe cinco participios regulares y cinco irregulares y úsalos en oraciones pasivas.",
    "Cambia tres oraciones activas de tu cuaderno a pasiva y explica cuándo conviene no decir quién actúa.",
)
